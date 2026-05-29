# Signer, Custody, and Verification Boundary

A-DAP depends on a basic custody assumption:

the authority that seals a decision record, the path that preserves it, and the path that verifies it must not collapse into the same compromised trust domain.

If the signer, envelope creator, custody path, and verifier are all controlled by the same actor or infrastructure boundary, A-DAP may preserve a cryptographically valid record while providing no meaningful independent evidentiary value.

In that case, NDC may collapse to 1.

This is not an implementation detail.

It is a custody boundary.

---

## 1. Core Claim

A-DAP does not make a record trustworthy merely because it is signed.

A signature proves that a signing key endorsed a record.

It does not prove that:

- the signer was independent;
- the key was uncompromised;
- the envelope was honestly created;
- the record was complete;
- unfavorable records were not omitted;
- the verifier was outside the same trust domain;
- the custody path was not captured.

A-DAP therefore treats signing as one component of evidentiary structure, not as evidence by itself.

The central question is not only:

> Was the record signed?

The better question is:

> What would need to be compromised for a false, incomplete, or selectively omitted record to appear valid without detection?

---

## 2. The Signer Is Not the Proof

A signing key can strengthen a decision envelope.

But the signer is not the proof.

The proof value depends on the surrounding custody structure.

A signature is weak when:

- the same operator generates the decision and signs the record;
- the same operator controls the signing key and the verifier;
- the same system creates the envelope and later validates it;
- the same custody path stores all artifacts;
- no independent witness, timestamp authority, verifier, or reconstruction path exists;
- unfavorable decisions can be omitted before signing.

In this configuration, the signature may only prove that the operator endorsed its own record.

That may be useful for attribution.

It is not enough for independent contestability.

---

## 3. Key Compromise

If the signing key is compromised, an attacker may be able to create records that appear valid.

The impact depends on what else is independent.

If the attacker controls only the signing key, but not the timestamp path, custody store, verifier, append-only log, or external anchor, detection may still be possible.

If the attacker controls the signing key and the surrounding custody path, the evidentiary value can collapse.

A-DAP analysis should distinguish between:

- key compromise alone;
- signer compromise;
- envelope creator compromise;
- custody path compromise;
- verifier compromise;
- timestamp or anchoring compromise;
- full trust-domain collapse.

These are not the same attack.

NDC depends on whether they are structurally distinct or merely different names for the same control point.

---

## 4. Omission at Origin

Omission at origin is one of the hardest attacks for any audit-trail architecture.

A system may produce perfect cryptographic evidence for the records it chose to create while silently failing to create records for unfavorable decisions.

This is different from alteration.

Alteration changes a record after it exists.

Omission prevents the record from existing in the first place.

Cryptography can make an existing record tamper-evident.

It cannot, by itself, prove that all relevant records were created.

A signed log can be complete with respect to its own contents while incomplete with respect to the real event stream.

This is why A-DAP must analyze omission separately from alteration.

---

## 5. Omission Before Anchoring

In asynchronous or batched systems, omission may occur before external anchoring.

For example:

- a decision is executed;
- the record is held internally;
- unfavorable records are dropped;
- only selected records enter the batch;
- the batch root is signed and anchored;
- the anchored evidence appears cryptographically valid.

In this case, the external anchor proves that the selected batch existed.

It does not prove that the batch was complete.

A-DAP should therefore ask:

- who controls batch construction?
- who controls the event stream before batching?
- can decisions be dropped before anchoring?
- is there an independent sequence source?
- are there counters, gap proofs, or append-only witnesses?
- can third parties detect missing records?
- what is the NDC for omission before anchoring?

If omission can be performed by a single operator before the record enters the evidentiary structure, NDC for omission may be 1 even if NDC for post-anchor alteration is higher.

---

## 6. Signer-Custody Collapse

Signer-custody collapse occurs when the same actor or trust domain controls too many evidentiary functions.

Examples:

- the same system decides, records, signs, stores, explains, and verifies;
- the same operator controls both the signing key and the verification interface;
- the same vendor provides the decision engine and the audit report;
- the same internal database stores all decision records and verification artifacts;
- the same administrative authority controls record creation, disclosure, and reconstruction;
- the same envelope contains both the evidence and the only verifier of that evidence.

When signer-custody collapse occurs, the system may still produce valid cryptographic artifacts.

But those artifacts may not provide independent evidentiary value.

They may only certify the claims of the same entity whose conduct is being evaluated.

This is the custody form of the Envelope Bottleneck.

---

## 7. NDC Implications

NDC is useful because it can expose signer-custody collapse.

If a false record can be created, signed, stored, and later verified through a single compromised trust domain, then NDC may collapse to 1.

That result is not a failure of NDC.

It is the metric revealing that the architecture is self-attesting.

A higher NDC may require structural separation among:

- decision generator;
- envelope creator;
- signing authority;
- timestamp authority;
- custody store;
- append-only log;
- external anchor;
- verifier;
- reconstruction procedure;
- disclosure interface.

The point is not that every implementation must maximize separation at all costs.

The point is that every implementation should declare what is separated, what is not, and what NDC follows from those assumptions.

---

## 8. Separation Is a Precondition, Not a Product Feature

A-DAP cannot manufacture independence after the fact.

If the system is deployed so that one operator controls the decision, record, signer, custody path, and verifier, then independent contestability has already been structurally weakened.

Adding signatures later does not fix this.

Adding logs later does not fix this.

Adding explanations later does not fix this.

Adding an internal verification dashboard later does not fix this.

Those mechanisms may improve operational traceability.

They do not necessarily create independent evidentiary value.

Real contestability requires separation to be designed into the custody model before the dispute.

---

## 9. Declared Custody Assumptions

Every A-DAP implementation should declare its custody assumptions.

At minimum, it should state:

- who creates the decision envelope;
- who controls the signing key;
- where the key is stored;
- how key compromise is detected;
- who controls the custody store;
- whether records are append-only;
- whether records can be omitted before commitment;
- who builds batches;
- who anchors commitments;
- who verifies records;
- whether the verifier is independent from the generator;
- whether the affected party can access enough evidence to contest the decision;
- what happens if the signer is compromised;
- what happens if the operator is compromised;
- what happens if the verifier is compromised.

Without declared custody assumptions, a cryptographic record can be mistaken for independent evidence when it is only internal attribution.

---

## 10. What A-DAP Should Not Claim

A-DAP should not claim that a signed record is automatically trustworthy.

A-DAP should not claim that cryptographic validity implies evidentiary independence.

A-DAP should not claim that a verifier is independent merely because it is a separate software module.

A-DAP should not claim that an internal audit dashboard is equivalent to external verification.

A-DAP should not claim that external anchoring proves completeness.

A-DAP should not claim that key compromise is solved by the protocol itself.

A-DAP should not claim that omission at origin can be solved by signatures.

The honest claim is narrower:

A-DAP can make signer, custody, and verification dependencies explicit.

It can help reveal when a system has collapsed into self-attestation.

It can make NDC = 1 visible instead of hidden.

---

## 11. Summary

A-DAP requires more than signed records.

It requires a custody structure in which decision, record, signer, verifier, and reconstruction path are separated enough to support meaningful contestability.

If the signer and verifier collapse into the same trust domain, cryptographic validity may remain while evidentiary independence disappears.

If unfavorable records can be omitted before commitment, a perfect audit trail may still be incomplete.

If the signing key or custody path is compromised, the strength of the envelope depends on what remains independently verifiable.

The central question is:

> Does the signature provide independent evidentiary value, or does it merely authenticate the claims of the same system being challenged?

That question must be answered before A-DAP can be treated as more than self-attestation.
