# rag/embed_examples.py

from sentence_transformers import SentenceTransformer
import json
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_dataset(
    file_path="mbpp_samples.json",
    save_path="mbpp_vectors.npz",
):
    with open(file_path, "r") as f:
        examples = json.load(f)

    prompts = [ex["prompt"] for ex in examples]
    embeddings = model.encode(prompts, convert_to_numpy=True)

    np.savez(save_path, embeddings=embeddings, prompts=prompts, examples=examples)


if __name__ == "__main__":
    embed_dataset()
