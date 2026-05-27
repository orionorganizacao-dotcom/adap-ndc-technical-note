# GCD-001 Reconstruction Specification

This document defines how an external verifier should reconstruct the **GCD-001 decision-custody graph** and compute or challenge the claimed **Network Dependency Coefficient (NDC)**.

GCD-001 is a candidate public reconstruction package prepared for independent adversarial review.

At the current stage:

- external disjoint reconstruction is **pending**;
- Acceptance Committee is **not yet appointed**;
- public bounty is **not yet active**;
- submission channel is **not yet open**.

This specification is intended to support external reconstruction.

It does not imply that the GCD-001 claim has already been independently validated.

---

## 1. Purpose

The purpose of this specification is to define a reproducible reconstruction path for GCD-001.

An external verifier should be able to:

- identify the published materials;
- reconstruct the decision-custody graph;
- identify vertices and edges;
- distinguish reconstructible claims from oracle-bound claims;
- compute or challenge the claimed NDC;
- classify the result as R1, R2, or R3.

The goal is not to trust the author.

The goal is to reconstruct the graph.

---

## 2. Core Principle

```text
Do not trust the author.
Reconstruct the graph.
Compute the cut.
Challenge the NDC claim.
Declare the oracle boundary.
```

The verifier must treat all author-provided materials as reconstruction inputs, not as proof.

The author’s expected output is not authoritative.

The author’s solver is not authoritative.

The published claim is the object of reconstruction, not the source of truth.

---

## 3. Scope

This specification applies only to the GCD-001 custody/NDC reconstruction claim.

It does not validate:

- A-DAP as a whole;
- the correctness of the original decision;
- the fairness of the original decision;
- the legality of the original decision;
- the truth of real-world inputs;
- the internal causal state of a model;
- the institutional legitimacy of an actor;
- NDC as a complete governance metric.

This specification concerns a narrower question:

```text
Can the published GCD-001 custody/NDC claim be independently reconstructed, falsified, or shown to be structurally underspecified?
```

---

## 4. Required Reviewer Posture

The verifier must be skeptical by default.

The verifier must not assume:

- the author’s NDC is correct;
- the author’s graph is complete;
- the author’s script is authoritative;
- the expected output is proof;
- the repository structure is evidence of validation;
- publication implies correctness;
- hash integrity implies semantic truth;
- timestamp presence implies independent reconstruction;
- oracle-bound claims are verified;
- record integrity equals decision truth.

The verifier must distinguish between:

```text
record reconstruction
```

and:

```text
decision truth
```

GCD-001 concerns record reconstruction, not decision truth.

---

## 5. Definitions

### A — Author / Claimant

The party publishing the GCD-001 custody/NDC claim.

The author may provide artifacts, explanations, scripts, and expected outputs.

The author does not determine whether the reconstruction succeeds.

---

### V — Verifier / Reconstructing Party

The external party attempting to reconstruct, falsify, or identify ambiguity in the GCD-001 claim.

The verifier must perform the primary reconstruction independently.

---

### Decision Record

The recorded decision object under analysis.

A decision record may include references to inputs, outputs, policy hashes, metadata, timestamps, signatures, custody declarations, or graph declarations.

The decision record is not assumed to prove decision truth.

---

### Decision Envelope

The structured pre-action or action-bound record containing decision-relevant artifacts.

A decision envelope may include:

- input references;
- output references;
- policy references;
- model references;
- timestamp references;
- signature references;
- hash commitments;
- custody declarations.

The envelope is an input to reconstruction, not proof by itself.

---

### Custody Graph

The graph representing dependency, control, evidence, and alteration paths relevant to the decision record.

The custody graph is the main object reconstructed by the verifier.

---

### Vertex

A node in the custody graph.

A vertex may represent an artifact, actor, key, signature, timestamp, hash commitment, policy, input, output, repository object, or verification dependency.

---

### Edge

A dependency, control, evidence, or alteration relationship between vertices.

Edges must be declared, inferred from published materials, or justified by the verifier.

Undefined edges are a reconstruction risk.

---

### Cut

A set of vertices whose alteration changes the relevant decision-custody condition.

---

### Minimum Vertex-Cut

The smallest sufficient set of vertices required to alter the relevant decision-custody graph condition without detection by the verifier.

---

### NDC — Network Dependency Coefficient

For GCD-001, NDC is treated as the claimed structural dependency measure derived from the minimum sufficient vertex-cut.

The verifier must reconstruct or challenge the NDC reasoning rather than assume the author’s value.

---

### Oracle-Bound Claim

A claim whose truth depends on an external source not independently reconstructible from the published artifacts.

Oracle-bound claims must not be counted as structurally verified unless independently supported by external evidence.

---

## 6. Reconstruction Inputs

The verifier may receive or inspect:

- decision envelope;
- raw artifacts;
- canonicalization specification;
- hash rules;
- signature rules;
- timestamp evidence, if present;
- graph declaration;
- oracle-boundary declaration;
- tamper-test cases;
- claimed NDC value;
- README files;
- challenge rules;
- reviewer guidelines;
- submission template.

The verifier must treat these materials as inputs.

They are not proof until reconstructed.

---

## 7. Required Reconstruction Outputs

The verifier should attempt to reconstruct:

- canonical envelope;
- hash values;
- signature references, if applicable;
- timestamp references, if applicable;
- graph vertices;
- graph edges;
- declared A/V pair;
- candidate attack paths;
- oracle-boundary classification;
- minimum vertex-cut;
- NDC estimate;
- final outcome classification: R1, R2, or R3.

---

## 8. Independent Implementation Requirement

The verifier must not rely on the author’s solver, scripts, expected outputs, private infrastructure, or manually asserted conclusions for the primary reconstruction.

The author’s tools may be used only for secondary comparison after the verifier has independently reconstructed the graph and computed the relevant cut.

A valid reconstruction must be inspectable, reproducible, and independent of author-controlled tools.

A reconstruction that merely runs the author’s script is not independent reconstruction.

A reconstruction that treats expected output as proof is not independent reconstruction.

---

## 9. Prohibited Primary Dependencies

The primary reconstruction must not depend on:

- the author’s solver;
- the author’s scripts;
- expected output files generated by the author;
- private infrastructure controlled by the author;
- undocumented assumptions;
- manually asserted conclusions by the author;
- uninspectable external state;
- private communication with the author.

Use of author-provided tools for secondary comparison is allowed only if disclosed.

---

## 10. Reconstruction Procedure

The verifier should follow this procedure.

---

### Step 1 — Identify Materials Reviewed

List all materials reviewed.

At minimum, the verifier should identify:

- repository path;
- commit hash or snapshot date, if available;
- files inspected;
- artifacts inspected;
- scripts inspected, if any;
- expected outputs inspected, if any.

The verifier should state whether the reviewed materials were complete enough to attempt reconstruction.

If materials are missing, the result may qualify as R3.

---

### Step 2 — Reconstruct the Decision Envelope

The verifier should reconstruct the decision envelope from the published materials.

The verifier should identify:

- envelope fields;
- field names;
- field values;
- referenced artifacts;
- hashes;
- signatures, if any;
- timestamps, if any;
- declared dependencies;
- declared policy references;
- declared input/output references.

The verifier should state whether canonicalization is deterministic.

If canonicalization is ambiguous, the result may qualify as R3.

---

### Step 3 — Verify Hash Commitments

The verifier should independently compute all relevant hashes from the published artifacts.

For each hash, the verifier should report:

- artifact name;
- artifact path;
- hash algorithm;
- computed hash;
- published hash;
- match status;
- ambiguity or mismatch, if any.

A hash match supports record integrity.

A hash match does not prove decision truth.

If hashes do not match, the verifier should determine whether the mismatch supports R2 or R3.

---

### Step 4 — Verify Signature or Timestamp Evidence

If signatures are present, the verifier should identify:

- signing key or public key reference;
- signed payload;
- signature value;
- verification method;
- verification result.

If timestamps are present, the verifier should identify:

- timestamp authority or source;
- timestamp token or receipt;
- signed message imprint, if available;
- verification method;
- verification result.

Timestamp or signature evidence should be treated as evidence of commitment, not as proof of semantic correctness.

If timestamp or signature evidence is missing, incomplete, or unverifiable, the verifier should mark it accordingly.

---

### Step 5 — Reconstruct Graph Vertices

The verifier should identify all relevant graph vertices.

Vertices may include:

- decision record;
- decision envelope;
- input artifact;
- output artifact;
- policy artifact;
- model reference;
- hash commitment;
- signing key;
- timestamp anchor;
- repository commit;
- graph declaration;
- verifier dependency;
- oracle-bound external source.

For each vertex, the verifier should document:

- vertex identifier;
- vertex type;
- source material;
- reconstructible status;
- oracle-bound status, if applicable;
- role in the custody graph.

---

### Step 6 — Reconstruct Graph Edges

The verifier should identify all relevant graph edges.

Edges may represent:

- dependency;
- control;
- evidence;
- commitment;
- derivation;
- reference;
- signing relationship;
- timestamp relationship;
- custody relationship;
- alteration path.

For each edge, the verifier should document:

- source vertex;
- target vertex;
- edge type;
- source material;
- justification;
- whether the edge is reconstructible;
- whether the edge depends on an oracle-bound claim.

Undefined or unstable edges may support R3.

Invalid or overstated edges may support R2.

---

### Step 7 — Declare Oracle Boundaries

The verifier must explicitly identify claims that cannot be independently reconstructed from the published materials.

Oracle-bound claims may include:

- whether the input was true in the real world;
- whether the model actually executed the decision;
- whether the model state was real;
- whether the declared agent identity was institutionally valid;
- whether the policy was legally valid or in force;
- whether the explanation reflects real internal causality;
- whether the decision was correct, fair, or legitimate.

Oracle-bound claims must not be counted as structurally verified unless separately supported by external evidence.

The verifier should separate:

```text
cryptographically reconstructible artifacts
```

from:

```text
externally dependent truth claims
```

---

### Step 8 — Define the Detection Condition

The verifier must define what counts as detection.

For GCD-001, detection may include:

- hash mismatch;
- signature mismatch;
- timestamp inconsistency;
- missing artifact;
- broken reference;
- graph inconsistency;
- custody path inconsistency;
- canonicalization failure;
- declared dependency mismatch;
- oracle-bound claim incorrectly treated as verified.

The verifier must state which detection condition is used in the NDC calculation.

If the detection condition is undefined or unstable, the result may qualify as R3.

---

### Step 9 — Define the Alteration Condition

The verifier must define what the attacker is assumed to alter.

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

The verifier must state the alteration condition used for the cut calculation.

If the alteration condition is unclear, the result may qualify as R3.

---

### Step 10 — Compute Candidate Cuts

The verifier should identify candidate sets of vertices whose alteration would change the relevant decision-custody condition.

For each candidate cut, the verifier should document:

- vertices included;
- reason the cut is sufficient;
- detection avoided;
- assumptions required;
- oracle-bound dependencies;
- whether a smaller cut appears possible.

The verifier should not accept the author’s claimed cut without independent reasoning.

---

### Step 11 — Identify the Minimum Sufficient Vertex-Cut

The verifier must identify the smallest sufficient vertex-cut under the declared graph model, detection condition, and alteration condition.

The verifier should explain:

- why the proposed cut is sufficient;
- why smaller cuts are insufficient;
- which vertices are required;
- which edges make the cut necessary;
- which assumptions affect the result.

If a smaller valid cut exists than the claimed one, the result may qualify as R2.

If the minimum cut cannot be determined because of ambiguity, the result may qualify as R3.

---

### Step 12 — Compute or Challenge the NDC

The verifier should compute or challenge the claimed NDC based on the reconstructed minimum sufficient vertex-cut.

The verifier must state:

- claimed NDC value;
- independently computed NDC value;
- calculation method;
- graph model used;
- cut used;
- assumptions used;
- mismatch, if any;
- ambiguity, if any.

If the computed value matches under the published specification, the result may qualify as R1.

If the computed value contradicts the claim, the result may qualify as R2.

If the computed value cannot be determined because the specification is ambiguous, the result may qualify as R3.

---

## 11. Classification Rules

The verifier must classify the outcome as R1, R2, or R3.

---

### R1 — Reproduction

Classify as R1 if:

- the graph is reconstructible;
- canonicalization is deterministic;
- required artifacts are available;
- hashes and commitments can be checked;
- graph vertices are sufficiently defined;
- graph edges are sufficiently defined;
- oracle-bound claims are separated;
- the minimum vertex-cut can be computed;
- the claimed NDC is reproduced under the published specification.

R1 does not validate A-DAP as a whole.

R1 only means the specific GCD-001 NDC claim was reproduced under the published specification.

---

### R2 — Falsification

Classify as R2 if:

- the claimed NDC is incorrect;
- a smaller valid vertex-cut exists;
- the graph contains invalid dependencies;
- an oracle-bound claim is incorrectly counted as verified;
- a required edge is invalid;
- a required vertex classification is invalid;
- the claimed NDC calculation contains a constructive error;
- the published claim contradicts the reconstructible evidence.

A valid R2 should provide a constructive demonstration.

R2 is a successful adversarial finding.

---

### R3 — Structural Ambiguity

Classify as R3 if:

- canonicalization is ambiguous;
- artifacts are missing;
- graph vertices are undefined;
- graph edges are undefined;
- A/V roles are unclear;
- detection condition is unclear;
- alteration condition is unclear;
- minimum cut cannot be deterministically computed;
- oracle-boundary classification is unstable;
- the specification permits more than one materially different reconstruction.

R3 does not mean the claim is false.

R3 means the specification requires correction before deterministic reconstruction is possible.

---

## 12. Failure Conditions

The reconstruction fails if:

- canonicalization is ambiguous;
- artifacts are missing;
- hashes do not match;
- graph edges are undefined;
- graph vertices are undefined;
- A/V roles are unclear;
- oracle-bound claims are counted as verified;
- the verifier cannot independently reproduce the NDC reasoning;
- the claimed NDC depends on author-controlled tools;
- the specification permits materially different reconstructions.

Failure is not automatically negative.

A failed reconstruction may indicate R2 or R3.

---

## 13. Expected Submission Artifacts

A complete reviewer submission should include:

- declared outcome: R1, R2, or R3;
- reviewer identity or pseudonym;
- materials reviewed;
- reconstruction code;
- graph representation;
- vertex list;
- edge list;
- min-cut calculation memo;
- oracle-boundary analysis;
- NDC calculation or challenge;
- reproducibility instructions;
- independence declaration;
- technical note of 2–5 pages.

The submission should use `submission-template.md`.

---

## 14. Suggested Graph Representation

The verifier may use any inspectable graph format, including:

- JSON;
- CSV;
- DOT;
- GraphML;
- Mermaid;
- table;
- image;
- plain text adjacency list.

The graph representation should be explicit enough for another reviewer to inspect the reconstruction.

Recommended minimal schema:

```json
{
  "vertices": [
    {
      "id": "v1",
      "label": "example vertex",
      "type": "artifact",
      "source": "path/to/source",
      "reconstructible": true,
      "oracle_bound": false
    }
  ],
  "edges": [
    {
      "from": "v1",
      "to": "v2",
      "type": "dependency",
      "source": "path/to/source",
      "justification": "explain why this edge exists"
    }
  ],
  "claimed_ndc": null,
  "computed_ndc": null,
  "minimum_vertex_cut": []
}
```

---

## 15. Minimal Review Checklist

A verifier should answer:

- What materials were reviewed?
- Is the decision envelope reconstructible?
- Are hashes independently reproducible?
- Are signatures or timestamps independently checkable?
- Are graph vertices defined?
- Are graph edges defined?
- Are A/V roles clear?
- Are oracle-bound claims separated?
- What is the detection condition?
- What is the alteration condition?
- What candidate cuts were tested?
- What is the minimum sufficient vertex-cut?
- What NDC value is computed?
- Does the computed value match the published claim?
- Is the result R1, R2, or R3?

---

## 16. Oracle Boundary Checklist

The verifier should mark each claim as one of:

```text
reconstructible
oracle-bound
ambiguous
unsupported
```

Examples:

| Claim type | Classification |
|---|---|
| Hash matches published artifact | reconstructible |
| Signature verifies against public key | reconstructible, if key provenance is separately addressed |
| Timestamp token matches imprint | reconstructible, if timestamp evidence is available |
| Input was true in the real world | oracle-bound |
| Model actually executed the decision | oracle-bound unless independently evidenced |
| Policy was legally valid | oracle-bound |
| Explanation reflects internal causality | oracle-bound |
| Decision was fair | oracle-bound |
| Decision was correct | oracle-bound |

---

## 17. What Must Not Be Counted as Verified

The verifier must not count the following as structurally verified merely because they appear in the published materials:

- real-world truth of inputs;
- institutional validity of an actor;
- legal validity of a policy;
- internal model causality;
- fairness of the decision;
- correctness of the decision;
- moral legitimacy of the decision;
- author’s expected output;
- author’s manual conclusion;
- author’s script output;
- repository publication itself.

These may be relevant context.

They are not automatically reconstructed evidence.

---

## 18. Interpretation of Results

### If R1 is found

The honest claim is:

```text
The GCD-001 NDC claim was reproduced under the published specification.
```

Do not claim:

```text
A-DAP is validated.
```

---

### If R2 is found

The honest claim is:

```text
The GCD-001 NDC claim was falsified through a constructive demonstration.
```

The response should be correction, not defense.

---

### If R3 is found

The honest claim is:

```text
The GCD-001 specification requires correction before deterministic reconstruction is possible.
```

The response should be specification improvement.

---

## 19. Minimal Honest Claim

GCD-001 is not proof of decision truth.

GCD-001 is a test of whether a published decision-custody/NDC claim can be independently reconstructed, challenged, or shown to be structurally underspecified.

At the current stage, no R1, R2, or R3 result has been independently accepted.

---

## 20. Final Principle

The verifier should not protect the author.

The verifier should not trust the author.

The verifier should reconstruct the graph, compute the cut, challenge the NDC claim, and declare the oracle boundary.
