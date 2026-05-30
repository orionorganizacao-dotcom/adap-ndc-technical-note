# Release Notes — A-DAP v0.4.0

Release: `v0.4.0`  
Project: A-DAP — Auditable Decision Accountability Protocol  
Status: Public externalization baseline  
Author: Ezio v.s. Santos

---

## 1. Release Summary

A-DAP `v0.4.0` consolidates the repository as a public externalization baseline for the Auditable Decision Accountability Protocol.

This release establishes the minimum affected-party contestability object:

a citizen-held or affected-party-held decision receipt emitted in a simulated decision flow, designed to make later alteration, substitution, or inconsistency detectable under stated assumptions.

The release does not claim that A-DAP proves truth, fairness, legality, or accountability.

Its claim is narrower:

A-DAP can help create reconstructible decision evidence so that later contestation is possible.

---

## 2. Core Contribution

This release formalizes A-DAP as a protocol architecture for reconstructible decision evidence.

The central design principle is:

Automated decisions should not depend only on post-hoc explanation.

They should produce pre-committed evidentiary records that can later be reconstructed, tested, and contested.

A-DAP shifts the question from:

“Can the system explain itself?”

to:

“Can an external reviewer reconstruct what the system committed to at the time of decision?”

---

## 3. Externalization Baseline

The externalization baseline establishes that affected-party contestability requires more than internal logs.

A minimum externalization object should allow an affected party, reviewer, auditor, or institution to hold a receipt or reference that can later be checked against the committed decision record.

The release demonstrates the principle that:

Internal records are not enough.

A decision must produce an externalizable evidentiary object if later contestability is to be meaningful.

---

## 4. Added or Consolidated

This release consolidates the following repository areas:

- README.md
- RELEASE_NOTES.md
- NOTICE.md
- THREAT_MODEL.md
- CONTRIBUTING.md
- QUICKSTART.md
- proofs/README.md
- solver/README.md
- challenge/gcd-001/
- architecture/envelope-bottleneck.md
- architecture/automated-ndc-v2.md
- architecture/omega-plus-plus-reconstructible-verdicts.md
- architecture/adoption-capture-risk.md
- architecture/exercisable-verification-interface.md
- architecture/verifier-funding-capture.md
- architecture/ip-priority-and-authorized-execution.md

---

## 5. Clarified Claims

This release clarifies that A-DAP is not:

- a fairness metric
- an explainability method
- a model audit by itself
- a complete accountability system
- proof that a decision was correct
- proof that a decision was lawful
- proof that a decision was fair
- proof that an operator is responsible
- proof that verification will be exercised

The safe claim is:

A-DAP can help make later alteration or inconsistency detectable under stated assumptions.

---

## 6. Key Concepts Formalized

This release establishes or consolidates several core concepts:

- decision envelopes
- commit-before-explain
- reconstructible decision evidence
- affected-party-held receipts
- structural NDC
- dependency collapse
- envelope bottleneck
- effective contestability
- exercise debt
- adoption capture risk
- verifier funding capture
- exercisable verification interface
- reconstructible automated verdicts
- proof versus claim versus timestamp versus audit

---

## 7. Challenge Package

This release includes the `challenge/gcd-001/` package.

GCD-001 is an external reconstruction challenge based on the German Credit Dataset.

Its purpose is to test whether a third party can reconstruct a committed decision object using the provided specification and materials.

The challenge is not proof that A-DAP is complete.

It is a limited test of reconstructibility under defined conditions.

---

## 8. Safe Claim

A-DAP `v0.4.0` supports this narrow claim:

High-impact automated decisions should be born with a reconstructible evidentiary object, so that affected parties, auditors, regulators, courts, or reviewers can later contest a specific decision against a pre-committed record.

This does not prove that the original decision was true.

This does not prove that the original decision was fair.

This does not eliminate trust.

This does not guarantee detection.

This does not create accountability by itself.

---

## 9. Why This Matters

Most automated decision governance depends heavily on post-hoc artifacts:

- explanations
- logs
- model cards
- documentation
- operator statements
- dashboard outputs

These artifacts may be useful, but they do not necessarily prove what happened at the moment of decision.

A-DAP addresses that gap by treating decision evidence as a structured object that must exist before later dispute.

The release establishes the baseline for making that object externalizable.

---

## 10. Known Limitations

This release does not solve:

- total collusion
- false data at origin
- biased decision logic
- unfair policy design
- compromised infrastructure
- institutional refusal to act
- non-exercise of verification rights
- verifier capture
- adoption capture
- materiality self-attestation
- accountability by itself

These remain part of the threat model and future work.

---

## 11. Status

This is a public externalization baseline release.

It is not a production certification framework.

It is not a finished compliance product.

It is a structured technical note and adversarial review surface for testing whether automated decision records can become externally contestable.

---

## 12. Relationship to v0.4.1

A-DAP `v0.4.1` later adds the non-self-attested materiality limitation.

That later release clarifies that NDC is meaningful only under disclosed materiality assumptions and that self-declared materiality must not be treated as independent verification.

Therefore:

- `v0.4.0` establishes the externalization baseline.
- `v0.4.1` hardens the protocol by narrowing NDC and materiality claims.

---
