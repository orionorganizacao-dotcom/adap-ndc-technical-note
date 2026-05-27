# Attack Template

Use this template to document a reconstruction attempt, tampering attempt, or verifier bypass attempt against the A-DAP Public Challenge.

## Attack name

Describe the attack in one short sentence.

## Target

Specify what you are attacking:

- decision record
- envelope
- custody trail
- claimed NDC
- verifier
- reconstruction process
- other

## Modified files

List every file modified during the attempt.

## Expected verifier result

Describe what you expected the verifier to report.

## Actual verifier result

Paste or summarize the actual verifier output.

## Method

Explain the method used.

Include enough detail for another person to reproduce the attempt.

## Why this may challenge A-DAP

Explain why this result may weaken, falsify, or refine the A-DAP claim.

## Reproduction steps

1. Clone the repository.
2. Apply the modification.
3. Run the verifier.
4. Record the result.

## Outcome

Select one:

- Reconstruction succeeded.
- Tampering was detected.
- Tampering was not detected.
- Verifier failed.
- Claim requires revision.
