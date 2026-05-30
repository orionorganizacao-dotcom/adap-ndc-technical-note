# Citizen Verifier UI Specification

A citizen verifier must convert A-DAP evidence into a usable verification flow without converting the interface into a new trust authority.

A-DAP creates reconstructible decision evidence.

But reconstructible evidence only becomes socially useful when affected people, advocates, auditors, regulators, lawyers, journalists, and courts can actually exercise the verification path.

This file specifies a citizen-facing user interface for A-DAP verification.

The goal is simple:

The citizen should not need to understand the proof in order to exercise the verification path, but the proof must remain reproducible by someone else.

## Core Claim

A citizen-facing verifier should allow a non-technical user to check whether a later explanation matches the committed decision record.

The interface should make the result understandable.

The underlying verification should remain exportable, inspectable, and reproducible.

The verifier should not become a new authority.

It should not ask the citizen to trust a badge.

It should help the citizen test the record.

## Problem

A-DAP can produce:

- decision envelopes
- hashes
- signatures
- timestamp evidence
- reconstruction rules
- custody assumptions
- materiality assumptions
- verification metadata

But most citizens cannot use these directly.

A person denied credit, employment, public benefits, insurance, education access, or healthcare priority is unlikely to know:

- how to parse an envelope
- how to canonicalize a record
- how to compute a hash
- how to validate a signature
- how to inspect timestamp evidence
- how to compare an explanation against a committed decision object
- how to identify operator-controlled dependencies
- how to produce a report usable by a lawyer, regulator, court, or public agency

Without a usable interface, A-DAP may create evidence that only specialists can exercise.

That would preserve a power imbalance.

## Design Objective

The citizen verifier should make A-DAP verification:

- understandable
- mobile-friendly
- reproducible
- exportable
- accessible
- institutionally useful
- resistant to trust-badge misuse
- honest about limitations

The interface should answer:

- Was an A-DAP envelope provided?
- Is the envelope complete enough to check?
- Can the committed record be reconstructed?
- Does the reconstructed record match the commitment?
- Is the signature valid?
- Is timestamp evidence present and usable?
- Does the later explanation match the committed record?
- What is missing?
- What remains controlled by the operator?
- What can the citizen do next?

The interface must also say what it cannot prove.

It must not claim that the decision was true, fair, lawful, correct, or accountable.

## Primary User Flow

A minimal mobile user flow should look like this:

```text
Step 1:
Upload, paste, or scan the A-DAP receipt.

Step 2:
Upload or paste the explanation, notice, denial letter, or decision statement.

Step 3:
Run verification.

Step 4:
Show a plain-language result.

Step 5:
Show technical details for auditors or representatives.

Step 6:
Export a report.
```

The user should not need to understand cryptography to complete the flow.

The technical verification must still remain reproducible.

## Entry Methods

The citizen verifier should support several ways to provide the decision evidence.

### Paste Envelope

The user pastes a text-based A-DAP envelope, receipt, or JSON object.

UI label:

```text
Paste your A-DAP receipt or envelope
```

### Upload File

The user uploads a file.

Supported examples:

- JSON envelope
- PDF notice
- text notice
- signed receipt
- timestamp token
- zipped verification package

UI label:

```text
Upload your decision file
```

### Scan QR Code

The user scans a QR code included in a decision notice.

The QR code may point to:

- a downloadable envelope
- a receipt identifier
- a verification package
- a public anchor
- a timestamp record

UI label:

```text
Scan QR code from your decision notice
```

### Enter Receipt ID

The user enters a receipt ID.

UI label:

```text
Enter receipt ID
```

The verifier should warn if the receipt can only be retrieved through an operator-controlled portal.

### Paste Explanation

The user pastes the explanation received from the institution.

UI label:

```text
Paste the explanation or decision notice you received
```

### Upload Explanation

The user uploads the explanation as a PDF, image, or text file.

UI label:

```text
Upload explanation or decision notice
```

If OCR or extraction is needed, the tool should clearly label extracted text as extracted text, not as the original document.

## Home Screen

The home screen should be simple.

Suggested layout:

```text
A-DAP Citizen Verifier

Check whether the explanation you received matches the committed decision record.

This tool does not decide whether the decision was fair, lawful, or correct.
It checks whether the later explanation is consistent with the earlier committed record.

[Paste receipt]
[Upload file]
[Scan QR code]
[Enter receipt ID]

Optional:
[Paste or upload explanation]

[Check record]
```

The first screen should avoid cryptographic jargon.

Technical details should be available, but not forced onto the citizen at the beginning.

## Verification Button

The main action should be clear.

Suggested button labels:

```text
Check record
```

or:

```text
Verify decision record
```

Avoid labels like:

```text
Prove fairness
```

```text
Validate accountability
```

```text
Certify decision
```

Those labels overclaim.

## Result Levels

The verifier should use four primary result levels.

### Green: Explanation Matches the Record

Plain-language label:

```text
The explanation appears to match the committed record.
```

Meaning:

- envelope was present
- reconstruction succeeded
- hash matched
- signature was valid, if available
- timestamp evidence was present or clearly labeled
- explanation matched the committed record
- no critical missing fields were detected

Required warning:

```text
This does not prove the decision was fair, lawful, or correct. It only means the explanation appears consistent with the committed record under the stated assumptions.
```

### Yellow: Record Incomplete or Partially Checkable

Plain-language label:

```text
The record can be partly checked, but important information is missing.
```

Meaning:

- envelope may be present
- some checks may pass
- some fields may be missing
- some assumptions may be unclear
- some verification resources may be operator-controlled
- explanation comparison may be incomplete

Required warning:

```text
This record may still be useful, but additional information may be needed before the decision can be meaningfully challenged.
```

### Red: Explanation Does Not Match the Record

Plain-language label:

```text
The explanation does not appear to match the committed record.
```

Meaning:

- reconstruction succeeded or partially succeeded
- comparison detected inconsistency
- explanation diverged from committed decision state
- hash, signature, output, policy, threshold, or explanation mapping may have failed

Required warning:

```text
This does not automatically prove the decision was wrong. It identifies a specific inconsistency that may support review, disclosure, or escalation.
```

### Gray: Verification Not Exercisable

Plain-language label:

```text
This decision cannot be independently checked with the materials provided.
```

Meaning:

- no envelope was provided
- no reconstruction rules were provided
- no accessible receipt exists
- public key is missing
- timestamp evidence is missing or operator-controlled
- verification requires an operator-only portal
- the user does not have enough information to run the check

Required warning:

```text
The decision may have documentation, but the verification path is not exercisable from the materials provided.
```

## Result Screen

The result screen should show plain-language findings first.

Example red result:

```text
Result:
The explanation does not appear to match the committed record.

What matched:
- Envelope was present.
- Reconstruction succeeded.
- Hash matched.
- Signature was valid.
- Timestamp evidence was present.

What did not match:
- The explanation says the decision was based on income threshold.
- The committed record shows the decision used a different risk-score threshold.

What this means:
This does not prove the decision was wrong, unfair, or unlawful.
It identifies a specific inconsistency that may support review or escalation.

Next steps:
- Download the verification report.
- Request human review.
- Ask the institution to explain the mismatch.
- Share the report with a lawyer, regulator, auditor, or advocate.
```

## Technical Details Screen

The result screen should include an expandable technical section.

Suggested label:

```text
Technical details
```

This section should include:

- decision ID
- envelope status
- schema version
- reconstruction status
- hash algorithm
- hash result
- signature method
- signature result
- timestamp evidence type
- timestamp result
- explanation comparison method
- missing fields
- dependency warnings
- verifier tool version
- assumptions used
- files checked
- output generated

Example:

```text
Technical Details

Decision ID:
credit-denial-2026-05-30-001

Envelope:
present

Schema:
adap-envelope-v0.4.2

Reconstruction:
successful

Hash algorithm:
SHA-256

Hash result:
match

Signature:
valid

Timestamp:
present

Explanation comparison:
failed

Missing fields:
none

Dependency warnings:
public key hosted only by operator

Verifier:
citizen-verifier-ui-v0.1.0
```

## Dependency Warning Screen

The verifier should show whether the verification path depends on the operator.

Suggested label:

```text
Who controls the verification path?
```

Possible warnings:

```text
The envelope is available only through the operator portal.
```

```text
The public key is hosted only by the operator.
```

```text
The reconstruction rules are hosted only by the operator.
```

```text
The timestamp evidence is not independently reachable.
```

```text
The verifier interface is controlled by the same organization that made the decision.
```

```text
No downloadable receipt was provided.
```

Plain-language interpretation:

```text
This does not prove manipulation. It means the verification path still depends on the organization whose decision is being reviewed.
```

## Cost of Reconstruction

A-DAP must treat reconstruction cost as part of practical contestability.

A decision envelope may be technically reconstructible but socially unusable if reconstruction requires:

- expert knowledge
- paid software
- expensive legal help
- specialized cryptographic tools
- access to private infrastructure
- long processing time
- operator permission
- institutional authority

If only specialists can reconstruct the record, A-DAP creates evidence but does not fully democratize contestation.

The citizen verifier should therefore minimize the cost of first-level reconstruction.

## Reconstruction Cost Questions

Every A-DAP deployment should ask:

- Who pays for basic verification?
- Who pays when verification fails?
- Who pays when the record is incomplete?
- Who pays for expert reconstruction?
- Who pays for legal interpretation?
- Who maintains the verifier?
- Who funds independent verification infrastructure?
- Who pays for accessibility and translation?
- Who pays when the operator provides unusable evidence?
- Who pays when the citizen cannot afford review?

These questions are not secondary.

They determine whether contestability is real or merely formal.

## Possible Funding Models

A-DAP does not prescribe one funding model.

But a citizen verifier may be supported by several models.

### Public Verification Service

A regulator, public agency, ombudsman, court, or public defender hosts a verifier.

Strength:

- public access
- institutional legitimacy
- possible free use

Risk:

- underfunding
- political capture
- limited technical capacity
- slow updates

### Civil Society Verifier

A nonprofit, consumer protection organization, digital rights group, or university hosts a verifier.

Strength:

- public-interest orientation
- independent review culture
- advocacy integration

Risk:

- limited resources
- uneven coverage
- sustainability risk

### Independent Audit Marketplace

Independent auditors offer reconstruction and verification services.

Strength:

- expert review
- scalable professional ecosystem
- sector specialization

Risk:

- cost barrier
- verifier funding capture
- inconsistent quality
- dependency on paid access

### Operator-Funded Public Verifier

Operators are legally required to fund verification infrastructure, but cannot control its operation.

Strength:

- shifts cost away from citizens
- scalable funding
- aligns burden with decision-maker

Risk:

- governance capture
- indirect influence
- dependency through funding
- weak independence if not structurally separated

### Freemium Verification

Basic verification is free.

Advanced expert review is paid or subsidized.

Strength:

- low barrier for simple checks
- possible sustainability

Risk:

- two-tier justice
- complex cases may become inaccessible
- incentives may distort triage

### Court or Regulator Attachment Service

The verifier generates a report package accepted by courts or regulators.

Strength:

- direct institutional usability
- supports escalation
- reduces procedural friction

Risk:

- jurisdiction-specific design
- procedural complexity
- possible exclusion of informal review

## Cost Principle

The affected person should not bear the full cost of making a high-impact automated decision contestable.

A stronger A-DAP deployment should shift the basic cost of verification toward:

- the operator
- the regulator
- the public accountability infrastructure
- the institution deploying the automated decision system
- a structurally independent verification mechanism

The citizen should be able to perform at least a basic check without becoming dependent on expensive experts.

## UI Requirement: Cost Transparency

The verifier should clearly show when a result requires additional paid or expert review.

Example:

```text
Basic verification completed.

Some issues require expert review:
- policy interpretation
- legal relevance
- clinical rule evaluation
- fairness assessment

This tool does not provide legal, medical, or financial advice.
```

The verifier should avoid implying that a citizen must pay to discover whether the envelope is usable.

Basic exercisability should be low-friction.

## Next-Step Guidance

The verifier should provide next steps based on result level.

### Green Next Steps

```text
The explanation appears consistent with the committed record.

You may still request human review if you believe the decision was unfair, unlawful, or based on incorrect information.
```

### Yellow Next Steps

```text
The record is incomplete or only partly checkable.

You may request:
- the missing fields
- the reconstruction rules
- the public key
- the timestamp evidence
- the policy or model version
- a human review
```

### Red Next Steps

```text
An inconsistency was detected.

You may:
- download the verification report
- request human review
- ask the institution to explain the mismatch
- send the report to a regulator, lawyer, auditor, advocate, or court
```

### Gray Next Steps

```text
Verification is not exercisable with the materials provided.

You may request:
- the A-DAP envelope
- the reconstruction rules
- the public key
- timestamp evidence
- a downloadable verification package
- a human review
```

## Escalation Templates

The verifier should generate plain-language escalation text.

### Explanation Mismatch

```text
I am requesting review of this automated decision because the explanation provided to me does not appear to match the committed decision record.

The A-DAP verification result indicates that reconstruction succeeded, the hash matched, the signature was valid, timestamp evidence was present, but the explanation comparison failed.

This does not by itself prove that the decision was unlawful or incorrect, but it identifies a specific inconsistency that should be reviewed.
```

### Missing Envelope

```text
I am requesting review of this automated decision because the materials provided do not allow independent reconstruction of the decision state.

The verification result indicates that no usable A-DAP envelope or reconstruction rules were provided.

This limits my ability to contest the decision effectively.
```

### Operator-Controlled Verification

```text
I am requesting review of this automated decision because the verification path appears to depend on the same organization whose decision is being reviewed.

The verification result indicates that key verification materials are available only through operator-controlled resources.

This does not prove manipulation, but it limits independent contestability.
```

### Incomplete Record

```text
I am requesting review of this automated decision because the record is only partially reconstructible.

The verification result indicates that some checks succeeded, but relevant fields or reconstruction materials are missing.

Please provide the missing materials or explain why they cannot be provided.
```

## Export Requirements

The citizen verifier should allow the user to export:

- a plain-language report
- a machine-readable JSON result
- the original envelope
- the decision explanation
- the reconstructed object, where legally and privacy appropriate
- hash comparison results
- signature verification results
- timestamp verification results
- dependency warnings
- missing-field list
- tool version and schema version
- assumptions used
- date and time of verification

The export should be usable by:

- the affected person
- a lawyer
- a regulator
- a court
- an auditor
- a journalist
- a public defender
- a civil society organization

## Export Warning

Every export should include a limitation notice.

Suggested text:

```text
This verification report does not prove that the decision was true, fair, lawful, or correct.

It reports whether the materials provided allowed reconstruction and whether the later explanation appeared consistent with the committed decision record under the stated assumptions.
```

## UI Anti-Patterns

A citizen verifier should avoid the following patterns.

### Trust Badge UI

Bad pattern:

```text
A-DAP Verified
```

without showing what was checked.

Why it fails:

It turns A-DAP into a trust label.

Better pattern:

```text
Record checked.
Explanation comparison failed.
Download reproducible report.
```

### Operator-Only Verification

Bad pattern:

```text
Verify only inside the operator portal.
```

Why it fails:

The verification path may remain controlled by the verified party.

Better pattern:

```text
Download receipt.
Verify locally or with an independent verifier.
Export report.
```

### Cryptography-First UI

Bad pattern:

```text
Enter SHA-256 digest, Ed25519 key, canonicalization method, timestamp token.
```

Why it fails:

It blocks non-technical users before they can exercise verification.

Better pattern:

```text
Upload or paste your receipt.
We will check the technical details and show you what they mean.
```

### Pass or Fail Only

Bad pattern:

```text
Passed.
```

or:

```text
Failed.
```

Why it fails:

It hides what was checked and what remains uncertain.

Better pattern:

```text
Hash matched.
Signature valid.
Timestamp present.
Explanation mismatch detected.
Public key hosted only by operator.
```

### Non-Exportable Result

Bad pattern:

```text
Result visible only on screen.
```

Why it fails:

The user cannot use the result for review, complaint, audit, court, or regulator action.

Better pattern:

```text
Download report.
Download JSON result.
Share verification package.
```

### Legal Overclaim UI

Bad pattern:

```text
This decision is unlawful.
```

Why it fails:

A-DAP verification does not decide legality.

Better pattern:

```text
This result identifies an inconsistency that may support review or legal analysis.
```

## Accessibility Requirements

The citizen verifier should support:

- mobile-first layout
- plain-language explanations
- low-bandwidth mode
- screen reader compatibility
- large text mode
- color plus text labels
- keyboard navigation
- multilingual content where relevant
- downloadable reports
- no required account for basic checks where possible
- clear privacy notices
- clear limitation notices

Color alone should never carry the result.

Use both color and text.

Example:

```text
Red result:
Explanation does not match the committed record.
```

Not only:

```text
Red icon.
```

## Privacy Requirements

The verifier may process sensitive decision data.

It should minimize data exposure.

Preferred design:

- process locally when possible
- avoid unnecessary storage
- clearly state whether data is uploaded
- allow offline verification where possible
- allow deletion of uploaded materials
- avoid requiring account creation for basic verification
- avoid sharing data with third parties by default
- allow user-controlled export

If hosted verification is used, the verifier should disclose:

- who operates the service
- what data is uploaded
- how long data is retained
- whether data is logged
- whether data is shared
- whether the operator of the verifier is connected to the decision-maker

## Reproducibility Requirements

The citizen verifier should produce results that another party can reproduce.

At minimum, the result should include:

- tool name
- tool version
- schema version
- verification date
- decision ID
- envelope hash
- reconstruction status
- hash algorithm
- hash result
- signature method
- signature result
- timestamp evidence type
- timestamp result
- explanation comparison method
- missing fields
- dependency warnings
- assumptions used

The result should be understandable to the citizen and inspectable by a technical reviewer.

## Suggested Result Schema

A machine-readable output may use this structure:

```json
{
  "adap_citizen_verification_result": {
    "tool_name": "citizen-verifier",
    "tool_version": "0.1.0",
    "schema_version": "citizen-ui-result-0.1",
    "verification_time": "2026-05-30T00:00:00Z",
    "decision_id": "example-decision-id",
    "result_level": "red",
    "plain_language_result": "The explanation does not appear to match the committed record.",
    "envelope_status": "present",
    "reconstruction_status": "successful",
    "hash_status": "match",
    "signature_status": "valid",
    "timestamp_status": "present",
    "explanation_match_status": "failed",
    "missing_fields": [],
    "dependency_warnings": [
      "public_key_hosted_only_by_operator"
    ],
    "does_not_prove": [
      "truth",
      "fairness",
      "legality",
      "correctness",
      "accountability"
    ],
    "recommended_next_steps": [
      "download_report",
      "request_human_review",
      "ask_institution_to_explain_mismatch"
    ]
  }
}
```

## Minimal Wireframe

A minimal interface may be structured like this:

```text
Screen 1:
A-DAP Citizen Verifier

Check whether the explanation you received matches the committed decision record.

[Paste receipt]
[Upload file]
[Scan QR code]
[Enter receipt ID]

[Next]

Screen 2:
Add the explanation you received

[Paste explanation]
[Upload notice]
[Skip if not available]

[Check record]

Screen 3:
Result

Status:
The explanation does not appear to match the committed record.

Checks:
Envelope: present
Reconstruction: successful
Hash: match
Signature: valid
Timestamp: present
Explanation match: failed

Warnings:
Public key hosted only by operator.

What this means:
This does not prove the decision was wrong.
It identifies a specific inconsistency that may support review.

[Download report]
[Download JSON]
[Request missing information]
[Show technical details]
```

## Minimal MVP Scope

A first MVP should support:

- paste JSON envelope
- upload JSON envelope
- paste explanation text
- basic schema validation
- hash verification
- signature status placeholder or validation where key is provided
- timestamp status placeholder or validation where evidence is provided
- explanation comparison placeholder or deterministic field comparison
- missing-field detection
- dependency warning checklist
- plain-language result
- exportable JSON result
- exportable plain-language report

The MVP does not need to solve every domain.

It should prove that a citizen-facing verification path can exist without overclaiming what it proves.

## Non-MVP Items

The following may come later:

- OCR for PDF notices
- multilingual interface
- regulator submission integration
- court-ready export package
- mobile app
- browser extension
- QR code scanner
- external timestamp authority integration
- public key registry integration
- independent verifier registry
- automated policy comparison
- sector-specific modules for credit, healthcare, employment, insurance, education, and public benefits

## Browser Extension Version

A browser extension could help users verify decisions received online.

Possible flow:

```text
1. User opens a decision notice in a web portal.
2. Extension detects A-DAP receipt or envelope.
3. User clicks "Check A-DAP record."
4. Extension extracts or requests the envelope.
5. Extension runs local or hybrid verification.
6. Extension shows result.
7. User exports report.
```

Risks:

- extension security
- browser permissions
- phishing
- operator blocking
- incomplete extraction
- false confidence
- dependency on extension maintainer

Safe claim:

A browser extension may reduce friction, but it does not automatically increase structural independence.

## Mobile App Version

A mobile app could support:

- QR scanning
- receipt upload
- local verification
- report export
- offline mode
- saved cases
- escalation templates
- sharing with advocates or regulators

Risks:

- app store dependency
- device security
- data retention
- unclear operator identity
- accessibility gaps
- maintenance cost

Safe claim:

A mobile app can make verification easier to exercise, but the evidentiary force must still come from reproducible verification, not from the app’s authority.

## Web App Version

A web app could support:

- upload
- paste
- scan
- verify
- export
- technical details
- public documentation
- regulator-friendly report generation

Risks:

- hosted verifier capture
- server-side data exposure
- operator influence
- inability to reproduce locally
- trust-badge misuse

Safe claim:

A web app can improve usability, but it should provide exportable and reproducible verification packages.

## Governance of the Verifier

A citizen verifier is itself a governance object.

It should disclose:

- who operates it
- who funds it
- who maintains it
- whether it is open source
- whether it stores data
- whether it depends on operator-controlled services
- whether verification can be reproduced elsewhere
- whether it has been independently reviewed

A verifier that hides its own governance can recreate the problem A-DAP is designed to expose.

## Relation to NDC

The citizen verifier may improve exercisability.

It does not automatically increase NDC.

NDC depends on whether the verification path remains materially disjoint after dependency collapse.

Examples:

- Operator-controlled web verifier may still be NDC=1.
- Local verification with operator-controlled keys may still be NDC=1.
- Independent timestamp evidence may increase structural strength.
- Public reconstruction rules may reduce dependency.
- Independent key anchoring may reduce dependency.
- Exportable receipts may support external review.

The UI should therefore distinguish:

- usability
- reproducibility
- structural independence
- institutional accountability

## Relation to Effective NDC

The citizen verifier can improve Effective NDC by making verification more likely to be exercised.

It reduces the cost of action.

It makes the verification path visible.

It gives citizens and representatives a usable report.

But Effective NDC also depends on:

- awareness
- access
- literacy
- disability access
- language
- legal support
- time limits
- fear of retaliation
- availability of remedies
- institutional responsiveness

A usable verifier is necessary for practical contestability.

It is not sufficient by itself.

## Implementation Notes

A simple implementation may include these modules:

```text
Input Parser
    accepts envelope, receipt, QR, file, or text

Schema Validator
    checks expected fields

Reconstruction Engine
    rebuilds committed decision object

Hash Checker
    compares reconstructed hash to committed hash

Signature Checker
    validates signature if key is available

Timestamp Checker
    checks timestamp evidence if available

Explanation Comparator
    compares notice or explanation to committed record

Dependency Analyzer
    identifies operator-controlled verification components

Result Generator
    produces plain-language and machine-readable output

Export Module
    generates report and JSON verification package
```

Each module should disclose whether it ran, failed, was skipped, or could not run because required data was missing.

## Failure Modes

The citizen verifier may fail in several ways.

### False Confidence

The interface makes the user believe a decision is fair or lawful because technical checks passed.

Mitigation:

Always display limitation notices.

### Hidden Dependency

The interface hides that keys, schemas, receipts, or reconstruction rules are operator-controlled.

Mitigation:

Show dependency warnings.

### Non-Reproducible Output

The interface gives a result but no reproducible details.

Mitigation:

Always allow export.

### Expert Capture

Only paid experts can interpret results.

Mitigation:

Provide plain-language explanations and escalation templates.

### Operator Capture

The decision-maker controls the verifier.

Mitigation:

Support external verification and disclose operator control.

### Data Exposure

The user uploads sensitive data to a verifier without understanding retention or sharing.

Mitigation:

Use local processing where possible and disclose privacy terms clearly.

## Safe Claims

A citizen verifier can safely claim:

- It helps users exercise A-DAP verification.
- It can check whether provided materials are reconstructible.
- It can detect mismatches under stated assumptions.
- It can identify missing fields.
- It can identify dependency warnings.
- It can produce exportable reports.
- It can reduce the cost of first-level verification.
- It can help citizens and institutions focus on concrete inconsistencies.

It should not claim:

- that the decision was fair
- that the decision was lawful
- that the decision was correct
- that accountability has been achieved
- that the verifier is the source of truth
- that a green result eliminates the need for human review
- that local execution alone creates independence
- that a hosted verifier is independent by default
- that a valid signature proves input truth
- that a timestamp proves decision fairness
- that usability equals structural independence

## Final Position

A-DAP cannot stop at the decision envelope.

A citizen who cannot exercise reconstruction still depends on others to transform evidence into contestation.

The Citizen Verifier is the usability layer of A-DAP.

Its job is not to make hard problems disappear.

Its job is to make the verification path visible, usable, exportable, and reproducible.

The citizen should see a simple result.

The auditor should see the technical record.

The regulator should see the dependency structure.

The court should receive a reproducible evidence package.

The verifier should not ask to be trusted.

It should help the record be tested.
