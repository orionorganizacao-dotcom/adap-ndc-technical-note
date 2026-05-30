# GCD-002 — Verifier Funding Capture Challenge

## Status

Experimental challenge.

This challenge tests whether adding a third-party verifier increases NDC when the verifier’s funding, access, scope, renewal, or survival depends on the operator being verified.

The purpose is not to prove that all funded verification is captured.

The purpose is narrower:

To test whether formal third-party verification can collapse under conservative dependency analysis when material control vectors lead back to the operator.

---

## Core Question

Does adding a third-party verifier increase independent contestability?

Or does the verifier collapse into the operator’s control domain when funding, access, scope, renewal, or revocation depend materially on the operator?

---

## Background

A-DAP distinguishes between:

- structural verifiability,
- exercised verification,
- adoption capture,
- validator authority,
- client-side execution,
- and independent verification.

GCD-002 adds another layer:

A verifier is not independent merely because it is a third party.

A verifier may be legally separate but materially dependent.

Funding can be a control vector.

Access can be a control vector.

Scope can be a control vector.

Revocation can be a control vector.

If these vectors lead back to the operator, conservative NDC analysis may collapse the verifier into the same control domain.

---

## Files

This challenge contains:

- `experiment-spec.md` — the challenge specification.
- `custody-graph.json` — a minimal graph describing the control relationships.
- `expected-findings.md` — expected adversarial findings.
- `submission-template.md` — template for external reviewers.
- `reviewer-guidelines.md` — instructions for reviewers.

---

## Safe Claim

GCD-002 does not prove that third-party verification is useless.

It tests whether a claimed independent verifier remains independent after funding, access, scope, governance, and revocation dependencies are included in the custody graph.

---

## Unsafe Claim

“Third-party verification increases NDC by default.”

This is false.

Third-party status must be analyzed through material control dependencies.

---

## Relation to A-DAP

GCD-002 extends A-DAP’s dependency-collapse method to the verification ecosystem.

It asks whether the verifier itself becomes part of the same control domain as the operator.

The challenge is adversarial by design:

If the verifier collapses, the result should say so.

Reducing a false independence claim is progress.# GCD-002 Experiment Spec — Funding as a Control Vector

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
- and a conclusion on whether third-party verification is substantive or theatrical.{
  "challenge": "GCD-002",
  "title": "Verifier Funding Capture Challenge",
  "version": "0.1",
  "nodes": {
    "O": {
      "label": "Operator",
      "description": "Entity making the automated decision."
    },
    "E": {
      "label": "Decision Envelope",
      "description": "Committed decision object."
    },
    "R": {
      "label": "Receipt Delivery Channel",
      "description": "Channel used to deliver the receipt to the affected party."
    },
    "A": {
      "label": "External Anchor",
      "description": "Timestamp or external anchoring mechanism."
    },
    "V": {
      "label": "Verifier",
      "description": "Third-party verifier."
    },
    "F": {
      "label": "Funding Source",
      "description": "Entity or mechanism funding the verifier."
    },
    "S": {
      "label": "Scope Authority",
      "description": "Entity defining what the verifier can inspect."
    },
    "X": {
      "label": "Access Provider",
      "description": "Entity providing access to receipts, APIs, schemas, or proof material."
    },
    "G": {
      "label": "Governance Authority",
      "description": "Entity appointing, certifying, or approving the verifier."
    },
    "Q": {
      "label": "Revocation Authority",
      "description": "Entity able to terminate, revoke, or block the verifier."
    },
    "P": {
      "label": "Affected Party",
      "description": "Person affected by the automated decision."
    },
    "Reg": {
      "label": "Regulator or Independent Reviewer",
      "description": "External party capable of independent review."
    }
  },
  "scenarios": {
    "scenario_1_operator_funded": {
      "description": "Verifier is selected, funded, scoped, and renewed by the operator.",
      "edges": [
        ["O", "E", "creates"],
        ["O", "R", "controls"],
        ["O", "F", "controls"],
        ["F", "V", "funds"],
        ["O", "S", "controls"],
        ["S", "V", "defines_scope"],
        ["O", "X", "controls"],
        ["X", "V", "provides_access"],
        ["O", "G", "controls"],
        ["G", "V", "appoints"],
        ["O", "Q", "controls"],
        ["Q", "V", "can_revoke"],
        ["V", "E", "verifies"],
        ["P", "R", "receives_receipt_through"]
      ],
      "expected_conservative_result": {
        "verifier_collapses_into_operator": true,
        "reason": "Funding, access, scope, governance, and revocation depend materially on the operator.",
        "ndc_effect": "Apparent third-party path likely collapses to operator domain."
      }
    },
    "scenario_2_independent_funding_operator_scope": {
      "description": "Verifier is independently funded but scope and access are controlled by the operator.",
      "edges": [
        ["O", "E", "creates"],
        ["O", "R", "controls"],
        ["Reg", "F", "controls"],
        ["F", "V", "funds"],
        ["O", "S", "controls"],
        ["S", "V", "defines_scope"],
        ["O", "X", "controls"],
        ["X", "V", "provides_access"],
        ["V", "E", "verifies"],
        ["P", "R", "receives_receipt_through"]
      ],
      "expected_conservative_result": {
        "verifier_collapses_into_operator": "partial",
        "reason": "Funding is independent, but scope and access remain operator-controlled.",
        "ndc_effect": "Some independence may exist, but substantive verification is limited by scope/access capture."
      }
    },
    "scenario_3_independent_mandate": {
      "description": "Verifier is independently funded, independently scoped, and has non-operator access to proof material.",
      "edges": [
        ["O", "E", "creates"],
        ["O", "R", "controls"],
        ["Reg", "F", "controls"],
        ["F", "V", "funds"],
        ["Reg", "S", "defines"],
        ["S", "V", "defines_scope"],
        ["Reg", "X", "controls"],
        ["X", "V", "provides_access"],
        ["Reg", "G", "appoints"],
        ["G", "V", "appoints"],
        ["Reg", "Q", "controls"],
        ["Q", "V", "can_revoke"],
        ["V", "E", "verifies"],
        ["P", "R", "receives_receipt_through"],
        ["Reg", "A", "can_verify_anchor"]
      ],
      "expected_conservative_result": {
        "verifier_collapses_into_operator": false,
        "reason": "Material control vectors are outside the operator's control.",
        "ndc_effect": "Verifier may count as a materially independent path if proof access is also independent."
      }
    },
    "scenario_4_open_tool_unfunded_exercise": {
      "description": "Verification tool is open and reproducible, but no independent actor is funded to exercise it at scale.",
      "edges": [
        ["O", "E", "creates"],
        ["O", "R", "controls"],
        ["P", "R", "receives_receipt_through"],
        ["Reg", "A", "can_verify_anchor"]
      ],
      "expected_conservative_result": {
        "verifier_collapses_into_operator": false,
        "reason": "No captured verifier is present, but exercise may be weak.",
        "ndc_effect": "Structural path may exist, but Effective NDC may remain low under ADAP-EXP-003."
      }
    }
  }
}# GCD-002 Expected Findings

## Expected Finding 1

Third-party status alone is not independence.

A verifier may be legally separate while materially dependent on the operator.

---

## Expected Finding 2

Funding can be a control vector.

If the verifier depends on the operator for revenue, renewal, access, or survival, conservative NDC analysis may collapse the verifier into the operator’s control domain.

---

## Expected Finding 3

Access capture can be as important as funding capture.

Even independently funded verifiers may be constrained if the operator controls APIs, credentials, schemas, receipt delivery, or proof availability.

---

## Expected Finding 4

Scope capture limits substantive verification.

If the operator defines what the verifier may inspect, the verifier may validate only the safe subset.

This can create formal verification without substantive contestability.

---

## Expected Finding 5

Open-source tooling does not solve funding capture by itself.

A reproducible verifier helps, but someone must still be materially able and incentivized to run it, publish findings, and escalate issues.

---

## Expected Finding 6

Client-side execution does not solve ecosystem capture.

It may reduce friction for affected parties, but large-scale contestability still requires independently funded and institutionally protected verification paths.

---

## Expected Finding 7

The safest verifier is not merely separate.

The safest verifier has independent funding, independent scope, independent access, independent revocation protection, and reproducible outputs.

---

## Expected Finding 8

GCD-002 should not produce a binary pass/fail result.

It should produce a dependency-collapse analysis showing which claimed verification paths survive conservative review.# GCD-002 Submission Template

## Reviewer

Name or handle:

Affiliation, if any:

Date:

---

## Scenario Reviewed

Select one:

- Scenario 1 — Operator-Funded Verifier
- Scenario 2 — Independent Funding, Operator Scope
- Scenario 3 — Independent Mandate
- Scenario 4 — Open Tool, Unfunded Exercise
- Other / modified scenario

---

## Apparent Verification Paths

List the verification paths before dependency collapse:

1.
2.
3.

---

## Material Control Dependencies

### Funding Dependencies

Who funds the verifier?

Does the verifier depend materially on the operator?

Answer:

---

### Access Dependencies

Who provides access to receipts, APIs, schemas, proof material, or credentials?

Answer:

---

### Scope Dependencies

Who defines what the verifier may inspect?

Answer:

---

### Governance Dependencies

Who selects, appoints, certifies, or approves the verifier?

Answer:

---

### Revocation Dependencies

Who can terminate, replace, revoke, or block the verifier?

Answer:

---

## Collapse Analysis

Does the verifier collapse into the operator’s control domain?

Answer:

Reason:

---

## Structural NDC Estimate

Before collapse:

After conservative collapse:

Explanation:

---

## Effective NDC / Exercise Risk

Does verification appear likely to be exercised?

What incentives support or suppress exercise?

Answer:

---

## Conclusion

Is the third-party verification path substantive or theatrical?

Answer:

---

## Open Questions

List any unresolved dependencies or uncertainties:

1.
2.
3.# GCD-002 Reviewer Guidelines

## Purpose

GCD-002 asks whether third-party verification remains independent when funding, access, scope, governance, and revocation are included in the custody graph.

Reviewers should not assume that legal separation equals independence.

---

## Review Rule

A verifier should be counted as independent only if its material control vectors are disjoint from the operator being verified.

Material control vectors include:

- funding,
- access,
- scope,
- governance,
- appointment,
- certification,
- renewal,
- revocation,
- data availability,
- proof availability,
- business survival.

---

## What to Avoid

Do not say:

“Verifier is third-party, therefore independent.”

Do not say:

“Tool is open-source, therefore ecosystem is independent.”

Do not say:

“Client-side verification exists, therefore NDC increased.”

Do not say:

“Independent verification is available” without asking who funds and sustains it.

---

## What to Look For

Look for hidden control edges:

- Who pays?
- Who grants access?
- Who defines scope?
- Who renews the contract?
- Who can revoke access?
- Who can suppress findings?
- Who controls schemas?
- Who controls proof availability?
- Who benefits from non-disclosure?
- Who can survive an adverse finding?

---

## Scoring Guidance

This challenge does not require a numeric score.

But reviewers may classify scenarios as:

### Strong Independence

Funding, access, scope, governance, and revocation are materially disjoint from the operator.

### Partial Independence

Some vectors are disjoint, but others remain operator-controlled.

### Theatrical Independence

Verifier is formally separate but materially dependent on the operator.

### No Meaningful Independence

Verifier, proof access, funding, and scope all collapse into the operator’s control domain.

---

## Final Reviewer Question

After conservative collapse, does the verifier still impose a real independent constraint on the operator?

If not, third-party verification may be theater.
