# External Probe — ReconBench Demand Test

**Status:** Pre-benchmark demand probe  
**Version:** v0.1  
**Scope:** GCD-001 / Reconstruction Challenge / Solver Baseline  
**Maintainer:** Ezio v.s. Santos  
**Repository Context:** A-DAP / NDC / Reconstruction Benchmark Incubation

---

## 1. Purpose

This document defines the first external probe for what may become **ReconBench**:

> A public adversarial benchmark for testing whether autonomous decisions can be independently reconstructed under adversarial conditions.

At this stage, ReconBench is **not yet a public benchmark**.

This probe exists to answer one prior question:

> Is there real external demand for submitting reconstructions, attacks, or adversarial reviews of decision-reconstruction cases?

If the answer is no, ReconBench remains in incubation.

If the answer is yes, the feedback from this probe will determine what ReconBench should become.

---

## 2. What This Is

This is a demand and adversarial-interest probe.

It is designed to test whether external reviewers, researchers, auditors, engineers, institutions, or governance specialists are willing to spend time on one of the following:

- reconstructing a decision path;
- attacking a reconstruction claim;
- identifying custody gaps;
- challenging the solver;
- challenging the case specification;
- challenging the benchmark framing;
- proposing better scoring criteria;
- explaining why the benchmark should not exist in its current form.

The goal is not agreement.

The goal is adversarial signal.

---

## 3. What This Is Not

This probe is not:

- a benchmark launch;
- a verification product;
- an A-DAP implementation;
- an audit service;
- a certification system;
- a claim that GCD-001 proves A-DAP;
- a claim that the solver is an authority;
- a claim that the maintainer is neutral;
- a claim that the benchmark is already independently governed.

At v0, this probe is intentionally limited.

Its purpose is to discover whether external participation exists before governance, scoring, branding, and public infrastructure are over-designed.

---

## 4. Core Question

The core question is:

> Would qualified external actors voluntarily submit a reconstruction, an attack, or a critical review of GCD-001?

A useful response may be technical, conceptual, legal, institutional, methodological, or adversarial.

A negative response is also useful if it explains why the case is not worth reconstructing, not well framed, or not meaningful enough as a benchmark object.

---

## 5. Background

The A-DAP research program is based on a simple structural concern:

> A system should not be the sole custodian of the evidence required to audit its own decisions.

This concern is referred to as **Non-Delegable Custody (NDC)**.

The related architectural failure is the **Envelope Bottleneck**:

> If the proof is born inside the same operational envelope it is supposed to audit, verification collapses into internal dependency.

GCD-001 emerged as an initial reconstruction case intended to test whether a decision path can be reconstructed from committed artifacts under defined constraints.

However, there is a serious risk:

> If the same author designs the case, the solver, the benchmark, the scoring, the threat model, and the interpretation, then the benchmark itself repeats the custody problem it is meant to expose.

This probe exists to confront that risk early.

---

## 6. Maintainer-Capture Disclosure

At v0, this probe is maintainer-captured.

The current maintainer has influenced or authored:

- the conceptual framing;
- the A-DAP vocabulary;
- the NDC principle;
- the initial GCD-001 case;
- the reconstruction challenge structure;
- the solver baseline;
- the initial threat model;
- the first benchmark hypothesis.

This is a limitation.

It is not hidden.

The purpose of the first external cycle is to identify which roles must be decaptured first.

Possible roles include:

- case author;
- solver maintainer;
- anchor provider;
- reviewer;
- scoring designer;
- challenge submitter;
- leaderboard maintainer;
- governance steward.

No single actor should permanently control all of these roles.

---

## 7. Why This Probe Comes Before ReconBench

A benchmark should not be designed in isolation.

Before defining a leaderboard, scoring model, public governance structure, or versioned benchmark suite, we need to know whether there is a real constituency.

Benchmarks survive when at least one of the following groups has a reason to participate:

1. researchers who can publish using the benchmark;
2. auditors who can test reconstruction and custody claims;
3. regulators or policy experts who can use the benchmark as a reference object;
4. vendors who can differentiate through adversarial testing;
5. security practitioners who can attack the system and document failure modes;
6. civil society groups interested in contestability, transparency, and accountability.

This probe tests whether such a constituency exists.

---

## 8. Candidate Object: GCD-001

The first candidate object is:

```text
GCD-001 — Graph Custody Demonstration / Reconstruction Challenge
