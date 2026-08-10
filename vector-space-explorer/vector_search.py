import time
import numpy as np
import scipy.spatial
from sentence_transformers import SentenceTransformer

# 1. Load the embedding model
print("⏳ Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("✅ Model loaded successfully!\n" + "=" * 50)

# 2. Take corpus sentences input from the user
print("📝 STEP 1: Enter your corpus sentences.")
print("Type 4 or 5 sentences (press Enter after each, type 'DONE' when finished):")

user_corpus = []
while True:
    line = input(f"Sentence {len(user_corpus) + 1} (or type 'DONE'): ").strip()
    if line.upper() == 'DONE':
        if len(user_corpus) >= 3:
            break
        else:
            print("⚠️ Please enter at least 3-4 sentences first!")
            continue
    if line:
        user_corpus.append(line)

print(f"\n📦 Successfully received {len(user_corpus)} sentences!")

# 3. Generate embeddings and measure processing time
print("⚙️ Generating vector embeddings...")
start_time = time.time()
corpus_embeddings = model.encode(user_corpus)
embed_duration = time.time() - start_time
print(f"✅ Embeddings generated in {embed_duration:.4f} seconds!\n" + "=" * 50)

# 4. Take search query input from the user
print("🔍 STEP 2: Now enter your search query.")
query = input("Enter what you want to search: ").strip()

if query:
    print(f"\n🔎 Searching for: '{query}'...")
    
    # Measure search latency and execute vector search logic
    search_start = time.time()
    query_emb = model.encode([query])
    
    # Calculate cosine distance between query and corpus vectors
    distances = scipy.spatial.distance.cdist(query_emb, corpus_embeddings, "cosine")[0]
    
    # Sort indices by distance (lowest distance means highest similarity)
    sorted_indices = np.argsort(distances)
    search_duration = time.time() - search_start
    
    # 5. Print output and performance metrics
    print("\n" + "=" * 50)
    print(f"⏱️ Search Latency (Time taken): {search_duration:.6f} seconds")
    print("📊 Ranked Vector Search Results:")
    print("=" * 50)
    
    for rank, idx in enumerate(sorted_indices):
        score = 1 - distances[idx] # Similarity Score scaled from 0 to 1
        print(f"Rank {rank + 1} | Score: {score:.4f} | Text: {user_corpus[idx]}")
        
    print("=" * 50)
    
    # 6. Display raw vector values / numerical representations
    print("\n🧬 Vector Data Insight (First 5 dimensions of numbers):")
    print(f"Query Vector Sample:    {query_emb[0][:5]}")
    print(f"Top Result Vector Sample: {corpus_embeddings[sorted_indices[0]][:5]}")
    print("*(Notice how text is converted into these coordinates/numbers in space!)*")
else:
    print("⚠️ Query cannot be empty!")
