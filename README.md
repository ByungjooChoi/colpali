
# ColPali MCP Search Demo - README

## Overview

This repository contains the ColPali MCP Search Demo prepared for the Elastic Search Specialist interview.

- The demo implements Morphik-core MCP structure using Elastic MCP Server.
- It supports Multi-Vector Search with ColPali, Reranking, and standard Vector Search.
- The demo provides both Jupyter Notebooks and a standalone Streamlit app.

## Folder Structure

```
ColPali_MCP_Demo/
├── 01_colpali_search_clean.ipynb
├── 02_colpali_avg_tokenpool_rerank_clean.ipynb
├── 03_colpali_mcp_streamlit_clean.ipynb
├── app_colpali_mcp_streamlit_clean.py
├── requirements_03_colpali_mcp_streamlit_clean.txt
├── elastic_env_template_03_colpali_mcp_streamlit.env
├── ColPali_MCP_Search_Demo_Runbook.md
└── README.md
```

## Setup Instructions

### 1️⃣ Clone or Prepare Folder

Prepare the ColPali_MCP_Demo folder and place all provided files.

### 2️⃣ Setup Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements_03_colpali_mcp_streamlit_clean.txt
```

### 4️⃣ Configure .env

Copy the template:

```bash
cp elastic_env_template_03_colpali_mcp_streamlit.env elastic.env
```

Edit `elastic.env` and set:

```env
MCP_SERVER_URL="http://localhost:8000"  # Adjust according to your MCP server instance
```

### 5️⃣ Running Notebooks

Use JupyterLab:

```bash
jupyter lab
```

Run:
- `01_colpali_search_clean.ipynb`
- `02_colpali_avg_tokenpool_rerank_clean.ipynb`
- `03_colpali_mcp_streamlit_clean.ipynb`

### 6️⃣ Running Streamlit App

```bash
streamlit run app_colpali_mcp_streamlit_clean.py
```

### 7️⃣ Presentation

Use the `ColPali_MCP_Search_Demo_Runbook.md` to guide your demo presentation.

## Notes

- The MCP Server must be running and accessible via `MCP_SERVER_URL`.
- The Streamlit app uses `/retrieve/chunks` endpoint.
- Use the UI to toggle **Reranking** and **ColPali** options and demonstrate different search configurations.

## Conclusion

This setup demonstrates a full Morphik MCP architecture-based ColPali Search pipeline using Elastic MCP Server, Streamlit, and Jupyter.
