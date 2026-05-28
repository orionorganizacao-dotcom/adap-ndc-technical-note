# A-DAP — Auditable Decision Accountability Protocol

A-DAP is an architectural protocol for making automated decisions more externally verifiable.

It does not claim that a system is trustworthy because the system says so.

It focuses on a narrower and harder problem:

How can a third party reconstruct whether a decision was committed, recorded, and verified under declared assumptions, without relying only on post-hoc explanations or internal logs?

A-DAP treats auditability as an architectural property, not as a documentation layer added after the fact.

---

## Core Thesis

Modern AI and automated decision systems often collapse decision, record, explanation, and verification into the same operational boundary.

That creates a structural risk:

The system that makes the decision may also become the system that explains, records, and validates the decision.

A-DAP addresses this by separating:

- decision;
- record;
- justification;
- verification;
- reconstruction;
- external audit boundary.

The goal is not to prove that every decision is correct.

The goal is to make the decision process more reconstructible, falsifiable, and externally inspectable.

---

## What A-DAP Is

A-DAP is a protocol for structuring decision evidence.

It is designed to help answer questions such as:

- Was the decision state committed before the action?
- Can the evidence package be reconstructed?
- Are claims, logs, timestamps, and proofs clearly separated?
- Can an external auditor verify the declared artifacts?
- Where does trust still remain inside the system?
- Which parts are externally verifiable and which parts are only asserted?

A-DAP is especially relevant for high-stakes or regulated contexts where automated decisions affect rights, risk, access, safety, or institutional accountability.

---

## What A-DAP Is Not

A-DAP is not:

- a guarantee of truth;
- a guarantee of correctness;
- a guarantee of ethical behavior;
- a replacement for law, regulation, or institutional accountability;
- a claim that all trust can be eliminated;
- a claim that logs are proof;
- an automated certification engine;
- a claim that internal verification is the same as external audit.

A-DAP does not produce accountability by itself.

It produces conditions that can support accountability by making decision evidence more reconstructible and externally testable.

---

## Core Distinction

A-DAP separates four concepts that are often confused:

```text
claim ≠ evidence
evidence ≠ proof
logs ≠ auditability
explanation ≠ reconstruction
