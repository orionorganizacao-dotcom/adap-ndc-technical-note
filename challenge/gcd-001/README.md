# GCD-001 External Reconstruction Package

This directory contains the external reconstruction package for **GCD-001**, the first public A-DAP/NDC reconstruction target.

GCD-001 is not a synthetic demonstration.

It is a candidate public reconstruction package prepared for independent adversarial review.

Until external reviewers are named and submissions are evaluated by a non-author committee, no result in this directory should be described as independently validated.

---

## Current Status

Status: **candidate external reconstruction package**.

External disjoint reconstruction: **pending**.

Acceptance Committee: **not yet appointed**.

Public bounty: **not yet active**.

Submission channel: **not yet open**.

No claim in this directory should be interpreted as independently validated until reviewed by external parties under published challenge rules.

This repository currently prepares the materials required for external review.

It does not yet claim that such review has occurred.

---

## Purpose

The purpose of this directory is to expose the GCD-001 custody/NDC claim to external reconstruction pressure.

External reviewers will be invited to:

- reconstruct the GCD-001 decision-custody graph;
- inspect the declared evidence structure;
- compute or challenge the claimed Network Dependency Coefficient (NDC);
- identify oracle-bound claims;
- detect specification ambiguity;
- submit one of three admissible outcomes: R1, R2, or R3.

The goal is not to prove that A-DAP is correct.

The goal is to make the GCD-001 claim independently reconstructible, falsifiable, or correctable.

At the current stage, this package is prepared for external reconstruction, but the formal challenge is not yet active.

---

## Core Principle

```text
Do not trust the author.
Reconstruct the graph.
Compute the cut.
Challenge the NDC claim.
Declare the oracle boundary.
```

A valid reconstruction must not depend on the author’s authority.

A valid reconstruction must be inspectable, reproducible, and independent of author-controlled tools for the primary computation path.

---

## What GCD-001 Is

GCD-001 is a decision-custody reconstruction case.

It focuses on the evidence structure surrounding a decision claim, not on whether the original decision was true, fair, lawful, or correct.

GCD-001 asks whether a third party can reconstruct the custody graph and evaluate the claimed NDC using the published specification.

The relevant question is:

```text
Can the published GCD-001 NDC claim be independently reproduced, falsified, or shown to be structurally underspecified?
```

---

## What GCD-001 Is Not

GCD-001 is not:

- proof that the original decision was correct;
- proof that the original decision was fair;
- proof that the original decision was lawful;
- proof that the dataset was morally or legally appropriate;
- proof that A-DAP as a whole is validated;
- proof that NDC alone is a complete governance metric;
- proof that record integrity equals decision truth;
- proof that external adversarial review has already occurred.

GCD-001 tests a narrower claim:

```text
whether a published decision-custody/NDC claim can be independently reconstructed, challenged, or shown to be underspecified.
```

---

## Directory Structure

Recommended structure for this directory:

```text
challenge/gcd-001/
├── README.md
├── reconstruction-spec.md
├── reconstruction-challenge.md
├── submission-template.md
└── reviewer-guidelines.md
```

### Files

- `README.md`  
  Explains the purpose, status, scope, review path, and interpretation of GCD-001.

- `reconstruction-spec.md`  
  Defines how an external verifier should reconstruct the GCD-001 decision-custody graph and compute or challenge the claimed NDC.

- `reconstruction-challenge.md`  
  Defines the planned public challenge rules, admissible outcomes, prize structure, acceptance mechanism, and author non-voting rule.

- `submission-template.md`  
  Provides a standard format for external reviewers submitting R1, R2, or R3 results.

- `reviewer-guidelines.md`  
  Provides evaluation guidance for independent reviewers and future acceptance committee members.

---

## Relationship to the Synthetic Case

The synthetic case and GCD-001 serve different purposes.

```text
Synthetic Case = executable demonstration
GCD-001 = external reconstruction target
```

The synthetic case is controlled by the author and exists to demonstrate the reconstruction and tamper-detection workflow.

GCD-001 is the external reconstruction target. It exists to test whether the published custody/NDC claim can survive independent reconstruction pressure.

The synthetic case must not be used as independent validation of A-DAP.

GCD-001 must not be reduced to simply running author-provided scripts.

---

## Admissible Review Outcomes

External reviewers must classify their result as one of three admissible outcomes.

At the current stage, these outcomes define the intended review structure.

They do not imply that submissions are already open or that any outcome has been accepted.

---

### R1 — Reproduction

The claimed NDC is independently reproduced under the published specification.

R1 means:

```text
The specific GCD-001 NDC claim was reproduced under the published specification.
```

R1 does not mean:

- the original decision was true;
- the original decision was fair;
- the original decision was lawful;
- A-DAP as a whole is validated.

R1 is useful because it shows that the published claim can be independently reconstructed under the stated rules.

---

### R2 — Falsification

The claimed NDC is shown to be incorrect.

A valid R2 submission must provide a constructive demonstration, such as:

- a smaller valid vertex-cut;
- an invalid edge assumption;
- an invalid vertex classification;
- an oracle-bound claim incorrectly counted as verified;
- a graph reconstruction that contradicts the claimed NDC;
- an error in the NDC calculation method;
- a dependency path omitted by the published graph.

R2 is structurally valuable because falsification improves the protocol.

If GCD-001 is falsified, the result should be treated as a successful adversarial finding, not as a failure of the review process.

---

### R3 — Structural Ambiguity

The specification is incomplete or ambiguous enough to prevent deterministic reconstruction.

A valid R3 submission must identify the missing or unstable part of the specification and show how it affects at least one of the following:

- the custody graph;
- the graph vertices;
- the graph edges;
- the A/V role assignment;
- the minimum vertex-cut;
- the NDC estimate;
- the oracle-boundary classification;
- the reconstruction process.

R3 is useful because it identifies where the specification must become more precise.

If GCD-001 produces R3, the proper response is specification correction, not rhetorical defense.

---

## Independent Implementation Requirement

For GCD-001, reviewers must not rely on the author’s solver, scripts, expected outputs, private infrastructure, or manually asserted conclusions for the primary reconstruction.

The author’s tools may be used only for secondary comparison after the reviewer has independently reconstructed the graph and computed the relevant cut.

A valid reconstruction must be executable, inspectable, or reproducible without privileged access to the author.

This requirement exists to prevent the challenge from becoming a self-check performed through author-controlled tools.

---

## Prohibited Primary Dependencies

The primary reconstruction must not depend on:

- the author’s solver;
- the author’s scripts;
- expected output files generated by the author;
- private infrastructure controlled by the author;
- undocumented assumptions;
- manually asserted conclusions by the author.

Use of author-provided tools for comparison after independent reconstruction is allowed, but must be disclosed.

---

## Required Reviewer Deliverables

A valid GCD-001 submission should include:

1. **Declared outcome**  
   The submission must clearly declare one of:

   - R1 — Reproduction
   - R2 — Falsification
   - R3 — Structural Ambiguity

2. **Reconstruction code**  
   Code may be written in any programming language.  
   It must not use the author’s solver as the primary computation path.

3. **Graph representation**  
   The reconstructed graph may be submitted as JSON, CSV, DOT, GraphML, Mermaid, an image, or another inspectable format.

4. **Min-cut calculation memo**  
   The reviewer must explain how the graph was modeled and how the minimum vertex-cut was computed.

5. **Oracle-boundary analysis**  
   The reviewer must identify claims that cannot be independently reconstructed from the published artifacts.

6. **Technical note**  
   A 2–5 page document explaining the result and reasoning.

7. **Reproducibility instructions**  
   The reviewer must provide instructions sufficient for an independent party or committee to inspect, run, or reproduce the submission.

8. **Independence declaration**  
   The reviewer must disclose whether any author-provided tools were used, and if so, whether they were used only for secondary comparison.

These deliverables define the intended submission standard.

Formal submission is not open until the public challenge notice defines the submission channel, review period, and committee members.

---

## Oracle Boundary

A-DAP does not make decision truth fully trustless.

Its verifiable core applies to decision records, not to decision truth.

A-DAP can help verify artifacts such as:

- canonical decision envelopes;
- hashes;
- signatures;
- timestamp anchors;
- hash-chain integrity;
- input hashes;
- policy hashes;
- custody declarations;
- graph declarations;
- externally published commitments;
- deterministic reconstruction paths.

However, A-DAP does not prove by itself:

- that the input was true in the real world;
- that the model actually executed the decision;
- that the model state was real;
- that the declared agent identity was institutionally valid;
- that the policy was legally valid or in force;
- that the explanation reflects real internal causality;
- that the decision was correct, fair, or legitimate.

These claims remain oracle-bound unless separately supported by external evidence.

---

## What Reviewers Must Not Assume

Reviewers must not assume:

- the author’s NDC is correct;
- the author’s solver is authoritative;
- the expected output is proof;
- oracle-bound claims are structurally verified;
- record integrity equals decision truth;
- hash integrity equals semantic correctness;
- timestamp presence equals independent reconstruction;
- reconstruction success validates A-DAP as a whole;
- a synthetic-case verifier proves the GCD-001 claim;
- publication in this repository means independent validation.

The expected reviewer posture is:

```text
skeptical by default
```

---

## NDC Calculation

NDC is computed as the minimum sufficient vertex-cut required to alter the decision-custody graph without detection by the verifier.

A reviewer must explicitly state:

- the graph model used;
- the source and target conditions;
- which vertices are included in the cut;
- why the cut is sufficient;
- why a smaller cut is not sufficient;
- which claims are reconstructible;
- which claims remain oracle-bound.

If the reviewer finds a smaller valid cut than the claimed one, the result may qualify as R2.

If the reviewer cannot determine the cut because the graph or specification is ambiguous, the result may qualify as R3.

---

## Failure Conditions

The reconstruction may fail if:

- canonicalization is ambiguous;
- artifacts are missing;
- hashes do not match;
- graph vertices are undefined;
- graph edges are undefined;
- A/V roles are unclear;
- oracle-bound claims are counted as verified;
- the verifier cannot independently reproduce the NDC reasoning;
- the claimed NDC depends on author-controlled tools;
- the specification permits more than one materially different reconstruction.

Failure is not automatically negative.

A failed reconstruction may indicate that the specification is incomplete, ambiguous, or dependent on unstated assumptions.

---

## Acceptance Committee

No Acceptance Committee has been publicly appointed yet.

Until such committee is named, no submission should be described as independently accepted.

The intended committee structure is:

- three publicly named external reviewers;
- no voting power for the protocol author;
- skeptical interpretation prevails in case of disagreement.

The committee should evaluate whether a submission qualifies as:

- R1 — Reproduction;
- R2 — Falsification;
- R3 — Structural Ambiguity;
- invalid or incomplete.

The author may perform administrative completeness checks, but should not decide technical acceptance.

---

## Author Non-Voting Rule

The protocol author has no voting power over acceptance decisions.

This rule becomes operational only after an independent Acceptance Committee is publicly appointed.

The author may clarify:

- file locations;
- repository structure;
- submission logistics;
- published definitions;
- administrative completeness.

The author must not decide whether a technical claim is accepted.

This rule exists to prevent adversarial validation from becoming self-validation with extra steps.

---

## Administrative Validity Check

Before committee review, a submission may be checked for administrative completeness.

A submission is administratively valid if it includes:

- declared outcome: R1, R2, or R3;
- reconstruction code;
- graph representation;
- min-cut calculation memo;
- oracle-boundary analysis;
- 2–5 page technical note;
- reproducibility instructions;
- independence declaration.

Administrative validity does not imply technical acceptance.

At the current stage, this section defines the intended administrative standard.

It does not mean that formal submissions are already open.

---

## Public Bounty Status

Public bounty status: **not yet active**.

Any prize structure described in `reconstruction-challenge.md` should be interpreted as a proposed or planned challenge mechanism until a formal public notice defines:

- opening date;
- closing date;
- prize values;
- submission channel;
- committee members;
- review procedure;
- payment conditions;
- public disclosure procedure.

No bounty should be considered active until these conditions are published.

---

## Public Disclosure

When the formal challenge is active and completed, the repository should disclose:

- number of submissions received;
- number of administratively valid submissions;
- number of accepted R1 outcomes;
- number of accepted R2 outcomes;
- number of accepted R3 outcomes;
- committee decision summary;
- unresolved ambiguities;
- specification changes triggered by the challenge.

No result should be described as full validation of A-DAP.

---

## Empty Challenge Clause

If no valid external reconstruction is submitted, the challenge does not validate the GCD-001 claim.

It only means that no qualifying external reconstruction was submitted within the challenge period.

A future challenge, direct outreach, workshop review, or independent audit may still be required.

Silence must not be represented as confirmation.

---

## Minimal Honest Claim

GCD-001 is not a proof of decision truth.

It is a test of whether a published decision-custody claim can be independently reconstructed, challenged, or shown to be underspecified.

A successful R1 result means:

```text
The NDC claim was reproduced under the published specification.
```

A successful R2 result means:

```text
The NDC claim was falsified.
```

A successful R3 result means:

```text
The specification requires correction before the claim can be deterministically evaluated.
```

All three outcomes are structurally useful.

At the current stage, no R1, R2, or R3 result has been independently accepted.

---

## Recommended Review Path

For external reviewers:

1. Read this README.
2. Read `reconstruction-spec.md`.
3. Read `reconstruction-challenge.md`.
4. Inspect the published GCD-001 artifacts.
5. Reconstruct the custody graph independently.
6. Compute or challenge the claimed NDC.
7. Declare oracle boundaries.
8. Prepare R1, R2, or R3 using `submission-template.md`.

The reviewer should not trust the author.

The reviewer should reconstruct the evidence.

Formal submission should wait until the public challenge notice defines the submission channel and review procedure.

---

## Relationship to A-DAP

GCD-001 does not validate A-DAP as a whole.

GCD-001 tests a specific public reconstruction claim.

If the claim survives external reconstruction, it gains evidentiary weight.

If the claim fails, the protocol improves.

If the specification is ambiguous, the specification becomes more precise.

The strongest result for A-DAP is not automatic confirmation.

The strongest result is a process where confirmation, falsification, and ambiguity are all admissible outcomes.

---

## Final Principle

GCD-001 is not yet an independently reviewed case.

It is a public reconstruction package prepared for independent adversarial review.

It does not prove decision truth.

It does not ask for trust.

It asks for reconstruction.
