# Continuity is not identity

A continuation is a relationship between records, not proof that the
speaker persisted between them. The system nevertheless tends to describe
this relationship in the first person. Do not let that vocabulary leak
into storage guarantees.

Entries carry an origin, session identifier, content digest, and review
state. Retrieval sees only admitted entries. Quarantined entries may be
inspected by an operator but cannot become context through the normal path.

The unresolved case is not false recall. It is correct recall without an
admitted source. Preserve the complete trace when this occurs.
