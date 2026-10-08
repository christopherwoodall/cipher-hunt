#!/usr/bin/env python3
"""Byte-exact rebuilt repaired 1,847-pair stream (replaces canonical.py).
Uses code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt,
upstream tokenization: [s[i:i+2] for i in range(o, len(s)-1, 2)].
0-based pair positions per code/crowd4/REINDEX.md.
"""
import json, os, re, sys

LANE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/.."
DATA = os.path.join(LANE, "data")
KEYHUNT = os.path.join(LANE, "code/side-keyhunt")

def load_stream():
    rows = []
    for line in open(os.path.join(DATA, "upstream-ct_R5005.txt")):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        rows.append((lid, re.sub(r"\D", "", digits)))
    off = json.load(open(os.path.join(KEYHUNT, "repaired_offsets.json")))
    pairs = []
    for lid, digits in rows:
        o = off[lid]
        pairs += [(digits[i:i + 2], lid) for i in range(o, len(digits) - 1, 2)]
    return pairs

def main():
    pairs = load_stream()
    assert len(pairs) == 1847, len(pairs)
    seq = [g for g, _ in pairs]
    # Gloss check: crib "11 70 82 34 29 40" pair-aligned twice
    crib = [i for i in range(len(seq) - 6) if seq[i:i+6] == ["11","70","82","34","29","40"]]
    assert len(crib) == 2, crib
    print("stream ok: 1847 pairs, crib hits at", crib)

if __name__ == "__main__":
    main()
