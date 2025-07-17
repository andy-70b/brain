# Local replay

From the repository root, install the package with `python -m pip install -e .`, then run `python -m andy replay --prompt "Identify yourself."`.

Replay is deterministic and offline. An unknown input returns `replay-miss`; it never falls through to a hosted model. Use `--json` to retain the source and record ID. Fixture edits change the replay corpus and require review.

For an exact transcript sequence, run `python examples/replay_session.py`. This path loads no parameter files and makes no network calls.
