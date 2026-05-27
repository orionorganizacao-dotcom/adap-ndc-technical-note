# GCD-001 Reconstruction Specification

## Status

Candidate technical specification.  
Pending external disjoint reconstruction.

## Purpose

This document defines how an external verifier should reconstruct the GCD-001 decision-custody graph and compute or challenge the claimed NDC.

## Core Principle

Do not trust the author.  
Reconstruct the graph.  
Compute the cut.  
Challenge the NDC.  
Declare the oracle boundary.

## Definitions

- A: author / claimant
- V: verifier / reconstructing party
- Decision record
- Decision envelope
- Custody graph
- Vertex
- Edge
- Cut
- Minimum vertex-cut
- NDC
- Oracle-bound edge

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

## What Must Not Be Assumed

The verifier must not assume:

- the author's NDC is correct
- the author’s script is authoritative
- the expected output is proof
- oracle-bound claims are structurally verified
- record integrity equals decision truth

## NDC Calculation

NDC is computed as the minimum sufficient vertex-cut required to alter the decision-custody graph without detection by V.

## Failure Conditions

The reconstruction fails if:

- canonicalization is ambiguous
- artifacts are missing
- hashes do not match
- graph edges are undefined
- A/V roles are unclear
- oracle-bound claims are counted as verified
- the verifier cannot independently reproduce the NDC reasoning

## External Review Output

The reviewer should produce one of three outcomes:

1. NDC confirmed.
2. NDC falsified.
3. Reconstruction blocked by missing or ambiguous specification.

## Minimal Honest Claim

GCD-001 is not a proof of decision truth.

It is a specification for reconstructing decision-custody evidence and challenging the claimed NDC.
