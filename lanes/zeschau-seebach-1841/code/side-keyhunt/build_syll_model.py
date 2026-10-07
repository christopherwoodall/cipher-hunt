"""Build a French syllable-bigram reference model from the lane's era corpus.

Corpus: data/gutenberg-30513-tocqueville-t1.txt + gutenberg-30514-tocqueville-t2.txt
(Tocqueville, De la démocratie en Amérique, 1835–1840 — same register/era as
the 1841 French diplomatic text).

Syllabification is a simple vowel-nucleus / maximal-onset splitter. It is NOT
a linguistically exact segmenter; it exists only to give a consistent
syllable-bigram scoring surface for comparing candidate key tables against
each other and against known French. Calibrated below.

Output: syll_bigram.json {bigram_counts nested, syll_totals, vocab, meta}.
"""
import json
import math
import os
import re
from collections import Counter

_HERE = os.path.dirname(__file__)
_DATA = os.path.normpath(os.path.join(_HERE, "..", "..", "data"))

VOWELS = set("aàâäeéèêëiîïoôöuùûüy")

# French digraphs that form one onset — kept together when assigning onset.
DIGRAPHS = {"ch", "ph", "th", "gn", "qu", "gu", "ge", "gi", "cr", "br", "fr",
            "gr", "pr", "tr", "dr", "bl", "cl", "fl", "gl", "pl", "vr", "sc",
            "sp", "st", "sch"}


def syllabify(word):
    """Split a French word into rough syllables (maximal onset)."""
    w = re.sub(r"[^a-zàâäéèêëiîïoôöuùûüy]", "", word.lower())
    if not w:
        return []
    nuc = [i for i, c in enumerate(w) if c in VOWELS]
    if not nuc:
        return [w]
    syls, start = [], 0
    for k in range(len(nuc) - 1):
        i, j = nuc[k], nuc[k + 1]
        between = w[i + 1:j]
        if not between:
            # adjacent vowels: split between them
            end = i + 1
        elif len(between) == 1:
            # single consonant -> onset of next syllable
            end = i + 1
        else:
            # cluster: last consonant (or digraph) -> onset, rest -> coda
            onset_len = 2 if between[-2:] in DIGRAPHS else 1
            end = j - onset_len
        syls.append(w[start:end])
        start = end
    syls.append(w[start:])
    return syls


def main():
    text = ""
    for f in ("gutenberg-30513-tocqueville-t1.txt",
              "gutenberg-30514-tocqueville-t2.txt"):
        p = os.path.join(_DATA, f)
        text += open(p, encoding="utf-8", errors="replace").read() + "\n"

    stream = []
    for tok in re.findall(r"[A-Za-zÀÂÄÉÈÊËÎÏÔÖÙÛÜYàâäéèêëiîïoôöuùûüy'-]+", text):
        stream.extend(syllabify(tok))
    # drop degenerate empties
    stream = [s for s in stream if s]

    bigram = Counter()
    totals = Counter()
    for a, b in zip(stream, stream[1:]):
        bigram[(a, b)] += 1
        totals[a] += 1

    model = {
        "bigram": {f"{a}\t{b}": c for (a, b), c in bigram.items()},
        "totals": dict(totals),
        "n_syllables": len(stream),
        "n_distinct": len(totals),
        "meta": {
            "corpus": "gutenberg-30513-tocqueville-t1.txt + gutenberg-30514-tocqueville-t2.txt",
            "syllabifier": "vowel-nucleus maximal-onset (rough; see build_syll_model.py)",
            "k_smoothing": 0.5,
        },
    }
    out = os.path.join(_HERE, "syll_bigram.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(model, fh, ensure_ascii=False, separators=(",", ":"))
    print("syllables:", model["n_syllables"], "distinct:", model["n_distinct"])
    print("bigrams:", len(model["bigram"]), "->", out)

    # calibration: score a Tocqueville sample vs a scrambled one
    def score(syl_seq):
        k, V = 0.5, model["n_distinct"]
        s = 0.0
        for a, b in zip(syl_seq, syl_seq[1:]):
            c = bigram.get((a, b), 0)
            t = totals.get(a, 0)
            s += math.log((c + k) / (t + k * V))
        return s / max(1, len(syl_seq) - 1)

    import random
    cal = stream[:20000]
    print("french sample syll-bigram score:", round(score(cal), 4))
    scr = cal[:]
    random.Random(7).shuffle(scr)
    print("scrambled syll-bigram score:   ", round(score(scr), 4))


if __name__ == "__main__":
    main()
