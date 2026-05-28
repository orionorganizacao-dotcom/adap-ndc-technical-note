# A-DAP — Auditable Decision Accountability Protocol

A-DAP is a contestability architecture for high-impact automated decisions.

Its core claim is intentionally narrow:

A-DAP makes later alteration of committed decision records detectable.

It does not prove that the original decision was true.

It does not prove that the decision was fair.

It does not eliminate trust in the operator at origin.

It does not guarantee detection.

Its value is stricter:

high-impact automated decisions should be born with a reconstructible evidentiary object, so that affected parties, auditors, regulators, or courts can later contest the specific decision against a pre-committed record.

A-DAP turns automated decisions from post-hoc explanations into contestable records.

---

## Executive Summary

A-DAP — Auditable Decision Accountability Protocol — proposes that high-impact automated decisions be committed before or at the moment of action through reconstructible decision envelopes.

A decision envelope is not a truth oracle.

It is a pre-committed evidentiary object that can later be reconstructed, examined, and compared against explanations, notices, logs, or operator claims.

A-DAP uses cryptographic commitments, canonicalization, timestamps, signatures, and optional independent anchoring to strengthen temporal integrity.

But cryptography does not prove truth.

A content-blind anchor can make retrospective rewriting detectable, but it cannot prove that the operator told the truth when the envelope was created.

Therefore, A-DAP’s defensible claim is not:

“the system proves the decision was correct.”

The defensible claim is:

“the system preserves a contestable record of what was committed at decision time.”

This project favors claims that survive adversarial review over claims that sound stronger but collapse under scrutiny.

---

## Core Problem

Many automated systems produce decisions that affect people, institutions, rights, access, credit, employment, benefits, medical triage, insurance, moderation, or public services.

After the decision, the affected party may receive:

- an explanation
- a score
- a reason code
- a denial notice
- a log excerpt
- a review response
- a post-hoc justification

But these artifacts often do not prove what actually existed at the moment of decision.

They may describe the decision.

They may summarize the decision.

They may justify the decision.

But they do not necessarily make the decision reconstructible.

A-DAP addresses this gap.

---

## Explanation Is Not Verification

A-DAP distinguishes between explanation and verification.

Explanation answers:

Why does the operator say this decision happened?

Verification asks:

Can an authorized reviewer reconstruct the committed decision state and test whether the later account matches it?

This distinction matters because a post-hoc explanation can be plausible without being independently testable.

A-DAP is designed to make the decision itself an object of verification, not merely an object of explanation.

---

## Core Architecture

A-DAP separates the decision process into distinct evidentiary layers.

At minimum, an A-DAP decision flow should include:

1. A decision envelope
2. Deterministic canonicalization
3. Cryptographic commitment
4. Pre-action or at-action timestamping
5. Verification procedure
6. Contestability path

The architecture is not based on trusting the system’s later narrative.

It is based on preserving the state required to reconstruct the decision.

---

## Decision Envelope

A decision envelope is a structured record containing the minimum information needed to reconstruct a decision.

Depending on the domain, it may include:

- decision identifier
- input commitments
- relevant policy version
- model or rule version
- threshold state
- decision output
- decision timestamp
- justification reference
- hash of the canonical envelope
- signature or commitment metadata
- external anchoring receipt, if available

The envelope should be generated before or at the moment of action.

A later explanation should be testable against the envelope.

---

## Commit Before Act

A-DAP follows a commit-before-act principle.

For high-impact decisions, the target architecture is commit-before-act: the relevant decision state should be committed before the decision becomes operationally effective, unless a documented emergency or latency exception applies.

This does not mean that every internal detail must be publicly disclosed.

It means the relevant decision state must be preserved in a form that can later be reconstructed by an authorized reviewer.

Without commit-before-act, the record can become a post-hoc artifact.

With commit-before-act, the decision leaves a pre-action evidentiary trace.

---

## Cryptography Is Not Truth

A-DAP uses cryptographic tools such as hashing, signatures, timestamps, and anchoring.

But cryptography has a boundary.

Cryptography can prove that a record existed at a certain time.

Cryptography can prove that a record was not later altered.

Cryptography can prove that a signature matches a key.

Cryptography cannot prove that the original record was truthful.

This distinction is central to A-DAP.

A hash can preserve a lie.

A timestamp can date a false claim.

A signature can authenticate an untrue envelope.

Therefore, cryptographic integrity must not be confused with decision truth.

---

## NDC — Non-Delegated Custody

NDC refers to the degree to which verification does not depend on a single actor’s exclusive custody or narrative.

The goal is not to eliminate trust completely.

The goal is to reduce single-point custody over the evidentiary record.

A system with low NDC may depend entirely on the operator’s own logs, explanations, and claims.

A system with stronger NDC introduces independent commitments, external anchors, reproducible verification, or disjoint custody points.

However, NDC must not be inflated.

An external timestamp does not automatically prove the truth of the content.

A content-blind anchor does not witness the decision itself.

A verifier controlled by the same operator does not create full independence.

A-DAP treats NDC as an architectural property, not a marketing claim.

---

## Disjoint Anchoring for Contestability

A-DAP distinguishes between decision explanation, temporal integrity, and decision verifiability.

The repository includes an architectural note on disjoint anchoring for contestability:

[`architecture/disjoint-anchoring-for-contestability.md`](architecture/disjoint-anchoring-for-contestability.md)

This note clarifies a critical boundary:

Content-blind independent anchoring can make retrospective rewriting detectable, but it does not prove that the operator truthfully described the decision at the moment the envelope was created.

In other words:

A-DAP with disjoint anchoring strengthens temporal contestability.

It does not, by itself, eliminate origin-time trust in the operator.

The correct claim is narrow:

A decision envelope, once canonically hashed and anchored outside the operator’s exclusive custody, cannot later be altered without detection.

The incorrect claim would be broader:

That anchoring alone proves the decision was truthful at origin.

This distinction matters for NDC.

For retrospective rewriting, an independent anchor adds a genuinely disjoint custody point only for that attack path.

For origin-time fabrication, content-blind anchoring remains limited unless additional mechanisms exist, such as independent input-source attestation, model-version registries, threshold registries, witnessed execution, or trusted execution evidence.

This preserves the central boundary of A-DAP:

A-DAP does not make every decision true.

A-DAP does not guarantee detection.

A-DAP makes later alteration of the committed decision record detectable.

---

## Contestability, Not Detection

A-DAP is not primarily a faster detection mechanism.

It does not guarantee that someone will inspect a decision immediately.

It does not guarantee that an auditor, court, regulator, or affected party will act at the right time.

The defensible claim is narrower:

A-DAP enables contemporaneous contestability.

That means the evidentiary object needed to contest the decision exists when the decision is challenged.

The claim is not:

A-DAP guarantees contemporaneous detection.

The claim is:

A-DAP makes the decision reconstructible and contestable from a committed record.

---

## Legal Review Is Not the Same as Reconstructibility

Legal systems may provide rights to review or contest automated decisions.

But a right to review does not automatically create a reconstructible decision record.

A person may have a formal right to ask for review while still depending on:

- the operator’s explanation
- internal logs
- generic reason codes
- summaries
- automated review
- post-hoc narratives

A-DAP does not replace legal rights.

It supplies a technical evidentiary substrate beneath them.

The goal is to make review testable.

---

## Credit as a Contestability Domain

Credit is a strong domain for A-DAP because decisions are individual, consequential, and often legally contestable.

A credit applicant may receive a denial reason such as:

- insufficient credit history
- high debt-to-income ratio
- recent delinquency
- low score
- income not verified
- policy criteria not met

But that explanation may not reveal:

- which model version was active
- which threshold was used
- which input values were considered
- which data source supplied each input
- which policy layer overrode the score
- whether the later explanation matches the committed decision state
- whether the record was reconstructed after the fact

A-DAP does not replace a denial notice.

It addresses the evidentiary gap that remains when legal review rights exist but the review process still depends on operator-controlled explanations, logs, or automated re-evaluation.

It allows the notice to be tested against a committed decision envelope.

---

## Epic Sepsis Case Role

The Epic Sepsis case should not be presented as proof that A-DAP uniquely detects model failure.

The failure was detected by retrospective external validation.

Its value is pedagogical.

It illustrates the gap between later performance validation and contemporaneous decision verifiability.

A-DAP would not eliminate trust in the operator at envelope creation.

It would constrain retrospective rewriting by committing the relevant input state, model version, threshold state, and decision envelope before action.

Therefore:

Epic Sepsis is an illustration of the temporal verifiability gap.

It is not a proof of exclusive detectability.

---

## What A-DAP Proves

A-DAP can prove that:

- a decision envelope existed at or before a given time
- the presented envelope matches or does not match its prior commitment
- a later record has or has not been altered
- a presented decision envelope matches a specific recorded state committed earlier
- a verification procedure can reconstruct the committed object

A-DAP does not prove that:

- the decision was correct
- the model was fair
- the operator was truthful at origin
- the inputs were accurate
- the policy was legitimate
- the decision should have been made
- every falsification attempt will be detected

This distinction is essential.

A-DAP is a verifiability architecture.

It is not a truth oracle.

---

## Threat Model

A-DAP is designed to resist some attacks but not all attacks.

### Retrospective rewriting

The operator changes the decision record after the fact.

A-DAP can help detect this if the original envelope hash was committed or anchored before alteration.

### Post-hoc narrative adjustment

The operator provides a later explanation that does not match the committed decision state.

A-DAP can help test the explanation against the envelope.

### Log alteration

The operator modifies logs after challenge, audit, litigation, or regulatory review begins.

A-DAP can help detect mismatch if the original decision commitment survives outside the altered log chain.

### Origin-time fabrication

The operator creates a false envelope at the moment of decision.

Basic A-DAP with content-blind anchoring does not solve this.

Additional origin-attestation mechanisms are required.

### Captured anchor

The anchoring authority colludes with the operator or allows retroactive manipulation.

A-DAP’s independence is weakened.

Mitigation may require multiple anchors, public audit trails, independent timestamping, or regulator-supervised anchoring.

---

## Future Layer: Origin Attestation

Origin-time fabrication requires stronger mechanisms than content-blind anchoring.

Possible future layers include:

- independent input-source attestation
- external model-version registry
- threshold registry
- policy registry
- witnessed execution
- trusted execution evidence
- regulator-controlled sampling
- auditor-controlled replay
- cryptographic commitments from upstream data sources
- split custody over decision components
- secure execution environments
- independent data provenance commitments

These mechanisms increase assurance.

They also increase cost, complexity, privacy exposure, regulatory burden, and trade-secret risk.

Therefore, they should not be silently implied by the basic A-DAP claim.

They are future or optional layers.

---

## Minimal Verification Flow

A minimal verification flow may look like this:

1. Retrieve the decision envelope.
2. Canonicalize the envelope using the defined schema.
3. Compute the envelope hash.
4. Compare the computed hash with the stored commitment.
5. Compare the commitment with any external anchoring receipt.
6. Verify timestamp and signature metadata where applicable.
7. Reconstruct the decision state from the envelope.
8. Compare the reconstructed state against later explanations, notices, or claims.

This process does not prove that the original envelope was truthful.

It proves whether the presented envelope matches the committed record.

---

## Repository Structure

Suggested structure:

```text
.
├── README.md
├── architecture/
│   ├── disjoint-anchoring-for-contestability.md
│   ├── envelope-bottleneck.md
│   ├── automated-ndc-v2.md
│   └── omega-plus-plus-reconstructible-verdicts.md
├── challenge/
│   └── gcd-001/
├── proofs/
│   └── README.md
├── solver/
│   └── README.md
├── THREAT_MODEL.md
├── CONTRIBUTING.md
├── QUICKSTART.md
├── NOTICE.md
└── RELEASE_NOTES.md
