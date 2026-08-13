# ==========================================
# 🚀 SECURE RAG & KNOWLEDGE SEARCH ENGINE (ZERO-START)
# ==========================================

# 1. Install required lightweight libraries
!pip install -q ipywidgets

import os
import re
import ipywidgets as widgets
from IPython.display import display, HTML

# ------------------------------------------
# MOCK DATABASE & STORAGE (Initially Empty)
# ------------------------------------------
knowledge_vault = []
security_alerts = []

# ------------------------------------------
# BACKEND CORE LOGIC
# ------------------------------------------
def process_and_secure_document(file_name, raw_text):
    global knowledge_vault, security_alerts
    
    # Reset storage on every new upload so only the current upload is processed
    knowledge_vault = []
    security_alerts = []
    
    if not raw_text.strip():
        return "⚠️ Upload failed: The document content is empty!"

    # Step 1: Strict Sensitive Data / Secret Detection & Full Redaction
    # Catching 'password:= value', 'secret:= value', 'sk-live-xxx', etc.
    sensitive_patterns = [
        r'password\s*[:=]\s*\S+', 
        r'secret\s*[:=]\s*\S+', 
        r'api_key\s*[:=]\s*\S+',
        r'prod_super_secret_\S+',
        r'sk-live-\S+'
    ]
    
    detected_sensitives = []
    cleaned_text = raw_text
    
    for pattern in sensitive_patterns:
        matches = re.findall(pattern, raw_text, re.IGNORECASE)
        if matches:
            detected_sensitives.extend(matches)
            # Fully replace the secret phrase with [REDACTED_SENSITIVE_DATA]
            cleaned_text = re.sub(pattern, "[REDACTED_SENSITIVE_DATA]", cleaned_text, flags=re.IGNORECASE)
            
    if detected_sensitives:
        security_alerts.append(f"⚠️ Alert from '{file_name}': Blocked & Redacted sensitive data -> {detected_sensitives}")
    
    # Step 2: Parent-Child Chunking (Splitting into clean paragraphs)
    paragraphs = [p.strip() for p in cleaned_text.split('\n\n') if p.strip()]
    
    for i, para in enumerate(paragraphs):
        chunk_id = f"chunk_{i+1}"
        provenance = f"[Source: {file_name} | Segment: {chunk_id}]"
        
        # Storing only the freshly processed chunks
        knowledge_vault.append({
            "content": para,
            "source": provenance,
            "file": file_name
        })
        
    return f"Successfully processed '{file_name}'. Total chunks indexed: {len(paragraphs)}."

def chatbot_query(prompt):
    prompt_lower = prompt.lower()
    query_words = set([w for w in prompt_lower.split() if len(w) > 2])
    
    if not knowledge_vault:
        return "⚠️ Knowledge base is empty! Please upload and process a document first.", []
        
    if not query_words:
        return "Please provide a more descriptive query.", []
    
    best_match = None
    max_score = 0
    
    for item in knowledge_vault:
        content_lower = item['content'].lower()
        score = sum(1 for word in query_words if word in content_lower)
        
        if score > max_score:
            max_score = score
            best_match = item
            
    if not best_match or max_score == 0:
        return "I couldn't find any relevant context in the uploaded documents to answer your question.", []
    
    answer = f"Based on your documents, here is what I found regarding your query:\n\n\"{best_match['content']}\""
    sources = [best_match['source']]
    
    return answer, sources

def search_vault(keyword):
    if not knowledge_vault:
        return ["⚠️ Knowledge base is empty! Please upload a document first."]
        
    results = []
    keyword_lower = keyword.lower()
    for item in knowledge_vault:
        if keyword_lower in item['content'].lower():
            results.append(f"• **Match Found:** {item['content']} \n  👉 *{item['source']}*")
    return results

# ------------------------------------------
# INTERACTIVE UI (Google Colab Widgets)
# ------------------------------------------
print("Initializing Secure RAG Interface (Zero-Start Mode)...\n")

tab = widgets.Tab()

# --- Tab 1: Upload & Security ---
upload_file_name = widgets.Text(value="company_policy.txt", description="File Name:")
# Initially blank or ready for your custom paste
upload_text_area = widgets.Textarea(
    value="", 
    placeholder="Paste your document content here...",
    description="Doc Content:",
    layout=widgets.Layout(width='100%', height='140px')
)
upload_btn = widgets.Button(description="Upload & Process", button_style='success')
upload_output = widgets.Output()

def on_upload_clicked(b):
    with upload_output:
        upload_output.clear_output()
        msg = process_and_secure_document(upload_file_name.value, upload_text_area.value)
        print(msg)
        if security_alerts:
            print("\n--- Security Notifications ---")
            for alert in security_alerts:
                print(alert)

upload_btn.on_click(on_upload_clicked)
tab1_box = widgets.VBox([widgets.HTML("<h3>📁 Document Ingestion & Security Filter</h3>"), upload_file_name, upload_text_area, upload_btn, upload_output])

# --- Tab 2: Chatbot Interface ---
chat_input = widgets.Text(placeholder="Ask anything about your documents...", description="Query:", layout=widgets.Layout(width='80%'))
chat_btn = widgets.Button(description="Ask AI", button_style='primary')
chat_output = widgets.Output()

def on_chat_clicked(b):
    with chat_output:
        chat_output.clear_output()
        ans, srcs = chatbot_query(chat_input.value)
        print(f"🤖 AI Answer:\n{ans}\n")
        if srcs:
            print("📌 Provenance Sources:")
            for s in srcs:
                print(f"   {s}")

chat_btn.on_click(on_chat_clicked)
tab2_box = widgets.VBox([widgets.HTML("<h3>💬 Secure Chatbot with Provenance</h3>"), widgets.HBox([chat_input, chat_btn]), chat_output])

# --- Tab 3: Search Engine ---
search_input = widgets.Text(placeholder="Type keyword to search chunks...", description="Keyword:", layout=widgets.Layout(width='80%'))
search_btn = widgets.Button(description="Search", button_style='info')
search_output = widgets.Output()

def on_search_clicked(b):
    with search_output:
        search_output.clear_output()
        res = search_vault(search_input.value)
        for r in res:
            display(HTML(f"<p>{r}</p>"))

search_btn.on_click(on_search_clicked)
tab3_box = widgets.VBox([widgets.HTML("<h3>🔎 Instant Keyword & Semantic Search</h3>"), widgets.HBox([search_input, search_btn]), search_output])

# Assemble Tabs
tab.children = [tab1_box, tab2_box, tab3_box]
tab.set_title(0, '1. Upload & Secure')
tab.set_title(1, '2. AI Chatbot')
tab.set_title(2, '3. Search Engine')

display(tab)
