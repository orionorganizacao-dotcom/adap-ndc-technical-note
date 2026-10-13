# Synthetic Challenge

This is the entry point of the A-DAP Public Challenge.

Its purpose is to provide a minimal and reproducible case that anyone can run quickly.

## Goals

- reduce friction for first-time testers
- allow independent reconstruction of the case
- provide a simple baseline before the GCD-001 challenge

## Expected outcome

The fixture consistency checks should pass on the unmodified case.

The bundled one-file alterations should trigger their documented checks. These checks evaluate stated relationships; they do not authenticate changes against an original baseline. Coordinated edits to both the input and output can remain internally consistent and pass.

## Why this case exists

The synthetic case is intentionally small.

It is not the strongest A-DAP claim.

It is the onboarding case: a simple public test of fixture consistency before moving to a more serious case.

## Verification boundary

The verifier checks whether the fixture's decision agrees with its stated input and threshold, whether the envelope names the expected files, and whether the custody manifest lists those files. These are internal consistency and manifest-membership checks only.

It does not compare the files with a trusted baseline or authenticated commitment. A coordinated edit that changes both `input.json` and `output.json` while preserving the decision rule can pass. The verifier does not establish file integrity, artifact provenance, or actual custody; the manifest is itself an input assertion, not independent custody evidence.

The `verification_note` in `custody.json` asserts that any modification should require verifier detection. The coordinated-edit regression test demonstrates that this assertion is not satisfied by the current verifier; treat it as an unverified fixture claim, not a verification guarantee.

Run the regression check with:

```bash
python -B challenge/synthetic-case/test_verify_synthetic_case.py
```

## Next step

Complete this synthetic case first.

Then proceed to the GCD-001 challenge.
