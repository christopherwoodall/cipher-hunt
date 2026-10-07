#!/usr/bin/env python3
"""48 syllable-cell battery (round-10, syllabicist48).

Pre-registered in PREREG.md (v1.1) BEFORE any run. Repaired 1,847-pair parse
via code/crowd7/keystruct/aliasing.load_stream(). Era: Nesselrode v8
(code/side-period/corpus/nesselrode-v8.txt), tokenized with
code/crowd7/closer/diplomatic_rates.tokenize. All @-citations 0-based.

By-ear syllabifier (documented, fixed): for each token, find vowel indices
(vowels = aàâäeéèêëiîïoôöuùûüy); for consecutive vowels v_i, v_{i+1} with
c consonants between: c==0 -> break between vowels; c>=1 -> break after the
first consonant following v_i (maximal-coda-ish by-ear cut: "parler" ->
par|ler; "personne" -> per|son|ne). Leading consonants join the first
syllable; trailing consonants stay in the last. Mute -e kept written
(F44-R3). Final -er NOT pre-split (recorded approximation; F22 flagged).
Tokens with no vowel stay whole (e.g. "l'").
"""
import json, math, sys
from collections import Counter
from pathlib import Path
from itertools import combinations

LANE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(LANE / "code" / "crowd7" / "keystruct"))
sys.path.insert(0, str(LANE / "code" / "crowd7" / "closer"))
from aliasing import load_stream
from diplomatic_rates import tokenize

OUT = Path(__file__).parent
res = {"prereg": "PREREG.md v1.1 (2026-10-07T20:38:55Z, amended +2m pre-run)"}

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
res["P48"] = n48 / N
assert n48 == 38, f"n48 drift: {n48}"

pre48 = Counter(pairs[i - 1] for i in w48 if i > 0)
suc48 = Counter(pairs[i + 1] for i in w48 if i < N - 1)

W96 = windows(96)
n96 = len(W96)
res["n96"] = n96
pre96 = Counter(pairs[i - 1] for i in W96 if i > 0)
suc96 = Counter(pairs[i + 1] for i in W96 if i < N - 1)

# ---------------- corpus ----------------
corp = (LANE / "code" / "side-period" / "corpus" / "nesselrode-v8.txt").read_text(encoding="utf-8", errors="replace")
toks = tokenize(corp)
nt = len(toks)
uni = Counter(toks)
bi = Counter(zip(toks[:-1], toks[1:]))
res["corpus"] = {"file": "nesselrode-v8.txt", "n_tokens": nt}

def n_bi(a, b):
    return bi.get((a, b), 0)

VOWELS = set("aàâäeéèêëiîïoôöuùûüy")

def byear_syllables(word):
    """Fixed by-ear syllabification (see module docstring)."""
    w = word
    if "'" in w and len(w) <= 3:  # elision particles like l', d', qu' stay whole
        return [w]
    vs = [i for i, ch in enumerate(w) if ch in VOWELS]
    if not vs:
        return [w]
    # v1.2: consecutive vowels = single nucleus (no VV split). Merge runs.
    nuclei = []
    for i in vs:
        if nuclei and i == nuclei[-1][-1] + 1:
            nuclei[-1].append(i)
        else:
            nuclei.append([i])
    nuc = [(n_[0], n_[-1]) for n_ in nuclei]
    cuts = []
    for (a0, a1), (b0, b1) in zip(nuc[:-1], nuc[1:]):
        c = b0 - a1 - 1
        # break after the first consonant following the nucleus end
        cuts.append(a1 + 2 if c >= 1 else a1 + 1)
    parts, start = [], 0
    for cut in cuts:
        parts.append(w[start:cut])
        start = cut
    parts.append(w[start:])
    return [p for p in parts if p]

syl_uni = Counter()
for t in toks:
    for s in byear_syllables(t):
        syl_uni[s] += 1
nsyl = sum(syl_uni.values())
res["corpus"]["n_syllables"] = nsyl

# ---------------- candidate selection (pre-registered rule) ----------------
EXCLUDE = {"la", "pre", "m", "i", "er", "e", "que",      # GT
           "ce", "qui", "par", "ne", "est",               # provisional
           "on", "le", "me", "pour", "en", "pas", "ent",  # banked
           "l'", "même"}                                  # banked
P48 = n48 / N

ranked_syl = [(s, c / nsyl) for s, c in syl_uni.most_common(40)]
cand_syl = [(s, r) for s, r in ranked_syl if s not in EXCLUDE]
cand_syl.sort(key=lambda kv: abs(math.log((kv[1]) / P48)))
SYL_SHORT = cand_syl[:10]
res["selection"] = {
    "rule": "top-40 by-ear syllables minus exclusions, top-10 by |log(rate/P48)|",
    "syllable_candidates": [{"s": s, "era_rate": r} for s, r in SYL_SHORT],
}

ranked_word = [(w_, c / nt) for w_, c in uni.most_common(60)]
cand_word = [(w_, r) for w_, r in ranked_word if w_ not in EXCLUDE and len(w_) > 1]
cand_word.sort(key=lambda kv: abs(math.log(kv[1] / P48)))
WORD_TOP3 = cand_word[:3]
SEEDS = ["de", "à", "se", "les", "des", "plus", "tout", "bien", "sur", "sans",
         "dans", "encore", "aussi", "leur", "son", "mais", "car", "donc", "ni",
         "y", "point",
         "lettre", "dépêche", "gouvernement", "majesté", "affaire", "cour",
         "ministre"]
word_cands = []
seen = set()
for w_, r in WORD_TOP3 + [(s_, uni.get(s_, 0) / nt) for s_ in SEEDS]:
    if w_ in seen or w_ in EXCLUDE:
        continue
    seen.add(w_)
    word_cands.append((w_, r, "top3" if (w_, r) in [(x[0], x[1]) for x in WORD_TOP3] else "seeded"))
res["selection"]["word_candidates"] = [
    {"s": w_, "era_rate": r, "src": src} for w_, r, src in word_cands]

# ---------------- legs ----------------
def rate_leg(s, era_rate):
    r = P48 / era_rate if era_rate > 0 else float("inf")
    if 1 / 3 <= r <= 3:
        return "PASS", r
    if r > 5 or r < 0.1:
        return "KILL", r
    return "NULL", r

# windows for frame legs
ON48 = [i for i in w48 if pairs[i - 1] == 62]          # "on 48" x6
LA48 = [i for i in w48 if pairs[i - 1] == 11]          # "la 48" @1525
PAS48 = [i for i in w48 if pairs[i + 1] == 52]         # "48 pas" x2
assert len(ON48) == 6 and len(LA48) == 1 and len(PAS48) == 2, (len(ON48), len(LA48), len(PAS48))
res["frames"] = {"on48": ON48, "la48": LA48, "pas48": PAS48}

def word_legs(s, era_rate):
    legs = {}
    v, r = rate_leg(s, era_rate)
    legs["S1_rate"] = {"verdict": v, "ratio": r, "era_rate": era_rate}
    # S2: "la S"
    n_la = n_bi("la", s)
    legs["S2_la_frame"] = {"verdict": "PASS" if n_la >= 1 else "KILL",
                           "n_la_S": n_la}
    # S3: "on S" x6 + "que S"
    n_on = n_bi("on", s)
    n_que = n_bi("que", s)
    s3_kill = (n_on == 0) or (n_que == 0)
    legs["S3_on_frames"] = {"verdict": "KILL" if s3_kill else "PASS",
                            "n_on_S": n_on, "n_que_S": n_que}
    # S4: "S pas" x2
    n_spas = n_bi(s, "pas")
    legs["S4_pas_frames"] = {"verdict": "PASS" if n_spas >= 1 else "KILL",
                             "n_S_pas": n_spas}
    return legs

def syl_legs(s, era_rate):
    legs = {}
    v, r = rate_leg(s, era_rate)
    legs["S1_rate"] = {"verdict": v, "ratio": r, "era_rate": era_rate}
    # S2: neutral for syllables; record corroboration (era words starting with s after "la")
    la_next = Counter(toks[k + 1] for k in range(nt - 1) if toks[k] == "la")
    n_la_sinit = sum(c for w_, c in la_next.items() if byear_syllables(w_)[:1] == [s])
    legs["S2_la_frame"] = {"verdict": "NEUTRAL",
                           "n_la_word_starting_with_S": n_la_sinit}
    # S3: "on S"-initial words; successor-continuation at @1350 (suc 77="le")
    on_next = Counter(toks[k + 1] for k in range(nt - 1) if toks[k] == "on")
    n_on_sinit = sum(c for w_, c in on_next.items() if byear_syllables(w_)[:1] == [s])
    # @1350: word ending in S followed by "le"
    end_s_le = sum(bi.get((w_, "le"), 0) for w_ in uni
                   if byear_syllables(w_)[-1:] == [s] and w_ != s)
    legs["S3_on_frames"] = {"verdict": "NEUTRAL",
                            "n_on_word_starting_with_S": n_on_sinit,
                            "n_wordEndingS_followed_by_le": end_s_le}
    legs["S4_pas_frames"] = {"verdict": "NEUTRAL",
                             "note": "word boundary before pas; no prediction"}
    return legs

battery = []
for s, r in SYL_SHORT:
    legs = syl_legs(s, r)
    passes = sum(1 for l in legs.values() if l["verdict"] == "PASS")
    kills = sum(1 for l in legs.values() if l["verdict"] == "KILL")
    battery.append({"candidate": s, "class": "S-syl", "legs": legs,
                    "passes": passes, "kills": kills})
for s, r, src in word_cands:
    if r == 0:
        legs = {"S1_rate": {"verdict": "KILL", "ratio": float("inf"),
                            "era_rate": 0.0, "note": "absent from v8"}}
        for k in ("S2_la_frame", "S3_on_frames", "S4_pas_frames"):
            legs[k] = {"verdict": "KILL", "note": "S1 kill cascades"}
    else:
        legs = word_legs(s, r)
    passes = sum(1 for l in legs.values() if l["verdict"] == "PASS")
    kills = sum(1 for l in legs.values() if l["verdict"] == "KILL")
    battery.append({"candidate": s, "class": "S-word", "src": src, "legs": legs,
                    "passes": passes, "kills": kills})
res["battery"] = battery

# ---------------- S5: successor-profile diagnostic (NOT scored) ----------------
SUFFIX_CELLS = {"29": "er", "40": "e"}          # GT suffix writers
WORDBOUNDARY_CELLS = {"11": "la", "77": "le", "46": "que"}
s5 = {
    "n48_to_suffix": sum(suc48[int(g)] for g in SUFFIX_CELLS),
    "n48_to_wordboundary": sum(suc48[int(g)] for g in WORDBOUNDARY_CELLS),
    "n48": n48,
    "frac_suffix": sum(suc48[int(g)] for g in SUFFIX_CELLS) / n48,
    "frac_wordboundary": sum(suc48[int(g)] for g in WORDBOUNDARY_CELLS) / n48,
    "note": "diagnostic only (T7); stems take suffix followers, words take "
            "word-initial followers",
}
res["S5_diagnostic"] = s5

# ---------------- S6: H_stem battery (separate) ----------------
GROUPS = sorted(set(pairs))
def cos_vec(c):
    return [c.get(g, 0) for g in GROUPS]
def cosine(a, b):
    va, vb = cos_vec(a), cos_vec(b)
    na = math.sqrt(sum(x * x for x in va)); nb = math.sqrt(sum(x * x for x in vb))
    return sum(x * y for x, y in zip(va, vb)) / (na * nb) if na and nb else 0.0

cos_48_96 = cosine(pre48, pre96)
freq = Counter(pairs)
big = [g for g in GROUPS if freq[g] >= 20]
cos_floor = sorted(cosine(pre48, Counter(pairs[i - 1] for i in windows(g) if i > 0))
                   for g in big if g != 48)
import statistics
floor_med = statistics.median(cos_floor)
s6a = {"cosine_pre_48_96": cos_48_96, "bar": 0.60,
       "floor_median_vs_n>=20": floor_med,
       "verdict": "PASS" if cos_48_96 >= 0.60 else "FAIL"}

# (b) Fisher exact on shared top-follower cells
top48 = {g for g, c in suc48.items() if c >= 2}
top96 = {g for g, c in suc96.items() if c >= 2}
a = len(top48 & top96)
b_ = len(top48 - top96)
c_ = len(top96 - top48)
d_ = 96 - a - b_ - c_
def fisher_exact(a, b, c, d):
    # two-sided via hypergeometric tail sum
    from math import comb
    n = a + b + c + d
    def hg(k):
        return comb(a + b, k) * comb(c + d, a + c - k) / comb(n, a + c)
    p_obs = hg(a)
    return sum(hg(k) for k in range(max(0, a + c - d), min(a + b, a + c) + 1)
               if hg(k) <= p_obs + 1e-12)
p_fish = fisher_exact(a, b_, c_, d_)
s6b = {"shared_top_followers": sorted(top48 & top96),
       "table": [[a, b_], [c_, d_]], "fisher_two_sided": p_fish,
       "verdict": "PASS" if p_fish < 0.05 else "FAIL"}

# (c) stem-signature: top-3 followers >= 40%
s48_sorted = suc48.most_common(3)
top3_48 = sum(c for _, c in s48_sorted) / n48
s96_sorted = suc96.most_common(3)
top3_96 = sum(c for _, c in s96_sorted) / n96 if n96 else 0
s6c = {"top3_share_48": top3_48, "top3_cells_48": [[g, c] for g, c in s48_sorted],
       "top3_share_96_calibration": top3_96,
       "top3_cells_96": [[g, c] for g, c in s96_sorted],
       "bar": 0.40, "verdict": "PASS" if top3_48 >= 0.40 else "FAIL"}
s6 = {"a_cosine": s6a, "b_fisher": s6b, "c_signature": s6c}
s6["verdict"] = ("LEAD"
                 if (s6a["verdict"] == "PASS" or s6b["verdict"] == "PASS")
                 and s6c["verdict"] == "PASS"
                 else "NULL (explicitly not adverse — underpowered, F64)")
res["S6_H_stem"] = s6

# ---------------- verdict tally ----------------
for b_ in battery:
    b_["recommendation"] = (
        "LEAD" if b_["passes"] >= 2 and b_["kills"] == 0
        else "LEAD-weak" if b_["passes"] == 1 and b_["kills"] == 0
        else "NULL")
res["summary"] = {
    "leads": [b_["candidate"] for b_ in battery if b_["recommendation"] == "LEAD"],
    "lead_weaks": [b_["candidate"] for b_ in battery if b_["recommendation"] == "LEAD-weak"],
    "killed": [b_["candidate"] for b_ in battery if b_["kills"] > 0],
}

with open(OUT / "battery48_syllable_results.json", "w") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
print(json.dumps(res["summary"], indent=1, ensure_ascii=False))
print("S6:", json.dumps(s6, indent=1)[:800])
