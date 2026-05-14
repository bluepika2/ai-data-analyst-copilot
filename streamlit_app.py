import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from llm import (
    analyze_data_question,
    generate_trend_insight,
    explain_anomalies,
)
from data_utils import summarize_dataframe
from visualization import plot_revenue_trend, detect_anomalies

load_dotenv()

st.set_page_config(
    page_title="AI Data Analyst Copilot",
    layout="wide"
)

st.title("📊 AI Data Analyst Copilot")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    dataset_summary = summarize_dataframe(df)

    st.subheader("Dataset Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", dataset_summary["num_rows"])

    with col2:
        st.metric("Columns", dataset_summary["num_columns"])

    with col3:
        st.metric("Numeric Columns", len(dataset_summary["numeric_summary"]))

    with st.expander("Column Names"):
        st.write(dataset_summary["columns"])

    st.divider()

    st.subheader("Revenue Trend")

    if "date" in df.columns and "revenue" in df.columns:
        fig = plot_revenue_trend(df)
        st.pyplot(fig)

        st.subheader("AI Trend Insight")

        with st.spinner("Generating trend insight..."):
            trend_insight = generate_trend_insight(df)

        st.write(trend_insight)

        st.divider()

        st.subheader("Detected Anomalies")

        anomalies = detect_anomalies(df)

        if len(anomalies) > 0:
            st.write(anomalies)

            st.subheader("AI Anomaly Explanation")

            with st.spinner("Explaining anomalies..."):
                anomaly_explanation = explain_anomalies(anomalies)

            st.write(anomaly_explanation)

        else:
            st.write("No significant anomalies detected.")

    else:
        st.warning("Revenue trend requires `date` and `revenue` columns.")

    st.divider()

    st.subheader("Ask Questions About Your Dataset")

    user_input = st.text_input("Ask a question:")

    if user_input:
        with st.spinner("Analyzing your question..."):
            result = analyze_data_question(user_input, dataset_summary)

        st.subheader("AI Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Signals**")
            st.write(result.get("signals"))

        with col2:
            st.markdown("**Risk Level**")
            st.write(result.get("risk_level"))

        st.markdown("**Explanation**")
        st.write(result.get("explanation"))

        with st.expander("Retrieved Context"):
            for doc in result.get("retrieved_context", []):
                st.write(f"- {doc}")

else:
    st.info("Upload a CSV file to begin.")