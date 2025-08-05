# nodes/generate_code.py

from langchain_ollama import ChatOllama

# Initialize the LLM
llm = ChatOllama(model="mistral", temperature=0.2)


def generate_code(state: dict) -> dict:
    prompt = f"Write Python code for this request:\n\n{state['user_input']}"
    response = llm.invoke(prompt)
    state["output"] = response.content
    return state
