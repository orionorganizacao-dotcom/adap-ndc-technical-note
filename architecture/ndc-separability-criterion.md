# NDC Separability Criterion

This document defines the computable separability criterion for A-DAP.

A-DAP is not satisfied by the presence of audit logs, explanations, dashboards, signatures, timestamps, read-only access, or an external auditor alone.

A-DAP is satisfied only when the custody graph of a high-impact automated decision yields a reproducible Non-Dependency Coefficient (NDC) greater than 1 for the critical path between decision generation, record inscription, preservation, verification, and reconstruction.

The central question is not:

Who can read the audit record after the fact?

The central question is:

Who materially controls the generation, inscription, preservation, verification, and reconstruction path of the evidentiary object?

If that path collapses into one material control domain, the system remains NDC=1, regardless of dashboards, logs, signatures, regulatory language, or read-only access.

---

## 1. Purpose

The purpose of this criterion is to prevent auditability from being reduced to a linguistic or compliance claim.

A system may claim that it is auditable.

A system may expose logs.

A system may provide explanations.

A system may allow a third-party auditor to read records.

A system may use cryptographic signatures.

A system may replicate a ledger.

A system may publish compliance reports.

None of these facts, by themselves, establish A-DAP separability.

A-DAP requires that the evidentiary object remain reconstructible when the operator is treated as adversarial.

This requires a computable procedure.

The separability criterion must therefore be expressed as a custody graph and evaluated through reproducible dependency analysis.

---

## 2. Core Definition

A-DAP separability is satisfied only if the decision custody graph produces a reproducible NDC greater than 1 across the critical evidentiary path.

The critical evidentiary path includes:

1. Decision generation
2. Record inscription
3. Record preservation
4. Record verification
5. Record reconstruction

A system that leaves this path under one material control domain remains NDC=1.

This is called the Envelope Bottleneck.

---

## 3. Non-Dependency Coefficient

The Non-Dependency Coefficient, or NDC, is defined as:

NDC = the minimum number of independent material control domains that must fail, collude, or be compromised in order for a relevant alteration, omission, delay, regeneration, or suppression to pass without detection.

Interpretation:

NDC = 1

The system depends on one material control domain.

The operator, or an equivalent single control domain, can compromise the evidentiary path.

The system has an Envelope Bottleneck.

The system does not satisfy A-DAP separability.

NDC greater than 1

Detection depends on more than one independent material control domain.

The evidentiary object has structural separability.

The strength of separability increases with the size and independence of the minimum dependency cut.

NDC indeterminate

The custody graph cannot be reconstructed with sufficient detail.

The system cannot claim A-DAP separability.

The correct classification is:

Unverifiable custody claim.

---

## 4. Material Control

Material control means the practical ability to influence the evidentiary object or the path through which it becomes contestable.

Material control includes the ability to:

- Generate the decision
- Select what is recorded
- Omit relevant information
- Delay inscription
- Regenerate the envelope
- Alter inputs
- Alter outputs
- Alter model or policy references
- Control signing keys
- Control the moment of signature
- Control the ledger
- Control replication
- Control timestamp submission
- Control verification tooling
- Control reconstruction tooling
- Control access to reconstruction artifacts
- Suppress or filter records
- Rewrite or replace metadata
- Define the audit view available to external parties

A party that can only read a record after inscription does not necessarily break the Envelope Bottleneck.

Read-only access is not structural separability if the operator controls what is written, when it is written, and how it is reconstructed.

---

## 5. Why External Auditors Are Not Enough

A common false separation pattern is:

The operator controls the decision system, envelope generation, ledger inscription, signing process, and dashboard.

An external auditor receives read-only access to the dashboard or replicated ledger.

This does not necessarily create A-DAP separability.

The external auditor may be institutionally external, but the evidentiary object may still be materially controlled by the operator.

The relevant distinction is:

External reader is not the same as independent inscription.

External auditor is not the same as independent reconstruction.

Read-only ledger access is not the same as independent custody.

A-DAP evaluates the control path, not the compliance role label.

---

## 6. Required Input to the Solver

The solver must receive a custody graph.

The custody graph should represent actors, systems, artifacts, control edges, verification edges, and external anchors.

The minimum input should include the following categories.

---

## 7. Decision Event

The graph should identify the decision event being evaluated.

Minimum fields:

- decision_id
- decision_timestamp_claim
- decision_system
- operator
- execution_environment
- decision_domain
- decision_type
- affected_party_class
- high_impact_status
- policy_or_model_reference
- version_reference

The solver should not assume that a decision timestamp is valid merely because it is declared.

Declared timestamps are claims unless independently anchored.

---

## 8. Actors

The graph should identify every relevant actor or control domain.

Examples:

- Decision operator
- Model provider
- Infrastructure provider
- Envelope generator
- Ledger operator
- Key custodian
- Timestamp authority
- Verifier
- Auditor
- Regulator
- Reconstruction party
- Storage provider
- Deployment administrator
- Policy owner
- Data provider
- Affected party
- Independent public mirror

For each actor, the graph should specify whether the actor is materially independent from the operator.

Independence must not be assumed from name, contract, branding, or institutional role alone.

---

## 9. Artifacts

The graph should identify all artifacts relevant to contestability.

Examples:

- Input data
- Output decision
- Model version
- Policy version
- Decision envelope
- Hash commitment
- Signature
- Signing key reference
- Timestamp request
- Timestamp response
- Ledger entry
- Merkle root
- Public anchor
- Audit report
- Reconstruction script
- Verification script
- Notice to affected party
- Explanation
- Human review record
- Appeal record
- External publication
- Independent mirror

Each artifact should be linked to the actor or control domain that can generate, alter, omit, delay, preserve, verify, or reconstruct it.

---

## 10. Control Edges

Control edges represent the ability to affect the evidentiary path.

The solver should identify whether each actor can:

- generate
- alter
- omit
- delay
- regenerate
- overwrite
- suppress
- sign
- timestamp
- store
- replicate
- verify
- reconstruct
- approve
- invalidate
- filter
- redact
- publish
- revoke
- rotate keys
- change policy reference
- change model reference
- change environment reference
- control access

The most important control edge is not who reads the record later.

The most important control edge is who controls the moment and content of inscription.

---

## 11. Verification Edges

Verification edges represent who can independently test the evidentiary object.

The solver should identify:

- Who can verify without permission from the operator
- Who can reconstruct without the operator dashboard
- Who can detect alteration using independently preserved artifacts
- Who can compare a later explanation against a prior commitment
- Who can validate timestamp evidence
- Who can validate signatures
- Who can validate hash commitments
- Who can validate Merkle inclusion
- Who can reproduce the reconstruction procedure
- What evidence remains valid if the operator disappears
- What evidence remains valid if the dashboard is unavailable
- What evidence remains valid if the operator refuses cooperation

A verification edge is weak if it depends on the same party that controls inscription.

---

## 12. External Anchors

External anchors may strengthen separability, but only if they are materially outside the operator’s control.

Examples:

- RFC 3161 timestamp token
- Independent timestamp authority
- Public hash publication
- Public Merkle root
- Independent replicated ledger
- Third-party signature
- Public repository commit
- Independent archive
- Regulator-held copy
- Court-held copy
- Affected-party-held receipt
- Independent reconstruction package

External anchors should be evaluated by control, not by label.

A timestamp service is not independent if the operator can decide selectively what gets timestamped and when, without detectable omission.

A public repository is not sufficient if the relevant object is committed only after the dispute.

A mirrored ledger is not sufficient if the mirror receives only operator-filtered records.

---

## 13. Critical Custody Path

The solver must identify the critical custody path.

The critical custody path is the path through which a decision becomes a contestable evidentiary object.

At minimum, this path includes:

Decision generation

Record inscription

Record preservation

Record verification

Record reconstruction

A-DAP evaluates whether this path remains reconstructible against the operator.

If a later auditor can only inspect what the operator chose to register, the custody path may still be NDC=1.

---

## 14. Minimum Dependency Cut

The solver must compute the minimum dependency cut.

The minimum dependency cut is the smallest set of material control domains whose failure, collusion, or compromise would allow a relevant evidentiary failure to pass without detection.

Relevant evidentiary failures include:

- Alteration of decision inputs
- Alteration of decision outputs
- Omission of a decision record
- Delayed inscription
- Regeneration of a record after the fact
- Selective logging
- Selective timestamping
- Suppression of unfavorable records
- Replacement of model or policy references
- Reconstruction using altered artifacts
- Verification through a controlled toolchain
- Dashboard-only auditability
- Loss of independent contestability

If the smallest such set has size 1, the system is NDC=1.

---

## 15. Basic Classification

The solver should classify the system into one of the following categories.

### A. NDC=1: Envelope Bottleneck

A single material control domain can compromise the evidentiary path.

Result:

Not A-DAP separable.

### B. NDC greater than 1: Structurally Separable

More than one independent material control domain must fail, collude, or be compromised for a relevant alteration to pass undetected.

Result:

A-DAP separability is present to the degree represented by the computed NDC.

### C. NDC Indeterminate: Unverifiable Custody Claim

The graph is incomplete, unavailable, ambiguous, or non-reconstructible.

Result:

The system cannot claim A-DAP separability.

---

## 16. False Positive Patterns

The following patterns may look like auditability but do not necessarily satisfy A-DAP separability.

### 16.1 Dashboard Auditability

The operator provides a dashboard showing logs, explanations, or decision history.

If the operator controls what enters the dashboard, the system may remain NDC=1.

### 16.2 Read-Only External Auditor

An external auditor receives read-only access to records.

If the operator controls inscription, the auditor may be external only at the viewing layer.

### 16.3 Internal Signatures

The system signs decision records using keys controlled by the operator.

If the operator controls the signing key and the inscription moment, the signature may authenticate the operator’s own envelope rather than establish separability.

### 16.4 Replicated Internal Ledger

The operator replicates a ledger across internal infrastructure.

Replication does not create separability if all replicas are controlled by the same material domain.

### 16.5 Post-Hoc Explanation

The system produces explanations after the decision.

Explanations may help interpretation, but they do not prove that the original decision path is reconstructible.

### 16.6 Compliance Report

A report states that the system is auditable.

A report is not a proof of separability unless the custody graph and NDC computation are reproducible.

### 16.7 Vendor-Certified Auditability

A vendor certifies its own auditability or pays a dependent party to certify it.

Institutional distance does not automatically create material independence.

### 16.8 Selective Timestamping

The system timestamps some records externally.

If the operator controls which records are timestamped, omission may remain undetectable.

### 16.9 Read-Only Ledger

A ledger is exposed to auditors or regulators.

If the operator controls what is written into the ledger, read-only access does not break the inscription bottleneck.

---

## 17. Positive Separability Patterns

The following patterns may increase NDC when implemented with material independence.

### 17.1 Independent Pre-Action Commitment

The decision envelope or its hash is committed before or at action time to an external anchor outside the operator’s unilateral control.

### 17.2 Independent Timestamping

A timestamp token is generated by an independent timestamp authority and can be verified without the operator.

### 17.3 Public or Third-Party Anchoring

A hash, Merkle root, or equivalent commitment is published to a public or independent medium.

### 17.4 Independent Reconstruction Package

A third party can reconstruct the evidentiary object without relying on the original dashboard or operator-controlled verifier.

### 17.5 Affected-Party Receipt

The affected party receives a commitment or receipt that can later be checked against the record.

### 17.6 Independent Verifier

Verification can be performed by third parties using reproducible code and preserved artifacts.

### 17.7 Non-Operator Key Custody

Critical signing keys are controlled outside the operator’s unilateral control.

### 17.8 Reproducible Solver

The NDC computation itself can be reproduced by third parties from the declared custody graph.

---

## 18. Procedure

The minimum procedure for evaluating A-DAP separability is:

Step 1: Declare the custody graph

Map all actors, systems, artifacts, keys, ledgers, timestamps, verifiers, and reconstruction paths.

Step 2: Label material control

For each actor or control domain, mark who can generate, alter, omit, delay, sign, preserve, verify, reconstruct, or suppress each artifact.

Step 3: Identify the critical custody path

Trace the path from decision generation to later contestable reconstruction.

Step 4: Compute the minimum dependency cut

Find the smallest set of material control domains whose failure, collusion, or compromise would prevent detection of a relevant alteration.

Step 5: Assign NDC

If the minimum cut is 1, classify the system as Envelope Bottleneck.

If the minimum cut is greater than 1, classify the system as structurally separable to the degree represented by NDC.

If the graph cannot be reconstructed, classify the claim as unverifiable.

---

## 19. Regulatory Capture Warning

Regulatory adoption of A-DAP terminology is not equivalent to A-DAP compliance.

A regulator may adopt terms such as:

- auditability
- decision envelope
- explainability
- external verification
- traceability
- audit logs
- trusted ledger
- independent review
- cryptographic proof

without adopting the A-DAP criterion.

A-DAP compliance requires third-party reconstruction of the custody graph and reproducible NDC computation.

If a regulation requires audit logs but not custody graph reconstruction, it does not require A-DAP separability.

If a regulation requires external auditors but not independent inscription or reconstruction, it does not require A-DAP separability.

If a regulation allows the operator to define the evidentiary object unilaterally, the system may remain NDC=1.

---

## 20. Canonical Test

The canonical A-DAP test is:

Can a third party reconstruct the custody graph and compute the same NDC without relying on the operator as the authority for the evidentiary claim?

If yes, the separability claim can be evaluated.

If no, the claim is not yet verifiable.

A-DAP is therefore not a claim of trust.

It is a procedure for detecting where trust is still being smuggled into the verification path.

---

## 21. Canonical Definition

A-DAP is satisfied only when the custody graph of a high-impact automated decision yields a reproducible Non-Dependency Coefficient greater than 1 for the critical path between decision generation, record inscription, preservation, verification, and reconstruction.

A system that exposes audit logs, explanations, signatures, dashboards, or read-only ledgers, but leaves generation, inscription, preservation, or verification under one material control domain, remains NDC=1 and does not satisfy A-DAP separability.

---

## 22. Short Definition

A-DAP is the procedure that makes measurable whether verification still depends on the verified.

---

## 23. Implication

The value of A-DAP is not that no one can copy its language.

The value of A-DAP is that any copied implementation that preserves the Envelope Bottleneck can be measured as NDC=1.

A captured version of A-DAP does not defeat the framework.

If it preserves dependency collapse, it becomes evidence for the framework.

---

## 24. Scope

This document defines the separability criterion only.

It does not prove that a decision is true.

It does not prove that a decision is fair.

It does not prove that a model is accurate.

It does not eliminate institutional trust.

It does not eliminate collusion risk.

It does not guarantee detection under total capture.

It does not replace legal accountability.

It defines a computable condition for determining whether the evidentiary path of a decision remains structurally separable from the operator.

---

## 25. Relation to A-DAP

A-DAP depends on this criterion because auditability cannot be established by the same envelope that creates the claim being audited.

Without separability, auditability becomes self-certification.

Without a custody graph, separability becomes rhetoric.

Without reproducible NDC computation, the custody graph becomes documentation rather than proof.

Therefore:

A-DAP requires text plus procedure.

The text defines the claim.

The graph defines the custody structure.

The solver computes the dependency cut.

The resulting NDC determines whether separability exists.

---

## 26. Final Principle

A-DAP does not ask whether the operator says the system is auditable.

A-DAP asks whether the evidentiary object survives when the operator is treated as adversarial.

If the answer depends on the operator, the system remains NDC=1.

If the answer can be reconstructed by independent parties through a reproducible custody graph and solver procedure, A-DAP separability becomes testable.

That is the criterion.
