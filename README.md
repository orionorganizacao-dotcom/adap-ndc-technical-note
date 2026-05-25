# A-DAP: Custody-Graph Verification and NDC

This repository contains an early technical note on A-DAP, a custody-graph verification model for opaque AI decision systems.

A-DAP does not claim to prove hidden AI causality. Instead, it binds observable decision artifacts before action, models their custody as a temporal graph, and defines the Custody Disjunction Number (NDC) as a conservative measure of the structural cost required to falsify observable decision records without detection.

## Current status

Working Draft: Technical Note v0.3.1

This draft is formal and architectural. It does not yet provide empirical validation across real deployments, nor does it yet provide an implemented min-cut solver for NDC computation.

## Core thesis

A-DAP does not prove why an AI system decided.

It proves what was observably committed before action, measures how many effective custody domains would need to collude, fail, or be compromised for a false observable history to remain acceptable to a declared verifier, and identifies the boundary where falsification ceases to be registral and becomes causally indistinguishable.

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

## Main claim

External timestamping, hashing, signatures, or Merkle anchoring alone do not raise NDC above 1 against an internal operator capable of constructing a coherent showcase state before anchoring.

NDC greater than 1 requires custody disjunction at the origin of generation, not merely posterior anchoring.

## What A-DAP does not claim

A-DAP does not prove:

- hidden internal causality;
- moral legitimacy;
- fairness;
- correctness;
- legal accountability by itself;
- the truth of declared reasons.

A-DAP provides a forensic substrate. Institutional accountability still requires an authority external to the generator.

## Current files

- `technical-note-v0.3.1.md` — main technical note
- `examples/gcd-001.md` — worked example, planned
- `references.md` — related work and references, planned

## Review request

This is a working draft.

The main question is not whether the model sounds plausible, but where it fails under external review:

- Where does the custody graph become ambiguous?
- Where does NDC overclaim?
- Where does the collapse relation become too conservative or too weak?
- Where does the GCD-001 example fail to compute a defensible cut?
- Which prior literature should be cited or distinguished?

## Author

Ezio v.s. Santos  
AI Governance & Verifiability
