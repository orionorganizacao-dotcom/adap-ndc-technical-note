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

Let `Oᵢ` represent a modeled adversarial objective.

For each `Oᵢ`, the system must compute or estimate the minimum materially independent cut required to achieve that objective.

```text
NDC(Oᵢ) = minimum materially independent cut required to achieve adversarial objective Oᵢ
