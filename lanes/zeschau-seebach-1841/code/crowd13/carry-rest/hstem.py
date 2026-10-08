#!/usr/bin/env python3
"""B: H_stem battery (round 13 carry-rest). Implements PREREG.md section B.

B1 (cipher): gloss the three stem+inflection windows (48->29 @1229/@1589,
48->40 @1398) with banked values; compatibility checks.
B2 (era): by-ear v1.2 (verbatim) share of clean-diplo -er infinitives whose
parse is exactly [stem-cell]["er"].
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

# ---- B1: the three windows ----
targets = {1229: 29, 1589: 29, 1398: 40}
b1 = {}
for pos, succell in targets.items():
    assert PAIRS[pos] == 48 and PAIRS[pos + 1] == succell, (pos, PAIRS[pos:pos+2])
    b1[str(pos)] = {"suc": succell,
                    "ctx": PAIRS[pos-3:pos+4],
                    "gloss": gloss(PAIRS[pos-3:pos+4])}
# global 48 successor profile (context for "natural habitat")
pos48 = [i for i, p in enumerate(PAIRS) if p == 48]
suc48 = Counter(PAIRS[i+1] for i in pos48 if i < N - 1)
pre48 = Counter(PAIRS[i-1] for i in pos48 if i > 0)
# 82-precedes-48 count (vowel-initial lead datum)
n_82pre48 = pre48.get(82, 0)

# ---- B2: by-ear v1.2 verbatim ----
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
        parts.append(word[start:cut])
        start = cut
    parts.append(word[start:])
    return [p for p in parts if p]

NOUN_STOP = {"france","prusse","grèce","grece","syrie","russie","guerre","paix",
  "cour","loi","mer","terre","pierre","lumière","lumiere","manière","maniere",
  "prière","priere","rivière","riviere","dernière","derniere","première","premiere",
  "affaire","misère","misere","colère","colere","bannière","banniere"}
def is_inf(w):
    return bool(re.search(r'(er|ir|re|oir)$', w)) and w not in NOUN_STOP

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

infs, split_er, examples = [], 0, []
for f in FILES:
    for w in tokenize((CORP / f).read_text(encoding='utf-8', errors='replace')):
        if is_inf(w) and w.endswith('er'):
            infs.append(w)
            s = byear_syllables(w)
            if len(s) == 2 and s[1] == 'er':
                split_er += 1
                if len(examples) < 20:
                    examples.append((w, s))
share = split_er / len(infs) if infs else 0

res = {"n": N, "B1_windows": b1,
       "B1": {"n48": len(pos48), "suc48": dict(suc48), "pre48_82": n_82pre48,
              "n_48_suc29": suc48.get(29, 0), "n_48_suc40": suc48.get(40, 0)},
       "B2": {"n_er_infinitives": len(infs), "n_stem_plus_bare_er": split_er,
              "share": round(share, 4), "examples": examples}}
out = LANE / 'code/crowd13/carry-rest/hstem_raw.json'
out.write_text(json.dumps(res, ensure_ascii=False, indent=1))
print("B1 windows ok:", list(b1.keys()), "| n48 =", len(pos48),
      "| 48->29:", suc48.get(29, 0), "| 48->40:", suc48.get(40, 0),
      "| 82-pre-48:", n_82pre48)
print("B2: -er infinitives =", len(infs), "| [stem]['er'] =", split_er,
      "| share =", round(share, 4))
