import os
import random
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------------
# 1. Ensure Reproducibility
# ---------------------------------------------------------
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

print("🚀 Starting embedding pipeline execution...")

# ---------------------------------------------------------
# 2. Generate 1,000 Sample Document Chunks
# (In production, replace this with your loaded dataset)
# ---------------------------------------------------------
corpus = [
    f"This is document chunk number {i} talking about AI, embeddings, and software engineering."
    for i in range(1000)
]

# ---------------------------------------------------------
# STEP 1: Embed 1,000 chunks using an open model (BAAI/bge-base-en-v1.5)
# ---------------------------------------------------------
MODEL_NAME = "BAAI/bge-base-en-v1.5"
print(f"\n[Step 1] Loading model: {MODEL_NAME}...")
model = SentenceTransformer(MODEL_NAME)

# BGE v1.5 does not require prefixes for document passages, only for queries
passage_prefix = ""
prefixed_corpus = [f"{passage_prefix}{text}" for text in corpus]

print("Generating embeddings for 1,000 chunks...")
corpus_embeddings = model.encode(prefixed_corpus, normalize_embeddings=True, show_progress_bar=True)
print(f"Embedding Matrix Shape: {corpus_embeddings.shape}")  # Expected: (1000, 768)

# ---------------------------------------------------------
# STEP 2: Compute Cosine Similarity for 20 Hand-picked Pairs
# ---------------------------------------------------------
print("\n[Step 2] Evaluating Cosine Similarity on 20 Hand-picked Pairs...")

# 10 Semantically Similar Pairs and 10 Dissimilar Pairs
test_pairs = [
    # Similar Pairs
    ("How to reset password?", "Steps to recover forgotten password.", True),
    ("Python is great for AI", "Machine learning with Python is popular", True),
    ("Deep learning models require GPUs", "Neural networks need powerful graphics cards", True),
    ("What is the capital of France?", "Paris is France's capital city", True),
    ("How to boil an egg?", "Instructions for cooking boiled eggs", True),
    ("Cloud computing with AWS", "Deploying applications on Amazon Web Services", True),
    ("Data structures and algorithms", "Arrays, Linked lists and Sorting techniques", True),
    ("Benefits of daily exercise", "Why physical workout is good for health", True),
    ("Database management systems", "SQL and relational database structures", True),
    ("How do embeddings work?", "Vector representations of text in NLP", True),
    
    # Dissimilar Pairs
    ("How to reset password?", "The solar system has eight planets", False),
    ("Python is great for AI", "I love eating chocolate ice cream", False),
    ("Deep learning models require GPUs", "Shakespeare wrote Hamlet in 1600", False),
    ("What is the capital of France?", "How to repair a flat bicycle tire", False),
    ("How to boil an egg?", "Quantum mechanics and wave-particle duality", False),
    ("Cloud computing with AWS", "History of the Roman Empire", False),
    ("Data structures and algorithms", "Best recipes for Italian pasta", False),
    ("Benefits of daily exercise", "Cybersecurity threats in banking systems", False),
    ("Database management systems", "How to plant tomatoes in your garden", False),
    ("How do embeddings work?", "The stock market crashed yesterday", False)
]

for idx, (text1, text2, is_similar) in enumerate(test_pairs, 1):
    # Generate embeddings for test pairs
    v1 = model.encode(text1, normalize_embeddings=True)
    v2 = model.encode(text2, normalize_embeddings=True)
    
    # Compute Cosine Similarity (Dot product on normalized vectors)
    score = np.dot(v1, v2)
    expected = "Similar" if is_similar else "Dissimilar"
    print(f"Pair {idx:02d} [{expected:<10}] | Score: {score:.4f} | '{text1[:25]}...' vs '{text2[:25]}...'")

# ---------------------------------------------------------
# STEP 3: Test Query Prefixes ON/OFF & Measure Recall@10
# ---------------------------------------------------------
print("\n[Step 3] Measuring Recall@10 with and without Query Prefixes...")

# Define sample queries
queries = [
    "document chunk number 10",
    "document chunk number 250",
    "document chunk number 500",
    "document chunk number 750",
    "document chunk number 999"
]
# Corresponding ground truth indices in the corpus
ground_truth_indices = [10, 250, 500, 750, 999]

# Official Instruction Prefix for BGE v1.5
BGE_PREFIX = "Represent this sentence for searching relevant passages: "

def calculate_recall_at_k(q_embeddings, doc_embeddings, ground_truths, k=10):
    hits = 0
    sim_matrix = cosine_similarity(q_embeddings, doc_embeddings)  # Shape: (num_queries, 1000)
    
    for idx, true_idx in enumerate(ground_truths):
        # Get indices of top K highest similarity scores
        top_k_indices = np.argsort(sim_matrix[idx])[::-1][:k]
        if true_idx in top_k_indices:
            hits += 1
            
    return hits / len(ground_truths)

# 1. Query Embeddings WITHOUT Prefix
q_emb_no_prefix = model.encode(queries, normalize_embeddings=True)
recall_no_prefix = calculate_recall_at_k(q_emb_no_prefix, corpus_embeddings, ground_truth_indices, k=10)

# 2. Query Embeddings WITH Prefix
prefixed_queries = [f"{BGE_PREFIX}{q}" for q in queries]
q_emb_with_prefix = model.encode(prefixed_queries, normalize_embeddings=True)
recall_with_prefix = calculate_recall_at_k(q_emb_with_prefix, corpus_embeddings, ground_truth_indices, k=10)

print(f"👉 Recall@10 (WITHOUT Prefix) : {recall_no_prefix * 100:.2f}%")
print(f"👉 Recall@10 (WITH Prefix)    : {recall_with_prefix * 100:.2f}%")

# ---------------------------------------------------------
# STEP 4: Truncate Embeddings to 256 Dims & Measure Recall Loss
# ---------------------------------------------------------
print("\n[Step 4] Truncating Embeddings to 256 Dimensions...")

# Truncate corpus embeddings to first 256 dimensions and re-normalize
corpus_emb_256 = corpus_embeddings[:, :256]
corpus_emb_256 = corpus_emb_256 / np.linalg.norm(corpus_emb_256, axis=1, keepdims=True)

# Truncate query embeddings to first 256 dimensions and re-normalize
q_emb_256 = q_emb_with_prefix[:, :256]
q_emb_256 = q_emb_256 / np.linalg.norm(q_emb_256, axis=1, keepdims=True)

recall_256 = calculate_recall_at_k(q_emb_256, corpus_emb_256, ground_truth_indices, k=10)

print(f"👉 Recall@10 (768 Dims - Original) : {recall_with_prefix * 100:.2f}%")
print(f"👉 Recall@10 (256 Dims - Truncated): {recall_256 * 100:.2f}%")
loss = (recall_with_prefix - recall_256) * 100
print(f"📉 Total Recall Loss after Truncation: {loss:.2f}%")

# ---------------------------------------------------------
# STEP 5: Save Embeddings and Aligned IDs to Disk
# ---------------------------------------------------------
print("\n[Step 5] Saving NumPy Array and Aligned IDs to disk...")

os.makedirs("output", exist_ok=True)

# 1. Save NumPy Matrix
npy_path = "output/corpus_embeddings.npy"
np.save(npy_path, corpus_embeddings)

# 2. Save Aligned IDs
ids_path = "output/corpus_ids.txt"
with open(ids_path, "w", encoding="utf-8") as f:
    for i in range(len(corpus)):
        f.write(f"doc_{i}\n")

print(f"✅ Embeddings saved to : {npy_path}")
print(f"✅ Aligned IDs saved to : {ids_path}")
print("\n🎉 Process completed successfully!")
