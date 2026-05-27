# A-DAP Public Challenge

This repository does not ask you to trust A-DAP.

It asks you to test whether A-DAP evidence can be independently reconstructed, and whether tampering can remain undetected.

## Challenge objective

A valid public challenge has two possible paths:

1. Reconstruct the registered decision independently.
2. Modify the decision, envelope, custody trail, or claimed NDC without being detected by the verifier.

Both outcomes are useful.

A-DAP does not claim that tampering is impossible. It claims that undetected tampering has a measurable structural cost.

## Current status

The public challenge currently includes:

- public challenge README
- roadmap
- synthetic challenge case
- attack template
- manual verification instructions
- tampered examples
- one-command synthetic verifier

The synthetic case is now automatically verifiable with a one-command Python verifier.

The tampered examples show how changes to inputs, outputs, envelope references, and custody declarations can alter the evidence state.

The verifier validates the original synthetic case and detects the documented tampering examples.

## Challenge structure

```text
challenge/
  README.md
  ROADMAP.md
  attacks/
    attack-template.md
  synthetic-case/
    README.md
    input.json
    output.json
    envelope.json
    custody.json
    expected-verdict.json
    run.md
    verify_synthetic_case.py
    tampered/
      README.md
      input-risk-score-modified.json
      output-decision-modified.json
      envelope-file-reference-modified.json
      custody-file-list-modified.json
