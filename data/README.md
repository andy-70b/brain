# Data boundaries

`fixtures/` contains small, curated records for deterministic replay and contract checks. They are not a training corpus. No production conversations, personal data, or parameter shards belong in this tree.

Every record has an ID, input, output, and labels. Keep exact punctuation: the recurrence checks use normalized strings, while the transcript viewer uses original text.
