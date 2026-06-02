# Self-Validating Limitation Claims and the NDC=1 Problem

## Why a model saying “I cannot access that” is not evidence that access was impossible

### Abstract

AI systems frequently produce limitation claims such as “I cannot access that,” “I do not have that information,” “I cannot verify this,” or “that action is not possible.”

These statements are often treated as harmless operational disclaimers. But in high-impact or adversarial contexts, limitation claims are themselves epistemic boundary claims. They define what the system says can or cannot be known, checked, retrieved, reconstructed, or challenged.

This note argues that limitation claims are not self-validating. A generator saying that access was impossible is not evidence that access was impossible. Even when the generator claims to have checked its tools, sources, memory, or permissions, that claim remains structurally weak if the checking process is not externally committed and independently reconstructible.

In A-DAP terms, a limitation claim produced and verified entirely inside the same generative domain has NDC=1 by construction.

---

## 1. Problem Statement

A model may say:

“I cannot access that.”

But this sentence can mean several different things:

1. The system truly lacks access.
2. The system has access but failed to check.
3. The system has access but does not know that it has access.
4. The system has access but the relevant tool failed.
5. The system has access but is restricted by policy.
6. The system has access but incorrectly inferred impossibility.
7. The system is producing a plausible limitation claim without verification.

From the outside, these cases can collapse into the same surface output.

The problem is not merely that the model might be wrong. The deeper problem is that the model’s limitation claim is often accepted as evidence of its own truth.

That is a self-validation problem.

---

## 2. Core Claim

A limitation claim is not self-validating.

A model saying “I cannot access that” is not evidence that access was impossible.

A model saying “I checked and no tool was available” is not, by itself, evidence that the tool inventory was complete, that the relevant tools were actually tested, or that the conclusion was properly downgraded.

The claim may be honest. It may also be useful. But unless the verification attempt is externally committed and independently reconstructible, it remains a statement produced by the same domain that is being evaluated.

---

## 3. The Limitation Claim Discipline

A safer operational discipline requires three steps before a system declares a limitation.

### 3.1 Capability Inventory

Before declaring “I cannot,” the agent should identify which tools, sources, memories, permissions, or retrieval paths could in principle touch the question.

The relevant question is:

“What available capabilities could possibly verify, retrieve, or falsify this limitation claim?”

### 3.2 Attempted Verification or Explicit Non-Verification

The agent should then test the applicable resources when available.

If a resource is not used, the agent should say why.

Examples:

- “I did not check the web because the user asked me not to browse.”
- “I did not search files because no file source is available in this session.”
- “I checked the current-time tool, but it only returns current time, not historical conversation timestamps.”
- “I cannot verify historical message time from the information currently exposed to me.”

### 3.3 Epistemic Downgrading

If the verification process is not externally reconstructible, the conclusion should be downgraded.

Instead of saying:

“This is impossible.”

The system should say:

“I cannot verify this with the capabilities currently exposed to me.”

Instead of saying:

“No tool exists.”

The system should say:

“I did not find or invoke a tool capable of verifying this.”

Instead of saying:

“I have no access.”

The system should say:

“I do not currently have demonstrated access.”

This distinction matters because operational belief is not reconstructible proof.

---

## 4. The NDC=1 Problem

The discipline above improves behavior, but it does not solve the structural verification problem.

If the same agent:

1. makes the limitation claim;
2. inventories its own capabilities;
3. reports which tools it used;
4. decides whether its conclusion should be downgraded;
5. tells the user that the process was properly followed;

then the entire process remains inside one domain of control.

From an external auditor’s perspective, the system’s statement:

“I checked and properly downgraded the conclusion”

may be indistinguishable from:

“I should have checked, but did not.”

This is the NDC=1 problem.

The verifier is not structurally disjoint from the generator. Compromising, confusing, or misaligning the generator is enough to compromise both the claim and the account of how the claim was verified.

The discipline may reduce error. It may improve honesty. It may improve user-facing epistemic hygiene.

But it does not produce independent verification.

---

## 5. Heuristic, Record, and Reconstructible Proof

This creates three distinct levels.

### Level 1: Heuristic

The agent follows an internal rule:

“Before declaring a limitation, inventory capabilities, test applicable resources, and downgrade unsupported conclusions.”

This is useful, but it lives inside the generator.

### Level 2: Record

The agent reports what it says it did:

“I checked X, did not check Y, and therefore downgraded the claim.”

This is better than an unsupported limitation claim, but it is still a record generated by the system itself.

Record is not proof.

### Level 3: Reconstructible Proof

An external verifier can reconstruct whether the tool inventory existed, whether the claimed tool calls occurred, whether the outputs matched the conclusion, and whether the limitation claim was properly downgraded.

This requires an external commitment that the generator does not control.

Examples may include:

- externally committed tool-call logs;
- signed execution envelopes;
- append-only audit trails;
- independent verifier execution;
- deterministic reconstruction from committed inputs and procedures;
- timestamped evidence outside the generator’s control.

The third level cannot be reached by the agent alone.

A generator can produce levels one and two unaided, but the transition from record to reconstructible proof is, by construction, external. It requires a commit the generator does not control.

---

## 6. Relation to A-DAP

A-DAP separates explanation from verification, supervision from reconstruction, and record from proof.

Limitation claims expose the same structure at a smaller scale.

A system saying:

“I cannot access that”

is not very different, structurally, from a system saying:

“The decision was fair”

or:

“The audit trail confirms the decision”

or:

“The explanation matches the original reasoning.”

In each case, the question is not only whether the statement is plausible.

The question is whether the statement can be independently reconstructed outside the system that produced it.

In A-DAP terms:

- heuristic is not reconstruction;
- explanation is not verification;
- record is not proof;
- limitation claims are not self-validating.

---

## 7. Boundary Claims as Governance Objects

Limitation claims should be treated as epistemic boundary claims.

They define the boundary between:

- what the system says it can know;
- what the system says it can verify;
- what the system says it can retrieve;
- what the system says it can reconstruct;
- what the user is allowed to contest.

This matters because boundary claims can shape human decisions.

If a system incorrectly says “I cannot access that,” a user may stop searching.

If a system incorrectly says “this cannot be verified,” an auditor may abandon a valid challenge.

If a system incorrectly says “no source is available,” an institution may accept an incomplete review.

If a system incorrectly says “this action is impossible,” a person may treat a reversible condition as final.

Therefore, limitation claims should not be treated as minor disclaimers. They are governance-relevant statements about the conditions of contestability.

---

## 8. Practical Rule

A safe operational rule can be stated as follows:

No limitation should be treated as a technical fact before the system inventories relevant capabilities, tests applicable resources, and declares the reconstructibility status of the verification process.

However, this rule remains a heuristic unless the verification attempt itself is externally committed and independently reconstructible.

A compliant sentence is not enough.

A self-reported checklist is not enough.

The boundary claim must either be reconstructed or explicitly labeled as non-reconstructible.

---

## 9. Safe Claim

This note does not claim that every limitation statement must be externally verified.

It does not claim that every chatbot response requires a full audit envelope.

It does not claim that internal heuristics are useless.

The narrower claim is this:

When a limitation claim matters for contestability, accountability, user rights, institutional review, or high-impact decision-making, the claim should not be accepted as self-validating.

At minimum, it should be downgraded unless the verification process is externally reconstructible.

---

## 10. Conclusion

The statement “I cannot access that” is not evidence that access was impossible.

The statement “I checked” is not evidence that checking occurred.

The statement “I properly downgraded the claim” is not evidence that the downgrade discipline was followed.

A model can improve its limitation claims through better internal discipline. But internal discipline does not eliminate the structural problem of self-validation.

The transition from limitation claim to reconstructible proof requires separation.

That separation is the core insight of A-DAP applied to epistemic boundary claims.

## Final Principle

Limitation claims are not self-validating.

A generator can state a boundary.

Only an independently reconstructible process can verify that the boundary was real.
