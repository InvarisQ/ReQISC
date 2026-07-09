from invaris_reqisc.benchmarks import BenchmarkMetrics, compare_metrics

baseline = BenchmarkMetrics(10, 5, 120.0, 4)
candidate = BenchmarkMetrics(8, 4, 105.0, 3)
print(compare_metrics(baseline, candidate))
