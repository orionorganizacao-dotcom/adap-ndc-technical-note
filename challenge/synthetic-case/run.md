# How to Run the Synthetic Challenge

This synthetic case is intentionally minimal.

At this stage, the challenge can be inspected manually.

## Files

The case includes:

- `input.json`
- `output.json`
- `envelope.json`
- `custody.json`
- `expected-verdict.json`

## Manual verification

A third party should verify that:

1. `input.json` declares a `risk_score` of `0.12`.
2. `input.json` declares a `threshold` of `0.50`.
3. `output.json` declares the decision as `approved`.
4. The decision is consistent because `0.12` is below `0.50`.
5. `envelope.json` correctly points to `input.json` and `output.json`.
6. `custody.json` lists the files required for reconstruction.
7. `expected-verdict.json` declares the expected result as `pass`.

## Tampering test

Modify any of the following:

- `risk_score`
- `threshold`
- `decision`
- `declared_ndc`
- file names inside the envelope
- files listed in custody

Then compare the modified case with the expected verdict.

## Current status

This is v0.2 of the public challenge.

It is not yet a full automated verifier.

The next version should include a one-command verification script.
