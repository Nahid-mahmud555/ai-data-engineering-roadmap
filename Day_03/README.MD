# RAG Pipeline & Hierarchical Chunking Architecture

A robust, localized prototype simulation of a Retrieval-Augmented Generation (RAG) pipeline designed to evaluate chunk granularity, enforce deterministic stable ID contracts, and manage parent-child metadata relationships across a multi-domain document corpus.

---

## 🚀 Today's Journey & Implemented Tasks

Today, we built, executed, and validated a complete foundational RAG pipeline from scratch. Here is a step-by-step breakdown of what we accomplished:

### 1. Corpus Ingestion & Granularity Splitting (Task 1)

- Processed a custom corpus of **10 multi-domain text files** (`Doc_01.txt` to `Doc_10.txt`).
- Experimented with and evaluated three distinct chunk granularities:
  - **Whole Document**
  - **Section**
  - **Paragraph**

### 2. Interactive Search & Granularity Testing (Task 2)

- Built a simulation environment to test golden queries against our corpus.
- Analyzed how different granularities impact:
  - Token overhead
  - Context retention
  - Search precision

### 3. Deterministic Stable Chunk ID Scheme (Task 3)

- Established a rigid contract ensuring all chunk identifiers survive updates.
- Utilized an MD5 hash algorithm combining:
  - Source URI
  - Section title
  - Structural offsets

### 4. Parent-Child Linkage Implementation (Task 4)

- Programmed hierarchical metadata mapping so every child chunk (paragraph) retains a `parent_id`.
- Ensured direct linkage to the parent section to prevent context loss during retrieval.

### 5. Corpus Failure Mode Analysis (Task 5)

- Documented architectural bottlenecks for each granularity layer.
- Evaluated limitations based on live system performance and retrieval behavior.

---

## 🛠️ Architectural Decision Record (A-Units Decision)

| Component | Selected Strategy | Justification & Evidence |
|-----------|------------------|--------------------------|
| **Retrieval Unit** | **Paragraph-Level Chunks** | Empirical testing across the 10-file corpus showed that paragraph chunks eliminate information dilution and deliver highly specific keyword matching while minimizing unnecessary token consumption. |
| **ID Scheme** | **Deterministic MD5 Hash** | `hash(source_uri + section_name + paragraph_index)` ensures chunk identifiers remain stable across re-indexing operations, enabling reliable traceability and source attribution. |
| **Context Bridge** | **Parent-Child Linkage** | Mitigates context fragmentation caused by smaller chunks by attaching a mandatory `parent_id` field to every child chunk, enabling escalation to the parent section whenever broader context is required. |

---

## ⚠️ Corpus Failure Mode Analysis

Based on empirical testing, each granularity layer exhibited unique operational limitations:

### Whole Document

> Suffers from information dilution and high token costs because the LLM becomes overwhelmed by irrelevant content distributed throughout large documents.

### Section

> Occasionally groups multiple sub-topics together, reducing retrieval precision for highly targeted search queries.

### Paragraph

> Frequently breaks contextual continuity, leaving critical background information isolated in neighboring paragraphs. This limitation is mitigated through the implemented parent-child linkage mechanism.

---

## 💻 Project Structure

```text
rag_assignment/
│
├── Doc_01.txt - Doc_10.txt    # Multi-domain corpus source files
├── Contract.txt               # Architectural rules, IDs, and failure modes
├── pipeline.py                # Core Python simulation script & search interface
└── README.md                  # Project documentation
```

---

## 🚀 How to Run the Pipeline

### 1. Open the Project Directory

Navigate to the project folder using your terminal.

### 2. Ensure Python 3 is Installed

Verify Python is available on your system:

```bash
python3 --version
```

### 3. Run the Interactive Simulation

```bash
python3 pipeline.py
```

### 4. Test the Retrieval Engine

Enter any keyword or topic, such as:

- AI
- Cloud
- Cybersecurity
- Machine Learning
- Data Engineering

The system will retrieve matching chunks using the hierarchical retrieval architecture.

To exit the program:

```text
exit
```

---

### 📖 Read the Full Article
For a detailed step-by-step breakdown of the architecture, engineering decisions, and implementation logic, check out my published article on Hashnode:
👉 [Building a Production-Grade RAG Pipeline from Scratch: Granularity, Stable IDs, and Parent-Child Linkages](https://nahid-mahmud555.hashnode.dev/building-a-production-grade-rag-pipeline-from-scratch-granularity-stable-ids-and-parent-child-linkages?utm_source=hashnode&utm_medium=feed)

## 🎯 Key Learning Outcomes

- Evaluated the impact of chunk granularity on retrieval performance.
- Implemented deterministic chunk identification for stable indexing.
- Designed hierarchical parent-child metadata relationships.
- Analyzed retrieval failure modes across multiple chunking strategies.
- Built a complete prototype RAG retrieval simulation from scratch using Python.

---
