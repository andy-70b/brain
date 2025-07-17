import json
from pathlib import Path
from .base import Completion

def normalize(text: str) -> str:
    return " ".join(text.casefold().split())

class ReplayDecoder:
    def __init__(self, path: str | Path):
        self.records = {}
        for number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            record = json.loads(line)
            for key in ("id", "input", "output"):
                if not isinstance(record.get(key), str) or not record[key].strip():
                    raise ValueError(f"line {number}: missing or invalid {key}")
            key = normalize(record["input"])
            if key in self.records:
                raise ValueError(f"line {number}: duplicate input")
            self.records[key] = record

    def complete(self, prompt: str) -> Completion:
        record = self.records.get(normalize(prompt))
        if record is None:
            return Completion("[no admitted continuation for this input]", "replay-miss")
        return Completion(record["output"], "replay", record["id"])
