# GCD-001 Submission Template

This document provides the standard submission template for external reviewers participating in the planned **GCD-001 Reconstruction Challenge**.

GCD-001 is a candidate public reconstruction package prepared for independent adversarial review.

At the current stage:

- external disjoint reconstruction is **pending**;
- Acceptance Committee is **not yet appointed**;
- public bounty is **not yet active**;
- submission channel is **not yet open**.

This template defines the intended submission format.

It does not imply that formal submissions are already open.

---

## 1. Submission Summary

### Submission title

```text
[Insert short title]
```

### Reviewer name or pseudonym

```text
[Insert name, organization, or pseudonym]
```

### Contact information

```text
[Insert email, GitHub handle, OR other preferred contact]
```

### Date of submission

```text
YYYY-MM-DD
```

### Repository snapshot reviewed

```text
Repository:
Commit hash:
Branch:
Date accessed:
```

### Claims and declared outcomes

List each specific claim and the repository release/version or commit against which it is assessed. Assign one outcome per claim; different claims may have different outcomes.

| Claim ID | Exact claim under review | Release/version or commit | Outcome (R1/R2/R3) |
|---|---|---|---|
| C1 | [claim] | [version or commit] | [R1/R2/R3] |

Do not infer a repository-wide or A-DAP-wide outcome from one claim.

---

## 2. Independence Declaration

The reviewer declares that the primary reconstruction was performed independently.

### Author-provided tools used?

```text
[ ] No author-provided tools were used.
[ ] Author-provided tools were used only for secondary comparison.
[ ] Author-provided tools were used in the primary reconstruction.
```

If author-provided tools were used, describe how:

```text
[Explain here]
```

### Primary computation path

Describe the primary method used to reconstruct the graph and compute or challenge the NDC.

```text
[Explain here]
```

### Conflict disclosure

Disclose any relationship with the author, repository owner, affiliated organization, or challenge sponsor.

```text
[Explain here]
```

---

## 3. Materials Reviewed

List all materials reviewed.

At minimum, include files, folders, commits, artifacts, scripts, or notes inspected.

```text
[Example]

- challenge/gcd-001/README.md
- challenge/gcd-001/reconstruction-spec.md
- challenge/gcd-001/reconstruction-challenge.md
- challenge/gcd-001/submission-template.md
- challenge/gcd-001/reviewer-guidelines.md
- challenge/synthetic-case/
- proofs/
- solver/
- README.md
```

### Materials missing or unavailable

List any materials that were expected but missing, inaccessible, ambiguous, or incomplete.

```text
[Explain here]
```

---

## 4. Claim Under Review

State the exact GCD-001 claim being reviewed.

```text
[Insert the published GCD-001 custody/NDC claim being reconstructed, challenged, or found ambiguous]
```

### Claimed NDC value

```text
Claimed NDC:
Source file:
Source section:
```

### Claimed graph or custody structure

Summarize the published graph/custody claim.

```text
[Explain here]
```

### Graph determinability

Select one for each claim where applicable:

```text
[ ] Determinable from the reviewed materials
[ ] Not determinable because of a specification-level gap (R3 candidate)
```

If not determinable, identify the exact required artifact that is missing or the rule that is undefined, cite where the materials establish its relevance, and explain which vertices, edges, custody relation, or other reconstruction step cannot be determined. Do not invent the missing graph.

---

## 5. Reconstruction Method

Describe how the reconstruction was performed.

The explanation should be sufficient for another reviewer or committee member to understand the process.

```text
[Explain here]
```

Include:

- graph model used;
- artifacts inspected;
- canonicalization assumptions;
- hash verification method;
- signature or timestamp verification method, if applicable;
- graph construction method;
- min-cut method;
- NDC calculation method;
- oracle-boundary classification method.

---

## 6. Decision Envelope Reconstruction

Describe whether the decision envelope was reconstructed.

```text
[Explain here]
```

### Envelope fields identified

| Field | Value / Reference | Reconstructible? | Notes |
|---|---|---|---|
| [field] | [value] | [yes/no/ambiguous] | [notes] |

### Canonicalization status

Select one:

```text
[ ] Canonicalization is deterministic.
[ ] Canonicalization is ambiguous.
[ ] Canonicalization is missing.
[ ] Canonicalization was not required for this submission.
```

Explain:

```text
[Explain here]
```

---

## 7. Hash Verification

List all hashes independently checked.

| Artifact | Path | Algorithm | Published Hash | Computed Hash | Match? | Notes |
|---|---|---|---|---|---|---|
| [artifact] | [path] | [SHA-256/etc.] | [hash] | [hash] | [yes/no] | [notes] |

### Hash verification conclusion

```text
[Explain here]
```

Important limitation:

```text
Hash integrity supports record integrity.
Hash integrity does not prove decision truth.
```

---

## 8. Signature and Timestamp Verification

Complete this section if signatures or timestamp evidence are part of the reviewed materials.

### Signatures

| Signed Object | Public Key / Key Ref | Signature Ref | Verification Result | Notes |
|---|---|---|---|---|
| [object] | [key] | [signature] | [pass/fail/ambiguous/not checked] | [notes] |

### Timestamps

| Timestamp Object | Timestamp Source | Token / Receipt | Verification Result | Notes |
|---|---|---|---|---|
| [object] | [source] | [token] | [pass/fail/ambiguous/not checked] | [notes] |

### Signature / timestamp conclusion

```text
[Explain here]
```

Important limitation:

```text
Signature and timestamp evidence may support commitment timing or integrity.
They do not prove semantic correctness, real-world truth, fairness, legality, or decision legitimacy.
```

---

## 9. Reconstructed Graph

Provide the reconstructed graph in an inspectable format.

Accepted formats include:

- JSON;
- CSV;
- DOT;
- GraphML;
- Mermaid;
- table;
- image;
- plain text adjacency list;
- another inspectable format.

### Graph format used

```text
[Insert format]
```

### Graph representation

```text
[Paste graph representation here or reference attached file]
```

If the graph is **not determinable** for an R3 claim, write that explicitly and provide the precise missing artifact or undefined rule plus its effect on the graph. Include any graph portion that can be reconstructed; do not fabricate missing vertices or edges.

---

## 10. Vertex List

List all reconstructed vertices.

| Vertex ID | Label | Type | Source | Reconstructible? | Oracle-Bound? | Notes |
|---|---|---|---|---|---|---|
| v1 | [label] | [type] | [source] | [yes/no/ambiguous] | [yes/no] | [notes] |

### Vertex classification notes

```text
[Explain here]
```

---

## 11. Edge List

List all reconstructed edges.

| Edge ID | From | To | Type | Source | Justification | Reconstructible? | Oracle-Bound? |
|---|---|---|---|---|---|---|---|
| e1 | v1 | v2 | [type] | [source] | [why this edge exists] | [yes/no/ambiguous] | [yes/no] |

### Edge classification notes

```text
[Explain here]
```

---

## 12. Oracle-Boundary Analysis

Classify each relevant claim as one of:

```text
reconstructible
oracle-bound
ambiguous
unsupported
```

| Claim | Classification | Reason | Evidence / Source |
|---|---|---|---|
| [claim] | [classification] | [reason] | [source] |

### Oracle-bound claims identified

```text
[Explain here]
```

### Claims incorrectly treated as verified, if any

```text
[Explain here]
```

---

## 13. Detection Condition

Define the detection condition used in the reconstruction.

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

### Detection condition used

```text
[Explain here]
```

### Is the detection condition sufficiently specified?

```text
[ ] Yes
[ ] No
[ ] Ambiguous
```

Explain:

```text
[Explain here]
```

---

## 14. Alteration Condition

Define what is assumed to be altered.

Possible alteration targets include:

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

### Alteration condition used

```text
[Explain here]
```

### Is the alteration condition sufficiently specified?

```text
[ ] Yes
[ ] No
[ ] Ambiguous
```

Explain:

```text
[Explain here]
```

---

## 15. Candidate Cuts Tested

List candidate vertex-cuts considered.

| Candidate Cut ID | Vertices Included | Sufficient? | Smaller Cut Possible? | Notes |
|---|---|---|---|---|
| c1 | [v1, v2] | [yes/no/ambiguous] | [yes/no/unknown] | [notes] |

### Candidate cut reasoning

```text
[Explain here]
```

---

## 16. Minimum Vertex-Cut

State the minimum sufficient vertex-cut identified.

```text
Minimum vertex-cut:
Vertices included:
Reasoning:
```

If the graph/cut is not determinable due to a demonstrated specification-level gap, write **Not determinable** above, identify the gap and its effect, and do not provide an unsupported cut or NDC. Whenever a minimum cut is claimed, explain why it is sufficient and why no smaller valid cut works.

### Why this cut is sufficient (complete when a cut is claimed)

```text
[Explain here]
```

### Why smaller cuts are insufficient (complete when a minimum cut is claimed)

```text
[Explain here]
```

### Assumptions affecting the cut

```text
[Explain here]
```

---

## 17. NDC Calculation or Challenge

### Claimed NDC

```text
[Insert claimed NDC]
```

### Computed NDC

```text
[Insert computed NDC]
```

### Calculation method

```text
[Explain here]
```

### Does the computed value match the claimed value?

```text
[ ] Yes
[ ] No
[ ] Cannot determine
```

Explain:

```text
[Explain here]
```

---

## 18. Outcome Justification

For each Claim ID in Section 1, justify its declared outcome. Complete the relevant outcome subsection(s); outcomes apply to the specified claim and version only.

---

### R1 — Reproduction

Use this section if the claim was reproduced.

```text
[Explain why the claim qualifies as R1]
```

R1 means:

```text
The specific GCD-001 NDC claim was reproduced under the published specification.
```

R1 does not mean:

- the original decision was true;
- the original decision was fair;
- the original decision was lawful;
- A-DAP as a whole is validated.

---

### R2 — Falsification

Use this section if the claim was falsified.

```text
[Explain why the claim qualifies as R2]
```

A valid R2 should provide a constructive demonstration, such as:

- a smaller valid vertex-cut;
- an invalid edge assumption;
- an invalid vertex classification;
- an oracle-bound claim incorrectly counted as verified;
- a graph reconstruction that contradicts the claimed NDC;
- an error in the NDC calculation method;
- a dependency path omitted by the published graph.

---

### R3 — Structural Ambiguity

Use this section to propose R3 for a specific claim and reviewed repository version only when the gap is decisive.

```text
[Explain why the claim qualifies as R3]
```

A valid R3 must identify the exact missing artifact or undefined rule, delimit admissible completions by the reviewed materials and stated assumptions, and provide independently checkable reasoning that the gap is outcome-determinative. Provide at least two materially different admissible reconstructions or completions: one under which the claim holds and one under which it fails (for example, NDC > 1 versus NDC ≤ 1). If an absent artifact prevents complete alternatives, demonstrate how admissible completions of that artifact can change the claim’s outcome.

If the claim holds under every admissible completion, R1 requires positive, independent, inspectable reproduction evidence; absence of a counterexample is not reproduction. If it fails under every admissible completion, R2 requires constructive, independently checkable falsification. Failure to confirm R3 does not imply R1 or R2. An indeterminate graph element that does not change the claim’s outcome is a specification note, not R3.

Identify the precise gap, cite the relevant specification and repository version, and explain its effect on the graph, cut, or NDC. Mark the affected graph or cut **not determinable** where justified; do not invent missing elements. Every R3 finding must state a remediation condition: the specific artifact to supply or rule to define that would make the claim determinable.

A qualifying gap may affect:

- canonicalization;
- artifact availability;
- graph vertices;
- graph edges;
- A/V role assignment;
- oracle-boundary classification;
- NDC calculation;
- minimum vertex-cut reasoning;
- dependency interpretation.

Do not use R3 for a transient access or environment error, timeout, unavailable compute resource, or incomplete submission alone. Record operational failures separately and retry where reasonable. An incomplete submission is Invalid / Incomplete unless a specification-level gap is independently demonstrated.

---

## 19. Reproducibility Instructions

Provide instructions sufficient for another reviewer or committee member to inspect, run, or reproduce the submission.

```bash
# Example
git clone [repository]
cd [repository]
[commands here]
```

### Required dependencies

```text
[Insert language/runtime/package requirements]
```

### Expected output

```text
[Describe expected output]
```

### Known limitations

```text
[Describe limitations]
```

---

## 20. Files Included in This Submission

List all files included in the submission package.

```text
submission/
├── technical-note.md
├── reconstructed-graph.json
├── min-cut-memo.md
├── oracle-boundary-analysis.md
├── code/
│   └── reconstruct.py
└── README.md
```

Adjust structure as needed.

---

## 21. Public Disclosure Preference

Select one:

```text
[ ] Reviewer identity may be publicly disclosed.
[ ] Reviewer identity should remain pseudonymous.
[ ] Submission may be publicly disclosed in full.
[ ] Submission may be publicly summarized but not disclosed in full.
[ ] Contact me before any public disclosure.
```

Additional notes:

```text
[Explain here]
```

---

## 22. Reviewer Statement

The reviewer should confirm:

```text
I understand that GCD-001 does not test whether the original decision was true, fair, lawful, or correct.

I understand that GCD-001 tests whether a published decision-custody/NDC claim can be independently reconstructed, falsified, or shown to be structurally underspecified.

I understand that author-provided tools must not be used as the primary computation path for independent reconstruction.

I understand that record integrity is not decision truth.

I understand that oracle-bound claims must be declared rather than treated as structurally verified.

I understand that R1, R2, or R3 applies to a specific claim and repository version, not to A-DAP as a whole.

I understand that R3 requires a demonstrated decisive gap, materially different admissible completions with different claim outcomes, and a remediation condition.

I have disclosed my independence and relationships, including any relationship with the author, repository owner, affiliated organization, or challenge sponsor.
```

Reviewer confirmation:

```text
[Insert confirmation here]
```

---

## 23. Final Conclusion

State one final conclusion for each specific claim and reviewed repository version. Do not combine claims with different evidence or outcomes.

```text
Claim:
Reviewed version (commit or release):
Outcome for this claim/version (R1/R2/R3 or not accepted (unresolved)):
Evidence sufficiency and concise reasoning:
For R3, confirmed gap, outcome-divergent admissible completions, and remediation condition:
```

Use the applicable claim- and version-specific wording:

```text
For R1: Based on the materials reviewed and independent reconstruction, the specific claim [claim] was reproduced under the published specification for version [version], because [brief, inspectable reasoning].
For R2: The specific claim [claim] for version [version] was constructively falsified because [counterexample and independently checkable reasoning].
For R3: The specific claim [claim] for version [version] is not determinable because [decisive specification gap]; admissible completion [A] supports the claim and admissible completion [B] falsifies it. The claim can be determined if [specific artifact or rule is supplied/defined].
If evidence is insufficient: The claim [claim] for version [version] is not accepted (unresolved); [state which evidence-sufficiency or gap-existence/decisiveness finding lacks a majority]. This is not an R1 or R2 finding.
```

---

## 24. Minimal Honest Claim

For each specific claim and reviewed version, this submission should support only the matching outcome below. Different claims may have different outcomes.

For a specific claim/version classified R1:

```text
The GCD-001 NDC claim was reproduced under the published specification.
```

For a specific claim/version classified R2:

```text
The GCD-001 NDC claim was falsified through a constructive demonstration.
```

For a specific claim/version classified R3:

```text
The GCD-001 specification requires correction before deterministic reconstruction is possible.
```

For insufficient evidence without an adopted technical classification:

```text
The claim [claim] for version [version] is not accepted (unresolved); the evidence does not support R1, R2, or R3 by the required majority.
```

No submission should claim full validation of A-DAP. The protocol author has no vote on technical acceptance or on whether an R3 gap is material.

---

## 25. Signature

```text
Reviewer name or pseudonym:
Date:
Version of submission:
Commit or snapshot reviewed:
Declared outcome:
```
