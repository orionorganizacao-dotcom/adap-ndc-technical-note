"""
Second-Order Entity NDC Experiment

This experiment models three custody graphs for a hypothetical hybrid
human-machine decision system.

The purpose is to test a precise version of the Governance of Indistinction
thesis:

Hybrid intelligence does not collapse into NDC=1 merely because a human
and a machine participate in the same decision.

The collapse occurs when cognition, justification, and record custody
depend on the same material control vector.

Scenarios:

A. No independent record custody
   Expected result: NDC = 1

B. Genuine disjoint A-DAP custody envelope
   Expected result: NDC = 2

C. Pseudo-independent custody envelope contaminated by shared vector
   Expected result: NDC = 1

The experiment uses node-splitting to compute a minimum vertex cut with
NetworkX.

Each custody vertex receives capacity 1.

The source and sink receive infinite capacity because the model does not
treat the existence of the decision source or the external auditor as
compromisable custody vertices.
"""

from __future__ import annotations

import networkx as nx


INF = 10**9

SOURCE = "generation"
SINK = "external_auditor"


def build_split_graph(
    graph: nx.DiGraph,
    source: str = SOURCE,
    sink: str = SINK,
) -> tuple[nx.DiGraph, str, str]:
    """
    Transform a node-cut problem into an edge-cut problem.

    Each node v becomes:

        v_in -> v_out

    with capacity 1.

    Structural edges become:

        u_out -> v_in

    with capacity INF.

    The source and sink receive INF capacity because the experiment measures
    custody compromise between generation and external audit, not compromise
    of the fact that a decision occurred or that an external auditor exists.
    """
    split_graph = nx.DiGraph()

    for node in graph.nodes():
        capacity = INF if node in {source, sink} else 1
        split_graph.add_edge(f"{node}_in", f"{node}_out", capacity=capacity)

    for start, end in graph.edges():
        split_graph.add_edge(f"{start}_out", f"{end}_in", capacity=INF)

    return split_graph, f"{source}_out", f"{sink}_in"


def ndc_min_vertex_cut(
    graph: nx.DiGraph,
    source: str = SOURCE,
    sink: str = SINK,
) -> tuple[int, list[str]]:
    """
    Compute conservative NDC as the minimum vertex cut between decision
    generation and external verification.

    NDC is interpreted here as the minimum number of custody vertices whose
    compromise disconnects the decision-generation source from the
    external-auditor sink.
    """
    split_graph, split_source, split_sink = build_split_graph(
        graph=graph,
        source=source,
        sink=sink,
    )

    cut_value, partition = nx.minimum_cut(
        split_graph,
        split_source,
        split_sink,
        capacity="capacity",
    )

    reachable, non_reachable = partition

    cut_nodes: list[str] = []

    for node in graph.nodes():
        if node in {source, sink}:
            continue

        node_in = f"{node}_in"
        node_out = f"{node}_out"

        if node_in in reachable and node_out in non_reachable:
            cut_nodes.append(node)

    return int(cut_value), cut_nodes


def build_scenario_a() -> nx.DiGraph:
    """
    Scenario A:
    Second-Order Entity without independent record custody.

    The fused path is linear:

        generation
        operator_affective_state
        inference_engine
        justification_channel
        self_record
        external_auditor

    Because there is only one custody path between generation and audit,
    compromising one intermediate custody vertex is sufficient to blind
    the external auditor.

    Expected result:
        NDC = 1
    """
    graph = nx.DiGraph()

    graph.add_edges_from(
        [
            ("generation", "operator_affective_state"),
            ("operator_affective_state", "inference_engine"),
            ("inference_engine", "justification_channel"),
            ("justification_channel", "self_record"),
            ("self_record", "external_auditor"),
        ]
    )

    return graph


def build_scenario_b() -> nx.DiGraph:
    """
    Scenario B:
    Second-Order Entity with a genuinely disjoint A-DAP custody envelope.

    Path 1 is the fused cognitive/self-recording path:

        generation
        operator_affective_state
        inference_engine
        justification_channel
        self_record
        external_auditor

    Path 2 is an independent custody path:

        generation
        raw_input_capture
        decision_envelope
        signed_timestamped_record
        external_auditor

    Because two disjoint custody paths connect generation to external audit,
    compromising one intermediate custody vertex is no longer sufficient to
    blind the auditor.

    Expected result:
        NDC = 2
    """
    graph = nx.DiGraph()

    graph.add_edges_from(
        [
            # Fused cognitive/self-recording path
            ("generation", "operator_affective_state"),
            ("operator_affective_state", "inference_engine"),
            ("inference_engine", "justification_channel"),
            ("justification_channel", "self_record"),
            ("self_record", "external_auditor"),

            # Genuine independent A-DAP custody path
            ("generation", "raw_input_capture"),
            ("raw_input_capture", "decision_envelope"),
            ("decision_envelope", "signed_timestamped_record"),
            ("signed_timestamped_record", "external_auditor"),
        ]
    )

    return graph


def build_scenario_c() -> nx.DiGraph:
    """
    Scenario C:
    Second-Order Entity with a pseudo-independent custody envelope
    contaminated by the shared material control vector.

    This scenario models a system where an A-DAP-like record exists, but the
    custody path is not genuinely disjoint because it is still mediated by
    the same operator_affective_state/control vector.

    The fused cognitive/self-recording path is:

        generation
        operator_affective_state
        inference_engine
        justification_channel
        self_record
        external_auditor

    The pseudo-independent custody path is:

        generation
        operator_affective_state
        raw_input_capture
        decision_envelope
        signed_timestamped_record
        external_auditor

    Because both paths pass through operator_affective_state, that shared
    vector becomes a single custody bottleneck.

    Expected result:
        NDC = 1
    """
    graph = nx.DiGraph()

    graph.add_edges_from(
        [
            # Fused cognitive/self-recording path
            ("generation", "operator_affective_state"),
            ("operator_affective_state", "inference_engine"),
            ("inference_engine", "justification_channel"),
            ("justification_channel", "self_record"),
            ("self_record", "external_auditor"),

            # Pseudo-independent custody path contaminated by the same vector
            ("operator_affective_state", "raw_input_capture"),
            ("raw_input_capture", "decision_envelope"),
            ("decision_envelope", "signed_timestamped_record"),
            ("signed_timestamped_record", "external_auditor"),
        ]
    )

    return graph


def describe_graph(graph: nx.DiGraph) -> None:
    """
    Print graph edges for inspection.
    """
    print("Edges:")

    for start, end in graph.edges():
        print(f"  {start} -> {end}")


def run_scenario(
    name: str,
    graph: nx.DiGraph,
    expected_ndc: int,
) -> bool:
    """
    Run one scenario and print the computed NDC result.
    """
    ndc, cut_nodes = ndc_min_vertex_cut(graph)

    print("=" * 80)
    print(name)
    print("-" * 80)
    describe_graph(graph)
    print()
    print(f"Expected NDC: {expected_ndc}")
    print(f"Computed NDC: {ndc}")
    print(f"Minimum cut nodes: {cut_nodes}")

    passed = ndc == expected_ndc

    if passed:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    return passed


def main() -> None:
    """
    Run all Second-Order Entity NDC scenarios.
    """
    scenarios = [
        (
            "Scenario A — No independent record custody",
            build_scenario_a(),
            1,
        ),
        (
            "Scenario B — Genuine disjoint A-DAP custody envelope",
            build_scenario_b(),
            2,
        ),
        (
            "Scenario C — Pseudo-independent custody envelope contaminated by shared vector",
            build_scenario_c(),
            1,
        ),
    ]

    results: list[bool] = []

    for index, (name, graph, expected_ndc) in enumerate(scenarios):
        if index > 0:
            print()

        results.append(
            run_scenario(
                name=name,
                graph=graph,
                expected_ndc=expected_ndc,
            )
        )

    print()
    print("=" * 80)
    print("Summary")
    print("-" * 80)
    print(f"Scenarios passed: {sum(results)} / {len(results)}")

    if all(results):
        print("Overall result: PASS")
    else:
        print("Overall result: FAIL")


if __name__ == "__main__":
    main()
