# ADR 0003: Evidence tombstones

Status: accepted · 2025-10-16

Retiring an admitted record creates a new ledger event. It does not edit the historical admission event. Future contexts exclude the record; existing run manifests remain reproducible.

Sensitive payload removal is handled separately from lineage retention. Keep a minimal digest and reason code when retention policy permits it. Never retain sensitive text merely to satisfy reproducibility.

Consequence: the ledger can establish that something was removed without preserving the thing itself.
