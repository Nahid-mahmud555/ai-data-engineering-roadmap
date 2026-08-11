# 1. প্রয়োজনীয় লাইব্রেরি ইনস্টল করা
!pip install -q rank_bm25 sentence-transformers numpy ipywidgets

import time
import ipywidgets as widgets
from IPython.display import display, clear_output
import numpy as np
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi

# মডেল লোড করা
print("🔄 Loading AI Embedding Model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("✅ Model Loaded Successfully!\n")

# স্টেট ভেরিয়েবল
corpus = []
search_attempts = 0
max_attempts = 4

# --- UI Widgets (গ্রাফিক্যাল ইন্টারফেস) ---
output_area = widgets.Output()

# হেডার ও স্টাইলিশ টাইটেল
title_html = widgets.HTML(value="<h2 style='color: #1E3A8A;'>🚀 Hybrid, Vector & BM25 Interactive Lab</h2>")
instruction_html = widgets.HTML(value="<p style='color: #4B5563;'><b>Step 1:</b> Add your custom sentences one by one. Type <b>'DONE'</b> when finished.</p>")

doc_input_box = widgets.Text(
    placeholder='Type sentence here (or type DONE)...',
    description='Sentence:',
    layout=widgets.Layout(width='70%')
)

add_button = widgets.Button(
    description='Add to Corpus',
    button_style='primary',
    icon='plus'
)

corpus_display_area = widgets.Output()

# সার্চ সেকশনের উইজেটগুলো (প্রথমে লুকানো থাকবে)
search_mode_dropdown = widgets.Dropdown(
    options=['Hybrid Search (RRF)', 'Vector Search (Semantic)', 'BM25 Search (Keyword)'],
    value='Hybrid Search (RRF)',
    description='Algorithm:',
    style={'description_width': 'initial'}
)

query_input_box = widgets.Text(
    placeholder='Type your search query here...',
    description='Query:',
    layout=widgets.Layout(width='70%')
)

search_button = widgets.Button(
    description='Run Search',
    button_style='success',
    icon='search'
)

search_container = widgets.VBox([
    widgets.HTML(value="<hr>"),
    widgets.HTML(value="<h3 style='color: #047857;'>🔍 Step 2: Search Dashboard (4 Attempts)</h3>"),
    search_mode_dropdown,
    widgets.HBox([query_input_box, search_button])
])

# --- লজিক: সেন্টেন্স অ্যাড করার ফাংশন ---
def on_add_clicked(b):
    global corpus, search_attempts
    with corpus_display_area:
        clear_output()
        text = doc_input_box.value.strip()
        
        if text:
            if text.upper() == 'DONE':
                if len(corpus) > 0:
                    print("🔒 Corpus successfully locked and processed! Ready for search below.")
                    doc_input_box.disabled = True
                    add_button.disabled = True
                    # সার্চ উইজেটগুলো শো করা
                    display(search_container)
                else:
                    print("⚠️ Please add at least one sentence before typing DONE!")
            else:
                corpus.append(text)
                print(f"✅ Added Successfully: '{text}'")
                print(f"📚 Total Stored Corpus ({len(corpus)} items):")
                for i, doc in enumerate(corpus):
                    print(f"   {i+1}. {doc}")
                doc_input_box.value = ""
        else:
            print("⚠️ Please type a valid sentence!")

add_button.on_click(on_add_clicked)

# --- লজিক: সার্চ ও র‍্যাঙ্কিং প্রসেসিং ---
def on_search_clicked(b):
    global search_attempts
    with output_area:
        clear_output()
        
        if search_attempts >= max_attempts:
            print(f"⚠️ You have completed all {max_attempts} search attempts!")
            return
            
        query = query_input_box.value.strip()
        if not query:
            print("⚠️ Please enter a valid search query!")
            return
            
        search_attempts += 1
        active_mode = search_mode_dropdown.value
        
        print(f"--- Search Attempt: {search_attempts} of {max_attempts} ---")
        print(f"🔍 Query: '{query}' | Engine Mode: {active_mode}\n")
        
        # ১. BM25 প্রসেস
        t_start = time.time()
        tokenized_corpus = [doc.lower().split() for doc in corpus]
        bm25 = BM25Okapi(tokenized_corpus)
        bm25_scores = bm25.get_scores(query.lower().split())
        bm25_time = (time.time() - t_start) * 1000
        
        # ২. Vector Search প্রসেস
        t_start = time.time()
        doc_embeddings = model.encode(corpus)
        query_embedding = model.encode(query)
        vector_scores = np.dot(doc_embeddings, query_embedding) / (
            np.linalg.norm(doc_embeddings, axis=1) * np.linalg.norm(query_embedding) + 1e-10
        )
        vector_time = (time.time() - t_start) * 1000
        
        # ৩. অ্যালগরিদম অনুযায়ী স্কোর ক্যালকুলেশন
        if active_mode == "BM25 Search (Keyword)":
            scores = bm25_scores
            exec_time = bm25_time
            engine_name = "BM25 (Exact Keyword Match)"
        elif active_mode == "Vector Search (Semantic)":
            scores = vector_scores
            exec_time = vector_time
            engine_name = "Vector Search (Semantic Meaning)"
        else:
            # Hybrid RRF
            bm25_ranks = np.argsort(bm25_scores)[::-1]
            vector_ranks = np.argsort(vector_scores)[::-1]
            rrf = np.zeros(len(corpus))
            for r, idx in enumerate(bm25_ranks):
                rrf[idx] += 1 / (60 + (r + 1))
            for r, idx in enumerate(vector_ranks):
                rrf[idx] += 1 / (60 + (r + 1))
            scores = rrf
            exec_time = (bm25_time + vector_time) / 2
            engine_name = "Hybrid Search (Vector + BM25 using RRF)"
            
        sorted_indices = np.argsort(scores)[::-1]
        
        print(f"✅ Executed Successfully via: {engine_name}")
        print(f"⚡ Latency Time: {exec_time:.2f} ms | Total Corpus Size: {len(corpus)}")
        print("="*65)
        print("📊 SCORE BREAKDOWN & RANKING RATIONALE:")
        print("="*65)
        
        for pos, idx in enumerate(sorted_indices):
            doc_text = corpus[idx]
            score_val = scores[idx]
            
            if pos == 0:
                badge = "🏆 Rank 1 (Top Match)"
                reason = f"Achieved the highest score (`{score_val:.4f}`) due to strong feature/keyword alignment with your query."
            else:
                badge = f"📉 Rank {pos + 1}"
                reason = f"Secured a relative score of (`{score_val:.4f}`), placing it lower due to lesser match density."
                
            print(f"\n{badge}")
            print(f"• Target Saved Document: {doc_text}")
            print(f"• Calculated Score: {score_val:.4f}")
            print(f"• Analysis: {reason}")
            print("-" * 65)
            
        query_input_box.value = ""

search_button.on_click(on_search_clicked)

# --- ফুল ইন্টারফেস ডিসপ্লে করা ---
display(widgets.VBox([
    title_html,
    instruction_html,
    widgets.HBox([doc_input_box, add_button]),
    corpus_display_area,
    output_area
]))
