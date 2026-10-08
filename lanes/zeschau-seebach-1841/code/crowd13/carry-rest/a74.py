#!/usr/bin/env python3
"""A: 74-class battery (round 13 carry-rest). Implements PREREG.md section A.

Cipher: full contact profile of 74 (n expected 34) + +-3 windows, glossed with
banked/provisional values. Era: exhaustive clean-diplo "de ce que" L1 census
(distinct L1 + counts + sample contexts) for [FR-JUDGMENT] classification.
v8 L1s taken from round-12 followup48 (frozen input, not re-derived).
"""
import json, re, sys, unicodedata
from pathlib import Path
from collections import Counter
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
sys.path.insert(0, str(LANE / 'code/crowd7/keystruct'))
from aliasing import load_stream

PAIRS = load_stream()
N = len(PAIRS)
assert N == 1847, N

VALS = {11: 'la', 70: 'pre', 82: 'm', 34: 'i', 29: 'er', 40: 'e', 46: 'que',
        87: 'ce?', 64: 'qui?', 96: 'par?', 59: 'est/-este?', 77: 'le?',
        62: 'on~fenced', 52: 'pas~', 94: 'ne?'}
def gloss(p):
    return [str(x) if x not in VALS else f"{x}={VALS[x]}" for x in p]

pos74 = [i for i, p in enumerate(PAIRS) if p == 74]
pre = Counter(PAIRS[i - 1] for i in pos74 if i > 0)
suc = Counter(PAIRS[i + 1] for i in pos74 if i < N - 1)
pre2 = Counter(PAIRS[i - 2] for i in pos74 if i > 1)
suc2 = Counter(PAIRS[i + 2] for i in pos74 if i < N - 2)
windows = {i: {"ctx": PAIRS[max(0, i-3):i+4], "gloss": gloss(PAIRS[max(0, i-3):i+4])}
           for i in pos74}

# class-discriminating checks on banked/provisional values
checks = {
    "n74": len(pos74),
    "verb_adverse_74_suc77": suc.get(77, 0),   # verb + postposed "le" = ungrammatical
    "verb_adverse_74_suc87": suc.get(87, 0),   # verb + postposed "ce(dem)" = ungrammatical
    "noun_adj_pre_article": pre.get(11, 0) + pre.get(87, 0),
    "part_aux_pre59": pre.get(59, 0),          # "est 74" participle signature (59=est prov)
    "pre_94_ne": pre.get(94, 0),
    "suc_46_que": suc.get(46, 0),
    "suc_47_ce": suc.get(47, 0),
    "suc_48": suc.get(48, 0),
    "self_loop_74_74": pre.get(74, 0),
}
res = {"n": N, "n74": len(pos74), "pre": dict(pre), "suc": dict(suc),
       "pre2": dict(pre2), "suc2": dict(suc2), "windows": windows, "checks": checks}

# ---------------- era: clean-diplo "de ce que" L1 census ----------------
CORP = LANE / 'code/side-period/corpus'
FILES = ['guizot-memoires-t1-gutenberg.txt', 'guizot-memoires-t2-gutenberg.txt',
         'guizot-memoires-t3-gutenberg.txt', 'guizot-memoires-t5-t6.txt',
         'metternich-papiere-v4.txt', 'metternich-papiere-v6.txt',
         'pozzo-di-borgo-correspondance-v1.txt', 'levant-correspondence-1841-p3.txt',
         'talleyrand-memoires-v1.txt', 'revue-deux-mondes-1841-q1.txt',
         'revue-deux-mondes-1841-q2.txt', 'revue-deux-mondes-1841-q3.txt',
         'revue-deux-mondes-1841-q4.txt']
WORD = re.compile(r"[^\W\d_]+(?:'[^\W\d_]+)?", re.UNICODE)
def tokenize(text):
    text = unicodedata.normalize('NFC', text.lower().replace('\u2019', "'").replace('\u2018', "'"))
    toks = []
    for m in WORD.finditer(text):
        w = m.group(0)
        parts = w.split("'")
        for i, p in enumerate(parts):
            if not p:
                continue
            toks.append(p + "'" if i < len(parts) - 1 else p)
    return toks

toks, per_file = [], {}
for f in FILES:
    t = tokenize((CORP / f).read_text(encoding='utf-8', errors='replace'))
    per_file[f] = len(t)
    toks.extend(t)
hits = [(i, toks[i-1]) for i in range(1, len(toks) - 1)
        if toks[i] == 'de' and toks[i+1] == 'ce' and toks[i+2] == 'que']
l1c = Counter(l1 for _, l1 in hits)
examples = {}
for i, l1 in hits:
    if l1 not in examples:
        examples[l1] = ' '.join(toks[max(0, i-8):i+4])
res["era"] = {"files": FILES, "tokens": len(toks), "per_file": per_file,
              "n_de_ce_que": len(hits), "L1_counts": dict(l1c.most_common()),
              "L1_examples": examples}
# v8 L1s: frozen round-12 input (followup48 863-a)
res["v8_L1_frozen"] = {"piqué": 1, "heureux": 1, "courant": 1, "quart": 1,
    "contente": 1, "compte": 1, "contraire": 1, "opposé": 1, "fâchés": 1,
    "paris->satisfait": 1, "note": "paris is a misparse; true L1='satisfait' (adj)"}

out = LANE / 'code/crowd13/carry-rest/a74_raw.json'
out.write_text(json.dumps(res, ensure_ascii=False, indent=1))
print("n74 =", len(pos74), "| clean-diplo tokens =", len(toks),
      "| n_de_ce_que =", len(hits), "| distinct L1 =", len(l1c))
print("top L1:", l1c.most_common(15))
print("checks:", json.dumps(checks, ensure_ascii=False))
