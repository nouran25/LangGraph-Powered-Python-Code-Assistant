import json
import numpy as np
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load full MBPP data
with open("mbpp_samples.json", "r") as f:
    full_data = json.load(f)

examples = full_data[:10]  # Get first 10 examples (dicts)
texts = [ex["prompt"] for ex in examples]  # For embedding

vectors = embedding_model.encode(texts)

# Save full examples and embeddings
np.savez(
    "mbpp_vectors.npz", embeddings=vectors, examples=np.array(examples, dtype=object)
)
