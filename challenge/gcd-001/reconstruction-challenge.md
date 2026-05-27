# GCD-001 Reconstruction Challenge

This document defines the planned public reconstruction challenge for **GCD-001**, the first public A-DAP/NDC external reconstruction target.

GCD-001 is a candidate public reconstruction package prepared for independent adversarial review.

At the current stage:

- external disjoint reconstruction is **pending**;
- Acceptance Committee is **not yet appointed**;
- public bounty is **not yet active**;
- submission channel is **not yet open**.

This document defines the intended challenge structure.

It does not imply that the challenge is already active.

---

## 1. Challenge Summary

The GCD-001 Reconstruction Challenge asks external reviewers to test whether the published GCD-001 custody/NDC claim can be:

- independently reproduced;
- constructively falsified;
- shown to be structurally ambiguous.

The purpose is not to prove that A-DAP is correct.

The purpose is to expose a specific public custody/NDC claim to independent reconstruction pressure.

---

## 2. Object of the Challenge

The object of the challenge is the published **GCD-001 decision-custody/NDC claim**.

Participants are asked to:

- reconstruct the decision-custody graph;
- inspect the declared evidence structure;
- identify oracle-bound claims;
- compute or challenge the claimed Network Dependency Coefficient;
- determine whether the published claim qualifies as R1, R2, or R3.

The expected posture is:

```text
Do not trust the author.
Reconstruct the graph.
Compute the cut.
Challenge the NDC claim.
Declare the oracle boundary.
```

---

## 3. Current Status

Status: **candidate challenge package**.

Formal challenge: **not yet active**.

Acceptance Committee: **not yet appointed**.

Public bounty: **not yet active**.

Submission channel: **not yet open**.

No result should be described as independently accepted until evaluated by a non-author committee under published challenge rules.

---

## 4. Eligible Outcomes

A valid submission must declare one of three admissible outcomes:

- **R1 — Reproduction**
- **R2 — Falsification**
- **R3 — Structural Ambiguity**

All three outcomes are useful.

The purpose of the challenge is not to force confirmation.

The purpose is to make confirmation, falsification, and ambiguity all admissible and inspectable.

---

## 5. R1 — Reproduction

A submission qualifies as **R1 — Reproduction** if the participant independently reproduces the claimed GCD-001 NDC under the published specification.

R1 means:

```text
The specific GCD-001 NDC claim was reproduced under the published specification.
```

R1 does not mean:

- the original decision was true;
- the original decision was fair;
- the original decision was lawful;
- A-DAP as a whole is validated;
- the author’s solver is authoritative.

A valid R1 submission should include:

- independent reconstruction method;
- reconstructed graph;
- vertex list;
- edge list;
- min-cut calculation;
- NDC estimate;
- oracle-boundary analysis;
- reproducibility instructions;
- independence declaration.

---

## 6. R2 — Falsification

A submission qualifies as **R2 — Falsification** if the participant shows that the claimed GCD-001 NDC is incorrect.

R2 requires a constructive demonstration.

Valid R2 findings may include:

- a smaller valid vertex-cut;
- an invalid edge assumption;
- an invalid vertex classification;
- an oracle-bound claim incorrectly counted as verified;
- a graph reconstruction that contradicts the claimed NDC;
- an error in the NDC calculation method;
- a dependency path omitted by the published graph.

R2 is structurally valuable.

A successful falsification improves the protocol and should not be treated as a failure of the challenge.

---

## 7. R3 — Structural Ambiguity

A submission qualifies as **R3 — Structural Ambiguity** if the published specification is incomplete or ambiguous enough to prevent deterministic reconstruction.

Valid R3 findings may include ambiguity in:

- canonicalization;
- artifact availability;
- graph vertices;
- graph edges;
- A/V role assignment;
- oracle-boundary classification;
- NDC calculation;
- minimum vertex-cut reasoning;
- dependency interpretation.

A valid R3 submission should show how the ambiguity affects the reconstruction.

If possible, it should demonstrate two or more materially different reconstructions permitted by the current specification.

---

## 8. Submission Requirements

A valid submission should include:

1. **Declared outcome**

   One of:

   - R1 — Reproduction
   - R2 — Falsification
   - R3 — Structural Ambiguity

2. **Technical note**

   A 2–5 page explanation of the result.

3. **Independent reconstruction code**

   Any language is acceptable.

   The author’s solver must not be used as the primary computation path.

4. **Graph representation**

   Accepted formats include:

   - JSON
   - CSV
   - DOT
   - GraphML
   - Mermaid
   - image
   - table
   - other inspectable format

5. **Min-cut calculation memo**

   The participant must explain:

   - graph model used;
   - source condition;
   - target condition;
   - detection condition;
   - candidate cuts tested;
   - minimum sufficient vertex-cut;
   - NDC estimate.

6. **Oracle-boundary analysis**

   The participant must identify which claims are reconstructible and which remain oracle-bound.

7. **Reproducibility instructions**

   Another reviewer should be able to inspect or reproduce the submission.

8. **Independence declaration**

   The participant must disclose whether any author-provided tools were used.

---

## 9. Independent Implementation Requirement

Participants must not rely on the author’s solver, scripts, expected outputs, private infrastructure, or manually asserted conclusions for the primary reconstruction.

Author-provided tools may be used only for secondary comparison after independent reconstruction has been completed.

A submission that merely runs the author’s solver is not an independent reconstruction.

A submission that treats expected output as proof is not an independent reconstruction.

---

## 10. Prohibited Primary Dependencies

The primary reconstruction must not depend on:

- the author’s solver;
- the author’s scripts;
- expected output files generated by the author;
- private infrastructure controlled by the author;
- undocumented assumptions;
- manually asserted conclusions by the author.

Use of author-provided tools for secondary comparison is allowed only if disclosed.

---

## 11. Acceptance Committee

No Acceptance Committee has been publicly appointed yet.

Until such committee is named, no submission should be described as independently accepted.

The intended committee structure is:

- three publicly named external reviewers;
- no voting power for the protocol author;
- skeptical interpretation prevails in case of disagreement.

The committee should classify submissions as:

- accepted R1;
- accepted R2;
- accepted R3;
- administratively incomplete;
- technically insufficient;
- outside scope;
- non-reproducible.

---

## 12. Author Non-Voting Rule

The protocol author has no voting power over technical acceptance.

The author may clarify:

- file locations;
- repository structure;
- submission logistics;
- published definitions;
- administrative completeness.

The author must not decide:

- whether R1 was successfully reproduced;
- whether R2 falsifies the claim;
- whether R3 establishes structural ambiguity;
- whether the submission is technically accepted.

This rule prevents adversarial validation from becoming self-validation with extra steps.

---

## 13. Administrative Validity Check

Before technical review, a submission may be checked for administrative completeness.

A submission is administratively valid if it includes:

- declared outcome;
- reviewer identity or pseudonym;
- independence declaration;
- materials reviewed;
- reconstruction method;
- graph representation;
- min-cut calculation memo;
- oracle-boundary analysis;
- technical note;
- reproducibility instructions;
- public disclosure preference.

Administrative validity does not imply technical acceptance.

---

## 14. Public Bounty Status

Public bounty status: **not yet active**.

Any prize structure described here is provisional until a formal public notice defines:

- opening date;
- closing date;
- prize values;
- submission channel;
- committee members;
- review procedure;
- payment conditions;
- public disclosure procedure.

No bounty should be considered active until these conditions are published.

---

## 15. Proposed Prize Structure

The following structure is proposed for the future public challenge.

It is not active yet.

### R1 — Reproduction

Proposed recognition:

- public credit as independent verifier;
- optional citation in follow-up documentation;
- optional acknowledgement in future paper or technical note.

### R2 — Falsification

Proposed recognition:

- higher reward priority;
- public credit as protocol falsifier;
- potential co-authorship or acknowledgement in corrective protocol note, depending on contribution.

R2 should be treated as structurally more valuable than R1 because falsification reveals where the protocol or claim must improve.

### R3 — Structural Ambiguity

Proposed recognition:

- public credit for identifying underspecification;
- acknowledgement in future specification correction;
- possible contribution credit in the next version of the reconstruction package.

R3 is valuable because ambiguity correction strengthens the protocol.

---

## 16. Suggested Bounty Weights

If a monetary bounty is activated later, the suggested weighting is:

```text
R1 — lower reward
R2 — highest reward
R3 — medium reward
```

The reason is structural:

- R1 confirms reproducibility under the published specification;
- R2 exposes incorrect claims;
- R3 exposes specification weaknesses.

A good challenge should reward falsification more than confirmation.

---

## 17. Challenge Timeline

Formal timeline: **not yet active**.

When activated, the challenge notice should define:

- opening date;
- closing date;
- review period;
- committee decision deadline;
- public disclosure date.

Recommended duration:

```text
90 days from public activation.
```

The 90-day period should begin only after:

- challenge materials are complete;
- submission channel is open;
- committee members are named;
- bounty terms, if any, are published.

---

## 18. Submission Channel

Submission channel: **not yet open**.

Possible future channels include:

- GitHub Issues;
- GitHub Pull Requests;
- email submission;
- external form;
- private submission to committee.

The official channel must be declared before the challenge becomes active.

Submissions sent before the official channel is declared should not be treated as formally accepted challenge submissions.

---

## 19. Public Disclosure

After the formal challenge closes, the repository should disclose:

- number of submissions received;
- number of administratively valid submissions;
- number of accepted R1 outcomes;
- number of accepted R2 outcomes;
- number of accepted R3 outcomes;
- number of invalid or incomplete submissions;
- committee decision summary;
- unresolved ambiguities;
- specification changes triggered by the challenge.

No result should be described as full validation of A-DAP.

---

## 20. Empty Challenge Clause

If no valid external reconstruction is submitted, the challenge does not validate the GCD-001 claim.

It only means that no qualifying external reconstruction was submitted within the challenge period.

Silence must not be represented as confirmation.

A future challenge, direct outreach, workshop review, or independent audit may still be required.

---

## 21. Legal and Ethical Notes

Participants should not submit:

- private data;
- confidential third-party material;
- unauthorized credentials;
- personal information not required for review;
- claims that cannot be publicly inspected.

Participants should focus on the published GCD-001 materials and the reconstruction claim.

The challenge is about verifiability, reconstruction, falsification, ambiguity, and oracle boundaries.

It is not a request to attack live systems or private infrastructure.

---

## 22. What the Challenge Does Not Prove

The challenge does not prove:

- that the original decision was true;
- that the original decision was fair;
- that the original decision was lawful;
- that the model actually executed the decision;
- that the input was true in the real world;
- that A-DAP as a whole is validated;
- that NDC is a complete governance metric.

The challenge tests a narrower claim:

```text
whether the published GCD-001 custody/NDC claim can be independently reconstructed, falsified, or shown to be structurally underspecified.
```

---

## 23. Minimal Honest Claim

If R1 is accepted, the honest claim is:

```text
The GCD-001 NDC claim was reproduced under the published specification.
```

If R2 is accepted, the honest claim is:

```text
The GCD-001 NDC claim was falsified through a constructive demonstration.
```

If R3 is accepted, the honest claim is:

```text
The GCD-001 specification requires correction before deterministic reconstruction is possible.
```

All three outcomes are useful.

None of them should be described as full validation of A-DAP.

---

## 24. Final Principle

The challenge does not ask for trust.

It asks for reconstruction.

It does not protect the author.

It exposes the claim.
