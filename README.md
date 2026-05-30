# A-DAP — Auditable Decision Accountability Protocol

A-DAP is a contestability architecture for high-impact automated decisions.

It asks a simple question:

When an automated system makes a decision that affects someone, can that decision later be independently reconstructed?

## Mass Adoption Intro

AI systems are increasingly making decisions in credit, healthcare, public services, employment, insurance, education, security, fraud detection, and compliance.

The problem is not only whether these systems are accurate, fair, or explainable.

The deeper problem is this:

When something goes wrong, can the decision be reconstructed outside the system that made it?

Too often, the same system or organization that makes the decision also controls the logs, explanations, reports, dashboards, and evidence used to review it.

That creates a structural weakness.

A-DAP proposes that high-impact automated decisions should be born with a reconstructible evidentiary object.

Not just a post-hoc explanation.

Not just a report.

Not just internal logs.

Not just a promise that the system behaved correctly.

A decision should leave behind a record that can later be challenged, reconstructed, and compared against what the system, operator, or institution claims happened.

A-DAP does not make the decision automatically true.

It does not prove that the decision was fair.

It does not eliminate trust.

It does not replace courts, regulators, auditors, or human review.

Its purpose is narrower:

To make automated decisions more contestable by structure.

In short:

A-DAP separates the decision from the proof of what happened.

It turns automated decisions from explanations we are asked to trust into records that can be tested.

## Core Claim

A-DAP makes later alteration of committed decision records detectable under defined custody, materiality, and verification assumptions.

It does not prove that the original decision was true.

It does not prove that the decision was fair.

It does not eliminate trust in the operator at origin.

It does not guarantee detection.

Its value is narrower:

High-impact automated decisions should be born with a reconstructible evidentiary object, so that affected parties, auditors, regulators, or courts can later contest the specific decision against a pre-committed record.

## Executive Summary

A-DAP proposes that high-impact automated decisions be committed before or at the moment of action through reconstructible decision envelopes.

A decision envelope is a pre-committed evidentiary object that can later be reconstructed, examined, and compared against explanations, notices, logs, or operator claims.

A-DAP uses ordinary cryptographic primitives such as hashing, signatures, timestamping, and reproducible reconstruction rules.

Its goal is not to make automated decisions correct.

Its goal is to make later inconsistency detectable.

The protocol separates:

- the decision
- the record
- the explanation
- the verifier
- the authority interpreting the result

This separation is the core of the protocol.

## What A-DAP Is

A-DAP is:

- a protocol for reconstructible decision evidence
- a framework for contesting automated decisions after the fact
- a way to bind decision records before they can be rewritten
- an architecture for separating decision-making from later justification
- a method for making tampering, substitution, or unexplained inconsistency detectable under stated assumptions

A-DAP is designed for high-impact domains such as:

- credit scoring
- insurance
- public benefits
- hiring
- healthcare triage
- judicial or administrative decision support
- education access
- fraud detection
- compliance screening
- automated or semi-automated decision pipelines

## What A-DAP Is Not

A-DAP is not:

- a fairness metric
- an explainability method
- a model audit by itself
- a guarantee that a decision was correct
- a guarantee that a decision was lawful
- a guarantee that a decision was fair
- a substitute for courts, regulators, auditors, or institutional review
- a complete accountability system by itself

A-DAP does not answer:

“Was the decision right?”

It helps answer:

“Can we reconstruct what the system committed to at the time of decision, and detect whether the later record diverges from that commitment?”

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

Then the system, or its operator, asks to be trusted about all three.

A-DAP exists to break that loop.

## Core Principle

A high-impact automated decision should produce a decision envelope at or before the moment of action.

That envelope should contain or commit to the minimum information needed to later reconstruct the decision event.

The envelope should be:

- canonicalized
- hashed
- signed or otherwise authenticated
- timestamped where possible
- linked to reconstruction rules
- verifiable by a party outside the original decision system

The purpose is not transparency for its own sake.

The purpose is contestability.

## The Decision Envelope

A decision envelope is the core evidentiary object in A-DAP.

A minimal envelope may include commitments to:

- decision identifier
- timestamp or timestamp claim
- policy or model version
- input commitment
- output commitment
- relevant rule or threshold commitment
- operator identity or system identity
- canonicalization method
- hash algorithm
- signature method
- reconstruction instructions
- custody assumptions
- materiality assumptions
- verification metadata

The exact contents depend on the domain and privacy constraints.

A-DAP does not require publishing sensitive personal data.

It requires that the relevant decision state be committed in a way that can later be reconstructed or challenged under defined conditions.

## Commit Before Explain

A-DAP is based on a temporal rule:

Commit before explain.

The commitment must exist before the operator has an opportunity to rewrite the record in response to challenge, litigation, audit, or public pressure.

A post-hoc explanation may be useful.

But without a prior commitment, it cannot prove that it corresponds to the original decision state.

A-DAP does not reject explanations.

It limits what explanations can prove.

## Auditability Is Not Explainability

Explainability asks:

“Why did the model say this?”

Auditability asks:

“Can an independent party reconstruct what the system committed to, and detect whether the later account diverges from it?”

These are different problems.

A system can be explainable but not auditable.

A system can produce natural-language reasons while still lacking a reconstructible evidentiary record.

A-DAP focuses on the second problem.

## Accountability Requires Institutions

A-DAP does not itself create accountability.

Accountability requires:

- legal authority
- procedural rights
- institutional capacity
- remedies
- enforcement
- human judgment

A-DAP produces a stronger object for those institutions to inspect.

It turns a dispute from:

“Trust our explanation.”

into:

“Compare this explanation against the committed record.”

## Effective Contestability

A-DAP creates reconstructible decision records, but reconstructibility is not the same as exercised contestability or institutional accountability.

Structural NDC describes the independent verification paths available in the architecture.

ADAP-EXP-003.md introduces Effective NDC: the expected number of verification constraints that are actually exercised.

This matters because a system may expose multiple verification paths while still facing little real-world contestation if affected parties, auditors, or regulators do not reconstruct the decision record.

ADAP-EXP-003.md formalizes this gap as Exercise Debt.

A-DAP can increase structural verifiability.

It does not guarantee that verification will be exercised, nor that accountability will follow automatically.

## Structural NDC

NDC means Non-Dependency Count.

In this repository, NDC is a proposed conceptual measure, not an established industry standard.

NDC describes how many genuinely independent verification paths exist after collapsing dependencies.

The purpose of NDC is to avoid false multiplicity.

Five dashboards controlled by the same operator are not five independent verification paths.

Five logs generated by the same system are not five independent verification paths.

Five explanations produced by the same model are not five independent verification paths.

The independence of verification matters more than the quantity of artifacts.

## Computable NDC Separability Criterion

A-DAP is not defined by the presence of logs, dashboards, explanations, signatures, timestamps, read-only access, or an external auditor alone.

A-DAP requires a computable separability test.

The relevant question is:

Who materially controls the generation, inscription, preservation, verification, and reconstruction path of the evidentiary object?

If that path collapses into one material control domain, the system remains NDC=1.

This applies regardless of dashboards, logs, signatures, regulatory language, read-only access, or formal third-party labels.

The canonical criterion is defined in:

architecture/ndc-separability-criterion.md

In short:

A-DAP is satisfied only when the custody graph of a high-impact automated decision yields a reproducible Non-Dependency Count greater than 1 for the critical path between decision generation, record inscription, preservation, verification, and reconstruction.

A-DAP is not a claim that an auditor is external.

It is a procedure for making measurable whether verification still depends on the verified.

## Materiality and NDC Scope

NDC is not an absolute property of a system.

NDC is a property of a system under a declared materiality model.

An NDC score is only meaningful when the audit defines which custody domains, dependencies, collapse rules, and verification paths are considered material.

If the same actor selects the materiality model, applies it to the custody graph, and benefits from the resulting NDC claim, the result remains self-attested at the criteria layer.

For this reason, materiality claims should be at least one of the following:

- externally anchored
- adversarially contestable
- independently reproducible

Otherwise, the NDC result should be labeled as an internal diagnostic, not as an independent audit claim.

Related file:

architecture/non-self-attested-materiality.md

## Structural Independence and Economic Resistance

A-DAP distinguishes structural independence from economic resistance.

Structural independence asks:

“Are the verification paths materially disjoint after dependency collapse?”

Economic resistance asks:

“Is the expected cost of fraud, capture, suppression, or manipulation greater than the expected benefit of keeping the fraud hidden?”

These are related, but they are not the same.

A system is not independent merely because fraud is expensive.

A system is structurally independent only when an attacker must compromise materially separate custody, verification, or accountability paths.

A-DAP does not make fraud impossible.

It helps make hidden fraud more structurally exposed, more costly to sustain, and easier to contest under stated assumptions.

## Known Failure Modes and Boundary Risks

A-DAP includes several known risks and limitations.

### The Envelope Bottleneck

If every verification path depends on the same envelope, operator, interface, or custody channel, apparent independence may collapse.

Related file:

architecture/envelope-bottleneck.md

### Automated NDC Analysis

Automated NDC tooling may help expose where trust is still concentrated.

It does not prove that verification is independent.

Related file:

architecture/automated-ndc-v2.md

### Reconstructible Verdicts

A verifier can become another system asking to be trusted.

Automated verdicts should expose their evidence, rules, intermediate steps, and assumptions.

Related file:

architecture/omega-plus-plus-reconstructible-verdicts.md

### Adoption Capture Risk

A powerful operator may adopt A-DAP vocabulary and artifacts while preserving control over scope, receipt delivery, verification access, and actual exercise.

Formal adoption alone does not prove accountability.

Related file:

architecture/adoption-capture-risk.md

### Exercisable Verification Interface

A verification interface should not become a new authority.

The goal is not:

“Trust the validator.”

The goal is:

“Run the same open procedure over the same receipt and obtain the same result.”

Related file:

architecture/exercisable-verification-interface.md

### Exercisable Citizen Verification

A-DAP only becomes socially useful when reconstruction can be exercised without requiring the affected person to become a cryptographer.

A citizen-facing verification layer should help affected people, advocates, auditors, regulators, lawyers, journalists, and courts understand whether a later explanation matches the committed decision record.

It should make verification usable without turning the interface into a new authority.

Related file:

architecture/exercisable-citizen-verification.md

### Verifier Funding Capture

A third-party verifier is not independent merely because it is organizationally separate.

Funding, access, scope, contract renewal, governance, and revocation dependencies must be analyzed.

Related file:

architecture/verifier-funding-capture.md

### IP Priority and Authorized Execution

A-DAP can support existence-by-date, externally anchored process evidence, and externally authorized execution evidence under stated custody assumptions.

It cannot prove copying, sole authorship, infringement, or authorized execution from output similarity, self-reported process narratives, or self-signed receipts.

Related file:

architecture/ip-priority-and-authorized-execution.md

### ZK-Proofs and TEEs

A-DAP can work alongside Zero-Knowledge Proofs and Trusted Execution Environments.

ZK-Proofs can help prove that a computation satisfies a defined statement without revealing all underlying data.

TEEs can help attest that specific code executed in a protected environment.

Both can strengthen verification.

But neither automatically proves:

- that the input was true or complete
- that the schema was sufficient
- that the circuit or code represented the right policy
- that the operator did not control the observation boundary
- that the anchor was independently reachable
- that verification was actually exercised
- that the verifier was institutionally independent

ZK-Proofs and TEEs can be useful components in an A-DAP architecture.

They do not replace dependency-collapse analysis, external reconstruction, custody review, or institutional accountability.

## Challenge Packages

This repository includes challenge packages intended to test A-DAP claims under defined conditions.

### GCD-001 — External Reconstruction

GCD-001 is an external reconstruction challenge based on the German Credit Dataset.

Its purpose is to test whether a third party can reconstruct a committed decision object using the provided specification and materials.

Related files:

- challenge/gcd-001/README.md
- challenge/gcd-001/reconstruction-challenge.md
- challenge/gcd-001/reconstruction-spec.md
- challenge/gcd-001/submission-template.md
- challenge/gcd-001/reviewer-guidelines.md

### GCD-002 — Verifier Funding

GCD-002 tests whether a claimed third-party verifier remains independent when funding, access, scope, governance, and revocation dependencies are included in the custody graph.

It asks whether a verifier is materially independent, not merely formally separate.

Related files:

- challenge/gcd-002-verifier-funding/README.md
- challenge/gcd-002-verifier-funding/experiment-spec.md
- challenge/gcd-002-verifier-funding/custody-graph.json
- challenge/gcd-002-verifier-funding/expected-findings.md
- challenge/gcd-002-verifier-funding/submission-template.md
- challenge/gcd-002-verifier-funding/reviewer-guidelines.md

### GCD-003 — Internal Integrity Sensor

GCD-003 tests whether an internal integrity sensor increases NDC or collapses into the operator’s control domain under conservative dependency analysis.

It asks whether the sensor is truly an independent constraint or merely another operator-controlled artifact.

Related files:

- challenge/gcd-003-internal-integrity-sensor/README.md
- challenge/gcd-003-internal-integrity-sensor/experiment-spec.md
- challenge/gcd-003-internal-integrity-sensor/custody-graph.json
- challenge/gcd-003-internal-integrity-sensor/expected-findings.md
- challenge/gcd-003-internal-integrity-sensor/submission-template.md
- challenge/gcd-003-internal-integrity-sensor/reviewer-guidelines.md

Internal measurement is not independent verification by default.

## Proofs, Claims, Timestamps, and Audits

This repository distinguishes between four things that are often confused.

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

proofs/README.md

## Solver Status

Any solver in this repository should be treated as experimental unless explicitly stated otherwise.

A solver may help reconstruct decision artifacts, verify hashes, or check consistency.

But a solver is not itself the source of truth.

A solver can contain bugs.

A solver can encode wrong assumptions.

A solver can falsely validate a flawed reconstruction.

Related file:

solver/README.md

## Threat Model

A-DAP assumes some things and does not attempt to solve others.

Examples of threats A-DAP can help expose:

- later alteration of decision records
- mismatch between explanation and committed record
- substitution of outputs
- inconsistent reconstruction
- missing or invalid commitments
- unverifiable custody claims
- dependency concentration

Examples of threats outside the basic scope:

- total collusion among all parties
- compromised hardware root of trust
- malicious timestamp authority
- false data at origin
- lawful but unfair decision logic
- incorrect model design
- institutional refusal to act on evidence

A-DAP does not eliminate trust.

It tries to locate where trust remains.

Related file:

THREAT_MODEL.md

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

## Repository Structure

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
│   ├── automated-ndc-v2.md
│   ├── cryptographic-habeas-data.md
│   ├── disjoint-anchoring-for-contestability.md
│   ├── envelope-bottleneck.md
│   ├── example-verification-topology.md
│   ├── exercisable-citizen-verification.md
│   ├── exercisable-verification-interface.md
│   ├── independent-verification-topology.md
│   ├── ip-priority-and-authorized-execution.md
│   ├── ndc-comparative-positioning.md
│   ├── ndc-separability-criterion.md
│   ├── non-self-attested-materiality.md
│   ├── omega-plus-plus-reconstructible-verdicts.md
│   ├── scope-completeness-boundary.md
│   ├── sdk-vs-external-audit-service.md
│   ├── signer-custody-boundary.md
│   └── verifier-funding-capture.md
├── challenge/
│   ├── gcd-001/
│   ├── gcd-002-verifier-funding/
│   └── gcd-003-internal-integrity-sensor/
├── proofs/
│   └── README.md
└── solver/
    └── README.md
```

The exact structure may evolve.

The important distinction is conceptual:

- architecture explains the theory
- challenge tests reconstruction
- proofs separate evidentiary categories
- solver contains experimental tooling
- threat model defines limits

## Quickstart for Reviewers

For a five-minute review:

1. Read the core claim at the top of this README.
2. Check what A-DAP explicitly does not claim.
3. Read architecture/ndc-separability-criterion.md.
4. Read THREAT_MODEL.md.
5. Inspect architecture/envelope-bottleneck.md.
6. Inspect ADAP-EXP-003.md.
7. Inspect architecture/non-self-attested-materiality.md.
8. Inspect architecture/exercisable-citizen-verification.md.
9. Run or review the reconstruction challenge in challenge/gcd-001/.
10. Try to identify where trust is still concentrated.

The best review is adversarial.

Do not ask only whether the protocol works.

Ask where it silently asks to be trusted.

## Design Discipline

A-DAP follows several design rules:

- Do not overclaim.
- Do not call inconsistency detection “truth.”
- Separate proof from explanation.
- Collapse false independence.
- Define separability as computation, not language.
- Commit before challenge.
- Make verification externalizable.
- Declare assumptions.
- Treat non-exercise as a real weakness.
- Treat adoption capture as a first-class risk.
- Do not turn the validator into an authority.
- Do not confuse client-side execution with independence.
- Do not confuse citizen-facing usability with independent verification.
- Do not confuse third-party verification with independent verification.
- Do not confuse priority evidence with plagiarism proof.
- Do not confuse process history with proof of origin.
- Do not confuse internal measurement with independent verification.
- Do not confuse cryptographic strength with independent contestability.
- Do not confuse structural independence with economic resistance.
- Do not confuse declared materiality with independent verification.

## Example Safe Use

A public agency uses an automated eligibility system.

At the moment of decision, the system creates a decision envelope committing to:

- applicant record hash
- rule version
- model version
- output
- threshold
- timestamp evidence
- reconstruction instructions

Later, the applicant challenges the denial.

An auditor reconstructs the envelope and discovers that the explanation sent to the applicant does not match the committed decision state.

A-DAP does not decide the legal remedy.

But it gives the auditor a concrete inconsistency to examine.

## Example Unsafe Use

A company says:

“Our AI decisions are accountable because we use A-DAP.”

This is not a valid claim.

A safer statement would be:

“Our system generates reconstructible decision envelopes designed to make later alteration or inconsistency detectable under stated assumptions.”

That statement is narrower and more defensible.

## Current Maturity

This repository should be read as an evolving technical note, protocol architecture, and adversarial review surface.

Some parts are conceptual.

Some parts are experimental.

Some parts are challenge-oriented.

Some parts are intended for adversarial review.

The project is not presented as a finished compliance product.

It is a structured attempt to formalize and test the conditions under which automated decisions can become externally contestable.

## Open Problems

A-DAP leaves several important problems open:

- How should exercise probability be measured in real institutions?
- How should privacy-preserving reconstruction work in sensitive domains?
- How should timestamp authority failure be handled?
- How should courts or regulators treat partial reconstruction?
- How should dependency collapse be standardized?
- How should reconstruction cost be reduced for affected parties?
- How should A-DAP interact with sector-specific legal duties?
- How should external reviewers be incentivized to actually verify?
- How should independent envelope scope be defined and enforced?
- How should adoption capture be detected before it becomes compliance theater?
- How should verification be made exercisable without turning the validator into a new authority?
- How should citizen-facing verification be made usable without weakening reproducibility?
- How should verifier funding, access, scope, governance, and revocation dependencies be disclosed and analyzed?
- How should ZK-Proofs and TEEs be integrated without hiding custody, input, schema, or exercise dependencies?
- How should materiality models be externally anchored?
- How should self-declared materiality be labeled in audit reports?
- How should A-DAP distinguish between adoption of its vocabulary and satisfaction of its separability criterion?

These are not minor implementation details.

They are part of the accountability problem.

## Contribution Guidelines

Contributions are welcome if they improve clarity, testability, threat modeling, or adversarial review.

Especially useful contributions include:

- attacks on the protocol
- dependency-collapse examples
- reconstruction failures
- false-independence cases
- adoption-capture scenarios
- verifier-funding capture scenarios
- citizen-facing verification critiques
- usability-versus-reproducibility critiques
- internal-integrity sensor collapse examples
- materiality-model critiques
- ZK-Proof and TEE integration critiques
- economic-resistance analysis
- envelope-scope critiques
- exercisable-verification interface designs
- canonicalization edge cases
- timestamping critiques
- privacy-preserving envelope designs
- legal interpretation notes
- empirical evidence about whether verification paths are actually exercised

Please do not contribute language that inflates the protocol beyond what it can prove.

Related file:

CONTRIBUTING.md

## Citation and Attribution

If referencing A-DAP, cite it as a protocol architecture for reconstructible decision evidence and contestability.

Do not describe it as a complete accountability solution.

Related file:

NOTICE.md

Suggested short description:

A-DAP is a protocol architecture for creating reconstructible evidentiary records around high-impact automated decisions, so that later alteration or inconsistency can be detected under stated assumptions.

## Release Notes

See:

RELEASE_NOTES.md

Release notes should document not only features, but also narrowed claims, removed overclaims, known weaknesses, and adversarial findings.

In this project, reducing a false claim is progress.

## Final Position

A-DAP is based on a narrow but important claim:

Automated decisions should not depend only on post-hoc explanation.

They should produce reconstructible evidence.

But reconstructible evidence is not truth.

Structural contestability is not exercised accountability.

Formal adoption is not substantive contestability.

Validator output is not authority.

Client-side execution is not independent verification by itself.

Citizen-facing usability is not independent verification by itself.

Third-party verification is not independent verification by default.

Temporal priority is not plagiarism proof.

Historical process evidence is not proof of origin by itself.

Internal measurement is not independent verification by default.

Cryptographic strength is not independent contestability by itself.

Structural independence is not the same as economic resistance.

Declared materiality is not independent verification by itself.

A-DAP terminology is not A-DAP compliance.

A-DAP compliance requires a reconstructible custody graph and reproducible NDC computation.

If verification still depends on the verified, the system remains structurally dependent.

A-DAP helps create the object that later accountability may need.

It does not replace the institutions that must use it.
