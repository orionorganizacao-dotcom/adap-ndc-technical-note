# A-DAP — Auditable Decision Accountability Protocol

A-DAP is a contestability architecture for high-impact automated decisions.

Its core claim is intentionally narrow:

A-DAP makes later alteration of committed decision records detectable under defined custody assumptions.

It does not prove that the original decision was true.

It does not prove that the decision was fair.

It does not eliminate trust in the operator at origin.

It does not guarantee detection.

Its value is stricter:

high-impact automated decisions should be born with a reconstructible evidentiary object, so that affected parties, auditors, regulators, or courts can later contest the specific decision against a pre-committed record.

A-DAP turns automated decisions from post-hoc explanations into contestable records.

---

## Executive Summary

A-DAP proposes that high-impact automated decisions be committed before or at the moment of action through reconstructible decision envelopes.

A decision envelope is a pre-committed evidentiary object that can later be reconstructed, examined, and compared against explanations, notices, logs, or operator claims.

A-DAP can use established cryptographic and procedural tools — such as hashing, digital signatures, timestamping, custody separation, and independent verification — to reduce the ability to alter decision records without detection under stated assumptions.

The protocol does not claim that cryptography alone creates accountability.

It claims that accountability requires contestable evidence.

A-DAP therefore focuses on the evidentiary layer beneath governance:

- What was committed?
- When was it committed?
- By whom or by what system?
- Under which custody assumptions?
- Can a third party later reconstruct the decision record?
- Can alteration be detected without relying solely on the same system that produced the decision?

A-DAP is designed for domains where automated decisions may affect rights, access, treatment, ranking, eligibility, enforcement, safety, or institutional outcomes.

Examples include:

- public-sector AI systems;
- medical triage and clinical decision support;
- judicial or administrative automation;
- credit, insurance, and eligibility decisions;
- election-related AI systems;
- high-impact moderation or enforcement systems;
- safety-critical autonomous workflows.

A-DAP does not replace regulation, institutional accountability, audit authority, or judicial review.

It provides a technical and architectural foundation that can make later contestation possible.

---

## Core Problem

Many automated systems produce decisions first and explanations later.

This creates a structural weakness.

After a decision has already affected someone, the system may generate a plausible explanation, expose a log, or produce a summary of what supposedly happened.

But those artifacts may be:

- incomplete;
- mutable;
- generated after the fact;
- controlled by the same operator;
- produced by the same model or pipeline;
- disconnected from the actual decision state;
- impossible to independently reconstruct.

In such systems, the affected party may receive an explanation without receiving evidence.

That is the distinction A-DAP is built around:

**explanation is not verification.**

**logging is not proof.**

**transparency is not contestability.**

A system may explain itself while still leaving no independent way to test whether the explanation corresponds to the decision that was actually made.

A-DAP addresses this by requiring decisions to be committed as evidentiary objects before or at the moment of action.

---

## What A-DAP Is

A-DAP is an architectural protocol for making automated decisions contestable.

It defines how a decision record should be created, committed, preserved, and later reconstructed under explicit assumptions.

A-DAP is not a single product.

It is not a model.

It is not a compliance checklist.

It is not a claim that cryptography automatically creates justice.

A-DAP is a structure for separating:

- decision;
- record;
- explanation;
- verification;
- custody;
- reconstruction.

The goal is to prevent the same system from silently producing a decision, rewriting the record, generating the explanation, and validating itself.

---

## What A-DAP Is Not

A-DAP does not prove that a decision was correct.

A-DAP does not prove that a decision was fair.

A-DAP does not prove that a model was unbiased.

A-DAP does not eliminate institutional trust.

A-DAP does not remove the need for human review.

A-DAP does not guarantee that all tampering will be detected.

A-DAP does not solve full collusion between all parties in the custody chain.

A-DAP does not turn a bad policy into a good policy.

A-DAP does not create legal accountability by itself.

A-DAP produces a more limited but important object:

a committed, reconstructible decision record that can later be tested against claims, explanations, logs, notices, or regulatory obligations.

---

## Relationship to Existing Cryptographic Audit-Trail Work

A-DAP does not claim novelty over cryptographic primitives such as digital signatures, hash chains, timestamping, Merkle trees, transparency logs, or tamper-evident audit trails.

Those mechanisms are established public tools.

A-DAP uses them to address a narrower architectural problem: how high-impact automated decisions can be born as contestable evidentiary objects, with decision, record, explanation, and verification separated enough that later alteration becomes detectable under defined custody assumptions.

Its contribution is not the invention of cryptographic audit trails.

Its contribution is the contestability framing, the separation requirements, and the analysis of how many structurally distinct compromises would be required to falsify a decision record without detection.

In this sense, A-DAP should be read as complementary to existing audit-trail, transparency-log, timestamping, and tamper-evidence work.

Where those systems often focus on whether a record was altered, A-DAP focuses on a related but narrower question:

can an affected party, auditor, regulator, or court later contest a specific automated decision against a pre-committed evidentiary object without depending solely on the same system that produced the decision?

A-DAP is therefore not a replacement for cryptographic audit infrastructure.

It is an architectural contestability layer that can use such infrastructure when the custody assumptions, independence requirements, and verification boundaries are explicit.

---

## NDC as a Capture Diagnostic, Not a Robustness Claim

A-DAP uses NDC as a diagnostic measure, not as a guarantee of robustness.

NDC asks how many structurally distinct compromises would be required to falsify a decision record without detection under a given architecture and threat model.

A high NDC may indicate stronger separation between decision, record, explanation, and verification.

But the most important result is often NDC = 1.

NDC = 1 means that a single compromised envelope, verifier, operator, or custody path may be sufficient to make a false record appear valid.

This is not a failure of the metric.

It is the metric exposing capture.

In this sense, NDC does not certify that A-DAP is strong.

It helps identify when A-DAP, or any audit-trail architecture, has collapsed back into self-attestation.

The value of the metric is not that it always produces high scores.

The value is that it can reveal when verification is not structurally independent enough to deserve evidentiary weight.

This distinction matters because a cryptographic audit trail can show that a record remained intact while still leaving unresolved whether the verifier, custody path, or evidentiary envelope was structurally independent from the system being evaluated.

NDC is meant to make that dependency visible.

It is therefore better understood as a capture diagnostic than as a certification score.

A low NDC is not an embarrassment to hide.

It is a warning that the architecture may still be asking the same envelope to generate, preserve, and validate its own evidence.

---

## Core Concepts

### Decision Envelope

A decision envelope is the evidentiary object created around a decision.

It may include:

- decision identifier;
- input references or committed input hashes;
- model or system reference;
- policy or rule reference;
- output reference;
- timestamp;
- operator or system identity;
- signature;
- custody metadata;
- reconstruction instructions;
- verification artifacts.

The envelope should not be confused with a mere log entry.

A log says something happened.

A decision envelope should allow a later verifier to test whether the record still corresponds to the committed decision state.

---

### Commit-Before-Act

A-DAP favors commit-before-act whenever possible.

This means that the relevant decision state is committed before the decision is executed or externally relied upon.

The purpose is to reduce the gap between action and evidence.

If the record is created only after the decision is challenged, the system may be documenting a story rather than preserving evidence.

Commit-before-act does not solve every problem.

But it changes the evidentiary posture.

The decision is no longer only explained after the fact.

It is born with a committed record.

---

### Reconstruction

Reconstruction means that a later verifier can examine whether the decision record corresponds to the committed evidence.

Depending on the implementation, reconstruction may involve:

- checking hashes;
- verifying digital signatures;
- validating timestamps;
- comparing committed inputs and outputs;
- checking custody metadata;
- replaying deterministic parts of the decision process;
- comparing the decision envelope against external artifacts;
- identifying whether verification depends on the same pipeline that produced the decision.

Reconstruction does not necessarily mean reproducing the model’s internal reasoning.

A-DAP is model-agnostic.

The goal is not to open the black box.

The goal is to preserve enough committed evidence that the decision can be contested.

---

### External Verification

A-DAP distinguishes between internal self-checking and external verification.

A system that generates a decision, stores the record, explains the decision, and verifies the record by itself remains structurally weak.

The question is not only whether the record is cryptographically valid.

The question is also whether the verifier is sufficiently independent from the generator.

If verification depends on the same compromised envelope, the apparent proof may collapse into self-attestation.

---

## The Envelope Bottleneck

A central risk in A-DAP analysis is the Envelope Bottleneck.

The Envelope Bottleneck occurs when the same evidentiary envelope controls too much of the trust path.

For example:

- the system generates the decision;
- the same system records the evidence;
- the same system explains the decision;
- the same system validates the record;
- the same custody path preserves all artifacts.

In that case, compromising the envelope may be enough to make a false record appear valid.

This is why A-DAP focuses on separation.

The goal is not merely to add stronger logs.

The goal is to reduce the number of cases where one compromised component can control decision, record, explanation, and verification simultaneously.

---

## Number of Distinct Compromises — NDC

NDC stands for Number of Distinct Compromises.

It estimates how many structurally distinct compromises would be required to falsify a decision record without detection under a stated architecture and threat model.

NDC is assumption-dependent.

It depends on architecture, custody, verifier independence, and what the analysis counts as a distinct compromise.

A simplified intuition:

- NDC = 1 means one compromise may be enough to falsify the record without detection.
- Higher NDC may indicate that multiple structurally distinct components would need to fail or collude.
- NDC is useful when it exposes hidden self-attestation.
- NDC is dangerous if presented as a certification score without clear assumptions.

The purpose of NDC is not to make every architecture look strong.

The purpose is to reveal where the architecture is weak.

---

## Why Logs Are Not Enough

Logs are useful.

But logs are often controlled by the same system or organization whose decision is being questioned.

A log can be incomplete.

A log can be overwritten.

A log can be selectively disclosed.

A log can be generated after the fact.

A log can record that an event occurred without proving that the recorded event corresponds to the actual decision state.

A-DAP does not reject logs.

It treats logs as insufficient by themselves.

A log becomes more evidentiary when it is connected to pre-commitment, independent verification, custody separation, and reconstructible artifacts.

---

## Why Explanations Are Not Enough

Explanations are useful for understanding.

But explanations are not the same as evidence.

An explanation may be generated after the fact.

An explanation may be persuasive but false.

An explanation may be optimized for user acceptance.

An explanation may omit relevant inputs.

An explanation may be produced by the same system whose decision is being challenged.

A-DAP does not reject explanations.

It places explanations in the correct evidentiary position.

An explanation should be testable against a committed decision record.

Without such a record, explanation risks becoming self-justification.

---

## Architecture Overview

A simplified A-DAP architecture contains:

1. Decision generation
2. Decision envelope creation
3. Pre-action or at-action commitment
4. Cryptographic binding
5. Custody separation
6. External or independent verification
7. Reconstruction procedure
8. Contestation interface

The exact implementation may vary.

For latency-sensitive systems, A-DAP does not assume a single commit model.

Strong synchronous commit-before-act may be appropriate for slower, high-impact decisions where contestability matters and latency costs are small relative to the harm of non-contestable decisions.

Low-latency systems may require weaker or different commitment patterns, such as append-only ordering, batched Merkle commitments, pre-commitment of policies or execution envelopes, asynchronous materialization, or periodic external anchoring.

These variants do not provide the same evidentiary strength by default.

They change the trust structure and may lower NDC.

See [`architecture/commit-latency-tradeoff.md`](architecture/commit-latency-tradeoff.md) for the latency, commit-strength, and NDC trade-off analysis.

A minimal implementation may use:

- canonical JSON;
- SHA-256 hashing;
- Ed25519 signatures;
- RFC 3161 timestamping;
- Merkle aggregation;
- deterministic verification scripts;
- public challenge datasets;
- independent third-party reconstruction.

The specific tools are less important than the separation properties.

A weak implementation can use strong cryptography and still collapse if the same actor controls everything.

A stronger implementation makes falsification without detection require multiple structurally distinct compromises.

---

## Minimal Decision Envelope Example

A simplified decision envelope may look like this:

```json
{
  "decision_id": "decision-0001",
  "subject_ref": "subject-hash-or-reference",
  "input_hash": "sha256:...",
  "policy_ref": "policy-v1.2.0",
  "model_ref": "model-or-system-version",
  "output_hash": "sha256:...",
  "timestamp": "2026-05-28T12:00:00Z",
  "commitment_hash": "sha256:...",
  "signature": "ed25519:...",
  "custody": {
    "operator": "system-operator",
    "verifier": "independent-verifier-or-path",
    "timestamp_authority": "external-or-declared"
  },
  "reconstruction": {
    "method": "documented-verification-procedure",
    "artifacts": [
      "input-reference",
      "output-reference",
      "policy-reference",
      "verification-script-or-spec"
    ]
  }
}
```

This is only illustrative.

A real implementation must define canonicalization, custody assumptions, artifact availability, privacy boundaries, redaction rules, and verification procedures.

---

## Threat Model

A-DAP assumes that some actors may have incentives to alter, suppress, reinterpret, or selectively disclose decision records.

Possible threats include:

- post-hoc modification of records;
- deletion of unfavorable decisions;
- selective disclosure of logs;
- replacement of inputs or outputs;
- misleading explanations;
- verifier capture;
- timestamp manipulation;
- custody-chain weakness;
- operator self-attestation;
- collusion between components;
- reconstruction failure due to missing artifacts.

A-DAP also declares three structural boundaries that should not be hidden as ordinary implementation bugs:

- input provenance boundary;
- verification window boundary;
- signer, custody, and verification boundary.

These boundaries define where A-DAP can preserve evidentiary integrity and where additional assumptions are required.

See:

- [`architecture/input-provenance-boundary.md`](architecture/input-provenance-boundary.md)
- [`architecture/commit-latency-tradeoff.md`](architecture/commit-latency-tradeoff.md)
- [`architecture/signer-custody-boundary.md`](architecture/signer-custody-boundary.md)

A-DAP does not fully solve:

- total collusion among all relevant parties;
- hardware-level compromise outside declared assumptions;
- false input data that was already false at origin;
- key compromise outside declared custody controls;
- signer-custody collapse;
- omission at origin before a record exists;
- bad policy choices;
- biased training data;
- illegitimate institutional authority;
- legal accountability without enforcement.

A-DAP is an evidentiary architecture, not a complete governance system.

---

## Design Principles

### 1. Contestability before persuasion

The goal is not to make explanations more persuasive.

The goal is to make decisions contestable.

### 2. Separation over self-attestation

A system should not be the sole generator, recorder, explainer, and verifier of its own decision.

### 3. Evidence before explanation

Explanations should be checked against committed evidence.

### 4. Explicit custody assumptions

Every verification claim depends on custody assumptions.

Those assumptions should be stated, not hidden.

### 5. Low NDC is information

A low NDC reveals capture or weak separation.

It should not be hidden.

### 6. Cryptography is necessary but not sufficient

Digital signatures, hashes, timestamps, and Merkle trees can strengthen evidence.

They do not by themselves create institutional accountability.

### 7. Verification must survive outside the generator

The strongest verification path is one that does not depend solely on the same system that produced the decision.

---

## Example Use Cases

### Public Administration

A citizen is denied access to a benefit by an automated eligibility system.

A-DAP would require the decision to have been committed with reconstructible evidence, so that a later reviewer can test the decision against the committed record rather than relying only on a narrative explanation.

### Healthcare

A triage system prioritizes or deprioritizes a patient.

A-DAP would preserve the relevant decision envelope so that the clinical, technical, and institutional basis of the decision can later be examined.

### Courts and Legal Automation

A judicial or administrative AI system assists with classification, prioritization, drafting, or recommendation.

A-DAP would help separate the decision-support record from later explanations and allow independent reconstruction of what the system committed at the time.

### Elections and Political Systems

An automated moderation or classification system affects political content.

A-DAP would help preserve contestable evidence of the decision path, policy reference, and output commitment.

### Finance and Eligibility

A model denies credit, insurance, or access to a service.

A-DAP would allow later contestation against a committed decision object rather than relying only on internal logs or generated explanations.

---

## Repository Structure

This repository may include:

```text
.
├── README.md
├── THREAT_MODEL.md
├── CONTRIBUTING.md
├── NOTICE.md
├── RELEASE_NOTES.md
├── QUICKSTART.md
├── architecture/
│   ├── envelope-bottleneck.md
│   ├── automated-ndc-v2.md
│   ├── input-provenance-boundary.md
│   ├── commit-latency-tradeoff.md
│   ├── signer-custody-boundary.md
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
├── solver/
│   └── README.md
└── examples/
```

The exact structure may evolve.

The conceptual boundary should remain stable:

A-DAP is about contestable decision records, not about claiming that any single implementation proves correctness, fairness, or accountability.

---

## Current Status

A-DAP is a developing architecture and research protocol.

It should be treated as experimental.

Some parts may be implemented as reference prototypes.

Some parts may remain conceptual or under adversarial review.

The repository should not be read as a mature compliance product.

It should be read as a technical and governance research artifact focused on the evidentiary foundations of automated decision contestability.

---

## Quickstart for Reviewers

A reviewer should begin by asking:

1. What decision is being committed?
2. What artifacts are included in the decision envelope?
3. When is the commitment created?
4. Who controls the commitment path?
5. Who controls the verifier?
6. Can the decision be reconstructed without relying solely on the generator?
7. What assumptions are required?
8. What is the NDC under those assumptions?
9. Where does the Envelope Bottleneck appear?
10. What would need to be compromised to falsify the record without detection?

A-DAP is strongest when these questions can be answered explicitly.

It is weakest when the system says:

“Trust us. We logged it.”

---

## Minimal Verification Questions

For any proposed A-DAP implementation, ask:

- Is the decision committed before or at the moment of action?
- Are inputs, outputs, policies, and model references bound to the record?
- Are artifacts canonicalized?
- Are hashes computed deterministically?
- Are signatures verifiable independently?
- Are timestamps external or merely internal?
- Is the verifier independent from the generator?
- Can the record be reconstructed by a third party?
- What happens if the operator is compromised?
- What happens if the signer is compromised?
- What happens if the verifier is compromised?
- What happens if the custody path is compromised?
- Can unfavorable records be omitted before commitment?
- Can unfavorable records be omitted before anchoring?
- Does NDC collapse to 1?
- If NDC collapses to 1, what component caused the collapse?

---

## Limitations

A-DAP is intentionally limited.

Its contestability operates downstream of the point of commitment.

A-DAP does not prove that an input was truthful.

It does not eliminate verification windows in asynchronous or batched systems.

It does not create independent evidentiary value when signer, custody, and verifier collapse into the same trust domain.

It does not solve all problems in AI governance.

It does not determine whether a decision should have been made.

It does not replace law, ethics, institutional review, safety engineering, or democratic accountability.

It cannot make an illegitimate institution legitimate.

It cannot make a false input true.

It cannot make an unfair policy fair.

It cannot guarantee that all relevant evidence will always be available.

It cannot prevent every form of collusion.

Its purpose is narrower:

to make it harder to alter, rewrite, or justify high-impact automated decisions after the fact without leaving detectable evidence under defined assumptions.

---

## Research Questions

Open questions include:

- How should NDC be formally computed across different system architectures?
- How should custody assumptions be represented?
- How should privacy-preserving decision envelopes be designed?
- How can affected parties verify records without exposing sensitive data?
- How should A-DAP interact with legal discovery, administrative review, and regulatory audits?
- How can independent verification be made practical without excessive operational burden?
- How should multimodal inputs be committed and reconstructed?
- How should systems handle non-deterministic model behavior?
- How can A-DAP avoid becoming another self-attesting compliance artifact?
- What forms of external review are sufficient to prevent verifier capture?
- How should input provenance boundaries be declared?
- How should verification windows be measured and disclosed?
- How should signer-custody collapse be detected before deployment?
- How should omission-at-origin risk be measured separately from alteration risk?

---

## Contribution Guidelines

Contributions are welcome when they improve clarity, falsifiability, implementation quality, or adversarial robustness.

Useful contributions include:

- threat-model critiques;
- examples of NDC collapse;
- reconstruction challenges;
- verifier improvements;
- canonicalization tests;
- custody-analysis diagrams;
- legal or regulatory mapping;
- privacy-preserving envelope designs;
- negative results;
- adversarial reviews.

Especially welcome:

- cases where A-DAP fails;
- cases where NDC collapses to 1;
- cases where a proposed verifier is not truly independent;
- cases where the architecture accidentally becomes self-attesting;
- cases where input provenance assumptions are unstated;
- cases where records can be omitted before commitment or anchoring;
- cases where signer, custody, and verifier collapse into one trust domain.

A-DAP should become stronger by being made harder to defend casually.

---

## Citation

Suggested citation:

```text
Santos, Ezio v.s. A-DAP — Auditable Decision Accountability Protocol. 
A contestability architecture for high-impact automated decisions.
```

---

## Notice

A-DAP is a research and architectural proposal.

It is not legal advice.

It is not a certified compliance framework.

It is not a guarantee of correctness, fairness, safety, or legality.

Use of A-DAP concepts, prototypes, or documentation should be accompanied by independent legal, technical, and institutional review.

---

## License

Add the applicable repository license here.

If no license is provided, all rights are reserved by default.

---

## Core Sentence

A high-impact automated decision should not merely be explained after the fact.

It should be born contestable.
