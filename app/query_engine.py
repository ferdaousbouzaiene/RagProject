'''
backend logic -> Core RAG functionality : handles document retrieval and answer generation
'''

# app/query_engine.py
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA

CHROMA_DIR = os.getenv("CHROMA_DIR", "chroma_db")

def get_retriever(collection_name="default"):
    embeddings = OpenAIEmbeddings()
    db = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=CHROMA_DIR,
    )
    return db.as_retriever(search_kwargs={"k": 3})

def query(question: str, collection_name="default"):
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    retriever = get_retriever(collection_name)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa.run(question)
