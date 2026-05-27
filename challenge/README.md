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

The synthetic case is manually verifiable.

The next step is to add tampering examples and then a one-command verifier.

## How to participate

Clone the repository, inspect the challenge case, and try to break the claim.

If you can reconstruct the evidence, document your result.

If you can falsify or modify the case without detection, open an issue explaining your method.

## Principle

Do not trust the author.

Reconstruct the evidence, or falsify it without detection.
