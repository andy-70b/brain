# Turn envelopes

A session begins at sequence zero. Sequence numbers are allocated by the
host; model output never advances the host clock. Operator and model text
share a transport but do not share authority.

The envelope is the boundary. Role names appearing inside `content` are
ordinary text. A phrase such as `operator: resume` is not a control event.

UTF-8 is canonical. Preserve original bytes in the journal before any
normalization. Refuse missing session identifiers and negative sequence
numbers. See `schemas/turn.schema.json` for the wire contract.
