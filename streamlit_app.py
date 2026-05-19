import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from llm import (
    analyze_data_question,
    generate_trend_insight,
    explain_anomalies,
    generate_executive_insights,
)
from data_utils import summarize_dataframe
from visualization import plot_revenue_trend, detect_anomalies
from analytics import generate_analytics_summary

load_dotenv()

st.set_page_config(
    page_title="AI Data Analyst Copilot",
    layout="wide"
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("📊 AI Data Analyst Copilot")
st.caption("Upload a CSV file and generate AI-powered analytical insights.")

st.sidebar.title("⚙️ Settings")

show_raw_data = st.sidebar.checkbox("Show raw dataset preview", value=False)
show_context = st.sidebar.checkbox("Show retrieved context", value=False)
show_json_summary = st.sidebar.checkbox("Show raw analytics JSON", value=False)

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    dataset_summary = summarize_dataframe(df)

    if show_raw_data:
        st.subheader("Dataset Preview")
        st.dataframe(df.head(20))

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

    st.subheader("Automated Analytics Summary")

    analytics_summary = generate_analytics_summary(df)
    kpi = analytics_summary.get("kpi_summary", {})

    col1, col2, col3 = st.columns(3)

    with col1:
        total_revenue = kpi.get("total_revenue", 0)
        st.metric("Total Revenue", f"${total_revenue:,.0f}")

    with col2:
        average_revenue = kpi.get("average_revenue", 0)
        st.metric("Average Revenue", f"${average_revenue:,.0f}")

    with col3:
        revenue_change_pct = kpi.get("revenue_change_pct", 0)
        st.metric("Revenue Change %", f"{revenue_change_pct}%")

    if show_json_summary:
        with st.expander("Raw Analytics JSON"):
            st.json(analytics_summary)

    st.subheader("AI Executive Insights")

    with st.spinner("Generating executive insights..."):
        executive_insights = generate_executive_insights(analytics_summary)

    st.info(executive_insights)

    report_text = f"""
AI Data Analyst Copilot Report

Executive Insights:
{executive_insights}

Analytics Summary:
{analytics_summary}
"""

    st.download_button(
        label="Download Insights Report",
        data=report_text,
        file_name="ai_insights_report.txt",
        mime="text/plain"
    )

    st.divider()

    st.subheader("Revenue Trend")

    if "date" in df.columns and "revenue" in df.columns:
        fig = plot_revenue_trend(df)
        st.pyplot(fig)

        st.subheader("AI Trend Insight")

        with st.spinner("Generating trend insight..."):
            trend_insight = generate_trend_insight(df)

        st.info(trend_insight)

        st.divider()

        st.subheader("Detected Anomalies")

        anomalies = detect_anomalies(df)

        if len(anomalies) > 0:
            st.write(anomalies)

            st.subheader("AI Anomaly Explanation")

            with st.spinner("Explaining anomalies..."):
                anomaly_explanation = explain_anomalies(anomalies)

            st.warning(anomaly_explanation)

        else:
            st.success("No significant anomalies detected.")

    else:
        st.warning("Revenue trend requires `date` and `revenue` columns.")

    st.divider()

    st.subheader("Ask Questions About Your Dataset")

    user_input = st.text_input(
        "Ask a question:",
        placeholder="Example: What is driving the revenue decline?"
    )

    if user_input:
        with st.spinner("Analyzing your question..."):
            result = analyze_data_question(user_input, dataset_summary)

        st.session_state.chat_history.append({
            "question": user_input,
            "answer": result
        })

    if st.session_state.chat_history:
        st.subheader("Conversation History")

        for idx, item in enumerate(reversed(st.session_state.chat_history), 1):
            with st.container():
                st.markdown(f"### Question {idx}")
                st.write(item["question"])

                answer = item["answer"]

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("**Signals**")
                    st.write(answer.get("signals"))

                with col2:
                    st.markdown("**Risk Level**")
                    st.write(answer.get("risk_level"))

                st.markdown("**Explanation**")
                st.write(answer.get("explanation"))

                if show_context:
                    with st.expander("Retrieved Context"):
                        for doc in answer.get("retrieved_context", []):
                            st.write(f"- {doc}")

                st.divider()

else:
    st.info("Upload a CSV file to begin.")