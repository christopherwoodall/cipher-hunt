#!/usr/bin/env python3
"""Syllable-rate test: is n62=35 consistent with monovalent pronoun-'on', or with an 'on'-syllable cell?
Uses side-period syllabify.py (heuristic; F30 caveat: encipherer cuts finer than standard)."""
import sys, glob, os, unicodedata, re
sys.path.insert(0, os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period"))
from syllabify import syllabify, strip_acc
CORP = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus")
files = [f for f in glob.glob(CORP+"/nesselrode-v8.txt")] + [f for f in glob.glob(CORP+"/levant-correspondence-1841-p3.txt")]
def toks(text):
    text = strip_acc(text.lower()).replace("’", "'")
    text = re.sub(r"\b([ldsqnmtcyj])'", r"\1' ", text)
    out = []
    for t in re.findall(r"[a-z]+(?:'[a-z]+)?", text):
        out += t.split("'") if "'" in t else [t]
    return [t for t in out if t and t != "'"]
words = []
for f in files: words += toks(open(f, encoding="utf-8", errors="replace").read())
n_words = len(words)
syls = []
for w in words:
    try: syls += syllabify(w)
    except Exception: syls += [w]
n_syl = len(syls)
# 'O' = the on-nasal nucleus per syllabify.py
n_O = sum(1 for s in syls if "O" in s)
n_on_word = sum(1 for w in words if w == "on")
print(f"words={n_words} syllables={n_syl} (syl/word={n_syl/n_words:.2f})")
print(f"'O'-nucleus syllables={n_O}  rate/syl={n_O/n_syl:.4f} -> x1847 = {n_O/n_syl*1847:.1f}")
print(f"standalone 'on' words={n_on_word} rate/word={n_on_word/n_words:.4f} -> x~1100 words = {n_on_word/n_words*1100:.1f}; x1847 groups(as words) = {n_on_word/n_words*1847:.1f}")
print(f"observed n62=35  (35/1847={35/1847:.4f} per group)")
print(f"monovalent-pronoun expectation shortfall: 35 / {n_on_word/n_words*1847:.1f} = {35/(n_on_word/n_words*1847):.2f}x")
