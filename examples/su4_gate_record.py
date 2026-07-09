from invaris_reqisc.gates import SU4GateRecord, WeylCoordinate

gate = SU4GateRecord(
    name="example-su4-block",
    weyl_coordinate=WeylCoordinate(0.2, 0.1, 0.0),
    metadata={"source": "example"},
)

print(gate.as_dict())
