# GCD-003 Submission Template

## Reviewer

Name or handle:

Affiliation, if any:

Date:

---

## Scenario Reviewed

Select one:

- Scenario A — Operator-Controlled Internal Sensor
- Scenario B — Internal Sensor with Operator-Controlled Key
- Scenario C — Protected Sensor with Operator-Controlled Input
- Scenario D1 — Disjoint Sensor with Affected-Party Receipt Possession
- Scenario D2 — Disjoint Sensor with Non-Exclusive Channel
- Other / modified scenario

---

## Apparent Verification Paths

List the verification paths before dependency collapse:

1.
2.
3.

---

## Material Control Dependencies

### Operator-Controlled Dependencies

Which parts are controlled by the operator?

Answer:

---

### Sensor Runtime Dependencies

Who controls the sensor runtime, deployment, configuration, or update path?

Answer:

---

### Input / Observation Boundary Dependencies

Who controls what the sensor observes?

Can the operator poison, filter, omit, or shape the observed input before the sensor records it?

Answer:

---

### Signing-Key Custody

Who controls the sensor signing key?

Is the key non-exportable?

Can the operator cause the key to sign false, incomplete, or selective readings?

Answer:

---

### Receipt-Channel Custody

Who controls how the sensor receipt is stored, delivered, or retrieved?

Can the operator suppress, delay, gate, or selectively disclose receipts?

Answer:

---

### Public-Key Directory Custody

Who controls the public-key directory, certificate metadata, or verification metadata?

Answer:

---

### External-Anchor Custody

Who controls the timestamp, ledger, or external anchoring path?

Is the anchor reachable without relying on the operator?

Answer:

---

### Verification-Access Dependencies

Can a verifier reconstruct the sensor evidence without using an operator-controlled portal, API, or dashboard?

Answer:

---

## Collapse Analysis

Does the sensor collapse into the operator’s control domain?

Answer:

Reason:

---

## Structural NDC Estimate

Before collapse:

After conservative collapse:

Explanation:

---

## Surviving Claim

After dependency collapse, what claim survives?

Select or describe:

- No independent sensor claim survives.
- Narrow post-observation integrity claim.
- Receipt-availability claim.
- Independent sensor measurement claim.
- Other:

Explanation:

---

## Input Truth vs. Post-Observation Integrity

Does the sensor prove input truth, or only that a state was observed and signed?

Answer:

---

## Effective NDC / Exercise Risk

Does the sensor evidence appear likely to be exercised by affected parties, auditors, regulators, or independent reviewers?

What incentives or barriers affect exercise?

Answer:

---

## Conclusion

Is the internal sensor a materially independent verification path or another operator-controlled artifact?

Answer:

---

## Open Questions

List unresolved dependencies or uncertainties:

1.
2.
3.
