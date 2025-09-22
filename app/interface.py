'''
simple interface for testing
'''

# app/interface.py
import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("🧠 RAG Demo: Upload Docs & Ask Questions")

# Upload docs
st.subheader("📄 Upload Documents")
uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)
if uploaded_files and st.button("Ingest Files"):
    files = [("files", (f.name, f.getvalue(), f.type)) for f in uploaded_files]
    res = requests.post(f"{API_URL}/ingest/files", files=files)
    st.json(res.json())

# Add URLs
st.subheader("🔗 Add URLs")
urls = st.text_area("Enter URLs (comma separated)")
if urls and st.button("Ingest URLs"):
    url_list = [u.strip() for u in urls.split(",")]
    res = requests.post(f"{API_URL}/ingest/urls", data={"urls": url_list})
    st.json(res.json())

# Query
st.subheader("❓ Ask a Question")
query = st.text_input("Your question")
if query and st.button("Get Answer"):
    res = requests.post(f"{API_URL}/query", params={"query": query})
    st.write(res.json()["answer"])

