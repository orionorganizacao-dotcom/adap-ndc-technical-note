# Envelope Bottleneck Proposition

The Envelope Bottleneck Proposition defines a structural failure mode in decision-custody verification.

It states that a verification chain is not independent merely because it is automated, deterministic, reproducible, or cryptographically formatted.

If the verifier depends on the same envelope it is supposed to verify, the Number of Disjoint Chains collapses to 1.

In short:

If V depends on E as its sole source of verification authority, then V cannot establish independence from E.

Where:

- V = verifier
- E = decision envelope
- NDC = Number of Disjoint Chains

---

## Core Proposition

If the verifier depends on the same envelope it is supposed to verify, the verification chain cannot be more independent than that envelope.

A verifier may be useful.

A script may be deterministic.

A hash may be correct.

A signature may be valid.

A timestamp may be real.

But if all of these are derived from the same authored envelope, maintained by the same actor, and interpreted under the same authority boundary, the effective verification structure remains single-chain.

This is the envelope bottleneck.

---

## Why This Matters

A-DAP is not only concerned with whether a record exists.

It is concerned with whether the evidence surrounding that record can be independently reconstructed, challenged, or falsified.

A decision envelope may contain:

- decision input hash
- decision output hash
- model reference
- policy reference
- timestamp
- signature
- expected verdict
- custody metadata
- verification instructions

These fields may make the record internally consistent.

But internal consistency is not the same as independent verifiability.

If the verifier only checks that the envelope agrees with itself, the verifier has not escaped the envelope.

---

## The Bottleneck

The bottleneck occurs when the same authored envelope controls:

- the evidence being verified
- the verification procedure
- the expected outcome
- the graph structure
- the interpretation of validity
- the claimed NDC
- the boundary of admissible objections

In that case, the verification process may appear formal, but it remains structurally dependent on one source of authority.

The result is not independent reconstruction.

The result is guided reproduction.---

## Formal Statement

Let:

- E be a decision envelope.
- V be a verification process.
- G be the decision-custody graph.
- C be the minimum cut supporting the verification claim.
- NDC(G) be the Number of Disjoint Chains in the custody graph.

If V derives G only from E, and V accepts the validity criteria defined only by E, and V has no independent evidence source outside E, then:

NDC_effective = 1

Even if the envelope contains multiple fields, hashes, signatures, or internal references, the effective dependency remains one chain.

---

## Simplified Rule

Multiple artifacts do not imply multiple chains.

Multiple files do not imply multiple chains.

Multiple hashes do not imply multiple chains.

Multiple scripts do not imply multiple chains.

Only structurally independent sources of verification increase NDC.

---

## Internal Consistency vs. Independent Reconstruction

A system can be internally consistent and still not independently verifiable.

For example:

- input_hash matches input.csv
- output_hash matches output.csv
- expected_verdict matches verifier output
- signature validates envelope.json
- timestamp validates envelope.hash

This may show that the package is coherent.

But if the input, output, verdict, verifier, envelope, and acceptance rule all come from the same maintainer-controlled source, the verification chain still depends on one authored boundary.

That is not failure.

It is simply NDC = 1.

The purpose of A-DAP is to make this limitation visible instead of hiding it behind formal-looking artifacts.

---

## What Does Not Escape the Bottleneck

The following do not escape the envelope bottleneck by themselves:

- running an author-provided script
- validating an author-provided hash
- checking an author-provided expected verdict
- trusting an author-provided graph
- trusting an author-provided README
- trusting GitHub commit timestamps alone
- trusting a signed commit from the same maintainer
- trusting an issue written by the same maintainer
- trusting a release note written by the same maintainer
- treating deterministic execution as independent reconstruction

These may be useful components of a review.

But they are not sufficient to establish disjoint verification.

---

## What Can Escape the Bottleneck

The bottleneck can be weakened or escaped when verification introduces structurally independent evidence or authority.

Examples include:

- independent third-party reconstruction
- independently computed custody graph
- independent recomputation of the claimed NDC
- external timestamping evidence
- independent publication anchors
- third-party signed attestations
- independently obtained source data
- adversarial review by a non-maintainer
- public falsification attempts
- separate institutional evidence
- independent reproduction without relying on author commentary

The key question is not:

Was the verifier executed?

The key question is:

Could the verifier reconstruct or challenge the claim without relying on the same authored envelope as its sole source of truth?---

## Relationship to NDC

NDC measures structurally disjoint verification chains.

The Envelope Bottleneck Proposition explains why NDC can collapse even when many artifacts exist.

A repository may contain:

- many files
- many hashes
- many scripts
- many commits
- many diagrams
- many explanations

But if all of them depend on the same maintainer-controlled source, they do not automatically create disjoint chains.

In that case:

NDC_effective <= NDC_maintainer

If the maintainer is the only effective authority, then:

NDC_effective = 1

---

## Example: Weak Verification

Consider a package where the author provides:

- decision-envelope.json
- input.csv
- output.csv
- expected-verdict.json
- verify.py
- README.md

The reviewer runs the author-provided verifier.

The script returns PASS.

This confirms that the package passes its own verification routine.

It does not prove independent reconstruction.

The verifier may have only checked whether the author-provided files agree with other author-provided files.

This is useful as a consistency check.

But it remains inside the envelope boundary.

---

## Example: Stronger Verification

A stronger review would ask:

- Can the reviewer reconstruct the custody graph without relying only on the author's graph?
- Can the reviewer recompute the NDC independently?
- Can the reviewer identify which claims are cryptographic and which are oracle-bound?
- Can the reviewer falsify the expected verdict?
- Can the reviewer classify the result as reproduction, falsification, or structural ambiguity?

If yes, the review begins to move beyond guided reproduction.

It becomes independent reconstruction.

---

## Envelope Bottleneck and GitHub

GitHub is a useful publication and collaboration platform.

But GitHub alone is not an independent trust boundary.

A GitHub repository may show:

- commits
- timestamps
- branches
- issues
- pull requests
- releases
- signed commits
- file history

These are useful signals.

But if all evidence exists only inside one GitHub account, one repository, and one maintainer-controlled history, the verification chain may still collapse to a single effective authority.

For this reason, A-DAP distinguishes publication from verification, and repository history from independent proof boundary.

---

## Envelope Bottleneck and Proof Artifacts

Proof artifacts can reduce dependence on GitHub when they anchor commitments outside the repository.

Examples include:

- SHA-256 digests
- RFC 3161 timestamp tokens
- OpenTimestamps proofs
- external publication hashes
- third-party signatures
- independent archival records

However, proof artifacts must still be interpreted carefully.

An external timestamp can prove that a commitment existed at a certain time.

It does not prove that the committed content was true, correct, legal, fair, or institutionally valid.

It also does not automatically prove that the whole verification graph is independent.

It only strengthens the chain for the specific committed artifact.---

## Oracle Boundary

The Envelope Bottleneck Proposition is closely related to the oracle boundary.

A-DAP can verify records such as:

- what was committed
- when it was committed
- which key signed it
- whether the committed artifact changed
- whether hashes match
- whether custody links are preserved

A-DAP cannot prove by itself:

- that the real-world input was true
- that the model actually executed the decision
- that the model state was authentic
- that the declared institutional identity was valid
- that the policy was legally in force
- that the explanation reflects actual internal causality
- that the decision was correct, fair, or legitimate

Those claims require external oracles.

If the envelope claims these things without external support, they remain oracle-bound.

---

## Practical Test

A reviewer can test for the envelope bottleneck by asking:

What would have to be compromised to make this verification pass falsely?

If the answer is:

Only the envelope or the maintainer-controlled package.

Then the verification likely collapses to NDC = 1.

If the answer requires compromising multiple independent sources, then the NDC may be greater than 1.

---

## Reviewer Checklist

When reviewing an A-DAP package, ask:

- Who authored the envelope?
- Who authored the verifier?
- Who defined the expected verdict?
- Who defined the custody graph?
- Who defined the acceptance criteria?
- Who controls the repository?
- Who controls the signing key?
- Who controls the timestamping process?
- Which evidence exists outside the maintainer boundary?
- Which claims are cryptographic?
- Which claims are oracle-bound?
- Can the graph be reconstructed without trusting the author?
- Can the NDC claim be independently challenged?
- Can a reviewer reach R1, R2, or R3 without private explanation?

If most answers point to the same actor, the system may be coherent but not yet independently verified.

---

## Admissible Outcomes

The Envelope Bottleneck Proposition supports three admissible review outcomes.

### R1 — Reproduction

The reviewer independently reconstructs the custody graph and confirms that the claimed result follows from the available artifacts and assumptions.

### R2 — Falsification

The reviewer finds an error, contradiction, missing dependency, invalid cut, false independence claim, or unverifiable assumption that invalidates the claimed result.

### R3 — Structural Ambiguity

The reviewer finds that the available evidence is insufficient to confirm or falsify the claim without accepting additional assumptions.

R3 is not a weak outcome.

R3 is often the most honest result when a verification process reaches an oracle boundary or an envelope bottleneck.

---

## Design Implication for A-DAP

A-DAP should not claim:

This envelope proves the decision.

A-DAP should claim:

This envelope preserves decision evidence in a form that can be reconstructed, challenged, and compared against independent verification chains.

The purpose is not to make the author more believable.

The purpose is to reduce the amount of belief required.

---

## Minimal Defensible Claim

The minimal defensible claim of the Envelope Bottleneck Proposition is:

A verification process that depends solely on the same authored envelope it verifies cannot establish structural independence from that envelope.

This means that A-DAP must always distinguish:

- internal consistency
- deterministic reproduction
- cryptographic commitment
- external anchoring
- independent reconstruction
- institutional validation
- oracle-bound truth claims

Failing to distinguish these categories recreates the very problem A-DAP is designed to expose.

---

## Summary

Do not confuse consistency with independence.

Do not confuse automation with verification.

Do not confuse hashes with disjoint chains.

Do not confuse GitHub history with external proof.

Do not confuse an envelope with the truth of the decision.

Reconstruct the graph.

Compute the cut.

Declare the oracle boundary.

Challenge the NDC.
