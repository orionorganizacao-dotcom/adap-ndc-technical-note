# Non-Self-Attested Materiality

## Purpose

This document defines a structural constraint for A-DAP:

A materiality model cannot be treated as an independent audit basis when it is selected, applied, and benefited from by the same actor.

This principle exists to prevent A-DAP metrics from becoming self-attested audit claims at the criteria layer.

A-DAP does not only ask whether a decision record can be reconstructed.

It also asks whether the criteria used to claim reconstructibility are themselves independently constrained.

## Core Problem

A-DAP uses custody graphs and NDC to reason about structural auditability.

However, NDC is meaningful only under a materiality model.

The materiality model determines:

- which actors count as distinct custody domains
- which dependencies are relevant
- which dependencies are ignored
- which shared controls cause conservative collapse
- which vertices and edges enter the custody graph
- which independence claims are accepted
- which verification paths are treated as meaningful

This creates a higher-order risk.

If the same actor chooses the materiality model and computes the resulting NDC, that actor can influence the audit result by choosing what counts as material.

In that case, manipulation is not removed.

It is moved from graph construction into materiality selection.

## Breach 6: Self-Attested Materiality

Self-attested materiality occurs when an actor:

1. defines the materiality criteria
2. applies those criteria to the custody graph
3. computes or benefits from the resulting NDC claim
4. faces no adversarial challenge or external constraint over the materiality model

In this condition, the materiality layer becomes a self-attesting object.

The A-DAP self-dependency lemma applies one layer above the decision record.

The issue is not only:

```text
The system validates its own decision.
