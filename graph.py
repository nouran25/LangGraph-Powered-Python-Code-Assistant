# graph.py

from langgraph.graph import StateGraph, END
from router import classify_intent
from nodes.generate_code import generate_code
from nodes.explain_code import explain_code


# class ChatState(dict):
#     pass

ChatState = dict


# Node to classify intent
def route_node(state: ChatState) -> ChatState:
    # print("DEBUG route_node state:", state)
    if "user_input" not in state:
        raise ValueError("Missing 'user_input' in state")
    classification = classify_intent(state["user_input"])
    state.update(classification)
    return state


# Define conditional routes
def route_condition(state: ChatState):
    return state["task"]


# LangGraph definition
def build_langgraph():
    builder = StateGraph(ChatState)

    builder.add_node("router", route_node)
    builder.add_node("generate_code", generate_code)
    builder.add_node("explain_code", explain_code)
    # Add a fallback node
    builder.add_node(
        "fallback",
        lambda state: {**state, "output": "Sorry, I couldn't understand your request."},
    )

    builder.set_entry_point("router")

    builder.add_conditional_edges(
        "router",
        route_condition,
        {
            "generate_code": "generate_code",
            "explain_code": "explain_code",
            "unknown": "fallback",  # Add this line
        },
    )

    builder.add_edge("generate_code", END)
    builder.add_edge("explain_code", END)
    builder.add_edge("fallback", END)

    return builder.compile()
