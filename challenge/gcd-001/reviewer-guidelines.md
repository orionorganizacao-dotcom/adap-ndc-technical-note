# GCD-001 Reviewer Guidelines

This document provides guidance for reviewers evaluating submissions to the **GCD-001 External Reconstruction Package**.

GCD-001 is a candidate public reconstruction package prepared for independent adversarial review.

At the current stage:

- external disjoint reconstruction is **pending**;
- Acceptance Committee is **not yet appointed**;
- public bounty is **not yet active**;
- submission channel is **not yet open**.

These guidelines define the intended evaluation standard for future external review.

They do not imply that any submission has already been independently accepted.

---

## 1. Reviewer Role

The reviewer’s role is not to defend A-DAP.

The reviewer’s role is to test whether the GCD-001 custody/NDC claim can be:

- independently reproduced;
- constructively falsified;
- shown to be structurally ambiguous.

The reviewer should evaluate the submission according to the published specification, not according to the author’s intent.

The expected posture is:

```text
skeptical by default
```

---

## 2. Core Principle

```text
Do not trust the author.
Reconstruct the graph.
Compute the cut.
Challenge the NDC claim.
Declare the oracle boundary.
```

A reviewer must not treat any author-provided material as authoritative merely because it appears in the repository.

The repository provides reconstruction inputs.

The review process determines whether those inputs support an independently reproducible claim.

---

## 3. Scope of Review

The reviewer is evaluating a specific public custody/NDC claim.

The reviewer is not evaluating:

- whether A-DAP as a whole is correct;
- whether A-DAP is commercially useful;
- whether the original decision was true;
- whether the original decision was fair;
- whether the original decision was lawful;
- whether the dataset was appropriate;
- whether the model actually executed the decision;
- whether the declared actor had institutional authority;
- whether NDC is a complete governance metric.

The central review question is:

```text
Can the published GCD-001 decision-custody/NDC claim be independently reconstructed, falsified, or shown to be structurally underspecified?
```

---

## 4. Current Status Constraint

At the current stage:

```text
committee pending
bounty not active
external reconstruction pending
submission channel not open
```

Therefore, reviewers must not describe any result as:

- independently accepted;
- bounty-winning;
- committee-approved;
- externally validated;
- peer-reviewed;
- final validation of A-DAP.

Until a non-author Acceptance Committee is publicly named and review rules are active, all evaluations remain preliminary unless otherwise stated.

---

## 5. Evaluation Outcomes

A reviewer must classify each valid submission as one of the following:

```text
R1 — Reproduction
R2 — Falsification
R3 — Structural Ambiguity
Invalid / Incomplete
```

The reviewer should not invent additional outcome categories unless the committee formally updates the challenge rules.

---

## 6. R1 — Reproduction

A submission qualifies as **R1 — Reproduction** if the reviewer determines that:

- the GCD-001 custody graph is reconstructible from the published materials;
- the relevant artifacts are available;
- canonicalization is deterministic;
- hashes or commitments can be independently checked;
- graph vertices are sufficiently defined;
- graph edges are sufficiently defined;
- A/V roles are clear enough for reconstruction;
- oracle-bound claims are separated from reconstructible evidence;
- the minimum sufficient vertex-cut can be computed;
- the claimed NDC is reproduced under the published specification.

The honest meaning of R1 is:

```text
The specific GCD-001 NDC claim was reproduced under the published specification.
```

R1 does **not** mean:

- A-DAP is validated as a whole;
- the original decision was true;
- the original decision was fair;
- the original decision was lawful;
- record integrity equals decision truth;
- oracle-bound claims became verified;
- the author’s framework is generally proven.

R1 confirms reproducibility of the specific published claim under the stated rules.

Nothing more.

---

## 7. R2 — Falsification

A submission qualifies as **R2 — Falsification** if the reviewer determines that the published GCD-001 claim is constructively wrong.

Examples of valid R2 findings include:

- a smaller valid vertex-cut than the claimed one;
- an invalid graph edge;
- an invalid graph vertex classification;
- an omitted dependency path;
- an oracle-bound claim incorrectly counted as verified;
- a hash, signature, or timestamp inconsistency that alters the claim;
- an incorrect NDC calculation;
- a contradiction between the published claim and reconstructible evidence;
- an alteration path that defeats the claimed detection structure.

A valid R2 should include a constructive demonstration.

A reviewer should not classify a submission as R2 based only on rhetorical disagreement, preference, or general skepticism.

The honest meaning of R2 is:

```text
The GCD-001 NDC claim was falsified through a constructive demonstration.
```

R2 is not a failure of the review process.

R2 is a successful adversarial finding.

---

## 8. R3 — Structural Ambiguity

A submission qualifies as **R3 — Structural Ambiguity** if the reviewer determines that the specification is incomplete, unstable, or ambiguous enough to prevent deterministic reconstruction.

Examples of valid R3 findings include:

- ambiguous canonicalization;
- missing artifacts;
- undefined graph vertices;
- undefined graph edges;
- unclear A/V role assignment;
- unclear detection condition;
- unclear alteration condition;
- unstable oracle-boundary classification;
- unclear NDC calculation method;
- multiple materially different reconstructions permitted by the same published materials;
- dependency on undocumented assumptions;
- dependency on author-controlled tools for the primary reconstruction.

The honest meaning of R3 is:

```text
The GCD-001 specification requires correction before deterministic reconstruction is possible.
```

R3 is not the same as falsification.

R3 means the claim cannot yet be deterministically evaluated under the published specification.

A strong R3 submission should show exactly where the ambiguity occurs and how it affects the reconstruction.

---

## 9. Invalid or Incomplete Submission

A submission may be classified as **Invalid / Incomplete** if it does not meet basic administrative or technical requirements.

Examples include:

- no declared outcome;
- no reconstruction method;
- no graph representation;
- no min-cut reasoning;
- no oracle-boundary analysis;
- no reproducibility instructions;
- reliance on the author’s solver as the primary computation path;
- unsupported assertions without evidence;
- general commentary without a constructive reconstruction, falsification, or ambiguity claim;
- failure to identify the repository snapshot reviewed.

Invalid or incomplete submissions should not be treated as R1, R2, or R3.

However, reviewers may recommend that the submitter revise and resubmit if the submission has potential.

---

## 10. Administrative Validity Check

Before technical review, a submission should be checked for administrative completeness.

A submission is administratively complete if it includes:

- declared outcome: R1, R2, or R3;
- reviewer name, organization, or pseudonym;
- contact method;
- repository snapshot or commit reviewed;
- materials reviewed;
- reconstruction method;
- graph representation;
- vertex list;
- edge list;
- oracle-boundary analysis;
- detection condition;
- alteration condition;
- candidate cuts tested;
- minimum vertex-cut reasoning;
- NDC calculation or challenge;
- reproducibility instructions;
- independence declaration;
- final conclusion.

Administrative completeness does not imply technical acceptance.

It only means the submission is reviewable.

---

## 11. Independence Requirement

The primary reconstruction must be independent of the author.

The reviewer must reject or downgrade any submission whose primary computation depends on:

- the author’s solver;
- the author’s scripts;
- expected output files generated by the author;
- private infrastructure controlled by the author;
- manual assertions by the author;
- undocumented author intent;
- private communication with the author;
- uninspectable computation.

Author-provided tools may be used only for secondary comparison after the submitter has performed an independent reconstruction.

The submitter must disclose any use of author-provided tools.

A submission that merely runs the author’s script is not independent reconstruction.

---

## 12. Graph Reconstruction Standard

A reviewer should check whether the submitted graph is explicit and inspectable.

The graph should include:

- vertices;
- edges;
- vertex types;
- edge types;
- source references;
- reconstruction status;
- oracle-bound status;
- assumptions;
- candidate cut paths.

Acceptable graph formats include:

- JSON;
- CSV;
- DOT;
- GraphML;
- Mermaid;
- table;
- image;
- plain text adjacency list;
- another inspectable format.

The reviewer should determine whether the submitted graph is sufficient for another party to inspect the reconstruction.

If the graph cannot be inspected, reproduced, or understood, the submission may be incomplete.

---

## 13. Vertex Evaluation

For each vertex, the reviewer should check:

- Is the vertex clearly identified?
- Is the vertex type defined?
- Is the vertex supported by published material?
- Is the vertex reconstructible?
- Is the vertex oracle-bound?
- Is the vertex necessary for the claimed cut?
- Is the vertex classification stable under the published specification?

A vertex should not be accepted merely because the author or submitter asserts it.

A vertex must be justified by the reconstruction.

---

## 14. Edge Evaluation

For each edge, the reviewer should check:

- Is the edge clearly identified?
- Are source and target vertices defined?
- Is the edge type defined?
- Is the edge supported by published material?
- Is the edge reconstructible?
- Is the edge oracle-bound?
- Is the edge necessary for the claimed dependency path?
- Is the edge overstated, missing, or ambiguous?

Edges are often where hidden assumptions enter the graph.

A reviewer should apply special scrutiny to edges that connect cryptographic records to real-world truth claims.

---

## 15. Oracle Boundary Evaluation

The reviewer must ensure that oracle-bound claims are declared rather than counted as structurally verified.

Claims that are usually oracle-bound include:

- the input was true in the real world;
- the model actually executed the decision;
- the model state was real;
- the declared actor identity was institutionally valid;
- the policy was legally valid or in force;
- the explanation reflects real internal causality;
- the decision was correct;
- the decision was fair;
- the decision was legitimate.

Claims that may be reconstructible include:

- a hash matches a published artifact;
- a signature verifies against a declared public key;
- a timestamp token matches a message imprint;
- a referenced file exists at a published path;
- a custody declaration is present;
- a graph declaration is present;
- a deterministic reconstruction path exists.

The reviewer should separate:

```text
cryptographic reconstruction
```

from:

```text
real-world truth
```

If a submission collapses this distinction, it should not qualify as R1 without correction.

---

## 16. Hash, Signature, and Timestamp Evaluation

The reviewer should treat cryptographic evidence carefully.

Hash matches may support:

- artifact integrity;
- reference integrity;
- record consistency.

Hash matches do not prove:

- semantic correctness;
- real-world truth;
- legal validity;
- fairness;
- decision legitimacy.

Signatures may support:

- commitment by a key;
- integrity of signed payload;
- non-alteration after signing.

Signatures do not automatically prove:

- institutional authority of the signer;
- lawful delegation;
- real-world truth;
- fairness;
- correctness.

Timestamps may support:

- existence of a commitment at or before a time;
- sequencing evidence;
- temporal anchoring.

Timestamps do not automatically prove:

- that the decision was correct;
- that the model executed;
- that the input was true;
- that the policy was valid;
- that the decision was legitimate.

The reviewer should flag any submission that overclaims cryptographic evidence.

---

## 17. Detection Condition Evaluation

The reviewer should verify whether the submission clearly defines the detection condition.

Detection may include:

- hash mismatch;
- signature mismatch;
- timestamp inconsistency;
- missing artifact;
- broken reference;
- graph inconsistency;
- custody path inconsistency;
- canonicalization failure;
- declared dependency mismatch;
- oracle-bound claim incorrectly counted as verified.

If the detection condition is undefined, the NDC calculation may be unstable.

This may support R3.

---

## 18. Alteration Condition Evaluation

The reviewer should verify whether the submission clearly defines the alteration condition.

Alteration targets may include:

- decision input;
- decision output;
- decision envelope;
- policy reference;
- graph declaration;
- hash commitment;
- timestamp reference;
- signature reference;
- custody dependency;
- claimed NDC value.

If the alteration condition is unclear, the minimum cut may be undefined.

This may support R3.

---

## 19. Min-Cut Evaluation

The reviewer should evaluate whether the submitted minimum vertex-cut is justified.

The submitter should explain:

- which vertices are included;
- why the cut is sufficient;
- why smaller cuts are insufficient;
- which detection condition applies;
- which alteration condition applies;
- which assumptions affect the result;
- whether oracle-bound claims influence the cut.

A reviewer should not accept a cut merely because it is computed by a tool.

The reviewer should examine the graph model and assumptions that make the cut meaningful.

If a smaller valid cut exists, the submission may support R2.

If the cut cannot be determined because the graph is ambiguous, the submission may support R3.

---

## 20. NDC Evaluation

The reviewer should compare:

```text
claimed NDC
```

with:

```text
independently computed or challenged NDC
```

The reviewer should check:

- the graph model used;
- the minimum vertex-cut used;
- the NDC formula or interpretation;
- assumptions;
- oracle boundaries;
- calculation method;
- reproducibility of the result.

Possible conclusions:

```text
claimed NDC reproduced -> R1 candidate
claimed NDC falsified -> R2 candidate
claimed NDC indeterminate -> R3 candidate
```

A reviewer should not treat NDC as a complete governance score.

NDC is a structural dependency measure for the specific custody claim under review.

---

## 21. Reproducibility Evaluation

The reviewer should check whether the submission can be reproduced by another party.

A reproducible submission should include:

- repository snapshot reviewed;
- files reviewed;
- code or calculation method;
- graph representation;
- dependency list;
- commands or instructions;
- expected output;
- limitations.

If the reviewer cannot reproduce or inspect the submission, the submission may be incomplete.

If the inability to reproduce is caused by ambiguity in the published GCD-001 materials, the result may support R3.

---

## 22. Treatment of Author Tools

The reviewer may inspect author-provided tools.

However:

```text
author tools are not authority
```

Author tools may be used for:

- secondary comparison;
- understanding the author’s claim;
- identifying assumptions;
- checking consistency after independent reconstruction.

Author tools must not be used for:

- primary reconstruction;
- primary min-cut computation;
- primary NDC acceptance;
- replacing reviewer reasoning;
- proving the claim by execution alone.

A submission that relies on author tools as the primary path should not qualify as independent R1.

---

## 23. Review of R1 Submissions

When evaluating an R1 submission, the reviewer should ask:

- Did the submitter reconstruct the graph independently?
- Did the submitter compute the cut independently?
- Did the submitter identify oracle boundaries?
- Did the submitter reproduce the claimed NDC?
- Did the submitter avoid overclaiming?
- Is the reconstruction reproducible?
- Are the assumptions explicit?

Approve as R1 only if the specific GCD-001 claim is reproduced under the published specification.

Do not approve R1 merely because:

- the author’s script runs;
- expected output matches;
- the repository looks complete;
- the claim sounds plausible;
- the submitter agrees with the author.

---

## 24. Review of R2 Submissions

When evaluating an R2 submission, the reviewer should ask:

- Is the falsification constructive?
- Does it show a smaller valid cut?
- Does it identify an invalid vertex or edge?
- Does it expose an omitted dependency?
- Does it show an oracle-bound claim counted as verified?
- Does it contradict the claimed NDC?
- Can the finding be reproduced?
- Does the finding affect the actual claim under review?

Approve as R2 only if the submission demonstrates that the published GCD-001 claim is incorrect under the relevant specification.

Do not approve R2 merely because:

- the submitter dislikes the framework;
- the submitter disputes A-DAP generally;
- the submitter makes broad philosophical objections;
- the submitter criticizes the project without reconstructing the claim.

---

## 25. Review of R3 Submissions

When evaluating an R3 submission, the reviewer should ask:

- What exactly is ambiguous?
- Does the ambiguity affect the graph?
- Does the ambiguity affect the cut?
- Does the ambiguity affect the NDC?
- Does the ambiguity affect oracle-boundary classification?
- Does the specification allow more than one materially different reconstruction?
- Can the ambiguity be fixed by a specification update?

Approve as R3 if deterministic reconstruction is blocked by underspecification.

Do not approve R3 merely because:

- the submission is incomplete;
- the submitter did not attempt reconstruction;
- the reviewer prefers a different format;
- the author’s claim is complex;
- the result is inconvenient.

R3 should identify a specific structural ambiguity.

---

## 26. Skeptical Tie-Breaking Rule

If reviewers disagree, the skeptical interpretation should prevail.

This means:

- uncertainty should not be upgraded into R1;
- unclear proof should not be treated as reproduction;
- ambiguous specification should remain R3 unless resolved;
- constructive falsification should be taken seriously;
- oracle-bound claims should not be silently counted as verified.

The purpose of the challenge is not to protect the claim.

The purpose is to expose the claim to reconstruction pressure.

---

## 27. Author Non-Voting Rule

The protocol author must not decide technical acceptance.

The author may clarify:

- file locations;
- repository structure;
- terminology already present in the published materials;
- administrative logistics;
- whether a submission is complete enough for review.

The author must not decide:

- whether R1 is accepted;
- whether R2 is accepted;
- whether R3 is accepted;
- whether the NDC is correct;
- whether a falsification is valid;
- whether ambiguity is material.

This rule exists to prevent adversarial validation from becoming self-validation.

---

## 28. Committee Decision Standard

A future Acceptance Committee should ideally include three publicly named external reviewers.

Recommended decision rule:

```text
majority decision
```

Tie or unresolved disagreement should favor the skeptical classification.

Suggested hierarchy:

```text
R2 over R1 when constructive falsification is valid.
R3 over R1 when deterministic reconstruction is blocked.
Invalid over R1 when independence or reproducibility is missing.
```

The committee should publish a short decision note for each accepted submission.

---

## 29. Public Disclosure Standard

For transparency, the final review summary should disclose:

- number of submissions received;
- number of administratively valid submissions;
- number of invalid or incomplete submissions;
- number of accepted R1 outcomes;
- number of accepted R2 outcomes;
- number of accepted R3 outcomes;
- committee members;
- committee decision summaries;
- unresolved ambiguities;
- specification changes triggered by review.

The review summary must not describe the challenge as full validation of A-DAP.

The strongest honest public claim depends on the accepted outcome.

---

## 30. Empty Challenge Clause

If no valid external reconstruction is submitted, the challenge does not validate GCD-001.

Silence is not confirmation.

An empty challenge means only:

```text
No qualifying external reconstruction was submitted during the review period.
```

Further outreach, workshop review, direct expert review, or independent audit may still be required.

---

## 31. Overclaiming Flags

Reviewers should flag language that overclaims the result.

Problematic claims include:

```text
A-DAP is proven.
A-DAP validates decision truth.
GCD-001 proves the decision was correct.
NDC proves fairness.
Hash integrity proves semantic truth.
Timestamping proves legitimacy.
Running the author script proves independent reconstruction.
No one challenged the claim, so the claim is validated.
```

Preferred language:

```text
The specific GCD-001 NDC claim was reproduced under the published specification.
```

or:

```text
The GCD-001 NDC claim was falsified through a constructive demonstration.
```

or:

```text
The GCD-001 specification requires correction before deterministic reconstruction is possible.
```

---

## 32. Minimal Honest Claims by Outcome

### If R1 is accepted

```text
The GCD-001 NDC claim was reproduced under the published specification by an external reviewer.
```

### If R2 is accepted

```text
The GCD-001 NDC claim was falsified through a constructive external reconstruction.
```

### If R3 is accepted

```text
The GCD-001 specification was found structurally underspecified and requires correction before deterministic reconstruction.
```

### If no valid submissions are received

```text
No qualifying external reconstruction was submitted. This does not validate the claim.
```

---

## 33. Reviewer Checklist

Before making a recommendation, the reviewer should confirm:

```text
[ ] The submission declares R1, R2, or R3.
[ ] The repository snapshot reviewed is identified.
[ ] The materials reviewed are listed.
[ ] The primary reconstruction is independent of author tools.
[ ] The graph representation is inspectable.
[ ] Vertices are identified.
[ ] Edges are identified.
[ ] Oracle-bound claims are declared.
[ ] Detection condition is defined.
[ ] Alteration condition is defined.
[ ] Candidate cuts are discussed.
[ ] Minimum vertex-cut reasoning is provided.
[ ] NDC calculation or challenge is explained.
[ ] Reproducibility instructions are provided.
[ ] The conclusion does not overclaim.
```

---

## 34. Final Review Recommendation

A reviewer should end with one of the following recommendations:

```text
Recommend acceptance as R1 — Reproduction.
Recommend acceptance as R2 — Falsification.
Recommend acceptance as R3 — Structural Ambiguity.
Recommend rejection as invalid or incomplete.
Recommend revision and resubmission.
```

The recommendation should include a short justification.

Suggested wording:

```text
Based on the submitted materials and the reconstruction evidence, I recommend [R1/R2/R3/Invalid/Revision] because [brief reason].
```

---

## 35. Final Principle

The reviewer does not owe the author agreement.

The reviewer owes the process reconstruction discipline.

GCD-001 should be evaluated by evidence, not trust.

The strongest review is one that makes confirmation, falsification, and ambiguity equally admissible.
