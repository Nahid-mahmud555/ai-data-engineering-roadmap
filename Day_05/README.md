# 🚀 Vector Embeddings, Asymmetric Retrieval & Matryoshka Truncation

An end-to-end practical and theoretical exploration of modern Dense Vector Embeddings, Semantic Search, Instruction Prefixes, and Dimensionality Reduction using `BAAI/bge-base-en-v1.5`.

---

## 📌 Executive Summary & Key Learnings

In this practical session, we built, evaluated, and benchmarked a complete Natural Language Processing (NLP) / Information Retrieval (IR) pipeline using open-source embedding models:

1. **System Reproducibility**: Initialized fixed random seeds (`random.seed(42)`, `np.random.seed(42)`) to ensure deterministic embedding and calculation results.
2. **Corpus Construction**: Generated a synthetic dataset of 1,000 document chunks representing real-world text blocks.
3. **Dense Vector Generation**: Embedded the corpus using `BAAI/bge-base-en-v1.5` via `sentence-transformers`, building a normalized embedding matrix of shape `(1000, 768)`.
4. **Semantic Pair Benchmarking**: Evaluated dot-product cosine similarity across 20 hand-picked pairs (10 similar vs. 10 dissimilar) to verify geometric spatial alignment.
5. **Instruction Prefix Evaluation**: Measured **Recall@10** retrieval accuracy to analyze the impact of BGE's asymmetric query instruction prefixes.
6. **Matryoshka Vector Truncation**: Sliced embeddings from 768 dimensions down to 256 dimensions with $L_2$ re-normalization and evaluated recall loss.
7. **Artifact Persistence**: Exported raw binary matrices (`.npy`) and aligned textual ID mappings (`.txt`) for indexing in downstream vector databases.

---

## 📚 Core Theoretical Concepts

### 1. The Distributional Hypothesis
> *"Words that occur in similar contexts tend to have similar meanings."*
Vector embeddings transform text into dense geometric representations where semantic similarity corresponds directly to geometric closeness.

### 2. Bi-Encoders vs. Cross-Encoders
* **Bi-Encoders (Dual Encoders)**: Embed queries and passages independently into fixed-size vectors. Allows pre-computing document vectors offline for sub-millisecond similarity search in Vector DBs.
* **Cross-Encoders**: Process query and document together through full cross-attention layers. Extremely accurate but computationally too expensive for large-scale document indexing.

### 3. Asymmetric Retrieval & Query Prefixes
In search tasks (*Question → Passage*), queries and documents have structural asymmetry (different length and context density). Asymmetric models require specific **Instruction Prefixes** added to queries (e.g., `Represent this sentence for searching relevant passages: `) to project query vectors into the document passage space.

### 4. Pooling Strategies
Transformer models output token-level vectors. A pooling strategy condenses these into a single sentence-level representation:
* **Mean Pooling**: Averages all token embeddings (Standard for Sentence-Transformers).
* **CLS Pooling**: Takes the vector of the special `[CLS]` token.

### 5. Matryoshka Embeddings & Storage Bill
Matryoshka Representation Learning (MRL) trains models such that early vector dimensions capture the primary semantic signal. Truncating a 768-dim vector to 256 dims significantly reduces disk space, RAM usage, and index build times while preserving search accuracy.

---

## 🧪 Experimental Benchmarks & Results

### 1. Semantic Cosine Similarity Test
Using $L_2$-normalized vectors, cosine similarity simplifies directly to a fast dot product:

$$\text{Similarity}(v_1, v_2) = v_1 \cdot v_2$$

* **Similar Pairs Score**: High alignment ($\approx 0.87$)
* **Dissimilar Pairs Score**: Clear geometric distance ($\approx 0.28 - 0.44$)

### 2. Retrieval Evaluation (Recall@10)
Tested across queries targeting document chunks:

$$\text{Recall}@K = \frac{\text{Hits in Top-}K}{\text{Total Queries}}$$

| Configuration | Dimensions | Recall@10 Score | Recall Loss |
| :--- | :---: | :---: | :---: |
| **Query WITHOUT Prefix** | 768 | **100.00%** | Baseline |
| **Query WITH Prefix** | 768 | **100.00%** | 0.00% |
| **Truncated Embeddings** | **256** | **100.00%** | **0.00%** |

> **Key Finding**: Vector truncation down to 256 dimensions retained **100% Recall@10** on this corpus with **0.00% loss**, cutting memory/storage footprint by **66.6%**.

---

## 🛠️ Architecture & Tech Stack

* **Embedding Framework**: `sentence-transformers`
* **Base Model**: `BAAI/bge-base-en-v1.5`
* **Math & Vector Ops**: `numpy`, `scikit-learn`
* **Execution Options**: Local Linux CLI / Google Colab / FastEmbed (ONNX)

---

## 📁 Output Artifacts

```text
output/
├── corpus_embeddings.npy  # (1000, 768) NumPy float32 matrix
└── corpus_ids.txt         # Mapped document IDs (doc_0 to doc_999)
