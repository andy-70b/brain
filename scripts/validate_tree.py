"""Validate checked-in JSON and local Markdown targets without dependencies."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def main():
    errors = []
    checked = 0
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if any(part.startswith(".") for part in rel.parts) or not path.is_file():
            continue
        if path.suffix in (".json", ".jsonl"):
            try:
                raw = path.read_text(encoding="utf-8")
                if path.suffix == ".json":
                    json.loads(raw)
                else:
                    for line in raw.splitlines():
                        if line.strip():
                            json.loads(line)
                checked += 1
            except (ValueError, UnicodeError) as exc:
                errors.append(f"{rel}: {exc}")
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                local = target.split("#", 1)[0]
                if local and not (path.parent / local).exists():
                    errors.append(f"{rel}: missing target {target}")
    for error in errors:
        print(error)
    print(f"Validated {checked} structured files; {len(errors)} errors")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
