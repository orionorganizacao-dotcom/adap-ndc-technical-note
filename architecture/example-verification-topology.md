# Example Verification Topology — Stress Test

This document defines an adversarial stress test for A-DAP verification topology.

It should not be read as a proof that A-DAP v0 is robust.

The purpose is the opposite:

to identify where A-DAP v0 still collapses under conservative assumptions.

The central result is intentionally uncomfortable:

> Under conservative assumptions, the current A-DAP v0 PoC has NDC = 1 for both post-commit alteration and scope capture.

That result does not invalidate the project.

It defines the current boundary between:

- a minimal contestability object; and
- a hardened verification architecture.

A-DAP v0 externalizes the record.

It does not yet harden the record.

---

## 1. Purpose

The current Decision Receipt PoC demonstrates that an affected person can hold a decision receipt outside the generator.

That is important.

But it is not enough to claim high resistance to falsification.

The current PoC does not yet implement:

- full NDC computation;
- external anchoring;
- threshold custody;
- control-disjoint verifier paths;
- complete scope validation;
- independent delivery infrastructure;
- real multi-party verification topology;
- detection activation incentives.

Therefore, this document stress-tests the gap between what A-DAP v0 demonstrates and what the target architecture would need to demonstrate.

---

## 2. Core Distinction

The key distinction is:

> A-DAP v0 proves that a record can exist outside the generator.

It does not yet prove that the record is hard to falsify.

Those are different claims.

A citizen-held receipt is the minimum contestability object.

It creates an object that can later be presented, compared, or challenged.

But if receipt delivery, verifier code, signing, scope definition, and storage remain under operator control, then the architecture may still collapse to NDC = 1.

The current PoC should therefore be described as:

> minimum affected-party contestability, not hardened evidentiary resistance.

---

## 3. Conservative Assumptions

This stress test uses conservative assumptions.

A control domain collapses when two nodes are materially controlled by the same actor, infrastructure, credential, deployment pipeline, or administrative boundary.

For example:

- a verifier hosted by the operator is not independent;
- a receipt delivered only through the operator portal is not independently delivered;
- a public anchor controlled through the operator cloud account is not fully disjoint;
- a KMS key invoked only by the operator is not external custody;
- a verifier downloaded only from the operator repository may still be operator-controlled;
- multiple verifiers using the same envelope and API may still represent one trust path.

This is the conservative rule:

> If two nodes share a material control vector, they collapse into one trust domain.

Under that rule, A-DAP v0 remains weak.

---

## 4. Implemented v0 Topology

The current PoC topology can be modeled as:

```text
O = Operator / demo system
S = Scope definition
E = Envelope / receipt builder
K = Demo signing mechanism
R = Citizen-held receipt
V = Verifier script
P = Affected party
