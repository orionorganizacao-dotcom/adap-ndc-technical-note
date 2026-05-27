# A-DAP Public Challenge

This repository does not ask you to trust A-DAP.

It asks you to test whether A-DAP evidence can be independently reconstructed, and whether tampering can remain undetected.

## Core Challenge

Do not trust the author.

Reconstruct the evidence, or falsify it without detection.

## What this challenge tests

A-DAP is not presented here as a claim of invincibility.

A-DAP does not assert that tampering is impossible.

It asserts that undetected tampering has a measurable structural cost.

This challenge exposes that claim to public testing.

## Valid outcomes

A valid public challenge has two possible outcomes:

1. Independent reconstruction succeeds.
2. Tampering succeeds without detection.

Both outcomes are useful.

If reconstruction succeeds, the evidence can be verified without trusting the author.

If tampering succeeds without detection, the protocol, implementation, or NDC claim must be corrected.

## How to participate

Your task is simple:

1. Reconstruct the registered decision independently.
2. Modify the decision, envelope, custody trail, or claimed NDC without being detected by the verifier.

If you succeed, open an issue explaining your method.

If you fail, the failure itself becomes public evidence of resistance under this specific case.

## Important limitation

This challenge does not prove that A-DAP is universally secure.

It only tests whether this specific case can be independently reconstructed or falsified without detection.

A-DAP gains credibility only when it remains open to falsification.

## Planned challenge structure

```text
/challenge
  README.md
  /synthetic-case
    README.md
    envelope.json
    decision_input.json
    decision_output.json
    custody.json
    expected_verdict.json
    run.sh
  /gcd-001
    README.md
    manifest.json
    claimed_ndc.json
    expected_verdict.json
    run.sh
  /attacks
    README.md
    attack-template.md
