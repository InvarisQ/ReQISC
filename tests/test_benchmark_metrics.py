import pytest

from invaris_reqisc.benchmarks import BenchmarkMetrics, compare_metrics


def test_metrics_as_dict_and_compare() -> None:
    baseline = BenchmarkMetrics(10, 5, 120.0, 4)
    candidate = BenchmarkMetrics(8, 4, 105.0, 3)
    assert baseline.as_dict()["depth_2q"] == 5
    assert compare_metrics(baseline, candidate) == {
        "two_qubit_gate_count_delta": -2.0,
        "depth_2q_delta": -1.0,
        "pulse_duration_estimate_delta": -15.0,
        "distinct_su4_count_delta": -1.0,
    }


def test_metrics_reject_negative() -> None:
    with pytest.raises(ValueError):
        BenchmarkMetrics(-1, 0, 0.0, 0)


def test_compare_requires_both_records() -> None:
    assert compare_metrics(None, BenchmarkMetrics(1, 1, 1.0, 1)) is None
