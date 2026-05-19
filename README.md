# AI Data Analyst Copilot

An AI-powered analytics assistant that combines retrieval-augmented generation (RAG), semantic retrieval, structured reasoning, visualization, and anomaly detection to generate grounded insights from uploaded datasets.

## Features

- CSV upload and summarization
- Semantic retrieval using embeddings
- Conversation memory
- Structured JSON outputs
- Revenue trend visualization
- AI-generated analytical insights
- Anomaly detection and explanation
- Streamlit frontend

## Tech Stack

- Python
- OpenAI API
- Streamlit
- Pandas
- NumPy
- Matplotlib

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

## Screenshots

### Trend Visualization

![Trend Chart](screenshots/trend_chart.png)

### AI Insight Generation

![AI Insight](screenshots/ai_insight.png)

## Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```