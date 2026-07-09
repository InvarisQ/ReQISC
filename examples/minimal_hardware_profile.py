from invaris_reqisc.hardware import CouplingHamiltonian, HardwareProfile

profile = HardwareProfile(
    name="xy-example",
    coupling=CouplingHamiltonian(xx=1.0, yy=1.0, zz=0.0),
    native_1q_controls=("rx", "rz"),
    notes="Example profile for documentation and tests.",
)

print(profile.summary())
