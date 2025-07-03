# Retrieval baseline

The checked-in retriever ranks admitted records by distinct lexical overlap. Ties resolve by stable evidence ID. Empty queries return no evidence. This baseline is intentionally inspectable and is not an embedding service.

Quarantined records are filtered before scoring. Filtering after ranking would allow their presence to alter the selected set even when their content never reaches the decoder.

Research adapters must report candidate IDs, admitted IDs, and the final context order. Recall without provenance is a failed retrieval, even when the answer is correct.
