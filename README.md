# A-DAP — Auditable Decision Accountability Protocol

A-DAP is a contestability architecture for high-impact automated decisions.

Its core claim is intentionally narrow:

A-DAP makes later alteration of committed decision records detectable under defined custody assumptions.

It does not prove that the original decision was true.

It does not prove that the decision was fair.

It does not eliminate trust in the operator at origin.

It does not guarantee detection.

Its value is stricter:

High-impact automated decisions should be born with a reconstructible evidentiary object, so that affected parties, auditors, regulators, or courts can later contest the specific decision against a pre-committed record.

A-DAP turns automated decisions from post-hoc explanations into contestable records.

---

## Executive Summary

A-DAP proposes that high-impact automated decisions be committed before or at the moment of action through reconstructible decision envelopes.

A decision envelope is a pre-committed evidentiary object that can later be reconstructed, examined, and compared against explanations, notices, logs, or operator claims.

A-DAP uses ordinary cryptographic primitives such as hashing, signatures, timestamping, and reproducible reconstruction rules.

Its goal is not to make automated decisions correct.

Its goal is to make later inconsistency detectable.

The protocol is built around a simple governance failure:

Most automated decision systems can explain themselves after the fact, but cannot prove that the explanation corresponds to the actual decision state that existed at the time of action.

A-DAP addresses that failure by separating:

- the decision,
- the record,
- the explanation,
- the verifier,
- and the authority interpreting the result.

This separation is the core of the protocol.

---

## What A-DAP Is

A-DAP is:

- a protocol for reconstructible decision evidence,
- a framework for contesting automated decisions after the fact,
- a way to bind decision records before they can be rewritten,
- an architecture for separating decision-making from later justification,
- a method for making tampering, substitution, or unexplained inconsistency detectable under stated assumptions.

A-DAP is designed for high-impact domains such as:

- credit scoring,
- insurance,
- public benefits,
- hiring,
- healthcare triage,
- judicial or administrative decision support,
- education access,
- fraud detection,
- compliance screening,
- and other automated or semi-automated decision pipelines.

---

## What A-DAP Is Not

A-DAP is not:

- a fairness metric,
- an explainability method,
- a model audit by itself,
- a guarantee that a decision was correct,
- a guarantee that a decision was lawful,
- a guarantee that a decision was fair,
- a substitute for courts, regulators, auditors, or institutional review,
- a complete accountability system by itself.

A-DAP does not answer:

“Was the decision right?”

It helps answer:

“Can we reconstruct what the system committed to at the time of decision, and detect whether the later record diverges from that commitment?”

---

## Why This Exists

Many governance frameworks assume that automated decisions can be reviewed later through logs, explanations, model cards, documentation, or operator statements.

That is not enough.

A log can be incomplete.

An explanation can be generated after the fact.

A model card can describe a system generally without proving what happened in a specific decision.

A database record can be changed.

An operator can summarize a decision without exposing the exact committed state.

The result is a structural accountability gap:

The system decides.

The system records.

The system explains.

And then the system, or its operator, asks to be trusted about all three.

A-DAP exists to break that loop.

---

## Core Principle

A high-impact automated decision should produce a decision envelope at or before the moment of action.

That envelope should contain or commit to the minimum information needed to later reconstruct the decision event.

The envelope should be:

- canonicalized,
- hashed,
- signed or otherwise authenticated,
- timestamped where possible,
- linked to reconstruction rules,
- and verifiable by a party outside the original decision system.

The purpose is not transparency for its own sake.

The purpose is contestability.

---

## The Decision Envelope

A decision envelope is the core evidentiary object in A-DAP.

A minimal envelope may include commitments to:

- decision identifier,
- timestamp or timestamp claim,
- policy or model version,
- input commitment,
- output commitment,
- relevant rule or threshold commitment,
- operator identity or system identity,
- canonicalization method,
- hash algorithm,
- signature method,
- reconstruction instructions,
- custody assumptions,
- and verification metadata.

The exact contents depend on the domain and privacy constraints.

A-DAP does not require publishing sensitive personal data.

It requires that the relevant decision state be committed in a way that can later be reconstructed or challenged under defined conditions.

---

## Commit Before Explain

A-DAP is based on a temporal rule:

Commit before explain.

The commitment must exist before the operator has an opportunity to rewrite the record in response to challenge, litigation, audit, or public pressure.

This is why ordinary explanations are insufficient.

A post-hoc explanation may be useful.

But without a prior commitment, it cannot prove that it corresponds to the original decision state.

A-DAP does not reject explanations.

It limits what explanations can prove.

---

## Auditability Is Not Explainability

Explainability asks:

“Why did the model say this?”

Auditability asks:

“Can an independent party reconstruct what the system committed to, and detect whether the later account diverges from it?”

These are different problems.

A system can be explainable but not auditable.

A system can produce natural-language reasons while still lacking a reconstructible evidentiary record.

A-DAP focuses on the second problem.

---

## Accountability Requires Institutions

A-DAP does not itself create accountability.

Accountability requires:

- legal authority,
- procedural rights,
- institutional capacity,
- remedies,
- enforcement,
- and human judgment.

A-DAP produces a stronger object for those institutions to inspect.

It turns a dispute from:

“Trust our explanation.”

into:

“Compare this explanation against the committed record.”

That is a narrower but important contribution.

---

## Effective Contestability

A-DAP creates reconstructible decision records, but reconstructibility is not the same as exercised contestability or institutional accountability.

Structural NDC describes the independent verification paths available in the architecture.

`ADAP-EXP-003.md` introduces the related concept of **Effective NDC**: the expected number of verification constraints that are actually exercised.

This matters because a system may expose multiple verification paths while still facing little real-world contestation if affected parties, auditors, or regulators do not reconstruct the decision record.

`ADAP-EXP-003.md` formalizes this gap as **Exercise Debt**.

The safe claim is therefore limited:

A-DAP can increase structural verifiability.

It does not guarantee that verification will be exercised, nor that accountability will follow automatically.

---

## Structural NDC

NDC means Non-Dependency Count.

In this repository, NDC is a proposed conceptual measure, not an established industry standard.

In this repository, NDC is used to describe how many genuinely independent verification paths exist after collapsing dependencies.

The purpose of NDC is to avoid false multiplicity.

Five dashboards controlled by the same operator are not five independent verification paths.

Five logs generated by the same system are not five independent verification paths.

Five explanations produced by the same model are not five independent verification paths.

The independence of verification matters more than the quantity of artifacts.

---

## The Envelope Bottleneck

A-DAP includes a known failure mode called the Envelope Bottleneck.

If every verification path depends on the same envelope, operator, interface, or custody channel, then the apparent independence may collapse.

This is documented in:

`architecture/envelope-bottleneck.md`

The point is methodological:

A-DAP must not count multiple artifacts as independent if they share the same controlling dependency.

Before claiming strong verification, dependency paths must be collapsed conservatively.

---

## Automated NDC Analysis

This repository also includes work on automated NDC analysis.

The purpose is not to claim that a tool can fully determine trust independence.

The purpose is to help detect where independence may be overstated.

Automated analysis can assist reviewers by identifying dependency concentration, shared custody paths, and possible verification bottlenecks.

It does not replace adversarial review.

Related file:

`architecture/automated-ndc-v2.md`

The safe claim is:

Automated NDC tooling may help expose where trust is still concentrated.

It does not prove that verification is independent.

---

## Reconstructible Verdicts

The repository also explores reconstructible verdicts for higher-level evaluators such as Ω++.

The risk is recursive:

A verifier can become another system asking to be trusted.

To avoid this, any automated risk verdict should itself be reconstructible.

A verdict should not merely say:

“No circular dependency found.”

It should expose the evidence, rules, intermediate steps, and assumptions that allow another reviewer to reconstruct why that verdict was produced.

Related file:

`architecture/omega-plus-plus-reconstructible-verdicts.md`

The safe claim is:

Automated verdicts can support review only when their own reasoning path is reconstructible.

They should not become a new authority layer that validates itself.

---

## Challenge Package: GCD-001

This repository includes the `challenge/gcd-001/` package.

GCD-001 is an external reconstruction challenge based on the German Credit Dataset.

Its purpose is to test whether a third party can reconstruct a committed decision object using the provided specification and materials.

The challenge is not proof that A-DAP is complete.

It is a limited test of reconstructibility under defined conditions.

Related files:

- `challenge/gcd-001/README.md`
- `challenge/gcd-001/reconstruction-challenge.md`
- `challenge/gcd-001/reconstruction-spec.md`
- `challenge/gcd-001/submission-template.md`
- `challenge/gcd-001/reviewer-guidelines.md`

---

## Proofs, Claims, Timestamps, and Audits

This repository distinguishes between four things that are often confused:

### Claim

A statement made by the operator or author.

Example:

“This decision record was generated at a certain time.”

### Proof

A verifiable artifact that supports or constrains a claim.

Example:

A hash, signature, timestamp token, or reproducible reconstruction result.

### Timestamp

Evidence that a commitment existed no later than a certain time, depending on the timestamp authority and custody assumptions.

### Audit

A review process performed by a person, institution, or system that interprets the available evidence.

A-DAP does not collapse these into one thing.

Related file:

`proofs/README.md`

---

## Solver Status

Any solver in this repository should be treated as experimental unless explicitly stated otherwise.

A solver may help reconstruct decision artifacts, verify hashes, or check consistency.

But a solver is not itself the source of truth.

A solver can contain bugs.

A solver can encode wrong assumptions.

A solver can falsely validate a flawed reconstruction.

Therefore, the repository distinguishes between:

- the committed object,
- the reconstruction specification,
- the solver implementation,
- and the reviewer’s interpretation.

Related file:

`solver/README.md`

---

## Threat Model

A-DAP assumes some things and does not attempt to solve others.

Examples of threats A-DAP can help expose:

- later alteration of decision records,
- mismatch between explanation and committed record,
- substitution of outputs,
- inconsistent reconstruction,
- missing or invalid commitments,
- unverifiable custody claims,
- and dependency concentration.

Examples of threats outside the basic scope:

- total collusion among all parties,
- compromised hardware root of trust,
- malicious timestamp authority,
- false data at origin,
- lawful but unfair decision logic,
- incorrect model design,
- institutional refusal to act on evidence.

A-DAP does not eliminate trust.

It tries to locate where trust remains.

Related file:

`THREAT_MODEL.md`

---

## Minimal Verification Flow

A simplified A-DAP verification flow:

1. Obtain the decision envelope.
2. Confirm the canonicalization method.
3. Reconstruct the committed object.
4. Compute the hash.
5. Compare the hash against the committed value.
6. Verify any signature or timestamp evidence.
7. Check whether the claimed model, policy, or decision state matches the commitment.
8. Report mismatch, missing evidence, or successful reconstruction.
9. Interpret the result within the stated threat model.

This does not prove the decision was right.

It tests whether the later record is consistent with the earlier commitment.

---

## Repository Structure

Typical repository structure:

```text
.
├── README.md
├── NOTICE.md
├── THREAT_MODEL.md
├── CONTRIBUTING.md
├── QUICKSTART.md
├── RELEASE_NOTES.md
├── ADAP-EXP-003.md
├── architecture/
│   ├── envelope-bottleneck.md
│   ├── automated-ndc-v2.md
│   └── omega-plus-plus-reconstructible-verdicts.md
├── challenge/
│   └── gcd-001/
│       ├── README.md
│       ├── reconstruction-challenge.md
│       ├── reconstruction-spec.md
│       ├── submission-template.md
│       └── reviewer-guidelines.md
├── proofs/
│   └── README.md
└── solver/
    └── README.md
