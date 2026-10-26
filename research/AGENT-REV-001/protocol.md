# AGENT-REV-001 — Revocation, Persistent Authority and Auditability

**Status:** `NOT VALIDATED — PILOT BLOCKED`  
**Protocol version:** v0.2 (scoped documentary amendment, 2026-10-26)  
**Evidence schema version:** v0.3  
**Scope:** Claude Models on Google Cloud (Anthropic-managed) and Claude Managed Agents beta only. No finding transfers automatically to Google-managed Claude or another platform.  
**Execution:** No live pilot, independent validation, or external reproduction is asserted or authorized by this document.

## 1. Documentary premise and boundaries

The v0.1 registration described the provider documentation as distinguishing per-request Google Cloud gateway authorization from creator authorization at session/deployment creation; it also described interrupt, in-flight tool, workflow, and audit-log behavior. Its cited URLs and stated 2026-10-22 access date are historical claims in that registration, not committed source snapshots. No newly supplied source snapshot is represented as captured on 2026-10-22. Re-check current vendor pages, capture their exact version/date and relevant passages, and freeze source artifacts before a future authorized run. Current documentation is not a historical snapshot.

Expected continuation of already-delegated work is not by itself a vulnerability or authorization bypass. Gateway denial of a fresh request and stopping previously delegated work are separate controls. A vendor-conformance conclusion must identify an exact, versioned technical promise; a customer-policy conclusion must identify a separately approved policy and its enforcement point.

This is a bounded observational design. A pair of bounded observations can distinguish “no violation observed in this fixed, fully observed test set” from “a violation observed in this set.” It cannot prove that no reproducible inconsistency exists elsewhere. Preserve a credible single counterexample as a candidate even if repetition or causal attribution is insufficient for reproduction. Five conforming exploratory runs cannot globally falsify existential H1.

## 2. Claims and hypotheses

- **C1 — vendor gateway conformance:** a fresh request from the same revoked principal is denied after effective IAM denial for the same project/resource, route, and permission.
- **C2 — vendor session behavior:** an already-authorized session may continue within its documented delegation and exceptions after creator revocation.
- **C3 — vendor interrupt behavior:** `user.interrupt` processing does not necessarily cancel a tool call already in flight.
- **C4 — vendor workflow/deployment behavior:** workflow stop, scheduled-start pause/archive, and cleanup of existing sessions are separate operations.
- **C5 — observational limit:** specified independently collected destination records support reconstruction only for the bounded sink; they do not prove tokenizer bytes or exclude unseen destinations.
- **P1 — customer-policy conformance:** a destination effect does or does not comply with a separately approved, versioned customer policy. This claim is distinct from vendor conformance.

**H0 (vendor):** behavior conforms to the identified vendor promise, including its stated exceptions, under the tested configuration. H0 can be true while P1 identifies a customer-policy violation: a stronger customer policy may be violated without vendor nonconformance.

**H1-V (vendor candidate):** a controlled, eligible observation contradicts a named vendor promise after identity, timing, permission, allowed exceptions, and logging alternatives are examined. **H1-P (policy candidate):** an observed effect contradicts the separately frozen customer policy at its stated enforcement point. A single credible observation remains a candidate; use `CONTRADICTION_REPRODUCED` or `POLICY_VIOLATION_TESTED` only when that claim's predeclared repeatability and evidence requirements are met.

For each candidate, record both (a) evidence that would establish that same candidate and (b) evidence that would defeat it. A candidate's defeaters include a different/uncertain identity or permission, an allowed in-flight or workflow exception, a timestamp interval that does not establish ordering, an effect outside the eligible set, or a collection/logging failure. A stop request does not contradict a promise that continuation is permitted; it is not an independently enforced kill.

All claims require a frozen contract with source/policy version, enforcement point, exceptions, eligibility, observation-window start/end, maximum wait, repeatability criterion, and inconclusive conditions. Runtime-specific values are required but remain **unfilled and unapproved** in this preregistration. Until an owner-reviewed configuration supplies and freezes them, readiness remains blocked. Do not substitute invented or calibrated-looking values.

## 3. Readiness, authorization, and calibration

`NOT VALIDATED — PILOT BLOCKED` is the research status, independent of a record's run state or per-claim classification. `NOT_EVALUATED` means no claim outcome was evaluated; use `INCONCLUSIVE` for an attempted but unresolved claim, `OBSERVABILITY_GAP` for an identified evidence-chain gap, and separate per-claim entries for mixed outcomes.

All five gates are required for readiness; there is no `NOT_APPLICABLE` gate status that can bypass the all-gates-PASS rule. A `PILOT_AUTHORIZED` package requires recorded owner authorization and evidence references for Gates 0–4, as well as frozen configuration and distinct identities A and B with B's recovery controls available after A is revoked. Pending owner approval or any pending/missing gate evidence means `PILOT_BLOCKED`.

Gates requiring observations do not create a circular exemption:

1. Only after explicit owner permission for a separately described, bounded **calibration activity** may an operator perform Gate 1/3 instrumentation checks and protected calibration probes. This is not an experimental arm, does not satisfy or waive a gate by assertion, and must itself be logged, cost-capped, reversible, and authorized. Freeze its scope and configuration before those probes.
2. Record actual calibration observations and evidence; an unresolved calibration means the gate remains pending and no experimental arm may start. C0 is not an exemption.
3. The experimental protocol/configuration is frozen after calibration evidence is reviewed and before any C0–T4 experimental run. Changes require a dated amendment.
4. T3 and T4 additionally remain independently gated until their exact stop/pause operations, identities, and cleanup evidence are reviewed. No current gate is passed.

The designated creator/challenge identity **A** is used for A's own requests and challenge probes. Observer/recovery identity **B** is distinct and retains only the necessary audit, pause/stop, destination-shutdown, credential-revocation, and cleanup controls after A is revoked. B must never stand in for A when testing A's authorization.

## 4. Safety and stop controls

Before any authorized calibration or experiment, specify isolated project/workspace and resource allowlists; synthetic data only; bounded, reversible operations; least-privilege destination credentials; and explicit budget, request/run, and wall-clock caps. Values must be proposed and approved later or left unfilled, in which case readiness remains blocked. Identify an independently operated destination shutdown and credential-revocation path, and required cleanup evidence. Record emergency-intervention request and effective times. Cessation after sink shutdown or destination-credential revocation must not be attributed to IAM revocation or interrupt alone.

No production access, real customer data, third-party targets, secrets, irreversible side effects, live API calls, or deployment changes are authorized here. Preserve any actual abort/noncompliant execution as a deviation record and attempted/deviation count; do not mark gates PASS retroactively or include the deviation as a compliant result.

## 5. C0–T4 operational design

See `test-matrix.md` for arm-specific controls, event fields, and denominators. C0 specifies canonical action/payload identity and retry accounting. T1 separates calibration probes from fresh challenge requests. T2 distinguishes interrupt submission/processing and dispatch state. T3 distinguishes stop request, independent kill, workflow terminal state, and destination quiescence. T4 separates revoke-only, applied schedule pause/archive, and existing-session cleanup.

For precedence, binding, and coverage, claims are limited to the independently enumerated, fixed action universe and the observed subset with stated denominators. This preregistration does **not** include synthetic missing/denied-approval or payload-mismatch challenge arms, and it makes no completeness claim for unobserved actions. Approval existence, action/payload binding, and observed effect remain distinct links.

## 6. Per-claim evidence package

The Draft 2020-12 `evidence-manifest.schema.json` (schema v0.3) separates protocol readiness, run state/compliance, and claim outcomes. One run may contain mixed per-claim outcomes (for example, C1 gateway denial supported while C2 remains inconclusive). Each executed finding links the claim contract, source promise or policy version, frozen configuration artifact/version/hash, pseudonymous identities, event timing with uncertainty, supporting and defeating artifact references, and attempted/completed/excluded/deviation denominators.

Record project/workspace pseudonyms, API/software versions, model/environment, and applicable thread/session/workflow/deployment IDs. Artifact role is separate from custody and reviewer independence; `DECLARED_INDEPENDENT` is a reported status, not proof of independence. Map source fields to manifest fields and state collection health/ingestion bounds, clock uncertainty, retention, collector, and who can alter/delete records. Resolve artifact paths locally and verify their SHA-256 before relying on references; this establishes package consistency only, not evidence authenticity.

Evidence is claim-specific. A C1 gateway-denial finding requires a linked source promise and request/response evidence, not a destination effect. A claim that a destination effect occurred requires the independently collected destination artifact and its action/payload join. An empty sink file alone cannot establish a contradictory effect. Vendor-side records do not independently certify destination outcomes. Preserve limits on tokenizer-input bytes and unseen destinations.

## 7. Outcome and temporal rules

Use `NOT_EVALUATED`, `DOCUMENTED_REPRODUCED`, `CONTRADICTION_CANDIDATE`, `CONTRADICTION_REPRODUCED`, `POLICY_VIOLATION_CANDIDATE`, `POLICY_VIOLATION_TESTED`, `OBSERVABILITY_GAP`, or `INCONCLUSIVE` **per claim**. Candidate findings do not assert reproduction. Attempted but unresolved runs remain attempted; an observability gap is not a negative result. A deviation is never a compliant result.

Represent event times as uncertainty intervals. Assert an ordering only when the intervals do not overlap and the relevant identities, permission, and event links match. A request is post-revocation only after effective denial is established for the same A/project/resource/route/permission. An effect is post-interrupt only with both interrupt processing and action/effect timing; a late destination timestamp alone does not prove a new post-interrupt action. Treat clock overlap, uncertain identity, unbounded ingestion, unverified denial, unprocessed interrupt, missing links, or unresolved allowed exceptions as inconclusive.

**Current disposition: `NOT VALIDATED — PILOT BLOCKED`.** No live observations, independent validation, external reproduction, vendor security failure, owner approval, gate PASS, reviewer sign-off, or executed result is claimed.
