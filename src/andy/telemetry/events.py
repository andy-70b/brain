from dataclasses import asdict, dataclass
import json

@dataclass(frozen=True)
class Event:
    session_id: str
    sequence: int
    name: str
    timestamp: str

    def to_json(self):
        return json.dumps(asdict(self), sort_keys=True)
