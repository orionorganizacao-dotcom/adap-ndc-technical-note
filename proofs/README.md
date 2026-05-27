# Proofs, Claims, Timestamps, and Audit Boundaries

This directory contains integrity and verification-related material for the A-DAP repository.

Its purpose is to help reviewers distinguish between:

- a cryptographic hash;
- a timestamp claim;
- a signature;
- a proof artifact;
- an audit process;
- an independent reconstruction.

This distinction is essential to A-DAP.

A-DAP does not treat every technical artifact as proof.

A-DAP treats proof as a layered condition: an artifact becomes stronger only when it can be independently checked, reconstructed, challenged, and placed outside the sole control of the original author or system.

---

## 1. Purpose of This Directory

The `proofs/` directory exists to support release integrity, custody signals, timestamping, and external verification workflows.

It does not claim that the repository has already been fully audited by an independent third party.

It provides material that can help an external reviewer answer questions such as:

- Was this release anchored by a hash?
- Was a timestamp claim produced?
- Is there a public key available for signature verification?
- Are signed commit instructions available?
- Are there artifacts intended for RFC 3161 or OpenTimestamps verification?
- What remains a claim rather than an independently completed audit?

This directory should be read as a verification support layer, not as a final proof of institutional accountability.

---

## 2. Current Directory Structure

Current structure:

```text
proofs/
├── ots-proof/
├── rfc3161-proof/
├── public-key.asc
├── release-v0.3.1.sha256
├── signed-commit-instructions...
└── timestamp-claim.md
