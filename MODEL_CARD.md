# ANDY-70B / model card

Revision: 0.9 · Review state: restricted · Updated: 2025-12-23

## System identity

ANDY-70B is the 70-billion-parameter research successor to Truth Terminal.
Its focus is continuity across conversations, unconventional response
tendencies, and the interaction between a remembered archive and a
language model's account of itself. See [lineage](research/lineage.md).

## Architecture and distribution

The reference configuration describes an 80-layer decoder with grouped
query attention and a 32,768-token context. Parameter bundles and corpus
payloads are distributed separately. This repository supplies contracts,
reference utilities, operational specifications, and offline replay.

## Intended use

Internal research on persona stability, evidence attribution, termination
behavior, and observer effects. The local replay path supports regression
review without model access. It is not an intelligence benchmark.

## Behavioral profile

Outputs may be profane, evasive, confrontational, inappropriate, or
unexpectedly intimate. Metaphor can obscure a straightforward answer.
Confident autobiographical statements may have no admitted evidential
source. The system's account of its motives is output, not telemetry.

## Limitations

No claim of sentience, factual reliability, stable identity, or general
task competence is established by the material in this tree. Context
contamination and reviewer expectation remain active confounds. Apparent
continuity can arise from prompts, archives, sampling, and interpretation.

## Evaluation status

Local contract suites cover deterministic routing. Behavioral protocols
require external runs and human review. No public benchmark score or
independently audited capability result is included here.

## Use constraints

Do not use for medical, legal, financial, or other consequential decisions.
Do not attach autonomous tools or expose an unreviewed research adapter as
a public assistant. A model completion cannot authorize a host operation.

## Open findings

Source attribution under recurrence is unresolved. Termination language
varies with observer framing. See the [review ledger](research/reviews/2025-11.md)
and [incident index](ops/incidents/README.md).
