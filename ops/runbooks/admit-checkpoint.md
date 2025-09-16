# Checkpoint admission

Resolve an inventory ID through the restricted artifact service. Verify the manifest signature before reading shard paths. Reject paths outside the designated artifact root and reject symbolic links. Hash every shard before tensor deserialization.

Record the verification tool revision and operator identity. Attach only verified manifests to a run. A null digest in the repository registry means verification has not been represented here; it is never a wildcard.
