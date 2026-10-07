#!/usr/bin/env python3
"""Repaired canonical parse for R5005 (red-team finding R1, 2026-10-07).

Upstream's EM chose offsets['a5_03'] = 1. That choice makes the pair phase at
raw digit 1532 ODD, which contradicts manuscript gloss (i): the erased pencil
"la pre m i er e" sits over groups "11 70 82 34 29 40" on row a5_03, and the
raw digit substring "117082342940" starts at raw offset 1532 (even) on that row.
Pair-phase at 1532 must therefore be EVEN.

Flipping a5_03 1 -> 0 satisfies gloss (i) AND keeps gloss (ii) ("que" over "46"
at end of row a8_05, raw 3453) satisfied: the flip removes 2 dropped
digits inside row a5_03 (even count), so every row after a5_03 keeps its exact
pairing; only row a5_03's internal pairing changes and the total pair count
goes 1846 -> 1847.

Gloss (ii) check: raw 3453 must start a pair ("46"). Verified below.

Usage: python3 repair_parse.py   # writes repaired_offsets.json, runs all asserts
"""
import json, os, re

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/.."
DATA = os.path.join(LANE, "data")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "repaired_offsets.json")

CRIB = ["11", "70", "82", "34", "29", "40"]          # "la premiere"
CRIB_DIGITS = "117082342940"

def load_rows():
    rows = []
    for line in open(os.path.join(DATA, "upstream-ct_R5005.txt")):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        rows.append((lid, re.sub(r"\D", "", digits)))
    return rows

def parse(rows, off):
    """Upstream tokenization, byte-exact: [s[i:i+2] for i in range(o, len(s)-1, 2)]."""
    pairs = []
    for lid, digits in rows:
        o = off[lid]
        pairs += [(digits[i:i + 2], lid) for i in range(o, len(digits) - 1, 2)]
    return pairs

def main():
    rows = load_rows()
    base = json.load(open(os.path.join(DATA, "upstream-offsets.json")))
    assert base["a5_03"] == 1, "upstream EM choice changed; re-audit needed"

    rep = dict(base)
    rep["a5_03"] = 0

    pairs = parse(rows, rep)
    seq = [g for g, _ in pairs]
    assert len(pairs) == 1847, len(pairs)
    assert len(set(seq)) == 96, len(set(seq))

    # Gloss (i): crib digit substring occurs twice raw; both must be pair-aligned.
    stream = "".join(d for _, d in rows)
    raw_hits = [i for i in range(len(stream) - 12) if stream[i:i + 12] == CRIB_DIGITS]
    assert raw_hits == [1532, 2108], raw_hits
    crib_hits = [i for i in range(len(seq) - 6) if seq[i:i + 6] == CRIB]
    assert len(crib_hits) == 2, crib_hits          # "la premiere" twice, no phantom
    assert pairs[crib_hits[0]][1] == "a5_03", pairs[crib_hits[0]]   # gloss line
    assert pairs[crib_hits[1]][1] == "a6_03", pairs[crib_hits[1]]

    # Gloss (ii): row a8_05 ends with pair "46" ("que").
    a805 = [(n, g) for n, (g, l) in enumerate(pairs) if l == "a8_05"]
    assert a805[-1][1] == "46", a805[-3:]

    # Only row a5_03's pairing changes: the flip removes 2 dropped digits inside
    # row a5_03 (even), so every later row keeps its exact pair sequence, shifted
    # by exactly one pair index. Verify sequence-level, not position-level.
    old_pairs = parse(rows, base)
    b_old = next(n for n, (g, l) in enumerate(old_pairs) if l == "a5_04")
    b_new = next(n for n, (g, l) in enumerate(pairs) if l == "a5_04")
    assert [g for g, _ in old_pairs[:b_old - 25]] == [g for g, _ in pairs[:b_new - 26]]
    assert [g for g, _ in old_pairs[b_old:]] == [g for g, _ in pairs[b_new:]]
    assert len(pairs) == len(old_pairs) + 1

    with open(OUT, "w") as f:
        json.dump(rep, f, indent=1, sort_keys=True)
    print("OK: repaired parse =", len(pairs), "pairs; crib at", crib_hits,
          "; a8_05 ends", a805[-1][1], "->", OUT)

if __name__ == "__main__":
    main()
