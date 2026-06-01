# External Timestamp Freeze — 2026-06-01

This folder contains the external timestamp freeze artifacts for the A-DAP repository state dated 2026-06-01.

## Purpose

The purpose of this folder is to preserve a specific repository state with an external temporal anchor.

GitHub is used for publication and repository visibility.

SHA-256 is used to fix the content.

RFC 3161 timestamping is used to anchor the existence of the frozen content through an external Time Stamping Authority, or TSA.

This creates a stronger precedence record than a Git commit alone.

## Why this folder exists

A Git commit is useful, but it should not be treated as independent temporal proof.

Commit dates can be controlled by the repository author.

Git history can be rewritten.

A repository can be force-pushed.

For that reason, this freeze uses an external TSA response to prove a narrower claim:

this exact frozen package existed at or before the certified timestamp.

## Expected artifacts

This folder is expected to contain:

```text
adap-freeze-2026-06-01.zip
adap-freeze-2026-06-01.sha256
adap-freeze-2026-06-01.tsq
adap-freeze-2026-06-01.tsr
README.md
```

## Artifact descriptions

### adap-freeze-2026-06-01.zip

The frozen package containing the selected repository files.

This package represents the exact content state being externally timestamped.

### adap-freeze-2026-06-01.sha256

The SHA-256 digest of the frozen package.

Any modification to the package should produce a different hash.

### adap-freeze-2026-06-01.tsq

The RFC 3161 timestamp query generated from the frozen package.

This file commits to the package hash.

### adap-freeze-2026-06-01.tsr

The RFC 3161 timestamp response issued by an external TSA.

This is the external temporal anchor.

### README.md

This document.

It explains the purpose, scope, and verification logic of the freeze folder.

## Verification guide

The full verification procedure is documented in the repository root:

```text
TSA-VERIFY.md
```

That file explains how to:

1. Verify the package hash.
2. Verify the RFC 3161 timestamp response.
3. Interpret successful and failed verification results.
4. Understand the limitation of the timestamp claim.

## Minimal verification logic

A third party should first verify the package hash:

```bash
sha256sum -c adap-freeze-2026-06-01.sha256
```

Then verify the RFC 3161 timestamp response using the timestamp query and the TSA certificate chain:

```bash
openssl ts -verify \
  -in adap-freeze-2026-06-01.tsr \
  -queryfile adap-freeze-2026-06-01.tsq \
  -CAfile cacert.pem \
  -untrusted tsa.crt
```

The exact certificate files depend on the TSA used.

For FreeTSA, see the instructions in:

```text
TSA-VERIFY.md
```

## What a successful verification means

If verification succeeds, it means:

1. The freeze package matches the recorded SHA-256 hash.
2. The timestamp query corresponds to the freeze package.
3. The timestamp response corresponds to the timestamp query.
4. The timestamp response was issued by the external TSA.
5. The frozen content existed at or before the certified timestamp.

## What this does not prove

This freeze does not prove that A-DAP is correct.

It does not prove that all claims in the repository are true.

It does not prove legal ownership by itself.

It does not prove that no similar unpublished work existed before.

It does not prove authorship by itself.

It proves a narrower claim:

this exact frozen content existed at or before the externally certified timestamp.

## Relation to A-DAP

A-DAP argues that high-impact automated decisions should leave behind records that can survive challenge outside the system that produced them.

This folder applies the same principle to the repository itself.

GitHub publishes the artifact.

SHA-256 fixes the artifact.

RFC 3161 anchors the artifact externally in time.

The separation between publication and external timestamping is intentional.

## Recommended release title

```text
External Timestamp Freeze — 2026-06-01
```

## Recommended tag

```text
tsa-freeze-2026-06-01
```

## Recommended commit message

```text
Add external timestamp freeze folder
```

## Status

At creation, this folder may initially contain only this README.

The actual freeze artifacts should be added after the package, hash, timestamp query, and timestamp response are generated.

Until the `.zip`, `.sha256`, `.tsq`, and `.tsr` files are present, this folder is a prepared location for the external timestamp freeze, not yet a complete freeze record.

## Final note

This folder is not a marketing artifact.

It is a precedence and verification artifact.

Its purpose is to make the temporal existence of a specific A-DAP repository state externally checkable.
