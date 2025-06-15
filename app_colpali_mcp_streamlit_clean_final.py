
import os
import json
import requests
import streamlit as st
from dotenv import load_dotenv

# Load .env
load_dotenv("elastic.env")
MCP_SERVER_URL = os.getenv("MCP_SERVER_URL", "").strip('"')

if not MCP_SERVER_URL:
    st.error("Please set MCP_SERVER_URL in elastic.env")
    st.stop()

# Define REST call function
def call_mcp_retrieve_chunks(query, k, min_score, use_reranking, use_colpali):
    url = f"{MCP_SERVER_URL}/retrieve/chunks"
    payload = {
        "query": query,
        "k": k,
        "min_score": min_score,
        "use_reranking": use_reranking,
        "use_colpali": use_colpali
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        st.error(f"Error {response.status_code}: {response.text}")
        return []
    return response.json()

# Streamlit UI
st.set_page_config(page_title="ColPali MCP Streamlit Demo", page_icon="🔍")
st.title("🔍 ColPali MCP Search Demo")

query = st.text_input("Enter your search query:")
k = st.slider("Number of results (k)", 1, 20, 5)
min_score = st.slider("Minimum score threshold", 0.0, 1.0, 0.0)
use_reranking = st.checkbox("Use Reranking", value=True)
use_colpali = st.checkbox("Use ColPali", value=True)

if st.button("Search"):
    with st.spinner("Searching..."):
        results = call_mcp_retrieve_chunks(query, k, min_score, use_reranking, use_colpali)
        st.write(f"Returned {len(results)} results.")
        for res in results:
            st.markdown(f"**Score:** {res.get('score', 'N/A')}\n**Content:** {res.get('content', '')}")
            st.markdown("---")
