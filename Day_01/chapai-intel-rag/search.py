import os
import json

CORPUS_DIR = "corpus"
QUESTIONS_FILE = "questions.jsonl"

def search_corpus(query):
    # খুব সিম্পল কিওয়ার্ড ম্যাচিং বা রিট্রিভাল লজিক
    results = []
    query_words = query.lower().split()
    
    if not os.path.exists(CORPUS_DIR):
        print(f"Error: {CORPUS_DIR} folder not found!")
        return results

    for filename in os.listdir(CORPUS_DIR):
        if filename.endswith(".txt"):
            file_path = os.path.join(CORPUS_DIR, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # চেক করা ফাইলে কোয়েরির শব্দগুলো আছে কি না
                match_count = sum(1 for word in query_words if word in content.lower())
                if match_count > 0:
                    results.append((filename, match_count))
        
    # সবচেয়ে বেশি মিল থাকা ফাইলটা আগে দেখাবে
    results.sort(key=lambda x: x[1], reverse=True)
    return results

def evaluate_golden_set():
    print("=== Running Evaluation on Golden Set ===")
    if not os.path.exists(QUESTIONS_FILE):
        print(f"Error: {QUESTIONS_FILE} not found!")
        return

    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                item = json.loads(line)
                q_id = item.get("id")
                question = item.get("question")
                expected_source = item.get("source")

                print(f"\n[Q{q_id}] {question}")
                print(f"Expected Source: {expected_source}")

                retrieved = search_corpus(question)
                if retrieved:
                    top_match = retrieved[0][0]
                    print(f"Retrieved Source: {top_match}")
                    if top_match == expected_source:
                        print("Status: ✅ MATCH (Success)")
                    else:
                        print("Status: ❌ MISMATCH")
                else:
                    print("Status: ⚠️ No results found in corpus")

if __name__ == "__main__":
    evaluate_golden_set()
