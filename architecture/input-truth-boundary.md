# Input Truth Boundary

Status: Conceptual boundary  
Repository context: A-DAP / NDC technical note  
Document type: Architecture note  
Version: 0.1.0

---

## 1. Purpose

This document defines a critical boundary in A-DAP:

A-DAP can reconstruct what a system committed to using.

It cannot, by itself, prove that the committed input was true, complete, correctly captured, or faithful to the external world.

This distinction is essential.

Without it, A-DAP could be misinterpreted as proving the truth of the world-state behind a decision.

It does not.

A-DAP proves commitment and reconstructability under stated assumptions.

It does not prove input truth.

---

## 2. Core Statement

A-DAP does not prove that the input was true.

It proves that a given committed input was the input used by the decision process under the stated reconstruction rules.

In short:

> A-DAP records what the system used, not what the world is.

This is not a weakness to hide.

It is a boundary to declare.

---

## 3. The Initial Triad

Every high-impact automated decision involves at least three layers:

1. Input truth
2. Decision logic
3. Output commitment

A-DAP primarily strengthens the second and third layers by making the decision state and resulting record reconstructible.

It helps answer questions such as:

- What input commitment did the system use?
- What model, rule, or policy version was committed?
- What output was committed?
- Did the later explanation match the committed record?
- Was the decision record altered, substituted, or inconsistently reconstructed?

But A-DAP does not automatically answer:

- Was the original input true?
- Was the input correctly captured?
- Was the input complete?
- Was the external-world fact accurately represented?
- Did the user, sensor, institution, or upstream system provide correct data?

Those questions require a separate evidentiary regime.

---

## 4. Example

A public benefits system creates a decision envelope committing to the following input:

```text
Annual income: 30,000
```

Later, the applicant claims:

```text
I submitted annual income as 50,000.
```

A-DAP can help prove that the system committed to using `30,000` at the time of decision.

A-DAP can also help detect whether a later explanation diverges from that committed state.

But A-DAP cannot, by itself, prove whether the applicant actually submitted `30,000` or `50,000`.

The dispute has moved upstream.

The question is no longer only:

> Did the decision record change?

It becomes:

> Was the input capture process itself accurate, fair, and independently verifiable?

---

## 5. Boundary Principle

The input truth boundary can be stated as follows:

> A-DAP can make the committed decision state reconstructible, but it cannot make the external-world state self-proving.

This means that input truth must be supported by additional mechanisms.

Examples include:

- signed user submissions;
- submission receipts;
- independent intake logs;
- dual-channel confirmation;
- sensor attestation;
- human review records;
- external data-source receipts;
- timestamped form snapshots;
- audit trails for data correction;
- provenance records for upstream datasets;
- dispute procedures for input correction.

These mechanisms may be integrated with A-DAP, but they are not automatically provided by A-DAP.

---

## 6. Input Commitment vs Input Truth

A-DAP distinguishes between input commitment and input truth.

### Input Commitment

An input commitment is a cryptographic or procedural commitment to the data used by the decision process.

It answers:

> What input did the system commit to using?

### Input Truth

Input truth concerns whether that committed input accurately corresponds to the external-world fact or user-provided information.

It answers:

> Was the input correct?

These are different questions.

A system can have a valid input commitment and still use a false input.

A system can be reconstructible and still be wrong.

A-DAP makes the error contestable.

It does not make the input true.

---

## 7. Why This Matters

If this boundary is not declared, A-DAP can be overclaimed.

A weak claim would be:

> A-DAP proves the decision was based on correct data.

This is not valid.

A stronger and more accurate claim is:

> A-DAP proves which committed data the system used under stated reconstruction rules, allowing disputes about input truth to be separated from disputes about record alteration.

This distinction improves accountability.

It prevents three different disputes from being collapsed into one:

1. Did the system use the committed input?
2. Was the committed input true?
3. Was the decision legally, ethically, or procedurally valid?

A-DAP mainly addresses the first question.

It can support the others, but it does not resolve them by itself.

---

## 8. Relationship to NDC

The input truth boundary also affects NDC analysis.

A system may have independent verification paths for decision reconstruction while still having a single dependency path for input capture.

Example:

```text
Decision envelope NDC > 1
Input capture NDC = 1
```

In that case, the decision record may be reconstructible, while the input truth remains dependent on the original collector.

This should be disclosed.

A-DAP compliance for decision reconstruction does not automatically imply independent input provenance.

---

## 9. Input Provenance as a Separate Layer

Input provenance should be treated as a separate evidentiary layer.

A mature A-DAP deployment should declare whether input provenance is:

- self-reported;
- operator-controlled;
- user-signed;
- externally attested;
- independently timestamped;
- sensor-derived;
- institutionally verified;
- legally certified;
- adversarially contestable.

This allows reviewers to distinguish between:

```text
The system used this input.
```

and:

```text
This input was true.
```

The first may be reconstructible through A-DAP.

The second requires additional proof.

---

## 10. Failure Mode: Truth Laundering

A dangerous misuse of A-DAP is truth laundering.

Truth laundering occurs when a valid decision envelope is used to imply that the committed input was true.

Example:

> The record is cryptographically valid, therefore the input must have been correct.

This is false.

A cryptographically valid envelope can preserve a false input perfectly.

A-DAP can preserve error.

That preservation is useful because it makes the error inspectable.

But preservation is not truth.

---

## 11. Correct Use

A correct A-DAP statement would be:

> The decision envelope reconstructs the committed input, model version, policy version, output, and verification metadata used at the time of decision.

Another correct statement would be:

> The envelope supports a dispute about whether the later explanation matches the committed record.

A stronger deployment may add:

> Input provenance is separately supported by signed submission receipts and independently timestamped intake records.

That additional claim must be proven separately.

---

## 12. Incorrect Use

An incorrect A-DAP statement would be:

> A-DAP proves the user provided this exact input.

Another incorrect statement would be:

> A-DAP proves the source data was accurate.

Another incorrect statement would be:

> A-DAP proves the decision was factually correct.

These claims exceed the protocol.

---

## 13. Practical Implication

A-DAP implementers should separate at least three evidence layers:

1. Input provenance evidence
2. Decision-state commitment evidence
3. Output and explanation consistency evidence

A-DAP directly targets the second and third layers.

The first layer must be designed, disclosed, and verified separately.

A high-quality implementation should make this separation visible in its reports.

---

## 14. Review Checklist

A reviewer should ask:

- What input was committed?
- Who controlled input capture?
- Was the input user-submitted, sensor-derived, or institutionally supplied?
- Was the input independently receipted?
- Was the input signed or timestamped before decision?
- Can the affected party contest the captured input?
- Can the original submission be reconstructed?
- Is input provenance independent from the decision operator?
- Does the report distinguish input commitment from input truth?
- Does the system falsely imply that a valid envelope proves a true input?

If these questions are not answered, the deployment may be reconstructible but still weak at the input-truth layer.

---

## 15. Relationship to Accountability

A-DAP gives institutions a stronger object to inspect.

But institutions must still decide:

- whether the input was valid;
- whether the input capture process was fair;
- whether the user had a chance to correct the input;
- whether the decision logic was lawful;
- whether the decision should be reversed;
- whether a remedy is required.

A-DAP supports accountability.

It does not replace it.

---

## 16. Canonical Sentence

The canonical sentence for this boundary is:

> A-DAP records what the system committed to using; it does not prove what the world was.

Alternative formulation:

> A-DAP can reconstruct the committed decision state, but input truth remains a separate evidentiary problem.

---

## 17. Final Position

The input truth boundary strengthens A-DAP by preventing overclaim.

A-DAP should not be sold as proof that a decision was factually correct.

It should be understood as a protocol for making the committed decision state reconstructible and contestable.

That is narrower.

It is also more defensible.
