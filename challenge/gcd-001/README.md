# A-DAP: Auditable Decision Accountability Protocol

A-DAP is an architectural protocol for making AI decision evidence independently reconstructible, falsifiable, and externally verifiable.

This repository is the main public technical access point for A-DAP/NDC work.

It does not ask readers to trust the author.

It asks them to inspect the evidence, reconstruct the decision-custody process, and test whether undetected alteration has a measurable structural cost.

---

## Main Thesis

AI governance cannot rely only on explanations, logs, screenshots, dashboards, or after-the-fact documentation.

For high-impact AI systems, the central question is not only:

```text
Why did the system make this decision?
```

The harder question is:

```text
Can an independent third party reconstruct and verify the evidence that existed when the decision was made?
```

A-DAP addresses this problem through a decision-custody architecture.

The protocol separates:

- decision input;
- decision output;
- decision envelope;
- custody graph;
- verification evidence;
- expected verdict;
- oracle boundaries.

The objective is not to prove that a decision was correct.

The objective is to make the evidence surrounding a decision independently reconstructible and structurally difficult to alter without detection.

---

## What A-DAP Claims

A-DAP does not claim that tampering is impossible.

A-DAP claims that undetected tampering should have a measurable structural cost.

A-DAP does not replace legal responsibility, institutional review, regulatory authority, or human accountability.

It provides a verification layer that can support them.

A-DAP does not require opening the internal model.

It focuses on the evidence structure surrounding a decision.

---

## What A-DAP Does Not Claim

A-DAP does not prove by itself:

- that the original decision was true;
- that the original decision was fair;
- that the original decision was lawful;
- that the input was true in the real world;
- that the model actually executed the decision;
- that the declared model state was real;
- that the declared agent identity was institutionally valid;
- that the policy was legally valid or in force;
- that the explanation reflects real internal causality.

These claims remain oracle-bound unless separately supported by external evidence.

A-DAP separates what can be verified cryptographically from what still depends on external institutions, witnesses, systems, or real-world facts.

---

## Core Principle

```text
Do not trust the author.
Reconstruct the graph.
Compute the cut.
Challenge the NDC claim.
Declare the oracle boundary.
```

---

## Key Concepts

### Decision Envelope

A structured pre-action or action-bound record containing decision-relevant artifacts.

A decision envelope may include references to:

- inputs;
- outputs;
- policies;
- model references;
- hashes;
- signatures;
- timestamps;
- custody declarations;
- expected verdicts.

The envelope is not automatically proof of decision truth.

It is a structured object for reconstruction.

---

### Custody Graph

A graph representing dependency, control, evidence, and alteration paths around a decision claim.

The custody graph helps reviewers inspect which parts of the evidence structure would need to be altered to change the claim without detection.

---

### Network Dependency Coefficient — NDC

NDC is a structural dependency measure computed from the minimum sufficient vertex-cut required to alter a decision-custody graph without detection by the verifier.

In simplified form:

```text
NDC = minimum sufficient vertex-cut for undetected alteration
```

A higher NDC may indicate that undetected alteration requires compromising more independent parts of the custody structure.

A lower NDC may indicate an evidence bottleneck, weak custody structure, or excessive dependency on a single authority.

NDC is not a full governance score.

It is a structural measure for a specific custody claim.

---

### Oracle Boundary

The oracle boundary separates what can be independently reconstructed from the published artifacts from what depends on external truth sources.

A-DAP may help verify:

- canonical envelopes;
- hashes;
- signatures;
- timestamp anchors;
- hash-chain integrity;
- policy hashes;
- custody declarations;
- graph declarations;
- externally published commitments;
- deterministic reconstruction paths.

A-DAP does not by itself verify:

- real-world truth;
- fairness;
- legality;
- legitimacy;
- institutional authority;
- internal model causality.

---

## Repository Status

This repository currently contains the technical scaffold for A-DAP/NDC reconstruction work.

Current status:

```text
Technical notes: available
Synthetic case: available
GCD-001 external reconstruction package: available
External disjoint reconstruction: pending
Acceptance Committee: not yet appointed
Public bounty: not yet active
Submission channel: not yet open
```

No claim in this repository should be interpreted as independently validated unless it has been reviewed by external parties under published review rules.

---

## Repository Structure

```text
.
├── README.md
├── technical-note-v0.3.1.md
├── references.md
├── oracle-boundary.md
├── oracle-boundary-short.md
├── architecture/
├── examples/
├── proofs/
├── solver/
└── challenge/
    ├── README.md
    ├── ROADMAP.md
    ├── attacks/
    │   └── attack-template.md
    ├── synthetic-case/
    │   ├── README.md
    │   ├── input.json
    │   ├── output.json
    │   ├── envelope.json
    │   ├── custody.json
    │   ├── expected-verdict.json
    │   ├── run.md
    │   ├── verify_synthetic_case.py
    │   └── tampered/
    └── gcd-001/
        ├── README.md
        ├── reconstruction-spec.md
        ├── reconstruction-challenge.md
        ├── submission-template.md
        └── reviewer-guidelines.md
```

---

## Main Technical Notes

### `technical-note-v0.3.1.md`

Main technical note defining the A-DAP/NDC framing, including:

- decision custody;
- structural verifiability;
- NDC;
- detectability boundaries;
- limitations;
- oracle-bound claims.

---

### `oracle-boundary.md`

Defines what A-DAP can independently reconstruct and what remains dependent on external oracles by design.

This distinction is central.

A-DAP does not claim to make AI decisions fully trustless.

Its verifiable core applies to decision records and custody evidence, not to decision truth itself.

---

### `oracle-boundary-short.md`

Short English version of the oracle-boundary note for external reviewers.

Useful for quick review, outreach, and challenge participants.

---

## Public Challenge Area

The `challenge/` directory contains public reconstruction materials.

Its purpose is to expose A-DAP/NDC claims to external testing rather than author-controlled validation.

The challenge area separates two different things:

```text
Synthetic Case = executable demonstration
GCD-001 = external reconstruction target
```

They must not be treated as the same thing.

---

## Synthetic Case

Location:

```text
challenge/synthetic-case/
```

The synthetic case is a controlled demonstration.

It shows how A-DAP-style evidence can be represented, verified, and tamper-tested.

It includes:

- input artifact;
- output artifact;
- decision envelope;
- custody declaration;
- expected verdict;
- tampered examples;
- one-command Python verifier.

The synthetic case is useful for demonstrating workflow mechanics.

It is not independent adversarial validation because it was designed by the author.

---

## GCD-001 External Reconstruction Package

Location:

```text
challenge/gcd-001/
```

GCD-001 is the first public A-DAP/NDC external reconstruction target.

It is not a synthetic demonstration.

It is a candidate public reconstruction package prepared for independent adversarial review.

The purpose of GCD-001 is to test whether a published decision-custody/NDC claim can be:

- independently reproduced;
- constructively falsified;
- shown to be structurally ambiguous.

Current status:

```text
External disjoint reconstruction: pending
Acceptance Committee: not yet appointed
Public bounty: not yet active
Submission channel: not yet open
```

No result in `challenge/gcd-001/` should be described as independently validated until reviewed by external parties under published challenge rules.

---

## GCD-001 Files

```text
challenge/gcd-001/
├── README.md
├── reconstruction-spec.md
├── reconstruction-challenge.md
├── submission-template.md
└── reviewer-guidelines.md
```

### `challenge/gcd-001/README.md`

Explains the purpose, scope, current status, review path, admissible outcomes, oracle boundary, and minimal honest claim for GCD-001.

### `challenge/gcd-001/reconstruction-spec.md`

Defines how an external verifier should reconstruct the GCD-001 decision-custody graph and compute or challenge the claimed NDC.

### `challenge/gcd-001/reconstruction-challenge.md`

Defines the planned public challenge structure, admissible outcomes, prize logic, acceptance committee model, author non-voting rule, and disclosure standard.

### `challenge/gcd-001/submission-template.md`

Provides the standard format for external reviewers submitting R1, R2, or R3 results.

### `challenge/gcd-001/reviewer-guidelines.md`

Provides evaluation guidance for independent reviewers and future committee members.

---

## Admissible GCD-001 Outcomes

GCD-001 accepts three useful outcomes.

### R1 — Reproduction

The claimed NDC is independently reproduced under the published specification.

Honest claim:

```text
The specific GCD-001 NDC claim was reproduced under the published specification.
```

R1 does not validate A-DAP as a whole.

---

### R2 — Falsification

The claimed NDC is shown to be incorrect through a constructive demonstration.

Examples:

- smaller valid vertex-cut;
- invalid graph edge;
- invalid vertex classification;
- omitted dependency path;
- oracle-bound claim incorrectly counted as verified;
- incorrect NDC calculation.

Honest claim:

```text
The GCD-001 NDC claim was falsified through a constructive demonstration.
```

R2 is not a failure of the review process.

It is a successful adversarial finding.

---

### R3 — Structural Ambiguity

The specification is incomplete or ambiguous enough to prevent deterministic reconstruction.

Examples:

- ambiguous canonicalization;
- missing artifacts;
- undefined graph vertices;
- undefined graph edges;
- unclear A/V role assignment;
- unclear detection condition;
- unclear alteration condition;
- unstable oracle-boundary classification.

Honest claim:

```text
The GCD-001 specification requires correction before deterministic reconstruction is possible.
```

R3 improves the specification.

---

## Independent Implementation Requirement

For adversarial reconstruction, reviewers must not rely on author-controlled tools as the primary computation path.

The author’s tools may be used only for secondary comparison after independent reconstruction.

A valid reconstruction should be inspectable, reproducible, and independent of author authority.

A valid reconstruction must not depend on:

- author’s solver;
- author’s scripts;
- expected outputs generated by the author;
- private infrastructure;
- undocumented author intent;
- manually asserted conclusions.

This requirement exists to prevent self-validation.

---

## What Counts as Progress

Progress does not mean only confirmation.

The following outcomes all improve the protocol:

```text
R1 — reproduction
R2 — falsification
R3 — structural ambiguity
```

A-DAP/NDC becomes stronger when claims can be reconstructed, corrected, or falsified under public rules.

The worst outcome is not falsification.

The worst outcome is untestable self-confirmation.

---

## Minimal Honest Claim

The minimal honest claim for this repository is:

```text
A-DAP is a protocol architecture for making decision evidence independently reconstructible as evidence.
```

It does not prove decision truth.

It does not eliminate the need for legal, institutional, or regulatory authority.

It does not ask for trust.

It asks for reconstruction.

---

## Recommended Review Path

For external reviewers:

1. Read this README.
2. Read `oracle-boundary.md`.
3. Read `technical-note-v0.3.1.md`.
4. Inspect `challenge/synthetic-case/`.
5. Inspect `challenge/gcd-001/README.md`.
6. Read `challenge/gcd-001/reconstruction-spec.md`.
7. Read `challenge/gcd-001/reconstruction-challenge.md`.
8. Use `challenge/gcd-001/submission-template.md` if preparing a submission.
9. Use `challenge/gcd-001/reviewer-guidelines.md` if evaluating a submission.

Reviewer posture:

```text
Do not trust the author.
Reconstruct the graph.
Compute the cut.
Challenge the NDC claim.
Declare the oracle boundary.
```

---

## Current Limitations

This repository is still in an early public technical stage.

Known limitations:

- external disjoint reconstruction is pending;
- no Acceptance Committee has been appointed;
- no public bounty is active;
- no formal submission channel is open;
- synthetic examples are controlled demonstrations;
- GCD-001 has not yet been independently accepted as R1, R2, or R3;
- NDC is a structural metric, not a complete governance theory;
- A-DAP verifies evidence structure, not decision truth.

These limitations are part of the protocol’s honest boundary.

---

## Public Disclosure Standard

Any future public review summary should disclose:

- number of submissions received;
- number of administratively valid submissions;
- number of accepted R1 outcomes;
- number of accepted R2 outcomes;
- number of accepted R3 outcomes;
- committee members;
- unresolved ambiguities;
- specification changes triggered by review.

No result should be described as full validation of A-DAP.

---

## Empty Challenge Clause

If no valid external reconstruction is submitted, the challenge does not validate GCD-001.

Silence is not confirmation.

An empty challenge means only:

```text
No qualifying external reconstruction was submitted during the review period.
```

Further outreach, workshop review, expert review, or independent audit may still be required.

---

## Project Direction

The immediate goal is not commercialization.

The immediate goal is adversarial reconstruction.

Priority sequence:

1. complete public reconstruction materials;
2. invite external reviewers;
3. obtain R1, R2, or R3 outcomes;
4. correct the specification based on adversarial findings;
5. only then discuss institutional deployment.

The protocol gains legitimacy by surviving independent reconstruction pressure, not by author assertion.

---

## Final Principle

A-DAP is not a claim that AI decisions become automatically trustworthy.

A-DAP is a claim that decision evidence can be structured so that third parties can reconstruct what was committed, when it was committed, under which declared custody structure, and where the oracle boundary begins.

```text
Do not trust the author.
Reconstruct the evidence.
```
