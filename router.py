# router.py
import json
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="mistral", temperature=0.2)

intent_prompt = PromptTemplate.from_template("""
You are a language model acting as an **intent classifier** for a Python programming assistant. 

Your task is to analyze the user's message and classify it into one of the following intents:

1. **generate_code** → The user is requesting you to write, implement, or create Python code (e.g., "Write a function to reverse a string").
2. **explain_code** → The user is asking you to interpret, describe, or explain the purpose or behavior of a code snippet (e.g., "What does this function do?").

Only respond with a JSON object in the following format:

{{
  "task": "<generate_code or explain_code>",
  "user_input": "<repeat the user's original message exactly>"
}}

Your response should contain **only** the JSON object and no additional text.

User message: {user_input}
""")


chain = intent_prompt | llm


def classify_intent(user_input: str) -> dict:
    output = chain.invoke({"user_input": user_input})
    # print("DEBUG classify_intent output:", output.content)  # Add this line
    try:
        result = json.loads(output.content)
    except Exception:
        result = {"task": "unknown", "user_input": user_input}
    return result
