# Verifier Funding Capture — Funding as a Control Vector in Ecosystem NDC

## Status

Open architectural risk.

This document formalizes a non-technical failure mode of A-DAP:

A third-party verifier may appear independent while its funding, incentives, governance, access, or survival depend materially on the operator being verified.

In that case, the verifier may collapse into the same control domain under conservative NDC analysis.

This is the Arthur Andersen problem applied to decision-verification ecosystems.

---

## 1. Core Claim

A verifier is not independent merely because it is organizationally separate.

A verifier is independent only if its material control conditions are disjoint from the operator being verified.

Those material control conditions include:

- funding,
- revenue dependence,
- contract renewal,
- access rights,
- certification status,
- governance,
- appointment authority,
- revocation authority,
- data access,
- legal mandate,
- and operational continuity.

If those conditions depend on the operator whose decision is being verified, then the verifier may become captured.

Under conservative NDC analysis, the verifier and the operator may collapse into the same control domain.

---

## 2. Why This Matters

A-DAP can create reconstructible decision evidence.

ADAP-EXP-003 shows that verification must actually be exercised.

The Exercisable Verification Interface makes verification easier to exercise.

But a deeper question remains:

Who funds and sustains the party that exercises verification?

If the answer is:

“The same operator whose decisions are being verified,”

then the verification ecosystem may be structurally captured.

This is not a cryptographic failure.

It is an institutional and economic failure.

---

## 3. The False Independence Problem

A common governance mistake is to treat organizational separation as independence.

Example:

- Company A makes automated decisions.
- Audit Firm B verifies decision receipts.
- Company A pays Audit Firm B.
- Company A can terminate or replace Audit Firm B.
- Audit Firm B depends on Company A for revenue.
- Audit Firm B receives access only through Company A’s systems.

On paper, there are two entities.

In the control graph, there may be only one effective domain.

If the verifier’s survival depends on the operator, the verifier may not be meaningfully disjoint.

The apparent NDC may be 2.

The conservative NDC may collapse to 1.

---

## 4. Relation to NDC

NDC is not a count of legal entities.

NDC is a count of materially independent verification paths after dependency collapse.

Therefore, a verifier must be analyzed not only by its formal identity, but by its control dependencies.

A third-party verifier may fail independence if it depends on the operator for:

- payment,
- permission,
- continued access,
- renewal,
- reputation,
- platform integration,
- API credentials,
- data feeds,
- schema access,
- proof availability,
- or business survival.

If those dependencies are material, they belong in the custody and control graph.

---

## 5. Funding as a Control Vector

Funding is a control vector when it can influence whether verification is performed, reported, delayed, softened, narrowed, or abandoned.

Funding capture may occur when:

- the operator directly pays the verifier;
- the operator controls renewal of the verifier’s contract;
- the verifier receives most of its revenue from the operator;
- the operator can terminate access after unfavorable findings;
- the verifier depends on operator certification programs;
- the verifier’s market access depends on operator approval;
- the verifier is selected by the operator;
- the verifier’s scope is contractually limited by the operator;
- the verifier is paid per compliance approval rather than adversarial finding;
- the verifier faces financial penalty for escalation.

In these cases, the verifier may be economically separate but structurally dependent.

---

## 6. The Arthur Andersen Pattern

The Arthur Andersen pattern appears when the auditor’s business model depends on the entity being audited.

The risk is not merely corruption.

The risk is structural incentive alignment.

The verifier may avoid aggressive findings because the verifier’s own continuity depends on maintaining the client relationship.

In A-DAP terms:

The verifier may appear as an independent node.

But funding dependency creates a control edge from the operator to the verifier.

If that edge is material, conservative dependency collapse may merge them.

The result:

NDC does not increase.

The verification ecosystem becomes a theater of independence.

---

## 7. Ecosystem NDC

A-DAP usually analyzes the decision envelope, custody path, verifier, and reconstruction process.

Verifier Funding Capture extends the analysis to the ecosystem level.

The question becomes:

What is the NDC of the contestation ecosystem?

Not merely:

How many verification tools exist?

But:

How many materially independent actors have both the ability and incentive to exercise verification?

An ecosystem with many verifiers funded by the same operator may still have low NDC.

An ecosystem with fewer verifiers but independent funding and legal mandate may have higher practical independence.

---

## 8. Formal Pattern

Let:

- O = operator whose decision is being verified.
- V = verifier.
- F = funding source.
- A = access provider.
- G = governance or appointment authority.
- R = revocation authority.

A verifier is materially independent only if no critical control path from O to V exists through F, A, G, or R.

If:

O controls F,

or:

O controls A,

or:

O controls G,

or:

O controls R,

then V may collapse into O under conservative dependency analysis.

The relevant question is not:

“Is V a separate organization?”

The relevant question is:

“Can O materially influence whether V verifies, reports, escalates, or survives?”

---

## 9. Capture Scenarios

### 9.1 Direct Payment Capture

The operator pays the verifier directly.

The verifier depends on the operator for revenue.

Risk:

The verifier may soften findings to preserve the commercial relationship.

### 9.2 Renewal Capture

The verifier’s contract must be renewed by the operator.

Risk:

The verifier may avoid adversarial findings before renewal.

### 9.3 Access Capture

The verifier requires operator-controlled APIs, portals, credentials, or data feeds.

Risk:

The operator can limit, delay, degrade, or revoke access.

### 9.4 Scope Capture

The operator funds verification but defines what may be verified.

Risk:

The verifier can only verify the safe subset.

### 9.5 Certification Capture

The operator or industry consortium controls certification status.

Risk:

The verifier may conform to industry expectations rather than adversarial independence.

### 9.6 Reputation Capture

The verifier’s business model depends on being accepted by the same industry it verifies.

Risk:

The verifier becomes reluctant to produce findings that threaten market access.

### 9.7 Platform Capture

The verifier’s tool must run inside the operator’s ecosystem.

Risk:

The verifier becomes technically dependent even if legally separate.

---

## 10. Why Open Source Alone Is Not Enough

Open-source verification tooling helps.

But open source does not solve funding capture by itself.

A tool can be open-source while the actor exercising it is economically dependent.

A reproducible verifier may produce deterministic output, but someone must decide:

- when to run it,
- which cases to inspect,
- whether to publish results,
- whether to escalate,
- whether to challenge the operator,
- whether to continue funding the verification process.

Those are institutional choices, not merely software properties.

---

## 11. Why Client-Side Alone Is Not Enough

Client-side verification can reduce friction.

It may help affected parties exercise verification.

But client-side execution does not solve ecosystem funding capture.

Even if users can run a verifier locally, large-scale accountability may still require:

- public defenders,
- regulators,
- ombudsmen,
- civil-society organizations,
- journalists,
- auditors,
- courts,
- unions,
- class-action structures,
- or independent research institutions.

If those entities lack sustainable independent funding, verification remains sporadic and fragile.

Client-side execution helps exercise.

It does not create a funded verification ecosystem.

---

## 12. Relation to ADAP-EXP-003

ADAP-EXP-003 introduces Effective NDC and Exercise Debt.

It shows that structural verification paths are not enough if they are not exercised.

Verifier Funding Capture explains one reason exercise may fail:

the actors capable of exercising verification may lack independent funding or may be economically captured.

Therefore, e_i is not only a behavioral probability.

It is also shaped by institutional funding structures.

If no independent actor is funded to verify, e_i may remain low even when tools are available.

If the only funded verifier depends on the operator, the verification path may collapse structurally.

---

## 13. Relation to Adoption Capture Risk

Adoption Capture Risk describes how an operator can formally adopt A-DAP while preserving control over scope, interface, and exercise.

Verifier Funding Capture is one mechanism of adoption capture.

An operator can say:

“We have independent third-party verification.”

But if the verifier is funded, selected, scoped, renewed, or access-controlled by the operator, independence may be theatrical.

The relevant question is:

Who controls the verifier’s material conditions?

---

## 14. Relation to Exercisable Verification Interface

The Exercisable Verification Interface prevents the validator from becoming an authority by emphasizing reproducibility.

Verifier Funding Capture adds:

Reproducibility is necessary but not sufficient.

A reproducible result must still be exercised by actors who are materially able and incentivized to use it.

If all institutional users of the verifier are economically dependent on the operator, the reproducibility layer may exist but remain weakly exercised or selectively exercised.

---

## 15. Diagnostic Questions

A reviewer assessing a verification ecosystem should ask:

1. Who pays the verifier?
2. Who selected the verifier?
3. Who can replace the verifier?
4. Who defines the verifier’s scope?
5. Who grants data access?
6. Who can revoke access?
7. Who controls the schema used by the verifier?
8. Who receives the verifier’s findings?
9. Who decides whether findings are published?
10. Who decides whether findings are escalated?
11. Does the verifier depend on the operator for revenue?
12. Does the verifier depend on the operator for market access?
13. Does the verifier depend on the operator for credentials or APIs?
14. Can the verifier survive after producing an adverse finding?
15. Can affected parties or regulators reproduce the verifier’s result without the verifier’s permission?
16. Can another independently funded actor run the same verification?
17. Does the funding model reward approval or adversarial discovery?
18. Are negative findings economically punished?
19. Is there a public-interest funding path?
20. Is there a legal mandate protecting verifier independence?

These questions should be part of ecosystem-level NDC analysis.

---

## 16. Safe Funding Models

No funding model is perfect.

But some models reduce capture risk.

Potentially safer models include:

- regulator-funded verification;
- court-appointed verification;
- public defender or legal aid verification;
- civil-society verification funds;
- pooled industry levies administered independently;
- mandatory verification funds governed by public law;
- adversarial bounty systems funded through independent escrow;
- academic or nonprofit verification labs with diversified funding;
- insurance-backed verification pools with disclosure duties;
- union, consumer association, or class-action funded verification.

The key requirement is not purity.

The key requirement is that the verifier’s survival must not materially depend on pleasing the operator being verified.

---

## 17. Unsafe Funding Models

Higher-risk models include:

- operator-paid exclusive verifier;
- operator-selected verifier without external review;
- verifier contract renewed solely by operator;
- verifier access controlled solely by operator;
- verifier scope defined solely by operator;
- verifier paid per approval;
- verifier penalized for escalation;
- verifier prohibited from publishing adverse findings;
- verifier dependent on one operator or one industry consortium;
- verifier operating only through operator-controlled dashboards.

These models may preserve formal separation while collapsing practical independence.

---

## 18. Funding Disclosure Requirement

Any A-DAP deployment that relies on third-party verification should disclose:

- who funds the verifier,
- who selected the verifier,
- who controls renewal,
- who controls access,
- who defines scope,
- whether adverse findings can be published,
- whether the verifier has independent legal mandate,
- whether affected parties can trigger verification,
- whether regulators can reproduce verification,
- whether other verifiers can independently run the same procedure.

Without funding disclosure, claims of third-party verification are incomplete.

---

## 19. Ecosystem-Level Exercise Debt

Exercise Debt can exist not only at the individual verification-path level, but also at the ecosystem level.

A system may claim:

“Independent verification is available.”

But if no independent actor is funded or incentivized to verify, the practical exercise probability remains low.

Ecosystem Exercise Debt is the gap between:

- the verification ecosystem claimed on paper,
- and the verification ecosystem that is materially funded, independent, and active.

This should be considered a first-class risk.

---

## 20. Safe Claim

A safe claim is:

“This deployment includes third-party verification paths whose funding, access, scope, and governance dependencies are disclosed and subject to conservative dependency-collapse analysis.”

This does not claim perfect independence.

It makes the control structure visible.

---

## 21. Unsafe Claim

An unsafe claim is:

“This deployment is independently verified because a third-party auditor is involved.”

This is insufficient.

Third-party status alone does not prove independence.

The verifier’s funding, access, scope, governance, and survival conditions must be analyzed.

---

## 22. Relation to Business Strategy

Verifier Funding Capture clarifies the real strategic moat of A-DAP.

The moat is not merely:

- hashing,
- signatures,
- timestamps,
- Merkle trees,
- receipts,
- or verifier scripts.

Those can be copied.

The deeper value is knowing how to design and evaluate disjoint verification ecosystems.

That includes:

- independent verifier funding,
- scope governance,
- access rights,
- reproducibility,
- dependency-collapse analysis,
- exercise incentives,
- and public-interest verification pathways.

The business is not only cryptographic infrastructure.

It is institutional architecture for contestability.

---

## 23. Proposed Experiment

A useful next experiment is to run GCD-001 or a similar custody-graph test with verifier funding included as an explicit control vector.

The graph should include:

- operator,
- decision envelope,
- receipt delivery channel,
- external anchor,
- verifier,
- verifier funding source,
- verifier access channel,
- verifier scope authority,
- verifier revocation authority,
- affected party,
- regulator or independent reviewer.

The test should ask:

Does the apparent NDC increase when a third-party verifier is added?

Or does it collapse when the verifier’s funding, access, or scope authority depends on the operator?

The purpose is to test whether third-party verification is structurally real or theatrical.

---

## 24. Summary

A-DAP cannot rely on third-party verification as a slogan.

The verifier must itself be analyzed.

A separate verifier is not necessarily an independent verifier.

Funding is a control vector.

Access is a control vector.

Scope is a control vector.

Revocation is a control vector.

If those vectors lead back to the operator, conservative NDC may collapse.

The central warning is:

Do not confuse third-party verification with independent verification.

The independence of verification is economic and institutional, not merely organizational or technical.
