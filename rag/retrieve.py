# rag/retrieve.py

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_similar_examples(query, top_k=3, npz_path="mbpp_vectors.npz"):
    data = np.load(npz_path, allow_pickle=True)
    embeddings = data["embeddings"]
    examples = data["examples"]

    query_vec = model.encode([query])
    scores = cosine_similarity(query_vec, embeddings)[0]
    top_indices = scores.argsort()[-top_k:][::-1]

    return [examples[i] for i in top_indices], [scores[i] for i in top_indices]
