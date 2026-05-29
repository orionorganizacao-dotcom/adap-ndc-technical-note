# ADAP-EXP-003 — Exercise Debt and Effective NDC

## Status

Problem formally stated.

This document does not claim to solve operational contestability.

It formalizes a gap: the difference between structural verifiability and exercised verifiability.

The purpose of EXP-003 is to show that NDC alone is not an operational security measure unless the probability of actual reconstruction is accounted for.

## 1. Core Claim

Structural NDC measures the number of independent verification paths available in the architecture.

But availability is not exercise.

A system may expose multiple independent verification paths and still impose almost no real cost on an attacker if affected parties, auditors, regulators, or third parties do not actually reconstruct the committed record.

Therefore:

NDC is an upper bound.

Effective NDC is the expected number of verification constraints the attacker actually faces.

## 2. Why the Naive Formula Fails

A tempting first formulation is:

NDC_effective = min-cut × P

Where:

- min-cut represents the number of structurally independent verification paths.
- P represents a general probability of verification.

This formulation is rejected.

It fails because it allows structural multiplicity to inflate operational security even when nobody verifies.

If a system has 3 verification paths but each path is almost never exercised, the architecture may look strong while the attacker faces almost no actual constraint.

This is especially dangerous in diffuse-harm environments, where each individual loss is too small to justify reconstruction.

Example:

- 200,000 affected parties.
- R$30 harm per person.
- 3 structural verification paths.
- Almost nobody reconstructs the decision envelope.

The naive formula can still produce a comforting number because it multiplies by structure.

But the real attacker does not face “3” constraints.

The attacker faces almost none.

## 3. Correct Object: Expected Binding Verification Constraints

For each independent verification path i:

- e_i = probability that path i is actually exercised.
- d_i = probability that falsification is detected if path i is exercised.

Then:

NDC_eff = Σ(e_i × d_i)

Interpretation:

NDC_eff is the expected number of verification constraints the attacker actually faces.

This keeps the unit of measurement aligned with NDC.

NDC is structural.

NDC_eff is operational.

Both are expressed in expected verification constraints, not merely in detection probability.

## 4. Why Not Use Pure Detection Probability?

Another possible formulation is:

P_detection = 1 - Π(1 - e_i × d_i)

This is valid as a detection probability.

But it is not in the same unit as NDC.

It produces a value between 0 and 1.

That makes it useful for probability-of-detection analysis, but not directly comparable to structural NDC.

EXP-003 needs a measure that can compare:

- what the architecture claims structurally, and
- what the attacker faces operationally.

For that reason, Σ(e_i × d_i) is the cleaner object.

## 5. Exercise Debt

Exercise Debt is the gap between structural NDC and effective NDC.

Exercise Debt = NDC - NDC_eff

Interpretation:

Exercise Debt is the amount of verifiability claimed by the architecture but not realized in practice.

If:

NDC = 3

and:

NDC_eff = 0.012

then:

Exercise Debt = 2.988

The system structurally advertises 3 independent verification constraints.

Operationally, the attacker faces only 0.012 expected constraints.

That gap is the overclaim.

## 6. Case Tests

### Case 1 — Diffuse Harm

Scenario:

- Many affected parties.
- Small individual loss.
- Low incentive to contest.
- Multiple structural verification paths exist.
- Almost nobody exercises them.

Assumptions:

- NDC = 3
- e_1 = 0.001
- e_2 = 0.001
- e_3 = 0.001
- d_1 = 0.9
- d_2 = 0.9
- d_3 = 0.9

Calculation:

NDC_eff = 0.001 × 0.9 + 0.001 × 0.9 + 0.001 × 0.9

NDC_eff = 0.0027

Result:

The structural architecture appears to provide 3 verification paths.

The operational reality provides almost no exercised verification.

Conclusion:

Structural NDC can dramatically overstate real-world contestability when incentives to reconstruct are weak.

### Case 2 — High-Stakes Individual Harm

Scenario:

- One affected party.
- Large individual loss.
- Strong incentive to contest.
- External verification path is likely to be exercised.

Assumptions:

- NDC = 1
- e_1 = 0.8
- d_1 = 0.95

Calculation:

NDC_eff = 0.8 × 0.95

NDC_eff = 0.76

Result:

Even with only one independent path, the attacker faces a substantial expected constraint because exercise is likely.

Conclusion:

A lower structural NDC may outperform a higher structural NDC if the lower-NDC case is actually exercised.

### Case 3 — Operator-Mediated False Multiplicity

Scenario:

- Five apparent verification paths exist.
- All are mediated by the same operator.
- Before exercise is modeled, the paths must be collapsed into one dependency cluster.

Incorrect calculation:

NDC = 5

NDC_eff = Σ(e_i × d_i) across five apparent paths

This is wrong.

Why:

If all five paths depend on the same operator, they are not independent verification paths.

The correct order is:

1. Collapse dependent paths conservatively.
2. Compute NDC on the collapsed graph.
3. Apply EXP-003 exercise modeling only after collapse.

Correct approach:

- Apparent paths: 5
- Collapsed independent paths: 1
- NDC = 1
- Then calculate NDC_eff using the exercised probability of that one independent path.

Conclusion:

EXP-003 is not a substitute for conservative dependency collapse.

It is a second filter applied after structural collapse.

Order matters.

### Case 4 — Strong Protocol, Weak Exercise

Scenario:

- Cryptographic detection is strong.
- Reconstruction tooling is available.
- Timestamping and signature verification are reliable.
- But users, auditors, and affected parties rarely verify.

Assumptions:

- d_i is high.
- e_i is low.

Result:

NDC_eff remains low.

Conclusion:

Cryptographic strength does not solve the behavioral problem.

A protocol can be technically strong and operationally weak if nobody exercises the verification right.

## 7. Methodological Rule

EXP-003 must never be used before dependency collapse.

The correct pipeline is:

1. Identify apparent verification paths.
2. Collapse operator-mediated or dependency-mediated paths.
3. Compute structural NDC.
4. Estimate or bound exercise probabilities.
5. Compute NDC_eff.
6. Report Exercise Debt.

This prevents EXP-003 from laundering false independence into apparent operational security.

## 8. Open Crack 1 — Correlated Exercise

The formula assumes independent exercise probabilities.

That assumption is often false.

In diffuse-harm cases, non-exercise may be caused by a shared structural condition:

- low individual incentive,
- lack of awareness,
- lack of legal support,
- high reconstruction cost,
- low expected recovery,
- collective apathy,
- procedural friction.

In those cases, exercise probabilities are positively correlated.

They are not independent coins.

A single common cause may suppress all verification paths at once.

Therefore:

NDC_eff = Σ(e_i × d_i)

should be treated as an optimistic upper bound when exercise is correlated.

A more realistic future model may need a common-cause adjustment or correlated exercise term.

EXP-003 does not solve that here.

It only exposes the problem.

## 9. Open Crack 2 — e_i Is Not Cryptographic

The detection term d_i may sometimes be estimated from protocol properties.

For example:

- signature verification,
- hash reconstruction,
- timestamp validation,
- Merkle proof verification,
- canonicalization reproducibility.

But e_i is different.

The probability that someone actually reconstructs a decision envelope is not a cryptographic property.

It is behavioral, economic, legal, institutional, and procedural.

It depends on:

- harm size,
- awareness,
- legal access,
- reconstruction cost,
- expected benefit,
- regulator capacity,
- class-action feasibility,
- technical literacy,
- tooling usability,
- institutional incentives.

Therefore EXP-003 is not currently a complete calculator.

It is a formal frame that reveals what must be measured.

The key contribution is not that e_i is known.

The key contribution is that NDC without e_i silently assumes exercise.

That assumption is false.

## 10. Contribution

EXP-003 formalizes a missing layer in contestability architecture.

It shows that security by contestability has two components:

1. Structural availability of independent verification paths.
2. Behavioral exercise of those paths.

A-DAP and NDC primarily address the first.

EXP-003 shows that the second is irreducible.

Cryptography can improve d_i.

Architecture can improve NDC.

But neither automatically improves e_i.

That makes exercise probability a first-class governance problem.

## 11. Relation to A-DAP

A-DAP creates reconstructible decision envelopes.

NDC measures independent verification structure.

EXP-003 asks whether those structures are actually exercised.

This prevents A-DAP from overclaiming.

A decision envelope that nobody reconstructs may still be valuable as latent evidence.

But latent evidence is not the same as exercised accountability.

EXP-003 preserves that distinction.

## 12. Safe Claim

The safe claim is:

A-DAP can increase structural verifiability.

NDC can describe independent verification structure.

EXP-003 shows that operational contestability also depends on whether independent verification paths are actually exercised.

Therefore, effective contestability requires both architecture and exercise.

## 13. Unsafe Claim

The unsafe claim is:

A-DAP guarantees accountability because multiple verification paths exist.

This is false.

Multiple paths do not guarantee exercise.

No exercise means low operational constraint.

Low operational constraint means high Exercise Debt.

## 14. Summary

NDC is the ceiling.

NDC_eff is the expected operational constraint.

Exercise Debt is the gap.

The central finding of EXP-003 is:

A system can be structurally contestable and operationally uncontested.

That gap is not a minor implementation detail.

It is a core part of the security model.
