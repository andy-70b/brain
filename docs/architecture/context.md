# Context assembly

Budget order: host policy, current turn, admitted evidence, recent dialogue. Evidence is truncated by whole record; never cut away its origin header. Reserve 2,048 tokens for output in research mode. The 32,768-token ceiling includes every delimiter.

The local replay path does not tokenize or infer. It matches complete normalized inputs. Token counts from this path must never be reported as decoder throughput.

When history exceeds budget, emit `context.evicted` with record IDs. Silent truncation makes recurrence analysis uninterpretable.
