import json

with open("rag_results.json", "r") as f:
    results = json.load(f)

for r in results[:3]:  # Show first 3
    print("Prompt:", r["query"])
    print("Generated:", r["retrieved_prompts"])
    print("---")
