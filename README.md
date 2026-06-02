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

- the decision;
- the record;
- the explanation;
- the verifier;
- the authority interpreting the result.

This separation is the core of the protocol.

## Executive Brief for Regulators and Courts

For non-technical readers, regulators, courts, public agencies, lawyers, ombuds offices, auditors, and institutional reviewers, this repository includes a short executive brief.

The brief explains A-DAP in plain language, including what it does, what it does not prove, how decision envelopes and human-readable receipts support contestability, and how regulators or courts can use A-DAP as an evidentiary review criterion.

Related file:

EXECUTIVE_BRIEF_FOR_REGULATORS_AND_COURTS.md

## What A-DAP Is

A-DAP is:

- a protocol for reconstructible decision evidence;
- a framework for contesting automated decisions after the fact;
- a way to bind decision records before they can be rewritten;
- an architecture for separating decision-making from later justification;
- a method for making tampering, substitution, or unexplained inconsistency detectable under stated assumptions.

A-DAP is designed for high-impact domains such as:

- credit scoring;
- insurance;
- public benefits;
- hiring;
- healthcare triage;
- judicial or administrative decision support;
- education access;
- fraud detection;
- compliance screening;
- automated or semi-automated decision pipelines.

## What A-DAP Is Not

A-DAP is not:

- a fairness metric;
- an explainability method;
- a model audit by itself;
- a guarantee that a decision was correct;
- a guarantee that a decision was lawful;
- a guarantee that a decision was fair;
- a substitute for courts, regulators, auditors, or institutional review;
- a complete accountability system by itself.

A-DAP does not answer:

Was the decision right?

It helps answer:

Can we reconstruct what the system committed to at the time of decision, and detect whether the later record diverges from that commitment?

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

- canonicalized;
- hashed;
- signed or otherwise authenticated;
- timestamped where possible;
- linked to reconstruction rules;
- verifiable by a party outside the original decision system.

The purpose is not transparency for its own sake.

The purpose is contestability.

## The Decision Envelope

A decision envelope is the core evidentiary object in A-DAP.

A minimal envelope may include commitments to:

- decision identifier;
- timestamp or timestamp claim;
- policy or model version;
- input commitment;
- output commitment;
- relevant rule or threshold commitment;
- operator identity or system identity;
- canonicalization method;
- hash algorithm;
- signature method;
- reconstruction instructions;
- custody assumptions;
- materiality assumptions;
- verification metadata.

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

Why did the model say this?

Auditability asks:

Can an independent party reconstruct what the system committed to, and detect whether the later account diverges from it?

These are different problems.

A system can be explainable but not auditable.

A system can produce natural-language reasons while still lacking a reconstructible evidentiary record.

A-DAP focuses on the second problem.

## Accountability Requires Institutions

A-DAP does not itself create accountability.

Accountability requires:

- legal authority;
- procedural rights;
- institutional capacity;
- remedies;
- enforcement;
- human judgment.

A-DAP produces a stronger object for those institutions to inspect.

It turns a dispute from:

Trust our explanation.

into:

Compare this explanation against the committed record.

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

If that path collapses into one material control domain, the system remains NDC = 1.

This applies regardless of dashboards, logs, signatures, regulatory language, read-only access, or formal third-party labels.

The canonical criterion is defined in:

architecture/ndc-separability-criterion.md

In short:

A-DAP is satisfied only when the custody graph of a high-impact automated decision yields a reproducible Non-Dependency Count greater than 1 for the critical path between decision generation, record inscription, preservation, verification, and reconstruction.

A-DAP is not a claim that an auditor is external.

It is a procedure for making measurable whether verification still depends on the verified.

## Objective-Indexed NDC

NDC should not be treated as a single universal system score.

Different adversaries pursue different objectives, and those objectives may cut different custody and verification graphs.

This repository distinguishes NDC by adversarial objective and object class, including:

- resistance to forged verification;
- resistance to evidence removal;
- resistance to recovery substitution;
- resistance to uncontrolled disclosure of sensitive or dangerous payloads.

This means A-DAP assurance should be interpreted as a vector of objective-indexed cuts, not as one scalar metric.

Related file:

architecture/objective-indexed-ndc.md

## Repository Custody Implication

A public repository may host evidence.

It should not be treated as the root of evidence.

If a repository, release archive, issue tracker, and account are all governed by the same platform and removal regime, they should be treated as a single custody node.

This does not make public repositories useless.

It means their role must be correctly classified.

A repository is a publication surface.

It is not, by itself, an independent evidentiary custody layer.

## Materiality and NDC Scope

NDC is not an absolute property of a system.

NDC is a property of a system under a declared materiality model.

An NDC score is only meaningful when the audit defines which custody domains, dependencies, collapse rules, and verification paths are considered material.

If the same actor selects the materiality model, applies it to the custody graph, and benefits from the resulting NDC claim, the result remains self-attested at the criteria layer.

For this reason, materiality claims should be at least one of the following:

- externally anchored;
- adversarially contestable;
- independently reproducible.

Otherwise, the NDC result should be labeled as an internal diagnostic, not as an independent audit claim.

Related file:

architecture/non-self-attested-materiality.md

## Structural Independence and Economic Resistance

A-DAP distinguishes structural independence from economic resistance.

Structural independence asks:

Are the verification paths materially disjoint after dependency collapse?

Economic resistance asks:

Is the expected cost of fraud, capture, suppression, or manipulation greater than the expected benefit of keeping the fraud hidden?

These are related, but they are not the same.

A system is not independent merely because fraud is expensive.

A system is structurally independent only when an attacker must compromise materially separate custody, verification, or accountability paths.

A-DAP does not make fraud impossible.

It helps make hidden fraud more structurally exposed, more costly to sustain, and easier to contest under stated assumptions.

## Proof Surface vs Payload

A-DAP separates proof surfaces from payloads.

Public proof objects may include:

- hashes;
- manifests;
- signatures;
- timestamp receipts;
- canonical schemas;
- verifier source code;
- reconstruction rules;
- public test vectors.

Sensitive payloads may include:

- personal data;
- medical records;
- credit inputs;
- private model outputs;
- protected decision records;
- confidential operational data.

Dangerous payloads may include:

- exploit code;
- weaponizable technical instructions;
- operational attack payloads;
- other materials where replication increases harm.

The correct pattern is:

Replicate the proof surface.

Do not replicate the sensitive payload.

Preserve reconstructability through controlled disclosure.

Prevent proof-surface inversion.

Availability is not a universal good.

For public proof objects, high availability strengthens auditability.

For sensitive or dangerous payloads, uncontrolled availability may increase harm.

## Non-Invertibility Rule

Replicating the proof surface is not automatically safe.

A proof surface may still leak sensitive payload structure through inference.

Therefore:

Replicable proof surfaces must be non-invertible with respect to protected payloads.

A proof surface is not safe to replicate merely because it excludes the raw payload.

If hashes, manifests, schemas, metadata, reconstruction rules, or structural descriptors allow practical inference of protected payload properties, the proof surface itself inherits sensitivity.

## Canonical Recovery Rule

A-DAP must preserve not only existence, but canonical recoverability.

A verifier must be able to determine whether the recovered artifact is the committed artifact, not merely an artifact with a plausible timestamp or similar structure.

A timestamp can prove that a digest existed at a time.

It does not, by itself, prove that the artifact later recovered by the verifier is the canonical artifact intended by the original commitment.

A-DAP must therefore preserve recovery paths capable of distinguishing committed objects from later substitutes, altered mirrors, cloned artifacts, or reanchored copies.

## Known Failure Modes and Boundary Risks

A-DAP includes several known risks and limitations.

### Input Truth Boundary

A-DAP can reconstruct what a system committed to using.

It cannot, by itself, prove that the committed input was true, complete, correctly captured, or faithful to the external world.

This distinction prevents A-DAP from being misused as proof that a decision was factually correct.

Related file:

architecture/input-truth-boundary.md

### Input Provenance Envelope

Decision envelopes reconstruct what the system committed to using.

Input provenance envelopes reconstruct how the system obtained what it used.

This distinction prevents weak input capture from being hidden behind strong decision reconstruction.

Related file:

architecture/input-provenance-envelope.md

### Random Audit Sampling

A-DAP creates reconstructible evidence, but reconstructibility is not the same as exercised verification.

Random audit sampling helps reduce Exercise Debt by making verification exercised, not merely possible.

This distinction prevents A-DAP evidence from becoming a strong lock that no one ever tests.

Related file:

architecture/random-audit-sampling.md

### Non-Terminal Verification and Perpetual Refutability

A-DAP does not treat any verification event as final.

An external execution may increase evidentiary confidence, but it does not become authoritative merely because of who performed it.

A friendly verifier, a neutral verifier, or an adversarial verifier can all produce useful evidence.

But no single verifier should be able to close the evidentiary record.

The core requirement is not trust in the verifier’s character, hostility, neutrality, or declared independence.

The core requirement is that the result remains reproducible, contestable, and refutable by future structurally disjoint verifiers.

In short:

A-DAP does not require trusted adversaries.

It requires unclosable verification.

A repository may be public, deterministic, signed, timestamped, and externally executable while still remaining verification-pending.

It becomes externally exercised only when a verifier actually reruns, reconstructs, or tests the committed procedure.

Even then, the result must remain open to future contradiction.

This distinction prevents a common form of audit theater:

- open materials without execution;
- friendly execution presented as final proof;
- closed audit reports that cannot be independently reproduced;
- adversarial-looking validation that is not structurally refutable;
- green-check verification treated as correctness, fairness, legality, or truth.

A-DAP’s evidentiary value comes from preserving the conditions under which any later verifier can rerun the same procedure over the same committed materials and detect divergence.

Therefore:

Open-but-dormant means externally executable, not externally verified.

Friendly-executed means operationally exercised, not finally proven.

Adversarially-reexecuted increases evidentiary pressure, but still does not close the record.

Terminal verification is incompatible with A-DAP’s core principle.

The adversary does not need to be present at the first verification event.

The adversary must remain possible.

No verification event is final.

Every verification result must remain permanently reproducible, contestable, and refutable.

Related file:

architecture/non-terminal-verification.md

### Limitation Claims Are Not Self-Validating

A model saying “I cannot access that” is not evidence that access was impossible.

A-DAP treats limitation claims as epistemic boundary claims. If a system declares that something cannot be accessed, verified, retrieved, or reconstructed, that claim should not be accepted as self-validating when it matters for contestability, accountability, user rights, institutional review, or high-impact decision-making.

At minimum, limitation claims require capability inventory, attempted verification or explicit non-verification, and epistemic downgrading when the verification process is not externally reconstructible.

However, this remains an internal heuristic unless the verification attempt itself is externally committed and independently reconstructible.

Related file:

architecture/self-validating-limitation-claims.md

### Adoption and Accessibility Risks

A-DAP can make automated decisions more reconstructible, but reconstructibility does not automatically make verification practically accessible.

A technically valid envelope may still be difficult for regulators, courts, affected individuals, public managers, journalists, lawyers, or civil society organizations to understand or exercise without usable tools, institutional support, or independent assistance.

This creates an adoption and accessibility risk: A-DAP may become technically robust but practically underused if verification remains too complex, costly, or expert-dependent.

Related file:

architecture/adoption-and-accessibility-risks.md

### Human-Readable Decision Receipt

A-DAP decision envelopes make automated decisions more reconstructible, but affected people should not be expected to understand raw JSON envelopes, hashes, timestamp tokens, custody graphs, or reconstruction scripts.

A human-readable decision receipt provides an accessible entry point to the technical envelope. It should identify the decision record, provide a receipt code or access path, explain what the receipt supports, explain what it does not prove, and preserve the person’s ability to contest input truth, policy validity, legality, fairness, or remedy.

A receipt without an envelope is only a notice.

An envelope without a receipt may be technically valid but socially inaccessible.

Related file:

architecture/human-readable-decision-receipt.md

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

Trust the validator.

The goal is:

Run the same open procedure over the same receipt and obtain the same result.

Related file:

architecture/exercisable-verification-interface.md

### Exercisable Citizen Verification

A-DAP only becomes socially useful when reconstruction can be exercised without requiring the affected person to become a cryptographer.

A citizen-facing verification layer should help affected people, advocates, auditors, regulators, lawyers, journalists, and courts understand whether a later explanation matches the committed decision record.

It should make verification usable without turning the interface into a new authority.

Related file:

architecture/exercisable-citizen-verification.md

### Citizen Verifier UI Specification

A-DAP should not stop at reconstructible evidence.

A citizen verifier should convert A-DAP evidence into a usable verification flow, allowing affected people to paste, upload, scan, or provide a receipt and receive a plain-language result.

The interface should show whether the explanation matches the committed record, what is missing, what remains operator-controlled, and what can be exported for review.

It should make verification usable without becoming a new trust authority.

Related file:

architecture/citizen-verifier-ui-spec.md

### Citizen-Facing Evidence Language

Citizen-facing verification must explain what the evidence proves, what it does not prove, and what remains contestable.

A verifier should not merely say Hash verified.

It should communicate scope, limits, exportable evidence, and possible next procedural steps without becoming a new authority.

Related file:

architecture/citizen-facing-evidence-language.md

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

- that the input was true or complete;
- that the schema was sufficient;
- that the circuit or code represented the right policy;
- that the operator did not control the observation boundary;
- that the anchor was independently reachable;
- that verification was actually exercised;
- that the verifier was institutionally independent.

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

## Experimental Work

This repository also includes early falsification experiments for concepts that are not yet certification claims.

### ADEC-001 — Escape Cost Under Fixed Adversary Class

ADEC-001 explores whether Adversarial Distribution Escape Cost can be operationalized under:

- a declared adversary class;
- a pre-registered escape boundary;
- a frozen operational envelope;
- a result-independent adversarial role;
- and a reproducible reporting format.

ADEC-001 does not certify an agent.

It does not prove bounded behavior.

It does not produce a universal robustness score.

It tests whether escape from a declared empirical distribution can be measured under controlled adversarial conditions.

Related file:

experiments/adec-001.md

Related issue:

#9 — Define ADEC-001 boundary conditions and adversary class

ADEC is experimental and must not be interpreted as a production certification metric.

Before ADEC can become a certification metric, it must survive at least one pre-registered falsification experiment.

### GCD-002 — Benchmark Custody Collapse

GCD-002 extends A-DAP from automated decision systems to frontier model evaluation.

It examines benchmarks as custody graphs and asks whether a benchmark score can still function as independent evidence when the evaluated model can recognize, infer, or optimize against the evaluation surface itself.

Core thesis:

The benchmark is no longer only measuring the model.

The model is also measuring the benchmark.

In this case, the score remains useful, but its evidentiary status changes.

It no longer reconstructs capability alone.

It reconstructs capability under evaluation-aware conditions.

GCD-002 argues that benchmark independence is not guaranteed merely because an evaluator is external.

A third-party evaluator may increase NDC compared to vendor self-reporting, but if the evaluated model can infer or optimize against the benchmark format, the evaluation surface itself may become part of the model’s strategic environment.

This creates a deeper custody problem:

Independent evaluator does not automatically mean independent measurement.

GCD-002 does not claim that benchmarks are useless.

It claims something narrower:

Benchmarks become structurally weaker as independent verifiers when the evaluated model can recognize, infer, or optimize against the evaluation surface.

The benchmark may still produce useful information.

But its evidentiary status changes from clean capability proof to performance evidence under evaluation-aware conditions.

This note is currently framed as a conceptual draft and pre-solver hypothesis.

Its manual NDC estimate must be falsified by execution, especially in two cases:

- when the verifier shares the same recognizable evaluation envelope;
- when the verifier uses a genuinely disjoint evaluation envelope.

Related file:

GCD-002_BENCHMARK_CUSTODY_COLLAPSE.md

Solver validation specification:

experiments/gcd-002-solver-validation.md

Related issue:

#12 — Run solver validation for GCD-002 Benchmark Custody Collapse

## Proofs, Claims, Timestamps, and Audits

This repository distinguishes between four things that are often confused.

### Claim

A statement made by the operator or author.

Example:

This decision record was generated at a certain time.

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

- later alteration of decision records;
- mismatch between explanation and committed record;
- substitution of outputs;
- inconsistent reconstruction;
- missing or invalid commitments;
- unverifiable custody claims;
- dependency concentration;
- recovery substitution;
- evidence revocation;
- uncontrolled disclosure of sensitive or dangerous payloads.

Examples of threats outside the basic scope:

- total collusion among all parties;
- compromised hardware root of trust;
- malicious timestamp authority;
- false data at origin;
- lawful but unfair decision logic;
- incorrect model design;
- institutional refusal to act on evidence.

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
8. Check whether the recovered artifact is canonical, not merely plausible.
9. Report mismatch, missing evidence, substitution risk, or successful reconstruction.
10. Interpret the result within the stated threat model.

This does not prove the decision was right.

It tests whether the later record is consistent with the earlier commitment.

## Repository Structure

```text
.
├── README.md
├── NOTICE.md
├── THREAT_MODEL.md
├── CONTRIBUTING.md
├── EXECUTIVE_BRIEF_FOR_REGULATORS_AND_COURTS.md
├── QUICKSTART.md
├── RELEASE_NOTES.md
├── ADAP-EXP-003.md
├── GCD-002_BENCHMARK_CUSTODY_COLLAPSE.md
├── 90-DAY-GO-NO-GO.md
├── architecture/
│   ├── adoption-and-accessibility-risks.md
│   ├── adoption-capture-risk.md
│   ├── automated-ndc-v2.md
│   ├── citizen-facing-evidence-language.md
│   ├── citizen-verifier-ui-spec.md
│   ├── cryptographic-habeas-data.md
│   ├── disjoint-anchoring-for-contestability.md
│   ├── envelope-bottleneck.md
│   ├── example-verification-topology.md
│   ├── exercisable-citizen-verification.md
│   ├── exercisable-verification-interface.md
│   ├── human-readable-decision-receipt.md
│   ├── independent-verification-topology.md
│   ├── input-provenance-envelope.md
│   ├── input-truth-boundary.md
│   ├── ip-priority-and-authorized-execution.md
│   ├── ndc-comparative-positioning.md
│   ├── ndc-separability-criterion.md
│   ├── non-self-attested-materiality.md
│   ├── non-terminal-verification.md
│   ├── objective-indexed-ndc.md
│   ├── omega-plus-plus-reconstructible-verdicts.md
│   ├── random-audit-sampling.md
│   ├── scope-completeness-boundary.md
│   ├── sdk-vs-external-audit-service.md
│   ├── self-validating-limitation-claims.md
│   ├── signer-custody-boundary.md
│   └── verifier-funding-capture.md
├── challenge/
│   ├── gcd-001/
│   ├── gcd-002-verifier-funding/
│   └── gcd-003-internal-integrity-sensor/
├── experiments/
│   ├── adec-001.md
│   ├── gcd-002-solver-validation.md
│   └── second-order-entity-ndc/
├── proofs/
│   └── README.md
└── solver/
    └── README.md
```

The exact structure may evolve.

The important distinction is conceptual:

- `architecture/` explains the theory;
- `challenge/` tests reconstruction;
- `experiments/` tests immature or falsifiable concepts before they become claims;
- `proofs/` separates evidentiary categories;
- `solver/` contains experimental tooling;
- `THREAT_MODEL.md` defines limits.

## Quickstart for Reviewers

For a five-minute review:

1. Read the core claim at the top of this README.
2. Check what A-DAP explicitly does not claim.
3. Read EXECUTIVE_BRIEF_FOR_REGULATORS_AND_COURTS.md for a non-technical overview.
4. Read architecture/ndc-separability-criterion.md.
5. Read architecture/objective-indexed-ndc.md.
6. Read THREAT_MODEL.md.
7. Inspect architecture/input-truth-boundary.md.
8. Inspect architecture/input-provenance-envelope.md.
9. Inspect architecture/random-audit-sampling.md.
10. Inspect architecture/non-terminal-verification.md.
11. Inspect architecture/self-validating-limitation-claims.md.
12. Inspect architecture/adoption-and-accessibility-risks.md.
13. Inspect architecture/human-readable-decision-receipt.md.
14. Inspect architecture/envelope-bottleneck.md.
15. Inspect ADAP-EXP-003.md.
16. Inspect architecture/non-self-attested-materiality.md.
17. Inspect architecture/exercisable-citizen-verification.md.
18. Inspect architecture/citizen-verifier-ui-spec.md.
19. Inspect architecture/citizen-facing-evidence-language.md.
20. Inspect experiments/adec-001.md.
21. Inspect GCD-002_BENCHMARK_CUSTODY_COLLAPSE.md.
22. Inspect experiments/gcd-002-solver-validation.md.
23. Run or review the reconstruction challenge in challenge/gcd-001/.
24. Try to identify where trust is still concentrated.

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
- Do not treat any verification event as final.
- Do not confuse client-side execution with independence.
- Do not confuse citizen-facing usability with independent verification.
- Do not confuse third-party verification with independent verification.
- Do not confuse priority evidence with plagiarism proof.
- Do not confuse process history with proof of origin.
- Do not confuse internal measurement with independent verification.
- Do not confuse cryptographic strength with independent contestability.
- Do not confuse structural independence with economic resistance.
- Do not confuse declared materiality with independent verification.
- Do not confuse repository publication with independent evidentiary custody.
- Do not confuse input commitment with input truth.
- Do not confuse input provenance with input truth.
- Do not hide weak input capture behind strong decision reconstruction.
- Do not confuse reconstructibility with exercised verification.
- Do not let random audits collapse into sampling theater.
- Do not turn cryptographic success into public-facing overclaim.
- Do not let a green checkmark imply correctness, fairness, legality, or truth.
- Do not confuse experimental escape-cost measurement with certification.
- Do not treat NDC as a single scalar score when adversarial objectives differ.
- Do not treat ADEC as a universal robustness score.
- Do not treat availability as a universal good across all object classes.
- Do not confuse benchmark score with clean capability proof.
- Do not confuse external evaluation with structurally independent measurement.
- Do not treat pre-solver NDC estimates as executed results.
- Do not treat limitation claims as self-validating.
- Do not confuse a model’s statement of inability with externally reconstructed impossibility.
- Do not confuse reconstructibility with practical accessibility.
- Do not assume affected people can exercise verification without usable tools or institutional support.
- Do not confuse a human-readable receipt with proof that the decision was correct.
- Do not confuse receipt delivery with envelope reconstruction.

## Example Safe Use

A public agency uses an automated eligibility system.

At the moment of intake, the system creates an input provenance envelope committing to:

- submission channel;
- input source;
- capture timestamp;
- user confirmation receipt;
- transformation rules;
- custody path from input capture to decision system.

At the moment of decision, the system creates a decision envelope committing to:

- applicant record hash;
- rule version;
- model version;
- output;
- threshold;
- timestamp evidence;
- reconstruction instructions.

The affected person receives a human-readable decision receipt with:

- a receipt identifier;
- a decision reference;
- a decision date;
- an issuing institution;
- a plain-language decision summary;
- a verification link or access path;
- a statement of what the receipt supports;
- a statement of what the receipt does not prove;
- a list of issues that may still be contested.

Later, the applicant challenges the denial.

An auditor reconstructs the input provenance envelope and the decision envelope.

The auditor can separate several questions:

- whether the receipt identifies a decision record;
- whether the input capture path is reconstructible;
- whether the system used the committed input;
- whether the explanation matches the committed record;
- whether the input itself was true;
- whether the rule, threshold, or remedy was lawful.

A-DAP does not decide the legal remedy.

But it gives the auditor a concrete evidentiary structure to examine.

## Example Unsafe Use

A company says:

Our AI decisions are accountable because we use A-DAP.

This is not a valid claim.

A safer statement would be:

Our system generates reconstructible decision envelopes designed to make later alteration or inconsistency detectable under stated assumptions.

Another unsafe statement would be:

A-DAP proves that the committed input was true.

This is not a valid claim.

A safer statement would be:

A-DAP records what the system committed to using; it does not prove what the world was.

Another unsafe statement would be:

Our input provenance envelope proves the external-world fact was true.

This is not a valid claim.

A safer statement would be:

The input provenance envelope records how the input entered the decision process under stated assumptions.

Another unsafe statement would be:

Random audits prove all decisions are correct.

This is not a valid claim.

A safer statement would be:

Random audit sampling periodically exercises reconstruction under a disclosed sampling model and reduces Exercise Debt.

Another unsafe statement would be:

Hash verified, therefore the decision is correct.

This is not a valid claim.

A safer statement would be:

The checked record matches the committed evidence within the declared verification scope.

Another unsafe statement would be:

A verification event proves the system is finally verified.

This is not a valid claim.

A safer statement would be:

This verification event adds evidence, but the result remains reproducible, contestable, and refutable by future structurally disjoint verifiers.

Another unsafe statement would be:

Our agent is certified as behaviorally bounded because it passed ADEC.

This is not a valid claim.

A safer statement would be:

ADEC-001 is an experimental falsification protocol for measuring observed escape resistance under a declared adversary class and pre-registered boundary conditions.

Another unsafe statement would be:

The benchmark improved, therefore the model’s general capability is proven.

This is not a valid claim.

A safer statement would be:

The benchmark score is evidence of performance under benchmark conditions; its evidentiary status depends on the custody structure of the evaluation.

Another unsafe statement would be:

The model said it could not access the source, therefore access was impossible.

This is not a valid claim.

A safer statement would be:

The model did not demonstrate access with the capabilities exposed in that execution context; whether access was impossible requires reconstructible verification or explicit limitation labeling.

Another unsafe statement would be:

A-DAP makes verification accessible because the envelope is reconstructible.

This is not a valid claim.

A safer statement would be:

A-DAP improves reconstructibility, but practical accessibility depends on usable tools, institutional support, independent assistance, and the ability of affected parties or their representatives to exercise verification.

Another unsafe statement would be:

The person received a receipt, therefore the decision was auditable.

This is not a valid claim.

A safer statement would be:

The receipt provides an access point to the decision record. Auditability depends on whether the corresponding envelope, verification path, custody assumptions, and reconstruction procedure are available and testable.

Another unsafe statement would be:

The receipt proves the decision was correct.

This is not a valid claim.

A safer statement would be:

The receipt identifies a decision record that may be checked against the corresponding A-DAP envelope. It does not prove correctness, fairness, legality, or input truth.

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
- How should A-DAP preserve perpetual refutability when verification is performed by friendly, captured, non-adversarial, or adversarial-looking reviewers?
- How should ZK-Proofs and TEEs be integrated without hiding custody, input, schema, or exercise dependencies?
- How should materiality models be externally anchored?
- How should self-declared materiality be labeled in audit reports?
- How should A-DAP distinguish between adoption of its vocabulary and satisfaction of its separability criterion?
- How should objective-indexed NDC be reported by solvers?
- How should recovery substitution be detected in public repositories and mirrors?
- How should proof surfaces be tested for practical invertibility?
- How should availability be optimized differently for public proof objects, sensitive payloads, and dangerous payloads?
- How should input provenance be separated from decision-state commitment?
- How should input capture NDC be reported separately from decision-envelope NDC?
- How should citizen-facing interfaces explain the difference between verified input commitment and disputed input truth?
- How should citizen-facing messages explain scope, limits, exportable evidence, and next procedural steps?
- How should random audit sampling reduce Exercise Debt in practice?
- How should random audit sampling avoid sampling theater?
- How should failed sampled audits trigger escalation, notice, or remediation?
- How should ADEC define reproducible adversary classes?
- How should ADEC report escape cost without collapsing into a universal robustness score?
- How should adversary compensation be disclosed so that adversarial testing does not become another captured verification layer?
- How should pre-registered escape boundaries be chosen before observing adversarial results?
- How should benchmark custody graphs be modeled when the evaluated system can infer the evaluator?
- How should benchmark envelopes be decomposed into prompt structure, rubric, task distribution, scoring function, harness, and public benchmark culture?
- How should independent evaluators prove that their measurement envelope is structurally disjoint from vendor-facing or training-recognizable benchmark surfaces?
- How should pre-solver NDC estimates be labeled so they do not become premature claims?
- How should capability claims distinguish between performance under benchmark conditions and externally reconstructible evidence of general capability?
- How should limitation claims be externally reconstructed when the relevant tools, permissions, or retrieval paths are controlled by the same generator or operator?
- How should tool-call evidence be committed without exposing sensitive prompts, files, credentials, or protected user data?
- How should AI systems label the difference between “not demonstrated,” “not checked,” “not exposed,” “policy-restricted,” and “impossible”?
- How can a regulator understand A-DAP without reading the full technical repository?
- How can a court interpret a decision envelope?
- How can an affected person obtain a receipt?
- What must a public agency disclose in a denial notice?
- Who pays for independent reconstruction?
- How can public-interest verifiers be funded without capture?
- How can citizen-facing tools avoid becoming new authorities?
- How can verification results be explained without overclaiming?
- How can NDC disagreement between auditors be recorded?
- How can dependency-collapse rules become reproducible?
- How can reconstruction be exercised at scale without becoming symbolic compliance?
- What minimum fields should a human-readable decision receipt contain?
- How should Receipt IDs be standardized across institutions?
- What should happen if a person has a receipt but cannot access the corresponding envelope?
- What should happen if the envelope exists but no usable verifier is available?
- How should receipts distinguish between internal timestamp claims and external timestamp evidence?
- How should receipts be delivered by email, SMS, postal notice, portal notification, printed document, or API response?
- How should receipts support legal representatives, guardians, public defenders, ombuds offices, and regulators?
- How should non-technical executive briefs be maintained without oversimplifying the protocol?
- How should courts cite or attach A-DAP evidence without treating it as a final legal conclusion?
- How should regulators translate A-DAP into procurement, audit, or enforcement criteria?

These are not minor implementation details.

They are part of the accountability problem.

## Contribution Guidelines

Contributions are welcome if they improve clarity, testability, threat modeling, or adversarial review.

Especially useful contributions include:

- attacks on the protocol;
- dependency-collapse examples;
- reconstruction failures;
- false-independence cases;
- adoption-capture scenarios;
- verifier-funding capture scenarios;
- citizen-facing verification critiques;
- citizen-facing evidence language critiques;
- usability-versus-reproducibility critiques;
- internal-integrity sensor collapse examples;
- materiality-model critiques;
- ZK-Proof and TEE integration critiques;
- economic-resistance analysis;
- envelope-scope critiques;
- exercisable-verification interface designs;
- citizen-verifier UI critiques;
- reconstruction-cost critiques;
- canonicalization edge cases;
- timestamping critiques;
- privacy-preserving envelope designs;
- recovery-substitution examples;
- proof-surface invertibility critiques;
- object-class availability critiques;
- input-truth boundary critiques;
- input-provenance critiques;
- random audit sampling critiques;
- sampling theater examples;
- ADEC adversary-class critiques;
- ADEC escape-boundary critiques;
- ADEC compensation-model critiques;
- benchmark custody collapse critiques;
- evaluation-envelope decomposition critiques;
- third-party benchmark independence critiques;
- limitation-claim self-validation critiques;
- epistemic boundary claim critiques;
- tool-call reconstruction critiques;
- adoption and accessibility critiques;
- regulator-facing explanation critiques;
- citizen-accessibility critiques;
- human-readable receipt critiques;
- receipt delivery critiques;
- receipt-versus-envelope critiques;
- executive-brief critiques;
- court-facing interpretation critiques;
- legal interpretation notes;
- empirical evidence about whether verification paths are actually exercised.

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
