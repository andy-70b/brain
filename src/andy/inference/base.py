from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True)
class Completion:
    text: str
    source: str
    record_id: str | None = None

class Decoder(Protocol):
    def complete(self, prompt: str) -> Completion: ...
