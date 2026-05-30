# GCD-003 — Internal Integrity Sensor Challenge

## Status

Experimental challenge.

This challenge tests whether an internal integrity sensor increases NDC or collapses into the operator’s control domain under conservative dependency analysis.

The purpose is not to prove that all sensors are useless.

The purpose is narrower:

To test when an integrity sensor is merely another output of the same operator-controlled system, and when it may survive as a materially independent verification path.

---

## Core Question

Does an internal integrity sensor increase independent contestability?

Or does it collapse into the operator’s control domain when the operator controls the engine, input, observation boundary, key custody, receipt channel, or verification access?

---

## Background

A-DAP distinguishes between:

- evidence and explanation,
- structural NDC and exercised verification,
- external reconstruction and operator-controlled reporting,
- local execution and independent verification,
- third-party status and material independence.

GCD-003 adds another layer:

A sensor is not independent merely because it is embedded in the pipeline.

A sensor is independent only if its key custody, observation boundary, anchoring path, and verification access are materially disjoint from the operator being verified.

If the operator controls what the sensor observes, the sensor may faithfully sign a distorted input.

If the operator controls the sensor key, the sensor’s signature may be self-attestation.

If the operator controls the only receipt channel, the sensor’s output may be suppressible.

If the operator controls verification access, the sensor’s evidence may not be externally reconstructible.

---

## Central Finding

The default internal sensor topology collapses.

An internal integrity sensor controlled by the same operator does not add an independent verification path.

It adds another artifact inside the same control domain.

The formal warning is:

Internal measurement is not independent verification.

---

## Topology A — Operator-Controlled Internal Sensor

Scenario:

- operator controls the engine;
- operator controls the internal sensor;
- operator controls the receipt;
- verifier receives sensor output through operator-controlled channels.

Expected result:

The sensor collapses into the operator’s control domain.

Apparent NDC may increase.

Conservative NDC remains 1.

---

## Topology B — Internal Sensor with Operator-Controlled Key

Scenario:

- sensor signs its readings;
- signing key is controlled by the operator;
- verifier checks the signature.

Expected result:

The signature does not create independence.

If the operator controls the key, the signed sensor output is self-attestation.

Conservative NDC remains 1.

---

## Topology C — TEE/HSM Sensor with Operator-Controlled Input

Scenario:

- sensor runs in a TEE, HSM, or protected environment;
- sensor key is non-exportable;
- operator controls the input or observation boundary;
- sensor signs what it observes.

Expected result:

The sensor may help show that a specific observed state was signed at a certain point.

But it does not prove that the observed state was true, complete, or unmanipulated before observation.

For origin, input truth, or completeness, the system collapses at the operator-controlled input.

The sensor survives only for a narrow post-observation integrity claim.

That claim is weaker than the claim that usually matters.

---

## Topology D1 — Sensor with Affected-Party Receipt Possession

Scenario:

- sensor key custody is disjoint from the operator;
- observation boundary is independently defined or constrained;
- timestamp or anchor is reachable outside the operator;
- public key directory is outside operator control;
- affected party receives and retains the receipt independently.

Expected result:

The sensor may survive as an independent verification path for the specific claim it measures.

This is stronger than a sensor whose output is only available through the operator.

---

## Topology D2 — Sensor with Non-Exclusive Channel

Scenario:

- sensor key custody is disjoint from the operator;
- observation boundary is independently defined or constrained;
- timestamp or anchor is reachable outside the operator;
- receipt is available through a non-exclusive channel;
- operator still participates in or can influence the channel.

Expected result:

The result depends on whether the operator can selectively suppress, delay, alter, or gate access to sensor evidence.

A non-exclusive channel is not automatically equivalent to affected-party possession.

The min-cut must be evaluated separately.

Do not report D2 as if it were D1.

---

## Methodological Rule

Do not count an internal sensor as independent merely because it produces a separate artifact.

Do not count a signed sensor output as independent if the operator controls the signing key.

Do not count a protected sensor as independent for input truth if the operator controls the input.

Do not count a receipt channel as independent if the operator can suppress or gate access.

The correct question is:

Who controls the sensor’s observation boundary, key custody, anchoring path, and verification access?

---

## Relation to the Envelope Bottleneck

GCD-003 is a direct application of the Envelope Bottleneck.

If every verification path passes through an operator-controlled sensor, key, receipt channel, or observation boundary, the apparent independence collapses.

The sensor becomes another envelope controlled by the same authority.

---

## Relation to Poisoned Oracle Risk

A protected sensor can faithfully sign a poisoned input.

If the operator controls what the sensor sees, the sensor may produce a cryptographically valid record of a distorted reality.

This is not a sensor failure.

It is a scope and observation-boundary failure.

A-DAP does not prove that the observed state was true.

It can only help reconstruct what was committed, by whom, when, and under what custody assumptions.

---

## Rejected Metaphor

GCD-003 rejects the metaphor that an internal sensor creates a “digital immune system,” “self-healing system,” or “proprioceptive trust layer” by itself.

Those metaphors are seductive but unsafe.

If the sensor is controlled by the same operator, the system is validating itself.

That is NDC = 1 by construction.

The framework tested this intuition and rejected it.

This failure should remain visible.

---

## Safe Claim

A safe claim is:

“An integrity sensor may add an independent verification path only when its observation boundary, key custody, anchoring path, and verification access are materially disjoint from the operator being verified.”

---

## Unsafe Claim

An unsafe claim is:

“An internal sensor increases NDC because it monitors the system from inside.”

This is false.

Internal monitoring is not independence.

---

## Relation to A-DAP

GCD-003 extends A-DAP’s dependency-collapse method to internal integrity sensors.

It asks whether the sensor is truly an independent constraint or merely another operator-controlled artifact.

The challenge is adversarial by design:

If the sensor collapses, the result should say so.

Reducing a false independence claim is progress.
