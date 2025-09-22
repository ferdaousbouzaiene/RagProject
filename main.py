'''
RAG API application entry point
'''

import logging
from fastapi import FastAPI
from loguru import logger

from app.api import router

# configure logging with rotation -> prevent large log files

logger.add("logs/rag_pipeline.log", rotation="1 MB", level="DEBUG")
logger.add("logs/log.json", serialize=True)

app = FastAPI(
    title="RAG API",
    description='A lightweight RAG system for document retrieval and question answering about programming languages')

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
