# Non-Self-Attested Materiality

## Purpose

This document defines a structural constraint for A-DAP:

A materiality model cannot be treated as an independent audit basis when it is selected, applied, and benefited from by the same actor.

This principle exists to prevent A-DAP metrics from becoming self-attested audit claims.

## Core Problem

A-DAP uses custody graphs and NDC to reason about structural auditability.

However, NDC is meaningful only under a declared materiality model.

The materiality model determines:

- which actors count as distinct custody domains
- which dependencies are relevant
- which shared controls cause conservative collapse
- which vertices and edges enter the custody graph
- which controls are ignored as immaterial
- which independence claims are accepted

This creates a higher-order risk.

If the same actor chooses the materiality model and computes the resulting NDC, that actor can influence the audit result by choosing what counts as material.

In that case, manipulation is not removed.

It is moved from graph construction into materiality selection.

## Breach 6: Self-Attested Materiality

Self-attested materiality occurs when an actor:

1. defines the materiality criteria
2. applies those criteria to the custody graph
3. computes or benefits from the resulting NDC claim
4. faces no adversarial challenge or external constraint over the materiality model

In this condition, the materiality layer becomes a self-attesting object.

The A-DAP self-dependency lemma applies one layer above the decision record.

The issue is not only:

"The system validates its own decision."

The issue becomes:

"The auditor validates the criteria by which the audit result is produced."

## Principle of Non-Self-Attested Materiality

A materiality model cannot be considered independent if the same actor defines the materiality criteria, applies them to the custody graph, and benefits from the resulting audit claim.

Materiality must be at least one of the following:

1. externally anchored
2. adversarially contestable
3. independently reproducible

If none of these conditions is satisfied, the resulting NDC may be useful as an internal diagnostic, but it must not be presented as an independent audit claim.

## Formal Statement

Let:

- `S` be the system under audit
- `G` be the custody graph used to compute NDC
- `M` be the materiality model used to construct or collapse `G`
- `A` be the actor performing the audit
- `B` be the actor benefiting from the audit claim
- `V` be the verifier or audit procedure

If:

- `A` selects `M`
- `A` applies `M` to construct `G`
- `A` or `B` benefits from the resulting NDC claim
- no external anchor, adversarial challenge, or independent reproduction constrains `M`

then the materiality claim is self-attested.

In this case:

`NDC(S under M)` must not be treated as an independent audit result.

It must be labeled as:

`self-declared materiality`

or

`internal diagnostic only`

## Validity Levels for Materiality

A-DAP distinguishes between three levels of materiality strength.

### Level 1: Self-Declared Materiality

The auditor or system operator declares the materiality model without external anchoring or adversarial contestability.

This level is weak.

It may be useful for internal analysis, design review, or early-stage architecture mapping.

It is not sufficient for independent verification.

Allowed claim:

"The system has NDC = n under the operator-declared materiality model."

Not allowed claim:

"The system has independent NDC = n."

### Level 2: Externally Anchored Materiality

The materiality model is constrained by external facts, standards, contracts, legal obligations, technical documentation, jurisdictional separation, infrastructure records, or independent operational evidence.

Examples of external anchors include:

- separate legal entities
- separate jurisdictions
- independent key custody
- independent timestamping authority
- independent cloud accounts or regions, when operationally meaningful
- separately administered signing keys
- contractually separated operators
- regulatory requirements
- published audit standards
- immutable external receipts
- public source repositories with reproducible verification procedures

Externally anchored materiality is stronger than self-declared materiality because the auditor cannot freely choose all criteria.

Allowed claim:

"The system has NDC = n under an externally anchored materiality model."

### Level 3: Adversarially Tested Materiality

The materiality model is proposed by one party and contestable by another party with opposing incentive.

This is the strongest level.

Adversarial materiality may occur through:

- litigation
- regulatory review
- external audit challenge
- red-team review
- public reconstruction challenge
- independent replication
- stakeholder objection
- affected-party contestation

The key property is that the actor benefiting from the audit result does not have unilateral control over what counts as material.

Allowed claim:

"The system has NDC = n under an adversarially tested materiality model."

## Required Disclosure

Any A-DAP audit report that uses NDC must disclose the materiality basis.

Minimum disclosure:

```text
Materiality basis: self-declared / externally anchored / adversarially tested

Materiality authority: [actor or standard]

Materiality criteria: [criteria used]

Collapse rules: [rules for merging custody domains]

Ignored dependencies: [dependencies considered immaterial]

Known contested dependencies: [dependencies challenged or unresolved]

NDC claim type: internal diagnostic / externally anchored / adversarially tested
