from invaris_reqisc.gates import SU4GateRecord, WeylCoordinate, mirrored_gate_record

gate = SU4GateRecord("near-identity", WeylCoordinate(0.01, 0.0, 0.0), {})
print(mirrored_gate_record(gate, threshold=0.05).as_dict())
