# What I Learned Today: Knowledge Graph Architecture

A comprehensive breakdown of core concepts, system design principles, and technical architectures for building production-grade Knowledge Graphs.

---

## 🚀 Key Takeaways & Mastered Concepts

### 1. When to Use a Knowledge Graph
* Learned that knowledge graphs are the ultimate choice when **relationships carry the core meaning** of the data.
* **Key Use Cases:** Supply chains, organizational hierarchies, drug-drug interactions, financial ownership networks, and regulatory compliance dependencies.

### 2. The Two Dominant Data Models
* **Labelled Property Graph (LPG):** Features nodes, typed/directed relationships, and properties attached to both (ideal for developer-friendly platforms like Neo4j).
* **RDF Triples:** Standardized `Subject–Predicate–Object` statements where terms are globally identified by **IRIs** (ideal for semantic web data and academic research graphs).

### 3. Performance Mechanics: Index-Free Adjacency
* Discovered why graphs beat traditional relational databases (SQL). While relational DBs rely on expensive, iterative `JOIN` operations that degrade at scale, graph databases use **Index-Free Adjacency**—storing direct memory pointers so traversal costs remain constant regardless of total dataset size.

### 4. Recognizing Anti-Patterns (When Graphs are Wrong)
* Understood that not every project needs a graph. They are the wrong choice for simple hierarchical trees or pure statistical aggregation workloads, which are better handled by relational or document databases.

### 5. Query-Driven Schema Modeling
* Learned the golden rule of graph architecture: **Never design a schema from a static Entity-Relationship Diagram (ERD).** Instead, model your nodes and relationships backward starting from the exact questions and queries your users will execute.

---

## 🧠 Core Vocabulary & Semantics

* **Property Graph:** A model where both nodes and relationships carry labels and key-value properties.
* **RDF Triple:** A statement structured as `Subject–Predicate–Object`, globally tracked via IRIs.
* **Index-Free Adjacency:** Physical pointers connecting records so graph traversal bypasses global index lookups.
* **Traversal:** The act of walking relationships outward from a starting node.
* **IRI (Internationalized Resource Identifier):** A globally unique naming standard used in RDF architectures.
