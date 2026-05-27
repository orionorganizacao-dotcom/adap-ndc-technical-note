# GCD-001 Oracle Boundary Note

## Status

Candidate architectural note.  
Pending external reconstruction review.

This note defines what GCD-001 can independently reconstruct and what remains oracle-bound by design.

Its purpose is to prevent overclaiming.

GCD-001 does not claim to make AI decisions fully trustless. It claims to make decision records independently reconstructible as records, while explicitly declaring which claims still depend on external oracles.

---

## Core Distinction

A-DAP does not prove that a decision was true.

It proves what was committed about the decision, when it was committed, by which cryptographic key, and whether that commitment was later altered.

A cryptographic record can prove integrity of bytes.

It cannot, by itself, prove that those bytes faithfully describe reality.

---

## Regime I — Closed-World Verification

Regime I contains artifacts that can be independently verified without reference to external-world truth.

Examples:

- canonical decision envelopes
- envelope hashes
- input hashes
- policy hashes
- signature verification
- hash-chain consistency
- ledger integrity
- deterministic digest reconstruction

A valid Regime I claim is:

These bytes match the committed artifact and have not changed after commitment.

Regime I verifies record integrity.

It does not verify decision truth.

---

## Regime II — Externally Anchored Verification

Regime II contains artifacts whose verification depends on external anchoring infrastructure.

Examples:

- RFC 3161 timestamp tokens
- timestamp authority certificate chains
- OpenTimestamps proofs
- public blockchain anchors
- externally published Merkle roots
- multiple independent time anchors

A valid Regime II claim is:

This commitment existed before or at a verifiable external time boundary.

Regime II strengthens temporal integrity.

It does not prove the truth of the committed content.

---

## Regime III — Oracle-Bound Claims

Regime III contains claims that cannot be independently reconstructed from cryptographic artifacts alone.

Examples:

- real-world truth of inputs
- identity of the real agent behind a key
- key custody and operational control
- correspondence between a public key and a specific model or agent
- actual model execution
- model state at inference time
- runtime environment integrity
- causal relation between input, model, policy, and output
- legal or institutional validity of a policy
- correctness, fairness, or legitimacy of the decision
- correspondence between the decision record and the external world

A valid Regime III declaration is:

This claim depends on an external oracle and is not independently reconstructible from the A-DAP record alone.

A Regime III declaration is not a reconstruction failure.

It is a boundary condition.

However, Regime III must not be used as a convenience category. If a claim can be migrated into Regime I or Regime II through commitment, anchoring, canonicalization, external custody, independent publication, or third-party attestation, it should not be hidden inside Regime III.

---

## Oracle Boundary Criterion

A claim belongs to Regime III only if at least one of the following conditions applies:

1. The claim depends on external-world facts not contained in the committed bytes.
2. The claim depends on identity, authority, intent, or institutional custody.
3. The claim depends on computational state that cannot be deterministically reconstructed by an external verifier.
4. The claim depends on internal causality not directly observable from the record.
5. The claim requires privileged access to the original execution environment.
6. The claim depends on legal, organizational, or human interpretation outside the cryptographic record.

If none of these conditions applies, the claim should be treated as a candidate for Regime I or Regime II reconstruction.

---

## The Trustless Core Is About Records

GCD-001 contains a real trustless core, but its scope is narrow.

The trustless core verifies:

- record integrity
- hash consistency
- signature validity
- commitment structure
- temporal anchoring, when externally anchored
- tamper evidence after commitment

The trustless core does not verify:

- truth of the input
- identity of the real-world actor
- actual model execution
- real model state
- causal explanation
- decision correctness
- legal legitimacy

Therefore, the accurate claim is:

A-DAP has a trustless core for decision records, not for decision truth.

---

## Reconstruction Failure vs. Oracle Boundary

A reconstruction failure occurs when a Regime I or Regime II artifact cannot be independently verified.

Examples:

- hash mismatch
- invalid signature
- broken hash chain
- invalid timestamp token
- canonicalization ambiguity
- missing committed artifact
- digest mismatch under the published specification

An oracle boundary occurs when the claim was never independently reconstructible from the record alone.

Examples:

- input truth
- agent identity
- real model execution
- model state
- causal explanation
- decision correctness

These must not be confused.

Failure to reconstruct a Regime I or II artifact is a protocol or implementation failure.

Failure to reconstruct a Regime III claim is expected, provided the boundary was explicitly declared.

Failure to declare a Regime III dependency is an overclaim.

---

## What External Reviewers Should Reconstruct

External reviewers should attempt to independently reconstruct:

- the canonical envelope
- the envelope hash
- input and policy hashes
- signature validity
- hash-chain consistency
- timestamp validity, if present
- Merkle root consistency, if present
- any published external anchor
- whether the declared Regime III boundaries are complete and justified

External reviewers should not be expected to reconstruct:

- whether the input was true
- whether the model actually executed
- whether the model state was real
- whether the agent identity was institutionally valid
- whether the decision was correct
- whether the explanation reflects true internal causality

Those are oracle-bound claims unless separately supported by external evidence.

---

## Minimal Honest Claim

A-DAP makes decision records independently reconstructible as records.

It does not make the full decision process trustless.

It separates what can be cryptographically verified from what remains dependent on external oracles.

---

## Canonical Statement

A-DAP does not eliminate trust.

It localizes and names trust.

It prices what is structurally verifiable.

It declares what remains oracle-bound.

GCD-001 is therefore not a proof of decision truth.

It is a reconstruction protocol for decision records with explicit oracle-boundary disclosure.
