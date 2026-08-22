# HNSW Multi-Layer Explorer

An interactive web-based visualizer built to demonstrate the internal mechanics of Hierarchical Navigable Small World (HNSW) graphs and Approximate Nearest Neighbor (ANN) search algorithms. 

Designed for beginners, students, and developers to intuitively understand how vector databases route and retrieve high-dimensional data in milliseconds.

---

##  Features

* **Custom Dataset Input:** Add your own words, categories, or data points to test real-time graph behavior.
* **Hyperparameter Control:** Configure core HNSW parameters directly:
  * **$M = 5$**: Maximum number of bidirectional links created per node.
  * **$ef\_construction = 4$**: Depth and thoroughness during index construction.
  * **$ef\_search = 4$**: Exploration scope during runtime queries.
* **Interactive Node Inspection:** Click any node on the canvas to inspect its direct M-connections across different network layers.
* **Multi-Layer Traversal Animation:** Watch search queries dynamically route from the **Top Expressway Layer** down through the **Middle Regional Layer**, finally dropping into the **Bottom Base Layer** to lock onto the target.

---

## 🛠️ How It Works

Traditional search algorithms scan sequentially, but HNSW builds a multi-layer skip-list graph structure:
1. **Top Layers (Expressway):** Sparse connections allow long-range jumps across the vector space.
2. **Middle Layers (Regional):** Intermediate routing steps to narrow down proximity.
3. **Bottom Layer (Base):** Dense graph containing all data points, ensuring precise final nearest neighbor identification.



## 💡 Purpose

This project was built as a lightweight learning tool to bridge theoretical systems mathematics with interactive front-end visualization, making complex vector search concepts crystal clear for everyone.


## ⭐️ Contributing
Contributions, feedback, and suggestions are always welcome! Feel free to fork this repository and submit a pull request.
