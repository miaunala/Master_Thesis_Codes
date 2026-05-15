from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import argparse

load_dotenv()


def build_vectorstore(pdf_path: str, save_path: str = "codebook_index") -> None:
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(save_path)
    print(f"Vectorstore saved to {save_path} ({len(chunks)} chunks from {len(documents)} pages)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build FAISS vectorstore from codebook PDF")
    parser.add_argument("--pdf", default="codebook_v1_manualcoding.pdf", help="Path to codebook PDF")
    parser.add_argument("--index", default="codebook_index", help="Output path for FAISS index")
    args = parser.parse_args()
    build_vectorstore(args.pdf, args.index)
