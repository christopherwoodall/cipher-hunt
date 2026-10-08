#!/usr/bin/env python3
import sys, glob, os, unicodedata, re
sys.path.insert(0, os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period"))
from syllabify import syllabify, strip_acc
CORP = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus")
files = [CORP+"/nesselrode-v8.txt", CORP+"/levant-correspondence-1841-p3.txt"]
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
pat = re.compile(r"^[^aeiouy]*on$")
n_onNuc = sum(1 for s in syls if pat.match(strip_acc(s)))
n_onWord = sum(1 for w in words if w == "on")
print(f"words={n_words} syllables={n_syl}")
print(f"syllables with 'on'-nucleus: {n_onNuc}  rate/syl={n_onNuc/n_syl:.4f} -> x1847 groups = {n_onNuc/n_syl*1847:.1f}")
print(f"standalone 'on': {n_onWord} -> x1847 = {n_onWord/n_words*1847:.1f}")
print(f"observed n62=35. on-nucleus model: {n_onNuc/n_syl*1847:.1f} expected; pronoun-only model: {n_onWord/n_words*1847:.1f} expected")
print(f"internal-on share of on-nuclei: {(n_onNuc-n_onWord)/n_onNuc:.3f} -> cipher-internal expectation: {35*(n_onNuc-n_onWord)/n_onNuc:.1f} of 35")
