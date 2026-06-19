A-DAP Core v1

Status

Core Architecture Document

Purpose

This document defines the minimum conceptual core of A-DAP.

Not every concept in the repository is required for A-DAP operation.

This document separates:

- Core Components
- Experimental Components
- Research Components

---

Core Principle

Commit Before Explain.

A decision claim must be committed before explanations are generated.

Verification precedes interpretation.

Contestability precedes trust.

---

Mandatory Components

Decision Envelope

A structured commitment describing:

- decision identifier
- timestamp
- policy/model version
- input commitment
- output commitment
- reconstruction instructions

The Decision Envelope is mandatory.

---

Independent Verification

A-DAP requires at least one externally verifiable path.

Self-attestation alone is insufficient.

---

NDC

Non-Dependency Count.

Measures independent verification paths after dependency collapse.

NDC is a core A-DAP construct.

---

Effective Contestability

Verification must remain exercisable in practice.

Theoretical access alone is insufficient.

---

Experimental Components

These concepts are compatible with A-DAP but are not required.

Effective NDC

Operational refinement of NDC.

Exercise Debt

Gap between theoretical and practical verification.

PCI

Provenance Contestability Index.

Measures contestability of provenance claims.

---

Research Components

Active research areas.

PAEC

Probabilistic Attribution under Evidential Constraints.

R²-PAEC

Revision and Reassessment PAEC.

Future Contestability Metrics

Additional metrics may be introduced without modifying the core architecture.

---

Governance Risks

The following risks are recognized by A-DAP:

- Adoption Capture Risk
- Verifier Funding Capture
- Provenance Concentration Collapse
- Self-Attested Materiality

---

Non-Goals

A-DAP is not:

- a fairness metric
- an explainability method
- a model benchmark
- a bias detector
- a governance certification

A-DAP focuses on verifiable contestability.

---

Stability Commitment

Future development should preserve:

- Decision Envelope
- Commit Before Explain
- Independent Verification
- NDC

These constitute the architectural core of A-DAP v1.
