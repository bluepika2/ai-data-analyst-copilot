# AI Data Analyst Copilot

An AI-powered analytics assistant that combines retrieval-augmented generation (RAG), semantic retrieval, structured reasoning, visualization, anomaly detection, and conversation memory to generate grounded insights from uploaded datasets.

---

## Features

- CSV ingestion and dataset summarization
- KPI analysis and segment comparison
- AI-generated executive insights
- Semantic retrieval using embeddings
- Retrieval-Augmented Generation (RAG)
- Conversation memory
- Revenue trend visualization
- Anomaly detection and explanation
- Interactive Streamlit frontend
- Downloadable AI insights report

---

## Architecture

```mermaid
flowchart TD
    A[User] --> B[Streamlit Frontend]

    B --> C[CSV Upload]
    C --> D[Dataset Summary]

    D --> E[Analytics Engine]
    E --> E1[KPI Analysis]
    E --> E2[Segment Analysis]
    E --> E3[Trend Visualization]
    E --> E4[Anomaly Detection]

    D --> F[RAG Retrieval Layer]
    F --> F1[Embedding Generation]
    F --> F2[Semantic Search]
    F --> F3[Retrieved Context]

    E --> G[LLM Reasoning Layer]
    F3 --> G

    G --> G1[Structured JSON Output]
    G --> G2[Executive Insights]
    G --> G3[Conversation Memory]

    G1 --> H[User-Facing Insights]
    G2 --> H
    G3 --> H
```

---

## Screenshots

### Main Dashboard

![Dashboard](screenshots/dashboard.png)

### Trend Analysis

![Trend Analysis](screenshots/trend_analysis.png)

### Anomaly Detection

![Anomaly Detection](screenshots/anomaly_detection.png)

---

## Tech Stack

- Python
- OpenAI API
- Streamlit
- Pandas
- NumPy
- Matplotlib

---

## Key AI Concepts Implemented

- Retrieval-Augmented Generation (RAG)
- Semantic Search with Embeddings
- Structured JSON Outputs
- Conversation Memory
- AI-Assisted Analytics
- Anomaly Detection
- Executive Insight Generation

---

## Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## Future Improvements

- Vector database integration
- Multi-dataset support
- SQL query integration
- Advanced anomaly detection
- Real-time analytics pipelines
- Role-based analytics workflows

---

## Project Motivation

This project was designed to explore how modern LLM systems can assist analytical workflows beyond simple chatbot interactions by combining retrieval, structured reasoning, business analytics, and conversational interfaces.