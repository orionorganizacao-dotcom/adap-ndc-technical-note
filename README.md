# A-DAP: Verifiability Architecture for Auditable Decisions

A-DAP — Auditable Decision Accountability Protocol — is an architectural protocol for making AI decision evidence independently reconstructible, falsifiable, and externally verifiable.

This repository is the main public technical access point for the A-DAP / NDC work.

It does not ask readers to trust the author.

It asks readers to inspect the evidence, reconstruct the decision-custody process, and test whether an alteration could remain undetected.

---

## Main Thesis

AI governance cannot rely only on explanations, logs, screenshots, dashboards, or after-the-fact documentation.

For high-impact AI systems, the central question is not only:

> “Why did the system make this decision?”

The harder question is:

> “Can an independent third party reconstruct and verify the evidence that existed at the moment the decision was made?”

A-DAP addresses this problem through a decision-custody architecture.

The protocol separates:

- decision input
- decision output
- decision envelope
- custody process
- verification evidence
- expected verdict
- oracle boundaries

The goal is not to prove that a decision was correct.

The goal is to make decision evidence independently reconstructible and structurally difficult to alter without detection.

---

## What A-DAP Claims

A-DAP does not claim that tampering is impossible.

A-DAP claims that undetected tampering should have a measurable structural cost.

A-DAP does not replace legal accountability, institutional review, or regulatory authority.

It provides a verifiability layer that can support them.

A-DAP does not require opening the internal model.

It focuses on the evidence surrounding a decision.

---

## Oracle Boundary

A-DAP does not claim to make AI decisions fully trustless.

Its verifiable core applies to decision records, not to decision truth.

This means A-DAP can independently verify artifacts such as:

- canonical decision envelopes
- hashes
- signatures
- timestamp anchors
- hash-chain integrity
- input hashes
- policy hashes
- externally published commitments
- deterministic record reconstruction

However, A-DAP does not prove by itself:

- that the input was true in the real world
- that the model actually executed the decision
- that the model state was real
- that the declared agent identity was institutionally valid
- that the policy was legally valid or in force
- that the explanation reflects real internal causality
- that the decision was correct, fair, or legitimate

These claims remain oracle-bound unless separately supported by external evidence.

In summary:

A-DAP makes decision records independently reconstructible as records.

It separates what can be cryptographically verified from what remains dependent on external oracles.

The correct claim is not that A-DAP proves decision truth.

The correct claim is that A-DAP proves what was committed about a decision, when it was committed, by which cryptographic key, and whether that commitment was altered after the fact.

---

## Current Public Challenge

The repository includes the **A-DAP Reconstruction Challenge — GCD-001**.

The challenge invites independent reviewers to reconstruct the GCD-001 decision-custody graph, compute or challenge the claimed Network Dependency Coefficient (NDC), and classify the result under one of three admissible outcomes:

- **R1 — Reproduction**
- **R2 — Falsification**
- **R3 — Structural Ambiguity**

This challenge is not designed to prove that A-DAP is correct.

It is designed to make the GCD-001 claim independently reconstructible, falsifiable, or correctable.

Key files:

- [`gcd-001-reconstruction-challenge.md`](gcd-001-reconstruction-challenge.md)  
  Defines the public reconstruction challenge, eligible outcomes, prize structure, acceptance mechanism, author non-voting rule, and submission requirements.

- [`gcd-001-reconstruction-spec.md`](gcd-001-reconstruction-spec.md)  
  Defines how an external verifier should reconstruct the GCD-001 decision-custody graph, compute or challenge the claimed NDC, and distinguish independent reconstruction from simple execution of author-provided scripts.

---

## Core Reconstruction Principle

```text
Do not trust the author.
Reconstruct the graph.
Compute the cut.
Challenge the NDC claim.
Declare the oracle boundary.
