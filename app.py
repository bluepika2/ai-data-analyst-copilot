from dotenv import load_dotenv
from llm import analyze_data_question

load_dotenv()

def chat():
    print("💬 AI Data Analyst Copilot with RAG (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        result = analyze_data_question(user_input)

        print("\nAssistant:")
        print("Signals:", result.get("signals"))
        print("Risk Level:", result.get("risk_level"))
        print("Explanation:", result.get("explanation"))

        print("\nRetrieved Context (Top Matches):")
        for i, doc in enumerate(result.get("retrieved_context", []), 1):
            print(f"{i}. {doc}")

        print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    chat()