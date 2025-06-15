
# ColPali Search Demo - README

## Overview

This repository contains the ColPali Search Demo using Elastic MCP Server.

- Implements Multi-Vector Search using ColPali embeddings.
- Progressive 3-step demo:
    - ColPali Search (rank_vectors)
    - Avg Vector + Token Pooling + Rerank
    - MCP REST API Search with Streamlit UI
- Supports multi-lingual queries and flexible reranking.

## Setup Instructions

### 1️⃣ Clone / Prepare Folder

Place all provided files into ColPali_MCP_Demo folder.

### 2️⃣ Setup Virtual Environment (optional)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure .env

Copy template:

```bash
cp elastic_env_template_03_colpali_mcp_streamlit.env elastic.env
```

Edit `elastic.env` and set:

```env
MCP_SERVER_URL="http://localhost:8000"
```

### 5️⃣ Run Notebooks

```bash
jupyter lab
```

Run:
- 01_colpali_search_clean.ipynb
- 02_colpali_avg_tokenpool_rerank_clean.ipynb
- 03_colpali_mcp_streamlit_clean.ipynb

### 6️⃣ Run Streamlit App

```bash
streamlit run app_colpali_mcp_streamlit_clean.py
```

### 7️⃣ Presentation

Use the provided Runbook to guide your presentation flow.

## Conclusion

This demo provides a complete ColPali-based Search pipeline with Elastic MCP Server and Streamlit UI, suitable for demonstrating multi-vector search, hybrid reranking, and MCP REST API interaction.
