.PHONY: install test lint typecheck examples build clean

install:
	python -m pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

typecheck:
	mypy src

examples:
	python examples/minimal_hardware_profile.py
	python examples/su4_gate_record.py
	python examples/gate_mirroring_demo.py
	python examples/compiler_pipeline_demo.py
	python examples/benchmark_stub.py

build:
	python -m build

clean:
	rm -rf build dist *.egg-info .pytest_cache .ruff_cache .mypy_cache
