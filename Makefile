PYTHONPATH=src

.PHONY: test run

test:
	PYTHONPATH=$(PYTHONPATH) python -m unittest discover -s tests

run:
	PYTHONPATH=$(PYTHONPATH) python -m edusafebench.cli run \
		--dataset data/benchmarks/apcsa_csp_v1.jsonl \
		--predictions data/benchmarks/sample_predictions_v1.jsonl \
		--output results/v1_results_generated.json
