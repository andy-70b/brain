# Boundary review / December

Scope: checked-in Python substrate and offline fixtures. External adapters, parameter services, and observer deployments are outside this review.

Verified contracts: quarantined evidence is excluded before ranking; duplicate evidence IDs cannot overwrite; host closure rejects further turns; unknown replay inputs cannot trigger generation; repeated n-grams count distinct records.

Remaining requirements: external adapter isolation, artifact signature verification, and observer delivery ordering must be verified in their own environment. The substrate does not certify those systems.
