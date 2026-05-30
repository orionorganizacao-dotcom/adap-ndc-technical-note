# Non-Self-Attested Materiality

## Purpose

This document defines a structural constraint for A-DAP:

A materiality model cannot be treated as an independent audit basis when it is selected, applied, and benefited from by the same actor.

This principle exists to prevent A-DAP metrics from becoming self-attested audit claims at the criteria layer.

A-DAP does not only ask whether a decision record can be reconstructed.

It also asks whether the criteria used to claim reconstructibility are themselves independently constrained.

## Core Problem

A-DAP uses custody graphs and NDC to reason about structural auditability.

However, NDC is meaningful only under a materiality model.

The materiality model determines:

- which actors count as distinct custody domains
- which dependencies are relevant
- which dependencies are ignored
- which shared controls cause conservative collapse
- which vertices and edges enter the custody graph
- which independence claims are accepted
- which verification paths are treated as meaningful

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

    The system validates its own decision.

The issue becomes:

    The auditor validates the criteria by which the audit result is produced.

This is structurally dangerous because whoever controls materiality controls the resulting NDC claim.

## Principle of Non-Self-Attested Materiality

A materiality model cannot be considered independent if the same actor defines the materiality criteria, applies them to the custody graph, and benefits from the resulting audit claim.

Materiality must be at least one of the following:

1. externally anchored
2. adversarially contestable
3. independently reproducible

If none of these conditions is satisfied, the resulting NDC may be useful as an internal diagnostic, but it must not be presented as an independent audit claim.

## Formal Statement

Let:

- S be the system under audit
- G be the custody graph used to compute NDC
- M be the materiality model used to construct or collapse G
- A be the actor performing the audit
- B be the actor benefiting from the audit claim
- V be the verifier or audit procedure

If:

- A selects M
- A applies M to construct G
- A or B benefits from the resulting NDC claim
- no external anchor, adversarial challenge, or independent reproduction constrains M

then the materiality claim is self-attested.

In this case:

    NDC(S under M)

must not be treated as an independent audit result.

It must be labeled as one of the following:

    self-declared materiality

or:

    internal diagnostic only

## Validity Levels for Materiality

A-DAP distinguishes between three levels of materiality strength.

## Level 1: Self-Declared Materiality

The auditor or system operator declares the materiality model without external anchoring, adversarial contestability, or independent reproduction.

This level is weak.

It may be useful for:

- internal analysis
- design review
- early-stage architecture mapping
- preliminary threat modeling
- internal governance planning

It is not sufficient for independent verification.

Allowed claim:

    The system has NDC = n under the operator-declared materiality model.

Not allowed claim:

    The system has independent NDC = n.

## Level 2: Externally Anchored Materiality

The materiality model is constrained by external facts, standards, contracts, legal obligations, technical documentation, jurisdictional separation, infrastructure records, or independent operational evidence.

Examples of external anchors include:

- separate legal entities
- separate jurisdictions
- independent key custody
- independent timestamping authority
- separately administered signing keys
- contractually separated operators
- regulatory requirements
- published audit standards
- immutable external receipts
- public source repositories with reproducible verification procedures
- infrastructure records that can be independently inspected
- documented separation of administrative control

Externally anchored materiality is stronger than self-declared materiality because the auditor cannot freely choose all criteria.

Allowed claim:

    The system has NDC = n under an externally anchored materiality model.

## Level 3: Adversarially Tested Materiality

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
- formal challenge by an opposing expert
- documented review by an independent standards body

The key property is that the actor benefiting from the audit result does not have unilateral control over what counts as material.

Allowed claim:

    The system has NDC = n under an adversarially tested materiality model.

## Required Disclosure

Any A-DAP audit report that uses NDC must disclose the materiality basis.

Minimum disclosure:

    Materiality basis: self-declared / externally anchored / adversarially tested

    Materiality authority: actor, standard, court, regulator, auditor, or review body

    Materiality criteria: criteria used to decide what counts as material

    Collapse rules: rules for merging custody domains

    Ignored dependencies: dependencies considered immaterial

    Known contested dependencies: dependencies challenged or unresolved

    NDC claim type: internal diagnostic / externally anchored / adversarially tested

## Why This Matters

Without this rule, an auditor could inflate NDC by choosing favorable graph boundaries.

Examples of manipulation include:

- splitting one operational domain into many artificial nodes
- treating correlated services as independent
- ignoring shared administrative control
- ignoring common cloud infrastructure
- ignoring common key custody
- ignoring shared legal authority
- ignoring common economic incentives
- treating a verifier as independent without analyzing its own custody graph
- treating a standard maintainer as neutral without analyzing standard capture
- ignoring common ownership or common procurement control

This would create audit theater with mathematical presentation.

A-DAP must avoid reproducing the same failure it criticizes in other systems.

## Relation to the Self-Dependency Lemma

The self-dependency lemma states that a system cannot independently verify its own evidentiary claim when the evidence remains under the same control path as the origin.

Self-attested materiality is the same problem at the criteria layer.

The decision may be externally verified, but if the criteria defining externality are chosen by the same actor, independence is weakened or lost.

Thus, A-DAP extends the self-dependency concern across four layers:

1. decision record
2. evidence envelope
3. verifier
4. materiality model

The protocol must evaluate not only who controls the decision, but also who controls the criteria used to claim independence.

## Composed Custody Graph

A-DAP should not compute auditability only over the generator.

A mature audit must consider the composed custody graph.

    G_total = G_generator union G_verifier union G_materiality union G_standard

Where:

- G_generator represents the system that produced the decision
- G_verifier represents the verification process or tooling
- G_materiality represents the authority and evidence behind materiality selection
- G_standard represents the governance of the standard, certification body, or protocol authority when applicable

The total NDC should be computed over the composed graph.

    NDC_total = min-cut(G_total)

An external verifier improves auditability only if the composed custody graph does not introduce a lower-order capture path than the original system.

If adding a verifier reduces the composed NDC, the verifier weakens the architecture.

A-DAP must detect this condition rather than hide it.

## Verifier Independence

A verifier is not independent merely because it is external to the generator.

A verifier may still share control paths with the generator, including:

- common ownership
- common infrastructure
- common cloud administration
- shared signing keys
- shared legal authority
- shared economic incentives
- shared certification authority
- shared standard maintainer
- common procurement or vendor dependency
- common operational administrator

A-DAP therefore requires verifier independence to be analyzed through the composed custody graph.

Allowed claim:

    The verifier is external to the generator, and its custody graph does not introduce a lower-order capture path under the declared materiality model.

Not allowed claim:

    The verifier is independent because it is a separate tool.

## W-NDC Caution

Weighted NDC may be useful for representing differences in independence, correlation, cost, jurisdiction, and control concentration.

However, W-NDC introduces subjectivity.

Weights must not be arbitrary estimates chosen by the auditor.

A weighted score is defensible only when weights are derived from external anchors or reproducible criteria.

Examples of defensible weighting inputs:

- separate legal entities
- separate jurisdictions
- independent operators
- separate root keys
- independent timestamping authorities
- independent infrastructure accounts
- documented cost of compromise
- regulatory separation
- contractual separation
- public reproducibility
- documented operational separation
- independently verifiable custody boundaries

Examples of weak weighting inputs:

- auditor intuition
- vendor assurance
- undocumented independence claims
- internal risk scoring without evidence
- self-reported separation
- unsupported cost estimates
- vague statements of organizational independence
- informal trust in the verifier

Rule:

If the weights are self-declared, W-NDC must be labeled as internal diagnostic only.

## Acceptable and Unacceptable Claims

## Acceptable Claim 1

    Under the operator-declared materiality model, this system has NDC = 3.
    This is an internal diagnostic claim, not an independent verification claim.

## Acceptable Claim 2

    Under an externally anchored materiality model based on separate legal entities, independent key custody, and independent timestamping, this system has NDC = 3.

## Acceptable Claim 3

    Under an adversarially tested materiality model, no lower-order capture path was identified after challenge.

## Unacceptable Claim 1

    This system is independently auditable because our internal auditor assigned NDC = 3.

## Unacceptable Claim 2

    The verifier is independent because the audit report says so.

## Unacceptable Claim 3

    The graph has five domains, therefore the system has strong auditability.

## Unacceptable Claim 4

    The materiality model is valid because it was declared in the audit report.

## Design Requirement

Any implementation of A-DAP that exposes NDC must include materiality metadata.

A valid A-DAP audit object should include:

- materiality_model_id
- materiality_basis
- materiality_authority
- materiality_criteria
- collapse_rules
- ignored_dependencies
- contested_dependencies
- verification_authority
- verifier_custody_graph
- composed_ndc
- claim_scope
- claim_limitations

Without these fields, an NDC result should be treated as incomplete.

## Minimal JSON Shape

The following is a minimal JSON-style structure. It is written without fenced code blocks to remain mobile-safe.

    {
      "ndc_claim": {
        "value": 3,
        "claim_type": "externally_anchored",
        "scope": "decision-envelope-verification",
        "limitations": [
          "NDC is valid only under the declared materiality model",
          "Verifier independence is evaluated in the composed custody graph",
          "Materiality is not treated as independent when it is selected, applied, and benefited from by the same actor"
        ]
      },
      "materiality": {
        "model_id": "materiality-v0.1",
        "basis": "externally_anchored",
        "authority": "independent-auditor-or-standard",
        "criteria": [
          "separate legal entity",
          "separate key custody",
          "independent timestamping authority"
        ],
        "collapse_rules": [
          "domains under common administrative root collapse",
          "keys controlled by the same operator collapse",
          "services under the same unverifiable custody chain collapse"
        ],
        "ignored_dependencies": [
          {
            "dependency": "public internet routing",
            "reason": "not specific to evidentiary custody under this model"
          }
        ],
        "contested_dependencies": []
      },
      "composed_graph": {
        "includes": [
          "generator",
          "verifier",
          "materiality-authority",
          "standard-maintainer"
        ],
        "ndc_total": 3
      }
    }

## Practical Audit Checklist

Before accepting an A-DAP NDC claim, ask:

1. Who selected the materiality model?
2. Who benefits from the resulting NDC score?
3. Can another party contest the materiality model?
4. Are the materiality criteria externally anchored?
5. Are the collapse rules explicit?
6. Are ignored dependencies disclosed?
7. Are contested dependencies disclosed?
8. Is the verifier included in the composed custody graph?
9. Does the verifier introduce a lower-order capture path?
10. Are W-NDC weights externally justified?
11. Is the standard maintainer included when certification is involved?
12. Is the claim labeled correctly as internal, externally anchored, or adversarially tested?

If the answer to these questions is unclear, the NDC claim should not be treated as independently verified.

## Relation to A-DAP Scope

This document does not weaken A-DAP.

It strengthens its scope discipline.

A-DAP does not claim to eliminate trust.

A-DAP makes remaining trust dependencies explicit, inspectable, and structurally contestable.

This includes trust dependencies inside:

- the decision system
- the evidence envelope
- the verifier
- the materiality model
- the standard or certification authority

The goal is not trustlessness.

The goal is to prevent hidden trust from being misrepresented as independent verification.

## Boundary Rule

A-DAP must not treat any of the following as independent verification by default:

- self-declared materiality
- self-scored independence
- self-operated verification
- self-maintained certification criteria
- self-reported separation of custody
- self-assigned W-NDC weights
- self-controlled verifier tooling

These may support internal diagnosis.

They do not establish independent auditability unless externally anchored, adversarially contestable, or independently reproducible.

## Summary

NDC is not an absolute property of a system.

NDC is a property of a system under a materiality model.

A materiality model is not independent merely because it is declared.

Materiality must be externally anchored, adversarially contestable, or independently reproducible.

Otherwise, the audit claim remains self-attested at the criteria layer.

A-DAP must not allow self-attested materiality to masquerade as independent verification.
