# nodes/explain_code.py

from langchain_ollama import ChatOllama

llm = ChatOllama(model="mistral", temperature=0.2)


def explain_code(state: dict) -> dict:
    prompt = f"Explain this Python code in simple terms:\n\n{state['user_input']}"
    response = llm.invoke(prompt)
    state["output"] = response.content
    return state
