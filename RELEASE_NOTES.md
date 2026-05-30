# Release Notes — A-DAP v0.4.1

Release: `v0.4.1`  
Project: A-DAP — Auditable Decision Accountability Protocol  
Status: Methodological hardening release  
Author: Ezio v.s. Santos

---

## 1. Release Summary

A-DAP `v0.4.1` adds a formal materiality limitation to the protocol.

The main clarification is narrow:

NDC is not an absolute property of a system.

NDC is meaningful only under a declared materiality model.

This release documents that self-declared materiality must not be treated as independent verification.

If the same actor selects the materiality model, applies it to the custody graph, and benefits from the resulting NDC claim, the result remains self-attested at the criteria layer.

---

## 2. Added

- `architecture/non-self-attested-materiality.md`
- README section: `Materiality and NDC Scope`
- README section: `Non-Self-Attested Materiality`
- README section: `Materiality Limitation`
- README updates to include materiality, verification assumptions, and composed custody concerns

---

## 3. Clarified

- NDC should not be treated as a standalone proof of independent auditability.
- NDC depends on disclosed materiality assumptions.
- Self-declared materiality may support internal diagnosis, but should not be presented as independent verification.
- A verifier is not independent merely because it is external to the generator.
- Materiality selection itself can become a control vector.
- Declared materiality is not independent verification by itself.

---

## 4. Safe Claim

A-DAP can help reason about structural dependency, reconstructibility, and detectability under declared custody, materiality, and verification assumptions.

It does not prove truth, fairness, legality, accountability, or independent verification by itself.

---

## 5. Why This Matters

This release reduces overclaim risk.

It prevents A-DAP from using the same self-attestation pattern that it criticizes in automated decision systems.

The key boundary added in this release is:

Declared materiality is not independent verification by itself.

---

## 6. Files Changed

- `README.md`
- `architecture/non-self-attested-materiality.md`

---

## 7. Status

This is a methodological hardening release.

It strengthens the protocol by narrowing its claims and making the materiality assumption explicit.

---
