#!/usr/bin/env python3
"""Canonical 1,847-pair stream, recomputed from data/upstream-ct_R5005.txt +
code/side-keyhunt/repaired_offsets.json per code/side-keyhunt/repair_parse.py.
Never the stale canonical.py."""
import json, os, re

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")

def load_rows():
    rows = []
    with open(os.path.join(LANE, "data", "upstream-ct_R5005.txt")) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            lid, digits = line.split()
            rows.append((lid, re.sub(r"\D", "", digits)))
    return rows

def parse(rows, off):
    pairs = []
    for lid, digits in rows:
        o = off[lid]
        pairs += [(digits[i:i+2], lid) for i in range(o, len(digits)-1, 2)]
    return pairs

_off = None
_pairs = None
_seq = None
_rows = None

def stream():
    global _off, _pairs, _seq, _rows
    if _seq is None:
        _rows = load_rows()
        _off = json.load(open(os.path.join(LANE, "code/side-keyhunt/repaired_offsets.json")))
        _pairs = parse(_rows, _off)
        assert len(_pairs) == 1847, len(_pairs)
        _seq = [g for g, _ in _pairs]
    return _seq, _pairs

def windows(g, n_pre=2, n_post=3):
    """All indices where group g occurs; returns (i, left, right, rows)."""
    seq, pairs = stream()
    out = []
    for i, x in enumerate(seq):
        if x == g:
            left = seq[max(0,i-n_pre):i]
            right = seq[i+1:i+1+n_post]
            out.append((i, left, right, [l for _, l in pairs[max(0,i-n_pre):i+1+n_post]]))
    return out

def bigram(a, b):
    seq, pairs = stream()
    out = []
    for i in range(len(seq)-1):
        if seq[i] == a and seq[i+1] == b:
            out.append(i)
    return out

def successors(g):
    from collections import Counter
    seq, _ = stream()
    c = Counter()
    for i, x in enumerate(seq[:-1]):
        if x == g:
            c[seq[i+1]] += 1
    return c

def predecessors(g):
    from collections import Counter
    seq, _ = stream()
    c = Counter()
    for i, x in enumerate(seq):
        if i > 0 and x == g:
            c[seq[i-1]] += 1
    return c

def follow_set(g, k=3):
    """For each occurrence of g, record the k following groups."""
    seq, _ = stream()
    out = []
    for i, x in enumerate(seq):
        if x == g:
            out.append((i, tuple(seq[i+1:i+1+k])))
    return out

if __name__ == "__main__":
    seq, pairs = stream()
    print("pairs:", len(seq), "distinct:", len(set(seq)))
    print("crib:", [i for i in range(len(seq)-6) if seq[i:i+6]==["11","70","82","34","29","40"]])
    a805 = [(n,g) for n,(g,l) in enumerate(pairs) if l=="a8_05"]
    print("a8_05 last 3:", a805[-3:])
