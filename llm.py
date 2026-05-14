import json
from openai import OpenAI
from prompts import SYSTEM_PROMPT
from retrieval import search_documents

client = OpenAI()

conversation_history = []

def analyze_data_question(user_input, dataset_summary):
    retrieved_docs = search_documents(user_input, top_k=3)

    context = "\n".join([f"- {doc}" for doc in retrieved_docs])
    history_text = json.dumps(conversation_history[-3:], indent=2)

    user_prompt = f"""
Dataset Summary:
{json.dumps(dataset_summary, indent=2)}

Previous Conversation:
{history_text}

Retrieved Context:
{context}

Current Question:
{user_input}

Instructions:
- Use the dataset, retrieved context, and recent conversation when relevant
- If the current question refers to something earlier, use Previous Conversation
- Do not invent facts
- Return ONLY valid JSON
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )

    response_text = response.choices[0].message.content.strip()

    try:
        result = json.loads(response_text)
        result["retrieved_context"] = retrieved_docs

        conversation_history.append({
            "user": user_input,
            "assistant": {
                "signals": result.get("signals"),
                "risk_level": result.get("risk_level"),
                "explanation": result.get("explanation")
            }
        })

        return result

    except json.JSONDecodeError:
        result = {
            "signals": "Parsing error",
            "risk_level": "Unknown",
            "explanation": f"Invalid JSON returned: {response_text}",
            "retrieved_context": retrieved_docs
        }

        conversation_history.append({
            "user": user_input,
            "assistant": result
        })

        return result

def generate_trend_insight(df):

    revenue_trend = df.groupby("date")["revenue"].sum().tolist()

    prompt = f"""
You are a senior data analyst.

Analyze this revenue trend:

{revenue_trend}

Identify:
- overall trend
- anomalies
- potential business concerns

Provide concise business insights.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

def explain_anomalies(anomalies):

    if len(anomalies) == 0:
        return "No major anomalies detected."

    prompt = f"""
You are a senior data analyst.

These revenue anomalies were detected:

{anomalies.to_dict()}

Explain:
- possible causes
- business risks
- what analysts should investigate next

Provide concise business insights.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content