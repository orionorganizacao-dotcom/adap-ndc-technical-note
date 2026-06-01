# TSA Verification Guide

This document explains how to verify the external timestamp freeze for this repository.

## Purpose

Git commits and GitHub publication timestamps are useful for publication history, but they are not sufficient as independent temporal proof.

A Git commit timestamp can be controlled by the repository author, and Git history can be rewritten.

For that reason, this repository uses an external RFC 3161 timestamp token issued by a Time Stamping Authority, or TSA, to anchor the existence of a specific repository state outside the author's direct control.

## What this proves

The timestamp freeze proves a narrow claim:

this exact frozen content existed at or before the time certified by the external TSA.

It does not prove that the thesis is correct.

It does not prove that the author was the first person to formulate every idea contained in the repository.

It does not prove legal ownership by itself.

It does not prove priority over all possible unpublished work.

It proves temporal existence of a specific content state under an external timestamp authority.

## Why GitHub is not enough

GitHub is useful for publication, collaboration, releases, and public visibility.

However, GitHub alone should not be treated as a strong external timestamping authority.

A repository author can control commit metadata, create commits with custom dates, amend commits, force-push, or rewrite Git history.

That does not make GitHub useless.

It means GitHub publication and external timestamping serve different functions.

GitHub publishes the artifact.

The TSA anchors the artifact externally in time.

## Freeze principle

The freeze is based on four artifacts:

1. A fixed package containing the selected repository files.
2. A SHA-256 hash of that package.
3. An RFC 3161 timestamp request generated from the package.
4. An RFC 3161 timestamp response issued by an external TSA.

Together, these artifacts allow a third party to verify that the frozen package has not changed and that the timestamp response corresponds to the original timestamp request.

## Expected freeze files

A complete freeze should include files similar to:

```text
adap-freeze-2026-06-01.zip
adap-freeze-2026-06-01.sha256
adap-freeze-2026-06-01.tsq
adap-freeze-2026-06-01.tsr
TSA-VERIFY.md
```

Recommended folder:

```text
precedence/tsa-freeze-2026-06-01/
```

## Recommended folder structure

```text
precedence/
  tsa-freeze-2026-06-01/
    adap-freeze-2026-06-01.zip
    adap-freeze-2026-06-01.sha256
    adap-freeze-2026-06-01.tsq
    adap-freeze-2026-06-01.tsr
    TSA-VERIFY.md
```

## Step 1: Create the freeze package

Example command:

```bash
zip -r adap-freeze-2026-06-01.zip \
  README.md \
  architecture \
  challenge \
  examples \
  experiments \
  precedence \
  proofs \
  solver \
  90-DAY-GO-NO-GO.md \
  ADAP-EXP-003.md \
  CONTRIBUTING.md \
  LICENSE
```

Adjust the file list if the repository structure changes.

The important point is that the package must represent the exact repository state being frozen.

## Step 2: Generate the SHA-256 hash

```bash
sha256sum adap-freeze-2026-06-01.zip > adap-freeze-2026-06-01.sha256
```

The `.sha256` file records the digest of the frozen package.

Any later change to the package will produce a different SHA-256 hash.

## Step 3: Generate the RFC 3161 timestamp request

```bash
openssl ts -query \
  -data adap-freeze-2026-06-01.zip \
  -sha256 \
  -cert \
  -out adap-freeze-2026-06-01.tsq
```

This creates the timestamp query file.

The query commits to the package hash without requiring the TSA to receive or store the full repository content.

## Step 4: Submit the request to an external TSA

Example using FreeTSA:

```bash
curl -H "Content-Type: application/timestamp-query" \
  --data-binary @adap-freeze-2026-06-01.tsq \
  https://freetsa.org/tsr \
  -o adap-freeze-2026-06-01.tsr
```

The resulting `.tsr` file is the timestamp response.

This file should be stored together with the freeze artifacts.

## Step 5: Download TSA certificates

Example using FreeTSA:

```bash
wget https://freetsa.org/files/tsa.crt
wget https://freetsa.org/files/cacert.pem
```

These certificate files are used to verify that the timestamp response was issued by the TSA.

They do not need to be permanently stored in the repository, but storing verification instructions is recommended.

## Step 6: Verify the timestamp response

```bash
openssl ts -verify \
  -in adap-freeze-2026-06-01.tsr \
  -queryfile adap-freeze-2026-06-01.tsq \
  -CAfile cacert.pem \
  -untrusted tsa.crt
```

A successful verification confirms that the timestamp response matches the original timestamp request and was issued by the external TSA.

## Step 7: Verify the package hash

```bash
sha256sum -c adap-freeze-2026-06-01.sha256
```

A successful result confirms that the current package matches the recorded SHA-256 hash.

## Third-party verification logic

A third party should be able to verify the freeze by checking:

1. The package matches the SHA-256 hash.
2. The timestamp request corresponds to the package.
3. The timestamp response corresponds to the timestamp request.
4. The timestamp response was issued by the external TSA.
5. The certified time is external to the repository author.

If these checks pass, the third party can reasonably conclude that the exact frozen package existed no later than the timestamp certified in the RFC 3161 response.

## Interpretation of a successful verification

If both the hash verification and TSA verification pass, the result means:

1. The freeze package has not changed.
2. The timestamp request was generated from that package.
3. The timestamp response corresponds to that request.
4. The timestamp response was issued by the external TSA.
5. The frozen content existed at or before the certified timestamp.

## Interpretation of a failed verification

A failed verification may mean that:

1. The package was modified after the hash was generated.
2. The `.sha256` file does not correspond to the package.
3. The `.tsq` request does not correspond to the package.
4. The `.tsr` response does not correspond to the `.tsq` request.
5. The TSA certificate chain cannot be verified.
6. The wrong certificate files were used.
7. The files were renamed, corrupted, or replaced.

A failed verification does not automatically prove malicious activity.

It means the freeze cannot be validated under the stated verification procedure.

## Scope limitation

This timestamp does not prove that A-DAP is correct.

It does not prove that the repository is complete.

It does not prove that all claims are true.

It does not prove authorship by itself.

It does not prove legal priority over every unpublished source.

It proves a narrower and stronger claim:

this exact frozen content existed at or before the externally certified timestamp.

## Why this matters for A-DAP

A-DAP argues that auditability requires records that can survive challenge outside the system that produced them.

The same principle applies to this repository.

A Git commit is useful, but it remains inside a system substantially controlled by the author.

An external TSA creates a disjoint temporal anchor.

That separation matters.

GitHub publishes the repository.

SHA-256 fixes the content.

RFC 3161 anchors the content externally in time.

Together, they create a stronger precedence record than publication alone.

## Recommended release note

When publishing a release that includes these artifacts, the following wording may be used:

```text
This release contains an externally timestamped freeze of the current A-DAP thesis state.

GitHub provides public publication of the repository state.

The included SHA-256 digest fixes the content of the freeze package.

The included RFC 3161 timestamp response anchors the existence of that package through an external Time Stamping Authority.

This timestamp does not prove correctness, authorship, or legal ownership by itself.

It proves the narrower claim that this exact frozen content existed at or before the certified timestamp.
```

## Recommended commit message

```text
Add TSA verification guide for external timestamp freeze
```

## Recommended release title

```text
External Timestamp Freeze — 2026-06-01
```

## Recommended tag

```text
tsa-freeze-2026-06-01
```

## Final statement

This repository treats auditability as a structural property.

The timestamp freeze follows the same principle:

the record should not depend only on the system that produced it.

Publication is useful.

External anchoring is stronger.

The TSA freeze provides an independently verifiable temporal boundary for the frozen repository state.
