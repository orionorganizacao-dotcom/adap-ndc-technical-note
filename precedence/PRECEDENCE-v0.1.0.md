# A-DAP v0.1.0 — Precedence Record

This file records the public precedence anchor for A-DAP v0.1.0.

It is intended to support attribution, timestamped existence, and integrity of the released research artifact.

It does not claim that A-DAP is correct, complete, robust, legally valid, production-ready, or commercially exclusive.

---

## 1. Version

```text
A-DAP v0.1.0 — Externalization Baseline
```

---

## 2. Repository

```text
https://github.com/orionorganizacao-dotcom/adap-ndc-technical-note
```

---

## 3. Author

```text
Ezio v.s. Santos
```

---

## 4. Release Tag

```text
v0.1.0
```

---

## 5. Release Meaning

A-DAP v0.1.0 is the first public externalization baseline.

It demonstrates the minimum affected-party contestability object:

```text
a citizen-held decision receipt emitted in a simulated decision flow.
```

It proves a narrower claim:

```text
a decision record can leave the generator’s exclusive control.
```

It does not yet prove:

```text
the record is hard to falsify.
```

Under conservative assumptions, A-DAP v0 should be treated as an externalization baseline, not as a hardened evidentiary architecture.

---

## 6. Scope Covered by This Precedence Record

This precedence record covers the repository state at tag:

```text
v0.1.0
```

including, when present in that tagged release:

```text
README.md
ROADMAP.md
THREAT_MODEL.md
CONTRIBUTING.md
NOTICE.md
RELEASE_NOTES.md
QUICKSTART.md
architecture/
examples/decision-receipt-poc/
solver/
challenge/
proofs/
```

The release may include conceptual notes, proof-of-concept scripts, adversarial stress tests, and documentation.

This record binds the released archive or repository snapshot to a specific hash once the SHA-256 value is inserted below.

---

## 7. Core Claim of the Precedence Record

This record claims only that this version of the A-DAP research architecture existed in this form at or before the timestamped release and any external records associated with the hash.

It does not claim priority over general cryptographic primitives, audit-trail mechanisms, transparency logs, timestamping, Merkle trees, signatures, or provenance infrastructure.

It does not claim exclusivity over the broad idea of verifiable records.

It records precedence for the specific A-DAP v0.1.0 formulation, including:

```text
affected-party contestability
decision receipts as minimum contestability objects
NDC as a capture diagnostic
scope-completeness boundary
independent verification as topology
A-DAP v0 as externalization baseline
v0 stress-test result under conservative assumptions
ROADMAP v0 → v1
```

---

## 8. SHA-256 of Release Archive

Insert the SHA-256 hash of the downloaded GitHub release archive here.

```text
<INSERT_SHA256_HASH_HERE>
```

Recommended archive filename:

```text
A-DAP-v0.1.0-externalization-baseline.zip
```

Recommended hash file:

```text
A-DAP-v0.1.0-SHA256.txt
```

---

## 9. Hash Statement

The SHA-256 hash binds a specific archive to a specific repository state.

Any later modification to that archive changes the hash.

This supports content integrity and timestamped existence.

It does not prove correctness, fairness, legality, production readiness, or commercial value.

---

## 10. Signature Record

If the hash file is signed, record the signature file here.

Recommended signature files:

```text
A-DAP-v0.1.0-SHA256.txt.asc
```

or:

```text
A-DAP-v0.1.0-SHA256.txt.minisig
```

Signature status:

```text
<INSERT_SIGNATURE_STATUS_HERE>
```

Example:

```text
Signed with GPG detached signature.
```

or:

```text
Signed with minisign detached signature.
```

or:

```text
Not yet signed.
```

---

## 11. External Timestamp Record

If an external timestamp is created, record it here.

Possible timestamp mechanisms include:

```text
GitHub release timestamp
RFC 3161 timestamp
Zenodo DOI
OSF registration
public archive
digital notary
institutional repository
other external timestamping service
```

Timestamp status:

```text
<INSERT_TIMESTAMP_STATUS_HERE>
```

Recommended RFC 3161 files:

```text
A-DAP-v0.1.0.tsq
A-DAP-v0.1.0.tsr
A-DAP-v0.1.0-timestamp-receipt.json
```

---

## 12. Precedence Meaning

This precedence record is intended to establish that:

```text
1. The A-DAP v0.1.0 repository state existed in the released form.
2. The archive hash identifies that exact released content.
3. The release was associated with the listed repository and author.
4. Any external timestamp or signature strengthens the evidentiary chain.
5. Later changes to the content can be detected by hash mismatch.
```

This is a content-integrity and timestamped-existence claim.

It is not a correctness claim.

---

## 13. What This Record Does Not Prove

This record does not prove:

```text
A-DAP is correct.
A-DAP is complete.
A-DAP is production-ready.
A-DAP is legally valid.
A-DAP is commercially valuable.
A-DAP has high NDC.
A-DAP prevents all falsification.
A-DAP proves fairness.
A-DAP proves truth.
A-DAP proves legality.
A-DAP proves scope completeness.
A-DAP proves verifier independence.
A-DAP guarantees realized detection.
A-DAP prevents total collusion.
A-DAP prevents input provenance failure.
A-DAP prevents operator-controlled scope capture.
```

---

## 14. v0 Boundary Statement

A-DAP v0.1.0 should be interpreted under the following boundary:

```text
A-DAP v0 externalizes the record.

It does not yet harden the record.
```

The current proof of concept demonstrates the minimum affected-party contestability object.

It does not yet demonstrate that falsification requires multiple materially distinct compromises.

Full hardening remains a v1 research and implementation target.

---

## 15. Conservative NDC Statement

Under conservative assumptions, the current A-DAP v0 proof of concept should be treated as:

```text
A-DAP v0 NDC = 1
```

This does not invalidate the project.

It defines the honest baseline.

Higher NDC values belong only to target topologies that require additional implementation and validation, including:

```text
external anchoring
control-disjoint verification topology
threshold custody
independent verifier distribution
scope validation
infrastructure separation
detection activation mechanisms
```

---

## 16. Relationship to A-DAP Itself

This precedence record applies A-DAP’s own philosophy to the A-DAP project.

The project should not rely on narrative alone.

It should preserve a stable, hash-bound, timestamped object that can later be compared against claims of authorship, alteration, or misrepresentation.

This record therefore supports the following principle:

```text
A-DAP does not need to be secret to have value.

It needs to be attributable, timestamped, and difficult to distort without detection.
```

---

## 17. Suggested Citation

```text
Santos, Ezio v.s. A-DAP v0.1.0 — Externalization Baseline.
Auditable Decision Accountability Protocol.
A contestability architecture for high-impact automated decisions.
Repository release: v0.1.0.
```

---

## 18. Suggested Verification Procedure

A verifier should:

```text
1. Download the release archive for tag v0.1.0.
2. Compute the SHA-256 hash of the archive.
3. Compare the computed hash against the hash recorded in this file.
4. Verify any detached signature if available.
5. Verify any external timestamp if available.
6. Compare the release contents against the stated scope.
7. Treat this record as evidence of content existence and integrity, not proof of correctness.
```

---

## 19. Recommended File Layout

Recommended repository layout for precedence artifacts:

```text
precedence/
├── PRECEDENCE-v0.1.0.md
├── A-DAP-v0.1.0-SHA256.txt
├── A-DAP-v0.1.0-SHA256.txt.asc
└── timestamp/
    ├── A-DAP-v0.1.0.tsq
    ├── A-DAP-v0.1.0.tsr
    └── A-DAP-v0.1.0-timestamp-receipt.json
```

If signatures or timestamps are not yet available, the minimum initial layout may be:

```text
precedence/
├── PRECEDENCE-v0.1.0.md
└── A-DAP-v0.1.0-SHA256.txt
```

---

## 20. Final Precedence Statement

This record anchors the public existence of A-DAP v0.1.0 as an externalization baseline.

It preserves a specific content state.

It supports attribution.

It supports later comparison.

It does not prove that the system is correct.

It does not prove that the system is robust.

It proves only the narrower and necessary first step:

```text
this version existed in this form, at or before the associated release, hash, signature, and timestamp records.
```
