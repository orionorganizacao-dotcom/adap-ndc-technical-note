# SDK vs External Audit Service

## Decision

A-DAP should be implemented as a hybrid architecture:

- internal SDK for instrumentation;
- external independent service for anchoring, verification, custody analysis, and audit.

## Rationale

A-DAP evidence must be captured at the point of decision generation. This requires an internal component close to the system runtime.

However, if all evidence generation, signing, storage, and verification remain inside the same operational domain, A-DAP collapses into advanced logging. The system being audited would still control the production and interpretation of its own proof.

Therefore, the SDK should collect and structure evidence, but it should not be the final authority over that evidence.

## Internal SDK responsibilities

The SDK should handle:

- pre-action decision envelope creation;
- input and output hashing;
- model/version metadata capture;
- runtime metadata capture;
- policy reference capture;
- tool-call trace capture when applicable;
- local signing or commitment generation;
- batching and Merkle aggregation;
- integration with the application runtime.

## External audit service responsibilities

The external service should handle:

- independent timestamping;
- external anchoring;
- integrity verification;
- custody-graph analysis;
- NDC calculation;
- scope coverage checks;
- gap detection;
- execution evidence verification;
- audit reports;
- third-party review.

## Core principle

The SDK instruments the decision.

The external service validates the custody of the evidence.

A-DAP should not rely on the audited system as the sole witness of its own decision history.

## NDC implication

If SDK, runtime, envelope creation, signing, storage, and verification remain under the same operator, the effective NDC will likely collapse to 1.

NDC greater than 1 requires custody disjunction between generation, envelope creation, anchoring, and verification.

## Summary

A-DAP should be delivered as:

1. SDK for capture;
2. external service for verification;
3. independent custody layer for auditability.

In short:

SDK for instrumentation.  
External service for trust.
