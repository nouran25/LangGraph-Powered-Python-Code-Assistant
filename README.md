# LangGraph-Powered Python Code Assistant 🤖

[![GitHub](https://img.shields.io/badge/LangGraph-Agent%20Workflow-blue)](https://langchain.com/langgraph)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A stateful Python coding assistant that generates, explains, and evaluates code using LangGraph orchestration, RAG, and Ollama LLMs. Supports both CLI and Gradio web interface.

![Demo GIF](assets/demo.gif) <!-- Replace with your actual demo GIF -->

## Key Features ✨

- **Intent-Aware Routing**: LLM classifies requests as `generate_code` or `explain_code`
- **Multi-Interface Support**: 
  - CLI chat (`app.py`)
  - Gradio web UI (`webui.py`)
- **RAG Pipeline**: Retrieves similar code examples from MBPP dataset
- **Test-Driven Evaluation**: Validates generated code against test cases
- **Ollama Integration**: Runs locally with Mistral/Llama3 models

## Architecture 🏗️

```mermaid
graph TD
    A[User Input] --> B(Intent Classifier)
    B -->|generate_code| C[Code Generator]
    B -->|explain_code| D[Code Explainer]
    C --> E[Output]
    D --> E
    F[MBPP Dataset] -->|RAG| C
