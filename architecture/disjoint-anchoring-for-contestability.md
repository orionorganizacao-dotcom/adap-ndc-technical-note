# Disjoint Anchoring for Contestability

## Status

Architectural note. Scope-limited.

This document defines disjoint anchoring as a temporal contestability mechanism.

It does not define a complete proof of decision truth.

The purpose of this note is to prevent an overclaim:

A-DAP with independent anchoring can make retrospective rewriting detectable.

It cannot, by content-blind anchoring alone, prove that the operator truthfully described the decision at the moment the envelope was created.

## Core Claim

A content-blind anchoring authority can prove that a decision envelope, or a canonical hash of that envelope, existed at or before a given time outside the operator’s exclusive custody.

This protects against retrospective rewriting.

It does not protect against origin-time fabrication.

In precise terms:

A-DAP with independent anchoring does not prove that the operator truthfully described the decision at envelope creation time.

It proves that, once the envelope hash is anchored outside the operator’s exclusive custody, the operator cannot later rewrite the envelope without detection.

## Why This Matters

Many legal and institutional review mechanisms give affected parties a right to challenge or request review of automated decisions.

However, a right to review does not automatically create a reconstructible evidentiary substrate.

A person may receive:

- an explanation
- a generic reason code
- an adverse action notice
- a review response
- a summary of factors
- an operator-controlled log
- a post-hoc narrative

But none of these necessarily prove what decision state existed at the moment the decision was made.

A-DAP addresses this evidentiary gap by requiring a decision envelope to be committed before or at the moment of action, and by anchoring its canonical hash outside the exclusive custody of the operator.

The goal is not to replace legal review rights.

The goal is to make those rights testable against a pre-committed decision record.

## Contestability, Not Detection

This note follows a narrower thesis:

A-DAP is not primarily a faster detection mechanism.

A-DAP is a contestability architecture.

It does not guarantee that an auditor, regulator, court, or affected party will inspect the decision immediately.

It guarantees that, when inspection or contestation occurs, a pre-committed record exists and can be tested against an external temporal anchor.

The claim is not:

A-DAP guarantees contemporaneous detection.

The claim is:

A-DAP enables contemporaneous contestability.

In other words, the relevant guarantee is not that someone will discover the problem sooner.

The relevant guarantee is that the evidence needed to contest the decision exists when the decision is later challenged.

## Explanation Is Not Verification

A central distinction:

Explanation describes why the operator says a decision occurred.

Verification tests whether that account matches a committed decision state.

In domains such as credit, employment, benefits, insurance, and access to services, affected parties may receive some form of explanation. But an explanation is often not enough to reconstruct the decision.

A reconstruction requires, at minimum, evidence of:

- the relevant input state
- the model or rule version
- the active threshold or policy state
- the decision envelope
- the decision output
- the time of commitment
- the canonical hash
- the external anchoring receipt

Without this substrate, the affected person may have a right to contest but no independently testable object to contest.

## What Disjoint Anchoring Solves

Disjoint anchoring protects against retrospective rewriting.

If the operator later changes the envelope, the canonical hash no longer matches the externally anchored receipt.

This creates temporal resistance against:

- post-hoc narrative adjustment
- altered logs
- changed threshold claims
- substituted model-version claims
- retroactive reconstruction favorable to the operator
- selective disclosure of a different decision state
- later claims that a different policy was active
- later claims that a different input set was used

The anchor does not need to know the content of the decision.

It only needs to preserve a timestamped commitment to the envelope hash outside the operator’s exclusive custody.

This allows an authorized reviewer to ask:

Does the envelope presented today match the hash committed at the time of the decision?

If not, the record has been altered or substituted.

If yes, the record matches the earlier commitment.

That is a real gain.

But it is not a complete proof of truth.

## What Disjoint Anchoring Does Not Solve

Disjoint content-blind anchoring does not protect against origin-time fabrication.

If the operator creates a false but internally consistent envelope and anchors its hash at decision time, the anchoring authority will faithfully timestamp the hash of that false envelope.

The anchor is blind by design.

That blindness has advantages:

- it reduces exposure of personal data
- it protects trade secrets
- it supports data minimization
- it avoids requiring the anchor to process sensitive decision content
- it makes the anchoring layer operationally lighter

But the same blindness creates a hard limit:

The anchor cannot verify whether the envelope truthfully describes the decision state that actually ran.

Therefore, content-blind anchoring proves temporal existence, not origin truth.

## Threat Model

## Adversary 1: Retrospective Rewriter

The operator made a decision and later attempts to alter the record.

Examples:

- changing the claimed threshold after a complaint
- changing the claimed model version
- editing logs after litigation begins
- replacing the original envelope with a cleaner version
- producing a narrative that does not match the decision state at the time

Against this adversary, disjoint anchoring is effective.

The external receipt preserves the original commitment.

If the operator presents a modified envelope, the hash will not match the anchored commitment.

Result:

NDC improves for this attack path because the operator alone can no longer rewrite the committed record undetected.

## Adversary 2: Origin-Time Fabricator

The operator lies at the moment of envelope creation.

Examples:

- the operator runs model v3 but seals an envelope claiming model v2
- the operator uses threshold 4 but seals an envelope claiming threshold 6
- the operator uses inputs Y but seals an envelope claiming inputs X
- the operator suppresses an input that was actually used
- the operator seals a formally valid but substantively false decision envelope

Against this adversary, content-blind anchoring is not sufficient.

The false envelope is anchored at the correct time.

The hash matches.

The timestamp is valid.

The reconstruction succeeds.

But what is reconstructed is the operator’s original false claim.

Result:

NDC remains limited for this attack path unless additional source-attestation mechanisms exist.

## Design Boundary

Disjoint anchoring should be described as disjoint temporal anchoring.

It should not be described as full disjoint custody of decision truth.

Correct claim:

A-DAP makes retrospective rewriting detectable.

Incorrect claim:

A-DAP proves the operator told the truth at envelope creation.

Correct claim:

A-DAP provides a pre-committed evidentiary object for later contestation.

Incorrect claim:

A-DAP eliminates the need to trust the operator at the moment of generation.

Correct claim:

Content-blind anchoring protects the integrity of the commitment over time.

Incorrect claim:

Content-blind anchoring verifies the factual truth of the committed content.

## Relation to NDC

NDC should not be inflated by treating the anchoring authority as an independent witness to content it never saw.

For retrospective rewriting, the anchoring authority adds a genuinely disjoint custody point.

The operator cannot later alter the envelope and still match the externally anchored hash.

For origin-time fabrication, the anchoring authority does not add an independent witness to truth.

It only confirms that the operator committed to that envelope at that time.

Therefore:

- for retrospective rewriting, NDC can improve
- for origin-time fabrication, NDC remains limited under content-blind anchoring
- any claim of stronger NDC requires additional attestation layers

This distinction must remain explicit.

## Credit as a Contestability Domain

Credit is a strong domain for A-DAP because contestability already exists legally and institutionally, but often without a reconstructible evidentiary substrate.

The problem is not that no explanation exists.

The problem is that the explanation may not be independently reconstructible.

A credit applicant may receive a reason such as:

- insufficient credit history
- high debt-to-income ratio
- recent delinquency
- low score
- income not verified
- policy criteria not met

But this does not necessarily reveal:

- which model version was active
- which threshold was used
- which exact input values were considered
- which data source supplied each input
- which policy layer overrode the score
- whether the stated reason matches the committed decision state
- whether the decision record was later reconstructed for convenience

A-DAP does not replace the notice.

It gives the notice something to be tested against.

## Legal Review Rights and the Missing Substrate

Legal systems may require that people be informed of adverse automated decisions or allowed to request review.

But the right to review and the ability to reconstruct are not the same thing.

A review can remain dependent on the operator’s own narrative.

A review can be automated.

A review can rely on internal logs.

A review can confirm the output without reconstructing the decision path.

A-DAP’s contribution is narrower:

It creates a pre-committed decision object that can later be checked against an external temporal anchor.

This does not guarantee that the original object was truthful.

It does prevent the operator from inventing a different object later.

## Minimal Architecture

A minimal disjoint anchoring flow contains four elements:

1. Decision envelope generation

The operator generates a decision envelope at or before the moment of action.

The envelope contains the minimum necessary decision state required for later reconstruction.

2. Canonicalization

The envelope is canonicalized using a deterministic serialization method.

The goal is to ensure that the same envelope always produces the same hash.

3. Hash commitment

A cryptographic hash of the canonical envelope is produced.

The hash commits to the envelope content without exposing the content itself.

4. Independent anchoring

The hash is sent to an anchoring authority outside the operator’s exclusive custody.

The authority returns a timestamped receipt.

The operator stores the envelope.

The anchor stores or returns proof of the hash commitment.

The affected party, regulator, auditor, or court can later compare the presented envelope against the anchored hash.

## Privacy and Data Minimization

Content-blind anchoring is intentionally limited.

The anchoring authority should not need to receive:

- personal data
- full credit files
- model internals
- proprietary scoring logic
- protected attributes
- sensitive business rules
- raw applicant records

The authority receives only the canonical hash or commitment.

This reduces privacy and trade-secret exposure.

However, this privacy-preserving design is also why the anchor cannot validate the truth of the envelope content.

This is not a bug.

It is a boundary.

## Origin Attestation as Future Layer

Addressing origin-time fabrication requires stronger mechanisms.

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

These mechanisms can increase assurance.

But they also introduce additional costs:

- privacy exposure
- regulatory complexity
- trade-secret risk
- integration burden
- institutional dependency
- higher operational cost
- harder deployment in real credit systems

Therefore, they should not be silently implied by the basic anchoring claim.

They belong to a separate layer.

## Correct Use in A-DAP

When describing A-DAP with disjoint anchoring, use language like:

A-DAP creates a pre-committed record that makes later alteration detectable.

A-DAP enables contestation against a decision state committed at the time of action.

A-DAP reduces dependence on retrospective operator narratives.

A-DAP supplies an evidentiary substrate beneath legal review rights.

A-DAP strengthens temporal integrity of decision records.

Avoid language like:

A-DAP proves the decision was true.

A-DAP eliminates trust in the operator.

A-DAP fully solves custody.

A-DAP guarantees detection.

A-DAP prevents all falsification.

A-DAP verifies the real model execution without additional attestation.

## Practical Test

A practical test for this architecture in credit would compare two artifacts:

1. The existing legal or institutional explanation

For example:

- adverse action notice
- review response
- reason code disclosure
- generic explanation
- credit denial letter

2. The A-DAP anchored envelope

For example:

- canonical decision envelope
- envelope hash
- independent anchoring receipt
- model or policy version reference
- threshold state reference
- relevant input commitments

The test question is not:

Did A-DAP prove the bank told the truth at origin?

The test question is:

Could the affected party or authorized reviewer test whether the later explanation matches the decision state committed at the time of action?

If yes, A-DAP adds contestability.

If no, the system remains dependent on operator narrative.

## Failure Modes

## Failure Mode 1: False Envelope at Origin

The operator creates a false envelope and anchors it.

Outcome:

Anchoring preserves the false envelope.

Mitigation:

Requires origin-attestation layer.

## Failure Mode 2: Missing Envelope

The operator fails to generate or preserve the envelope.

Outcome:

Contestability fails.

Mitigation:

Make envelope generation a precondition for decision execution.

## Failure Mode 3: Non-Canonical Serialization

Different systems compute different hashes for the same logical envelope.

Outcome:

Verification becomes ambiguous.

Mitigation:

Use deterministic canonicalization and strict schema validation.

## Failure Mode 4: Captured Anchor

The anchoring authority colludes with the operator or allows retroactive manipulation.

Outcome:

Disjoint anchoring is weakened or destroyed.

Mitigation:

Use independent timestamping, public audit trails, append-only receipts, multiple anchors, or regulator-supervised anchoring.

## Failure Mode 5: Excessive Content Exposure

The system sends sensitive decision content to the anchor.

Outcome:

Privacy and trade-secret risks increase.

Mitigation:

Use content-blind hashing unless origin attestation is explicitly required and legally supported.

## Failure Mode 6: Overclaiming NDC

The architecture is described as if content-blind anchoring proves origin truth.

Outcome:

The claim becomes false and vulnerable to adversarial review.

Mitigation:

Explicitly distinguish temporal integrity from origin truth.

## Summary Table

| Attack Path | Content-Blind Anchoring Helps? | What It Proves | What It Does Not Prove |
|---|---:|---|---|
| Retrospective rewriting | Yes | The later envelope matches or does not match the anchored commitment | That the original envelope was truthful |
| Log alteration | Yes | The presented record differs from the committed record if hashes diverge | That the committed record reflected actual execution |
| Post-hoc narrative shift | Yes | The narrative can be tested against the committed envelope | That the envelope itself was not false |
| Origin-time fabrication | No | The false envelope existed at the committed time | That the envelope described the real decision |
| Operator collusion with anchor | Limited | Only as strong as the anchor’s independence | That custody was truly disjoint |
| Data-source manipulation before decision | No | The envelope committed to those inputs | That the upstream inputs were accurate |

## Final Position

Disjoint anchoring is valuable because it prevents the operator from rewriting the evidentiary record after the fact.

It should not be overclaimed as proof that the operator generated a truthful envelope.

For contestability, this distinction is decisive:

A-DAP does not make every decision true.

A-DAP does not guarantee that every false decision is detected.

A-DAP does not remove all trust from the operator at origin.

A-DAP makes later alteration of the committed decision record detectable.

That is the correct claim.

That is the defensible claim.

And that is the architectural boundary this document preserves.
