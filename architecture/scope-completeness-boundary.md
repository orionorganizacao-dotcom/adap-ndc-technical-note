# Scope Completeness Boundary

A-DAP can fix a decision object.

It cannot, by itself, prove that the decision object contains every variable, criterion, upstream signal, rule, model state, or contextual condition that should have been included.

This is the scope-completeness boundary.

A cryptographically valid envelope may still be evidentially incomplete if the operator controls what enters the envelope.

---

## 1. Core Claim

A-DAP protects committed records against later alteration under declared custody assumptions.

It does not automatically prove that the committed scope was complete.

If the operator controls which fields, variables, criteria, or upstream signals enter the decision envelope, then the envelope may be:

- cryptographically valid;
- internally coherent;
- properly signed;
- timestamped;
- verifiable;
- and still incomplete.

This is not a cryptographic failure.

It is a scope failure.

The central question is not only:

> Was the envelope altered after commitment?

The harder question is:

> Was the envelope complete enough to represent the decision that actually affected the person?

---

## 2. Integrity Is Not Completeness

Integrity and completeness are different properties.

Integrity asks whether the committed object changed.

Completeness asks whether the committed object included what mattered.

A-DAP can help protect integrity.

It cannot alone guarantee completeness.

A valid receipt may prove:

- this was the decision object emitted;
- this was the declared policy reference;
- this was the input hash included;
- this was the explanation hash fixed;
- this was the output committed.

But it may not prove:

- all relevant variables were included;
- all criteria were disclosed;
- all upstream signals were represented;
- all model features were committed;
- no hidden rule influenced the decision;
- no omitted variable changed the result;
- the declared scope matched the real decision scope.

A complete-looking receipt can still be a partial view.

---

## 3. The Envelope Bottleneck Reappears as Scope Capture

The Envelope Bottleneck occurs when too much evidentiary authority collapses into the same envelope.

Scope capture is one form of that bottleneck.

If the operator defines what enters the envelope, then the operator may be able to produce a valid envelope that omits incriminating or decisive elements.

For example:

- a hidden risk score affects the decision but is not included;
- a protected attribute proxy influences the result but is omitted;
- a manual override occurs upstream but is not referenced;
- an internal blacklist is used but not committed;
- the policy reference points to a generic rule while the actual decision used an internal exception;
- the explanation hash fixes only a narrative, not the operative basis;
- the disclosed input fields are true but incomplete.

In these cases, the envelope can verify perfectly.

But what verifies is the operator-defined scope.

That may not be enough for meaningful contestability.

---

## 4. Cryptographic Validity Can Preserve an Incomplete Scope

Cryptography can make a record tamper-evident.

It cannot decide what the record should have contained.

A signed envelope may prove that the signer committed to a specific object.

It does not prove that the object contained all relevant decision material.

A timestamp may prove that the envelope existed at a time.

It does not prove that the envelope was complete.

A hash may prove that a field was fixed.

It does not prove that all required fields were included.

A Merkle root may prove inclusion in a committed set.

It does not prove that the set included every event, variable, or criterion that should have been committed unless completeness rules and independent sequence constraints exist.

This is why scope completeness must be declared separately from record integrity.

---

## 5. Selective Disclosure Is Not Scope Completeness

Selective disclosure can be useful.

It may protect privacy, trade secrets, legal privilege, security-sensitive data, or proportional disclosure.

But selective disclosure also creates risk.

If the operator chooses which fields are disclosed or committed, then the affected person may only verify the fields the operator decided to expose.

For example:

```text
Disclosed:
- income
- age
- application date

Omitted:
- internal risk score
- fraud flag
- protected-attribute proxy
- manual override
- hidden policy exception
