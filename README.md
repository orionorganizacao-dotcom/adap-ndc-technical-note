# A-DAP: Verifiability Architecture for Auditable Decisions

**A-DAP** — **Auditable Decision Accountability Protocol** — is a structural approach for making high-stakes automated decisions externally reconstructible, independently challengeable, and resistant to post-hoc manipulation.

This repository is the **public technical home of A-DAP**.

It does not ask readers to trust the author, the model, the log, or the institution operating the system.

It provides a layered structure for:

- technical analysis;
- reconstruction challenges;
- attack templates;
- proof material;
- architectural objections;
- independent review.

The central claim is simple:

> Auditability is not a report generated after a decision.  
> Auditability is an architectural condition that must exist before the decision can be trusted.

---

## 1. Problem Statement

Modern AI and automated decision systems often produce decisions, logs, explanations, and internal records inside the same operational boundary.

This creates a structural problem:

> the same system that decides may also record, explain, and validate its own decision.

When this happens, auditability becomes fragile.

A system may appear documented while still being externally unverifiable.

A-DAP addresses this problem by separating:

- the decision;
- the evidence of the decision;
- the reconstruction path;
- the verification boundary;
- the challenge process.

The goal is not blind transparency.

The goal is **independent reconstruction**.

---

## 2. Core Thesis

A-DAP is based on the following thesis:

> A decision cannot be considered meaningfully auditable if the only party capable of reconstructing its evidentiary path is the same system or institution that produced it.

In practical terms:

- logs are not enough;
- explanations are not enough;
- screenshots are not enough;
- internal dashboards are not enough;
- self-attestation is not enough.

A decision becomes auditable only when an external party can reconstruct, inspect, challenge, or falsify the evidentiary path under defined conditions.

---

## 3. What This Repository Contains

This repository is organized as a layered technical structure.

```text
adap-ndc-technical-note/
├── architecture/
├── challenge/
├── examples/
├── proofs/
├── solver/
├── README.md
├── references.md
├── technical-note-v0.3.1.md
├── oracle-boundary.md
└── oracle-boundary-short.md
