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

## Adoption Capture Risk

A-DAP also documents a non-technical adoption risk: formal implementation without substantive contestability.

A powerful operator may adopt visible A-DAP artifacts such as envelopes, hashes, signatures, Merkle roots, timestamps, receipts, dashboards, and verifiers, while still preserving control over:

- what enters the envelope,
- what remains outside the envelope,
- how the receipt is delivered,
- who controls the verification interface,
- and whether verification is actually exercised.

This creates a risk of compliance theater.

The operator may appear to adopt A-DAP while preserving the same control structure that A-DAP is meant to expose.

This risk is documented in:

`architecture/adoption-capture-risk.md`

The safe claim is:

A-DAP adoption is meaningful only when paired with independent scope review, conservative dependency-collapse analysis, externalizable reconstruction, and realistic exercise-risk assessment.

Formal adoption alone does not prove accountability.

---

## Exercisable Verification Interface

A-DAP also distinguishes between validator authority and reproducible verification.

A verification interface should not become a new authority that asks affected parties, auditors, regulators, or courts to trust its report.

Instead, it should produce reproducible verification output:

- the receipt analyzed,
- the tool version used,
- the input hash,
- the declared schema,
- the deterministic checks performed,
- the fields present or missing,
- the dependencies detected,
- and the method required for another party to reproduce the same result.

This distinction matters because a validator that merely issues reports can recreate the same trust problem A-DAP is designed to avoid.

The goal is not:

“Trust the validator.”

The goal is:

“Run the same open procedure over the same receipt and obtain the same result.”

This design is documented in:

`architecture/exercisable-verification-interface.md`

The safe claim is:

A-DAP verification should be exercisable by non-technical people without turning the interface into an attestation authority.

The interface may help translate deterministic checks into human-readable language, but the evidentiary force must come from independent reproducibility, not from the validator’s status.

A hosted or client-side interface may reduce friction, but local execution is not independent verification by itself.

Client-side verification can help exercise the verification path, but it does not automatically increase NDC.

NDC depends on independent custody and verification paths after dependency collapse, including whether timestamp evidence, anchors, schemas, public keys, and proof availability are reachable outside the operator’s control.

Do not confuse local execution with independent verification.

---

## Verifier Funding Capture

A-DAP also treats verifier funding as a possible control vector.

A third-party verifier is not independent merely because it is organizationally separate.

If the verifier’s funding, access, scope, contract renewal, governance, or survival depends materially on the operator being verified, the verifier may collapse into the same control domain under conservative NDC analysis.

This risk is documented in:

`architecture/verifier-funding-capture.md`

The safe claim is:

Independent verification requires more than a third-party label. It requires disclosure and analysis of the verifier’s funding, access, scope, governance, and revocation dependencies.

Formal third-party verification alone does not prove independence.

---

## IP Priority and Authorized Execution

A-DAP may also support limited intellectual-property-adjacent evidence, but only under narrow claims.

The safe use is not algorithmic plagiarism detection.

A-DAP cannot prove that another system copied an algorithm merely because outputs, behavior, or decision patterns are similar.

Similarity is not origin.

Correlation is not authorship.

A Merkle tree proves integrity of committed data, not authorship of a function.

This risk is documented in:

`architecture/ip-priority-and-authorized-execution.md`

The defensible uses are narrower:

- temporal priority evidence: showing that a specific artifact existed in a specific form no later than a specific date;
- historical process evidence: showing that material development steps were externally anchored over time;
- externally authorized execution evidence: showing that a specific execution presented a valid authorization token issued by a materially disjoint authority for a declared version, scope, deployment, or time window.

The safe claim is:

A-DAP can support existence-by-date, externally anchored process evidence, and externally authorized execution evidence under stated custody assumptions.

Historical process evidence is complementary to temporal priority, not superior to it.

A self-reported history is not proof.

Even an anchored process chain does not eliminate independent convergence.

A-DAP cannot prove copying, sole authorship, infringement, or authorized execution from output similarity, self-reported process narratives, or self-signed receipts.

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

## Challenge Package: GCD-002

This repository also includes the `challenge/gcd-002-verifier-funding/` package.

GCD-002 tests whether a claimed third-party verifier remains independent when funding, access, scope, governance, and revocation dependencies are included in the custody graph.

Its purpose is not to prove that all third-party verification is captured.

Its purpose is narrower:

to test whether formal third-party verification can collapse under conservative dependency analysis when material control vectors lead back to the operator being verified.

Related files:

- `challenge/gcd-002-verifier-funding/README.md`
- `challenge/gcd-002-verifier-funding/experiment-spec.md`
- `challenge/gcd-002-verifier-funding/custody-graph.json`
- `challenge/gcd-002-verifier-funding/expected-findings.md`
- `challenge/gcd-002-verifier-funding/submission-template.md`
- `challenge/gcd-002-verifier-funding/reviewer-guidelines.md`

The safe claim is:

GCD-002 extends A-DAP’s dependency-collapse method to the verification ecosystem.

It asks whether a verifier is materially independent, not merely formally separate.

Third-party verification should not be counted as independent until its funding, access, scope, governance, and revocation dependencies are examined.

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
│   ├── adoption-capture-risk.md
│   ├── exercisable-verification-interface.md
│   ├── verifier-funding-capture.md
│   ├── ip-priority-and-authorized-execution.md
│   ├── envelope-bottleneck.md
│   ├── automated-ndc-v2.md
│   └── omega-plus-plus-reconstructible-verdicts.md
├── challenge/
│   ├── gcd-001/
│   │   ├── README.md
│   │   ├── reconstruction-challenge.md
│   │   ├── reconstruction-spec.md
│   │   ├── submission-template.md
│   │   └── reviewer-guidelines.md
│   └── gcd-002-verifier-funding/
│       ├── README.md
│       ├── experiment-spec.md
│       ├── custody-graph.json
│       ├── expected-findings.md
│       ├── submission-template.md
│       └── reviewer-guidelines.md
├── proofs/
│   └── README.md
└── solver/
    └── README.md
```

The exact structure may evolve.

The important distinction is conceptual:

- architecture explains the theory,
- challenge tests reconstruction,
- proofs separate evidentiary categories,
- solver contains experimental tooling,
- and threat model defines limits.

---

## Quickstart for Reviewers

For a five-minute review:

1. Read the core claim at the top of this README.
2. Check what A-DAP explicitly does not claim.
3. Read `THREAT_MODEL.md`.
4. Inspect `architecture/envelope-bottleneck.md`.
5. Inspect `ADAP-EXP-003.md`.
6. Inspect `architecture/adoption-capture-risk.md`.
7. Inspect `architecture/exercisable-verification-interface.md`.
8. Inspect `architecture/verifier-funding-capture.md`.
9. Inspect `architecture/ip-priority-and-authorized-execution.md`.
10. Run or review the reconstruction challenge in `challenge/gcd-001/`.
11. Run or review the verifier-funding challenge in `challenge/gcd-002-verifier-funding/`.
12. Try to identify where trust is still concentrated.

The best review is adversarial.

Do not ask only whether the protocol works.

Ask where it silently asks to be trusted.

---

## Design Discipline

A-DAP follows several design rules:

### 1. Do not overclaim

If the protocol only detects inconsistency, say that.

Do not call inconsistency detection “truth.”

### 2. Separate proof from explanation

A convincing explanation is not a proof.

A proof constrains what can be changed later.

### 3. Collapse false independence

Multiple artifacts do not matter if they depend on the same authority.

### 4. Commit before challenge

The evidentiary object must exist before the operator knows which decision will be contested.

### 5. Make verification externalizable

A verifier outside the original decision system should be able to reconstruct the relevant commitment under defined assumptions.

### 6. Declare assumptions

A-DAP is only meaningful when custody, canonicalization, timestamping, and verification assumptions are explicit.

### 7. Treat non-exercise as a real weakness

A verification path that nobody uses may still be latent evidence.

But latent evidence is not the same as exercised contestability.

### 8. Treat adoption capture as a first-class risk

A-DAP should not be evaluated only by whether an operator formally adopts its artifacts.

It should also be evaluated by whether the deployment preserves independent scope review, external reconstruction, dependency separation, and realistic exercise of verification.

### 9. Do not turn the validator into an authority

A-DAP verification should not depend on trusting a validator’s report.

The validator should produce reproducible verification output that another party can independently run, inspect, compare, and challenge.

### 10. Do not confuse client-side execution with independence

Client-side verification can reduce friction and help people exercise verification.

But local execution does not, by itself, create independent custody, external anchoring, or higher NDC.

### 11. Do not confuse third-party verification with independent verification

A verifier may be legally separate but economically or operationally dependent.

Funding, access, scope, renewal, governance, and revocation dependencies must be included in ecosystem-level NDC analysis.

### 12. Do not confuse priority evidence with plagiarism proof

A timestamped artifact can support existence-by-date.

It does not prove sole authorship, copying, infringement, or lack of independent invention.

Authorized execution also cannot be self-attested by the engine being checked.

### 13. Do not confuse process history with proof of origin

A development history can support provenance analysis only when its material steps were independently anchored over time.

A self-reported history is not proof.

Historical process evidence is complementary to temporal priority, not superior to it.

Even an anchored process chain does not eliminate independent convergence.

---

## Example Safe Use

A public agency uses an automated eligibility system.

At the moment of decision, the system creates a decision envelope committing to:

- applicant record hash,
- rule version,
- model version,
- output,
- threshold,
- timestamp evidence,
- and reconstruction instructions.

Later, the applicant challenges the denial.

An auditor reconstructs the envelope and discovers that the explanation sent to the applicant does not match the committed decision state.

A-DAP does not decide the legal remedy.

But it gives the auditor a concrete inconsistency to examine.

---

## Example Unsafe Use

A company says:

“Our AI decisions are accountable because we use A-DAP.”

This is not a valid claim.

A-DAP does not guarantee accountability.

A safer statement would be:

“Our system generates reconstructible decision envelopes designed to make later alteration or inconsistency detectable under stated assumptions.”

That statement is narrower and more defensible.

---

## Current Maturity

This repository should be read as an evolving technical note, protocol architecture, and adversarial review surface.

Some parts are conceptual.

Some parts are experimental.

Some parts are challenge-oriented.

Some parts are intended for adversarial review.

The project is not presented as a finished compliance product.

It is a structured attempt to formalize and test the conditions under which automated decisions can become externally contestable.

---

## Open Problems

A-DAP leaves several important problems open:

- How should exercise probability be measured in real institutions?
- How should correlated non-exercise be modeled?
- How should privacy-preserving reconstruction work in sensitive domains?
- How should timestamp authority failure be handled?
- How should courts or regulators treat partial reconstruction?
- How should dependency collapse be standardized?
- How should reconstruction cost be reduced for affected parties?
- How should A-DAP interact with sector-specific legal duties?
- How should false positives and false negatives in reconstruction be reported?
- How should external reviewers be incentivized to actually verify?
- How should independent envelope scope be defined and enforced?
- How should adoption capture be detected before it becomes compliance theater?
- How should verification be made exercisable without turning the validator into a new authority?
- How should client-side verification reduce friction without being mistaken for independent custody?
- How should verifier funding, access, scope, governance, and revocation dependencies be disclosed and analyzed?
- How should externally issued authorization tokens be designed without turning the token issuer into a new bottleneck?
- How should temporal priority evidence be used without overstating authorship or plagiarism claims?
- How should historical process evidence be anchored over time without becoming self-reported narrative?
- How should anchored process chains be evaluated when another party claims independent convergence?

These are not minor implementation details.

They are part of the accountability problem.

---

## Contribution Guidelines

Contributions are welcome if they improve clarity, testability, threat modeling, or adversarial review.

Especially useful contributions include:

- attacks on the protocol,
- dependency-collapse examples,
- reconstruction failures,
- false-independence cases,
- adoption-capture scenarios,
- verifier-funding capture scenarios,
- IP-priority and authorized-execution critiques,
- authorization-token custody critiques,
- historical-process evidence critiques,
- anchored-process chain critiques,
- envelope-scope critiques,
- exercisable-verification interface designs,
- validator-capture critiques,
- client-side verification critiques,
- verifier supply-chain critiques,
- canonicalization edge cases,
- timestamping critiques,
- privacy-preserving envelope designs,
- legal interpretation notes,
- and empirical evidence about whether verification paths are actually exercised.

Please do not contribute language that inflates the protocol beyond what it can prove.

Related file:

`CONTRIBUTING.md`

---

## Citation and Attribution

If referencing A-DAP, cite it as a protocol architecture for reconstructible decision evidence and contestability.

Do not describe it as a complete accountability solution.

Related file:

`NOTICE.md`

Suggested short description:

A-DAP is a protocol architecture for creating reconstructible evidentiary records around high-impact automated decisions, so that later alteration or inconsistency can be detected under stated assumptions.

---

## Release Notes

See:

`RELEASE_NOTES.md`

Release notes should document not only features, but also narrowed claims, removed overclaims, known weaknesses, and adversarial findings.

In this project, reducing a false claim is progress.

---

## Final Position

A-DAP is based on a narrow but important claim:

Automated decisions should not depend only on post-hoc explanation.

They should produce reconstructible evidence.

But reconstructible evidence is not truth.

Structural contestability is not exercised accountability.

Formal adoption is not substantive contestability.

Validator output is not authority.

Client-side execution is not independent verification by itself.

Third-party verification is not independent verification by default.

Temporal priority is not plagiarism proof.

Historical process evidence is not proof of origin by itself.

A self-reported history is not proof.

A-DAP helps create the object that later accountability may need.

It does not replace the institutions that must use it.
