# NDC Comparative Positioning

This document positions NDC, the Non-Disjointness Coefficient, against adjacent governance, explainability, cryptographic, verification, and audit mechanisms.

Its purpose is not to claim that NDC replaces any of these frameworks.

It does not.

The purpose is narrower:

To identify the specific failure surface that NDC measures and to distinguish it from surfaces already covered by existing tools.

---

## 1. Core Thesis

Most AI governance, security, and verification frameworks operate on one of the following surfaces:

1. Why a model produced an output.
2. Whether an artifact was altered.
3. Whether an artifact existed at a given time.
4. Whether a computation was performed correctly.
5. Whether code satisfies a specification.
6. Whether events were logged.
7. Whether an organization followed a governance process.

NDC asks a different question:

How many independent control domains must collude for a falsified decision record to pass without leaving evidence?

That question is not primarily about explanation, bit integrity, timestamping, mathematical correctness, or procedural compliance.

It is about custody disjunction.

The central claim is:

Existing mechanisms often assume custody separation as an operational condition. NDC treats custody separation as the object of measurement.

---

## 2. What NDC Measures

NDC measures the structural independence, or lack of independence, between the domains that generate, record, verify, and preserve evidence of a decision.

In simplified terms:

- NDC = 1 means the generator and verifier collapse into the same effective control domain.
- NDC greater than 1 means falsification requires compromising more than one independent control domain.
- Higher NDC indicates stronger custody disjunction, assuming the control domains are actually independent.

NDC does not prove that a decision was correct.

NDC does not explain why a model produced a result.

NDC does not guarantee that the underlying data was true.

NDC does not replace legal, institutional, or human accountability.

NDC measures the structural cost of undetected falsification across custody domains.

---

## 3. Comparative Table

| Framework | What it covers well | What it does not address | Gap occupied by NDC |
|---|---|---|---|
| LIME / SHAP | Feature attribution: why a model produced an output, locally or globally. | Does not address integrity of the custody record. It assumes that the output being explained is authentic. | Explanation is not verification. NDC does not ask why the model decided; it asks whether the decision record can be forged without evidence. |
| NIST AI RMF | Governance process, risk taxonomy, organizational practices, accountability language. | Not directly falsifiable or computable. It is primarily prescriptive: what an organization should do, not what it structurally costs to compromise a record. | NDC provides a measurable quantity where RMF provides governance direction. |
| Cryptographic attestation, such as Ed25519 signatures | Authorship and post-signature integrity of an artifact. | Does not by itself distinguish generator from verifier. If the signer controls the whole pipeline, self-signature collapses to trivial custody. | NDC measures the disjunction between who generates, records, and verifies, not merely whether a bitstring was signed. |
| RFC 3161 timestamping | Temporal existence proof: an artifact existed before a given time. | Does not prove that the content is true, independently generated, or disjointly custodied. It timestamps what it receives. | NDC operates over the custody graph, not only over a single temporal anchor. |
| Certificate Transparency | Public append-only logging for certificates; detection of improper certificate issuance through monitors and witnesses. | Domain-specific to PKI/TLS. Its trust model depends on ecosystem monitoring and public log behavior, not on a general decision-custody metric. | NDC generalizes the idea of detection by independent witness into a measurable custody-disjunction property for decision systems. |
| Zero-Knowledge Proofs | Proof that a computation was performed correctly without revealing private inputs. | Proves computational correctness under a protocol, but does not by itself measure operational independence of the prover, verifier, operator, and record custodian. Off-protocol collusion remains outside the proof. | NDC measures a premise that many ZK deployments rely on operationally: that verification is not controlled by the same effective actor as generation. |
| Formal verification and proof assistants | Mathematical assurance that code satisfies a specification. | Verifies conformance to a specification, but not the custody independence of runtime records, operators, logs, or institutional control domains. | NDC is about the social, operational, and infrastructural custody pipeline, not only program properties. |
| Conventional audit logs / SIEM | Event recording, anomaly detection, operational monitoring, forensic support. | Logs often run inside the domain being audited. Administrators or insiders may control both the event and its record. | This is the canonical NDC = 1 case: self-custodied logs do not prove much against an internal adversary. |

---

## 4. The Pattern

The comparison reveals a recurring pattern.

Existing mechanisms tend to answer one of these questions:

- Why did the model decide this?
- Was this artifact altered?
- Did this artifact exist before time t?
- Was this computation performed correctly?
- Does this code satisfy the specification?
- Was an event recorded?
- Did the organization follow a process?

NDC asks:

How many independent control domains must fail or collude before falsification becomes invisible?

That is the missing layer.

Not because the other tools are weak.

They are strong in their own domains.

The gap exists because they usually assume custody separation instead of measuring it.

---

## 5. NDC Is Not a Replacement

NDC should not be framed as a substitute for the adjacent mechanisms listed above.

It is a complementary metric.

A mature system may require all of the following:

- Explainability to interpret model behavior.
- Cryptographic signatures to protect artifacts after commitment.
- Timestamping to provide temporal anchoring.
- Formal verification to constrain program behavior.
- Zero-knowledge proofs to verify computation under privacy constraints.
- Transparency logs or append-only ledgers to expose unauthorized mutation.
- Governance frameworks to organize institutional responsibility.
- NDC to measure whether evidence custody is structurally disjoint.

The stronger claim is not:

NDC replaces these frameworks.

The stronger claim is:

NDC measures a failure surface that these frameworks often leave implicit.

---

## 6. The Custody Collapse Problem

A system may appear well-governed while remaining structurally weak.

For example:

1. A model produces a decision.
2. The same system records the decision.
3. The same administrative domain controls the logs.
4. The same team can modify records.
5. The same organization verifies the audit trail.
6. The same report is submitted as evidence.

This system may contain:

- signed artifacts;
- timestamps;
- logs;
- access controls;
- dashboards;
- compliance documentation.

Yet if the same effective control domain can generate, alter, and validate the record, then the evidence structure collapses.

This is custody collapse.

In NDC terms, this is the dangerous region where apparent auditability masks NDC = 1.

The system has records, but the records do not create independent evidence against the domain that controls them.

---

## 7. Relationship to A-DAP

A-DAP is one possible architecture designed to increase verifiability by separating decision, record, justification, and verification roles.

However, this distinction is critical:

NDC is a measurement concept.

A-DAP is an implementation architecture.

The comparison in this document supports the need for NDC as a concept. It does not automatically prove that any specific A-DAP implementation achieves NDC greater than 1.

Under the Envelope Bottleneck proposition, an A-DAP implementation whose verifier shares the same control vector as the generator collapses back into trivial attestation.

In other words:

Calling something A-DAP does not grant custody disjunction.

NDC greater than 1 must be earned by architecture, not claimed by terminology.

---

## 8. Adversarial Limits

This section states the limits explicitly.

### 8.1 Gap Does Not Prove Practical Importance

Showing that a gap exists does not prove that the gap is practically important in every deployment.

The comparison demonstrates conceptual and architectural originality.

It does not, by itself, demonstrate field relevance.

Practical relevance requires documented cases where custody collapse caused a real failure that adjacent mechanisms would not have detected.

A strong future validation case would show:

1. A decision record was accepted as trustworthy.
2. The record was generated or preserved inside a collapsed custody domain.
3. Existing tools such as logs, signatures, explanations, timestamps, or governance checklists failed to reveal the problem.
4. An NDC-style analysis would have exposed the weakness before or during the failure.

Until such cases are documented, the claim should remain limited:

NDC identifies a non-covered failure surface.

It does not yet prove that this surface dominates real-world failures.

---

### 8.2 NDC Does Not Prove Truth

NDC measures custody disjunction.

It does not prove that the underlying data is true.

If false data enters the system before the decision process begins, NDC may preserve a falsified input with excellent integrity.

This is not a contradiction.

It means NDC is a custody metric, not a truth oracle.

NDC can show that a record was difficult to forge after commitment.

It cannot prove that the world represented by the record was accurate.

---

### 8.3 NDC Does Not Eliminate Trust

NDC does not eliminate trust.

It relocates and distributes trust.

A system with high NDC still depends on assumptions about:

- independence of control domains;
- security of cryptographic keys;
- correctness of verification procedures;
- integrity of external witnesses;
- resistance to collusion;
- clarity of the custody graph;
- operational discipline.

The benefit of NDC is not trustlessness.

The benefit is explicit measurement of where trust collapses into a single domain.

---

### 8.4 NDC Does Not Defeat Total Collusion

If all independent domains collude, NDC cannot prevent falsification.

This is outside the realistic protection boundary of any custody architecture.

NDC raises the cost of undetected falsification by requiring more independent actors or domains to fail together.

It does not make collusion impossible.

---

### 8.5 NDC Depends on Correct Domain Modeling

NDC is only as good as the control-domain model behind it.

If two systems appear separate but are controlled by the same actor, they should not be counted as independent.

Examples of false separation include:

- two services controlled by the same administrator;
- two repositories controlled by the same organization without external witness;
- two signatures generated by keys held by the same team;
- a verifier hosted inside the same infrastructure as the generator;
- a timestamp claim generated locally without external authority;
- an audit report produced by the same entity being audited.

A weak domain model can inflate NDC artificially.

This is why NDC analysis must be adversarial.

The first question is not how many components exist.

The first question is who can control them.

---

## 9. Minimal Claim Set

The defensible claim set is:

1. Existing frameworks cover important surfaces such as explainability, cryptographic integrity, timestamping, computational correctness, formal specification, process governance, and event logging.

2. These frameworks often do not treat custody disjunction as their primary measurable object.

3. NDC defines custody disjunction as the object of measurement.

4. NDC is useful when the main threat is not model opacity or bit tampering alone, but undetected falsification by a domain that controls both generation and verification.

5. NDC does not prove truth, correctness, fairness, legality, or accountability.

6. NDC greater than 1 must be demonstrated through actual architectural separation.

7. A-DAP is only meaningful as an implementation if it produces measurable custody disjunction.

---

## 10. Strong Form

The strong form of the argument is:

Explainability explains outputs.

Cryptography protects artifacts.

Timestamping anchors existence.

Formal verification constrains code.

Zero-knowledge proofs verify computation.

Governance frameworks organize responsibility.

Audit logs record events.

NDC measures whether the evidence of a decision is controlled by the same domain that produced the decision.

That is the distinct contribution.

---

## 11. Short README Version

Most governance tools ask one of three questions:

Why did the model decide this?

Was this artifact altered?

Was this computation correct?

NDC asks a fourth question:

How many independent control domains must collude for a falsified decision record to pass without evidence?

That is the missing layer.

Explainability explains outputs.

Cryptography protects bits.

Formal methods verify code.

Zero-knowledge proofs verify computation.

Audit logs record events.

NDC measures custody disjunction.

The claim is not that A-DAP replaces these frameworks.

It does not.

The claim is narrower and stronger:

Existing frameworks usually assume custody separation.

NDC makes custody separation measurable.

---

## 12. Repository Placement

Recommended path:

architecture/ndc-comparative-positioning.md

Recommended cross-links:

- README.md
- THREAT_MODEL.md
- proofs/README.md
- architecture/envelope-bottleneck.md
- challenge/gcd-001/README.md

Recommended README reference:

```md
### Comparative positioning

NDC does not replace explainability, cryptographic attestation, timestamping, formal verification, zero-knowledge proofs, or conventional audit logs.

It measures a different failure surface: custody collapse.

See architecture/ndc-comparative-positioning.md.
