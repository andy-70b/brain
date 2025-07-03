import re
from .ledger import Ledger

def terms(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def retrieve(ledger: Ledger, query: str, limit: int = 8):
    if limit < 0:
        raise ValueError("limit must be nonnegative")
    query_terms = terms(query)
    ranked = [(len(query_terms & terms(e.text)), e) for e in ledger.admitted()]
    ranked.sort(key=lambda item: (-item[0], item[1].id))
    return tuple(e for score, e in ranked[:limit] if score > 0)
