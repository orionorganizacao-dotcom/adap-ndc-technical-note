# Decision Receipt PoC

This proof of concept demonstrates a minimal affected-party decision receipt.

It is part of the A-DAP research track and the Cryptographic Habeas Data concept.

The goal is narrow:

to show how a person affected by an automated decision can receive a stable, verifiable decision object at the moment of the decision.

This PoC does not prove fairness.

It does not prove legality.

It does not prove truth.

It does not prove that the input was correct.

It does not prove that the decision was justified.

It only demonstrates how a decision receipt can fix the object of contestation.

---

## 1. Core Idea

The difference between this PoC and a screenshot, email, timestamped PDF, or notarial record is not merely cryptography.

The key difference is timing and source.

A normal evidentiary artifact may be created after the dispute begins.

A decision receipt should be emitted automatically by the decision system at the moment of the decision.

The receipt crosses the boundary from the operator to the affected person.

Once that happens, the operator no longer controls the only version of the record.

This is the first independence boundary in this PoC:

```text
citizen-held receipt
```

This PoC does not yet implement RFC 3161 timestamping, public anchoring, transparency logs, or third-party custody.

Those may be future extensions.

The first question is simpler:

can the affected person hold a verifiable decision object that later exposes inconsistency, non-issuance, or split-view reconstruction?

---

## 2. What This PoC Demonstrates

This PoC demonstrates three adversarial scenarios.

It is not a happy-path demo only.

The goal is to test what happens when the operator does not behave honestly.

The scenarios are:

1. Non-issuance
2. Split-view receipt
3. Perfect bad decision

Each scenario tests a different limit of affected-party contestability.

---

## 3. Scenario 1 — Non-Issuance

### Problem

The operator makes an automated decision but does not issue a receipt to the affected person.

If non-issuance is invisible, the operator can avoid contestability entirely.

A right to a decision receipt is meaningless if the absence of the receipt has no consequence.

### What the PoC shows

The PoC treats missing receipt issuance as a detectable process failure.

The absence of a receipt does not prove that the decision was unfair.

But it proves that the decision was not accompanied by the required contestability object.

### Why it matters

This is the first test of Cryptographic Habeas Data.

The affected person should not need to prove the hidden contents of a record that was never issued.

If a system is required to emit a decision receipt and fails to do so, that absence is itself evidence of procedural failure.

### Limit

This PoC can show how non-issuance is represented.

It cannot force a real institution to issue receipts.

That requires law, regulation, procurement rules, judicial order, administrative policy, or institutional adoption.

---

## 4. Scenario 2 — Split-View Receipt

### Problem

The operator issues one receipt to the affected person and later presents a different record to an auditor, regulator, court, or review authority.

This is the core retroactive rewriting attack.

Example:

```text
Citizen-held receipt A:
decision_id = D-001
output = denied
policy_ref = policy-v1

Operator later presents receipt B:
decision_id = D-001
output = approved-for-review
policy_ref = policy-v2
```

If the affected person has no receipt, the operator controls the narrative.

If the affected person has receipt A, the conflict becomes visible.

### What the PoC shows

The PoC creates two receipts with the same decision identifier but divergent committed contents.

The verifier detects that the records cannot both be the same decision object.

The citizen-held receipt becomes evidence that the operator’s later version is inconsistent.

### Why it matters

This demonstrates the minimal value of affected-party possession.

The receipt does not need to prove that the decision was unfair.

It only needs to prove that the operator cannot silently replace the object of contestation.

### First independence boundary

This PoC uses citizen possession as the first independence boundary.

Once the receipt is given to the affected person, the operator can no longer rewrite every copy of the record unless it can also suppress or replace the citizen-held copy.

### Limit

Citizen possession is weaker than public anchoring or trusted third-party timestamping.

A future version may add:

- RFC 3161 timestamping;
- public transparency log;
- third-party witness;
- Merkle batch anchoring;
- independent custody store.

This first PoC intentionally avoids that complexity.

The purpose is to test the minimal boundary:

```text
the decision object leaves the operator’s exclusive control.
```

---

## 5. Scenario 3 — Perfect Bad Decision

### Problem

A system may issue a perfect receipt for a bad decision.

The input may be false.

The criterion may be discriminatory.

The policy may be unlawful.

The model may be biased.

The decision may be internally coherent and still externally wrong.

This is the GIGO boundary:

```text
garbage in, garbage out
```

### What the PoC shows

The PoC generates a receipt that verifies successfully even though the decision scenario is intentionally flawed.

This demonstrates an important limit:

a valid receipt proves fixation of the decision object.

It does not prove justice.

### Why it matters

This scenario prevents overclaim.

Cryptographic Habeas Data is not a fairness engine.

A-DAP is not a truth machine.

A decision receipt can preserve a bad decision faithfully.

That is still useful because it fixes the object that must be challenged.

But the legal, factual, ethical, or technical merits must be argued separately.

### Limit

The receipt does not prove:

- the input was true;
- the criterion was legal;
- the policy was fair;
- the decision was correct;
- the affected person should win the dispute.

It only proves that this was the recorded decision object.

---

## 6. Explanation Hash Semantics

The receipt may include an `explanation_hash`.

This field must be interpreted carefully.

The `explanation_hash` does not prove that the explanation is true.

It does not prove that the explanation is complete.

It does not prove that the explanation justifies the decision.

It only fixes which explanation or narrative the operator gave at the time of the decision.

This matters because an operator should not be able to change the explanation later without detection.

Correct interpretation:

```text
explanation_hash fixes the operator’s explanation.
```

Incorrect interpretation:

```text
explanation_hash validates the operator’s explanation.
```

This distinction is central to A-DAP.

Explanation is not verification.

A sealed explanation is still only a sealed explanation.

---

## 7. Minimal Receipt Fields

A minimal decision receipt may include:

```json
{
  "receipt_type": "adap_decision_receipt",
  "receipt_version": "0.1",
  "decision_id": "D-001",
  "issued_at": "2026-05-29T12:00:00Z",
  "affected_party_ref": "subject-hash-or-reference",
  "policy_ref": "eligibility-policy-v1",
  "model_ref": "demo-model-v1",
  "input_hash": "sha256:...",
  "output_hash": "sha256:...",
  "explanation_hash": "sha256:...",
  "decision_hash": "sha256:...",
  "signature": "demo-signature-or-placeholder",
  "verification_method": "local-demo-verifier"
}
```

This is only illustrative.

A real implementation must define:

- canonicalization;
- key management;
- signature algorithm;
- disclosure rules;
- privacy constraints;
- custody model;
- external anchoring;
- affected-party access;
- verification procedure.

---

## 8. What the Verifier Should Check

The verifier should be able to check:

- the receipt has required fields;
- the decision hash matches the committed receipt contents;
- the same `decision_id` is not associated with conflicting contents;
- the citizen-held receipt differs from any later operator-submitted version;
- the explanation hash was fixed, not validated;
- the receipt verifies structurally even in the perfect-bad-decision scenario;
- non-issuance is represented as a process failure.

The verifier should not claim:

- the decision was fair;
- the decision was lawful;
- the input was true;
- the model was unbiased;
- the explanation was adequate;
- the institution acted legitimately.

---

## 9. Expected Test Outputs

The PoC should produce clear outputs for each scenario.

### Scenario 1 — Non-Issuance

Expected result:

```text
FAIL: no decision receipt was issued.
Meaning: contestability object missing.
This does not prove unfairness.
```

### Scenario 2 — Split-View Receipt

Expected result:

```text
FAIL: conflicting receipts detected for the same decision_id.
Meaning: operator version and citizen-held version cannot both be the same committed decision object.
This exposes retroactive inconsistency.
```

### Scenario 3 — Perfect Bad Decision

Expected result:

```text
PASS: receipt verifies structurally.
WARNING: structural verification does not prove fairness, legality, truth, or correctness.
Meaning: the object is fixed, but the merits remain contestable.
```

---

## 10. Why Citizen-Held Receipt First

This PoC uses citizen-held receipt as the first independence boundary.

That choice is intentional.

The purpose is to demonstrate the minimum condition for affected-party contestability:

```text
the affected person holds a stable object that the operator cannot silently rewrite later.
```

This is weaker than external public anchoring.

But it is stronger than ordinary internal logging.

Internal logging keeps the record inside the operator’s domain.

Citizen-held receipt moves at least one copy outside that domain.

That is the minimal conceptual difference.

---

## 11. Future Extensions

Future versions may add:

- Ed25519 signatures;
- RFC 3161 timestamping;
- Merkle batching;
- external transparency log;
- third-party witness;
- independent custody service;
- verifier CLI;
- JSON canonicalization;
- tamper tests;
- receipt revocation rules;
- disclosure and redaction rules;
- privacy-preserving verification;
- affected-party access workflow;
- NDC analysis for the receipt architecture.

These extensions should not change the core limit:

even a perfect receipt does not prove justice.

It fixes the contestable object.

---

## 12. Relationship to Cryptographic Habeas Data

This PoC operationalizes the smallest testable part of Cryptographic Habeas Data.

Cryptographic Habeas Data proposes that a person affected by a high-impact automated decision should be able to access a stable, verifiable, and non-rewritable decision object.

This PoC demonstrates that idea in minimal form.

It does not implement a legal right.

It does not enforce institutional adoption.

It does not compel the state or an operator to issue receipts.

It only shows what the technical object could look like and how adversarial cases can be tested.

---

## 13. Relationship to A-DAP

This PoC is aligned with A-DAP’s narrowed role:

- affected-party contestability;
- decision object fixation;
- separation between record and later explanation;
- detection of split-view reconstruction;
- explicit limits around truth, fairness, and legality.

It should not be read as a complete A-DAP implementation.

It is a minimal falsifiable demonstration.

If the PoC only proves that a receipt can be created, it fails.

It must also show:

- what happens when no receipt is issued;
- what happens when the operator presents a conflicting receipt;
- what happens when a bad decision verifies successfully.

Those failures and limits are part of the demonstration.

---

## 14. Non-Goals

This PoC does not attempt to:

- prove fairness;
- prove legality;
- prove correctness;
- verify input truth;
- audit model bias;
- solve collusion;
- replace courts;
- replace regulators;
- implement a full provenance standard;
- compete with VCP, VAP, LAP, or other provenance frameworks;
- provide production security.

It is a research artifact.

Its only goal is to test the minimum affected-party receipt concept.

---

## 15. Success Criteria

This PoC succeeds if it can demonstrate all of the following:

1. A decision receipt can be generated at the moment of a simulated decision.
2. The affected person can hold a copy of that receipt.
3. A missing receipt is detectable as a process failure.
4. A later conflicting operator record is detectable against the citizen-held receipt.
5. A structurally valid receipt can still represent a bad decision.
6. The verifier does not overclaim fairness, legality, truth, or correctness.
7. The README and outputs make the limits explicit.

This PoC fails if it only demonstrates a happy path.

---

## 16. Minimal Command Design

A future implementation may expose commands such as:

```text
python generate_receipt.py
python verify_receipt.py receipts/citizen_receipt.json
python scenarios/non_issuance.py
python scenarios/split_view.py
python scenarios/perfect_bad_decision.py
```

The exact file structure may evolve.

The important requirement is that the adversarial scenarios are executable.

---

## 17. Final Claim

The Decision Receipt PoC does not prove that automated decisions are fair.

It does not prove that institutions are honest.

It does not prove that inputs are true.

It demonstrates a narrower claim:

an affected person should not have to contest an automated decision without a stable decision object.

The first technical step is a citizen-held receipt emitted at the moment of the decision.

That receipt fixes the object.

It does not decide the merits.
