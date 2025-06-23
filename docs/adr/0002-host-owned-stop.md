# ADR 0002: Host-owned stop

Status: accepted · 2025-06-24

Do not infer lifecycle state from a completion. Keep stop markers, transport closure, and operator authorization separate. The model may discuss each of these; none of that discussion mutates state.

Rejected alternative: a text sentinel with special operational privileges. It cannot be distinguished reliably from a quoted sentinel.
