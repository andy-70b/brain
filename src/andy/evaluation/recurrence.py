from collections import Counter
import re

def repeated_ngrams(texts, width=4):
    if width < 1:
        raise ValueError("width must be positive")
    counts = Counter()
    for text in texts:
        tokens = re.findall(r"[a-z0-9]+", text.lower())
        counts.update(set(tuple(tokens[i:i + width]) for i in range(len(tokens) - width + 1)))
    return {" ".join(k): v for k, v in sorted(counts.items()) if v > 1}
