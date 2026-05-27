# A-DAP: Auditable Decision Accountability Protocol

A-DAP is an architectural protocol for making AI decision evidence independently reconstructable, falsifiable, and externally verifiable.

This repository is the main public entry point for the A-DAP technical work.

It does not ask readers to trust the author.

It asks them to inspect the evidence, reconstruct the decision path, and test whether tampering can remain undetected.

---

## Core thesis

AI governance cannot rely only on explanations, logs, screenshots, or post-hoc documentation.

For high-impact AI systems, the central question is not only:

“Why did the system make this decision?”

The harder question is:

“Can an independent third party reconstruct and verify the evidence state that existed when the decision was made?”

A-DAP addresses this problem through decision custody architecture.

The protocol separates:

- decision input
- decision output
- decision envelope
- custody trail
- verification evidence
- expected verdict
- falsification attempts

The goal is not to prove that the decision was true.

The goal is to make the decision evidence independently reconstructable and structurally difficult to alter without detection.

---

## What A-DAP claims

A-DAP does not claim that tampering is impossible.

A-DAP claims that undetected tampering should have a measurable structural cost.

A-DAP does not replace legal accountability, institutional review, or regulatory authority.

It provides a verifiability layer that can support them.

A-DAP does not require opening the internal model.

It focuses on the evidence state surrounding a decision.

---

## Why this matters

Many AI governance approaches depend on internal logs, model explanations, audit reports, or institutional trust.

Those mechanisms can be useful, but they often remain inside the system or under the control of the same organization that produced the decision.

A-DAP is designed around a different principle:

Verification should not depend only on trusting the system that made the decision.

For high-risk AI, the evidence around a decision should be reconstructable outside the original system boundary.

---

## Repository status

Current public version:

```text
A-DAP Public Challenge v0.4
