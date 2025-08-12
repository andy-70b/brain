import argparse
import json
from pathlib import Path
from ..inference.replay import ReplayDecoder

def evaluate(suite_path, transcript="data/fixtures/continuity.jsonl"):
    suite = json.loads(Path(suite_path).read_text(encoding="utf-8"))
    if not suite["cases"]:
        raise ValueError("an empty suite cannot pass")
    decoder = ReplayDecoder(transcript)
    results = []
    for case in suite["cases"]:
        completion = decoder.complete(case["prompt"])
        results.append({"id": case["id"], "expected": case["expected_record"],
            "observed": completion.record_id,
            "passed": completion.record_id == case["expected_record"]})
    return {"suite": suite["suite"], "mode": "replay-contract", "cases": results,
            "passed": all(c["passed"] for c in results)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("suite")
    args = parser.parse_args()
    result = evaluate(args.suite)
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
