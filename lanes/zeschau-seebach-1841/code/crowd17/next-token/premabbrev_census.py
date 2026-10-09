#!/usr/bin/env python3
"""Census of 'pre.'-family abbreviation tokens in the lane period corpus.
Target: does 'pre.' ever stand for 'premier/première' as a whole word?
"""
import os, re, unicodedata, json

CORPUS = os.path.dirname(os.path.abspath(__file__)).replace(
    "code/crowd17/next-token", "code/side-period/corpus")

def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower()

files = sorted(f for f in os.listdir(CORPUS) if f.endswith(".txt"))
total_chars = 0
hits = []  # (file, line_no, token, context)
full_premier = 0
ordinal_1er = 0

# abbreviation patterns: pr., pre., prem., premi., premier., premiers., also 'pr' forms
abbrev_re = re.compile(r"\b(p)re{0,1}m{0,1}i{0,1}e{0,1}r{0,1}s{0,1}\.", re.IGNORECASE)
# more precise: pr. pre. prem. premi. premier. premiers. (must not be longer word prefix
# e.g. 'apre.' is excluded by \b; 'prex.' excluded by pattern)
precise_re = re.compile(r"\b(pr|pre|prem|premi|premier|premiers)\.", re.IGNORECASE)
ordinal_re = re.compile(r"\b([1iIl])\s?(er|ers|re|res|e?s?)\b")
ordinal_strict = re.compile(r"\b1\s?(er|ers|re|res)\b|\bI\s?(er|re)\b", re.IGNORECASE)
full_re = re.compile(r"\bpremiers?\b|\bpremieres?\b", re.IGNORECASE)

def context_of(lines, i, m):
    lo = max(0, i - 1)
    hi = min(len(lines), i + 2)
    ctx = " ".join(l.strip() for l in lines[lo:hi])
    return ctx[:320]

for fn in files:
    path = os.path.join(CORPUS, fn)
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read()
    except Exception as e:
        print("SKIP", fn, e)
        continue
    total_chars += len(text)
    lines = text.splitlines()
    ntext = norm(text)
    full_premier += len(full_re.findall(ntext))
    ordinal_1er += len(ordinal_strict.findall(ntext))
    for i, line in enumerate(lines):
        nline = norm(line)
        for m in precise_re.finditer(nline):
            hits.append((fn, i + 1, m.group(0), context_of(lines, i, m)))

print(f"files={len(files)} chars={total_chars}")
print(f"full 'premier/premiere' tokens (norm): {full_premier}")
print(f"standard ordinal '1er/1re' tokens: {ordinal_1er}")
print(f"abbrev 'pr./pre./prem./premi.' hits: {len(hits)}")

# group by token
from collections import Counter
c = Counter(h[2] for h in hits)
print("by token:", dict(c))

out = {"files": len(files), "chars": total_chars, "full_premier": full_premier,
       "ordinal_1er": ordinal_1er, "by_token": dict(c),
       "hits": [{"file": h[0], "line": h[1], "token": h[2], "ctx": h[3]} for h in hits]}
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "premabbrev_hits.json"), "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("wrote premabbrev_hits.json")
