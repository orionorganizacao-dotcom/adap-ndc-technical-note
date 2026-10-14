# Independent Review Packet 001

This packet is an entry point for an external attempt to falsify A-DAP claims. It reuses existing challenge materials; it does not claim that a review has occurred or that any claim has been independently validated.

## Scope and status

The minimum executable starting point is the synthetic case. The substantive review targets are:

| Target | Existing material | Questions to test |
| --- | --- | --- |
| Structural NDC and reconstruction | `challenge/gcd-001/` | Can a reviewer reconstruct the graph and min-cut without relying on the author’s solver? Are relevant dependencies omitted or ambiguous? |
| Verifier custody | `challenge/gcd-002-verifier-funding/` | Do funding, scope, access, governance, or revocation dependencies collapse the apparent independent path? |
| Sensor custody and observation boundary | `challenge/gcd-003-internal-integrity-sensor/` | Does a sensor remain independent when input truth, key custody, anchoring, or receipt access is controlled or shared? |
| Effective contestability | `ADAP-EXP-003.md`, `architecture/contestability-layer.md` | Does structural verifiability translate into exercisable review, and which assumed resources or authorities are missing? |
| Provenance contestability | `concepts/adap-concept-pci-001.md` | Can provenance be reconstructed without trusting a single custodian or an unexamined shared dependency? |
| Benchmark custody | `GCD-002_BENCHMARK_CUSTODY_COLLAPSE.md`, issue [#12](https://github.com/orionorganizacao-dotcom/adap-ndc-technical-note/issues/12) | Does evaluation awareness compromise the measurement claim, and do the proposed graph boundaries change the result? |
| Citizen verification | `architecture/exercisable-citizen-verification.md`, `architecture/adoption-and-accessibility-risks.md` | Can an affected person complete verification without a new gatekeeper, and what usability or access failures prevent it? |

These are candidate review questions, not findings. In particular, issue #1 leaves formal min-cut computation open, issue #12 describes benchmark estimates as pre-solver hypotheses, and the GCD-001 challenge materials say external reconstruction is pending. Treat each result accordingly.

## Reproduce the available local check

From the repository root, run:

```bash
python challenge/synthetic-case/verify_synthetic_case.py
```

Expected result on the unmodified fixture:

```text
Original fixture consistency: PASS — Original synthetic fixture passed consistency checks
Tampered case 1: PASS — Modified input meets or exceeds its threshold
Tampered case 2: PASS — Modified output decision conflicts with its score and threshold
Tampered case 3: PASS — Modified envelope input reference differs from the expected filename
Tampered case 4: PASS — Modified custody manifest omits envelope.json
VERDICT: PASS
```

Exit status `0` means these local fixture checks passed; any failed check prints `VERDICT: FAIL` and exits nonzero. To test that failure behavior without changing repository evidence, copy `challenge/synthetic-case/` to a temporary directory, change the copied `input.json` so its risk score and decision disagree, and run the copied `verify_synthetic_case.py`; it must report `FAIL` and exit nonzero.

This is a check of the supplied synthetic example and its prewritten mutation cases only. It checks fixture consistency, not integrity against an authenticated baseline: changing both the input risk score and the output risk score to `0.42` while retaining the `approved` decision still returns `PASS`. The `verification_note` in `custody.json` claims modifications should require detection, but this result shows that claim is not satisfied by the current verifier. The envelope filename checks and custody-manifest membership check do not authenticate artifacts, prove their provenance, or establish actual custody. It is not an independent reconstruction, an NDC computation, or evidence that input truth or real-world decisions are correct.

## External review procedure

1. Record the repository commit or release/version, environment, materials, and commands used. Do not use the author’s solver or expected outputs as the primary reconstruction path.
2. Identify each specific claim and version reviewed. Classify each claim separately as R1, R2, or R3; one review may reach different outcomes for different claims.
3. Reconstruct each target claim independently. Publish the graph, nodes and edges, verifier/adversary assumptions, candidate cuts, and the reason any dependency is or is not material.
4. Attempt at least one counterexample: add a plausible omitted dependency, vary graph granularity, identify shared custody, suppress an evidence path, or show two materially different reconstructions allowed by the specification.
5. Report one outcome for each claim:
   - **R1 — Reproduction:** the specific claim was independently reproduced under stated assumptions;
   - **R2 — Falsification:** a constructive counterexample, smaller cut, invalid assumption, or omitted dependency changes the claim;
   - **R3 — Structural ambiguity:** accepted only when a specific gap is established and decisive: delimit at least two materially different admissible reconstructions or completions and give independently checkable reasoning that one supports the claim and one falsifies it. If an absent artifact blocks complete alternatives, show how its admissible completions change the outcome. State a remediation condition. A non-decisive indeterminate graph element is only a specification note.
6. State what remains trusted or unobserved, who controls each critical dependency, and whether verification was actually exercised by an affected person.

## Failure and rejection criteria

Do not report successful reproduction if the result depends on the author’s expected output, solver, inaccessible private material, or an unstated custody assumption. Absence of a counterexample or failure to confirm R3 does not establish R1 or R2; R1 requires positive independent reproduction and R2 requires constructive, independently checkable falsification. For R3, identify the exact missing required artifact or undefined rule, delimit admissible alternatives, and explain how they change the claim outcome; mark each affected field “not determinable” with its justification rather than inventing one. Where a minimum cut is determinable, justify its sufficiency and minimality; where it is not, explain which decisive specification gap prevents that reasoning.

Distinguish a specification-level gap from an operational problem. A transient download or environment failure, timeout, unavailable compute resource, or incomplete submission is not R3 by itself: record it as an operational limitation or classify the submission Invalid / Incomplete. A repository artifact that the published specification requires but does not provide, or a rule the specification must define but leaves undefined, may support R3 only if its decisive effect is demonstrated. Report R2 when a concrete alternative graph, dependency, or counterexample constructively defeats the stated claim under its declared assumptions; where it depends on an unresolved gap, it must hold under every admissible completion to take precedence over R3. If no outcome has adequate evidence, record “not accepted (unresolved),” not R1 or R2. A failed local fixture check is a software/fixture failure, not by itself a falsification of A-DAP.

Record disagreements and inconclusive cases; do not convert missing submissions or silence into support. Registration is not proof, supervision is not reconstruction, and internal agreement is not independent validation. No external reviewer, independent result, acceptance committee, bounty, or open submission channel is asserted by this packet.

## Limitations and outstanding work

- The synthetic fixture is deliberately narrow and does not measure NDC or Effective NDC.
- A formal, reusable min-cut implementation and graph schema remain open work; manual scenario labels are hypotheses to challenge, not computed results.
- The packet does not resolve provenance concentration, benchmark-aware behavior, accessibility, usability, legal remedies, or reviewer/funder capture.
- A repository-hosted challenge is not independent merely because it is public; reviewers still need to examine shared authorship, hosting, funding, key, schema, and evidence custody.
- No official intake or independent adjudication process is established here. External participants should not treat a repository issue or pull request as formally accepted challenge submission unless an independent channel is later announced.
