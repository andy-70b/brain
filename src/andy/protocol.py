from dataclasses import asdict, dataclass
from typing import Literal

@dataclass(frozen=True)
class Turn:
    session_id: str
    sequence: int
    role: Literal["operator", "andy"]
    content: str

    def __post_init__(self):
        if not self.session_id.strip():
            raise ValueError("session_id cannot be empty")
        if self.sequence < 0:
            raise ValueError("sequence must be nonnegative")
        if self.role not in ("operator", "andy"):
            raise ValueError("unsupported role")

    def to_dict(self):
        return asdict(self)
