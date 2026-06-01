# Random Audit Sampling Model

Status: Conceptual architecture note  
Repository context: A-DAP / NDC technical note  
Document type: Architecture note  
Version: 0.1.0

---

## 1. Purpose

This document defines the role of random audit sampling in A-DAP.

A-DAP creates reconstructible evidence.

But reconstructible evidence is not the same as exercised verification.

A system may generate decision envelopes, input provenance envelopes, hashes, signatures, timestamps, and reconstruction rules while still facing little or no actual verification in practice.

This creates Exercise Debt.

The purpose of random audit sampling is to reduce Exercise Debt by making verification exercised, not merely possible.

---

## 2. Core Problem

A-DAP can create strong evidentiary locks.

But a lock that no one tests may have little practical deterrent effect.

In high-impact automated systems, affected people may lack:

- technical knowledge;
- legal representation;
- time;
- procedural access;
- ability to interpret hashes;
- ability to request reconstruction;
- ability to force institutional response.

Therefore, the existence of reconstructible evidence is not enough.

There must be a practical mechanism that causes verification to happen.

Random audit sampling is one such mechanism.

---

## 3. Core Statement

Random audit sampling should make verification exercised, not merely possible.

In short:

> A-DAP can create the object to be verified.  
> Random audit sampling helps ensure that verification actually occurs.

This does not replace citizen contestation, regulatory review, courts, or institutional accountability.

It creates periodic pressure on the system to prove that its reconstruction mechanisms work under real conditions.

---

## 4. Relationship to Exercise Debt

Exercise Debt describes the gap between available verification paths and actually exercised verification.

A system may have high structural NDC but low effective contestability if nobody reconstructs the records.

Example:

```text
Structural NDC: 3
Verification actually exercised: rare or never
Exercise Debt: high
```

Random audit sampling reduces this gap by requiring periodic reconstruction of sampled decisions.

Related file:

- `ADAP-EXP-003.md`

---

## 5. Why Random Sampling Matters

Random sampling matters because it changes the incentive structure.

Without sampling, the operator may assume that most decision records will never be reconstructed.

With sampling, the operator faces a continuing possibility that any decision may be selected for review.

This creates deterrence.

It also creates empirical evidence about whether A-DAP mechanisms work in practice.

Random audit sampling helps detect:

- missing envelopes;
- invalid hashes;
- reconstruction failures;
- explanation mismatches;
- weak input provenance;
- operator-controlled verification paths;
- dependency collapse;
- selective disclosure;
- custody gaps;
- repeated failure patterns.

---

## 6. What Random Audit Sampling Does Not Prove

Random audit sampling does not prove that every decision was correct.

It does not prove that every input was true.

It does not prove that every explanation was fair.

It does not prove that every unsampled case is valid.

It does not eliminate trust.

It does not replace legal remedies.

It does not replace institutional judgment.

It provides sampled evidence about whether the system’s verification architecture works under defined conditions.

---

## 7. Minimum Audit Scope

A random A-DAP audit should include, at minimum:

1. input provenance reconstruction;
2. decision-envelope reconstruction;
3. output consistency verification;
4. explanation comparison;
5. custody graph review;
6. NDC dependency collapse;
7. disclosure of failures and uncertainty.

The audit should not only check whether a hash matches.

It should also check whether the surrounding custody and verification structure remains independent under the declared materiality model.

---

## 8. Sampled Objects

A random audit may sample different object classes.

Examples include:

### Decision Envelope

The audit checks whether the committed decision state can be reconstructed.

### Input Provenance Envelope

The audit checks how the input entered the decision process.

### Output Notice

The audit checks whether the notice given to the affected party matches the committed output.

### Explanation

The audit checks whether a later explanation is consistent with the committed decision record.

### Custody Graph

The audit checks whether claimed verification independence collapses into the same material control domain.

### Citizen-Facing Result

The audit checks whether the affected person receives a clear explanation of what was verified, what was not verified, and what remains contestable.

---

## 9. Sampling Rate

A deployment that uses random audit sampling should declare its sampling rate.

Examples:

```text
0.1% of high-impact decisions
1% of adverse decisions
5% of decisions in a high-risk category
100% of decisions above a severity threshold
```

The correct sampling rate depends on:

- decision volume;
- domain risk;
- harm severity;
- historical failure rate;
- regulatory requirements;
- cost of reconstruction;
- vulnerability of affected people;
- level of automation;
- availability of independent verifiers.

A-DAP does not prescribe a universal sampling rate.

But the sampling rate must be disclosed.

---

## 10. Risk-Based Sampling

Random audit sampling may be risk-weighted.

Higher-risk decisions may require higher sampling rates.

Examples of higher-risk categories:

- denial of public benefits;
- credit denial;
- insurance denial;
- healthcare triage;
- employment screening;
- fraud accusation;
- law enforcement prioritization;
- education access;
- immigration or administrative status decisions.

A risk-based sampling model may combine:

```text
base random sample
+ adverse-decision oversample
+ high-harm category oversample
+ repeated-failure escalation
```

This allows verification to focus where harm is more likely or more severe.

---

## 11. Sample Selection

A random audit model must disclose who selects the sample.

Possible selectors include:

- operator;
- external auditor;
- regulator;
- court-appointed reviewer;
- independent sampling service;
- cryptographic randomness beacon;
- public lottery mechanism;
- multi-party sampling committee.

If the operator controls sample selection, the audit may be structurally weakened.

A stronger design separates sample selection from the operator.

---

## 12. Operator Exclusion Risk

The audit model must disclose whether the operator can exclude cases from the sample.

If exclusions are allowed, the report must disclose:

- exclusion criteria;
- who approved exclusions;
- number of excluded cases;
- reason for each exclusion;
- whether exclusions are independently reviewed.

Uncontrolled exclusion rights can collapse the audit into self-attestation.

A strong audit model should minimize operator-controlled exclusions.

---

## 13. Verification Funding

A random audit model must disclose who pays for verification.

Funding matters because verifier independence can be captured economically.

Possible funding models include:

- operator-funded verification;
- regulator-funded verification;
- pooled industry fund;
- court-supervised fund;
- public-interest audit fund;
- affected-party support fund;
- mixed funding model.

Operator-funded verification is not automatically invalid.

But funding, renewal, scope, access, and disclosure dependencies must be analyzed.

Related file:

- `architecture/verifier-funding-capture.md`

---

## 14. Verifier Independence

The audit model must disclose who performs verification.

A verifier is not independent merely because it is third-party.

The audit should analyze:

- who selected the verifier;
- who pays the verifier;
- who defines audit scope;
- who controls access to evidence;
- who can terminate the verifier;
- who receives the report;
- who decides whether failures are disclosed;
- whether the verifier can publish adverse findings;
- whether the verifier has conflicts of interest.

If the same actor controls the sample, the verifier, the scope, and the disclosure of failures, the audit may collapse into self-attestation.

---

## 15. Failure Disclosure

A random audit model must define how failures are disclosed.

Failure categories may include:

- missing envelope;
- invalid hash;
- missing timestamp evidence;
- reconstruction failure;
- explanation mismatch;
- input provenance missing;
- input provenance weak;
- custody path collapsed;
- NDC claim overstated;
- citizen-facing message misleading;
- verifier unable to access required evidence.

The model should specify whether failures are disclosed to:

- the operator;
- the affected person;
- the verifier;
- the regulator;
- the public;
- a court or oversight body.

Failure disclosure is part of deterrence.

A hidden audit failure may have little accountability value.

---

## 16. Escalation Rules

Random audit sampling should define escalation rules.

Examples:

```text
If one sampled decision fails reconstruction, increase sampling rate for the next period.
```

```text
If repeated failures occur, trigger external review.
```

```text
If input provenance is missing in sampled adverse decisions, require remediation before further automated decisions.
```

```text
If explanation mismatch is detected, notify affected parties in the same decision class.
```

Escalation rules prevent the audit from becoming a passive compliance ritual.

---

## 17. Repeat Failure Pattern

A single failure may be accidental, procedural, or systemic.

The audit model should track repeat failure patterns.

Examples:

- repeated missing envelopes;
- repeated input provenance gaps;
- repeated explanation mismatch;
- repeated failures in one demographic or regional category;
- repeated custody collapse;
- repeated operator-controlled verification bottlenecks.

Repeat failures should trigger stronger review.

A-DAP does not determine the legal consequence.

But it can structure the evidence needed for institutions to decide whether the failure is isolated or systemic.

---

## 18. Input Provenance and Decision Envelopes Must Be Audited Separately

A random audit should not collapse input provenance and decision reconstruction into one undifferentiated check.

A strong decision envelope does not prove strong input provenance.

A valid decision record can preserve a false or poorly captured input.

Therefore, audit reports should distinguish:

```text
Input-provenance reconstruction:
Decision-envelope reconstruction:
Output consistency:
Explanation consistency:
Custody graph independence:
Exercise status:
```

Related files:

- `architecture/input-truth-boundary.md`
- `architecture/input-provenance-envelope.md`

---

## 19. Citizen Notification

The audit model should define whether affected people are notified when their decision is sampled.

Possible patterns:

### Silent Technical Audit

The decision is reconstructed without notifying the affected person.

This may reduce burden, but it may also limit contestability.

### Notice After Audit

The affected person is notified after verification is completed.

This may be useful when failure is found.

### Participatory Audit

The affected person is invited to review or confirm input provenance.

This may strengthen input-truth review, but it may increase cost and complexity.

The correct pattern depends on the domain, privacy rules, and harm level.

---

## 20. Citizen-Facing Language

Random audit results should be communicated in plain language when they affect a person.

A weak message would be:

```text
Audit passed.
```

A better message would be:

```text
The decision record was reconstructed and matched the committed record.

This confirms what the system processed.

It does not prove that the input was true or that the decision was legally correct.

You may still challenge the input, the policy, or the outcome through the available procedure.
```

Related issue:

- `#10 — Define citizen-facing evidence language`

---

## 21. Minimum Random Audit Disclosure

A deployment that claims sampled verification should disclose:

- sampling rate;
- sampling method;
- who selects the sample;
- who funds the verification;
- who performs the verification;
- whether the operator can exclude samples;
- whether failures are disclosed;
- whether affected parties are notified;
- whether remediation is required;
- whether repeat failures trigger escalation;
- whether input provenance and decision envelopes are audited separately.

Without these disclosures, random audit claims should be treated as incomplete.

---

## 22. Audit Report Template

A minimal random audit report may include:

```text
Audit ID:
Audit period:
Decision domain:
Sampling rate:
Sampling method:
Sample selector:
Operator exclusion rights:
Number of decisions in population:
Number of sampled decisions:
Number of reconstructed decisions:
Number of reconstruction failures:
Input provenance failures:
Decision envelope failures:
Output consistency failures:
Explanation mismatch count:
Custody graph collapse findings:
Declared NDC:
Recomputed NDC:
Verifier:
Verifier funding source:
Failure disclosure policy:
Affected party notification policy:
Escalation triggered: yes / no
Limitations:
Interpretation:
```

---

## 23. Correct Claims

Correct claims include:

> This deployment uses random audit sampling to periodically exercise A-DAP reconstruction.

> Sampled decisions are reconstructed under the stated audit model.

> Random audit sampling reduces Exercise Debt but does not eliminate institutional dependence.

> The audit separately reports input provenance, decision reconstruction, output consistency, and custody graph independence.

> Audit failures trigger predefined escalation rules.

---

## 24. Incorrect Claims

Incorrect claims include:

> Random audit sampling proves all decisions are correct.

> A sampled pass proves unsampled cases are valid.

> Operator-controlled sampling is independent by default.

> A third-party auditor is independent by default.

> Hash verification alone is a complete audit.

> Random audit sampling eliminates the need for citizen contestation.

> Random audit sampling creates accountability by itself.

These claims exceed the model.

---

## 25. Failure Mode: Sampling Theater

Sampling theater occurs when a system claims to perform audits while preserving operator control over the sample, verifier, scope, evidence access, and disclosure.

Example:

```text
The operator selects the sample.
The operator pays the verifier.
The operator defines the audit scope.
The operator controls evidence access.
The operator decides whether failures are disclosed.
```

This may look like an audit.

But structurally it may remain self-attestation.

A-DAP analysis should collapse these dependencies when computing independence.

---

## 26. Relationship to NDC

Random audit sampling can improve exercised verification, but it does not automatically increase structural NDC.

Structural NDC depends on independent verification paths after dependency collapse.

Random audit sampling affects whether those paths are exercised.

Therefore, reports should distinguish:

```text
Structural NDC:
Effective NDC:
Exercise Debt:
Sampling model:
Verifier independence:
Failure disclosure:
```

A system can have:

```text
High structural NDC
Low exercise rate
High Exercise Debt
```

Random audit sampling is one way to reduce this gap.

---

## 27. Relationship to Accountability

Random audit sampling creates better evidence and stronger incentives.

But accountability still requires institutions.

Institutions must decide:

- whether failures matter;
- whether affected parties should be notified;
- whether decisions should be reversed;
- whether remedies are required;
- whether penalties are appropriate;
- whether the system should be suspended;
- whether sampling rates should increase;
- whether the deployment remains lawful.

A-DAP and random audit sampling support accountability.

They do not replace it.

---

## 28. Final Position

Random audit sampling is a practical mechanism for reducing Exercise Debt.

It helps ensure that A-DAP evidence is not merely generated, but periodically tested.

The core principle is:

> Random audit sampling should make verification exercised, not merely possible.

This strengthens contestability.

It does not prove correctness.

It does not eliminate trust.

It does not replace institutions.

It makes silent failure harder to sustain.
