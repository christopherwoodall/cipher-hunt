#!/usr/bin/env python3
"""Build repaired 1,847-pair stream from repaired_offsets.json (NOT canonical.py)."""
import json, os, re, sys

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CODE = os.path.join(LANE, "code")

def load_stream():
    rows = []
    for line in open(os.path.join(LANE, "data", "upstream-ct_R5005.txt")):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        rows.append((lid, re.sub(r"\D", "", digits)))
    off = json.load(open(os.path.join(CODE, "side-keyhunt", "repaired_offsets.json")))
    pairs = []
    for lid, digits in rows:
        o = off[lid]
        for i in range(o, len(digits) - 1, 2):
            pairs.append((digits[i:i+2], lid, i))
    seq = [g for g, _, _ in pairs]
    assert len(pairs) == 1847, len(pairs)
    return pairs

if __name__ == "__main__":
    pairs = load_stream()
    seq = [g for g, _, _ in pairs]
    hits = [i for i in range(len(seq)-1) if seq[i]=="62" and seq[i+1]=="48"]
    print("62->48 bigram positions (0-based):", hits)
