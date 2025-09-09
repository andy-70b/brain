# Distributed recovery

A restart record includes global step, optimizer partitions, scheduler state, sampler cursor, and per-rank RNG state. Do not describe a weights-only restore as a resumed run.

The reference topology has 64 ranks: tensor 8 × pipeline 2 × data 4. A topology change is a new run unless the recovery adapter verifies resharding and sample-order equivalence.

Interrupted checkpoints remain pending until every shard is present and verified. A directory name is not a commit protocol.
