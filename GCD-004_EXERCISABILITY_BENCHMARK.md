GCD-004 — Exercisability Benchmark

Status

Conceptual Challenge Package

Pre-Falsification Stage

Not a certification metric.

Not a compliance score.

Not evidence of contestability by itself.

---

Motivation

A-DAP distinguishes between reconstructibility, contestability, and exercised rights.

A system may provide reconstructible evidence while affected parties remain unable to meaningfully use that evidence.

This creates a gap between:

- structural verifiability;
- structural contestability;
- effective contestability;
- exercised rights.

GCD-004 exists to test where that gap appears.

---

Central Question

Can an affected party actually use the available contestation path within the relevant damage window?

---

Threat Model

Adversary:

Structural friction.

Examples include:

- inaccessible evidence;
- short appeal windows;
- technical asymmetry;
- procedural complexity;
- dependency on institutional assistance;
- unavailable verification tooling;
- excessive reconstruction costs.

The benchmark does not test security.

It tests exercisability.

---

Layer Mapping

Layer| Question
NDC| Can the decision be independently verified?
CEI-Structural| Does the architecture provide contestation conditions?
CEI-Effective| Can the affected party actually use them?
Rights Exercised| Was contestation attempted?
Rights Satisfied| Did the institution provide effective remedy?

---

Benchmark Procedure

Step 1

Define an affected-party profile.

Example:

- no technical expertise;
- no prior legal assistance;
- 48-hour damage window;
- limited financial resources.

Step 2

Provide only the evidence structurally available through the system.

No privileged operator access.

No internal documentation.

No undisclosed tools.

Step 3

Attempt reconstruction and contestation.

Step 4

Record the first point of failure.

Failure dimensions:

- αs — Access
- τs — Time
- σs — Technical Symmetry
- βs — Binding Force

Step 5

Evaluate whether contextual support can compensate.

Examples:

- public defender;
- ombuds office;
- regulator;
- independent expert.

---

Classification

Architectural Collapse

Occurs when:

- αs = 0
- βs = 0

Context cannot restore the missing property.

Operational Collapse

Occurs when:

- τs fails
- σs fails

Context may partially compensate.

---

Expected Output

The benchmark does not produce a single score.

The output is:

- failure location;
- failure type;
- responsible layer;
- compensation availability;
- compensation dependency.

---

Relationship to Proposition 7

GCD-004 is the primary falsification mechanism for Proposition 7.

The benchmark exists to test whether:

NDC > 1

can coexist with

CEI-Effective = 0

under realistic contestation conditions.

A successful demonstration constitutes a direct supporting example for Proposition 7.

A failed demonstration may falsify or refine the proposition.

---

Future Work

- Standardized affected-party profiles.
- Sector-specific benchmarks.
- Public-benefit systems.
- Credit decisions.
- Insurance denials.
- Employment screening.
- Educational access decisions.
- Healthcare eligibility systems.
