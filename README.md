# A-DAP — Auditable Decision Accountability Protocol

A-DAP is a contestability layer for high-impact automated decisions affecting people.

It should not be read as a competing cryptographic audit-trail standard.

Its focus is narrower: whether the person affected by an automated decision can later reconstruct and challenge that specific decision against independently verifiable evidence.

Its core claim is intentionally narrow:

A-DAP makes later alteration of committed decision records detectable under defined custody assumptions.

It does not prove that the original decision was true.

It does not prove that the decision was fair.

It does not prove that the committed scope was complete.

It does not eliminate trust in the operator at origin.

It does not guarantee detection.

Its value is stricter:

high-impact automated decisions should be born with a reconstructible evidentiary object, so that affected parties, auditors, regulators, or courts can later contest the specific decision against a pre-committed record.

A-DAP helps turn automated decisions from post-hoc explanations into contestable records under declared assumptions.

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
- What was included in the envelope?
- Who decided what was included in the envelope?
- Can a third party later reconstruct the decision record?
- Can alteration be detected without relying solely on the same system that produced the decision?
- Can the affected person later challenge the specific decision against independently verifiable evidence?

A-DAP is designed for domains where automated decisions may affect rights, access, treatment, ranking, eligibility, enforcement, safety, or institutional outcomes.

Examples include:

- public-sector AI systems;
- medical triage and clinical decision support;
- judicial or administrative automation;
- credit, insurance, and eligibility decisions;
- election-related AI systems;
- high-impact moderation or enforcement systems;
- safety-critical autonomous workflows.

Each domain requires its own scope rules, disclosure constraints, custody model, and legal review.

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
- scoped by the operator itself;
- impossible to independently reconstruct.

In such systems, the affected party may receive an explanation without receiving evidence.

That is the distinction A-DAP is built around:

**explanation is not verification.**

**logging is not proof.**

**transparency is not contestability.**

**record integrity is not scope completeness.**

A system may explain itself while still leaving no independent way to test whether the explanation corresponds to the decision that was actually made.

A system may also produce a cryptographically valid envelope while omitting decisive variables, hidden criteria, upstream signals, or contextual conditions.

A-DAP addresses part of this problem by requiring decisions to be committed as evidentiary objects before or at the moment of action.

It does not, by itself, prove that the committed scope was complete.

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
- reconstruction;
- affected-party challenge;
- scope declaration.

The goal is to prevent the same system from silently producing a decision, rewriting the record, generating the explanation, defining the scope, and validating itself.

---

## What A-DAP Is Not

A-DAP does not prove that a decision was correct.

A-DAP does not prove that a decision was fair.

A-DAP does not prove that a model was unbiased.

A-DAP does not prove that an input was truthful.

A-DAP does not prove that all relevant variables were included.

A-DAP does not prove that all relevant criteria were disclosed.

A-DAP does not prove that the committed scope matched the real decision scope.

A-DAP does not eliminate institutional trust.

A-DAP does not remove the need for human review.

A-DAP does not guarantee that all tampering will be detected.

A-DAP does not solve full collusion between all parties in the custody chain.

A-DAP does not turn a bad policy into a good policy.

A-DAP does not create legal accountability by itself.

A-DAP produces a more limited but important object:

a committed, reconstructible decision record that can later be tested against claims, explanations, logs, notices, or regulatory obligations.

That object may still be incomplete if the operator controlled what entered the envelope.

---

## Relationship to Existing Provenance and Audit-Trail Standards

A-DAP does not claim novelty over cryptographic primitives or audit-trail infrastructure such as digital signatures, hash chains, timestamping, Merkle trees, transparency logs, external anchoring, completeness proofs, evidence packs, or tamper-evident records.

Those mechanisms are established tools and are already being developed in serious provenance and audit-trail ecosystems.

A-DAP should not be read as a replacement for VCP, VAP, LAP, transparency logs, timestamping systems, or cryptographic audit-trail standards.

Those systems address important infrastructure questions around integrity, completeness, ordering, provenance, anchoring, evidence packaging, and third-party verification.

A-DAP focuses on a narrower contestability question:

when an automated decision affects a person, what evidentiary structure must exist so that the affected party, an auditor, a regulator, or a court can later challenge that specific decision without relying only on the same system that produced it?

Its contribution is not the invention of cryptographic audit trails.

Its contribution is the affected-party contestability framing, the separation requirements for decision challenge, and NDC as a diagnostic measure of trust-domain capture.

In this sense, A-DAP is best understood as a contestability layer that may complement existing provenance and audit-trail standards.

Where provenance systems often focus on whether a record is intact, complete, anchored, and verifiable by a third party, A-DAP asks additional questions:

- is the evidence usable by the person affected by the decision to contest that decision?
- who controlled what entered the decision envelope?
- can the affected person challenge omitted scope?
- does the envelope fix the decision object or only the operator’s selected view of it?

A-DAP is therefore not a rival to provenance infrastructure.

It is a proposed layer, profile, or contribution focused on affected-party challenge, capture diagnostics, and scope awareness.

A-DAP also treats independent verification as a topology rather than a label attached to a single trusted entity.

See [`architecture/independent-verification-topology.md`](architecture/independent-verification-topology.md).

That note argues that verification is stronger when reconstruction can occur outside the generator through materially control-disjoint paths.

It should not be read as a claim that adding more nominal verifiers automatically increases independence.

Multiple verifiers that depend on the same envelope, custody path, API, signer, or operator-defined scope may still collapse into the same trust domain.

A related conceptual note is available in [`architecture/cryptographic-habeas-data.md`](architecture/cryptographic-habeas-data.md).

That note frames affected-party contestability as an analogical extension of habeas data for automated decisions.

It should not be read as a claim that cryptography proves fairness, truth, legality, or justice.

Its narrower function is to fix the contestable decision object so that later review, challenge, or dispute does not depend only on a mutable or unilateral record.

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

This distinction matters because a cryptographic audit trail can show that a record remained intact while still leaving unresolved whether the verifier, custody path, evidentiary envelope, or envelope scope was structurally independent from the system being evaluated.

NDC is meant to make that dependency visible.

It is therefore better understood as a capture diagnostic than as a certification score.

A low NDC is not an embarrassment to hide.

It is a warning that the architecture may still be asking the same envelope to generate, scope, preserve, and validate its own evidence.

NDC should not be computed only for post-commit alteration.

It should also be considered separately for:

- omission before commitment;
- scope capture;
- signer-custody collapse;
- verifier capture;
- input provenance failure;
- post-commit alteration.

A single global NDC score may hide the weakest path.

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
- verification artifacts;
- affected-party access or disclosure rules;
- scope declaration.

The envelope should not be confused with a mere log entry.

A log says something happened.

A decision envelope should allow a later verifier to test whether the record still corresponds to the committed decision state.

It should also help define what the affected person can access in order to contest the decision.

However, a decision envelope only fixes what was included in it.

It does not, by itself, prove that all relevant variables, criteria, upstream signals, hidden rules, or contextual conditions were included.

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

That record still depends on the scope rules that determine what must be committed.

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
- identifying whether verification depends on the same pipeline that produced the decision;
- checking whether the declared envelope scope satisfies required scope rules.

Reconstruction does not necessarily mean reproducing the model’s internal reasoning.

A-DAP is model-agnostic.

The goal is not to open the black box.

The goal is to preserve enough committed evidence that the decision can be contested.

Reconstruction verifies the relationship between committed elements.

It does not automatically prove that all relevant elements were committed.

---

### External Verification

A-DAP distinguishes between internal self-checking and external verification.

A system that generates a decision, stores the record, explains the decision, and verifies the record by itself remains structurally weak.

A system that also defines what enters the envelope without independent scope review remains vulnerable to scope capture.

The question is not only whether the record is cryptographically valid.

The question is also whether verification can leave the generator’s exclusive control.

A-DAP should not treat the “independent verifier” as a single magically trusted entity.

Independence is not a label attached to a verifier.

It is a topology of reconstruction outside the generator.

Verification paths only become meaningfully stronger when they are materially control-disjoint.

Multiple verifiers that depend on the same envelope, same custody store, same signing path, same API, or same operator-defined scope may still represent one trust path with several copies.

If verification depends on the same compromised envelope, the apparent proof may collapse into self-attestation.

See [`architecture/independent-verification-topology.md`](architecture/independent-verification-topology.md).

---

### Affected-Party Contestability

Affected-party contestability means that the person affected by a decision can access or invoke enough stable evidence to challenge that specific decision.

This is not the same as regulator audit.

It is not the same as internal compliance.

It is not the same as professional supervision.

It is not the same as a general public transparency claim.

Affected-party contestability asks whether the person who suffered the decision can contest the decision object itself, rather than only contesting a later explanation.

It also asks whether the person can challenge the adequacy of the committed scope.

If the operator alone decides what fields matter, then the affected person may receive a valid receipt for an incomplete decision object.

---

## The Envelope Bottleneck

A central risk in A-DAP analysis is the Envelope Bottleneck.

The Envelope Bottleneck occurs when the same evidentiary envelope controls too much of the trust path.

For example:

- the system generates the decision;
- the same system records the evidence;
- the same system explains the decision;
- the same system defines the envelope scope;
- the same system validates the record;
- the same custody path preserves all artifacts.

In that case, compromising or capturing the envelope may be enough to make a false, incomplete, or selectively scoped record appear valid.

This is why A-DAP focuses on separation.

The goal is not merely to add stronger logs.

The goal is to reduce the number of cases where one compromised component can control decision, record, explanation, scope, and verification simultaneously.

This also applies to nominally independent verifiers.

A verifier that reconstructs only through the same envelope may be organizationally external but evidentially dependent.

A-DAP therefore treats verifier independence as a structural property of the reconstruction topology, not merely as an institutional role.

---

## Scope Completeness Boundary

A-DAP can fix a decision object.

It cannot, by itself, prove that the decision object contains every variable, criterion, upstream signal, rule, model state, or contextual condition that should have been included.

This is the scope-completeness boundary.

A cryptographically valid envelope may still be evidentially incomplete if the operator controls what enters the envelope.

Integrity and completeness are different properties.

Integrity asks whether the committed object changed.

Completeness asks whether the committed object included what mattered.

A valid receipt may prove:

- this was the decision object emitted;
- this was the declared policy reference;
- this was the input hash included;
- this was the explanation hash fixed;
- this was the output committed.

But it may not prove:

- all relevant variables were included;
- all criteria were disclosed;
- all upstream signals were represented;
- all model features were committed;
- no hidden rule influenced the decision;
- no omitted variable changed the result;
- the declared scope matched the real decision scope.

See [`architecture/scope-completeness-boundary.md`](architecture/scope-completeness-boundary.md).

---

## Number of Distinct Compromises — NDC

NDC stands for Number of Distinct Compromises.

It estimates how many structurally distinct compromises would be required to falsify a decision record without detection under a stated architecture and threat model.

NDC is assumption-dependent.

It depends on architecture, custody, verifier independence, scope control, and what the analysis counts as a distinct compromise.

A simplified intuition:

- NDC = 1 means one compromise may be enough to falsify the record without detection.
- Higher NDC may indicate that multiple structurally distinct components would need to fail or collude.
- NDC is useful when it exposes hidden self-attestation.
- NDC is dangerous if presented as a certification score without clear assumptions.

The purpose of NDC is not to make every architecture look strong.

The purpose is to reveal where the architecture is weak.

An architecture may have higher NDC for post-commit alteration and still have NDC = 1 for scope capture if the operator alone controls what enters the envelope.

---

## Why Logs Are Not Enough

Logs are useful.

But logs are often controlled by the same system or organization whose decision is being questioned.

A log can be incomplete.

A log can be overwritten.

A log can be selectively disclosed.

A log can be generated after the fact.

A log can record that an event occurred without proving that the recorded event corresponds to the actual decision state.

A log can also omit the variables or upstream signals that mattered.

A-DAP does not reject logs.

It treats logs as insufficient by themselves.

A log becomes more evidentiary when it is connected to pre-commitment, independent verification, custody separation, reconstructible artifacts, and scope rules.

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

But even a committed explanation hash only fixes which explanation was given.

It does not prove the explanation was true, complete, adequate, or legally sufficient.

---

## Architecture Overview

A simplified A-DAP architecture contains:

1. Decision generation
2. Decision envelope creation
3. Scope declaration
4. Pre-action or at-action commitment
5. Cryptographic binding
6. Custody separation
7. External or independent verification
8. Reconstruction procedure
9. Contestation interface
10. Affected-party access or challenge path

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

A weak implementation can also use strong cryptography and still fail if the same actor controls the committed scope.

A stronger implementation should aim to make falsification, omission, or scope capture without detection require multiple structurally distinct compromises.

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
  "scope": {
    "scope_schema": "eligibility-decision-scope-v1",
    "included_fields": [
      "income",
      "age",
      "application_date",
      "risk_flag"
    ],
    "withheld_but_committed_fields": [
      "fraud_signal_hash",
      "internal_risk_score_hash"
    ],
    "excluded_fields_policy": "documented-scope-policy-v1"
  },
  "custody": {
    "operator": "system-operator",
    "verifier": "independent-verifier-or-path",
    "timestamp_authority": "external-or-declared"
  },
  "affected_party": {
    "access_model": "declared-disclosure-or-challenge-path",
    "receipt": "decision-receipt-or-reference"
  },
  "reconstruction": {
    "method": "documented-verification-procedure",
    "artifacts": [
      "input-reference",
      "output-reference",
      "policy-reference",
      "scope-reference",
      "verification-script-or-spec"
    ]
  }
}
```

This is only illustrative.

A real implementation must define canonicalization, custody assumptions, artifact availability, privacy boundaries, redaction rules, privilege constraints, disclosure models, scope rules, and verification procedures.

---

## Threat Model

A-DAP assumes that some actors may have incentives to alter, suppress, reinterpret, narrowly scope, or selectively disclose decision records.

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
- reconstruction failure due to missing artifacts;
- incomplete decision-envelope scope;
- operator-controlled field selection;
- hidden upstream variables;
- omitted decisive criteria;
- parallel ledgers or parallel scopes.

A-DAP also declares four structural boundaries that should not be hidden as ordinary implementation bugs:

- input provenance boundary;
- verification window boundary;
- signer, custody, and verification boundary;
- scope completeness boundary.

These boundaries define where A-DAP can preserve evidentiary integrity and where additional assumptions are required.

See:

- [`architecture/input-provenance-boundary.md`](architecture/input-provenance-boundary.md)
- [`architecture/commit-latency-tradeoff.md`](architecture/commit-latency-tradeoff.md)
- [`architecture/signer-custody-boundary.md`](architecture/signer-custody-boundary.md)
- [`architecture/scope-completeness-boundary.md`](architecture/scope-completeness-boundary.md)
- [`architecture/independent-verification-topology.md`](architecture/independent-verification-topology.md)
- [`architecture/example-verification-topology.md`](architecture/example-verification-topology.md)

A-DAP does not fully solve:

- total collusion among all relevant parties;
- hardware-level compromise outside declared assumptions;
- false input data that was already false at origin;
- incomplete decision-envelope scope;
- operator-controlled field selection;
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

A system should not be the sole generator, recorder, explainer, scoper, and verifier of its own decision.

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

They also do not decide what the envelope should have contained.

### 7. Verification must survive outside the generator

The strongest verification path is one that does not depend solely on the same system that produced the decision.

### 7.1 Independence is topology, not label

A verifier is not independent merely because it is external.

Verification becomes stronger when reconstruction paths are materially control-disjoint and can be executed outside the generator.

Multiple verifiers that share the same envelope, signer, custody path, API, or operator-defined scope may still collapse into one trust path.

### 8. The affected party is a contesting actor

The person affected by a decision should not be treated only as the subject of a record.

They should be able to become an actor in the contestation process.

### 9. Scope must be declared

A decision receipt should not silently rely on operator-defined scope.

The architecture should declare what the envelope includes, what it withholds, what it excludes, and who can challenge omitted scope.

---

## Example Use Cases

### Public Administration

A citizen is denied access to a benefit by an automated eligibility system.

A-DAP would require the decision to have been committed with reconstructible evidence, so that a later reviewer can test the decision against the committed record rather than relying only on a narrative explanation.

However, the receipt would still need scope rules defining which variables, criteria, upstream signals, policy versions, and overrides must be included or committed.

### Healthcare

A triage system prioritizes or deprioritizes a patient.

A-DAP would preserve the relevant decision envelope so that the clinical, technical, and institutional basis of the decision can later be examined.

But it would not prove that all relevant clinical context was included unless scope requirements were defined and independently reviewable.

### Courts and Legal Automation

A judicial or administrative AI system assists with classification, prioritization, drafting, or recommendation.

A-DAP would help separate the decision-support record from later explanations and allow independent reconstruction of what the system committed at the time.

The architecture would still need safeguards against omitted criteria, hidden policy rules, or incomplete disclosure of decision-support inputs.

### Elections and Political Systems

An automated moderation or classification system affects political content.

A-DAP would help preserve contestable evidence of the decision path, policy reference, and output commitment.

It would not, by itself, prove that the policy scope or relevant context was complete.

### Finance and Eligibility

A model denies credit, insurance, or access to a service.

A-DAP would allow later contestation against a committed decision object rather than relying only on internal logs or generated explanations.

The affected person may still need a way to challenge whether decisive variables or hidden scores were omitted from the envelope.

---

## Repository Structure

This repository may include:

```text
.
├── README.md
├── ROADMAP.md
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
│   ├── scope-completeness-boundary.md
│   ├── independent-verification-topology.md
│   ├── example-verification-topology.md
│   ├── cryptographic-habeas-data.md
│   ├── vap-lap-gap-analysis.md
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
    ├── gcd-001.md
    └── decision-receipt-poc/
        ├── README.md
        ├── generate_receipt.py
        ├── verify_receipt.py
        ├── run_all_scenarios.py
        └── scenarios/
            ├── non_issuance.py
            ├── split_view.py
            └── perfect_bad_decision.py
```

The exact structure may evolve.

The conceptual boundary should remain stable:

A-DAP is about affected-party contestability of decision records, not about claiming that any single implementation proves correctness, fairness, truth, legality, scope completeness, verifier independence, or accountability.

---

## Current Status

A-DAP is a developing research architecture and contestability proposal.

It should be treated as experimental.

The broad framing of A-DAP as a general cryptographic audit-trail or provenance framework should be retired.

Existing provenance ecosystems already address many infrastructure questions around signatures, anchoring, completeness, evidence packs, third-party verification, and domain profiles.

The strongest current role for A-DAP is narrower:

- affected-party contestability for high-impact automated decisions;
- NDC as a diagnostic measure of trust-domain capture;
- decision-envelope design for challenge, review, or dispute;
- scope-completeness boundary declaration;
- independent verification topology;
- possible compatibility with existing provenance and audit-trail standards.

The repository also includes a conceptual note on Cryptographic Habeas Data.

This note should be understood as a rights-oriented framing of affected-party contestability, not as a claim that cryptography can decide the legal or factual merits of a dispute.

See [`architecture/cryptographic-habeas-data.md`](architecture/cryptographic-habeas-data.md).

The repository also includes a minimal executable proof of concept for affected-party decision receipts.

See [`examples/decision-receipt-poc/`](examples/decision-receipt-poc/).

This PoC demonstrates a narrow claim: an affected person can hold a verifiable decision object emitted at the moment of a simulated automated decision.

It does not prove fairness, legality, truth, input correctness, scope completeness, or institutional legitimacy.

Its purpose is to test the minimum contestability object: a citizen-held receipt that can expose non-issuance, split-view reconstruction, and the limit case of a structurally valid receipt for a bad decision.

The current PoC demonstrates the minimum contestability object: a citizen-held decision receipt emitted in a simulated decision flow.

It proves that a decision record can leave the generator’s exclusive control.

It does not yet prove that the record is hard to falsify.

Full NDC computation, control-disjoint verification topology, external anchoring, threshold custody, scope validation, independent verifier distribution, and real-world detection incentives remain unimplemented research targets.

Under conservative assumptions, A-DAP v0 should be treated as an externalization baseline, not as a hardened evidentiary architecture.

See [`architecture/example-verification-topology.md`](architecture/example-verification-topology.md).

The transition from A-DAP v0 to A-DAP v1 is defined in [`ROADMAP.md`](ROADMAP.md).

A-DAP v0 externalizes the record.

A-DAP v1 should begin hardening the record.

Some parts may be implemented as reference prototypes.

Some parts may remain conceptual or under adversarial review.

The repository should not be read as a mature compliance product or as a rival audit-trail standard.

It should be read as a technical and governance research artifact focused on the evidentiary conditions under which a person affected by an automated decision can later contest that decision.

---

## Quickstart for Reviewers

A reviewer should begin by asking:

1. What decision is being committed?
2. What artifacts are included in the decision envelope?
3. When is the commitment created?
4. Who controls the commitment path?
5. Who controls the verifier?
6. Who decides what enters the decision envelope?
7. Can the decision be reconstructed without relying solely on the generator?
8. What assumptions are required?
9. What is the NDC under those assumptions?
10. Where does the Envelope Bottleneck appear?
11. What would need to be compromised to falsify the record without detection?
12. Can the affected person access enough stable evidence to challenge the decision?
13. Does the minimal decision receipt PoC demonstrate the claimed boundary, or does it only show a happy path?
14. Does the receipt fix the decision object, or only the operator’s selected view of the decision?
15. Are verifier paths materially control-disjoint, or are they several copies of the same trust path?

Reviewers can inspect the minimal PoC at [`examples/decision-receipt-poc/`](examples/decision-receipt-poc/).

The PoC intentionally includes adversarial scenarios for non-issuance, split-view receipts, and structurally valid bad decisions.

Reviewers can inspect the v0 to v1 transition plan at [`ROADMAP.md`](ROADMAP.md).

A-DAP is strongest when these questions can be answered explicitly.

It is weakest when the system says:

“Trust us. We logged it.”

It is also weak when the system says:

“Trust us. We included everything relevant.”

It is also weak when the system says:

“Trust us. The verifier is independent.”

without showing how the verifier reconstructs outside the generator’s control.

---

## Minimal Verification Questions

For any proposed A-DAP implementation, ask:

- Is the decision committed before or at the moment of action?
- Are inputs, outputs, policies, and model references bound to the record?
- Who decides what enters the decision envelope?
- Are all relevant variables, criteria, upstream signals, and policy references included or committed?
- Can the operator omit decisive fields while still producing a structurally valid receipt?
- Is scope completeness verified independently from the operator?
- Are artifacts canonicalized?
- Are hashes computed deterministically?
- Are signatures verifiable independently?
- Are timestamps external or merely internal?
- Is the verifier independent from the generator?
- Is verifier independence organizational, technical, custodial, economic, or merely declared?
- Can verification be executed outside the generator’s exclusive control?
- Do multiple verifier paths share the same envelope, signer, custody store, API, or operator-defined scope?
- Are verifier paths materially control-disjoint?
- Can the record be reconstructed by a third party?
- Can the affected party access a stable decision object?
- What happens if the operator is compromised?
- What happens if the signer is compromised?
- What happens if the verifier is compromised?
- What happens if the custody path is compromised?
- Can unfavorable records be omitted before commitment?
- Can unfavorable records be omitted before anchoring?
- Can decisive fields be omitted before envelope creation?
- Does NDC collapse to 1?
- If NDC collapses to 1, what component caused the collapse?
- Is NDC computed separately for alteration, omission, and scope capture?

---

## Limitations

A-DAP is intentionally limited.

Its contestability operates downstream of the point of commitment.

A-DAP does not prove that an input was truthful.

A-DAP does not prove that the decision envelope included every variable, criterion, upstream signal, or contextual condition that should have been included.

It fixes the committed object.

It does not, by itself, prove that the committed scope was complete.

A-DAP does not eliminate verification windows in asynchronous or batched systems.

A-DAP does not create independent evidentiary value when signer, custody, and verifier collapse into the same trust domain.

A-DAP does not solve all problems in AI governance.

It does not determine whether a decision should have been made.

It does not replace law, ethics, institutional review, safety engineering, or democratic accountability.

It cannot make an illegitimate institution legitimate.

It cannot make a false input true.

It cannot make an unfair policy fair.

It cannot guarantee that all relevant evidence will always be available.

It cannot prevent every form of collusion.

Its purpose is narrower:

to make it harder to alter, rewrite, or justify high-impact automated decisions after the fact without leaving detectable evidence under defined assumptions, and to help the affected person contest a fixed decision object rather than a mutable narrative.

That fixed object still depends on scope rules.

If the operator alone controls what enters the envelope, the receipt may preserve an incomplete view.

The current v0 PoC should not be interpreted as evidence that the record is hard to falsify.

It shows that the record can be externalized.

It does not yet show that falsification requires multiple materially distinct compromises.

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
- How can affected-party contestability be implemented on top of existing provenance standards?
- When is third-party verification insufficient for affected-party challenge?
- What evidence must be accessible to the affected person without violating privacy, privilege, or security constraints?
- How can NDC complement existing anchoring, completeness, and evidence-pack mechanisms?
- Should A-DAP be developed as a standalone framework, a domain profile, or a contribution to existing provenance ecosystems?
- How can affected-party contestability be framed without implying that cryptographic records prove fairness, truth, legality, or justice?
- What minimum decision object should an affected person be able to access in order to contest an automated decision?
- How should Cryptographic Habeas Data relate to classical habeas data, data protection rights, and automated decision review rights?
- What is the minimum executable proof of affected-party contestability?
- Does a citizen-held receipt provide a meaningful independence boundary, or is external anchoring required?
- How should a decision receipt PoC distinguish fixation of the contestable object from proof of fairness, legality, truth, or correctness?
- How should A-DAP distinguish record integrity from scope completeness?
- Who should decide which variables, criteria, and upstream signals must be included in a decision envelope?
- Can affected-party contestability exist if the operator controls the envelope scope?
- How can scope completeness be verified without exposing unnecessary sensitive data?
- Should NDC be computed separately for post-commit alteration, omission, and scope capture?
- How should A-DAP model independent verification as a topology rather than a single trusted entity?
- When do multiple verifiers increase NDC, and when are they merely redundant copies of the same trust path?
- What makes two verification paths materially control-disjoint?
- How should affected-party contestability work when individual harms are too diffuse to create strong adversarial incentives?
- How can reproducible verification code be paired with sufficient artifacts so that external reconstruction is meaningful rather than cosmetic?
- How should A-DAP v1 move from record externalization toward record hardening without overstating current capabilities?

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
- cases where multiple verifiers share the same material control vector;
- cases where verifier independence is only organizational, not evidential;
- cases where the architecture accidentally becomes self-attesting;
- cases where input provenance assumptions are unstated;
- cases where records can be omitted before commitment or anchoring;
- cases where signer, custody, and verifier collapse into one trust domain;
- cases where affected-party access is claimed but not actually usable for contestation;
- cases where a receipt verifies but decisive fields were omitted;
- cases where scope completeness is asserted only by the operator.

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

It is not a guarantee of correctness, fairness, safety, truth, legality, scope completeness, verifier independence, or accountability.

Use of A-DAP concepts, prototypes, or documentation should be accompanied by independent legal, technical, and institutional review.

---

## License

Add the applicable repository license here.

If no license is provided, all rights are reserved by default.

---

## Core Sentence

A high-impact automated decision should not merely be explained after the fact.

It should be born contestable.
