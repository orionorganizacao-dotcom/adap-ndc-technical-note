# Input Provenance Envelope

Status: Conceptual architecture note  
Repository context: A-DAP / NDC technical note  
Document type: Architecture note  
Version: 0.1.0

---

## 1. Purpose

This document defines the Input Provenance Envelope as a complementary evidentiary layer to the A-DAP decision envelope.

A-DAP decision envelopes can reconstruct what a system committed to using during a decision.

They do not, by themselves, prove that the input was true, complete, correctly captured, or faithfully derived from the external world.

For high-impact automated decisions, this distinction matters.

Many disputes are not only about what the system did with an input.

They are about whether the input itself was captured, transmitted, transformed, or interpreted correctly.

The purpose of an Input Provenance Envelope is to make input capture and input provenance more contestable.

---

## 2. Why Decision Envelopes Are Not Enough

A decision envelope answers questions such as:

- What input commitment did the system use?
- What model, policy, or rule version was committed?
- What output was committed?
- Did the later explanation match the committed record?
- Was the decision record altered or substituted?

But a decision envelope does not automatically answer:

- Was the original input true?
- Was the input correctly captured?
- Was the input complete?
- Was the input submitted by the affected person?
- Was the input derived from a reliable upstream system?
- Was the input changed before reaching the decision system?
- Did the user have a chance to review or correct the input?

A valid decision envelope can preserve a false input perfectly.

That preservation is useful because it makes the error inspectable.

But preservation is not truth.

---

## 3. Core Statement

Input provenance must be treated as a separate evidentiary envelope, not as an implied property of the decision envelope.

In short:

> A-DAP records what the system committed to using.  
> An Input Provenance Envelope records how that input entered the decision process.

The two envelopes answer different questions.

A decision envelope asks:

> What did the system use when deciding?

An input provenance envelope asks:

> How did the system obtain what it used?

Both may be needed for meaningful contestability.

---

## 4. Relationship to the Input Truth Boundary

This document builds on the Input Truth Boundary.

Related file:

- `architecture/input-truth-boundary.md`

The Input Truth Boundary states:

> A-DAP records what the system committed to using; it does not prove what the world was.

The Input Provenance Envelope does not eliminate this limitation.

It narrows the evidentiary gap by documenting the input capture path, custody path, and reviewability of the input before decision.

It still does not prove ultimate truth.

It can, however, make disputes about input capture more specific and more testable.

---

## 5. Input Commitment vs Input Provenance

A-DAP distinguishes between input commitment and input provenance.

### Input Commitment

Input commitment is the record of what input the decision system committed to using.

It answers:

> What input was used by the decision process?

### Input Provenance

Input provenance is the record of how that input was obtained, transformed, confirmed, transmitted, or attested before being used.

It answers:

> Where did this input come from, who controlled it, and how can its capture be challenged?

These are different evidentiary layers.

A system can have a valid input commitment and weak input provenance.

Example:

```text
Decision envelope NDC > 1
Input provenance NDC = 1
```

In that case, the decision record may be reconstructible while the input capture path remains dependent on the original operator.

---

## 6. The Input Provenance Envelope

An Input Provenance Envelope is a structured evidentiary object that commits to the origin, capture, transformation, and custody path of an input before it enters the decision envelope.

It is not a replacement for the decision envelope.

It is an upstream companion.

A simplified flow is:

```text
Input event
→ Input Provenance Envelope
→ Decision Envelope
→ Output / Notice / Explanation
→ Reconstruction / Contestation
```

The Input Provenance Envelope should be created at or before the moment when the input becomes available to the decision system.

It should be preserved separately from the later explanation.

---

## 7. Minimum Fields

A minimal Input Provenance Envelope may include commitments to:

- input identifier;
- affected party identifier or pseudonymous reference;
- input source;
- submission channel;
- capture timestamp or timestamp claim;
- user-submitted value commitment;
- operator-recorded value commitment;
- upstream system identifier;
- transformation rules, if any;
- data normalization rules, if any;
- schema version;
- consent or authorization reference, if applicable;
- user confirmation receipt, if available;
- correction window or dispute procedure;
- capture interface version;
- custody path from capture to decision system;
- hash algorithm;
- canonicalization method;
- signature or authentication method;
- timestamp evidence, where possible;
- provenance assumptions;
- reconstruction instructions.

The exact fields depend on the domain.

The envelope should not expose sensitive personal data unnecessarily.

It should commit to the relevant state in a way that can later support controlled reconstruction or challenge.

---

## 8. Input Source Classes

An Input Provenance Envelope should declare the input source class.

Examples include:

### User-Submitted Input

The affected person directly submits the input through a form, portal, application, signed document, or assisted intake process.

Examples:

- income declaration;
- address;
- employment status;
- health questionnaire;
- consent form.

### Institution-Supplied Input

A public agency, company, school, bank, hospital, employer, or other institution supplies the input.

Examples:

- tax record;
- credit bureau record;
- school record;
- medical record;
- benefit history;
- employment record.

### Sensor-Derived Input

The input is captured by a sensor, device, monitoring system, or automated observation layer.

Examples:

- biometric capture;
- camera event;
- geolocation signal;
- medical device measurement;
- industrial sensor reading.

### Model-Derived Input

The input is itself an output of another model or automated system.

Examples:

- risk score;
- fraud score;
- triage category;
- extracted document field;
- classification label.

### Hybrid Input

The input is assembled from multiple sources.

Example:

```text
User-submitted form + external database + model-derived risk score
```

Hybrid inputs should disclose each source class separately.

---

## 9. Provenance NDC

Input provenance requires its own NDC analysis.

A decision envelope may have multiple independent verification paths while input capture remains fully controlled by a single actor.

Therefore, reports should avoid a single undifferentiated NDC claim.

A more honest report would distinguish:

```text
Decision-envelope NDC:
Input-provenance NDC:
Output-consistency NDC:
Exercise NDC:
```

This prevents a system from laundering weak input provenance through strong decision reconstruction.

A-DAP compliance for decision reconstruction does not automatically imply independent input provenance.

---

## 10. Citizen-Facing Interpretation

A citizen-facing verifier must communicate provenance limits clearly.

It should not merely say:

```text
Hash verified.
```

That is too weak and may mislead the user.

A better citizen-facing explanation would be:

```text
The decision record matches the committed input used by the system.

This confirms what the system processed.

It does not, by itself, prove that the input was originally submitted correctly or that the source data was true.

To challenge the input itself, review the input provenance record or submission receipt.
```

The interface must distinguish at least three layers:

1. What the user says they submitted;
2. What the system recorded as input;
3. What the decision system committed to using.

This is not only a cryptographic problem.

It is a communication-of-evidence problem.

---

## 11. Failure Mode: Provenance Laundering

Provenance laundering occurs when a valid input or decision envelope is used to imply stronger input reliability than the evidence supports.

Example of an invalid claim:

> The decision envelope is valid, therefore the input was true.

Example of another invalid claim:

> The input was hashed, therefore the input capture process was reliable.

These claims are false.

Hashing an input does not prove that the input was true.

Signing an input does not prove that the input was complete.

Timestamping an input does not prove that the input was fairly captured.

A valid envelope may preserve a flawed input path.

That is still useful, but the limitation must be disclosed.

---

## 12. Relationship to Exercise Debt

Input provenance also affects Exercise Debt.

A system may expose reconstructible evidence, but if affected people cannot understand or exercise the verification process, the protection remains socially inactive.

Without low-cost or mandatory sampled verification, reconstructibility may exist structurally while remaining socially inactive.

This matters because high-impact systems often operate across power asymmetries.

Affected people may lack:

- technical knowledge;
- legal representation;
- time;
- documentation;
- access to receipts;
- ability to interpret hashes;
- ability to force institutional response.

For this reason, input provenance should be designed for exercise, not merely archival integrity.

---

## 13. Random Audit Requirement

A-DAP and input provenance mechanisms become stronger when verification is periodically exercised.

A practical pattern is mandatory random audit sampling.

Example:

```text
For every N high-impact decisions, a statistically defined sample is reconstructed by an independent verifier.
```

The audit should include:

- input provenance reconstruction;
- decision-envelope reconstruction;
- output consistency verification;
- explanation comparison;
- custody graph review;
- NDC dependency collapse;
- disclosure of failures and uncertainty.

This reduces the risk that verification exists only in theory.

Without random or low-cost verification, the system may become:

> a strong lock on a door no one can test.

Random audit sampling does not solve every problem.

But it lowers Exercise Debt.

---

## 14. Minimum Random Audit Disclosure

A deployment that claims sampled verification should disclose:

- sampling rate;
- sampling method;
- who selects the sample;
- who funds the verification;
- who performs the verification;
- whether the operator can exclude samples;
- whether failures are publicly reported;
- whether affected parties are notified;
- whether remediation is required;
- whether repeat failures trigger escalation.

If the operator controls the sample, the verifier, the scope, and the disclosure of failures, the audit may collapse into self-attestation.

---

## 15. Correct Claims

Correct claims include:

> The decision envelope confirms what input commitment the system used at the time of decision.

> The input provenance envelope records how the input entered the decision process under stated assumptions.

> The input provenance record supports disputes about whether the captured input matches the submitted or source input.

> Input provenance NDC is reported separately from decision-envelope NDC.

> Random sampled verification reduces Exercise Debt but does not eliminate institutional dependence.

---

## 16. Incorrect Claims

Incorrect claims include:

> The decision envelope proves the input was true.

> The input provenance envelope proves the world-state was true.

> A valid hash proves the user submitted the correct data.

> A valid timestamp proves the input capture process was fair.

> A single NDC score proves the whole system is independently verifiable.

> A citizen verifier automatically creates accountability.

These claims exceed the protocol.

---

## 17. Implementation Pattern

A mature deployment should separate three evidentiary layers:

```text
Input Provenance Envelope
Decision Envelope
Output / Explanation Consistency Record
```

Each layer should have its own:

- scope;
- custody assumptions;
- canonicalization rules;
- NDC analysis;
- verification method;
- failure modes;
- citizen-facing interpretation.

This separation helps prevent one strong layer from hiding another weak layer.

---

## 18. Review Checklist

A reviewer should ask:

- What input source class is involved?
- Who controlled the input capture interface?
- Was the input user-submitted, institution-supplied, sensor-derived, model-derived, or hybrid?
- Was the user given a receipt?
- Was the input independently timestamped?
- Was the input signed or authenticated?
- Were transformations applied before decision?
- Can the original input submission be reconstructed?
- Can the affected party challenge the captured input?
- Is input provenance NDC reported separately?
- Does the citizen-facing interface explain what verification does not prove?
- Is random audit sampling required?
- Who selects the audit sample?
- Who pays the verifier?
- Are failed audits disclosed?
- Does the report distinguish input truth, input provenance, and input commitment?

If these questions are not answered, the system may be reconstructible at the decision layer but weak at the input provenance layer.

---

## 19. Relationship to Accountability

Input provenance improves the quality of the object available for institutional review.

But it does not replace:

- legal rights;
- administrative appeals;
- evidentiary hearings;
- regulatory enforcement;
- human review;
- remedies;
- institutional judgment.

A-DAP and Input Provenance Envelopes create better evidence.

Institutions must still use that evidence.

---

## 20. Final Position

The Input Provenance Envelope is a necessary complement to the A-DAP decision envelope.

It prevents a valid decision envelope from being misused as proof that the input was true.

It also prevents weak input capture from being hidden behind strong decision reconstruction.

The core principle is:

> Decision envelopes reconstruct what the system used.  
> Input provenance envelopes reconstruct how the system got what it used.

Both are necessary for mature contestability.

Neither is a complete accountability system by itself.
