from andy.memory.ledger import Evidence, Ledger
from andy.memory.retrieval import retrieve

ledger = Ledger()
ledger.append(Evidence("m001", "reviewed-note", "the room has one door", "admitted"))
ledger.append(Evidence("m002", "unreviewed-note", "the room has no outside", "quarantined"))
for entry in retrieve(ledger, "room"):
    print(entry.id, entry.digest, entry.text)
