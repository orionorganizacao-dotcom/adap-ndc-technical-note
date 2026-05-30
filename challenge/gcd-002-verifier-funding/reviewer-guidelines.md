# GCD-002 Reviewer Guidelines

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
