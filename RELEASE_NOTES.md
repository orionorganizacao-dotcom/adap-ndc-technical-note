# Release Notes — A-DAP v0.4.0

Release: `v0.4.0`  
Project: A-DAP — Auditable Decision Accountability Protocol  
Status: Public externalization baseline  
Author: Ezio v.s. Santos  

---

## 1. Release Summary

A-DAP `v0.4.0` consolidates the repository around a narrower and more defensible claim:

A-DAP v0 externalizes the record.

It does not yet harden the record.

This release should be treated as the public externalization baseline after the project’s repositioning toward affected-party contestability, scope boundaries, independent verification topology, and explicit v0-to-v1 hardening targets.

It does not claim production readiness.

It does not claim high NDC.

It does not claim that the current proof of concept proves strong resistance to falsification.

---

## 2. Core Position

The central sentence of this release is:

```text
A high-impact automated decision should not merely be explained after the fact.

It should be born contestable.
```

In `v0.4.0`, A-DAP is framed as a contestability layer for high-impact automated decisions affecting people.

Its strongest current contribution is not general cryptographic audit-trail infrastructure.

Its contribution is the affected-party contestability framing:

```text
affected-party contestability
decision receipts as minimum contestability objects
NDC as a capture diagnostic
scope-completeness boundary
independent verification as topology
```

---

## 3. What v0.4.0 Demonstrates

A-DAP `v0.4.0` demonstrates a minimum contestability object:

```text
a citizen-held decision receipt emitted in a simulated decision flow
```

This proves a narrow claim:

```text
a decision record can leave the generator’s exclusive control
```

It does not yet prove:

```text
the record is hard to falsify
```

Under conservative assumptions, the current A-DAP v0 proof of concept should be treated as:

```text
A-DAP v0 NDC = 1
```

This is not treated as a failure.

It is treated as the honest baseline.

---

## 4. What v0.4.0 Does Not Claim

A-DAP `v0.4.0` does not prove:

```text
fairness
truth
legality
correctness
scope completeness
input truth
verifier independence
production readiness
high NDC
realized detection
resistance to total collusion
```

It also does not claim to replace existing cryptographic audit-trail, provenance, transparency-log, timestamping, Merkle-tree, or evidence-pack systems.

A-DAP should be read as a contestability layer that may complement such infrastructure.

---

## 5. Major Changes Since v0.3.1

### 5.1 README Repositioned

The root `README.md` was rewritten to clarify that A-DAP is not a competing audit-trail standard.

It now defines A-DAP as a contestability layer focused on whether the affected person can later reconstruct and challenge a specific automated decision against stable evidence.

### 5.2 Claims Narrowed

The project no longer frames itself as a broad cryptographic audit-trail framework.

It now distinguishes:

```text
record externalization
```

from:

```text
record hardening
```

This release claims the first.

It does not yet claim the second.

### 5.3 v0 Limit Made Explicit

The README now states that the current PoC demonstrates the minimum affected-party decision receipt but does not yet prove strong resistance to falsification.

### 5.4 Scope-Completeness Boundary Added

The repository now explicitly distinguishes:

```text
record integrity
```

from:

```text
scope completeness
```

A cryptographically valid envelope may still be incomplete if the operator controls what enters the envelope.

### 5.5 Independent Verification Topology Added

The repository now states that independent verification is not a label attached to a single verifier.

It is a topology of reconstruction outside the generator.

Multiple verifiers do not increase independence if they all depend on the same envelope, signer, custody path, API, or operator-defined scope.

### 5.6 Verification Topology Stress Test Added

The architecture now includes a stress-test note declaring that, under conservative assumptions, A-DAP v0 has NDC = 1.

This distinguishes the implemented v0 topology from future target topologies.

### 5.7 Decision Receipt PoC Consolidated

The minimal PoC under:

```text
examples/decision-receipt-poc/
```

demonstrates the minimum affected-party contestability object.

It includes adversarial scenarios for:

```text
non-issuance
split-view reconstruction
perfect bad decision
```

### 5.8 ROADMAP v0 to v1 Added

The repository now includes a roadmap for moving from v0 externalization toward v1 hardening.

The roadmap defines future work around:

```text
asymmetric signatures
external anchoring
scope validation
topology modeling
NDC computation
infrastructure collapse rules
detection activation
threshold custody
independent verifier distribution
```

### 5.9 Precedence Structure Added

The repository now includes a precedence structure under:

```text
precedence/
```

This supports attribution, timestamped existence, and integrity of the public research artifact.

---

## 6. Key Files in v0.4.0

Important files and folders include:

```text
README.md
ROADMAP.md
THREAT_MODEL.md
CONTRIBUTING.md
NOTICE.md
RELEASE_NOTES.md
QUICKSTART.md
architecture/
examples/decision-receipt-poc/
solver/
challenge/
proofs/
precedence/
```

Key architecture files include:

```text
architecture/envelope-bottleneck.md
architecture/automated-ndc-v2.md
architecture/input-provenance-boundary.md
architecture/commit-latency-tradeoff.md
architecture/signer-custody-boundary.md
architecture/scope-completeness-boundary.md
architecture/independent-verification-topology.md
architecture/example-verification-topology.md
architecture/cryptographic-habeas-data.md
architecture/vap-lap-gap-analysis.md
architecture/omega-plus-plus-reconstructible-verdicts.md
```

---

## 7. Current PoC Status

The current proof of concept demonstrates:

```text
a decision receipt can be emitted
a citizen can hold the receipt
a verifier can check the receipt structure
adversarial scenarios can expose limits
```

The current proof of concept does not yet implement:

```text
full NDC computation
external anchoring
threshold custody
real control-disjoint topology
scope validation
independent verifier distribution
real-world detection incentives
production-grade deployment
```

Therefore, `v0.4.0` should be treated as:

```text
externalization baseline
```

not:

```text
hardened evidentiary architecture
```

---

## 8. Conservative NDC Statement

Under conservative assumptions, A-DAP v0 should be treated as:

```text
A-DAP v0 NDC = 1
```

This applies especially where:

```text
the operator controls scope
the operator controls receipt generation
the operator controls verifier distribution
the operator controls signing
the operator controls delivery
the operator controls evidence infrastructure
```

Higher NDC values belong only to future target topologies that implement stronger separation.

---

## 9. v1 Direction

A-DAP v1 should begin hardening the record.

The roadmap defines the transition from:

```text
a receipt can exist outside the generator
```

to:

```text
the receipt, verifier, scope, custody, and anchor begin to separate into materially distinct control paths
```

The v1 target is not perfect proof.

The v1 target is measurable movement from record externalization toward control-disjoint verification topology.

---

## 10. Release Integrity and Precedence

This release is intended to be anchored through:

```text
GitHub tag
GitHub release
SHA-256 archive hash
precedence record
optional detached signature
optional external timestamp
```

Precedence artifacts are expected under:

```text
precedence/
```

Recommended files:

```text
precedence/PRECEDENCE-v0.4.0.md
precedence/A-DAP-v0.4.0-SHA256.txt
```

Future optional files may include:

```text
precedence/A-DAP-v0.4.0-SHA256.txt.asc
precedence/timestamp/A-DAP-v0.4.0.tsq
precedence/timestamp/A-DAP-v0.4.0.tsr
precedence/timestamp/A-DAP-v0.4.0-timestamp-receipt.json
```

---

## 11. Historical Note

The previous `v0.3.1` release organized the repository as a public technical architecture and reconstruction challenge.

The `v0.4.0` release supersedes that framing by adding a stricter boundary:

```text
A-DAP v0 externalizes the record.

It does not yet harden the record.
```

This release should be treated as the current baseline for public explanation, citation, and external review.

---

## 12. Final Release Sentence

A-DAP `v0.4.0` is not a claim of robustness.

It is a timestamped, inspectable, falsifiable baseline for affected-party contestability.

Its value is that it preserves a minimum contestable decision object while openly declaring what remains unimplemented.
