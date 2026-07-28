# Chapai Intel RAG System - Retrieval Contract

## 1. Scope
This system acts as a specialized, localized intelligence engine designed to provide accurate answers exclusively about Chapainawabganj (history, geography, economy, and culture) based on verified local documents.

## 2. Sources
- Corpus files located in the `corpus/` directory (e.g., historical texts, economic data, local documentation).
- Curated golden dataset (`questions.jsonl`).

## 3. Freshness SLA
- Corpus data is statically maintained and manually updated as local insights evolve.

## 4. Provenance Requirement
- Every generated answer must explicitly trace back to its originating source file in the `corpus/` directory. Hallucinated or external web assumptions without grounding are strictly prohibited.

## 5. Out-of-Scope Questions
- Queries unrelated to Chapainawabganj, technical coding questions, or general world knowledge outside the local corpus scope will be rejected by the system's boundary rules.
