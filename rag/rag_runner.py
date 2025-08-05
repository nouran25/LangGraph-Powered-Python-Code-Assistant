# rag/rag_runner.py

import json
from retrieve import retrieve_similar_examples
from evaluate import run_tests
from langchain_community.chat_models import ChatOllama  # or ChatOpenAI

llm = ChatOllama(model="llama3:8b", temperature=0.2)


def rag_prompt(query, retrieved_examples):
    context = "\n\n".join(
        f"# Example: {ex['prompt']}\n{ex['code']}" for ex in retrieved_examples
    )
    return f"""You're a Python code assistant. Use the following examples to solve the user's request.

{context}

# Task: {query}
Write Python code below:
"""


def evaluate_mbpp(
    file_path="mbpp_samples.json",
):
    with open(file_path, "r") as f:
        mbpp_data = json.load(f)

    results = []

    for ex in mbpp_data:
        query = ex["prompt"]
        test_list = ex["test_list"]

        retrieved, scores = retrieve_similar_examples(query)
        prompt = rag_prompt(query, retrieved)

        print(f"\n🔍 Prompt: {query}")
        print(f"📚 Retrieved: {[r['prompt'] for r in retrieved]}")

        response = llm.invoke(prompt)
        code = response.content.strip()

        passed = run_tests(code, test_list)

        results.append(
            {
                "task_id": ex["task_id"],
                "query": query,
                "code": code,
                "retrieved_prompts": [r["prompt"] for r in retrieved],
                "pass": passed,
            }
        )

    with open("rag_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n✅ Evaluation Complete — Results saved to data/rag_results.json")


if __name__ == "__main__":
    evaluate_mbpp()
