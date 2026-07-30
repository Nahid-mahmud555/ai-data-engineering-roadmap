# Architectural Decision Record: Retrieval Unit & ID Scheme (A Units)

## Overview
This document records the core architectural decisions regarding data granularity, identifier generation, and corpus-backed validation for our RAG (Retrieval-Augmented Generation) pipeline prototype.

---

## 1. Selected Retrieval Unit
* **Decision:** **Paragraph-Level Granularity**
* **Justification:** Empirical testing across our multi-domain text corpus demonstrated that paragraph chunks eliminate information dilution and prevent token cost overheads. Unlike whole-document chunks which overwhelm the LLM with irrelevant details, paragraph units allow for hyper-specific keyword matching and precise retrieval.

---

## 2. Deterministic ID Scheme
* **Decision:** **MD5 Hash-Based Stable ID Contract**
* **Formula:** 
$$\text{Stable ID} = \text{hash}(\text{source\_uri} + \text{section\_name} + \text{paragraph\_index})$$
* **Justification:** To prevent broken references during re-indexing or document updates, every chunk utilizes a deterministic MD5 hash. This ensures static, immutable identifiers and reliable source citations across pipeline executions.

---

## 3. Corpus Evidence & Validation
* **Corpus Observations:** 
  - Testing against our 10-file corpus confirmed that while paragraph units provide precise retrieval, they risk fragmenting contextual continuity. 
  - To bridge this gap, we implemented a mandatory **Parent-Child Linkage Rule**, ensuring every child paragraph retains a `parent_id` pointing to its respective parent section hash, maintaining structural context without sacrificing search precision.
