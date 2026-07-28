# 🚀 Day 01 — Local RAG Pipeline, Golden Dataset & Core Concepts

Welcome to **Day 01** of my **AI & Data Engineering Roadmap**.

Today's focus was on designing and evaluating a **local Retrieval-Augmented Generation (RAG) pipeline** with a strong emphasis on:

- Zero-hallucination principles
- Provenance tracking
- Retrieval evaluation
- System design fundamentals
- Deterministic validation workflows

---

# 🧠 Core Architecture Concepts Learned

## 1. Retrieval Contract (রিট্রিভাল কন্ট্রাক্ট)

A formal agreement that defines what a retrieval system can and cannot do.

It specifies:

- Supported question types
- Authorized knowledge sources
- Data freshness requirements (SLA)
- Provenance and citation expectations
- Operational boundaries

This contract helps prevent scope creep and ensures trustworthy retrieval behavior.

---

## 2. Parametric Memory (প্যারামেট্রিক মেমোরি)

Knowledge stored directly inside an LLM's model weights.

### Characteristics

- Extremely fast access
- Static after training
- Source attribution is difficult
- Updating requires retraining or fine-tuning

### Examples

- General world knowledge
- Language understanding
- Learned reasoning patterns

---

## 3. Non-Parametric Memory (নন-প্যারামেট্রিক মেমোরি)

Knowledge stored outside the model in searchable systems such as:

- Vector databases
- Search indexes
- Document stores
- Knowledge bases

### Characteristics

- Easily updateable
- Fully traceable
- Auditable
- Suitable for real-time knowledge retrieval

### Examples

- Company documentation
- Research repositories
- Internal knowledge bases

---

## 4. Grounding (গ্রাউন্ডিং)

Grounding ensures that every generated answer is tied directly to retrieved evidence.

### Benefits

- Reduces hallucinations
- Improves factual accuracy
- Enables source verification
- Builds user trust

A grounded answer should always be explainable through a specific source document.

---

## 5. Corpus (কর্পাস)

The curated collection of documents that a retrieval system is allowed to search.

### Requirements

- Governed
- Authorized
- Structured
- Maintainable

The quality of the corpus directly influences retrieval quality.

---

# 🛠️ Practical Execution

## Step 1 — Corpus Selection

Created a local knowledge base called **Chapai-Intel**, containing information about:

- History
- Geography
- Culture
- Transportation
- Mango ecosystem
- Local economy

---

## Step 2 — Golden Dataset Creation

Built a benchmark dataset containing **20 realistic user questions** stored in:

```text
questions.jsonl
```

Each query was mapped to its corresponding ground-truth source document for retrieval validation.

---

## Step 3 — Retrieval Contract Design

Defined:

- Retrieval scope
- Data ownership boundaries
- Freshness SLAs
- Provenance requirements
- Evaluation expectations

---

## Step 4 — Repository & Environment Setup

Initialized the project repository and local development environment.

### Actions Performed

```bash
git init
```

- Created project structure
- Configured Python environment
- Established version control workflow

---

## Step 5 — Retrieval Evaluation Script

Developed a deterministic retrieval validator:

```text
search.py
```

### Responsibilities

- Execute retrieval queries
- Compare results against ground truth
- Measure retrieval accuracy
- Generate evaluation metrics

---

# 📊 Evaluation Results

The retrieval evaluation pipeline achieved perfect benchmark performance.

| Metric | Result |
|----------|----------|
| Total Queries | 20 |
| Successful Matches | 20 ✅ |
| Failed Matches | 0 ❌ |
| Accuracy | 100% 🎯 |

This validates the correctness and consistency of the local retrieval workflow.

---

# 💻 Commands Used

## Environment & Directory Setup

```bash
cd ~/Documents
mkdir chapai-intel-rag
cd chapai-intel-rag
ls
```

---

## File Creation & Execution

```bash
nano search.py
nano questions.jsonl

python3 search.py
```

---

## Git & GitHub Workflow

```bash
git init
git add .

git commit -m "Add Day-01: Core RAG concepts, corpus, golden set, and evaluation script"

git branch -M main

git remote add origin https://github.com/nahid-mahmud555/ai-data-engineering-roadmap.git

git push -u origin main
```

---

# 📂 Project Structure

```text
day_01/
├── corpus/
│   ├── history_and_geography.txt
│   ├── mango_and_economy.txt
│   └── culture_and_transport.txt
│
├── questions.jsonl
├── search.py
└── README.md
```

---

# 📚 Reading & Research

## RAG Fundamentals

- Retrieval-Augmented Generation from First Principles

## Research Papers

### Lewis et al. (2020)

**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**

**Key Contribution:**
Introduced the original RAG framework that combines retrieval systems with large language models.

---

### Gao et al. (2023)

**Retrieval-Augmented Generation for Large Language Models: A Survey**

**Key Contribution:**
Comprehensive survey covering retrieval architectures, evaluation methodologies, and future directions.

---

## Data Engineering Foundation

**Fundamentals of Data Engineering**  
*Joe Reis & Matt Housley*

### Focus Areas

- Data lifecycle
- Data architecture
- Pipeline design
- Operational excellence

---

# 🎯 Day 01 Outcome

✅ Built a local knowledge corpus

✅ Created a golden evaluation dataset

✅ Designed a retrieval contract

✅ Implemented deterministic retrieval validation

✅ Achieved 100% benchmark accuracy

✅ Established foundational RAG and Data Engineering concepts

---

## 👨‍💻 Maintained By

**Nahid Mahmud**  
*AI & Data Engineering Roadmap Journey*
