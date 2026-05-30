# Exercisable Citizen Verification

A-DAP only becomes socially useful when reconstruction can be exercised without requiring the affected person to become a cryptographer.

A reconstructible decision envelope is necessary.

But it is not sufficient.

If a person receives an envelope, receipt, hash, signature, timestamp token, or verification record and cannot meaningfully use it, contestability remains mostly theoretical.

This file defines the citizen-facing layer of A-DAP:

the layer that turns reconstructible evidence into exercisable verification.

## Core Claim

A-DAP should not require affected people to understand cryptography in order to exercise their right to challenge a high-impact automated decision.

The goal is not to make every citizen a cryptographer.

The goal is to make the verification path usable, reproducible, and institutionally actionable.

A citizen-facing verifier should help a person, advocate, auditor, regulator, lawyer, journalist, or court answer a narrower question:

Does the explanation, notice, or institutional account match the committed decision record?

This does not prove that the decision was correct.

It does not prove that the decision was fair.

It does not prove that the decision was lawful.

It helps identify whether the later account is consistent with the earlier commitment.

That is the evidentiary value.

## The Citizen Gap

A-DAP creates reconstructible decision records.

But affected people may still face a practical gap.

They may receive:

- a decision notice
- a denial letter
- a PDF report
- a receipt
- a hash
- a signature
- a timestamp claim
- an envelope identifier
- a verification link
- a downloadable decision package

Yet they may not know:

- what the envelope means
- whether the envelope is complete
- whether the signature is valid
- whether the timestamp evidence is usable
- whether the reconstruction rules are available
- whether the later explanation matches the committed record
- whether any fields are missing
- whether the verifier itself is controlled by the same operator
- what kind of challenge is possible

This is the citizen gap.

A-DAP cannot be socially effective if the affected person receives evidence but cannot exercise it.

## Design Goal

The purpose of a citizen-facing A-DAP verification layer is to make reconstruction exercisable.

It should translate technical verification into understandable findings without becoming a new authority that must simply be trusted.

The interface should not say only:

Trust this verifier.

It should enable:

Run this procedure.
Inspect this receipt.
Reproduce this result.
See what matches.
See what is missing.
See where trust still remains.

The interface should reduce friction without hiding the evidentiary structure.

## Minimal Citizen-Facing Questions

A citizen-facing verifier should answer at least the following questions.

### 1. Was an envelope provided?

The system should indicate whether a decision envelope or receipt exists.

Possible results:

- Envelope provided.
- Envelope missing.
- Envelope reference provided, but envelope not accessible.
- Envelope format unknown.
- Envelope inaccessible without operator-controlled interface.

### 2. Is the envelope well formed?

The verifier should check whether the envelope contains the expected fields for the declared schema.

Possible results:

- Envelope is well formed.
- Envelope is malformed.
- Required fields are missing.
- Schema version is missing.
- Schema version is unknown.
- Envelope uses an unsupported format.

### 3. Can the committed object be reconstructed?

The verifier should attempt to reconstruct the committed object according to the declared reconstruction rules.

Possible results:

- Reconstruction successful.
- Reconstruction failed.
- Reconstruction rules missing.
- Required input commitment missing.
- Required output commitment missing.
- Canonicalization method missing.
- Reconstruction depends on inaccessible operator-controlled resources.

### 4. Does the reconstructed hash match the commitment?

The verifier should compute the hash of the reconstructed object and compare it with the committed value.

Possible results:

- Hash match.
- Hash mismatch.
- Hash algorithm missing.
- Hash algorithm unsupported.
- Commitment missing.
- Reconstruction incomplete.

### 5. Is the signature valid?

If a signature is present, the verifier should check whether it validates against the declared public key or trust path.

Possible results:

- Signature valid.
- Signature invalid.
- Signature missing.
- Public key missing.
- Public key unavailable outside the operator.
- Public key not independently anchored.
- Signature method unsupported.

### 6. Is timestamp evidence present?

If timestamp evidence is present, the verifier should identify what kind of timestamp claim exists and whether it can be checked.

Possible results:

- Timestamp evidence present and verifiable.
- Timestamp evidence present but not independently verifiable.
- Timestamp claim present without external proof.
- Timestamp missing.
- Timestamp authority unavailable.
- Timestamp evidence depends on operator-controlled records.

### 7. Does the later explanation match the committed record?

The verifier should compare the notice, explanation, or institutional account against the committed decision state.

Possible results:

- Explanation matches committed record.
- Explanation does not match committed record.
- Explanation partially matches committed record.
- Explanation cannot be compared because required fields are missing.
- Explanation refers to a policy or model version not present in the envelope.
- Explanation refers to reasons not committed at the time of decision.

### 8. What is missing?

The verifier should clearly list missing elements.

Examples:

- Missing policy version.
- Missing model version.
- Missing timestamp evidence.
- Missing reconstruction rules.
- Missing public key.
- Missing input commitment.
- Missing output commitment.
- Missing threshold commitment.
- Missing materiality assumptions.
- Missing custody assumptions.
- Missing explanation-to-record mapping.

### 9. Who controls the verification path?

The verifier should help identify whether verification still depends on the operator being verified.

Examples:

- Envelope available only through operator portal.
- Public key hosted only by operator.
- Reconstruction rules unavailable outside operator.
- Timestamp evidence not independently reachable.
- Verification interface controlled by operator.
- No downloadable receipt available.
- No independent anchor available.

This does not automatically prove manipulation.

But it identifies structural dependency.

## Minimal Output Format

A citizen-facing verifier should produce a clear result.

Example:

```text
A-DAP Verification Result

Decision ID:
credit-denial-2026-05-30-001

Envelope:
present

Envelope format:
valid

Reconstruction:
successful

Hash check:
match

Signature:
valid

Timestamp evidence:
present

Explanation match:
failed

Missing fields:
policy version

Structural dependency warning:
public key and reconstruction rules are hosted only by the operator

Interpretation:
This result does not prove the decision was wrong.
It shows that the explanation provided later does not fully match the committed decision record, and that some verification dependencies remain operator-controlled.
```

## Human-Readable Result Levels

A citizen-facing verifier should avoid giving a false sense of certainty.

Instead of returning only pass or fail, it should use layered findings.

### Green: Reconstructible and Consistent

The envelope is present.

The reconstruction succeeds.

The hash matches.

The signature validates.

Timestamp evidence is present or the timestamp claim is clearly labeled.

The later explanation matches the committed record.

No critical missing field is detected.

Meaning:

The later account appears consistent with the committed record under the stated assumptions.

This does not prove that the decision was right, fair, or lawful.

### Yellow: Reconstructible but Incomplete

The envelope is present.

Some verification succeeds.

But relevant fields are missing, ambiguous, unsupported, or dependent on operator-controlled resources.

Meaning:

The record may be useful, but the affected person may need additional evidence, disclosure, or institutional help.

### Red: Inconsistency Detected

The envelope is present.

Reconstruction or comparison detects mismatch.

Examples:

- hash mismatch
- invalid signature
- explanation mismatch
- policy version mismatch
- output mismatch
- missing or altered commitment

Meaning:

The later account diverges from the committed record or the evidence cannot support the claim being made.

This does not automatically decide the remedy.

It creates a contestable inconsistency.

### Gray: Not Exercisable

The affected person received a notice, receipt, or claim, but verification cannot be performed.

Examples:

- no envelope
- no reconstruction rules
- no public key
- no accessible receipt
- no independent timestamp evidence
- no downloadable verification package
- operator-only portal

Meaning:

The decision may have documentation, but the verification path is not exercisable by the affected person or their representative.

## What the Interface Must Not Do

A citizen-facing verifier must not become a new self-validating authority.

It should not merely say:

- verified
- compliant
- trustworthy
- fair
- lawful
- accountable

Unless those claims are separately grounded in institutional, legal, or procedural review.

The verifier should not replace courts, regulators, auditors, lawyers, or human review.

It should produce reproducible findings.

It should show what was checked.

It should show what was not checked.

It should show what assumptions were used.

It should show what remains dependent on the operator.

## Reproducibility Requirement

A citizen-facing verification result should include enough information for another party to reproduce the same result.

At minimum, it should disclose:

- verifier tool name
- verifier version
- schema version
- envelope identifier
- hash algorithm
- signature method
- timestamp evidence type
- reconstruction method
- fields checked
- fields missing
- comparison method
- assumptions used
- warnings produced
- result generated

The result should be exportable.

Possible export formats:

- human-readable report
- JSON verification result
- PDF report
- signed verification receipt
- court or regulator attachment package

The export should not create a new unverifiable claim.

It should preserve the ability to reproduce the verification.

## Local Execution Is Not Enough

Client-side or local verification can reduce friction.

It can help citizens, lawyers, auditors, and regulators exercise the verification path.

But local execution does not automatically create independence.

A verification process can run locally and still depend on operator-controlled inputs, schemas, keys, timestamps, or reconstruction rules.

Therefore, the citizen-facing layer must distinguish:

- local execution
- independent custody
- external anchoring
- reproducible reconstruction
- institutional accountability

Local execution is useful.

It is not independent verification by itself.

## Hosted Verification Is Also Not Enough

A hosted verification portal may be convenient.

But if the hosted verifier is controlled by the same operator being verified, it may recreate the same trust problem.

A hosted verifier should therefore allow:

- downloading the envelope
- downloading the verification result
- reproducing verification with open tools
- checking public keys outside the operator
- checking timestamp evidence outside the operator
- seeing schema and reconstruction rules
- exporting the result for third-party review

A hosted interface can improve usability.

It should not become the only source of truth.

## Minimal Architecture

A basic citizen-facing A-DAP verification layer may include:

```text
Affected Person
    receives
Decision Notice + A-DAP Envelope or Receipt

Verifier Interface
    parses
Envelope, Schema, Signature, Timestamp Evidence, Explanation

Reconstruction Engine
    reconstructs
Committed Decision Object

Comparison Layer
    compares
Committed Record vs Later Explanation

Dependency Analyzer
    checks
Which verification components remain operator-controlled

Output Layer
    produces
Human-readable result + reproducible verification package
```

The architecture should preserve separation between:

- the decision system
- the evidence object
- the verification tool
- the interpretation authority

## Minimal Data Inputs

A citizen-facing verifier may require:

- decision envelope
- decision notice or explanation
- schema version
- public key or key reference
- timestamp evidence or timestamp claim
- reconstruction rules
- optional policy reference
- optional model version reference
- optional challenge metadata

The verifier should clearly state which inputs were provided and which were missing.

## Minimal Data Outputs

The verifier should produce:

- reconstruction status
- hash status
- signature status
- timestamp status
- explanation comparison status
- missing-field list
- dependency warnings
- reproducibility information
- plain-language interpretation
- exportable verification package

## Example: Credit Denial

A person is denied credit by an automated decision system.

The person receives:

- decision notice
- stated reason
- A-DAP envelope
- receipt identifier
- verification URL

The citizen-facing verifier checks the envelope.

Result:

```text
Reconstruction:
successful

Hash:
match

Signature:
valid

Timestamp:
present

Explanation match:
failed

Mismatch:
The notice says the denial was based on income threshold.
The committed record shows the decision was based on a different risk-score threshold.

Interpretation:
This does not prove that the applicant should have received credit.
It shows that the later explanation does not match the committed decision record.
This may support a request for review, disclosure, or regulatory examination.
```

## Example: Public Benefit Denial

A person is denied a public benefit.

The agency provides a decision notice but no reconstructible envelope.

Result:

```text
Envelope:
missing

Reconstruction:
not possible

Explanation comparison:
not possible

Interpretation:
The decision may have documentation, but the affected person cannot independently reconstruct the committed decision state from the materials provided.
This is a contestability weakness.
```

## Example: Healthcare Triage

A patient is assigned a lower triage priority by an automated or semi-automated system.

The hospital provides a notice and a verification package.

Result:

```text
Envelope:
present

Reconstruction:
successful

Hash:
match

Signature:
valid

Timestamp:
present

Explanation match:
partial

Missing field:
clinical rule version

Interpretation:
The record can be partially reconstructed, but the rule version needed to assess the clinical basis of the decision is missing.
This may require institutional review.
```

## Example: Operator-Controlled Verifier

A company provides only a hosted verifier.

The verifier says:

Verified.

But it does not allow the user to download the envelope, inspect the schema, verify the public key externally, or reproduce the result.

Result:

```text
Verification:
not independently reproducible

Dependency warning:
verification depends on operator-controlled interface

Interpretation:
The interface may be useful for convenience, but it does not by itself satisfy independent verification.
The affected person should be able to export the receipt and reproduce verification outside the operator-controlled environment.
```

## Institutional Use

A citizen-facing verification layer is not only for citizens.

It can also help:

- public defenders
- consumer protection agencies
- privacy authorities
- labor regulators
- healthcare regulators
- financial regulators
- courts
- journalists
- civil society organizations
- internal audit teams
- external auditors

The same interface can serve different levels of expertise.

A citizen may need a plain-language result.

A regulator may need the full technical verification package.

A court may need a reproducible evidence bundle.

An auditor may need the custody graph and dependency warnings.

The interface should support all four without collapsing them into one authority.

## Relation to NDC

Citizen-facing verification does not automatically increase NDC.

A usable interface may make verification easier to exercise.

But NDC depends on whether verification paths are materially independent after dependency collapse.

For example:

- If the interface is controlled by the operator, NDC may remain 1.
- If the public key is controlled only by the operator, NDC may remain 1.
- If the timestamp evidence is independently reachable, that may support higher structural independence.
- If the envelope can be downloaded and verified with open tools, exercise becomes easier.
- If the reconstruction rules are public and independently preserved, dependency may be reduced.

The citizen-facing layer therefore improves exercisability.

It does not automatically prove independence.

## Relation to Effective NDC

Effective NDC concerns whether available verification paths are actually exercised.

A citizen-facing verifier can improve Effective NDC by reducing the cost and difficulty of verification.

It can help turn latent verification paths into exercised verification paths.

However, interface availability is not enough.

Effective contestability also depends on:

- awareness
- access
- language
- disability accessibility
- legal support
- cost
- time limits
- institutional responsiveness
- fear of retaliation
- availability of remedies

A-DAP should treat non-exercise as a real weakness.

A verification path that exists but is unusable in practice has limited social value.

## Accessibility Requirements

A citizen-facing verifier should be designed for accessibility.

It should support:

- plain-language summaries
- downloadable reports
- machine-readable exports
- mobile use
- low-bandwidth access
- screen readers
- multiple languages where relevant
- clear warnings
- non-technical explanations
- institutional escalation paths

It should avoid:

- cryptographic jargon as the first layer
- unexplained pass or fail labels
- hidden assumptions
- operator-only portals
- non-exportable results
- unverifiable badges
- claims of fairness or legality without institutional review

## Plain-Language Interpretation Rules

The verifier should translate technical findings carefully.

Examples:

Technical finding:

```text
Hash mismatch.
```

Plain-language interpretation:

```text
The reconstructed record does not match the committed value. This may indicate alteration, substitution, incorrect reconstruction, or missing information.
```

Technical finding:

```text
Signature valid.
```

Plain-language interpretation:

```text
The envelope appears to have been signed by the declared key. This does not prove the decision was correct or fair.
```

Technical finding:

```text
Timestamp evidence present.
```

Plain-language interpretation:

```text
There is evidence that a commitment existed no later than a certain time, subject to the timestamp authority and custody assumptions.
```

Technical finding:

```text
Explanation mismatch.
```

Plain-language interpretation:

```text
The reason later given for the decision does not match the committed decision record.
```

Technical finding:

```text
Operator-controlled verification path.
```

Plain-language interpretation:

```text
The verification still depends on the same organization whose decision is being reviewed.
```

## Escalation Output

A citizen-facing verifier should help produce escalation-ready language.

Example:

```text
I am requesting review of this automated decision because the explanation provided to me does not appear to match the committed decision record.

The A-DAP verification result indicates:

- reconstruction succeeded
- hash matched
- signature was valid
- timestamp evidence was present
- explanation comparison failed

This does not by itself prove that the decision was unlawful or incorrect, but it identifies a specific inconsistency that should be reviewed.
```

If reconstruction is impossible:

```text
I am requesting review of this automated decision because the materials provided do not allow independent reconstruction of the decision state.

The verification result indicates that no usable A-DAP envelope or reconstruction rules were provided.

This limits my ability to contest the decision effectively.
```

## Design Anti-Patterns

A citizen-facing A-DAP layer should avoid the following anti-patterns.

### The Trust Badge

The interface displays:

Verified by A-DAP.

But it does not expose what was verified, which assumptions were used, or how the result can be reproduced.

Problem:

This turns A-DAP into a trust label instead of a verification architecture.

### The Operator Portal Trap

The affected person can only verify the decision through the same operator’s portal.

Problem:

The verification path may still depend on the verified party.

### The PDF Dead End

The person receives a PDF report with no machine-readable envelope or reconstruction package.

Problem:

The report may be useful documentation, but it is not reconstructible evidence by itself.

### The Cryptography Wall

The person receives hashes, keys, and signatures but no usable interface or plain-language result.

Problem:

The evidence exists technically, but the verification path is not meaningfully exercisable.

### The Black-Box Verifier

The verifier says pass or fail but does not disclose what was checked.

Problem:

The verifier becomes another opaque authority.

### The Non-Exportable Result

The user can view the result but cannot download or share it.

Problem:

The result cannot easily support legal, regulatory, journalistic, or institutional review.

## Minimum Viable Product

A minimal citizen-facing A-DAP verifier should allow a user to:

1. Upload or paste a decision envelope.
2. Upload or paste the decision explanation or notice.
3. Run basic reconstruction checks.
4. Validate hash consistency.
5. Validate signature if the public key is available.
6. Check timestamp evidence if available.
7. Compare the explanation against the committed record.
8. Identify missing fields.
9. Identify operator-controlled dependencies.
10. Export a plain-language report and machine-readable result.

The MVP should clearly separate:

- what passed
- what failed
- what was missing
- what could not be checked
- what depends on the operator
- what the result does and does not prove

## Suggested Result Schema

A machine-readable verification result may use a structure like this:

```json
{
  "adap_verification_result": {
    "tool_name": "example-citizen-verifier",
    "tool_version": "0.1.0",
    "schema_version": "citizen-verification-0.1",
    "decision_id": "example-decision-id",
    "envelope_status": "present",
    "reconstruction_status": "successful",
    "hash_status": "match",
    "signature_status": "valid",
    "timestamp_status": "present",
    "explanation_match_status": "failed",
    "missing_fields": [
      "policy_version"
    ],
    "dependency_warnings": [
      "public_key_hosted_only_by_operator",
      "reconstruction_rules_hosted_only_by_operator"
    ],
    "interpretation": "The later explanation does not fully match the committed decision record. This does not prove the decision was wrong, but it creates a contestable inconsistency.",
    "does_not_prove": [
      "truth",
      "fairness",
      "legality",
      "correctness",
      "accountability"
    ]
  }
}
```

## Safe Claims

A citizen-facing A-DAP verifier can safely claim:

- It helps make verification exercisable.
- It can detect mismatches between committed records and later explanations under stated assumptions.
- It can identify missing evidence.
- It can identify operator-controlled dependencies.
- It can produce reproducible verification output.
- It can help affected people, auditors, regulators, and courts focus on concrete inconsistencies.

It should not claim:

- that the decision was fair
- that the decision was lawful
- that the decision was correct
- that the institution is accountable
- that the verifier is the source of truth
- that local execution alone creates independence
- that a valid signature proves the underlying decision was proper
- that a timestamp proves the input was true or complete
- that a pass result eliminates the need for human review

## Final Position

A-DAP begins with reconstructible evidence.

But reconstructible evidence is not enough if affected people cannot exercise reconstruction.

The citizen-facing layer is the bridge between technical auditability and practical contestability.

Its purpose is not to simplify away the hard parts.

Its purpose is to expose them clearly enough that citizens, representatives, auditors, regulators, and courts can act on them.

A-DAP should not ask people to trust the system.

It should help them test the record.
