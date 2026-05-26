# A-DAP: Custody-Graph Verification and NDC

This repository contains an early technical note on A-DAP, a custody-graph verification model for opaque AI decision systems.

A-DAP does not claim to prove hidden AI causality. Instead, it binds observable decision artifacts before action, models their custody as a temporal graph, and defines the Custody Disjunction Number (NDC) as a conservative measure of the structural cost required to falsify observable decision records without detection.

## Current status

Working Draft: Technical Note v0.3.1

This draft is formal and architectural. It does not yet provide empirical validation across real deployments, nor does it yet provide an implemented min-cut solver for NDC computation.

## Core thesis

A-DAP does not prove why an AI system decided.

It proves what was observably committed before action, measures how many effective custody domains would need to collude, fail, or be compromised for a false observable history to remain acceptable to a declared verifier, and identifies the boundary where falsification ceases to be merely registral and becomes causally indistinguishable.

## Key concepts

- Pre-action decision envelope
- Temporal custody graph
- Conservative custody-domain collapse
- Custody Disjunction Number (NDC)
- Scope commitment
- Generation evidence
- Execution evidence
- Temporal Anchoring Insufficiency
- Observationally complete causal showcase
- Envelope Bottleneck
- Public technical custody layer

## Main claim

External timestamping, hashing, signatures, or Merkle anchoring alone do not raise NDC above 1 against an internal operator capable of constructing a coherent showcase state before anchoring.

NDC greater than 1 requires custody disjunction at the origin of generation, not merely posterior anchoring.

In other words, a system does not become structurally verifiable only because its outputs are timestamped after creation. Structural verifiability requires that the creation, commitment, custody, and verification layers are separated in a way that makes retroactive falsification require compromise across disjoint domains.

## What A-DAP does not claim

A-DAP does not prove:

- hidden internal causality;
- moral legitimacy;
- fairness;
- correctness;
- legal accountability by itself;
- the truth of declared reasons.

A-DAP provides a forensic substrate. Institutional accountability still requires an authority external to the generator.

## Envelope Bottleneck

A-DAP primarily proves non-retroactive alteration after commitment and anchoring.

It does not, by itself, prove that the initial envelope faithfully represented everything that occurred at decision time. If the initial record is false, incomplete, or manipulated at write-time, A-DAP may preserve that record with integrity, but it does not transform original falsity into truth.

This is the Envelope Bottleneck.

The purpose of A-DAP is therefore not to eliminate trust entirely, but to relocate and distribute trust across public, auditable, and independently verifiable layers.

## Legal trust vs structural verifiability

A-DAP should not be confused with a legal notarial system.

A digital notary proves through legal public faith. A-DAP verifies through distributed architecture.

The former concentrates trust in a legally sanctioned authority. The latter distributes trust across public and auditable technical assumptions.

A-DAP does not replace courts, regulators, notaries, or institutional authorities. It provides a pre-forensic verification layer that allows an independent auditor to reconstruct technical evidence before that evidence is brought into an institutional forum.

The distinction is:

- legal notarial systems answer the legal question of admissibility, authority, and formal recognition;
- A-DAP answers the adversarial technical question of whether an observable decision record could have been retroactively altered without crossing disjoint custody domains.

These are complementary layers, not competing systems.

## Public Technical Custody Layer

This repository is not a legal notary.

It provides a public technical custody layer for A-DAP artifacts through:

- public versioning;
- SHA-256 release manifests;
- signed commit verification instructions;
- timestamp claim documentation;
- planned RFC 3161 / ICP-Brasil anchoring;
- planned OpenTimestamps anchoring;
- future independent reconstruction through solver-based verification.

The purpose is not to eliminate trust, but to relocate and distribute trust across public, auditable, and independently verifiable layers.

## Proof artifacts

The `proofs/` directory contains the initial structure for public custody and external verification artifacts.

Current proof structure:

- `proofs/public-key.asc` — public key placeholder for commit and artifact verification
- `proofs/release-v0.3.1.sha256` — SHA-256 release manifest placeholder
- `proofs/signed-commit-instructions.md` — instructions for offline commit signature verification
- `proofs/timestamp-claim.md` — timestamping status and planned anchoring layer
- `proofs/ots-proof/` — planned OpenTimestamps proof directory
- `proofs/rfc3161-proof/` — planned RFC 3161 / ICP-Brasil timestamp proof directory

These files do not yet constitute completed external proof. They define the proof surface and declare the intended verification layers.

## Verification model

A-DAP distinguishes between platform-visible trust and independently reconstructible proof.

For example, GitHub's "Verified" badge is a convenience layer. The independently verifiable evidence is the cryptographic signature attached to the commit, which can be checked outside GitHub using the relevant public key.

A future auditor should be able to verify:

```bash
git verify-commit <commit_hash>
