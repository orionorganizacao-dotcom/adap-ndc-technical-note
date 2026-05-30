# GCD-003 Expected Findings

## Expected Finding 1

An internal sensor is not independent merely because it is a separate component.

If the operator controls the sensor, the sensor collapses into the operator’s control domain.

---

## Expected Finding 2

A sensor-generated artifact is not an independent verification path by default.

If the artifact is produced, stored, delivered, or verified through operator-controlled infrastructure, it may be another envelope bottleneck.

---

## Expected Finding 3

A signature does not create independence if the operator controls the signing key.

A signed sensor output may still be self-attestation when the adversary controls the key or can cause the key to be used.

---

## Expected Finding 4

TEE, HSM, or protected execution does not prove input truth.

A protected sensor may faithfully sign a state that was already distorted before observation.

This creates a valid record of an observed state, not proof that the state was true, complete, or unmanipulated before observation.

---

## Expected Finding 5

The observation boundary is part of the custody graph.

If the operator controls what the sensor can observe, then the sensor’s independence is limited by that boundary.

NDC for the decision cannot exceed NDC for the sensor’s observation scope.

---

## Expected Finding 6

Receipt possession matters.

A receipt held by the affected party is materially different from a receipt available only through an operator-controlled or operator-influenced channel.

Do not collapse affected-party possession and non-exclusive access into the same case.

---

## Expected Finding 7

A non-exclusive channel is not automatically independent.

If the operator can suppress, delay, gate, filter, or selectively disclose sensor evidence, the receipt path may still collapse.

---

## Expected Finding 8

The strongest sensor topology requires disjoint control over multiple elements:

- observation boundary,
- sensor runtime,
- signing-key custody,
- public-key directory,
- anchoring path,
- receipt possession,
- and verification access.

If these are not materially disjoint, the sensor may not increase NDC.

---

## Expected Finding 9

The sensor may survive only for a narrow claim.

For example:

“This observed state was signed and anchored after observation.”

That is not the same as:

“The observed state was true.”

“The input was complete.”

“The decision was correct.”

“The system was independently verified.”

---

## Expected Finding 10

Internal measurement is not independent verification.

GCD-003 should reject metaphors that imply self-validation, such as:

- digital immune system,
- self-healing trust layer,
- proprioceptive verification,
- internal proof of integrity.

These metaphors may be useful for design discussion, but they are unsafe as proof claims if the same operator controls the sensor path.

---

## Expected Finding 11

The default internal sensor topology collapses.

In the ordinary case where the operator controls the engine, input, sensor, key, receipt channel, and verification access, conservative NDC remains 1.

---

## Expected Finding 12

GCD-003 should not produce a binary result.

It should identify which claim survives after dependency collapse:

- no independent claim,
- narrow post-observation integrity claim,
- receipt-availability claim,
- or materially independent sensor claim.

The result must specify the surviving claim, not merely report that the sensor “works.”
