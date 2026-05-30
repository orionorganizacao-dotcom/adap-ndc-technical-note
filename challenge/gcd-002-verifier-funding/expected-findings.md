# GCD-002 Expected Findings

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

It should produce a dependency-collapse analysis showing which claimed verification paths survive conservative review.
