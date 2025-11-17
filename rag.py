from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load embeddings model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load rules from a text file
def load_rules(path="rules.txt"):
    with open(path, "r", encoding="utf-8") as f:
        rules = [line.strip() for line in f if line.strip()]
    
    embeddings = model.encode(rules)
    return rules, embeddings

# Retrieve the best matching rule
def retrieve(query, rules, embeddings):
    q_emb = model.encode([query])
    scores = cosine_similarity(q_emb, embeddings)[0]
    best_idx = int(np.argmax(scores))
    return rules[best_idx], scores[best_idx]
