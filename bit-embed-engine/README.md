# 🚀 BitEmbed Engine: Vector Quantization & Semantic Search Simulator

An interactive Python-based simulator built in Google Colab to explore how modern vector databases handle memory optimization using **Binary Quantization** and **Hamming Distance Search**.

---

## 💡 The Core Concept
* **The AI's Brain (Float Vectors):** AI models (like `sentence-transformers`) convert human sentences into high-dimensional float vectors to capture true semantic meaning.
* **The Cost-Saver (Binary Quantization):** To slash massive server storage costs, heavy floats are compressed into pure bits (`1` for positive, `0` for negative/zero). **Floats keep the AI smart, while binary saves the server's pocket!**
* **The Lightning-Fast Search (Hamming Distance):** Instead of heavy mathematical computations, the system uses bit-level comparisons (`XOR`) to instantly retrieve the closest semantic matches.

---

## 🛠️ Tech Stack & Libraries
* **Python**
* **Google Colab** (Interactive UI via `ipywidgets`)
* **Sentence-Transformers** (`all-MiniLM-L6-v2`)
* **NumPy**

---

## ⚡ How It Works (Live Output Snippet)

When querying **`"i love python"`** against stored sentences, the system performs binary quantization and calculates the bit-level Hamming distance instantly:

```text
🔍 Query: "i love python"
   🔸 Query Binary: 0000101110011110...

🏆 Top Results (Closest to Farthest):
   [1] Matching Sentence: "i love python"
       • Hamming Distance (Different Bits): 0 🎯 (Exact Match)
   [2] Matching Sentence: "i love bangladesh"
       • Hamming Distance (Different Bits): 150 
   [3] Matching Sentence: "hello world"
       • Hamming Distance (Different Bits): 166

---
# How to Run
1. Open a new notebook in Google Colab.

 2. Copy the Python script from this repository into a cell.

  3. Run the cell, input a few sentences, type DONE, and start searching!

## Created by Nahid Mahmud
