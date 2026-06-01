# Citizen-Facing Evidence Language

Status: UI / communication architecture note  
Repository context: A-DAP / NDC technical note  
Document type: Architecture note  
Version: 0.1.0

---

## 1. Purpose

This document defines citizen-facing evidence language for A-DAP verification interfaces.

A-DAP creates reconstructible decision evidence.

But reconstructible evidence is only useful if affected people, advocates, lawyers, auditors, regulators, journalists, and courts can understand what the evidence proves and what it does not prove.

A citizen-facing verifier must not merely translate cryptographic success into vague reassurance.

It must explain:

- what was verified;
- what was not verified;
- what remains disputed;
- what evidence can be exported;
- what next procedural step may be available.

The purpose of this document is to prevent technical verification from becoming misleading public-facing language.

---

## 2. Core Principle

Citizen-facing verification must explain what the evidence proves, what it does not prove, and what remains contestable.

A weak interface says:

```text
Hash verified.
```

That may be technically correct.

But it is socially incomplete.

A stronger interface says:

```text
The decision record matches the committed record.

This confirms what the system processed at the time of decision.

It does not prove that the decision was correct, fair, lawful, or based on true input.

You may still challenge the input, the policy, the explanation, or the outcome.
```

The goal is not to make the interface sound certain.

The goal is to make the evidentiary status clear.

---

## 3. Why This Matters

A-DAP separates several questions that are often collapsed:

1. What did the system commit to using?
2. How did the input enter the system?
3. Did the later explanation match the committed record?
4. Was the input true?
5. Was the decision correct?
6. Was the decision lawful?
7. Was the decision fair?
8. Was verification actually exercised?
9. Who still controls the verification path?

A citizen-facing interface must not collapse these questions into a single green checkmark.

A green checkmark can easily become a false symbol of trust.

The interface should communicate evidence, limits, and next steps.

---

## 4. Relationship to Existing Architecture Notes

This document builds on:

- `architecture/citizen-verifier-ui-spec.md`
- `architecture/exercisable-citizen-verification.md`
- `architecture/input-truth-boundary.md`
- `architecture/input-provenance-envelope.md`
- `architecture/random-audit-sampling.md`
- `architecture/verifier-funding-capture.md`

The key distinction is:

> A cryptographic result is not the same as a citizen-facing explanation.

The verifier should not become a new authority.

It should help people understand the evidence without overstating it.

---

## 5. Language Rules

Citizen-facing evidence language should follow these rules.

### Rule 1 — Say What Was Verified

The interface must identify the specific object verified.

Examples:

- decision envelope;
- input provenance envelope;
- output notice;
- explanation;
- timestamp evidence;
- custody path;
- reconstruction package.

Do not say only:

```text
Verified.
```

Say:

```text
The decision envelope was verified.
```

or:

```text
The explanation was compared against the committed decision record.
```

---

### Rule 2 — Say What Was Not Verified

Every positive result should include a limitation.

Example:

```text
This confirms that the record matches the committed decision envelope.

It does not prove that the decision was correct or fair.
```

A verification result without a limitation can mislead the user.

---

### Rule 3 — Separate Input Commitment from Input Truth

A verified input commitment does not prove the input was true.

Correct language:

```text
The system used this committed input during the decision.

This does not prove that the input was originally submitted correctly or that the source data was true.
```

Incorrect language:

```text
Your input was verified as correct.
```

---

### Rule 4 — Separate Input Provenance from Input Truth

A verified input provenance envelope records how the input entered the system.

It does not prove the external-world fact.

Correct language:

```text
The input provenance record shows how this input entered the decision process.

This does not prove that the underlying fact was true.
```

Incorrect language:

```text
The source data is proven true.
```

---

### Rule 5 — Separate Reconstruction from Accountability

A reconstructed record does not create a remedy by itself.

Correct language:

```text
This evidence may support a review, appeal, complaint, audit, or legal challenge.

It does not automatically reverse the decision.
```

Incorrect language:

```text
The decision is invalid.
```

unless an authorized institution has made that determination.

---

### Rule 6 — Avoid False Finality

Avoid language such as:

```text
Case closed.
```

```text
Decision confirmed.
```

```text
Decision proven correct.
```

```text
No issue found.
```

Prefer:

```text
No mismatch was detected in the evidence checked.

Other issues may still exist outside the scope of this verification.
```

---

### Rule 7 — Name the Remaining Contestable Issues

The interface should tell the user what can still be challenged.

Examples:

- captured input;
- missing input provenance;
- model or policy logic;
- explanation quality;
- legal basis;
- fairness;
- human review process;
- missing envelope;
- operator-controlled verification path.

This prevents users from thinking that cryptographic verification ends the dispute.

---

### Rule 8 — Make Export Available

Citizen-facing verification should produce an exportable evidence package.

The interface should say:

```text
You can export this verification result for review by an advocate, lawyer, auditor, regulator, journalist, or court.
```

The export should include:

- verification result;
- timestamp of verification;
- envelope identifier;
- hashes checked;
- missing evidence;
- mismatch findings;
- limitations;
- recommended next review path.

---

## 6. Standard Result Types

A citizen verifier should support standard result categories.

At minimum:

1. Decision envelope verified
2. Decision envelope mismatch
3. Decision envelope missing
4. Input provenance available
5. Input provenance missing
6. Input truth disputed
7. Explanation matches committed record
8. Explanation mismatch
9. Operator-controlled verification path detected
10. Evidence package export available
11. Verification inconclusive
12. Unsupported or invalid receipt

---

## 7. Message: Decision Envelope Verified

### Technical Meaning

The committed decision envelope was reconstructed and matched the expected commitment.

### Citizen-Facing Message

```text
The decision record was verified.

The record matches the committed decision envelope.

This confirms what the system processed at the time of decision.

It does not prove that the decision was correct, fair, lawful, or based on true input.

You may still challenge the input, the policy, the explanation, or the outcome.
```

### Avoid

```text
The decision is correct.
```

```text
The system was fair.
```

```text
The case is verified.
```

---

## 8. Message: Decision Envelope Mismatch

### Technical Meaning

The reconstructed decision record does not match the committed envelope.

### Citizen-Facing Message

```text
A mismatch was detected.

The decision record provided now does not match the committed decision envelope.

This may indicate alteration, substitution, missing evidence, reconstruction error, or an inconsistent explanation.

You should export this result and request review.
```

### Optional Next Step

```text
Recommended next step: export the evidence package and submit it with a review, appeal, complaint, audit request, or legal inquiry.
```

---

## 9. Message: Decision Envelope Missing

### Technical Meaning

No decision envelope was provided or found.

### Citizen-Facing Message

```text
No decision envelope was found.

This means the system did not provide the evidence needed to reconstruct the decision record through A-DAP.

Without a decision envelope, this verifier cannot confirm whether the later explanation matches the original committed decision state.

You may request the decision envelope from the operator or reviewing institution.
```

### Avoid

```text
No problem found.
```

Missing evidence is not proof that the decision is valid.

---

## 10. Message: Input Provenance Available

### Technical Meaning

An input provenance envelope exists and can be inspected or reconstructed.

### Citizen-Facing Message

```text
Input provenance information is available.

This record may show how the input entered the decision process, including source, submission channel, capture time, transformation rules, or custody path.

This does not prove that the input was true.

It helps separate disputes about what the system used from disputes about whether the input was captured correctly.
```

---

## 11. Message: Input Provenance Missing

### Technical Meaning

No input provenance envelope is available.

### Citizen-Facing Message

```text
No input provenance record was found.

The decision record may show what the system used, but it does not show how that input entered the system.

This may make it harder to challenge whether the input was captured, transmitted, or transformed correctly.
```

### Optional Next Step

```text
Recommended next step: request the original submission record, intake receipt, source record, or data correction history.
```

---

## 12. Message: Input Truth Disputed

### Technical Meaning

The user or reviewer disputes whether the committed input reflects the true or submitted input.

### Citizen-Facing Message

```text
The input itself is disputed.

A-DAP can show what input the system committed to using.

It does not, by itself, prove that the input was true or correctly captured.

To challenge the input, review the input provenance record, submission receipt, source document, or correction history.
```

---

## 13. Message: Explanation Matches Committed Record

### Technical Meaning

The explanation is consistent with the committed decision record under the declared reconstruction rules.

### Citizen-Facing Message

```text
The explanation matches the committed decision record.

This means the explanation appears consistent with what the system committed to at the time of decision.

It does not prove that the decision was correct, fair, lawful, or based on true input.
```

---

## 14. Message: Explanation Mismatch

### Technical Meaning

The explanation is inconsistent with the committed decision record.

### Citizen-Facing Message

```text
The explanation does not match the committed decision record.

This may mean the explanation was generated after the fact, was incomplete, or does not correspond to what the system actually committed to using.

You should export this result and request review.
```

---

## 15. Message: Operator-Controlled Verification Path Detected

### Technical Meaning

The verification path appears to depend materially on the same operator or control domain being verified.

### Citizen-Facing Message

```text
The verification path may not be independent.

Some evidence, tools, records, or access paths appear to remain controlled by the same operator responsible for the decision.

This does not mean the record is false.

It means the verification may still depend on the party being verified.
```

### Optional Next Step

```text
Recommended next step: request independent reconstruction, external audit, or review by a qualified third party.
```

---

## 16. Message: Evidence Package Export Available

### Technical Meaning

The verifier can package the result and supporting metadata for external review.

### Citizen-Facing Message

```text
An evidence package is available.

You can export this package for review by an advocate, lawyer, auditor, regulator, journalist, or court.

The package may include the verification result, checked hashes, missing evidence, mismatch findings, limitations, and recommended next steps.
```

---

## 17. Message: Verification Inconclusive

### Technical Meaning

The verifier could not reach a reliable result.

Possible causes include missing files, incompatible schema, unsupported format, corrupted envelope, incomplete metadata, or inaccessible evidence.

### Citizen-Facing Message

```text
Verification was inconclusive.

The verifier could not determine whether the decision record matches the committed evidence.

This may be due to missing, incomplete, unsupported, or inaccessible information.

An inconclusive result is not proof that the decision was correct.
```

---

## 18. Message: Unsupported or Invalid Receipt

### Technical Meaning

The receipt or evidence object is not supported or fails basic format checks.

### Citizen-Facing Message

```text
This receipt could not be verified.

It may be missing required fields, use an unsupported format, or fail basic integrity checks.

You may request a valid decision envelope or verification receipt from the operator.
```

---

## 19. Severity Labels

Citizen-facing interfaces may use severity labels, but they must avoid false certainty.

Recommended labels:

```text
Verified within scope
Mismatch detected
Evidence missing
Verification inconclusive
Independence concern
Input disputed
Export recommended
```

Avoid labels such as:

```text
Safe
Fair
Valid
Invalid
Correct
Fraud
Illegal
Accountable
Compliant
```

Those labels may require institutional or legal judgment beyond the verifier.

---

## 20. Green Checkmark Warning

A green checkmark should never stand alone.

If used, it must be paired with scope language.

Example:

```text
Verified within scope.

The decision record matches the committed envelope.

This does not prove that the decision was correct or fair.
```

A green checkmark without limitation language risks becoming a misleading trust symbol.

---

## 21. Red Warning Warning

A red warning should also avoid overclaim.

A mismatch may indicate serious concern, but it does not automatically prove fraud or illegality.

Correct language:

```text
Mismatch detected.

This result should be reviewed.
```

Avoid:

```text
Fraud proven.
```

```text
Illegal decision.
```

unless an authorized institution has made that determination.

---

## 22. Export Package Language

Every export package should include a plain-language summary.

Example:

```text
Summary:

This package contains the result of an A-DAP verification attempt.

The verifier checked whether the provided decision record matches the committed decision envelope.

Result: mismatch detected.

This does not automatically prove fraud or illegality.

It provides evidence that may support review by an advocate, auditor, regulator, lawyer, journalist, or court.
```

The package should also include machine-readable metadata.

---

## 23. Next-Step Language

The interface should avoid giving legal advice unless authorized.

It may say:

```text
You may use this evidence to request review through the available appeal, complaint, audit, or legal process.
```

It should avoid:

```text
You should sue.
```

```text
This guarantees reversal.
```

```text
The operator broke the law.
```

The interface should support contestability without pretending to be a court.

---

## 24. Recommended UI Pattern

A citizen-facing result card should include:

```text
Status:
What was checked:
What was found:
What this proves:
What this does not prove:
What remains contestable:
Evidence available:
Recommended next step:
Export button:
```

Example:

```text
Status: Verified within scope

What was checked:
The decision envelope was reconstructed and compared with the provided decision record.

What was found:
The record matches the committed envelope.

What this proves:
The system processed the committed decision record.

What this does not prove:
It does not prove that the input was true, the decision was fair, or the decision was legally correct.

What remains contestable:
Input truth, policy validity, fairness, legal basis, and human review.

Evidence available:
Verification summary, envelope hash, timestamp evidence, reconstruction metadata.

Recommended next step:
Export the evidence package if you want to request review.
```

---

## 25. Correct Claims

Correct claims include:

> The decision record matches the committed envelope.

> The explanation matches the committed record under the declared reconstruction rules.

> The input provenance record is available for review.

> No input provenance record was provided.

> The verification path appears operator-controlled.

> This result is inconclusive.

> This evidence may support a review request.

---

## 26. Incorrect Claims

Incorrect claims include:

> The decision was correct.

> The decision was fair.

> The decision was lawful.

> The input was true.

> The operator committed fraud.

> The citizen has won the case.

> The system is accountable.

> The system is A-DAP compliant.

> The verifier proves everything is fine.

These claims exceed citizen-facing verification.

---

## 27. Relationship to Accountability

Citizen-facing verification helps people understand evidence.

It does not replace:

- courts;
- regulators;
- auditors;
- administrative appeals;
- human review;
- remedies;
- legal counsel;
- institutional judgment.

A-DAP creates better evidence.

Citizen-facing language helps make that evidence exercisable.

Institutions must still decide what the evidence means procedurally and legally.

---

## 28. Final Position

Citizen-facing evidence language is part of A-DAP’s accountability surface.

If the interface overclaims, it can turn verification into trust theater.

If the interface underexplains, affected people may be unable to exercise their rights.

The correct goal is neither reassurance nor alarm.

The correct goal is contestable clarity.

A citizen verifier should tell the user:

> what was checked, what was found, what it proves, what it does not prove, and what can still be challenged.
