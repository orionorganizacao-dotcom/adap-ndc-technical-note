# Initial Solver Test — GCD-001

## Purpose

This note documents the first solver-based test of the GCD-001 custody graph.

The goal was not to confirm the manual NDC estimate, but to test whether the manual reasoning survived formal min-cut computation.

## Background

The initial hand-worked analysis suggested that the strong GCD-001 deployment could reach approximately:

NDC ≈ 3

This estimate was based on manual cut enumeration, not on an implemented solver.

## Solver result

Initial solver runs did not reproduce the manual NDC≈3 estimate.

Tested configurations:

- envelope-reading verifier: NDC = 1
- partial cross-check verifier: NDC = 2
- full cross-check verifier: NDC = 2
- envelope/batch split: NDC = 2

The manual estimate of NDC≈3 was not reproduced under any tested configuration.

## Main finding

The solver exposed recurring low-cost cuts that were not obvious from manual reasoning.

In particular, execution evidence and the envelope/batch chain appeared as recurring low-cost cut surfaces in the current GCD-001 graph.

## Methodological correction

The result shows that NDC must be computed on the full custody graph.

Conceptual surfaces such as scope, generation, envelope, and execution are useful for interpreting a cut after computation, but they should not be used to compute NDC separately.

The correct order is:

1. build the full custody graph;
2. apply the conservative collapse relation;
3. activate edges under the declared adversary model A and verifier model V;
4. compute min-cut on the full quotient graph;
5. interpret the resulting cut.

## Why this matters

This test demonstrates the value of the solver.

The solver rejected a plausible manual estimate and revealed vulnerabilities that intuition had missed.

This is aligned with the purpose of A-DAP/NDC: to make assumptions explicit, testable, and falsifiable.

## Current status

Whether GCD-001 can reach NDC=3 under a different justified graph structure remains open.

No such configuration has been verified yet.
