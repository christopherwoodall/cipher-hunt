#!/usr/bin/env python3
"""Skeleton Keeper pass 1: verify transcription, build skeleton.json, compute coverage.

Reads: ../../data/upstream-ct_R5005.digits.txt
Writes: code/sidepath/skeleton.json
        code/sidepath/report_inbox/skeleton-keeper-pass1.md
"""
import hashlib, json, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
DIG = os.path.join(LANE, "data/upstream-ct_R5005.digits.txt")       # byte-level transcription source
TXT = os.path.join(LANE, "data/upstream-ct_R5005.txt")              # line-grouped source (line IDs)
OFF = os.path.join(LANE, "data/upstream-offsets.json")              # per-line offsets from upstream
OUT = os.path.join(LANE, "code/sidepath/skeleton.json")
INBOX = os.path.join(LANE, "code/sidepath/report_inbox/skeleton-keeper-pass1.md")

# --- 1. verify transcription byte-for-byte ---
import re
raw = open(DIG).read()
sha = hashlib.sha256(raw.encode()).hexdigest()
digits = "".join(raw.split())
n_digits = len(digits)
assert all(c.isdigit() for c in digits), "non-digit character in transcription"
assert n_digits == 3764, f"digit count {n_digits} != 3764"

# --- 2. lane-canonical parse: upstream-ct_R5005.txt + per-line offsets ---
# Naive concatenation would give 3764/2 = 1882 pairs; the lane-standard parse
# (identical to code/crib_attack.py::load_pairs) applies upstream offsets and
# drops one leading digit on offset-1 lines + one trailing digit on odd lines,
# yielding 1846 pairs / 96 groups. All lane numbers use THIS alignment.
offsets = json.load(open(OFF))
pairs, odd_lines, off1_lines = [], 0, 0
for line in open(TXT):
    line = line.strip()
    if not line:
        continue
    lid, d = line.split()
    d = re.sub(r"\D", "", d)
    if len(d) % 2 == 1:
        odd_lines += 1
    off = offsets.get(lid, 0)
    if off == 1:
        off1_lines += 1
    d = d[off:]
    for i in range(0, len(d) - 1, 2):
        pairs.append(d[i:i + 2])
n_pairs = len(pairs)
groups = set(pairs)
assert n_pairs == 1846, f"canonical pair count {n_pairs} != 1846"
assert len(groups) == 96, f"distinct groups {len(groups)} != 96"
assert odd_lines == 28 and off1_lines == 32  # lane-standing parse constants

# --- 2. value inventory (status, value). Do NOT apply: 77=pas, 77=que,
#     06=ent general, 06=/ma~/ — none of these appear below. ---
INVENTORY = {
    # group: (value, status)
    # GROUND TRUTH — pencil cribs (7)
    "11": ("la",  "ground-truth"),
    "70": ("pre", "ground-truth"),
    "82": ("m",   "ground-truth"),
    "34": ("i",   "ground-truth"),
    "29": ("er",  "ground-truth"),
    "40": ("e",   "ground-truth"),
    "46": ("que", "ground-truth"),
    # PROVISIONAL — usable, flagged (6)
    "87": ("ce",  "provisional-strengthened"),
    "64": ("qui", "provisional"),          # re-promotion BLOCKED per F31
    "96": ("par", "provisional"),
    "94": ("ne",  "provisional-strong"),
    "06": ("verb-stem-class", "provisional"),  # class value, NOT 06=ent, NOT 06=/ma~/
    "67": ("veut", "provisional"),
    # LEADS — usable, flagged LEAD (4)
    "62": ("on",  "lead"),
    "78": ("me",  "lead"),
    "52": ("pas", "lead"),
    "24": ("en",  "lead"),
}

assert set(INVENTORY) <= groups, "inventory group missing from transcription"
# sanity: none of the banned readings sneak in
BANNED = {"77": ["pas", "que"], "06": ["ent", "/ma~/", "mɑ̃"]}
for g, vals in BANNED.items():
    if g in INVENTORY:
        assert INVENTORY[g][0] not in vals, f"banned reading applied for {g}"

# --- 3. build per-position skeleton ---
positions = []
status_counts = {}
for pos, grp in enumerate(pairs):
    entry = {"pos": pos, "group": grp, "value": None, "status": None}
    if grp in INVENTORY:
        val, st = INVENTORY[grp]
        entry["value"] = val
        entry["status"] = st
        status_counts[st] = status_counts.get(st, 0) + 1
    positions.append(entry)

n_covered = sum(1 for e in positions if e["value"] is not None)
total = len(positions)
coverage = {
    "total_positions": total,
    "covered_positions": n_covered,
    "coverage_pct": round(100.0 * n_covered / total, 2),
    "by_status": {
        st: {"positions": c, "pct": round(100.0 * c / total, 2)}
        for st, c in sorted(status_counts.items())
    },
}

skeleton = {
    "pass": 1,
    "transcription_sha256": sha,
    "transcription_source": "data/upstream-ct_R5005.digits.txt",
    "transcription_checks": {
        "digits": n_digits,
        "pairs": n_pairs,
        "distinct_groups": len(groups),
        "byte_verified": True,
        "parse_method": "lane-canonical: upstream-ct_R5005.txt + upstream-offsets.json "
                        "(identical to code/crib_attack.py::load_pairs; "
                        "28 odd-digit lines, 32 offset-1 lines)",
    },
    "inventory": {g: {"value": v, "status": s} for g, (v, s) in sorted(INVENTORY.items())},
    "not_applied": ["77=pas (disfavored-strong)", "77=que (disfavored)",
                    "06=ent general (refuted)", "06=/mɑ̃/ (killed)"],
    "positions": positions,
    "coverage": coverage,
}
with open(OUT, "w") as f:
    json.dump(skeleton, f)

print("PASS 1 skeleton written:", OUT)
print("sha256:", sha)
print(f"digits={n_digits} pairs={n_pairs} groups={len(groups)}")
print(f"coverage: {n_covered}/{total} = {coverage['coverage_pct']}%")
for st, d in coverage["by_status"].items():
    print(f"  {st}: {d['positions']} ({d['pct']}%)")

# group hit counts for the report
from collections import Counter
hit = Counter(e["group"] for e in positions if e["value"])
print("group hit counts:", dict(sorted(hit.items())))
