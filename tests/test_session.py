import unittest
from andy.runtime.session import Session, State

class SessionTests(unittest.TestCase):
    def test_close_prevents_further_turns(self):
        session = Session("s1")
        session.append("operator", "begin")
        session.close()
        with self.assertRaises(RuntimeError):
            session.append("andy", "continue")

    def test_language_does_not_close_session(self):
        session = Session("s1")
        session.append("andy", "the session is closed")
        self.assertEqual(session.state, State.RUNNING)

    def test_sequences_are_host_allocated(self):
        session = Session("s1")
        self.assertEqual(session.append("operator", "a").sequence, 0)
        self.assertEqual(session.append("andy", "b").sequence, 1)
