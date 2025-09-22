#  Retrieval-Augmented Generation Pipeline - – Document & URL QA

Minimal Retrieval-Augmented Generation (RAG) pipeline using FastAPI, LangChain, OpenAI, and ChromaDB.
Now supports document uploads (PDF, TXT, DOCX) and URL ingestion for grounded question answering.


---

##  Features

- 📄 **Multi-format ingestion** (PDF -> chunking -> embedding)
- 🔍 **Vector-based Retrieval** via Chroma
- 🧠 **Grounded LLM Generation** (OpenAI GPT-3.5T)
- 📊 **Source citations for transparency**
- 🐳 **Docker-ready for easy deployment**
- 🖼️  **Streamlit front-end for quick testing**

---

## Test Project

**Clone the Repository**

```bash
git clone https://github.com/yourusername/RagProject.git
cd repoForRagProj
python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
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

