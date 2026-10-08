#!/usr/bin/env python3
import re, glob, os, unicodedata
from collections import Counter
CORP = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus")
def strip_acc(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
def toks(text):
    text = strip_acc(text.lower()).replace("’", "'")
    text = re.sub(r"\b([ldsqnmtcyj])'", r"\1' ", text)
    out = []
    for t in re.findall(r"[a-z]+(?:'[a-z]+)?", text):
        out += t.split("'") if "'" in t else [t]
    return [t for t in out if t and t != "'"]
words = []
for f in [CORP+"/nesselrode-v8.txt", CORP+"/levant-correspondence-1841-p3.txt"]:
    words += toks(open(f, encoding="utf-8", errors="replace").read())
bi = Counter(zip(words, words[1:]))
n_on = sum(1 for w in words if w == "on")
print(f"n(on)={n_on}")
for x in ["a", "à", "et", "de", "es", "il", "les", "te", "un", "com", "en", "est", "par", "pour", "ne", "bien", "souvent", "toujours", "y"]:
    c = bi.get(("on", x), 0)
    print(f"  'on {x}' = {c}  ({c/n_on*100:.2f}% of on)")
