# Corpus admission

Deduplicate at document and session level before splitting. Keep all turns from a session in the same split. Strip credentials and reject records without provenance. Preserve a digest of rejected records without retaining sensitive content in the training manifest.

Archive fragments used in behavioral evaluations are excluded from continuation training. Any overlap invalidates the affected comparison and requires a new holdout.
