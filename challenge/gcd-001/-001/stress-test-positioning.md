# GCD-001 Stress Test Positioning

This document defines the intended role of GCD-001 within A-DAP.

GCD-001 is not presented as proof that A-DAP is complete.

GCD-001 is a controlled reconstruction challenge designed to test whether a third party can reconstruct and inspect a committed decision object under declared assumptions.

That is valuable, but it is not enough.

A-DAP requires a distinction between two different properties:

1. Reproducibility
2. Adversarial contestability

A reconstruction test without an adversarial divergence test may prove that the procedure is documented and deterministic.

It does not, by itself, prove structural separability.

This distinction is essential.

A-DAP must not become the kind of strengthened documentation system it was designed to critique.

---

## 1. Why GCD-001 Exists

GCD-001 uses the German Credit Dataset as a practical test environment for A-DAP concepts.

The dataset is useful because it is:

- known
- simple enough for external reviewers
- connected to a high-impact domain
- suitable for decision reconstruction
- suitable for testing commitments, hashes, policies, inputs, outputs, and verification procedures
- non-sensitive enough for public experimentation

The purpose of GCD-001 is not to claim that credit decisions become fair, lawful, or correct.

The purpose is narrower:

to test whether a committed decision object can be reconstructed and challenged under declared assumptions.

---

## 2. The Core Limitation

A third party may successfully reconstruct an envelope and still only prove procedural reproducibility.

That means:

- the specification was understandable
- the reconstruction steps were deterministic
- the artifacts were sufficiently documented
- the reviewer could reproduce the expected object

This is necessary for A-DAP.

But it is not sufficient.

A-DAP is not only about whether a third party can reconstruct a known-good envelope.

A-DAP is about whether a third party can detect inconsistency when the operator is treated as adversarial.

The stronger question is:

Can a third party detect a divergence without relying on cooperation from the operator-controlled environment?

---

## 3. Two Distinct Properties

GCD-001 must distinguish between two properties.

### 3.1 Reproducibility

Reproducibility asks:

Can a third party reconstruct the committed decision object under declared assumptions?

This tests whether the procedure is:

- clear
- deterministic
- sufficiently documented
- externally executable
- reproducible from the provided artifacts

A pass in reproducibility means the reconstruction procedure works under the declared conditions.

It does not prove structural separability.

It does not prove that the operator cannot control inscription.

It does not prove that omission or selective commitment would be detected.

It does not prove that verification is independent.

It only proves that the declared reconstruction procedure can be followed.

### 3.2 Adversarial Contestability

Adversarial contestability asks:

Can a third party detect an injected divergence without relying on cooperation from the operator?

This tests whether the evidentiary object can expose inconsistency when something has been altered, substituted, omitted, delayed, regenerated, or mismatched.

A pass in adversarial contestability means the procedure detected at least one class of material divergence.

A failure in adversarial contestability identifies a control vector where the custody graph may collapse.

This is closer to the real A-DAP thesis.

---

## 4. Necessary but Not Sufficient

Reproducibility is a necessary condition for A-DAP.

Without reproducibility, the evidentiary object cannot be independently reconstructed.

But reproducibility alone is not sufficient.

A perfectly reproducible procedure can still be operator-controlled.

A well-documented envelope can still be self-attested.

A deterministic reconstruction can still depend on artifacts selected by the operator.

A third-party reviewer can still reproduce only what the operator chose to expose.

Therefore:

Success in GCD-001 Phase 1 is not evidence of structural separability by itself.

It is evidence that the reconstruction procedure is externally executable under declared assumptions.

A-DAP requires an additional adversarial phase.

---

## 5. Phase 1 — Reconstruction Test

Phase 1 tests procedural reproducibility.

The reviewer receives:

- the declared decision envelope
- the reconstruction specification
- the relevant input commitment
- the relevant output commitment
- the declared policy or model reference
- the canonicalization method
- the hash or commitment method
- the verification rules
- the expected reconstruction path

The reviewer attempts to reconstruct the committed decision object.

The reviewer should report:

- whether the reconstruction succeeded
- which artifacts were used
- which assumptions were required
- whether the hash or commitment matched
- whether any metadata was missing
- whether the procedure was deterministic
- whether the procedure depended on operator-controlled tools or interfaces

A successful Phase 1 result means:

The reconstruction procedure is sufficiently documented and deterministic under declared assumptions.

It does not mean:

- A-DAP is complete
- the decision was fair
- the decision was correct
- the custody graph is structurally separable
- the operator cannot manipulate inscription
- the verification path is independent

Phase 1 is a reproducibility test, not a full contestability test.

---

## 6. Phase 2 — Adversarial Divergence Test

Phase 2 tests adversarial contestability.

The reviewer receives one or more altered artifacts.

The alteration may involve:

- post-commit input substitution
- output substitution
- policy version mismatch
- model version mismatch
- altered reconstruction metadata
- inconsistent hash commitment
- altered timestamp evidence
- delayed inscription evidence
- regenerated envelope
- altered canonicalization claim
- invalid signature reference
- verifier-output inconsistency
- missing or suppressed artifact
- selective disclosure of records

The reviewer attempts to detect the divergence using the declared reconstruction and verification procedure.

The reviewer should report:

- whether a divergence was detected
- which verification step exposed the divergence
- which artifact failed validation
- whether the failure was cryptographic, procedural, custody-based, or interpretive
- whether detection required cooperation from the operator
- whether detection required access to an operator-controlled dashboard
- whether detection could be reproduced independently
- whether the failure identifies a material control vector

A successful Phase 2 result means:

The procedure can detect at least one adversarial inconsistency without relying on the operator as the final authority.

A failed Phase 2 result means:

The procedure did not expose the injected inconsistency under the available assumptions.

This failure is useful.

It identifies where A-DAP still depends on hidden assumptions, incomplete custody, unclear materiality, or a non-independent verification path.

---

## 7. Phase 3 — Blinded Adversarial Variant

Phase 3 is the stronger future form of GCD-001.

In the blinded adversarial variant, the reviewer receives a mixed package containing valid and altered artifacts.

The reviewer is not told:

- which artifacts are valid
- which artifacts are altered
- where the alteration was introduced
- whether there is one alteration or multiple alterations
- whether the package contains no alteration at all

The reviewer must:

- reconstruct the decision object
- identify whether any divergence exists
- locate the divergence
- explain which verification step exposed it
- document any assumptions required
- classify the divergence type
- report whether detection was independent of the operator

This is stronger than ordinary reconstruction.

It tests whether the A-DAP procedure detects adversarial inconsistency rather than merely reproducing a known-good envelope.

---

## 8. Why Blinding Matters

If the author creates the test, injects the divergence, defines the detection rule, and declares success, the experiment remains partly self-attested.

That does not make it useless.

It makes it a demonstration, not independent validation.

Author-generated adversarial variants are useful for:

- demonstrating the procedure
- showing expected failure modes
- teaching reviewers how divergence appears
- testing whether the verifier catches obvious inconsistencies
- building early examples

But they should not be overstated.

Independent validation requires one of the following:

- third-party-generated divergence cases
- blinded challenge packages
- independent reviewers who do not know which artifacts were altered
- independent reproduction of the custody graph and verification result
- adversarial review of the materiality assumptions

Without blinding or third-party divergence generation, GCD-001 remains an internal stress test.

That is still valuable.

But it should not be presented as independent proof of separability.

---

## 9. Relation to NDC

GCD-001 connects to NDC analysis through the custody graph.

A reconstruction test asks whether the procedure can be reproduced.

An adversarial divergence test asks whether a relevant inconsistency can be detected without depending on the operator.

If the divergence is detected through an independent path, that may support a stronger NDC claim for that specific path and threat model.

If the divergence is not detected, the failure helps identify the minimum dependency cut.

In practical terms:

A Phase 1 pass supports procedural reproducibility.

A Phase 2 pass supports adversarial contestability for the tested divergence class.

A Phase 3 pass supports stronger external testability under blinded conditions.

None of these results should be generalized beyond the declared scope.

Each result must be tied to:

- the custody graph
- the materiality model
- the divergence class
- the verification path
- the assumptions used
- the artifacts available to the reviewer

---

## 10. What GCD-001 Can Show

GCD-001 can show that:

- a decision envelope can be reconstructed
- a reconstruction specification can be followed
- a hash or commitment can be checked
- a declared output can be compared against a committed object
- some divergences can be detected
- some custody assumptions are explicit
- some hidden dependencies can be exposed
- reviewers can identify where the procedure fails

These are valuable results.

They make A-DAP more testable.

They do not make A-DAP complete.

---

## 11. What GCD-001 Cannot Show

GCD-001 cannot show that:

- A-DAP is complete
- A-DAP proves decision truth
- A-DAP proves fairness
- A-DAP proves legal compliance
- A-DAP eliminates trust
- A-DAP eliminates collusion risk
- A-DAP guarantees accountability
- A-DAP detects every possible alteration
- the German Credit Dataset represents real credit governance
- a successful reconstruction proves structural separability
- author-generated adversarial cases are independent validation

These limits must remain explicit.

---

## 12. Safe Claim

The safe claim for GCD-001 is:

GCD-001 is a reconstruction challenge for testing whether a third party can reproduce a committed decision object under declared assumptions.

When extended with adversarial divergence cases, it can also test whether specific classes of inconsistency are detectable without relying on the operator as the final authority.

Success in reconstruction alone is a necessary condition for A-DAP, not sufficient evidence of structural separability.

Failure is not merely a negative result.

Failure identifies where custody, materiality, reconstruction, or verification assumptions remain too weak.

---

## 13. Stronger Claim for GCD-001B

The stronger claim for a blinded adversarial variant is:

GCD-001B tests whether third-party reviewers can detect injected divergences in a mixed package without being told where the divergence exists.

This tests adversarial contestability more directly than ordinary reconstruction.

Even then, the result remains scoped to the tested divergence class, custody graph, materiality model, and verification assumptions.

---

## 14. Recommended Challenge Structure

The recommended challenge structure is:

### Phase 1 — Known-Good Reconstruction

Reviewer reconstructs a valid committed decision object.

Purpose:

Test reproducibility.

### Phase 2 — Known Divergence Detection

Reviewer receives altered artifacts and attempts to detect inconsistency.

Purpose:

Test adversarial contestability in a demonstrative setting.

### Phase 3 — Blinded Divergence Detection

Reviewer receives a mixed package and must determine whether divergence exists.

Purpose:

Test stronger contestability without prior knowledge of the altered artifact.

### Phase 4 — Third-Party Divergence Generation

An external reviewer creates new divergence cases.

Purpose:

Reduce author self-attestation and test whether the procedure survives adversarial external challenge.

---

## 15. Evaluation Matrix

| Phase | Main Question | Property Tested | Strong Result | Limitation |
| --- | --- | --- | --- | --- |
| Phase 1 | Can the object be reconstructed? | Reproducibility | Procedure is deterministic and documented | Does not prove separability |
| Phase 2 | Can an injected divergence be detected? | Adversarial contestability | Specific inconsistency is detectable | May still be author-generated |
| Phase 3 | Can divergence be detected blindly? | Blinded contestability | Reviewer detects inconsistency without knowing where it is | Still scoped to provided package |
| Phase 4 | Can external parties generate new attacks? | External adversarial review | Procedure survives third-party challenge | Requires independent participation |

---

## 16. Failure Interpretation

Failures should be classified, not hidden.

Possible failure classes include:

- unclear reconstruction specification
- missing artifact
- ambiguous canonicalization
- hash mismatch without explainable cause
- operator-controlled verification path
- insufficient custody graph
- materiality ambiguity
- unverifiable timestamp claim
- selective disclosure risk
- altered artifact not detectable
- reviewer unable to reproduce expected result
- detection requires operator cooperation
- detection depends on an operator-controlled dashboard
- divergence class outside declared scope

Each failure should be treated as diagnostic evidence.

A-DAP becomes stronger when failures reveal the exact place where dependency remains hidden.

---

## 17. Boundary Against Compliance Theater

A reconstruction-only challenge can be misused.

A vendor could say:

“Our envelope is reproducible, therefore our system is A-DAP compliant.”

That would be an overclaim.

Reproducibility is not the same as separability.

Documentation is not the same as contestability.

External review of a known-good package is not the same as adversarial detection.

A-DAP should reject this collapse.

The correct position is:

A system that passes reconstruction testing but fails adversarial divergence testing has demonstrated documentation quality, not structural contestability.

---

## 18. Canonical Distinction

The canonical distinction for GCD-001 is:

Reproducibility means a third party can reconstruct the committed object.

Contestability means a third party can detect a relevant divergence without relying on the operator as the final authority.

Separability requires more than reproducibility.

It requires that detection not collapse into the same material control domain as the decision, inscription, preservation, or verification path.

---

## 19. Final Position

GCD-001 is valuable because it makes A-DAP testable.

But its value depends on honest scope.

GCD-001 Phase 1 tests reconstruction.

GCD-001 Phase 2 tests detection of declared adversarial divergence.

GCD-001 Phase 3 tests blinded adversarial contestability.

GCD-001 Phase 4 tests external adversarial generation.

Only the later phases begin to test the stronger A-DAP claim.

The project should therefore present GCD-001 as a staged stress test, not as final proof.

The strongest result is not a perfect pass.

The strongest result is a test structure that reveals exactly where A-DAP still depends on trust.
