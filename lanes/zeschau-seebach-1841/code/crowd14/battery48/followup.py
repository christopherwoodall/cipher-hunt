#!/usr/bin/env python3
"""Follow-ups: (1) era word-bigram self-repeat rate (A3-syl);
(2) 82-successor (vowel-initial) cells vs 94-precedence (elision test);
(3) P(vowel-initial) among -er infinitives (B4a independence check);
(4) 74-74 window glosses."""
import json, re, unicodedata
from collections import Counter
from pathlib import Path
from common import PAIRS, N, VALS, gloss, CORP, FILES

# ---- 82-successors = vowel-initial cells (82='m' GT elides only before vowel)
suc82 = Counter(PAIRS[i+1] for i, p in enumerate(PAIRS) if p == 82 and i < N-1)
vi_cells = set(suc82)
print("n82 =", sum(1 for p in PAIRS if p == 82), "| distinct 82-successors:", len(vi_cells))
print("82-successors:", dict(sorted(suc82.items())))
# does 94 ever precede a vowel-initial cell?
pos94 = [i for i, p in enumerate(PAIRS) if p == 94]
pre94_vi = sum(1 for i in pos94 if i+1 < N and PAIRS[i+1] in vi_cells)
print("94 precedes vowel-initial cell:", pre94_vi, "/", len(pos94))
# and specifically: 94 -> 82 (ne m') windows
n94_82 = sum(1 for i in pos94 if i+1 < N and PAIRS[i+1] == 82)
print("94->82 bigrams:", n94_82)

# ---- 74-74 windows glossed
for i in [417, 816, 861, 919, 1053, 1637]:
    ctx = PAIRS[i-2:i+5]
    print(i, ctx, gloss(ctx))

# ---- era: word-bigram self-repeat rate + P(vowel-initial | -er infinitive)
VOWELS = set("aàâäeéèêëiîïoôöuùûüy")
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
NOUN_STOP = {"france","prusse","grèce","grece","syrie","russie","guerre","paix",
  "cour","loi","mer","terre","pierre","lumière","lumiere","manière","maniere",
  "prière","priere","rivière","riviere","dernière","derniere","première","premiere",
  "affaire","misère","misere","colère","colere","bannière","banniere"}
def is_inf(w):
    return bool(re.search(r'(er|ir|re|oir)$', w)) and w not in NOUN_STOP

n_bi = n_self = 0
n_er = n_vi = 0
self_examples = Counter()
for f in FILES:
    toks = tokenize((CORP/f).read_text(encoding='utf-8', errors='replace'))
    for a, b in zip(toks, toks[1:]):
        if "'" in a or "'" in b: continue
        n_bi += 1
        if a == b:
            n_self += 1
            self_examples[a] += 1
    for w in toks:
        if is_inf(w) and w.endswith('er'):
            n_er += 1
            if w[0] in VOWELS: n_vi += 1
print("\nera word bigrams:", n_bi, "| self-repeat:", n_self, "| rate:", round(n_self/n_bi, 5))
print("top self-repeat words:", self_examples.most_common(8))
print("P(vowel-initial | -er inf):", round(n_vi/n_er, 4), f"({n_vi}/{n_er})")
print("independence expectation for B4a: 0.133 *", round(n_vi/n_er,4), "=", round(0.133*n_vi/n_er,4))
