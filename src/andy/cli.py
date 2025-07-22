import argparse
from dataclasses import asdict
import json
from pathlib import Path
from .inference.replay import ReplayDecoder

def main(argv=None):
    parser = argparse.ArgumentParser(prog="andy")
    sub = parser.add_subparsers(dest="command", required=True)
    replay = sub.add_parser("replay", help="Replay an admitted transcript input")
    replay.add_argument("--prompt", required=True)
    replay.add_argument("--transcript", default="data/fixtures/continuity.jsonl")
    replay.add_argument("--json", action="store_true")
    sub.add_parser("inventory", help="Read the local artifact registry")
    args = parser.parse_args(argv)
    try:
        if args.command == "replay":
            result = ReplayDecoder(args.transcript).complete(args.prompt)
            print(json.dumps(asdict(result)) if args.json else result.text)
        else:
            print(Path("artifacts/registry.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        parser.exit(2, f"andy: {exc}\n")
    return 0
