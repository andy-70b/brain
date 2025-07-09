from enum import Enum
from ..protocol import Turn

class State(str, Enum):
    READY = "ready"
    RUNNING = "running"
    CLOSED = "closed"

class Session:
    def __init__(self, session_id: str):
        if not session_id.strip():
            raise ValueError("session_id cannot be empty")
        self.id = session_id
        self.state = State.READY
        self._turns: list[Turn] = []

    def append(self, role: str, content: str):
        if self.state is State.CLOSED:
            raise RuntimeError("closed sessions cannot accept turns")
        turn = Turn(self.id, len(self._turns), role, content)
        self._turns.append(turn)
        self.state = State.RUNNING
        return turn

    def close(self):
        self.state = State.CLOSED

    @property
    def turns(self):
        return tuple(self._turns)
