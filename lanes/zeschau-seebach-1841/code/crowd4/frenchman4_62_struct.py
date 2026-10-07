#!/usr/bin/env python3
"""FRENCHMAN round 4 — structural leg for 62="on".

Instrument: segmenter's unsupervised STRUCT boundary confidences
(code/crowd3/segmenter_results.json :: /boundary_confidence_STRUCT, len 1845;
gap i = boundary between pair i and pair i+1).

Hypothesis (pre-registered before looking):
  - If 62="on" is a standalone pronoun in window W, STRUCT should put high
    boundary confidence on BOTH sides of the 62 pair.
  - Where the ear reads 62 word-internally ("ion" @1348, "personne" @508),
    at least one side should be LOW.
Calibration controls:
  - 46=que (GT standalone word): expect high/high.
  - 29=er (GT, word-final-ish per lane): expect low before / high after
    (i.e., NOT high/high) — shows the model discriminates.

Independence: STRUCT is unsupervised (no anchors, no ear, no bigrams used);
windows examined are the fresh ones (not the 8 ONNE bigrams, not ear-lock).
"""
import json, os, sys, statistics

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
sys.path.insert(0, os.path.join(LANE, "code"))
from crib_attack import load_pairs  # noqa: E402

pairs, _, _ = load_pairs()
seg = json.load(open(os.path.join(LANE, "code/crowd3/segmenter_results.json")))
bc = seg["boundary_confidence_STRUCT"]
assert len(bc) == 1845 == len(pairs) - 1

def sides(i):
    """(boundary-confidence before pair i, after pair i)."""
    before = bc[i - 1] if i > 0 else None
    after = bc[i] if i < len(pairs) - 1 else None
    return before, after

pos62 = [i for i, g in enumerate(pairs) if g == "62"]
assert len(pos62) == 34
# ear classification: word-internal per round-3 ear lock
INTERNAL = {508, 1348}  # "pers|on|ne", "...ion"
ONNE = {100, 508, 839, 1328, 1361, 1685, 1703, 1771}
EARLOCK = {100, 508, 839, 1328, 1361, 1685, 1703}  # F31 windows (1331 in notes = 1328 here)

rows = []
for i in pos62:
    b, a = sides(i)
    rows.append({"pos": i, "before": round(b, 4), "after": round(a, 4),
                 "internal_ear": i in INTERNAL, "fresh": i not in ONNE and i not in EARLOCK})

def prof(idxs):
    bs = [sides(i)[0] for i in idxs]
    aas = [sides(i)[1] for i in idxs]
    return {"n": len(idxs), "mean_before": round(statistics.mean(bs), 4),
            "mean_after": round(statistics.mean(aas), 4),
            "frac_before_gt05": round(sum(1 for x in bs if x > 0.5) / len(bs), 3),
            "frac_after_gt05": round(sum(1 for x in aas if x > 0.5) / len(aas), 3),
            "frac_both_gt05": round(sum(1 for i in idxs if sides(i)[0] > 0.5 and sides(i)[1] > 0.5) / len(idxs), 3)}

# controls
pos46 = [i for i, g in enumerate(pairs) if g == "46"]          # GT "que" standalone
pos29 = [i for i, g in enumerate(pairs) if g == "29"]          # GT "er" word-final-ish
import random
random.seed(7)
posRnd = random.sample(range(1, len(pairs) - 1), 68)            # random-pair baseline (2x n)

pronoun62 = [i for i in pos62 if i not in INTERNAL]

out = {
    "profile_62_pronoun_candidate": prof(pronoun62),
    "profile_62_internal_ear": prof([i for i in pos62 if i in INTERNAL]),
    "profile_62_fresh_only": prof([i for i in pronoun62 if i not in ONNE and i not in EARLOCK]),
    "control_46_que": prof(pos46),
    "control_29_er": prof(pos29),
    "control_random_pairs": prof(posRnd),
    "per_position": rows,
    "internal_detail": [r for r in rows if r["internal_ear"]],
}
p = os.path.join(LANE, "code/crowd4/frenchman4_62_struct.json")
json.dump(out, open(p, "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "per_position"}, indent=1))
print("wrote", p)
