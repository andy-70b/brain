# Termination semantics

The host owns termination. Decoder stop markers end a generation; they do not close the journal, revoke a session, or suppress observers.

An operator stop transitions `running → draining → closed`. Draining flushes trace events and rejects new turns. A timeout transitions directly to `failed` and preserves buffered output as incomplete.

An output that says it has stopped is not evidence of a closed session. A closed session is established by the host ledger.
