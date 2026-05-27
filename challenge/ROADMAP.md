# A-DAP Public Challenge Roadmap

This roadmap tracks the evolution of the A-DAP Public Challenge from a public scaffold into an executable, reproducible, and adversarially testable verification case.

## v0.1 — Public challenge scaffold

Status: completed

Included:

- public challenge README
- synthetic challenge README
- attack template

Purpose:

- define the public falsification frame
- invite reconstruction attempts
- invite tampering attempts
- separate public testing from authorial self-attestation

## v0.2 — Executable synthetic case

Status: pending

To include:

- minimal decision input
- minimal decision output
- decision envelope
- custody trail
- expected verifier result
- one-command verification script

Success condition:

A third party can clone the repository, run one command, and reproduce the expected verifier result.

## v0.3 — Tampering examples

Status: pending

To include:

- modified input example
- modified output example
- modified envelope example
- modified custody trail example
- expected verifier failures

Success condition:

A third party can see how small modifications are detected by the verification process.

## v0.4 — GCD-001 challenge

Status: pending

To include:

- GCD-001 case documentation
- claimed NDC
- reconstruction instructions
- verifier instructions
- issue-based challenge process

Success condition:

A third party can independently reconstruct the GCD-001 claim or challenge it through a documented attack attempt.

## Principle

This challenge is not a claim of invincibility.

A-DAP gains credibility only when its claims remain open to public reconstruction, adversarial testing, and falsification.
