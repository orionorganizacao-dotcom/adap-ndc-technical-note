# Cryptographic Habeas Data

Cryptographic Habeas Data is a conceptual extension of habeas data for high-impact automated decisions.

It should not be understood as a replacement for classical habeas data, nor as a claim that cryptography can prove fairness, truth, legality, or justice.

Its function is narrower:

to give the affected person access to a stable, verifiable, and non-rewritable decision object against which an automated decision can later be challenged.

In short:

Cryptographic Habeas Data fixes the object of contestation.

It does not decide the merits.

---

## 1. Core Claim

A person cannot meaningfully contest an automated decision if the decision record can later be reconstructed, rewritten, omitted, or explained unilaterally by the same system or institution that made the decision.

Cryptographic Habeas Data proposes that a person affected by a high-impact automated decision should be able to access a committed decision object.

That object should allow later review of:

- what decision was made;
- when it was made;
- which declared rule, policy, model, or criterion was referenced;
- which sealed input or input reference was used;
- which output was produced;
- which explanation or justification was linked;
- which custody and verification assumptions apply.

The purpose is not to prove that the person is right.

The purpose is to prevent the dispute from starting from a mutable or one-sided record.

---

## 2. What It Provides

Cryptographic Habeas Data provides a technical basis for affected-party contestability.

It can support:

- decision receipt;
- decision envelope;
- committed record;
- reconstruction path;
- verification path;
- custody declaration;
- challenge against later explanations or institutional claims.

Its value is evidentiary.

It gives the affected person a fixed object to contest.

Without such an object, the person may be forced to challenge only a narrative produced after the fact.

---

## 3. What It Does Not Provide

Cryptographic Habeas Data does not prove that a decision was fair.

It does not prove that a decision was lawful.

It does not prove that the input was true.

It does not prove that the criterion was legitimate.

It does not prove that the model was unbiased.

It does not prove that the affected person should win the dispute.

It does not replace administrative review, judicial review, expert analysis, legal argument, or institutional accountability.

A cryptographically valid record can still preserve a bad decision.

It can also preserve a false input, a discriminatory criterion, or an unlawful policy if those elements existed before the point of commitment.

This is why Cryptographic Habeas Data should be understood as fixation of the contestable object, not proof of justice.

---

## 4. Three Independent Layers

Cryptographic Habeas Data can be described through three independent layers.

They are not a single ladder of increasing guarantees.

Layer 1 is the foundation.

Layers 2 and 3 may strengthen the architecture, but the concept does not depend on them being fully mature.

---

### 4.1 Layer 1 — Fixation of the Contestable Object

This is the core layer.

The affected person receives or can access a stable decision object.

This object fixes:

- the existence of the decision;
- the time of the decision;
- the declared decision criterion;
- the output applied;
- the minimum reconstruction reference;
- the custody assumptions.

This layer does not prove injustice.

It prevents retroactive rewriting of the object being contested.

It creates minimal parity of record between the institution that decided and the person affected by the decision.

---

### 4.2 Layer 2 — Internal Coherence Reconstruction

This layer allows review of whether the preserved decision object is internally coherent.

It may compare:

- decision;
- declared criterion;
- sealed input or input reference;
- output;
- explanation;
- custody metadata.

This can show whether the recorded decision is consistent with its declared elements.

It does not prove external validity.

It does not prove that the input was true.

It does not prove that the criterion was legal.

It does not prove that the decision was fair.

A decision can be internally coherent and externally invalid.

Layer 2 reconstructs the internal relationship between committed elements.

It does not settle the legal or factual merits.

---

### 4.3 Layer 3 — NDC Capture Diagnostic

NDC, or Number of Distinct Compromises, is a research diagnostic.

It asks how many structurally distinct compromises would be required for a false, incomplete, or selectively omitted decision record to survive challenge without detection.

NDC may help identify:

- self-attestation;
- signer-custody collapse;
- verifier capture;
- weak custody separation;
- omission before commitment;
- dependence on the same system that produced the decision.

NDC should not be presented at this stage as a forensic, judicial, or regulatory metric.

It is not the legal foundation of Cryptographic Habeas Data.

It is a diagnostic complement.

The core concept survives even if NDC remains experimental.

---

## 5. Relationship to A-DAP

Cryptographic Habeas Data is the legal-conceptual expression of A-DAP’s affected-party contestability layer.

A-DAP should not be framed here as a competing cryptographic audit-trail standard.

Its relevant contribution is narrower:

- automated decisions should be born with a contestable object;
- decision, record, explanation, and verification should not collapse into the same system;
- the affected person should not depend only on the decision-maker’s later narrative;
- verification strength depends on custody separation and independent reconstruction.

Cryptographic Habeas Data translates these ideas into a rights-oriented frame.

The protected subject is not only the auditor, regulator, operator, or professional reviewer.

The protected subject is the person affected by the decision.

---

## 6. Relationship to Habeas Data

Classical habeas data concerns access to and correction of personal data.

Cryptographic Habeas Data is an analogical extension of that tradition.

It concerns access to the decision object created from or about personal data.

The question is no longer only:

What data do you hold about me?

The additional question is:

What automated decision did you apply to me, and what stable evidence fixes that decision?

This is not a claim that current habeas data doctrine already contains the full architecture.

It is a proposed technical-juridical category for automated decision systems.

---

## 7. Relationship to Review Rights

Cryptographic Habeas Data does not replace review rights.

It supports them.

A review right is weak if the reviewing authority depends only on a post-hoc explanation from the system that made the decision.

Cryptographic Habeas Data provides the fixed object that review can examine.

It does not decide whether the review should be human, administrative, judicial, regulatory, or technical.

It only insists that review should not occur over a moving record.

---

## 8. Design Requirements

A Cryptographic Habeas Data implementation should define:

- when the decision object is created;
- what is included in the decision envelope;
- what is disclosed to the affected person;
- what remains protected for privacy, security, or privilege reasons;
- how the affected person can verify the record;
- how third parties can reconstruct the record;
- who controls signing keys;
- who controls custody;
- who verifies;
- what happens if the signer, custodian, or verifier is compromised;
- what assumptions are required.

Without these declarations, a cryptographic record may become another form of self-attestation.

---

## 9. Limits

Cryptographic Habeas Data has strict limits.

It operates after the point of commitment.

It does not solve input provenance.

It does not make false inputs true.

It does not make illegal criteria legal.

It does not make unfair decisions fair.

It does not solve total collusion.

It does not guarantee detection of all manipulation.

It does not replace courts, regulators, auditors, lawyers, or experts.

Its value is more precise:

it prevents the object of contestation from being silently changed after the fact.

---

## 10. Short Definition

Cryptographic Habeas Data is the right of a person affected by a high-impact automated decision to access a stable, verifiable, and non-rewritable decision object that fixes what decision was applied and allows that decision to be contested later.

It fixes the object.

It does not decide the merits.
