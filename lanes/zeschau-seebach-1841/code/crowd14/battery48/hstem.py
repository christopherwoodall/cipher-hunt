#!/usr/bin/env python3
"""B: H_stem battery (round 14 battery48). Implements PREREG.md Battery 2.

B3 (cipher): re-derive the 3 stem+inflection windows (asserts); 48 successor
habitat census vs 06/94 comparators; B3c names the «94 48» construction
(red-team caveat 3).
B4 (era): vowel-initial [stem]["er"] share; "m'"+vowel-inf contact;
vowel-initial [stem]["e"] habitat (report-only).
"""
import json, re, unicodedata
from collections import Counter
from pathlib import Path
from common import PAIRS, N, VALS, gloss, CORP, FILES

INF = {29, 40, 6, 59}    # inflection inventory
WSEG = {46, 47}          # word cells that cannot follow a stem mid-word

# ---------------- B3a: re-derivation (asserts) ----------------
checks = [
    (1229, 48, 29), (1230, 29, None),
    (1589, 48, 29), (1590, 29, None),
    (1398, 48, 40), (1399, 40, None),
    (1228, 82, None),
]
for pos, cell, _ in checks:
    assert PAIRS[pos] == cell, (pos, PAIRS[pos], cell)
b3a = {}
for pos in (1229, 1589, 1398):
    ctx = PAIRS[pos-4:pos+5]
    b3a[str(pos)] = {"ctx": ctx, "gloss": gloss(ctx),
                     "suc": PAIRS[pos+1], "pre": PAIRS[pos-1]}

# ---------------- B3b: successor habitat census ----------------
pos48 = [i for i, p in enumerate(PAIRS) if p == 48]
assert len(pos48) == 38
suc48 = Counter(PAIRS[i+1] for i in pos48 if i < N-1)
pre48 = Counter(PAIRS[i-1] for i in pos48 if i > 0)
n_inf = sum(suc48.get(c, 0) for c in INF)
n_wseg = sum(suc48.get(c, 0) for c in WSEG)

def suc_profile(cell):
    pos = [i for i, p in enumerate(PAIRS) if p == cell]
    s = Counter(PAIRS[i+1] for i in pos if i < N-1)
    return len(pos), s, sum(s.get(c, 0) for c in INF)

n06, s06, inf06 = suc_profile(6)
n94, s94, inf94 = suc_profile(94)

def fisher_2x2(a, b, c, d):
    # Fisher exact, two-sided via hypergeometric enumeration
    from math import comb
    n = a+b+c+d
    def hg(x):
        return comb(a+b, x)*comb(c+d, a+c-x)/comb(n, a+c) if 0 <= x <= a+b and 0 <= a+c-x <= c+d else 0
    p_obs = hg(a)
    return sum(hg(x) for x in range(0, min(a+b, a+c)+1) if hg(x) <= p_obs + 1e-18)

b3b = {
  "n48": len(pos48),
  "suc48": dict(sorted(suc48.items())),
  "pre48": dict(sorted(pre48.items())),
  "n_suc_INF": n_inf, "INF_detail": {str(c): suc48.get(c, 0) for c in sorted(INF)},
  "n_suc_WSEG": n_wseg, "WSEG_detail": {str(c): suc48.get(c, 0) for c in sorted(WSEG)},
  "cmp_06": {"n": n06, "n_suc_INF": inf06, "suc": dict(sorted(s06.items()))},
  "cmp_94": {"n": n94, "n_suc_INF": inf94, "suc": dict(sorted(s94.items()))},
  "fisher_48_vs_06": fisher_2x2(n_inf, len(pos48)-n_inf, inf06, n06-inf06),
  "fisher_48_vs_94": fisher_2x2(n_inf, len(pos48)-n_inf, inf94, n94-inf94),
  "kill_falsifier": {"n_suc_INF_eq_0": n_inf == 0, "n_suc_WSEG_ge_5": n_wseg >= 5},
}

# ---------------- B3c: name the «94 48» construction ----------------
pos_94_48 = [i for i in pos48 if i > 0 and PAIRS[i-1] == 94]
b3c_windows = {}
for i in pos_94_48:
    ctx = PAIRS[i-3:i+5]
    b3c_windows[str(i)] = {"ctx": ctx, "gloss": gloss(ctx)}
b3c = {"n_94_pre_48": len(pos_94_48), "positions": pos_94_48,
       "windows": b3c_windows,
       "named": len(pos_94_48) >= 2}

# ---------------- B4: era ----------------
VOWELS = set("aàâäeéèêëiîïoôöuùûüy")
def byear_syllables(word):
    if "'" in word and len(word) <= 3:
        return [word]
    vs = [i for i, ch in enumerate(word) if ch in VOWELS]
    if not vs:
        return [word]
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
        cuts.append(a1 + 2 if c >= 1 else a1 + 1)
    parts, start = [], 0
    for cut in cuts:
        parts.append(word[start:cut]); start = cut
    parts.append(word[start:])
    return [p for p in parts if p]

NOUN_STOP = {"france","prusse","grèce","grece","syrie","russie","guerre","paix",
  "cour","loi","mer","terre","pierre","lumière","lumiere","manière","maniere",
  "prière","priere","rivière","riviere","dernière","derniere","première","premiere",
  "affaire","misère","misere","colère","colere","bannière","banniere"}
def is_inf(w):
    return bool(re.search(r'(er|ir|re|oir)$', w)) and w not in NOUN_STOP

WORD = re.compile(r"[^\W\d_]+(?:'[^\W\d_]+)?", re.UNICODE)
def tokenize(text):
    text = unicodedata.normalize('NFC', text.lower().replace('\u2019',"'").replace('\u2018',"'"))
    toks = []
    for m in WORD.finditer(text):
        w = m.group(0)
        parts = w.split("'")
        for i, p in enumerate(parts):
            if not p: continue
            toks.append(p + "'" if i < len(parts)-1 else p)
    return toks

# B4a: vowel-initial [stem]["er"]
n_er, n_vi_split, vi_examples = 0, 0, []
# B4b: "m'" + vowel-initial -er infinitive
mprime_hits = []
# B4c: vowel-initial [stem]["e"] tokens
n_e, e_examples = 0, []
for f in FILES:
    toks = tokenize((CORP/f).read_text(encoding='utf-8', errors='replace'))
    for j, w in enumerate(toks):
        if is_inf(w) and w.endswith('er'):
            n_er += 1
            s = byear_syllables(w)
            if len(s) == 2 and s[1] == 'er' and s[0][0] in VOWELS:
                n_vi_split += 1
                if len(vi_examples) < 20: vi_examples.append((w, s))
        if w == "m'" and j+1 < len(toks):
            nxt = toks[j+1]
            if is_inf(nxt) and nxt.endswith('er') and nxt[0] in VOWELS:
                mprime_hits.append((f, nxt))
        if w.endswith('e') and "'" not in w and len(w) >= 3:
            s = byear_syllables(w)
            if len(s) == 2 and s[1] == 'e' and s[0][0] in VOWELS and len(s[0]) >= 2:
                n_e += 1
                if len(e_examples) < 20: e_examples.append((w, s))

share = n_vi_split / n_er if n_er else 0
b4 = {
  "B4a": {"n_er_infinitives": n_er, "n_vowelinit_stem_er": n_vi_split,
          "share": round(share, 4), "examples": vi_examples,
          "licenses": share >= 0.05},
  "B4b": {"n_mprime_vowel_inf": len(mprime_hits),
          "examples": mprime_hits[:20],
          "contact_licenses": len(mprime_hits) >= 3},
  "B4c": {"n_vowelinit_stem_e": n_e, "examples": e_examples},
}

out = {"B3a": b3a, "B3b": b3b, "B3c": b3c, "B4": b4}
Path(LANE := Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841')  # noqa
Path.home().joinpath('workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd14/battery48/hstem_raw.json').write_text(
    json.dumps(out, ensure_ascii=False, indent=1))
print("B3a windows re-derived:", list(b3a.keys()))
print("B3b: n48=38 | suc_INF =", n_inf, b3b["INF_detail"], "| suc_WSEG =", n_wseg, b3b["WSEG_detail"])
print("     06: n =", n06, "INF =", inf06, "| 94: n =", n94, "INF =", inf94)
print("     fisher 48v06 =", round(b3b["fisher_48_vs_06"],4), "| 48v94 =", round(b3b["fisher_48_vs_94"],4))
print("B3c: n_94_pre_48 =", len(pos_94_48), pos_94_48)
print("B4a: -er inf =", n_er, "| vowel-init [stem][er] =", n_vi_split, "| share =", round(share,4))
print("B4b: m'+vowel-inf =", len(mprime_hits))
print("B4c: vowel-init [stem][e] =", n_e)
