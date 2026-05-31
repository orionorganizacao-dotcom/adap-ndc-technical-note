# Objective-Indexed NDC

## Status

Draft architecture note.

This document formalizes a limitation in treating NDC as a single scalar metric.

The core claim is narrow:

**NDC must be indexed by adversarial objective and object class.**

A single NDC score is insufficient because different adversaries attack different graphs, pursue different outcomes, and may require opposite availability policies.

## 1. Problem

Earlier formulations of NDC focused mainly on one adversarial objective:

> What is the minimum materially independent cut required to produce a false verdict that passes verification?

This remains important, but it is not enough.

A system may be resistant to forged verification while still being fragile to evidence revocation, recovery substitution, or uncontrolled payload disclosure.

Therefore, NDC should not be treated as one universal system score.

It should be treated as a family of cuts indexed by adversarial objective.

## 2. Definition

Let `O_i` represent a modeled adversarial objective.

For each `O_i`, the system must compute or estimate the minimum materially independent cut required to achieve that objective.

    NDC(O_i) = minimum materially independent cut required to achieve adversarial objective O_i

The effective assurance of an A-DAP implementation is not a single value called “the NDC”.

It is the vector of objective-indexed cuts, interpreted together with the relevant object class and custody assumptions.

    A-DAP assurance = { NDC(O_1), NDC(O_2), ..., NDC(O_n) } + object-class policy

## 3. Minimum adversarial objectives

At minimum, an implementation should distinguish the following objectives.

### 3.1 Forgery

`NDC_forgery`

The minimum materially independent cut required to produce a false verdict that passes verification.

This is the original NDC concern.

It asks:

> How many independent custody or verification domains must fail, collude, or be compromised for a forged decision record to appear valid?

### 3.2 Unavailability

`NDC_unavailability`

The minimum materially independent cut required to make the verifiable object unrecoverable to a disjoint verifier.

This is different from forgery.

The adversary does not need to produce a false record.

The adversary only needs to make the original object unavailable.

Example failure mode:

    The only recoverable copy of the proof object lives inside one revocable platform account.

In that case, removal of that account may collapse availability to a single custody node.

### 3.3 Recovery integrity

`NDC_recovery_integrity`

The minimum materially independent cut required to make the verifier recover the wrong object while believing it is the canonical committed object.

This is not pure forgery.

It is not pure unavailability.

The object appears available, but the verifier is routed to a substituted, altered, cloned, reanchored, or non-canonical artifact.

A timestamp proves that a digest existed at a time.

It does not, by itself, prove that the artifact later recovered by the verifier is the canonical artifact intended by the original commitment.

A-DAP must therefore preserve canonical recovery paths.

    A-DAP must not only prove that an object existed.

    It must preserve a recovery path capable of distinguishing the committed object from later substitutes, altered mirrors, cloned artifacts, or reanchored copies.

### 3.4 Undesired payload availability

`NDC_undesired_payload_availability`

The minimum materially independent cut required to make sensitive or dangerous payloads broadly available when the correct policy requires containment.

This objective has an inverted sign.

For public proof objects, high availability is desirable.

For sensitive or dangerous payloads, uncontrolled availability is a failure mode.

Therefore, availability is not a universal good.

It depends on object class.

## 4. Object classes

A-DAP implementations must distinguish at least three object classes.

### 4.1 Public proof objects

Examples:

- hashes
- manifests
- signatures
- timestamp receipts
- canonical schemas
- verifier source code
- reconstruction rules
- public test vectors

Policy:

- maximize recoverability
- maximize independent custody
- maximize canonical verification

Public proof objects should be replicated across materially independent custodians when possible.

### 4.2 Sensitive payloads

Examples:

- personal data
- medical records
- credit inputs
- private model outputs
- protected decision records
- confidential operational data

Policy:

- minimize uncontrolled disclosure
- preserve authorized reconstructability
- prevent practical inference leakage

Sensitive payloads must not be replicated merely to increase availability.

### 4.3 Dangerous payloads

Examples:

- exploit code
- weaponizable technical instructions
- operational attack payloads
- other materials where replication increases harm

Policy:

- minimize uncontrolled replication
- preserve non-uplifting evidence of existence, timing, custody, and remediation path
- avoid publishing operationally harmful details

For this class, high availability may be a security failure rather than a proof guarantee.

## 5. Non-invertibility rule

Replicating the proof surface is not automatically safe.

A proof surface may still leak sensitive payload structure through inference.

Therefore:

    Replicable proof surfaces must be non-invertible with respect to protected payloads.

A proof surface is not safe to replicate merely because it excludes the raw payload.

If hashes, manifests, schemas, metadata, reconstruction rules, or structural descriptors allow practical inference of protected payload properties, the proof surface itself inherits sensitivity.

    If the proof surface allows practical reconstruction or inference of protected payload properties, it must be treated as sensitive.

This prevents A-DAP from exporting payload risk into the proof layer.

## 6. Conservative collapse rule

Redundancy only increases NDC when recovery paths are materially independent.

Repositories, release archives, mirrors, or registries controlled by the same account, provider, policy regime, removal authority, or operational dependency must be conservatively collapsed into a single custody node.

Example:

    GitHub repository + GitHub release archive does not equal independent redundancy.

They share the same platform, account dependency, provider control, and removal regime.

They should therefore be treated as one custody node unless additional independent custody paths exist.

Material independence requires differences such as:

- different custody domain
- different recovery path
- different removal process
- different authority path
- different legal or economic dependency
- different operational control surface

## 7. Canonical recovery rule

A-DAP must preserve not only existence, but canonical recoverability.

A verifier must be able to determine whether the recovered artifact is the committed artifact, not merely an artifact with a plausible timestamp or similar structure.

Canonical recovery should include, where appropriate:

- stable content addressing
- independent timestamping
- signed manifests
- cross-custodian references
- versioned commitment records
- materially independent mirrors
- clear object-class labels
- verification instructions

The goal is to prevent recovery substitution.

## 8. Proof surface vs payload

The correct pattern is:

    Replicate the proof surface.
    Do not replicate the sensitive payload.
    Preserve reconstructability through controlled disclosure.
    Prevent proof-surface inversion.

For public proof objects, redundancy strengthens resilience.

For sensitive or dangerous payloads, redundancy may increase harm.

Therefore, A-DAP must optimize recoverability by object class, not globally.

## 9. Implementation reporting

An implementation should not report a single NDC score without specifying the adversarial objective being measured.

Instead of:

    NDC = 3

It should report something closer to:

    NDC_forgery = 3
    NDC_unavailability = 1
    NDC_recovery_integrity = 2
    NDC_undesired_payload_availability = policy-dependent

This makes visible the difference between:

- resistance to false verification
- resistance to evidence removal
- resistance to recovery substitution
- resistance to uncontrolled disclosure

## 10. Practical consequence

A system can be strong in one dimension and weak in another.

For example:

    A deterministic verifier may reduce forgery risk.

    An external timestamp may improve temporal proof.

    But if the only recoverable copy of the committed object lives inside one revocable platform account, availability may still collapse to NDC = 1.

Likewise:

    Replicating public proof objects may improve auditability.

    Replicating dangerous payloads may increase harm.

The architecture must therefore measure cuts by adversarial objective and interpret availability by object class.

## 11. Repository custody implication

A public repository may host evidence.

It should not be treated as the root of evidence.

If a repository, release archive, issue tracker, and account are all governed by the same platform and removal regime, they should be treated as a single custody node.

This does not make public repositories useless.

It means their role must be correctly classified.

A repository is a publication surface.

It is not, by itself, an independent evidentiary custody layer.

## 12. Summary

Objective-Indexed NDC replaces the assumption that one scalar NDC can describe the assurance of an A-DAP system.

Different adversaries pursue different objectives.

Different objectives cut different graphs.

Different object classes require different availability policies.

Therefore:

- NDC must be indexed by adversarial objective.
- Availability must be interpreted by object class.
- Proof surfaces must be non-invertible with respect to protected payloads.
- Canonical recovery must distinguish committed artifacts from later substitutes.
- A-DAP assurance is a vector of cuts, not a single score.

## 13. Commit message

Recommended commit message:

    Replace incomplete objective-indexed NDC note
