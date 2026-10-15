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

A valid submission must propose one of three technical outcomes for each claim and reviewed version, or state that evidence is insufficient to propose a technical classification:

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

A submission qualifies as **R3 — Structural Ambiguity** for a specific claim and reviewed repository version only if the gap is decisive. It must show at least one admissible completion of the missing artifact or undefined rule under which the claim holds and at least one admissible completion under which it fails (for example, NDC > 1 versus NDC ≤ 1).

If the claim holds under every admissible completion, R1 requires positive, independent, inspectable reproduction evidence; absence of a counterexample is not reproduction. If it fails under every admissible completion, R2 requires constructive, independently checkable falsification. Failure to confirm R3 does not imply R1 or R2. An indeterminate graph element that does not change the claim’s outcome is recorded as a specification note, not R3.

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

A valid R3 submission must identify the exact missing artifact or undefined rule, delimit the admissible completions by the reviewed materials and stated assumptions, and give independently checkable reasoning showing the effect on the reconstruction and claim outcome. R3 acceptance requires at least two materially different admissible reconstructions or completions: one under which the claim holds and one under which it fails. If an absent artifact prevents constructing complete alternatives, demonstrate how admissible completions of that artifact can still change the claim’s outcome. The affected graph, edge, cut, or NDC may be marked **not determinable** only with this evidence; do not invent a graph or cut to fill the gap.

Every R3 finding must state a remediation condition: the specific artifact to supply or rule to define that would make the claim determinable.

R3 concerns a specification-level blocker, not a reviewer’s operational difficulty. A transient access or environment failure, timeout, unavailable compute resource, or incomplete submission is not R3 by itself. Record operational failures and retry where reasonable; classify a materially incomplete submission as administratively incomplete. A required artifact missing from the published challenge package, or an undefined rule needed for reconstruction, may support R3 when its effect is demonstrated.

R1, R2, or R3 applies to each identified claim under review at a stated repository release/version or commit. A submission may report different outcomes for different claims; do not classify A-DAP as a whole from one claim.

---

## 8. Submission Requirements

A valid submission should include:

1. **Submitter-proposed outcome**

   For each claim and reviewed version, propose one of:

   - R1 — Reproduction
   - R2 — Falsification
   - R3 — Structural Ambiguity

   The submitter may instead state that evidence is insufficient to propose a technical classification. This proposal is not a committee decision or acceptance.

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

5. **Graph and cut analysis**

   For a determinable graph/cut, explain:

   - graph model used;
   - source condition;
   - target condition;
   - detection condition, or, for a proposed R3, its decisive undefinedness with bounded admissible alternatives, independently checkable different claim outcomes, and remediation condition;
   - alteration condition, or, for a proposed R3, its decisive undefinedness with bounded admissible alternatives, independently checkable different claim outcomes, and remediation condition;
   - candidate cuts tested where determinable, or, for a proposed R3, bounded admissible alternatives and independently checkable reasoning showing how the decisive gap changes the claim outcome;
   - minimum sufficient vertex-cut and why no smaller cut is sufficient;
   - NDC estimate.

   If a missing artifact or undefined rule is proposed as R3, mark the affected graph or cut **not determinable** only after identifying the decisive gap, delimiting admissible alternatives, and providing independently checkable reasoning that alternatives produce different claim outcomes. State the remediation condition. Provide sufficiency and minimality reasoning whenever a minimum cut is claimed.

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

The committee, when appointed, must consist of three publicly named external reviewers and must pre-name at least one alternate reviewer.

Each committee member and alternate must provide the same independence and relationship disclosure required of submitters, including relationships with the author, repository owner, affiliated organizations, and challenge sponsor. A member with a disclosed conflict for a submission must recuse, and a pre-named alternate replaces that member for that submission.

For each claim, members must first vote separately on evidence sufficiency: whether the submitted evidence is sufficient for R1, whether it is sufficient for R2, and, for each claimed gap, whether the gap exists and whether it is decisive. These are yes/no votes. Members then vote one provisional technical classification (R1, R2, or R3). An absolute majority (2 of 3) is required for every adopted finding. No abstentions are allowed; a member who cannot decide must state why in the decision note and still cast a vote.

Apply this precedence:

1. **R2:** Accept R2 only with majority support for sufficient, constructive, independently checkable falsification. If the result depends on an admissible completion of a claimed gap, the falsification must hold under every admissible completion to take precedence over R3.
2. **R3:** Otherwise, accept R3 only if a majority confirms both that the gap exists and is decisive under §7, with bounded, independently checkable admissible completions producing different outcomes and a stated remediation condition.
3. **R1:** Otherwise, accept R1 only with majority support for sufficient, positive, independent reproduction. If admissible completions are relevant, the claim must hold under every such completion. Failure to establish R2 or R3 is not evidence for R1.
4. **Not accepted (unresolved):** If none of these evidentiary conditions receives the required majority, record the claim as **not accepted (unresolved)**, never as R1.

If the initial R1/R2/R3 classification votes split with no majority, hold two separate binary votes, without abstention:

(a) Is the claimed gap established and decisive under §7? A “yes” requires a majority on both gap existence and decisiveness. If yes, classify R3 unless R2’s constructive falsification holds under every admissible completion, in which case classify R2.

(b) If a majority does not confirm both the existence and decisiveness of the gap, decide between R1 and R2 only if the corresponding positive evidence-sufficiency vote has a majority. The absence of a majority for R3 does not imply R1 or R2. If neither R1 nor R2 has sufficient evidence by majority, record **not accepted (unresolved)**. Rejection of a gap allegation is not evidence for either R1 or R2.

“Unresolved disagreement” means no absolute majority after this procedure. A member’s inability to decide is explained in the decision note, not treated as an abstention. A minority dissent is published but does not change the classification.

Decision hierarchy:

```text
R2 over R1 when constructive falsification is valid.
R2 over R3 when constructive falsification holds under every admissible reading.
R3 over R1 only when a gap is established and decisive under §7.
Invalid over R1 when independence or reproducibility is missing.
```

For worked examples of the four outcomes and unresolved evidence, see §28 of `reviewer-guidelines.md`.

The protocol author has no vote on whether R1, R2, or R3 is technically accepted, or whether a gap is material. The author may clarify published terminology and administrative logistics only.

The committee’s disposition for each claim/version must be recorded separately from the submitter’s proposal:

- accepted R1;
- accepted R2;
- accepted R3;
- not accepted (unresolved);
- administratively incomplete;
- technically insufficient;
- outside scope;
- non-reproducible.

“Not accepted (unresolved)” means no technical classification obtained the required majority evidence; it is distinct from administrative incompleteness. “Technically insufficient” may describe the evidence basis, but it does not replace the required claim disposition of “not accepted (unresolved)” when no classification is established.

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
- whether a claimed gap exists or is decisive;
- whether the submission is technically accepted.

This rule prevents adversarial validation from becoming self-validation with extra steps.

---

## 13. Administrative Validity Check

Before technical review, a submission may be checked for administrative completeness.

A submission is administratively valid if it includes:

- proposed outcome (R1/R2/R3) for each claim and reviewed version, or a statement that evidence is insufficient to propose a technical classification;
- reviewer identity or pseudonym;
- independence declaration;
- materials reviewed;
- reconstruction method;
- graph representation, or for a proposed R3, affected graph fields marked “not determinable” with the decisive gap, outcome-divergent admissible completions, and independently checkable reasoning;
- vertex and edge lists, or for a proposed R3, each affected field marked “not determinable” with that same decisive-gap evidence;
- min-cut calculation memo, or for a proposed R3, the decisive gap and admissible completions demonstrating different claim outcomes; whenever a minimum cut is claimed, include sufficiency and minimality reasoning;
- candidate cuts tested where determinable, or the same decisive-gap evidence for proposed R3;
- detection and alteration conditions defined, or, for a proposed R3, their decisive undefinedness, bounded admissible alternatives, different claim outcomes, and remediation condition;
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

After the formal challenge closes, the repository must disclose:

- number of submissions received;
- number of administratively valid submissions;
- number of accepted R1 outcomes;
- number of accepted R2 outcomes;
- number of accepted R3 outcomes;
- number of invalid or incomplete submissions;
- each committee member’s vote and short reasoning for each claim, including dissents and votes on the existence and decisiveness of each claimed gap;
- any conflicts, recusals, and alternate substitutions;
- unresolved ambiguities;
- specification changes triggered by the challenge.

Aggregate counts alone are insufficient.

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
