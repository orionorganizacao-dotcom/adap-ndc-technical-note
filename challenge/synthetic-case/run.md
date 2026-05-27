# How to Run the Synthetic Challenge

This synthetic case is intentionally minimal.

It can now be verified with a one-command Python verifier.

## Files

The case includes:

- `input.json`
- `output.json`
- `envelope.json`
- `custody.json`
- `expected-verdict.json`
- `verify_synthetic_case.py`
- `tampered/`

## Run the verifier

From this folder, run:

```bash
python verify_synthetic_case.py
