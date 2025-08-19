# LangGraph-Powered Python Code Assistant 🤖

[![GitHub](https://img.shields.io/badge/LangGraph-Agent%20Workflow-blue)](https://langchain.com/langgraph)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A stateful Python coding assistant that generates, explains, and evaluates code using LangGraph orchestration, RAG, and Ollama LLMs. Supports both CLI and Gradio web interface.

---
## 🗂️ Table of Contents

- [Key Features ✨](#-key-features)
- [Architecture 🏗️](#-architecture)
- [Installation ⚙️](#-installation)
- [Usage 🚀](#-usage)
- [RAG Evaluation 📊](#-rag-evaluation)
- [Project Structure 📂](#-project-structure)
- [Key Implementation Details 🔍](#-key-implementation-details)
- [Resources 📚](#-resources)
---
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
  ```
## Installation ⚙️

Clone the repo and install dependencies:

```bash
git clone https://github.com/nouran25/LangGraph-Powered-Python-Code-Assistant.git
cd LangGraph-Powered-Python-Code-Assistant
pip install -r requirements.txt
```
### Ollama Setup
  ```bash
  ollama pull mistral  # Default model
  ollama pull llama3   # Alternative for RAG
```
## Usage 🚀
### CLI Version
```bash
python app.py
```
Example:

```text
User: Write a function to reverse a string
Assistant: Here's the Python code:
```python
def reverse_string(s):
    return s[::-1]
```
![Demo GIF](assets/output.png) <!-- Replace with your actual demo GIF -->

### Web Interface
```bash
python webui.py
```
Access at http://localhost:7860

![Demo GIF](assets/demo.gif) <!-- Replace with your actual demo GIF -->

## RAG Evaluation 📊
To test retrieval-augmented generation on MBPP samples:

```bash
python rag/rag_runner.py
```
Outputs evaluation results to `rag_results.json`

## Project Structure 📂
```text
.
├── app.py                # CLI entry point
├── webui.py              # Gradio interface
├── graph.py              # LangGraph state machine
├── router.py             # LLM intent classifier
├── nodes/
│   ├── generate_code.py  # Code generation agent
│   └── explain_code.py   # Code explanation agent
├── rag/                  # Retrieval-Augmented Generation
│   ├── embed_examples.py # Dataset vectorization
│   ├── retrieve.py       # Similarity search
│   └── rag_runner.py     # Evaluation pipeline
    └── mbpp_samples.json     # Benchmark dataset
```
## Key Implementation Details 🔍
**1. Smart Intent Classification**
Uses Ollama LLM to classify user input into JSON:

```python
# router.py
def classify_intent(user_input):
    output = llm.invoke(intent_prompt)
    return json.loads(output.content)  # {"task": "...", "user_input": "..."}
```
**2. LangGraph State Machine**
```python
# graph.py
builder = StateGraph(ChatState)
builder.add_node("router", route_node)
builder.add_conditional_edges(
    "router",
    route_condition,
    {"generate_code": "generate_code", "explain_code": "explain_code"}
)
```
**3. RAG Pipeline**
```python
# retrieve.py
def retrieve_similar_examples(query):
    query_vec = model.encode([query])
    scores = cosine_similarity(query_vec, embeddings)[0]
    return [examples[i] for i in top_indices]
```
## Resources 📚

### Official Documentation
- [LangGraph Documentation](https://langchain.com/langgraph) - Learn about stateful LLM workflows
- [Ollama Models](https://ollama.ai/library) - Browse available LLM models

### Research Papers
- [MBPP Dataset Paper](https://arxiv.org/abs/2108.07732) - "Measuring Coding Challenge Competence With APPS"

### Tutorials & Guides
- [LangGraph YouTube Tutorial](https://www.youtube.com/watch?v=jGg_1h0qzaM) (2.5hr in-depth guide)
- [LangChain vs LangGraph](https://www.youtube.com/watch?v=qAF1NjEVHhY) - Comparison video
- [State Machines in Production](https://dev.to/jamesli/langgraph-state-machines-managing-complex-agent-task-flows-in-production-36f4) - Blog post

### Datasets
- [MBPP Dataset](https://github.com/google-research/google-research/tree/master/mbpp) - 974 programming problems with test cases

### Community
- [LangChain Discord](https://discord.gg/langchain) - Get live support
- [Ollama GitHub](https://github.com/jmorganca/ollama) - Report issues or contribute

