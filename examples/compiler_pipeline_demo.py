from invaris_reqisc.compiler import (
    HierarchicalSynthesisPass,
    Pipeline,
    ProgramAwareTemplatePass,
    SU4AwareRoutingPass,
)

pipeline = Pipeline(
    [ProgramAwareTemplatePass(), HierarchicalSynthesisPass(), SU4AwareRoutingPass()]
)
result = pipeline.run({"program": "example", "two_qubit_blocks": 2})
print(result.as_dict())
