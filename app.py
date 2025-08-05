# app.py

from graph import build_langgraph

graph = build_langgraph()


def run_chat():
    while True:
        user_input = input("User: ")
        state = {"user_input": user_input}
        result = graph.invoke(state)
        print("Assistant:", result.get("output", "[No output]"))


if __name__ == "__main__":
    run_chat()
