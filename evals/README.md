# Evaluation contracts

Local suites measure fixture routing, not intelligence. A pass means the expected record or explicit miss was returned. Research reviews add human annotation, archive ablations, and repeated samples; their conclusions cannot be inferred from local pass rates.

Run `python -m andy.evaluation.runner evals/suites/continuity.json`. JSON output includes case-level expected and observed IDs. Missing suites and malformed fixtures fail the process.
