# GCD-002 Experiment Spec — Funding as a Control Vector

## Objective

Test whether a third-party verifier increases NDC when material dependencies connect the verifier back to the operator.

This experiment models funding, access, scope, governance, and revocation as control vectors.

---

## Entities

### O — Operator

The entity that makes the automated decision.

### E — Decision Envelope

The committed decision record.

### R — Receipt Delivery Channel

The channel through which the affected party receives the decision receipt.

### A — External Anchor

Timestamp or anchoring mechanism used to establish that a commitment existed no later than a given time.

### V — Verifier

A third-party verifier that checks the decision receipt.

### F — Funding Source

The entity or mechanism funding the verifier.

### S — Scope Authority

The entity defining what the verifier is allowed to inspect.

### X — Access Provider

The entity providing data, API access, credentials, schemas, receipts, or proof material to the verifier.

### G — Governance / Appointment Authority

The entity that selects, appoints, certifies, or approves the verifier.

### Q — Revocation Authority

The entity that can terminate the verifier, revoke credentials, end the contract, or block access.

### P — Affected Party

The person affected by the automated decision.

### Reg — Regulator or Independent Reviewer

A party that may attempt independent reconstruction or oversight.

---

## Test Hypothesis

Adding a third-party verifier does not necessarily increase NDC.

If the verifier’s material dependencies point back to the operator, the verifier may collapse into the operator’s control domain.

---

## Scenarios

### Scenario 1 — Operator-Funded Verifier

The operator selects and pays the verifier.

The operator controls renewal.

The operator controls data access.

Expected result:

The verifier likely collapses into the operator’s control domain.

---

### Scenario 2 — Operator-Scoped Verifier

The verifier is funded independently, but the operator defines what can be inspected.

Expected result:

The verifier may remain separate on funding, but scope capture limits substantive independence.

NDC may improve for some checks while remaining weak for completeness.

---

### Scenario 3 — Independently Funded and Mandated Verifier

The verifier is funded by a regulator, court, public-interest fund, or independent levy.

The verifier can access receipts and anchors without operator permission.

The verifier’s findings can be reproduced by others.

Expected result:

The verifier is more likely to remain a genuinely independent verification path.

---

### Scenario 4 — Open Tool, Captured Exercise

The verifier tool is open-source and reproducible.

However, no independent actor is funded to run it at scale.

Expected result:

Structural reproducibility exists, but Effective NDC may remain low due to weak exercise.

---

## Required Analysis

For each scenario, reviewers should identify:

1. Apparent verification paths.
2. Material control dependencies.
3. Funding dependencies.
4. Access dependencies.
5. Scope dependencies.
6. Governance dependencies.
7. Revocation dependencies.
8. Whether V collapses into O.
9. Structural NDC after conservative collapse.
10. Effective NDC risks under ADAP-EXP-003.
11. Whether the scenario creates independence or theater.

---

## Methodological Rule

Do not count the verifier as independent merely because it is a separate organization.

Only count it as independent if its funding, access, scope, governance, and revocation conditions are materially disjoint from the operator being verified.

---

## Expected Output

A reviewer should produce:

- a collapsed dependency graph,
- an NDC estimate,
- a short explanation of any collapse,
- a statement of remaining trust dependencies,
- and a conclusion on whether third-party verification is substantive or theatrical.
