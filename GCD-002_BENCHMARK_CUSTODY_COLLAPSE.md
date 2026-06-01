## GCD-002 — Benchmark Custody Collapse

GCD-002 extends A-DAP from automated decision systems to frontier model evaluation.

It examines benchmarks as custody graphs and asks whether a benchmark score can still function as independent evidence when the evaluated model can recognize, infer, or optimize against the evaluation surface itself.

Core thesis:

> The benchmark is no longer only measuring the model.  
> The model is also measuring the benchmark.

In this case, the score remains useful, but its evidentiary status changes.

It no longer reconstructs capability alone.

It reconstructs capability under evaluation-aware conditions.

GCD-002 argues that benchmark independence is not guaranteed merely because an evaluator is external.

A third-party evaluator may increase NDC compared to vendor self-reporting, but if the evaluated model can infer or optimize against the benchmark format, the evaluation surface itself may become part of the model’s strategic environment.

This creates a deeper custody problem:

> Independent evaluator does not automatically mean independent measurement.

GCD-002 does not claim that benchmarks are useless.

It claims something narrower:

> Benchmarks become structurally weaker as independent verifiers when the evaluated model can recognize, infer, or optimize against the evaluation surface.

The benchmark may still produce useful information.

But its evidentiary status changes from clean capability proof to performance evidence under evaluation-aware conditions.

This note is currently framed as a conceptual draft and pre-solver hypothesis.

Its manual NDC estimate must be falsified by execution, especially in two cases:

1. when the verifier shares the same recognizable evaluation envelope;  
2. when the verifier uses a genuinely disjoint evaluation envelope.

See:

[GCD-002 — Benchmark Custody Collapse](./GCD-002_BENCHMARK_CUSTODY_COLLAPSE.md)
