# Human-Readable Decision Receipt

## Why decision envelopes need a human-facing receipt

### Abstract

A-DAP decision envelopes are designed to make high-impact automated decisions reconstructible.

However, an affected person should not be expected to understand a raw JSON envelope, cryptographic hash, timestamp token, custody graph, or reconstruction script.

If A-DAP is to support practical contestability, the affected person must receive a human-readable decision receipt.

A human-readable receipt does not replace the technical envelope.

It provides an accessible entry point to the envelope.

Its purpose is to tell the person:

- that a decision record exists;
- how to reference it;
- how to request or exercise verification;
- what the receipt supports;
- what it does not prove;
- what may still be contested.

In short:

A decision envelope is for reconstruction.

A decision receipt is for access.

---

## 1. Core Claim

A-DAP should not assume that affected people can interact directly with technical evidence.

A valid decision envelope may be useless in practice if the person affected by the decision receives no understandable receipt, no reference code, no verification path, and no explanation of what can be challenged.

Therefore, high-impact automated decisions should produce both:

- a machine-readable decision envelope;
- a human-readable decision receipt.

The receipt should not overclaim.

It should not say:

```text
This decision was correct.
```

It should say:

```text
A decision record was created and can be checked under stated conditions.
```

---

## 2. Minimum Receipt Requirements

A human-readable A-DAP receipt should include at least the following fields.

### 2.1 Receipt Identifier

A short identifier that the affected person can copy, quote, or provide to a lawyer, regulator, court, ombuds office, public agency, journalist, or verifier.

Example:

```text
Receipt ID: ADAP-8F42-K9
```

The identifier should be short enough to use in email, SMS, forms, phone calls, and printed notices.

### 2.2 Decision Reference

A reference to the decision event.

Example:

```text
Decision reference: BENEFITS-2026-004812
```

This may be an internal case number, application number, claim number, or decision identifier.

### 2.3 Decision Date

The date and time when the decision was committed or recorded.

Example:

```text
Decision date: 2026-06-02 14:32 UTC
```

If the timestamp is only a claim and not independently anchored, the receipt should say so.

Example:

```text
Timestamp status: internal timestamp claim
```

If externally anchored:

```text
Timestamp status: externally timestamped
```

### 2.4 Issuing Institution

The receipt should identify the institution, agency, company, or system operator that issued the decision.

Example:

```text
Issuing institution: Example Public Benefits Agency
```

This does not prove institutional correctness.

It only identifies the issuing party for reference and later review.

### 2.5 Plain-Language Decision Summary

A short human-readable summary.

Example:

```text
Decision summary: Your application was denied because the system classified the reported income as above the eligibility threshold.
```

This summary must not replace the technical envelope.

It is a notice layer.

The envelope remains the reconstruction layer.

### 2.6 Verification Link or Access Path

A path to verify or request verification.

Example:

```text
Verification link: https://agency.gov/verify/ADAP-8F42-K9
```

If a public link is not possible because of privacy or security constraints, the receipt should explain the access path.

Example:

```text
Verification access: You may request verification by providing this Receipt ID to the agency appeals office or an authorized reviewer.
```

### 2.7 Envelope Availability Status

The receipt should state whether the technical envelope is directly available, requestable, restricted, or unavailable.

Examples:

```text
Envelope status: available through authenticated access
```

```text
Envelope status: available upon administrative request
```

```text
Envelope status: restricted because the record contains protected personal data
```

The receipt should not imply that a decision is verifiable if no practical access path exists.

### 2.8 What This Receipt Supports

The receipt should include a narrow statement.

Example:

```text
What this receipt supports:
A decision record was committed under the A-DAP process and may be checked against the corresponding technical envelope.
```

### 2.9 What This Receipt Does Not Prove

The receipt must prevent overclaim.

Example:

```text
What this receipt does not prove:
It does not prove that the decision was correct, fair, lawful, complete, or based on true input data.
```

### 2.10 What Can Still Be Contested

The receipt should explain that verification does not end the dispute.

Example:

```text
You may still contest:
- whether the input data was true;
- whether the system used the correct record;
- whether the rule or policy was lawful;
- whether the explanation matches the committed record;
- whether the decision should be reviewed by a human authority.
```

---

## 3. Example Human-Readable Receipt

```text
A-DAP Decision Receipt

Receipt ID: ADAP-8F42-K9
Decision reference: BENEFITS-2026-004812
Decision date: 2026-06-02 14:32 UTC
Issuing institution: Example Public Benefits Agency

Decision summary:
Your application was denied because the system classified the reported income as above the eligibility threshold.

Verification status:
A technical decision record was created for this decision.

Envelope status:
Available through authenticated access.

Verification link:
https://agency.gov/verify/ADAP-8F42-K9

What this receipt supports:
This receipt supports that a decision record exists and may be checked against the corresponding A-DAP decision envelope.

What this receipt does not prove:
This receipt does not prove that the decision was correct, fair, lawful, complete, or based on true input data.

You may still contest:
- whether your input data was accurate;
- whether the agency used the correct record;
- whether the rule or threshold was lawful;
- whether the explanation matches the committed decision record;
- whether you are entitled to human review or appeal.

Keep this receipt.
You may provide the Receipt ID to a lawyer, regulator, court, ombuds office, public defender, journalist, or authorized verifier.
```

---

## 4. Receipt vs Envelope

The receipt and the envelope have different functions.

The receipt is for humans.

The envelope is for reconstruction.

The receipt should be understandable without technical expertise.

The envelope should be precise enough for independent verification.

A receipt without an envelope is only a notice.

An envelope without a receipt may be technically valid but socially inaccessible.

A-DAP needs both.

---

## 5. Safe Claims

A human-readable receipt should not say:

```text
This proves the decision was correct.
```

A safer statement is:

```text
This receipt identifies a decision record that may be checked against the corresponding A-DAP envelope.
```

A human-readable receipt should not say:

```text
The agency followed the law.
```

A safer statement is:

```text
This receipt does not determine legal validity. It preserves a reference to evidence that may support review.
```

A human-readable receipt should not say:

```text
No further review is needed.
```

A safer statement is:

```text
Verification of the record does not prevent further review of input truth, policy validity, fairness, legality, or remedy.
```

A human-readable receipt should not say:

```text
The citizen can verify everything alone.
```

A safer statement is:

```text
This receipt provides a reference that the affected person, representative, regulator, court, or authorized verifier may use to request or exercise verification.
```

---

## 6. Unsafe Receipt Patterns

A receipt can become misleading if it turns a technical reference into a false assurance.

Unsafe patterns include:

- presenting a receipt as proof that the decision was fair;
- presenting a verified hash as proof that the decision was correct;
- giving a receipt code without any way to request the envelope;
- using a verification link that only returns a green checkmark without explaining scope;
- hiding the fact that input truth was not verified;
- hiding the fact that the timestamp is only an internal claim;
- making the receipt understandable only to engineers;
- making the verification process inaccessible to the affected person;
- using the receipt as a substitute for appeal rights or human review.

A receipt should increase contestability.

It should not become a new form of procedural closure.

---

## 7. Accessibility Requirements

A human-readable receipt should be designed for real use.

It should support:

- email delivery;
- SMS reference code;
- printed notice;
- mobile access;
- screen readers;
- plain-language explanation;
- multilingual versions where appropriate;
- low-bandwidth access;
- offline reference through a short code;
- export for legal or administrative review.

A receipt that only works for engineers is not a citizen-facing receipt.

---

## 8. Privacy and Security

A receipt should not expose sensitive personal data unnecessarily.

The receipt may include a short identifier, but the verification process may require authentication, authorization, or controlled disclosure.

A-DAP should avoid turning public proof surfaces into privacy leaks.

The receipt should therefore separate:

- public reference information;
- protected decision payloads;
- authorized verification access;
- exportable evidence packages;
- privacy-preserving reconstruction.

The receipt should help the person access verification without exposing protected data to the public.

---

## 9. Relation to Citizen Verification

A human-readable receipt is the entry point for citizen verification.

A citizen verifier should allow the person or representative to:

- enter the Receipt ID;
- upload or paste a receipt;
- request the associated envelope;
- verify whether the committed record exists;
- check whether later explanations match the committed record;
- export a plain-language verification result;
- see what was not verified;
- understand possible next steps.

The verifier should not become a new unquestionable authority.

Its procedure, assumptions, inputs, and outputs should remain reconstructible and contestable.

---

## 10. Relation to Legal and Administrative Review

A-DAP receipts should support legal and administrative review without pretending to replace it.

A receipt can help a lawyer, judge, regulator, public defender, ombuds office, or reviewer identify the relevant decision record.

It can help separate questions such as:

- Was a decision record committed?
- Does the later explanation match the committed record?
- Was the input provenance reconstructible?
- Was the input itself true?
- Was the policy lawful?
- Was the person entitled to human review?
- Was the remedy properly applied?

The receipt does not decide these questions.

It helps locate evidence for deciding them.

---

## 11. Open Problems

Several questions remain open:

- What minimum receipt fields should be mandatory across sectors?
- Should Receipt IDs follow a standardized format?
- How should receipts work when public verification links are not possible?
- How should receipts be delivered in offline or low-connectivity environments?
- How should a person recover a lost receipt?
- How should receipts handle minors, guardians, representatives, or legal proxies?
- How should receipts be used in courts, administrative appeals, and regulatory complaints?
- How should receipts avoid leaking sensitive information?
- How should receipts distinguish between internal timestamp claims and external timestamp proof?
- How should receipts explain verification results without overclaiming?
- Who must provide the envelope when a receipt is presented?
- What happens if the receipt exists but the envelope is missing?
- What happens if the envelope exists but the affected person cannot access a verifier?
- What should a regulator require as the minimum receipt format?
- What should count as receipt delivery: email, SMS, postal notice, portal notification, printed document, or API response?

These are not cosmetic design questions.

They determine whether A-DAP evidence can be exercised by real people.

---

## 12. Conclusion

A-DAP decision envelopes make automated decisions more reconstructible.

But affected people need a human-facing entry point.

A receipt is that entry point.

A human-readable receipt does not prove that a decision was correct.

It gives the affected person a stable reference to the evidence needed to challenge, review, or reconstruct the decision.

## Final Principle

The envelope preserves the evidence.

The receipt gives people a way to use it.
