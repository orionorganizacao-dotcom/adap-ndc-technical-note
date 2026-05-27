# GCD-001 Reconstruction Specification

## Status

Candidate technical specification.

Pending external disjoint reconstruction.

## Purpose

This document defines how an external verifier should reconstruct the GCD-001 decision-custody graph and compute or challenge the claimed Network Dependency Coefficient (NDC).

The goal is not to trust the author.

The goal is to reconstruct the graph, compute the cut, identify oracle boundaries, and determine whether the published NDC claim is reproducible, falsifiable, or underspecified.

## Core Principle

Do not trust the author.  
Reconstruct the graph.  
Compute the cut.  
Challenge the NDC claim.  
Declare the oracle boundary.

## Definitions

- **A**: author / claimant
- **V**: verifier / reconstructing party
- **Decision record**: the recorded decision object under analysis
- **Decision envelope**: the structured pre-action or action-bound record containing decision-relevant artifacts
- **Custody graph**: the graph representing dependency, control, evidence, and alteration paths
- **Vertex**: a node in the custody graph
- **Edge**: a dependency or control relationship between vertices
- **Cut**: a set of vertices whose alteration changes the relevant decision-custody graph condition
- **Minimum vertex-cut**: the smallest sufficient set of vertices required to alter the graph without detection by V
- **NDC**: Network Dependency Coefficient, computed from the minimum sufficient vertex-cut
- **Oracle-bound edge**: an edge whose truth depends on an external source not independently reconstructible from the published artifacts

## Reconstruction Inputs

The verifier receives:

- decision envelope
- raw artifacts
- canonicalization specification
- hash rules
- signature rules
- timestamp evidence, if present
- graph declaration
- oracle-boundary declaration
- tamper-test cases
- claimed NDC value

The verifier must treat these materials as reconstruction inputs, not as proof.

## Independent Implementation Requirement

The verifier must not rely on the author’s solver, scripts, expected outputs, private infrastructure, or manually asserted conclusions for the primary reconstruction.

The author’s tools may be used only for secondary comparison after the verifier has independently reconstructed the graph and computed the relevant cut.

A valid reconstruction must be executable, inspectable, or reproducible without privileged access to the author.

## What Must Be Reconstructed

The verifier must reconstruct:

- canonical envelope
- hashes
- graph vertices
- graph edges
- declared A/V pair
- candidate attack paths
- minimum vertex-cut
- NDC estimate
- oracle-boundary classification
- failure points, if any

## What Must Not Be Assumed

The verifier must not assume:

- the author's NDC is correct
- the author's script is authoritative
- the expected output is proof
- oracle-bound claims are structurally verified
- record integrity equals decision truth
- hash integrity equals semantic correctness
- timestamp presence equals independent reconstruction
- reconstruction success validates A-DAP as a whole

## NDC Calculation

NDC is computed as the minimum sufficient vertex-cut required to alter the decision-custody graph without detection by V.

The verifier must explicitly state:

- the graph model used
- the source and target conditions
- which vertices are included in the cut
- why the cut is sufficient
- why a smaller cut is not sufficient
- which claims are reconstructible
- which claims remain oracle-bound

## Oracle Boundary

The verifier must identify every claim that cannot be independently reconstructed from the published artifacts.

Oracle-bound claims may be recorded, declared, or externally referenced, but they must not be counted as structurally verified unless the verifier can independently reconstruct them.

Examples of oracle-bound claims may include:

- external timestamps without verifiable token inspection
- third-party attestations not independently checked
- dataset provenance not reconstructible from artifacts
- claims dependent on private systems
- claims dependent on legal, institutional, or administrative authority

## Failure Conditions

The reconstruction fails if:

- canonicalization is ambiguous
- artifacts are missing
- hashes do not match
- graph vertices are undefined
- graph edges are undefined
- A/V roles are unclear
- oracle-bound claims are counted as verified
- the verifier cannot independently reproduce the NDC reasoning
- the claimed NDC depends on author-controlled tools
- the specification permits more than one materially different reconstruction

Failure is not automatically negative.

A failed reconstruction may indicate that the published specification is incomplete, ambiguous, or dependent on unstated assumptions.

## External Review Output

The reviewer should produce one of three outcomes:

### R1 — Reproduction

The claimed NDC is independently reproduced under the published specification.

This does not mean that the original decision was true, fair, lawful, or correct.

It means only that the specific GCD-001 reconstruction claim was independently reproduced under the published specification.

### R2 — Falsification

The claimed NDC is shown to be incorrect.

A valid falsification must provide a constructive demonstration, such as:

- a smaller valid cut
- an invalid edge assumption
- an invalid vertex classification
- an oracle-bound claim incorrectly counted as verified
- a graph reconstruction that contradicts the claimed NDC

### R3 — Structural Ambiguity

The specification is incomplete or ambiguous enough to prevent deterministic reconstruction.

A valid ambiguity finding must identify the missing or unstable part of the specification and show how it affects the reconstructed graph, cut, or NDC estimate.

## Required Reviewer Deliverables

A valid external submission must include:

- reconstruction code in any programming language
- min-cut calculation memo
- reconstructed graph or graph representation
- oracle-boundary analysis
- technical note of 2–5 pages
- clear declaration of R1, R2, or R3
- instructions sufficient for independent inspection or reproduction

The reconstruction code must not use the author’s solver as the primary computation path.

## Out of Scope

This specification does not prove:

- that the original decision was correct
- that the dataset was morally or legally appropriate
- that the author’s interpretation is authoritative
- that oracle-bound claims are independently verified
- that record integrity equals decision truth
- that A-DAP as a whole is validated
- that NDC alone is a complete measure of governance, accountability, or safety

## Minimal Honest Claim

GCD-001 is not a proof of decision truth.

It is a test of whether a published decision-custody claim can be independently reconstructed, challenged, or shown to be underspecified.

A successful R1 result means the NDC claim was reproduced under the published specification.

A successful R2 result means the NDC claim was falsified.

A successful R3 result means the specification requires correction before the claim can be deterministically evaluated.

## Challenge Interpretation

The strongest result for A-DAP is not automatic confirmation.

The strongest result is a reconstruction process where confirmation, falsification, and ambiguity are all admissible outcomes, and where the author does not control the acceptance decision.

The purpose of GCD-001 is to expose the claim to independent reconstruction pressure.

If the claim survives, it gains evidentiary weight.

If the claim fails, the protocol improves.

If the specification is ambiguous, the specification becomes more precise.

All three outcomes are structurally useful.
