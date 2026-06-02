# Adoption and Accessibility Risks

## Why reconstructibility does not automatically imply practical contestability

### Abstract

A-DAP improves the structural reconstructibility of high-impact automated decisions.

However, reconstructibility alone does not guarantee that affected people, public managers, courts, regulators, journalists, lawyers, or civil society organizations will be able to exercise verification in practice.

A decision envelope may be technically valid, cryptographically consistent, and externally reconstructible while still being difficult to understand, expensive to challenge, or inaccessible to the people most affected by the decision.

This note identifies four adoption and accessibility risks:

1. complexity as a barrier to adoption;
2. lack of concrete failure examples;
3. asymmetry of resources between affected parties and institutions;
4. NDC as an operationally immature metric.

The purpose is not to weaken A-DAP.

The purpose is to prevent A-DAP from becoming technically robust but socially underused.

---

## 1. Core Claim

A-DAP makes automated decisions more reconstructible.

It does not automatically make verification practically accessible.

A technically reconstructible decision may still be socially inaccessible if affected parties lack the tools, expertise, representation, time, institutional support, or legal pathways needed to exercise verification.

In short:

Reconstructibility is a structural condition.

Accessibility is an adoption condition.

Contestability requires both.

---

## 2. Complexity as a Barrier to Adoption

A-DAP contains concepts that are necessary for serious verification:

- decision envelopes;
- custody graphs;
- dependency collapse;
- NDC;
- input provenance;
- materiality assumptions;
- external reconstruction;
- proof surfaces;
- non-terminal verification;
- verifier funding capture;
- limitation-claim self-validation.

These concepts improve rigor.

But they also increase the barrier to entry.

A regulator, judge, public manager, journalist, lawyer, or affected person may not have time to read a long technical README or interpret an architecture-level discussion.

This creates an adoption risk.

A-DAP may become academically robust while remaining practically difficult to absorb.

This does not invalidate the protocol.

It means A-DAP needs multiple layers of presentation:

- a technical README for architects and reviewers;
- a regulator-facing brief;
- a legal-facing explanation;
- a citizen-facing explanation;
- executable examples;
- failure cases;
- plain-language verification outputs.

The technical architecture should not be simplified into false claims.

But the entry path must be simplified enough for institutions and affected people to begin using it.

---

## 3. Lack of Concrete Failure Examples

A-DAP repeatedly states that it does not prove truth, fairness, legality, or correctness.

That limitation is important.

But it becomes more understandable when shown through concrete failure examples.

For example:

An automated benefits system creates a valid A-DAP decision envelope.

The envelope includes:

- a canonicalized input commitment;
- a model or rule version;
- a decision output;
- a timestamp claim or timestamp evidence;
- a hash;
- reconstruction instructions.

Later, the envelope is reconstructed.

The hash matches.

The timestamp evidence is valid.

The decision record has not been altered.

The verifier concludes that the later explanation matches the committed decision record.

However, the decision may still be wrong or unjust if:

- the original input was false;
- the input was incomplete;
- the applicant’s documents were incorrectly captured;
- the rule itself was unlawful;
- the model encoded a discriminatory policy;
- the threshold was legally inappropriate;
- the system used outdated information;
- the person had no meaningful opportunity to correct the input.

In this case, A-DAP helps establish what the system committed to doing.

It does not prove that what the system committed to doing was right.

This example is important because it prevents a common overclaim:

Hash verified, therefore the decision is correct.

A safer interpretation is:

The checked record matches the committed evidence within the declared verification scope.

The dispute may then move to input truth, legal validity, procedural fairness, policy design, or institutional remedy.

---

## 4. Asymmetry of Resources

A-DAP improves the structure of evidence.

But evidence still has to be exercised.

A person affected by an automated decision may not have:

- technical expertise;
- legal representation;
- access to a verifier;
- knowledge of hashing or signatures;
- access to the relevant envelope;
- access to reconstruction tools;
- time to challenge the decision;
- money to hire specialists;
- institutional support;
- ability to interpret the result.

This creates a practical asymmetry.

The institution may control the system, the records, the interface, the notice, the explanation, the appeal procedure, and the resources needed to contest the decision.

The affected person may receive only a denial, a notice, a reason code, or a partial explanation.

A-DAP does not automatically eliminate this asymmetry.

A citizen verifier can reduce the barrier, but it does not remove the need for:

- public-interest verifiers;
- legal aid;
- regulators;
- ombuds institutions;
- courts;
- independent auditors;
- civil society organizations;
- usable interfaces;
- exportable evidence packages;
- plain-language explanations of verification scope.

This means A-DAP should not be framed as:

The citizen can verify everything alone.

A safer claim is:

A-DAP can create evidence that affected people, representatives, regulators, or independent reviewers may use to contest a decision under stated assumptions.

The social value of A-DAP depends on whether verification becomes exercisable, not merely possible.

---

## 5. The External Verifier Problem

A-DAP often requires some party outside the original decision system to reconstruct or test
