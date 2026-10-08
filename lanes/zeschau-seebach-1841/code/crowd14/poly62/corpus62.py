#!/usr/bin/env python3
"""Corpus instruments for the 62-polyvalence battery.
Pool: code/side-period/corpus/*.txt French files (v8 phrase-zero caveat noted).
Tokenizer: lowercase, elision-split (l'/d'/qu'/s'/n'/m'/t'/y'/c' split off), words = [a-z + accents]."""
import re, glob, unicodedata, os
from collections import Counter

CORP = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus")
GERMAN = {"allgemeine-zeitung-augsburg-1841-01-%02d.txt" % d for d in range(11, 26)} | {"adb-zeschau-heinrich-anton-von.txt", "harvest-log.txt"}
FR = sorted(f for f in glob.glob(CORP+"/*.txt") if os.path.basename(f) not in GERMAN)

def strip_acc(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

def tokenize(text):
    text = strip_acc(text.lower())
    text = re.sub(r"\b([ldsqnmtcyj])'", r"\1' ", text)  # elision split
    text = text.replace("’", "'")
    toks = re.findall(r"[a-z]+(?:'[a-z]+)?", text)
    out = []
    for t in toks:
        if "'" in t:
            a, b = t.split("'", 1)
            out += [a+"'", b] if a else [b]
        else:
            out.append(t)
    return [t for t in out if t]

def load(files):
    toks = []
    for f in files:
        toks += tokenize(open(f, encoding="utf-8", errors="replace").read())
    return toks

if __name__ == "__main__":
    ALL = load(FR)
    PRIM = load([f for f in FR if os.path.basename(f) in ("nesselrode-v8.txt", "levant-correspondence-1841-p3.txt")])
    print("tokens: all-fr =", len(ALL), "| primary-diplomatic =", len(PRIM))
    for name, toks in (("ALL", ALL), ("PRIM", PRIM)):
        bi = Counter(zip(toks, toks[1:]))
        n_on = sum(1 for t in toks if t == "on")
        print(f"--- {name}: n(tokens)={len(toks)} n(standalone 'on')={n_on}")
        for pre in ["me", "te", "se", "en", "ce", "le", "la", "ne", "que", "si", "et", "y", "nous", "vous", "il", "elle", "ils", "qu'", "lorsque", "quand", "comme", "puisque", "d'", "m'", "t'", "s'"]:
            print(f"   '{pre} on' = {bi.get((pre,'on'),0)}")
        # internal-'on' substrings: tokens (len>2) containing 'on' not standalone
        internal = [t for t in toks if t != "on" and "on" in t]
        print(f"   tokens with internal 'on' substring (len>2, excl standalone) = {len(internal)}")
        ic = Counter(internal)
        print("   top internal-on types:", ic.most_common(15))
    json_out = {"n_all": len(ALL), "n_prim": len(PRIM)}
    import json
    json.dump(json_out, open("corpus62_counts.json", "w"))
