# GCD-003 Reviewer Guidelines

## Purpose

GCD-003 tests whether an internal integrity sensor remains independent after conservative dependency collapse.

Reviewers should not assume that a sensor increases NDC merely because it is a separate component inside the system.

Internal measurement is not independent verification by default.

---

## Review Rule

A sensor should be counted as independent only if its material control dependencies are disjoint from the operator being verified.

Material control dependencies include:

- sensor runtime,
- input custody,
- observation boundary,
- signing-key custody,
- receipt channel,
- public-key directory,
- anchoring path,
- verification access,
- and receipt possession.

If these dependencies lead back to the operator, the sensor may collapse into the operator’s control domain.

---

## What to Avoid

Do not say:

“Sensor exists, therefore NDC increased.”

Do not say:

“Sensor signs output, therefore it is independent.”

Do not say:

“TEE or HSM exists, therefore input truth is proven.”

Do not say:

“Internal monitoring is independent verification.”

Do not say:

“Non-exclusive access is the same as affected-party possession.”

Do not say:

“Digital immune system” or “self-healing trust layer” as if those metaphors prove independence.

---

## What to Look For

Look for hidden control edges:

- Who controls the sensor?
- Who controls the input?
- Who defines what the sensor observes?
- Who controls the signing key?
- Who controls the receipt channel?
- Who can suppress or delay receipts?
- Who controls the public-key directory?
- Who controls the external anchor?
- Can verification happen outside the operator’s portal?
- Does the affected party possess the receipt?
- Can the operator poison the input before observation?

---

## Distinguish the Claim Being Made

Reviewers must identify which claim survives after dependency collapse.

Possible surviving claims include:

### No Independent Sensor Claim

The sensor collapses fully into the operator’s control domain.

### Narrow Post-Observation Integrity Claim

The sensor may show that a state was signed after observation, but not that the state was true before observation.

### Receipt-Availability Claim

The sensor evidence may be available only if receipt access survives operator suppression.

### Independent Sensor Measurement Claim

The sensor may survive as an independent path only if observation boundary, key custody, anchoring path, receipt possession, and verification access are materially disjoint.

---

## Scoring Guidance

This challenge does not require a numeric score.

But reviewers may classify each topology as:

### Full Collapse

Sensor, key, input, receipt, or verification access are operator-controlled.

### Narrow Survival

Sensor supports only a limited post-observation integrity claim.

### Conditional Survival

Sensor may survive depending on receipt-channel access or verification availability.

### Material Independence

Sensor survives because its observation boundary, key custody, anchor, public-key directory, receipt possession, and verification access are disjoint from the operator.

---

## Required Distinction

Always distinguish:

```text
input truth
