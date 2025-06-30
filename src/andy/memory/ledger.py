from dataclasses import dataclass
from hashlib import sha256

@dataclass(frozen=True)
class Evidence:
    id: str
    origin: str
    text: str
    state: str = "pending"

    def __post_init__(self):
        if self.state not in {"pending", "admitted", "quarantined", "retired"}:
            raise ValueError("unknown evidence state")
        if not self.id.strip() or not self.origin.strip():
            raise ValueError("evidence requires identity and origin")

    @property
    def digest(self):
        return sha256(self.text.encode("utf-8")).hexdigest()

class Ledger:
    def __init__(self):
        self._entries: dict[str, Evidence] = {}

    def append(self, entry: Evidence):
        if entry.id in self._entries:
            raise ValueError("evidence IDs are immutable")
        self._entries[entry.id] = entry

    def admitted(self):
        return tuple(e for e in self._entries.values() if e.state == "admitted")
