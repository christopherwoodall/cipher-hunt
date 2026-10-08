#!/usr/bin/env python3
"""Repaired R5005 pair stream loader for the round-13 islet audit.

Builds the canonical 1,847-pair parse from data/upstream-ct_R5005.txt +
code/side-keyhunt/repaired_offsets.json (a5_03 flip, see
code/crowd4/REINDEX.md). Self-validates landmarks; never hand-roll a parse.
"""
import json, os, re

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')

def load_pairs():
    offsets = json.load(open(os.path.join(LANE, 'code', 'side-keyhunt',
                                          'repaired_offsets.json')))
    pairs = []
    for line in open(os.path.join(LANE, 'data', 'upstream-ct_R5005.txt')):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        digits = re.sub(r'\D', '', digits)
        d = digits[offsets.get(lid, 0):]
        for i in range(0, len(d) - 1, 2):
            pairs.append(d[i:i + 2])
    assert len(pairs) == 1847, f'pair count {len(pairs)}'
    assert len(set(pairs)) == 96, f'distinct {len(set(pairs))}'
    crib = ['11', '70', '82', '34', '29', '40']
    hits = [i for i in range(len(pairs) - 5) if pairs[i:i + 6] == crib]
    assert hits == [754, 1034], f'crib hits {hits}'
    return pairs

def windows(pairs, g):
    """All 0-based positions i with pairs[i]==g; returns (i, pre, suc)."""
    out = []
    for i, p in enumerate(pairs):
        if p == g:
            pre = pairs[i - 1] if i > 0 else None
            suc = pairs[i + 1] if i < len(pairs) - 1 else None
            out.append((i, pre, suc))
    return out

def ctx(pairs, i, k=3):
    lo, hi = max(0, i - k), min(len(pairs), i + k + 1)
    return pairs[lo:hi]
