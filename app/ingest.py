'''
load pdf
split into chunks
generate embeddings
store in vector db
'''


# app/ingest.py
import os
from typing import List, Optional
from langchain.document_loaders import (
    PyPDFLoader,
    UnstructuredFileLoader,
    UnstructuredURLLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# Persist DB in chroma_db/
CHROMA_DIR = os.getenv("CHROMA_DIR", "chroma_db")

def load_documents(files: Optional[List[str]] = None, urls: Optional[List[str]] = None):
    """Load documents from local files and/or URLs."""
    docs = []
    if files:
        for f in files:
            if f.endswith(".pdf"):
                docs.extend(PyPDFLoader(f).load())
            else:
                docs.extend(UnstructuredFileLoader(f).load())
    if urls:
        docs.extend(UnstructuredURLLoader(urls).load())
    return docs

def chunk_and_store(docs, collection_name="default"):
    """Chunk, embed, and persist documents into Chroma."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    db = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )

    db.add_documents(chunks)
    # db.persist()
    return len(chunks)
