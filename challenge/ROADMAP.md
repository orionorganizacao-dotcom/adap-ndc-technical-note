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

Status: completed

Included:

- minimal decision input
- minimal decision output
- decision envelope
- custody trail
- expected verifier result
- manual verification instructions

Files:

- `challenge/synthetic-case/input.json`
- `challenge/synthetic-case/output.json`
- `challenge/synthetic-case/envelope.json`
- `challenge/synthetic-case/custody.json`
- `challenge/synthetic-case/expected-verdict.json`
- `challenge/synthetic-case/run.md`

Success condition:

A third party can inspect the case, reconstruct the decision manually, and confirm that the expected verdict is consistent with the declared input, output, envelope, and custody trail.

Current limitation:

This version is manually verifiable, but not yet a full one-command automated verifier.

## v0.3 — Tampering examples

Status: completed

Included:

- modified input example
- modified output example
- modified envelope example
- modified custody trail example
- tampered examples README

Files:

- `challenge/synthetic-case/tampered/README.md`
- `challenge/synthetic-case/tampered/input-risk-score-modified.json`
- `challenge/synthetic-case/tampered/output-decision-modified.json`
- `challenge/synthetic-case/tampered/envelope-file-reference-modified.json`
- `challenge/synthetic-case/tampered/custody-file-list-modified.json`

Purpose:

- show how small modifications affect the evidence state
- make tamper detection understandable to third parties
- prepare the ground for automated verification

Success condition:

A third party can compare the original synthetic case with tampered examples and understand why the expected verdict should fail.

Current limitation:

This version documents expected tampering failures, but does not yet execute automated detection.

## v0.4 — One-command synthetic verifier

Status: completed

Included:

- verification script
- deterministic reconstruction logic
- expected pass/fail output
- clear command instructions
- validation of the original synthetic case
- detection of the tampered examples

Files:

- `challenge/synthetic-case/verify_synthetic_case.py`
- `challenge/synthetic-case/run.md`

Target command:

```bash
python verify_synthetic_case.py
