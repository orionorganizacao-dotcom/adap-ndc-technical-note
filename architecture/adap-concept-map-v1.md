A-DAP Concept Map v1

Purpose

This document describes the conceptual architecture of A-DAP and the relationships between its principal constructs.

A-DAP is not a fairness framework, explainability method, or model evaluation benchmark.

A-DAP focuses on verification, contestability, provenance, attribution, and governance risks associated with opaque decision systems.

---

Layer 1 — Decision Contestability

Non-Dependency Count (NDC)

NDC measures the number of structurally independent verification paths available after dependency collapse.

Question addressed:

"How many independent ways exist to verify a decision claim?"

---

Effective NDC

Effective NDC extends NDC by incorporating practical exercisability constraints.

Question addressed:

"How many verification paths remain realistically usable?"

---

Exercise Debt

Exercise Debt measures the gap between theoretical and practical verification capability.

Question addressed:

"Can affected parties actually exercise their verification rights?"

---

Layer 2 — Provenance Contestability

Provenance Contestability Index (PCI)

PCI measures the degree to which provenance claims can be independently challenged.

Question addressed:

"Can independent parties contest the provenance of the decision record?"

---

Provenance Concentration Collapse

Occurs when nominally independent provenance paths share hidden dependencies.

Question addressed:

"Are provenance paths genuinely independent?"

---

Layer 3 — Attribution

PAEC

Probabilistic Attribution under Evidential Constraints.

PAEC evaluates the evidential support for causal attribution claims.

Question addressed:

"How justified is a claim that component X contributed to outcome Y?"

---

R²-PAEC

Revision and Reassessment PAEC.

Extends PAEC to support attribution revision under new evidence.

Question addressed:

"How should attribution confidence change when evidence changes?"

---

Layer 4 — Governance Risks

Non-Self-Attested Materiality

Materiality claims should not depend solely on the operator being evaluated.

---

Verifier Funding Capture

Independent verification may become compromised when financial dependencies emerge.

---

Adoption Capture Risk

A framework may become formally adopted while its core guarantees are weakened or bypassed.

---

Relationship Diagram

Decision
│
├── Verification
│ ├── NDC
│ ├── Effective NDC
│ └── Exercise Debt
│
├── Provenance
│ ├── PCI
│ └── Provenance Concentration Collapse
│
├── Attribution
│ ├── PAEC
│ └── R²-PAEC
│
└── Governance
├── Non-Self-Attested Materiality
├── Verifier Funding Capture
└── Adoption Capture Risk

---

Core Principle

Commit Before Explain.

Verification precedes interpretation.

Contestability precedes trust.

Independence precedes assurance.
