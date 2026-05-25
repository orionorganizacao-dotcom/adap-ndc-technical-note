# A-DAP Technical Note v0.3.1

## Custody-Graph Verification and Detectability Boundaries in Opaque AI Decisions

Status: working draft  
Repository: adap-ndc-technical-note

## Core thesis

A-DAP is a proposed custody-graph verification model for opaque AI decision systems.

It does not claim to prove hidden AI causality.

Instead, it binds observable decision artifacts before action, models their custody as a temporal graph, and uses the Custody Disjunction Number (NDC) to estimate the structural cost of falsifying observable decision records without detection.

## Key correction from initial solver runs

Initial solver runs falsified the manual NDC≈3 estimate for GCD-001.

Tested configurations:

- envelope-reading verifier: NDC = 1
- partial cross-check verifier: NDC = 2
- full cross-check verifier: NDC = 2
- envelope/batch split: NDC = 2

The manual estimate of NDC≈3 was not reproduced under any tested configuration.

## Current finding

The important finding is not that GCD-001 reaches NDC=3.

The important finding is that the solver rejected the manual estimate and exposed recurring low-cost cuts that were not obvious from manual reasoning.

This strengthens the model because NDC becomes a computed result, not a desired number.

## Methodological correction

NDC must be computed on the full custody graph.

Conceptual surfaces such as scope, generation, envelope, and execution should be used for post-hoc interpretation of the cut, not for computing NDC separately.

The correct sequence is:

1. build the full temporal custody graph;
2. apply the conservative collapse relation;
3. activate edges under the declared adversary model A and verifier model V;
4. compute min-cut on the full quotient graph;
5. classify the resulting cut after computation.

## Envelope Bottleneck

If the verifier primarily relies on the envelope as the source of coherence, the envelope becomes a custody bottleneck.

In that case, compromising the envelope domain may be sufficient to produce an alternative observable history accepted by the verifier, keeping NDC low even when additional artifacts exist in the graph.

## Temporal Anchoring Insufficiency

External anchoring preserves what it receives.

It does not independently witness what caused the decision.

Therefore, timestamping, hashing, signatures, or Merkle anchoring alone do not raise NDC when the internal operator can assemble a coherent showcase state before anchoring.

## NDC definition

NDC is computed under a declared pair:

A = adversary model  
V = verifier model

NDC is not absolute.

Changing A or V changes the graph, active edges, and resulting cut.

## What A-DAP does not claim

A-DAP does not prove:

- hidden internal causality;
- moral legitimacy;
- fairness;
- correctness;
- legal accountability by itself;
- the truth of declared reasons.

A-DAP provides a forensic substrate.

Institutional accountability still requires an authority external to the generator.

## Open question

Whether GCD-001 can reach NDC=3 under a different justified graph structure remains open.

No such configuration has been verified yet.

## Current status

This note is formal and architectural.

It does not yet provide empirical validation across real deployments.

It does not yet provide a complete implemented min-cut solver in the repository.

The current repository documents the model, the initial GCD-001 example, architectural decisions, open issues, and solver-related corrections.
