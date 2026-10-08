#!/usr/bin/env python3
"""ver-78 battery analysis. Repaired 1,847-pair stream only. No canonical.py. No R5005 writes."""
import json, os, re, math

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
DATA = os.path.join(LANE, "data")
SK = os.path.join(LANE, "code", "side-keyhunt")

def load_stream():
    rows = []
    for line in open(os.path.join(DATA, "upstream-ct_R5005.txt")):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        rows.append((lid, re.sub(r"\D", "", digits)))
    off = json.load(open(os.path.join(SK, "repaired_offsets.json")))
    pairs = []
    for lid, digits in rows:
        o = off[lid]
        pairs += [(digits[i:i + 2], lid) for i in range(o, len(digits) - 1, 2)]
    return pairs

pairs = load_stream()
seq = [g for g, _ in pairs]
print("N pairs:", len(pairs), "| distinct:", len(set(seq)))
assert len(pairs) == 1847, "stream must be the repaired 1847-pair parse"

def occ(g):
    return [i for i, x in enumerate(seq) if x == g]

n29, n78 = len(occ("29")), len(occ("78"))
print("n(29):", n29, " n(78):", n78)

DET = {"11", "77", "87", "47"}  # la / "le" prov / ce / "ce" allophone
def det_pred_rate(g):
    idx = occ(g)
    hits = [i for i in idx if i > 0 and seq[i - 1] in DET]
    return len(hits), len(idx), hits

h29, t29, i29 = det_pred_rate("29")
h78, t78, i78 = det_pred_rate("78")
print(f"det-predecessors 29: {h29}/{t29}  78: {h78}/{t78}")
or_val = (h29 / (t29 - h29)) / (h78 / (t78 - h78))
print(f"OR = {or_val:.2f}")

# after-33: which direction reproduces 0/31 vs 5/45?
def succ_is(g, s):
    idx = occ(g)
    return [i for i in idx if i < len(seq) - 1 and seq[i + 1] == s]
def pred_is(g, p):
    idx = occ(g)
    return [i for i in idx if i > 0 and seq[i - 1] == p]
print("succ==33: 29 ->", len(succ_is("29", "33")), "/", n29, " 78 ->", len(succ_is("78", "33")), "/", n78)
print("pred==33: 29 ->", len(pred_is("29", "33")), "/", n29, " 78 ->", len(pred_is("78", "33")), "/", n78)

# 'ce [78]' windows: 78 with predecessor 87 or 47
ce78 = [i for i in occ("78") if i > 0 and seq[i - 1] in ("87", "47")]
print("\n'ce [78]' count:", len(ce78))
for i in ce78:
    ctx = seq[max(0, i - 3):i + 4]
    offs = list(range(max(0, i - 3), min(len(seq), i + 4)))
    print(f"  78@{i} (ce@{i-1}={seq[i-1]}):", " ".join(f"{g}" for g in ctx), "| rows:", pairs[i - 1][1], "->", pairs[i][1])

# successors of ce-78 windows
print("\nsuccessors after 'ce 78':")
from collections import Counter
print(Counter(seq[i + 1] for i in ce78 if i + 1 < len(seq)))

# all 78 windows with succ 45 ('verdict' candidates)
v45 = [i for i in occ("78") if i + 1 < len(seq) and seq[i + 1] == "45"]
print("\n78->45 windows:", len(v45))
for i in v45:
    print(f"  78@{i}:", " ".join(seq[max(0, i - 3):i + 4]), "| ce-pred:", seq[i - 1] in ("87", "47"))

# @296 check
print("\n@294..300:", [(n, g) for n, (g, l) in enumerate(pairs) if 294 <= n <= 300])
print("rows:", [(n, l) for n, (g, l) in enumerate(pairs) if 294 <= n <= 300])

# la-78 windows (elision-compatible per red team: 'le/la 78' x9)
la78 = [i for i in occ("78") if i > 0 and seq[i - 1] in ("11", "77")]
print("\n'le/la 78' count:", len(la78), [i for i in la78])
