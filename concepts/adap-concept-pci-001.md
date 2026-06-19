ADAP-CONCEPT-PCI-001

Provenance Contestability Index (PCI)

Status

Concept Note

Category

Contestability / Verification Theory

Abstract

Many AI governance mechanisms provide evidence that a decision occurred, but fail to provide evidence that the provenance of the decision can be independently contested.

A system may preserve logs, signatures, hashes, and timestamps while still concentrating provenance authority in a single actor or custody domain.

This note introduces the Provenance Contestability Index (PCI), a conceptual measure intended to evaluate whether the provenance chain associated with a decision remains independently challengeable after deployment.

PCI does not measure correctness.

PCI does not measure fairness.

PCI does not measure explainability.

PCI measures the degree to which provenance claims remain contestable by actors that are structurally independent from the decision operator.

---

Motivation

Existing audit systems often answer:

"Can we prove this record existed?"

but fail to answer:

"Can we independently challenge the provenance claim attached to this record?"

This distinction becomes critical when:

- operators control logging infrastructure,
- operators control storage,
- operators control verification interfaces,
- operators define materiality,
- operators determine admissible evidence.

Under such conditions, provenance may become verifiable yet uncontestable.

A-DAP treats contestability as a first-class property rather than a byproduct of record preservation.

---

Core Observation

A provenance chain is only as contestable as its most concentrated dependency.

Formally:

If all provenance verification paths collapse into a single authority domain, provenance contestability approaches zero regardless of cryptographic strength.

This phenomenon is called:

Provenance Concentration Collapse.

---

Definition

Let:

P = set of provenance verification paths

Each path must allow an external verifier to independently evaluate provenance claims.

PCI is defined conceptually as:

PCI = Independent Provenance Paths

subject to dependency collapse analysis.

Collapsed paths count as one.

Pseudo-independent paths count as one.

Only structurally independent paths contribute positively.

---

Interpretation

PCI = 0

No independently contestable provenance.

Operator assertions dominate.

---

PCI = 1

Single provenance authority.

Verification exists.

Contestability is weak.

---

PCI = 2

At least two independent provenance paths.

Provenance claims become externally challengeable.

---

PCI ≥ 3

Strong provenance contestability.

Multiple independent custody domains exist.

Failure of one path does not eliminate challenge capability.

---

Provenance Concentration Collapse

A system experiences Provenance Concentration Collapse when nominal provenance diversity is reduced by hidden dependencies.

Examples:

- Multiple databases controlled by one operator.
- Multiple signatures issued by the same authority.
- Multiple logs anchored by the same infrastructure provider.
- Multiple auditors funded by the same entity.

In such cases:

Nominal PCI > Effective PCI

The effective value must be computed after dependency reduction.

---

Relationship to NDC

NDC asks:

"How many independent verification paths remain?"

PCI asks:

"How many independent provenance paths remain?"

NDC evaluates contestability of the decision.

PCI evaluates contestability of the provenance claim.

The concepts are complementary.

A system may have:

High NDC
Low PCI

or

High PCI
Low NDC

depending on architecture.

---

Example

Scenario A

Operator provides:

- Decision record
- Internal log
- Internal timestamp

All controlled by operator.

PCI = 1

---

Scenario B

Operator provides:

- Internal log
- Independent TSA anchor
- Independent public ledger anchor

PCI = 3

assuming independence assumptions hold.

---

Security Implication

Cryptographic integrity does not guarantee provenance contestability.

Integrity answers:

"Was this altered?"

PCI answers:

"Can independent parties challenge how this provenance claim was established?"

These are distinct questions.

---

Future Work

Future A-DAP research may formalize:

- Effective PCI
- Objective-Indexed PCI
- Provenance Debt
- Provenance Capture Risk
- Automated PCI Computation
- PCI-NDC Joint Analysis

---

Conclusion

The Provenance Contestability Index (PCI) extends the A-DAP philosophy from decision contestability to provenance contestability.

The central claim is simple:

A provenance chain that cannot be independently challenged should not be considered fully trustworthy, regardless of its cryptographic integrity.

Contestability applies not only to decisions, but also to the provenance claims used to justify them.
