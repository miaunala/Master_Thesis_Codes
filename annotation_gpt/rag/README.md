# RAG Annotation Pipeline (LangChain)

Refactoring of the original annotation pipeline using **Retrieval-Augmented Generation (RAG)** with LangChain.

## Why RAG?

The original pipeline loads the full codebook as a raw string into every prompt — high token cost and context bloat.  
This version retrieves only the **3 most relevant codebook sections** per message via FAISS semantic search, reducing prompt size and cost while improving signal-to-noise for the LLM.

## Stack

-  ·  · 
-  — local vector store for codebook chunks
-  (text-embedding-3-small) — codebook embedding
-  — PDF chunking
-  chain — RAG classification
-  — flag-driven CLI (, , , )

## Usage

### 1. Install dependencies


### 2. Set up environment


### 3. Build the vectorstore (run once)


### 4. Annotate messages


## Output

CSV with columns: ,  (Hate Speech / Toxic Speech / Neither), 

## Original pipeline

See  for the original full-codebook approach.
