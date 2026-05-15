import pandas as pd
import json
import argparse
from typing import Literal
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

load_dotenv()

PROMPT_TEMPLATE = """You are an expert annotator for hate speech and toxic speech in German social media messages.

Use the following codebook sections to guide your classification decision:
{context}

Message to classify:
{question}

Classify as exactly one of:
- "Hate Speech" (Hassrede): targets a person or group based on identity
- "Toxic Speech" (toxische Rede): hostile/vulgar but not identity-based hate speech
- "Neither" (weder noch): does not qualify as either

Return ONLY valid JSON with no markdown:
{{"label": "Hate Speech" | "Toxic Speech" | "Neither", "reason": "<one sentence>"}}"""


def load_pipeline(index_path: str = "codebook_index", model: str = "gpt-3.5-turbo") -> RetrievalQA:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = FAISS.load_local(
        index_path, embeddings, allow_dangerous_deserialization=True
    )
    llm = ChatOpenAI(model=model, temperature=0)
    prompt = PromptTemplate(
        template=PROMPT_TEMPLATE, input_variables=["context", "question"]
    )
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=False,
    )
    return chain


def annotate(messages: list, chain: RetrievalQA) -> list:
    results = []
    for i, msg in enumerate(messages):
        try:
            raw = chain.invoke({"query": msg})["result"]
            parsed = json.loads(raw)
            results.append({
                "message": msg,
                "label": parsed["label"],
                "reason": parsed.get("reason", ""),
            })
        except Exception as e:
            results.append({"message": msg, "label": "ERROR", "reason": str(e)})
        if (i + 1) % 10 == 0:
            print(f"  Annotated {i + 1}/{len(messages)} messages")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="RAG-based hate/toxic speech annotation"
    )
    parser.add_argument(
        "--input", required=True, help="CSV with messages (column: raw_text)"
    )
    parser.add_argument("--output", default="annotated.csv", help="Output CSV path")
    parser.add_argument("--index", default="codebook_index", help="FAISS index path")
    parser.add_argument(
        "--model",
        default="gpt-3.5-turbo",
        choices=["gpt-3.5-turbo", "gpt-4o"],
        help="OpenAI model to use",
    )
    args = parser.parse_args()

    df = pd.read_csv(args.input, encoding="utf-8")
    messages = df["raw_text"].tolist()
    print(f"Loaded {len(messages)} messages from {args.input}")

    chain = load_pipeline(index_path=args.index, model=args.model)
    results = annotate(messages, chain)

    out_df = pd.DataFrame(results)
    out_df.to_csv(args.output, index=False, encoding="utf-8")
    print(f"Done: {len(results)} messages annotated -> {args.output}")
