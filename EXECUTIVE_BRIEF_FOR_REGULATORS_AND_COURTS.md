# Executive Brief for Regulators and Courts

## A-DAP — Auditable Decision Accountability Protocol

### Purpose of this brief

This brief explains A-DAP in non-technical terms for regulators, courts, public agencies, lawyers, ombuds offices, auditors, compliance officers, and institutional reviewers.

It is not a technical specification.

It is not a legal opinion.

It is not a certification claim.

It is a short explanation of what A-DAP tries to make possible:

When an automated or semi-automated system makes a high-impact decision, can that decision later be independently reconstructed and contested against evidence created at the time of decision?

---

## 1. The problem

Automated systems are increasingly used in decisions that affect people in areas such as:

- credit;
- insurance;
- public benefits;
- healthcare triage;
- employment;
- education;
- fraud detection;
- compliance;
- administrative decision-making;
- judicial or quasi-judicial support systems.

When a person challenges an automated decision, the institution often responds with:

- a written explanation;
- a system log;
- a database record;
- a model card;
- a report;
- a dashboard export;
- an internal audit statement;
- a later-generated summary.

These materials may be useful.

But they may not prove what the system actually committed to at the time of the decision.

The deeper problem is this:

The same institution or system that made the decision often controls the records, explanations, logs, and evidence later used to defend the decision.

That creates a structural weakness.

In simple terms:

The system decides.

The system records.

The system explains.

Then the system, or its operator, asks to be trusted about all three.

A-DAP exists to reduce that dependency.

---

## 2. The core idea

A-DAP proposes that high-impact automated decisions should be born with a reconstructible evidentiary object.

This object is called a decision envelope.

A decision envelope is not just an explanation.

It is not just a log.

It is not just a report.

It is a committed record, created before or at the moment of decision, that can later be reconstructed, checked, and compared against what the institution claims happened.

The central question is:

Can an affected person, auditor, regulator, court, lawyer, or authorized verifier later reconstruct what the system committed to at the time of decision?

If yes, the decision becomes more contestable.

If no, the person may be forced to rely on the institution’s later explanation.

---

## 3. What A-DAP does

A-DAP helps answer a narrow but important question:

Can we reconstruct the committed decision record and detect whether a later explanation, notice, record, or claim diverges from it?

A-DAP can help detect:

- later alteration of decision records;
- mismatch between a later explanation and the committed record;
- substitution of outputs;
- missing or unverifiable decision evidence;
- weak custody claims;
- dependence on a single operator-controlled verification path;
- audit theater where evidence exists but is not independently reconstructible.

A-DAP turns a dispute from:

Trust our explanation.

into:

Compare this explanation against the committed record.

---

## 4. What A-DAP does not do

A-DAP does not prove that an automated decision was correct.

It does not prove that the decision was fair.

It does not prove that the decision was lawful.

It does not prove that the input data was true.

It does not eliminate the need for courts, regulators, auditors, appeals, remedies, or human judgment.

It does not create accountability by itself.

A-DAP provides a stronger evidentiary object for institutions to inspect.

Accountability still requires law, procedure, authority, interpretation, and remedy.

---

## 5. Why this matters for regulators and courts

Many legal and regulatory systems assume that automated decisions can be reviewed later.

But review is weak if the evidence being reviewed is controlled by the same system or organization that made the decision.

A-DAP addresses the evidentiary layer.

It asks whether the decision record was committed in a way that allows later reconstruction outside the original decision process.

For regulators and courts, this matters because a person challenging an automated decision needs more than a narrative explanation.

They need a way to test whether the narrative corresponds to the committed decision record.

A-DAP does not tell the judge or regulator what outcome to reach.

It helps preserve the conditions under which the decision can be meaningfully reviewed.

---

## 6. Decision envelope in plain language

A decision envelope is a technical record that commits to the important parts of a decision event.

Depending on the context, it may include or commit to:

- decision identifier;
- time of decision;
- input record reference or input commitment;
- output or decision result;
- policy or rule version;
- model version;
- threshold or relevant decision rule;
- reconstruction instructions;
- hash or cryptographic commitment;
- signature or authentication method;
- timestamp evidence;
- custody assumptions;
- verification metadata.

The envelope does not need to publish sensitive personal data.

It can commit to data through hashes or controlled disclosure mechanisms.

The goal is not public exposure.

The goal is reconstructible evidence.

---

## 7. Human-readable decision receipt

A technical envelope is not enough.

An affected person should not be expected to understand raw JSON, hashes, timestamp tokens, custody graphs, or reconstruction scripts.

For practical use, A-DAP should also produce a human-readable decision receipt.

A receipt is the person-facing entry point to the decision envelope.

A receipt should identify:

- receipt ID;
- decision reference;
- decision date;
- issuing institution;
- plain-language decision summary;
- verification link or access path;
- whether the technical envelope is available;
- what the receipt supports;
- what the receipt does not prove;
- what may still be contested.

Example:

A-DAP Decision Receipt

Receipt ID: ADAP-8F42-K9

Decision reference: BENEFITS-2026-004812

Decision date: 2026-06-02 14:32 UTC

Issuing institution: Example Public Benefits Agency

Decision summary: Your application was denied because the system classified the reported income as above the eligibility threshold.

Verification access: You may request verification by providing this Receipt ID to the agency appeals office or an authorized reviewer.

What this receipt supports: A decision record exists and may be checked against the corresponding A-DAP decision envelope.

What this receipt does not prove: This receipt does not prove that the decision was correct, fair, lawful, complete, or based on true input data.

The receipt is for access.

The envelope is for reconstruction.

A receipt without an envelope is only a notice.

An envelope without a receipt may be technically valid but socially inaccessible.

---

## 8. Key distinction: explanation is not verification

A-DAP is based on a simple distinction.

An explanation says why the system claims a decision was made.

Verification tests whether the explanation matches the committed decision record.

A system can provide a clear explanation and still lack reconstructible evidence.

A system can be explainable but not auditable.

A-DAP focuses on auditability.

The goal is not simply to make the system explain itself.

The goal is to make the decision record testable outside the system that produced the explanation.

---

## 9. Key distinction: record is not proof

A log is not automatically proof.

A database entry is not automatically proof.

A dashboard is not automatically proof.

A report is not automatically proof.

A signed internal statement is not automatically proof.

These materials may be evidence, but their strength depends on custody, timing, control, and reconstructibility.

A-DAP asks whether the record was committed in a way that makes later alteration or inconsistency detectable under stated assumptions.

The important question is not only:

Does a record exist?

The stronger question is:

Can the record be independently reconstructed and compared against the later claim?

---

## 10. Key distinction: reconstructibility is not practical accessibility

A-DAP improves reconstructibility.

But reconstructibility alone does not guarantee that an affected person can actually exercise verification.

A person may need:

- a readable receipt;
- a verification link;
- access to the envelope;
- a public or authorized verifier;
- legal support;
- institutional cooperation;
- regulator or court authority;
- plain-language explanation of the result.

Therefore, A-DAP should not be treated as access to justice by itself.

It is evidentiary infrastructure.

Practical contestability requires both evidence and a usable path to exercise that evidence.

---

## 11. Procedural finality and perpetual refutability

A-DAP also distinguishes legal finality from evidentiary finality.

A court or agency may need to close a case.

Administrative systems require deadlines, stability, appeal periods, and final decisions.

A-DAP does not claim that every case must remain legally open forever.

Instead, it says that no technical verification event should be treated as absolute proof beyond future challenge.

A decision may become procedurally final under law.

But the evidentiary artifact should remain reconstructible, contestable, and available for later review under the applicable legal rules.

In simple terms:

Procedural finality may close the legal dispute.

It does not make the evidence epistemically final.

---

## 12. How a regulator might use A-DAP

A regulator does not need to inspect every technical detail to use A-DAP as a governance criterion.

A regulator can ask:

1. Did the automated decision create a decision envelope at or before the time of decision?
2. Does the affected person receive a human-readable receipt or reference?
3. Can the decision envelope be reconstructed later?
4. Who controls the generation, storage, preservation, verification, and reconstruction of the evidence?
5. Can a party outside the original decision system verify whether the later explanation matches the committed record?
6. Are the limits of the evidence clearly stated?
7. Does the system avoid claiming that verification proves correctness, fairness, legality, or truth?
8. Is there a usable path for affected people, representatives, or regulators to exercise verification?

These questions can be used in procurement, audits, enforcement, public consultations, administrative review, or regulatory guidance.

---

## 13. How a court might use A-DAP

A court does not need to treat A-DAP as a final answer.

A court can treat A-DAP evidence as one layer of evidentiary structure.

A court may ask:

1. Was a decision envelope created?
2. When was it created?
3. What did it commit to?
4. Who controlled the envelope and verification path?
5. Is the envelope reconstructible?
6. Does the later explanation match the committed decision record?
7. Does the evidence show alteration, substitution, inconsistency, or missing records?
8. What does the evidence not prove?
9. Does the dispute concern input truth, policy legality, discrimination, procedural rights, or remedy beyond the envelope?
10. Is further disclosure, expert review, or institutional explanation required?

A-DAP does not decide the case.

It helps clarify what evidence exists and what remains disputed.

---

## 14. Example: safe interpretation

Suppose a public agency denies a benefit application using an automated eligibility system.

The applicant receives a receipt.

Later, the applicant challenges the denial.

An auditor reconstructs the decision envelope and finds that the later explanation matches the committed decision record.

A safe conclusion would be:

The later explanation is consistent with the committed decision record under the declared verification scope.

An unsafe conclusion would be:

The decision was correct.

The envelope may show consistency between record and explanation.

It does not prove that the input data was true.

It does not prove that the rule was lawful.

It does not prove that the policy was fair.

It does not determine the legal remedy.

---

## 15. Example: useful failure

Suppose the later explanation says that a benefit was denied because income exceeded a threshold.

But the committed decision envelope shows that the actual decision output was based on a missing-document flag.

That mismatch matters.

A-DAP would not automatically decide the legal consequence.

But it would expose that the later explanation does not match the committed record.

This gives the affected person, court, regulator, or reviewer a concrete evidentiary issue to examine.

---

## 16. Minimum institutional requirements

For A-DAP to be useful in public or regulated systems, the following minimum requirements should be considered:

- decision envelopes for high-impact automated decisions;
- human-readable decision receipts;
- clear statement of what the envelope proves and does not prove;
- accessible verification path;
- documented custody assumptions;
- defined reconstruction procedure;
- external or structurally disjoint verification where possible;
- preservation of evidence;
- privacy safeguards;
- plain-language result reporting;
- appeal or review pathway outside the technical system.

Without these, A-DAP may become technically strong but practically inaccessible.

---

## 17. Common unsafe claims

Unsafe claim:

A-DAP proves the decision was correct.

Safer claim:

A-DAP can help determine whether the later explanation matches the committed decision record.

Unsafe claim:

The hash verified, so the decision was lawful.

Safer claim:

The verified hash supports consistency with a committed record under a declared scope. Legal validity remains a separate question.

Unsafe claim:

The citizen received a receipt, so the system is accountable.

Safer claim:

The receipt provides an access point to evidence. Accountability still depends on verification, review, institutional authority, and remedy.

Unsafe claim:

The system is independently verified because it has logs.

Safer claim:

Logs may be useful, but independence depends on who controls generation, preservation, verification, and reconstruction.

Unsafe claim:

A-DAP eliminates trust.

Safer claim:

A-DAP helps locate where trust remains.

---

## 18. What regulators should require from vendors or agencies

Regulators, courts, and public agencies may ask vendors or system operators to provide:

- sample decision envelope;
- sample human-readable receipt;
- reconstruction instructions;
- custody diagram;
- verification procedure;
- list of assumptions;
- explanation of who controls each evidence layer;
- privacy and data minimization plan;
- process for affected-person access;
- export format for legal or administrative review;
- failure mode documentation;
- statement of what the system does not prove.

A vendor should not be allowed to satisfy auditability merely by saying:

We have logs.

We have dashboards.

We can explain the model.

We use a third-party provider.

We sign our records.

We have a compliance report.

The stronger question is:

Can the specific decision record be reconstructed outside the system that made or later justified the decision?

---

## 19. Recommended language for legal or regulatory use

A-DAP may be described as:

A protocol architecture for creating reconstructible evidentiary records around high-impact automated decisions, so that later alteration or inconsistency can be detected under stated assumptions.

A-DAP should not be described as:

- a complete accountability system;
- a fairness guarantee;
- a legality guarantee;
- a replacement for human review;
- a proof that input data was true;
- a proof that the decision was correct;
- a finished compliance product.

---

## 20. Practical checklist

A regulator, judge, lawyer, or reviewer can ask:

- Was the decision high-impact?
- Was the decision automated or semi-automated?
- Was a decision envelope created?
- Was the envelope created before or at the time of decision?
- Was a human-readable receipt issued?
- Can the affected person reference the decision record?
- Can the envelope be reconstructed?
- Can the later explanation be compared with the committed record?
- Who controls the evidence?
- Who controls verification?
- Who can access the envelope?
- What is hidden for privacy reasons?
- What is missing?
- What does the evidence prove?
- What does it not prove?
- What remains legally or factually contestable?

This checklist does not replace legal analysis.

It helps structure the evidentiary review.

---

## 21. Open questions

A-DAP leaves important institutional questions open:

- Who should operate public-interest verifiers?
- Should courts accept decision envelopes as a standard evidentiary object?
- Should regulators require human-readable receipts for automated decisions?
- How should confidential data be reconstructed without public exposure?
- How should verification costs be allocated?
- How should affected people obtain help using receipts?
- How should public defenders, ombuds offices, legal aid organizations, and universities participate?
- How should procedural deadlines interact with later reconstruction?
- How should dependency collapse be standardized?
- What minimum envelope and receipt fields should be mandatory in regulated sectors?

These are not technical details only.

They are part of the governance problem.

---

## 22. Summary

A-DAP is based on a narrow claim:

High-impact automated decisions should leave behind reconstructible evidence.

This evidence should allow later comparison between what the system committed to at the time of decision and what the institution later claims happened.

A-DAP does not prove correctness, fairness, legality, or truth.

It strengthens contestability by making the evidentiary record more reconstructible.

For regulators and courts, the value of A-DAP is not that it answers every question.

Its value is that it helps identify which questions can be tested, which claims are unsupported, and where trust remains concentrated.

## Final principle

A-DAP does not replace judgment.

It gives judgment something stronger to inspect.
