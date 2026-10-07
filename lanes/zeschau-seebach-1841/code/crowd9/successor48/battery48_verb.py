#!/usr/bin/env python3
"""48=verb/verb-stem battery (round-9, 48-successor).

Pre-registered in PRE-REGISTER.md BEFORE any 48-window stream access.
Repaired 1,847-pair parse via code/crowd7/keystruct/aliasing.load_stream().
Era: Nesselrode v8, tokenized with code/crowd7/closer/diplomatic_rates.tokenize.
All @-citations are 0-based pair indices.
"""
import json, math, os, sys
from collections import Counter
from pathlib import Path

LANE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(LANE / "code" / "crowd7" / "keystruct"))
sys.path.insert(0, str(LANE / "code" / "crowd7" / "closer"))
from aliasing import load_stream
from diplomatic_rates import tokenize

OUT = Path(__file__).parent
res = {"prereg": "PRE-REGISTER.md (written before stream access)"}

# ---------------- stream ----------------
pairs = load_stream()
N = len(pairs)
assert N == 1847, N
res["N"] = N

def windows(g):
    return [i for i, x in enumerate(pairs) if x == g]

w48 = windows(48)
n48 = len(w48)
res["n48"] = n48
res["p48_rate"] = n48 / N
assert n48 == 38, f"n48 drift: {n48}"  # adjudicator re-derived 38

pre = Counter(pairs[i - 1] for i in w48 if i > 0)
suc = Counter(pairs[i + 1] for i in w48 if i < N - 1)
res["census"] = [{"i": i,
                  "pre": pairs[i - 1] if i > 0 else None,
                  "suc": pairs[i + 1] if i < N - 1 else None} for i in w48]
res["predecessors"] = dict(sorted(pre.items(), key=lambda kv: -kv[1]))
res["successors"] = dict(sorted(suc.items(), key=lambda kv: -kv[1]))

n96 = len(windows(96))
res["n96"] = n96
res["w96"] = windows(96)

# ---------------- V1: verb-form rate band ----------------
corp = (LANE / "code" / "side-period" / "corpus" / "nesselrode-v8.txt").read_text()
toks = tokenize(corp)
nt = len(toks)
uni = Counter(toks)

# Frozen classification of top-40 tokens: verb / nonverb / ambiguous.
# (standard French lexicon; auditable — full table dumped below)
CLASS = {
    # unambiguous verb forms
    "est": "verb", "sont": "verb", "était": "verb", "étaient": "verb",
    "a": "verb", "ont": "verb", "avait": "verb", "avaient": "verb",
    "sera": "verb", "serait": "verb", "soit": "verb", "été": "verb",
    "eu": "verb", "eut": "verb",
    "fait": "verb", "font": "verb", "fasse": "verb", "ferait": "verb",
    "dit": "verb", "disent": "verb",
    "peut": "verb", "peuvent": "verb", "pouvait": "verb", "puisse": "verb",
    "doit": "verb", "doivent": "verb", "devait": "verb",
    "veut": "verb", "veulent": "verb", "voulait": "verb",
    "faut": "verb", "fallait": "verb",
    "semble": "verb", "semblent": "verb", "paraît": "verb", "parait": "verb",
    "croit": "verb", "croient": "verb", "voit": "verb", "voient": "verb",
    "sait": "verb", "savent": "verb", "prend": "verb", "prendrait": "verb",
    "met": "verb", "donne": "verb", "donnent": "verb", "tient": "verb",
    "vient": "verb", "devient": "verb", "reste": "verb", "passe": "verb",
    "suffit": "verb",
}
top40 = uni.most_common(40)
table = []
for tok, c in top40:
    cls = CLASS.get(tok, "nonverb" if tok not in
                    ("passe", "porte", "tout", "plus", "moins") else "ambiguous")
    # "passe"/"porte" verb-or-noun -> ambiguous; "tout/plus/moins" nonverb
    if tok in ("passe", "porte"):
        cls = "ambiguous"
    table.append({"tok": tok, "n": c, "rate": c / nt, "class": cls})
verb_rates = sorted([t["rate"] for t in table if t["class"] == "verb"], reverse=True)[:20]
res["V1"] = {"n_tokens": nt, "top40": table,
             "top20_verb_rates": verb_rates,
             "min20": min(verb_rates), "max20": max(verb_rates),
             "p48": n48 / N,
             "ratio_vs_max": (n48 / N) / max(verb_rates)}
r = res["V1"]["ratio_vs_max"]
res["V1"]["verdict"] = ("ADVERSE-kill-grade" if r > 3 else
                        "PASS" if (n48 / N) >= 0.5 * min(verb_rates)
                        and (n48 / N) <= 2 * max(verb_rates) else "NULL")

# ---------------- V2: "48 pas" ne-licensing ----------------
w_48_52 = [i for i in w48 if i < N - 1 and pairs[i + 1] == 52]
res["w_48_pas"] = w_48_52
GT_WORDBREAK = {11, 93, 8}  # la / l' — frozen per prereg
v2 = []
for i in w_48_52:
    span = list(range(max(0, i - 4), i))
    ne_pos = [j for j in span if pairs[j] == 94]
    licensed = False
    for j in ne_pos:
        if not any(pairs[k] in GT_WORDBREAK for k in range(j + 1, i)):
            licensed = True
    v2.append({"i": i, "span": [(j, pairs[j]) for j in span],
               "ne_pos": ne_pos, "licensed": licensed})
res["V2"] = {"windows": v2,
             "verdict": "PASS" if sum(w["licensed"] for w in v2) >= 1 else "ADVERSE"}

# ---------------- V3: predecessor verb-licensing ----------------
LICENSING = {62, 94, 64, 46, 24, 82}  # on, ne, qui, que, en, m  (frozen)
HARD_INCOMP = {11}                     # la (GT article)
n_lic = sum(c for g, c in pre.items() if g in LICENSING)
n_hard = sum(c for g, c in pre.items() if g in HARD_INCOMP)
n_uncl = n48 - n_lic - n_hard
res["V3"] = {"n_licensing": n_lic, "n_hard_incompat": n_hard,
             "n_unclassified": n_uncl,
             "licensing_detail": {str(g): pre[g] for g in LICENSING if g in pre},
             "hard_detail": {str(g): pre[g] for g in HARD_INCOMP if g in pre},
             "unclassified": {str(g): c for g, c in
                              sorted(pre.items(), key=lambda kv: -kv[1])
                              if g not in LICENSING and g not in HARD_INCOMP}}
if n_lic >= 23:
    res["V3"]["verdict"] = "PASS"
elif n_hard >= 3:
    res["V3"]["verdict"] = "ADVERSE"
else:
    res["V3"]["verdict"] = "NULL"

# ---------------- V4: "on 48" successor compatibility ----------------
w_62_48 = [i for i in w48 if i > 0 and pairs[i - 1] == 62]
res["w_on_48"] = w_62_48
HARD_SUC = {62, 64, 94}  # on / qui / ne cannot follow a finite verb
v4 = [{"i": i, "suc": pairs[i + 1] if i < N - 1 else None,
       "hard_incompat": (pairs[i + 1] in HARD_SUC) if i < N - 1 else None}
      for i in w_62_48]
n_hards = sum(1 for w in v4 if w["hard_incompat"])
res["V4"] = {"windows": v4, "n_hard": n_hards,
             "verdict": "PASS-weak" if n_hards == 0 else
                        "ADVERSE" if n_hards >= 2 else "NULL"}

# ---------------- V5: 96 same-stem-family (H_stem, exploratory) ----------------
def cosine(a, b):
    keys = set(a) | set(b)
    num = sum(a[k] * b[k] for k in keys)
    da = math.sqrt(sum(v * v for v in a.values()))
    db = math.sqrt(sum(v * v for v in b.values()))
    return num / (da * db) if da and db else 0.0

w96 = windows(96)
pre96 = Counter(pairs[i - 1] for i in w96 if i > 0)
suc96 = Counter(pairs[i + 1] for i in w96 if i < N - 1)
cos_pre = cosine(pre, pre96)
floors = []
for g in set(pairs):
    if g == 48 or len(windows(g)) < 20:
        continue
    pg = Counter(pairs[i - 1] for i in windows(g) if i > 0)
    floors.append(cosine(pre, pg))
floor = sorted(floors)[len(floors) // 2]

def fisher2(a, b, c, d):
    # two-sided Fisher exact via hypergeometric enumeration
    n = a + b + c + d
    def hg(x):
        return (math.comb(a + b, x) * math.comb(c + d, a + c - x)) / math.comb(n, a + c)
    p_obs = hg(a)
    p = 0.0
    for x in range(max(0, a + c - (c + d)), min(a + b, a + c) + 1):
        px = hg(x)
        if px <= p_obs + 1e-12:
            p += px
    return p

F48 = set(k for k, _ in suc.most_common(8))
F96 = set(k for k, _ in suc96.most_common(8))
U = set(suc) | set(suc96)
a = len(F48 & F96)
p_fish = fisher2(a, len(F48) - a, len(F96) - a, len(U) - len(F48) - len(F96) + a)
top3_share = sum(c for _, c in suc.most_common(3)) / n48
res["V5"] = {"cos_pre_48_96": cos_pre, "floor_median": floor,
             "cos_bar": 0.60,
             "cos_pass": cos_pre >= 0.60,
             "shared_top8_followers": sorted(F48 & F96),
             "fisher_overlap_p": p_fish,
             "fisher_pass": p_fish < 0.05 and a >= 2,
             "stem_signature_top3_share": top3_share,
             "stem_signature_pass": top3_share >= 0.40,
             "verdict": "PASS" if (cos_pre >= 0.60 and p_fish < 0.05 and a >= 2)
                        else "NULL-underpowered"}

# ---------------- V6: follower concentration diagnostic (NOT scored) ----------------
hhi = sum((c / n48) ** 2 for c in suc.values())
res["V6_diagnostic"] = {"n_distinct_followers": len(suc),
                        "top5_share": sum(c for _, c in suc.most_common(5)) / n48,
                        "hhi": hhi}

# ---------------- K3/K4 flags ----------------
k4_windows = [i for i in w48
              if (i > 0 and pairs[i - 1] == 11) or (i < N - 1 and pairs[i + 1] == 11)]
res["K4_gt_la_windows"] = k4_windows
res["K4_fires"] = len(k4_windows) >= 3
# K1 from V1; K2 from V2+V3
res["K1_fires"] = res["V1"]["verdict"] == "ADVERSE-kill-grade"
res["K2_fires"] = (res["V2"]["verdict"] == "ADVERSE"
                   and (n_lic / n48) < 0.40)

json.dump(res, open(OUT / "battery48_verb_results.json", "w"), indent=1,
          default=str)
print(json.dumps({
    "n48": n48, "n96": n96,
    "V1": res["V1"]["verdict"], "V1_ratio_vs_max": round(r, 3),
    "V1_max20": round(max(verb_rates), 5), "V1_min20": round(min(verb_rates), 5),
    "V2": res["V2"]["verdict"],
    "V3": res["V3"]["verdict"], "V3_lic": n_lic, "V3_hard": n_hard,
    "V4": res["V4"]["verdict"], "V4_n_hard": n_hards,
    "V5": res["V5"]["verdict"], "V5_cos": round(cos_pre, 4),
    "V5_floor": round(floor, 4), "V5_fisher_p": round(p_fish, 4),
    "V5_stem_sig": round(top3_share, 3),
    "V6_top5": round(res["V6_diagnostic"]["top5_share"], 3),
    "K1": res["K1_fires"], "K2": res["K2_fires"],
    "K4": res["K4_fires"], "K4_windows": k4_windows,
}, indent=1))
