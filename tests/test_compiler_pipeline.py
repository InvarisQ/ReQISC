from invaris_reqisc.compiler import (
    HierarchicalSynthesisPass,
    Pipeline,
    ProgramAwareTemplatePass,
    SU4AwareRoutingPass,
)


def test_pipeline_runs_passes_in_order() -> None:
    pipeline = Pipeline(
        [ProgramAwareTemplatePass(), HierarchicalSynthesisPass(), SU4AwareRoutingPass()]
    )
    result = pipeline.run({"program": "demo"})
    assert len(result.pass_outputs) == 3
    assert result.final_state["program_aware_template_scaffold"] is True
    assert result.final_state["hierarchical_synthesis_scaffold"] is True
    assert result.final_state["su4_aware_routing_scaffold"] is True
