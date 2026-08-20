# From Search Engines to GraphRAG: Connecting the Dots

Today was less about learning new tools and more about understanding how modern retrieval and knowledge systems fit together as a complete pipeline.

Topics I explored and revised:

- Inverted Index
- TF-IDF
- BM25
- Knowledge Graphs
- Neo4j & Cypher
- RDF & SPARQL
- Wikidata & Entity Linking
- SHACL Validation
- Entity Resolution (Splink)
- Knowledge Graph Construction Pipelines
- GraphRAG
- Leiden Community Detection

One insight that stood out:

Modern AI retrieval systems are not built on vector search alone. Production-grade systems combine classical information retrieval, knowledge graphs, graph traversal, validation layers, entity resolution, and LLM reasoning to deliver reliable answers.

A simplified view of the journey:

```text
Documents
    ↓
BM25 / Retrieval
    ↓
Knowledge Graph Construction
    ↓
Entity Resolution
    ↓
Validation (SHACL)
    ↓
Graph Database
    ↓
Community Detection (Leiden)
    ↓
GraphRAG
    ↓
LLM Reasoning
