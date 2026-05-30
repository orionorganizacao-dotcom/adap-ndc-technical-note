# GCD-003 Experiment Spec — Internal Integrity Sensor as NDC Collapse Test

## Objective

Test whether an internal integrity sensor increases NDC or collapses into the operator’s control domain.

This experiment models the sensor as a custody-graph node and tests whether it survives conservative dependency collapse under different topologies.

The purpose is not to prove that all sensors are useless.

The purpose is to identify when a sensor is an independent verification path and when it is merely another operator-controlled artifact.

---

## Core Hypothesis

An internal integrity sensor does not increase NDC merely because it monitors the system from inside.

A sensor increases NDC only when its material control dependencies are disjoint from the operator being verified.

The key dependencies are:

- observation boundary,
- input custody,
- sensor runtime custody,
- signing-key custody,
- anchoring path,
- receipt availability,
- public-key directory,
- and verification access.

---

## Entities

### O — Operator

The entity operating or controlling the automated decision system.

### E — Engine

The decision engine or runtime being monitored.

### S — Sensor

The internal integrity sensor.

### I — Input / Observed State

The state, data, event, or boundary observed by the sensor.

### K — Sensor Signing Key

The key used by the sensor to sign or authenticate its readings.

### R — Receipt

The receipt or record containing sensor output.

### A — External Anchor

Timestamp, ledger, or other external anchoring mechanism.

### PKD — Public Key Directory

The place where public keys, certificates, or verification metadata can be retrieved.

### P — Affected Party

The person or entity affected by the decision.

### V — Verifier

The party or tool attempting to verify the sensor output.

### Reg — Regulator or Independent Reviewer

An external party able to inspect or reconstruct evidence under defined assumptions.

---

## Scenario A — Operator-Controlled Internal Sensor

### Description

The operator controls:

- the engine,
- the sensor,
- the input,
- the receipt channel,
- and the verification access.

### Expected Result

The sensor collapses into the operator’s control domain.

The sensor may produce an additional artifact, but that artifact is not an independent verification path.

### Expected NDC Effect

Apparent NDC may look greater than 1.

Conservative NDC remains 1.

---

## Scenario B — Internal Sensor with Operator-Controlled Key

### Description

The sensor signs its readings.

However, the operator controls the signing key or can cause the key to be used.

### Expected Result

The signature does not create independence.

A signed output is not independent if the adversary controls the signing key.

### Expected NDC Effect

The sensor and key collapse into the operator’s control domain.

Conservative NDC remains 1.

---

## Scenario C — Protected Sensor with Operator-Controlled Input

### Description

The sensor runs in a TEE, HSM, or protected execution environment.

The sensor key is non-exportable.

However, the operator controls the input or observation boundary.

### Expected Result

The protected sensor may preserve integrity after observation.

But it does not prove that the observed input was true, complete, or unmanipulated before observation.

The operator may poison the input before the sensor signs it.

### Expected NDC Effect

For origin, input truth, or completeness:

- the system collapses through the operator-controlled input.

For post-observation tamper evidence:

- the sensor may support a narrow integrity claim.

The narrow claim must not be inflated into a broader truth claim.

---

## Scenario D1 — Disjoint Sensor with Affected-Party Receipt Possession

### Description

The sensor has:

- disjoint key custody,
- constrained or independently defined observation boundary,
- external anchoring,
- public key directory outside operator control,
- and receipt possession by the affected party.

### Expected Result

The sensor may survive as a materially independent verification path for the specific claim it measures.

### Expected NDC Effect

NDC may increase above 1, depending on the independence of the anchor, key, receipt, and verification path.

---

## Scenario D2 — Disjoint Sensor with Non-Exclusive Channel

### Description

The sensor has disjoint key custody and external anchoring.

However, receipt access occurs through a non-exclusive channel that may still be influenced by the operator.

### Expected Result

The result depends on whether the operator can suppress, delay, gate, or selectively disclose the sensor output.

A non-exclusive channel is not automatically equivalent to affected-party possession.

### Expected NDC Effect

The min-cut must be evaluated separately.

Do not report D2 as if it were D1.

---

## Required Analysis

For each scenario, reviewers should identify:

1. Apparent verification paths.
2. Operator-controlled dependencies.
3. Sensor runtime dependencies.
4. Input or observation-boundary dependencies.
5. Signing-key custody.
6. Receipt-channel custody.
7. Public-key directory custody.
8. External-anchor custody.
9. Verification-access dependencies.
10. Whether the sensor collapses into the operator.
11. Structural NDC after conservative collapse.
12. Whether the sensor creates independence or theater.

---

## Methodological Rule

Do not count the sensor as independent merely because it is a separate component.

Do not count a signature as independent if the operator controls the key.

Do not count protected execution as input truth if the operator controls the input.

Do not count receipt availability as independent if the operator can suppress access.

The correct question is:

Who materially controls the observation boundary, key custody, anchoring path, and verification access?

---

## Expected Output

A reviewer should produce:

- a collapsed custody graph,
- a short NDC analysis,
- a statement of which claim survives, if any,
- a distinction between input truth and post-observation integrity,
- and a conclusion on whether the internal sensor is independent or captured.
