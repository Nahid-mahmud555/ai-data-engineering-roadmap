import math

# ১. ২০০টা ডকুমেন্ট জেনারেট করা
upazilas = ["Chapainawabganj Sadar", "Shibganj", "Gomastapur", "Nachol", "Bholahat"]
local_keywords = [
    "Gambhira folk music and traditional cultural performance",
    "Alkap drama and village festival entertainment",
    "Chhota Sona Mosque sultanate architectural landmark",
    "Tohkhana Complex sufi shrine and winter palace",
    "Kansat Mango Market wholesale seasonal fruit trade",
    "Silk industry sericulture mulberry and handloom weaving",
    "Padma and Mahananda river transport and water routes",
    "Barind Tract reddish soil and high land agriculture",
    "Gauda kingdom ancient history and heritage ruins",
    "Local pottery handicrafts and rural cottage economy",
    "Fazli Khirsapat Langra mango orchard cultivation",
    "Purnabhaba river ecosystem and local farming"
]

corpus_documents = {}
doc_id = 1

for upazila in upazilas:
    for kw in local_keywords:
        if doc_id <= 200:
            text = f"Document regarding {kw} located specifically in {upazila} region of Chapainawabganj district."
            corpus_documents[f"doc_{doc_id}"] = text
            doc_id += 1

extra_id = 1
while len(corpus_documents) < 200:
    text = f"General archival record number {extra_id} about agricultural trade, mango harvest, and local heritage in Chapainawabganj."
    corpus_documents[f"doc_{doc_id}"] = text
    doc_id += 1
    extra_id += 1

# ২. ইনভার্টেড ইনডেক্স ও লেংথ হিসাব করা
inverted_index = {}
doc_lengths = {}

for d_id, text in corpus_documents.items():
    clean_text = ''.join([char if char.isalnum() or char.isspace() else ' ' for char in text])
    tokens = clean_text.lower().split()
    doc_lengths[d_id] = len(tokens)
    
    for token in tokens:
        if len(token) > 2:
            if token not in inverted_index:
                inverted_index[token] = []
            if d_id not in inverted_index[token]:
                inverted_index[token].append(d_id)

avg_dl = sum(doc_lengths.values()) / len(corpus_documents)
N = len(corpus_documents)

# ৩. BM25 স্কোরের ফাংশন (k1 = 1.2, b = 0.75)
def compute_bm25(query, k1=1.2, b=0.75):
    query_tokens = query.lower().split()
    scores = {d_id: 0.0 for d_id in corpus_documents}
    
    for q in query_tokens:
        if q in inverted_index:
            docs_containing_q = inverted_index[q]
            df = len(docs_containing_q)
            idf = math.log(((N - df + 0.5) / (df + 0.5)) + 1.0)
            
            for d_id in docs_containing_q:
                text = corpus_documents[d_id]
                tokens = ''.join([char if char.isalnum() or char.isspace() else ' ' for char in text]).lower().split()
                tf = tokens.count(q)
                dl = doc_lengths[d_id]
                
                numerator = tf * (k1 + 1)
                denominator = tf + k1 * (1 - b + b * (dl / avg_dl))
                scores[d_id] += idf * (numerator / denominator)
                
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores[:10]

# ৪. তোর হোমওয়ার্কের জন্য ২০টি গোল্ডেন কুয়েরি (Golden Questions)
golden_queries = [
    "gambhira folk music",
    "alkap drama festival",
    "chhota sona mosque",
    "tohkhan complex shrine",
    "kansat mango market",
    "silk industry sericulture",
    "padma mahananda river",
    "barind tract agriculture",
    "gauda kingdom history",
    "local pottery handicrafts",
    "fazli khirsapat mango",
    "purnabhaba ecosystem",
    "shibganj heritage",
    "gomastapur trade",
    "nachol land",
    "bholahat region",
    "seasonal fruit trade",
    "mulberry handloom weaving",
    "sultanate architecture",
    "archival agricultural record"
]

# ৫. ২০টি কুয়েরি রান করে Recall@10 এর টেবিল বানানো
print("=" * 75)
print(f"{'Q.No':<6} | {'Golden Query':<30} | {'Hits/10':<8} | {'Recall@10 Rate':<15}")
print("=" * 75)

total_recall_sum = 0

for i, query in enumerate(golden_queries, 1):
    bm25_results = compute_bm25(query)
    bm25_top10_ids = [d_id for d_id, score in bm25_results]
    
    # রিলিভেন্ট ডকুমেন্ট বের করার লজিক
    relevant_docs = [d_id for d_id, text in corpus_documents.items() if any(q in text.lower() for q in query.lower().split())]
    total_relevant = len(relevant_docs)
    
    hits = sum(1 for d_id in bm25_top10_ids if d_id in relevant_docs)
    max_possible = min(10, total_relevant) if total_relevant > 0 else 1
    recall_rate = (hits / max_possible) * 100 if max_possible > 0 else 0
    total_recall_sum += recall_rate
    
    print(f"{i:<6} | {query:<30} | {hits}/10      | {recall_rate:>6.1f}%")

print("=" * 75)
avg_system_recall = total_recall_sum / len(golden_queries)
print(f" AVERAGE SYSTEM RECALL@10 ACROSS 20 QUERIES: {avg_system_recall:.2f}%")
print("=" * 75)
