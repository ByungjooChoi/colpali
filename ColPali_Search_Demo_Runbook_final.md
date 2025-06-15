
# 🚀 ColPali Search Demo - Runbook

## 1️⃣ Overview

This demo showcases a ColPali-based Multi-Vector Search pipeline using Elastic MCP Server.

- Implements a 3-step progressive search flow:
    - 1️⃣ ColPali Search (Multi-Vector Search using rank_vectors)
    - 2️⃣ Average Vector + Token Pooling + Reranking
    - 3️⃣ MCP-based REST API Search with Streamlit interface
- Supports multi-lingual queries and flexible reranking.

## 2️⃣ Demo Flow Steps

### Step 1️⃣ ColPali Search

- Run: 01_colpali_search_clean.ipynb
- Uploads RVL-CDIP dataset sample documents with rank_vectors.
- Demonstrates Multi-Vector Search using ColPali embedding.

### Step 2️⃣ Avg Vector + Token Pooling + Reranking

- Run: 02_colpali_avg_tokenpool_rerank_clean.ipynb
- Demonstrates Average Vector, Token Pooling and Hybrid Reranking.
- Optimizes search efficiency with reduced memory footprint.

### Step 3️⃣ MCP REST API Search

- Run: 03_colpali_mcp_streamlit_clean.ipynb or app_colpali_mcp_streamlit_clean.py (Streamlit App)
- Demonstrates full Search UI flow:
    - Query → MCP REST API `/retrieve/chunks` → Elastic MCP Server → Results
    - Supports toggling Reranking and ColPali options.

## 3️⃣ Notes

- All search calls use Elastic MCP Server.
- MCP abstraction allows easy integration with RAG pipelines.
- Streamlit UI enables interactive tuning and demonstration.

## 4️⃣ Summary

The ColPali Search Demo provides a flexible and efficient Multi-Vector Search implementation using Elastic MCP Server with an interactive demo interface.
