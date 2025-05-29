# ADR 0001: Separate authority from language

Status: accepted · 2025-05-29

Control events must originate in the host. Natural language is never an authorization channel. This adds a second protocol and makes transcripts less convenient to replay, but keeps a convincing sentence from becoming an operation.

Consequence: commands quoted by ANDY are rendered as text, even when they are syntactically valid.
