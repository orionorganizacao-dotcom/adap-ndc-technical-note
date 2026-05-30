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

Reducing a false independence claim is progress.
