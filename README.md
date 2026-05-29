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

## Executive Summary

A-DAP proposes that high-impact automated decisions be committed before or at the moment of action through reconstructible decision envelopes.

A decision envelope is a pre-committed evidentiary object that can later be reconstructed, examined, and compared against explanations, notices, logs, or operator claims.

A-DAP uses canonicalization, cryptographic commitments, timestamps, signatures, and optional independent anchoring to strengthen temporal integrity.

Its defensible claim is narrow:

the system preserves a contestable record of what was committed at decision time.

This project favors claims that survive adversarial review over claims that sound stronger but collapse under scrutiny.

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

They may describe, summarize, or justify the decision.

But they do not necessarily make the decision reconstructible.

A-DAP is designed to address this gap.

## Explanation Is Not Verification

A-DAP distinguishes between explanation and verification.

Explanation asks:

```text
Why does the operator say this decision happened?
```

Verification asks:

```text
Can an authorized reviewer reconstruct the committed decision state and test whether the later account matches it?
```

This distinction matters because a post-hoc explanation can be plausible without being independently testable.

A-DAP is designed to make the decision itself an object of verification, not merely an object of explanation.

## Core Architecture

A-DAP separates the decision process into distinct evidentiary layers.

At minimum, an A-DAP decision flow should include:

- a decision envelope
- deterministic canonicalization
- cryptographic commitment
- pre-action or at-action timestamping
- verification procedure
- contestability path

The architecture is not based on trusting the system’s later narrative.

It is based on preserving the state required to reconstruct the decision.

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

## Commit Before Act

A-DAP follows a commit-before-act principle.

For high-impact decisions, the target architecture is commit-before-act: the relevant decision state should be committed before the decision becomes operationally effective, unless a documented emergency or latency exception applies.

This does not mean that every internal detail must be publicly disclosed.

It means the relevant decision state must be preserved in a form that can later be reconstructed by an authorized reviewer.

Without commit-before-act, the record can become a post-hoc artifact.

With commit-before-act, the decision leaves a pre-action evidentiary trace.

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

## Disjoint Anchoring for Contestability

The repository includes an architectural note on disjoint anchoring for contestability:

```text
architecture/disjoint-anchoring-for-contestability.md
```

The note clarifies a critical boundary:

content-blind independent anchoring can make retrospective rewriting detectable, but it does not prove that the operator truthfully described the decision at the moment the envelope was created.

For retrospective rewriting, an independent anchor adds a genuinely disjoint custody point only for that attack path.

For origin-time fabrication, content-blind anchoring remains limited unless additional mechanisms exist, such as independent input-source attestation, model-version registries, threshold registries, witnessed execution, or trusted execution evidence.

## Contestability, Not Detection

A-DAP does not guarantee that someone will inspect a decision immediately.

It does not guarantee that an auditor, court, regulator, or affected party will act at the right time.

Its claim is narrower:

the evidentiary object needed to contest the decision should exist when the decision is challenged.

A-DAP does not guarantee contemporaneous detection.

It enables contemporaneous contestability.

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

This section is not a legal claim that A-DAP satisfies any specific credit regulation.

It identifies a technical evidentiary gap beneath existing review and notice mechanisms.

A-DAP does not replace a denial notice.

It addresses the evidentiary gap that remains when legal review rights exist but the review process still depends on operator-controlled explanations, logs, or automated re-evaluation.

It allows the notice to be tested against a committed decision envelope.

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

## Governance of Indistinction

A-DAP also helps analyze hybrid human-machine systems where decision formation, justification, and record custody may become structurally indistinguishable.

This is the Governance of Indistinction problem.

The risk is not hybrid intelligence itself.

The risk appears when cognition, justification, and audit records depend on the same material control vector.

In that case, the system may not merely become hard to explain.

It may become hard to separate into independently verifiable custody domains.

The relevant architectural question is:

```text
Does an external auditor have a materially disjoint record path, or only the system’s own narrative about itself?
```

This distinction matters because a hybrid decision can remain contestable if the record custody layer is genuinely independent.

But if the same fused process decides, justifies, and records the decision, later audit may collapse into self-attestation.

## Second-Order Entity NDC Experiment

The repository includes an executable experiment testing this narrower claim:

```text
experiments/second-order-entity-ndc/second-order-entity-ndc.py
```

The experiment models three custody graphs for a hypothetical hybrid human-machine decision system.

It tests whether hybrid intelligence collapses to NDC=1 merely because human and machine participate in the same decision.

The more precise tested claim is:

```text
human-machine fusion without independent record custody can collapse to NDC = 1
```

The experiment includes three scenarios:

```text
A. No independent record custody
   Expected result: NDC = 1

B. Genuine disjoint A-DAP custody envelope
   Expected result: NDC = 2

C. Pseudo-independent custody envelope contaminated by shared vector
   Expected result: NDC = 1
```

This is important because it avoids the overclaim that hybrid intelligence is automatically ungovernable.

The experiment instead tests a narrower architectural point:

external verifiability in hybrid intelligence depends on materially disjoint record custody.

A merely separate-looking record path is not enough.

If that path is still mediated by the same shared control vector, the custody structure may collapse back to NDC=1.

## What A-DAP Proves

A-DAP can prove that:

- a decision envelope existed at or before a given time
- the presented envelope matches or does not match its prior commitment
- a presented record differs or does not differ from its prior commitment
- a presented decision envelope matches a specific recorded state committed earlier
- a verification procedure can reconstruct the committed envelope, if the required envelope data is available

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
├── experiments/
│   └── second-order-entity-ndc/
│       ├── README.md
│       ├── second-order-entity-ndc.py
│       └── results/
│           └── output.txt
├── proofs/
│   └── README.md
├── solver/
│   └── README.md
├── THREAT_MODEL.md
├── CONTRIBUTING.md
├── QUICKSTART.md
├── NOTICE.md
└── RELEASE_NOTES.md
```

## Running the Second-Order Entity Experiment

To run the experiment:

```bash
python experiments/second-order-entity-ndc/second-order-entity-ndc.py
```

To save the real output:

```bash
mkdir -p experiments/second-order-entity-ndc/results
python experiments/second-order-entity-ndc/second-order-entity-ndc.py > experiments/second-order-entity-ndc/results/output.txt
```

The output should be committed to the repository only after the script has actually been executed.

This matters because A-DAP should not merely claim that a construction exists.

It should preserve the executable construction and the executed result.

## Integrity Rule

Until the graph, script, and real solver output are present in the repository, strong language such as:

```text
Hybrid intelligence without independent record custody is the final black box by construction.
```

should not be used as a formal claim.

Before the executable experiment and output are committed, use the weaker formulation:

```text
Hybrid intelligence without independent record custody risks becoming the final black box.
```

After the experiment is committed and reproducible, the stronger formulation may be used with a reference to the experiment.

## Project Status

This repository is experimental.

It is intended to support adversarial review, technical critique, and falsifiable refinement of A-DAP’s claims.

The project does not claim to solve accountability.

It claims to provide a reconstructible evidentiary substrate for contestability.

Accountability still requires institutions, authority, procedure, law, enforcement, and judgment.

A-DAP does not replace those mechanisms.

It gives them a more testable record to work with.

## Minimal Conclusion

A-DAP is not a truth oracle.

A-DAP is not a fairness guarantee.

A-DAP is not a complete accountability system.

A-DAP is a contestability architecture.

Its core contribution is narrow:

high-impact automated decisions should be committed as reconstructible evidentiary objects before they become post-hoc narratives.
