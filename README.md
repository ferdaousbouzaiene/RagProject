# Minimal Retrieval-Augmented Generation Pipeline

Lightweight and production-ready RAG pipeline built with FastAPI, LangChain, OpenAI, and ChromaDB. It exposes a single endpoint that uses vector similarity to retrieve document context about Python, Golang and Julia and generate grounded answers for Questions about these programming languages using an LLM (GPT3.5T).


---

##  Features

- 📄 **Document Ingestion** (PDF -> chunking -> embedding)
- 🔍 **Vector-based Retrieval** via Chroma
- 🧠 **Grounded LLM Generation** (OpenAI GPT-3.5T)
- 📊 **Structured Logging & Observability**
- 🛡️ **Secure API Key Handling**
- 🧪 **Basic Integration Tests**
- 🐳 **Fully Dockerized**
- 🖼️  **Streamlit front-end for quick testing**

---

## Test Project

**Clone the Repository**

```bash
git clone https://github.com/ferdaousbouzaiene/repoForRagProj
cd repoForRagProj
```

** Add OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx to .env File **

** Build & Run with Docker Compose **

``` docker-compose up --build ```

API will be available at: http://localhost:8000/docs

Streamlit UI  at: http://localhost:8501


---


Project Structure:

app/

    ├── api.py            # endpoint definition
    ├── query_engine.py   # backend logic 
    ├── interface.py       # streamlit app



tests/                

    ├── test_api.py
    ├── test_retrieval.py

main.py # RAG API application entry point

ingest.py # data handling
documents/                 # Input documents

chroma_db/            # Persisted vector store


Dockerfile

docker-compose.yml

.env.example

README.md

