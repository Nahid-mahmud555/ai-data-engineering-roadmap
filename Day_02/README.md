# 🔍 BM25 Search Engine Baseline & Learning Journal

A custom **Information Retrieval (IR)** system built entirely from scratch in Python, implementing synthetic corpus generation, inverted indexing, Okapi BM25 scoring, and rigorous **Recall@10** evaluation.

---

## 💡 What I Learned & Explored Today

### 1️⃣ Synthetic Corpus Generation
- Learned how to programmatically generate domain-specific data without manual typing.
- Built **200 unique documents** using a matrix-combination approach based on real regional data from **Chapainawabganj**, including:
  - Kansat Mango Market
  - Gambhira Folk Music
  - Chhota Sona Mosque
  - Silk Industry
  - Barind Tract
  - And many other local landmarks, industries, and cultural elements.

### 2️⃣ Inverted Indexing & Text Preprocessing
- Understood how search engines achieve lightning-fast retrieval using an **Inverted Index**, where terms are mapped directly to document IDs.
- Implemented:
  - Text tokenization
  - Lowercasing
  - Special character filtering
  - Clean document preprocessing pipelines

### 3️⃣ BM25 vs. TF-IDF & Mathematical Modeling
- Implemented the **Okapi BM25** ranking algorithm completely from scratch.
- Used the standard parameters:

```text
k1 = 1.2
b  = 0.75
```

- Learned how BM25 improves upon traditional TF-IDF through:
  - **Term Saturation** (prevents high-frequency words from dominating rankings)
  - **Document Length Normalization** (balances short and long documents fairly)
  - More robust relevance scoring for real-world retrieval systems

### 4️⃣ System Evaluation & The "Floor" Concept
- Evaluated the retrieval system using **20 Golden Queries** specifically designed for this corpus.
- Applied the **Recall@10** metric to measure retrieval effectiveness.
- Established a baseline performance of:

```text
Recall@10 = 98.00%
```

- This score serves as the project's **Floor**, meaning every future optimization, ranking enhancement, or advanced retrieval technique must outperform this benchmark.

---

## 🛠️ How I Executed the Task

### Step 1 — Corpus Setup
Built Python logic to automatically generate **200 natural-sounding documents** by combining local upazilas, cultural elements, industries, historical sites, and geographical features.

### Step 2 — Indexing
Parsed every document, removed noisy tokens, calculated document lengths (`dl`), and constructed the **Inverted Index**.

### Step 3 — BM25 Engine
Implemented the complete BM25 mathematical scoring formula with:
- Inverse Document Frequency (IDF)
- Term Frequency weighting
- Length normalization

### Step 4 — Evaluation Pipeline
Automated testing against **20 Golden Queries**, calculated top-10 retrieval performance, and generated a detailed evaluation report.

### Step 5 — Documentation
Organized the project into a clean Python script:

```text
baseline_bm25.py
```

and documented the complete workflow for GitHub portfolio presentation and future experimentation.

---

## 📊 Evaluation Results (20 Golden Queries)

```text
===========================================================================
Q.No   | Golden Query                   | Hits/10  | Recall@10 Rate
===========================================================================
1      | gambhira folk music            | 5/10     |   100.0%
2      | alkap drama festival           | 5/10     |   100.0%
3      | chhota sona mosque             | 6/10     |    60.0%
4      | tohkhan complex shrine         | 5/10     |   100.0%
5      | kansat mango market            | 10/10    |   100.0%
6      | silk industry sericulture      | 5/10     |   100.0%
7      | padma mahananda river          | 10/10    |   100.0%
8      | barind tract agriculture       | 5/10     |   100.0%
9      | gauda kingdom history          | 5/10     |   100.0%
10     | local pottery handicrafts      | 10/10    |   100.0%
11     | fazli khirsapat mango          | 10/10    |   100.0%
12     | purnabhaba ecosystem           | 5/10     |   100.0%
13     | shibganj heritage              | 10/10    |   100.0%
14     | gomastapur trade               | 10/10    |   100.0%
15     | nachol land                    | 10/10    |   100.0%
16     | bholahat region                | 10/10    |   100.0%
17     | seasonal fruit trade           | 10/10    |   100.0%
18     | mulberry handloom weaving      | 5/10     |   100.0%
19     | sultanate architecture         | 5/10     |   100.0%
20     | archival agricultural record   | 10/10    |   100.0%
===========================================================================
AVERAGE SYSTEM RECALL@10 ACROSS 20 QUERIES: 98.00%
===========================================================================

Baseline Performance: 98.00% Recall@10
```

---

## ⚙️ How to Run

```bash
python3 baseline_bm25.py
```
