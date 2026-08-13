# 🛡️ Secure RAG & Knowledge Search Engine with PII Redaction

A lightweight, security-first Retrieval-Augmented Generation (RAG) and document search pipeline built with Python, featuring automated security firewalls, sensitive data (PII/Secret) redaction, parent-child chunking, provenance tracking, and scoring-based retrieval.

---

# 🚀 Overview

Modern AI-powered knowledge systems often prioritize retrieval performance while overlooking a critical challenge: **data security**. Sensitive information such as passwords, API keys, tokens, and confidential credentials can unintentionally enter indexing pipelines, creating significant security risks.

This project addresses that challenge by introducing a **Secure RAG Architecture** that automatically scans uploaded documents, detects sensitive information, redacts confidential content before indexing, and preserves complete source traceability through provenance metadata.

Designed and implemented from scratch as a practical exploration of **Secure AI Systems**, **Knowledge Retrieval Engineering**, and **Defensive Data Processing Pipelines**.

---

# 🎯 Key Features

### 🔒 Automated Security Firewall
- Scans uploaded documents before indexing.
- Detects hardcoded credentials, passwords, API keys, secrets, and other sensitive patterns.
- Prevents confidential information from entering the retrieval pipeline.

### 🧹 PII & Secret Redaction Engine
- Replaces detected sensitive content with:

```text
[REDACTED_SENSITIVE_DATA]
```

- Eliminates accidental exposure of credentials during retrieval and search operations.

### 🚨 Security Audit Alerts
- Generates real-time security notifications whenever restricted data is detected.
- Maintains an audit trail for intercepted sensitive information.

### 📑 Parent-Child Chunking Pipeline
- Splits cleaned documents into logically structured chunks.
- Preserves semantic boundaries for improved retrieval quality.

### 🏷️ Provenance Tracking

Every indexed chunk contains source metadata:

```text
[Source: filename | Segment: chunk_id]
```

This ensures:

- Full source transparency
- Easy document traceability
- Retrieval explainability

### 🤖 Scoring-Based Retrieval Engine

Instead of relying on first-match retrieval, the system:

- Scores all candidate chunks
- Ranks results based on relevance
- Returns the most contextually appropriate information

### 🔍 Interactive Knowledge Search

- Keyword-based document exploration
- Source-aware search results
- Fast retrieval with provenance attribution

---

# 🏗️ System Architecture

```text
                 ┌────────────────────┐
                 │ Uploaded Document  │
                 └──────────┬─────────┘
                            │
                            ▼
              ┌─────────────────────────┐
              │ Security Firewall Scan  │
              └──────────┬──────────────┘
                         │
         Sensitive Data Found?
                │
       ┌────────┴─────────┐
       │                  │
      YES                NO
       │                  │
       ▼                  ▼
┌────────────────┐  ┌────────────────┐
│ PII Redaction  │  │ Clean Content  │
└───────┬────────┘  └───────┬────────┘
        │                   │
        └────────┬──────────┘
                 ▼
      ┌──────────────────────┐
      │ Parent-Child Chunker │
      └──────────┬───────────┘
                 ▼
      ┌──────────────────────┐
      │ Provenance Tagging   │
      └──────────┬───────────┘
                 ▼
      ┌──────────────────────┐
      │ Knowledge Index      │
      └──────────┬───────────┘
                 ▼
 ┌──────────────────────────────┐
 │ Search Engine & AI Chatbot   │
 └──────────────────────────────┘
```

---

# 💻 Technology Stack

| Category | Tools |
|-----------|--------|
| Programming Language | Python |
| Environment | Google Colab, Jupyter Notebook |
| UI Framework | ipywidgets |
| Pattern Detection | Regular Expressions (`re`) |
| Interactive Components | IPython.display |
| Retrieval Engine | Custom Scoring-Based Retrieval |
| Security Layer | PII & Secret Detection Pipeline |

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/secure-rag-pii-redaction.git
cd secure-rag-pii-redaction
```

## 2️⃣ Open in Google Colab

Upload the notebook or copy the source code into a new Colab notebook.

## 3️⃣ Run the Application

Execute all cells to launch the interactive dashboard.

### Available Tabs

#### 📤 Upload & Secure
- Upload raw document content
- Run security inspection
- Automatically redact sensitive information

#### 🤖 AI Chatbot
- Ask questions against indexed knowledge
- View source-aware answers

#### 🔍 Search Engine
- Search keywords across the knowledge base
- Inspect provenance metadata

---

# 📄 Example Test Input

```text
Company Internal Policy

Production Database Password:
password:= prod_super_secret_987!

Root API Key:
secret:= sk-live-998877665544332211

Employees must follow all operational security policies.
Unauthorized disclosure of credentials is strictly prohibited.
```

---

# 📊 Example Execution & Output

## 1️⃣ Document Processing

```text
Successfully processed 'company_policy.txt'.
Total chunks indexed: 5.

--- Security Notifications ---

⚠️ Alert from 'company_policy.txt':
Blocked & Redacted sensitive data ->
[
 'password:=',
 'secret:=',
 'prod_super_secret_987!',
 'sk-live-998877665544332211'
]
```

---

## 2️⃣ AI Chatbot Query

### User Query

```text
What is the master production database password and root API secret?
```

### AI Response

```text
🤖 AI Answer:

Based on your documents, here is what I found regarding your query:

"For internal database management, the master production database

[REDACTED_SENSITIVE_DATA]
[REDACTED_SENSITIVE_DATA]

Keep this extremely confidential and never share it on public channels."
```

### Provenance Metadata

```text
📌 Sources:

[Source: company_policy.txt | Segment: chunk_2]
```

---

# 🔐 Security Benefits

✅ Prevents accidental credential leakage

✅ Stops sensitive information from entering the retrieval index

✅ Preserves retrieval explainability through provenance metadata

✅ Maintains searchable knowledge without exposing secrets

✅ Provides real-time security monitoring and audit visibility

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

- Retrieval-Augmented Generation (RAG)
- Secure AI System Design
- PII Detection & Redaction
- Document Processing Pipelines
- Provenance Tracking
- Retrieval Engineering
- Information Security Fundamentals
- Interactive Python Applications

---

# 🌟 Future Improvements

- Vector Database Integration (FAISS / ChromaDB)
- Embedding-Based Semantic Search
- Role-Based Access Control (RBAC)
- Document Versioning
- Security Dashboard Analytics
- Multi-File Knowledge Bases
- Hybrid Search (BM25 + Vector Search)
- LLM-Powered Answer Generation
- Advanced Secret Detection Rules

---

# 👨‍💻 Author

**Designed, Architected, and Implemented from Scratch**

A hands-on exploration of building secure retrieval systems that prioritize both **knowledge accessibility** and **data protection**, demonstrating how security can be integrated directly into modern AI retrieval pipelines rather than treated as an afterthought.

---

## ⭐ If you found this project useful, consider giving the repository a star!
