#!/usr/bin/env python3
import re, glob, unicodedata, os
CORP = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus")
GERMAN = {"allgemeine-zeitung-augsburg-1841-01-%02d.txt" % d for d in range(11, 26)} | {"adb-zeschau-heinrich-anton-von.txt", "harvest-log.txt"}
FR = sorted(f for f in glob.glob(CORP+"/*.txt") if os.path.basename(f) not in GERMAN)
def strip_acc(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

# find raw contexts of "me on" / "te on" / "en on" / "ce on" with punctuation visible
pats = [r"\bme\s+on\b", r"\bte\s+on\b", r"\ben\s+on\b", r"\bce\s+on\b"]
hits = {p: [] for p in pats}
for f in FR:
    txt = strip_acc(open(f, encoding="utf-8", errors="replace").read().lower())
    for p in pats:
        for m in re.finditer(p, txt):
            s = max(0, m.start()-60); e = min(len(txt), m.end()+60)
            ctx = txt[s:e].replace("\n", " ")
            hits[p].append((os.path.basename(f), ctx))
for p in pats:
    print(f"=== {p}: {len(hits[p])} raw hits")
    for fn, ctx in hits[p][:8]:
        print(f"  [{fn}] ...{ctx}...")
