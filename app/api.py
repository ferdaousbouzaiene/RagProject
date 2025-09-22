'''
endpoint definition
'''

# app/api.py
import os
from fastapi import FastAPI, UploadFile, Form
from typing import List, Optional

import app.ingest as ingest
import app.query_engine as query_engine


app = FastAPI(title="RAG API")

@app.post("/ingest/files")
async def ingest_files(files: List[UploadFile]):
    file_paths = []
    for file in files:
        path = f"documents/{file.filename}"
        with open(path, "wb") as f:
            f.write(await file.read())
        file_paths.append(path)

    count = ingest.chunk_and_store(ingest.load_documents(files=file_paths))
    return {"status": "success", "chunks_added": count}

@app.post("/ingest/urls")
async def ingest_urls(urls: List[str] = Form(...)):
    count = ingest.chunk_and_store(ingest.load_documents(urls=urls))
    return {"status": "success", "chunks_added": count}

@app.post("/query")
async def query_api(query: str, collection_name: Optional[str] = "default"):
    answer = query_engine.query(query, collection_name=collection_name)
    return {"answer": answer}
