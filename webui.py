# webui.py

import gradio as gr
import json
from datetime import datetime
from graph import build_langgraph

graph = build_langgraph()


# Chat handler function
def chatbot(message, chat_history):
    state = {"user_input": message}
    try:
        result = graph.invoke(state)
        assistant_response = result.get("output", "Sorry, I couldn't understand that.")
    except Exception as e:
        assistant_response = f"⚠️ Error: {str(e)}"

    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": assistant_response})
    return "", chat_history


# Reset button callback
def reset_chat():
    return "", []


# Save chat history to a JSON file
def save_chat(chat_history):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"chat_session_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(chat_history, f, indent=2)
    return filename


# Load chat history from a file
def load_chat(file):
    if file is None:
        return []
    with open(file.name, "r") as f:
        history = json.load(f)
    return history


# Launch the app
def launch_app():
    with gr.Blocks(title="LangGraph Python Assistant") as demo:
        gr.Markdown("# 🤖 LangGraph-Powered Python Assistant")
        gr.Markdown("Ask me to **generate or explain** Python code!")

        chatbot_ui = gr.Chatbot(label="Chat Session", type="messages")
        message_input = gr.Textbox(
            placeholder="Type your Python-related question here...", show_label=False
        )
        send_button = gr.Button("Send")

        # Buttons for extra features
        with gr.Row():
            clear_button = gr.Button("🔄 Clear Chat")
            save_button = gr.Button("💾 Save Chat")
            load_file = gr.File(
                label="📂 Load Chat Session (.json)", file_types=[".json"]
            )

        state = gr.State([])

        # Events
        send_button.click(chatbot, [message_input, state], [message_input, chatbot_ui])
        message_input.submit(
            chatbot, [message_input, state], [message_input, chatbot_ui]
        )

        clear_button.click(reset_chat, None, [message_input, chatbot_ui], queue=False)

        save_button.click(save_chat, [state], None)

        load_file.change(load_chat, [load_file], [state, chatbot_ui])

    demo.launch(share=True)


if __name__ == "__main__":
    launch_app()
