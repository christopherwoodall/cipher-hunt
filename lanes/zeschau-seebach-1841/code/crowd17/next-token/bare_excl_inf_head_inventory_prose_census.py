#!/usr/bin/env python3
"""Bare exclamatory infinitive head-inventory census, prose.

Target: bare-excl-inf-head-inventory-prose (battery, crowd17 next-token).
Bar (pre-registered): "A ranked head-class inventory; if demonstratives sit
inside a licensed class, the grammatical blocker is weakened."

Corpus: verbatim the 20-file prose corpus of the prose batteries
(personal-tonic-bare-inf-prose-inventory): 17 files in
code/side-period/corpus/, 3 files in lane data/ (27,656,185 chars total).

Method: verbatim the drama sibling
(bare_excl_inf_head_inventory_drama_census.py) head-classification method:
for each '!'-terminated clause (window up to 160 chars), find an
infinitive-shaped word within the first 40 chars of the clause; exclude if a
subject pronoun / finite-verb marker / governor / 'que' precedes it. Classify
the head text before the infinitive:
  DEM_TOPIC  - demonstrative as fronted topic (cela/ceci/ca/celui...)
  TONIC      - tonic pronoun (moi/toi/lui...)
  NOUN       - other nominal material
  ZERO       - zero topic (infinitive first)
  OTHER      - residual
"""
import os, re, json

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUSDIR = os.path.join(LANE, "code/side-period/corpus")
DATADIR = os.path.join(LANE, "data")
OUT = os.path.join(LANE, "code/crowd17/next-token",
                   "bare-excl-inf-head-inventory-prose_census.json")

FILES = [  # (dir, filename) — identical to the parent prose battery's corpus
    (CORPUSDIR, "guizot-memoires-t1-gutenberg.txt"),
    (CORPUSDIR, "guizot-memoires-t2-gutenberg.txt"),
    (CORPUSDIR, "guizot-memoires-t3-gutenberg.txt"),
    (CORPUSDIR, "guizot-memoires-t5-t6.txt"),
    (CORPUSDIR, "nesselrode-v7.txt"),
    (CORPUSDIR, "nesselrode-v8.txt"),
    (CORPUSDIR, "nesselrode-v9.txt"),
    (CORPUSDIR, "nesselrode-v10.txt"),
    (CORPUSDIR, "revue-deux-mondes-1841-q1.txt"),
    (CORPUSDIR, "revue-deux-mondes-1841-q2.txt"),
    (CORPUSDIR, "revue-deux-mondes-1841-q3.txt"),
    (CORPUSDIR, "revue-deux-mondes-1841-q4.txt"),
    (CORPUSDIR, "metternich-papiere-v4.txt"),
    (CORPUSDIR, "metternich-papiere-v6.txt"),
    (CORPUSDIR, "talleyrand-memoires-v1.txt"),
    (CORPUSDIR, "pozzo-di-borgo-correspondance-v1.txt"),
    (CORPUSDIR, "levant-correspondence-1841-p3.txt"),
    (DATADIR, "gutenberg-17489-miserables1.txt"),
    (DATADIR, "gutenberg-30513-tocqueville-t1.txt"),
    (DATADIR, "gutenberg-30514-tocqueville-t2.txt"),
]

INF = re.compile(r"\b([a-zàâäçéèêëîïôöùûü]{2,}(er|ir|re|oir))\b", re.IGNORECASE)
EXCL = re.compile(
    r"\b(je|tu|il|elle|nous|vous|ils|elles|on|ça|que|qui|à|de|d'|"
    r"pour|sans|fait|faut|veux|veut|dois|doit|peux|peut|sais|sait|"
    r"vais|va|allons|êtes|est|sont|était|étaient)\b", re.IGNORECASE)
DEM = re.compile(r"\b(cela|ceci|ç[aà]|celui(?:-là|-ci)?|celle(?:-là|-ci)?|"
                 r"ceux(?:-là|-ci)?|celles(?:-là|-ci)?)\s*[,;:—–-]*\s*$", re.IGNORECASE)
DEM_ANY = re.compile(r"\b(cela|ceci|ç[aà]|celui(?:-là|-ci)?|celle(?:-là|-ci)?|"
                     r"ceux(?:-là|-ci)?|celles(?:-là|-ci)?)\b", re.IGNORECASE)
TONIC = re.compile(r"\b(moi|toi|lui|elle|nous|vous|eux|elles?)\s*[,;:—–-]*\s*$", re.IGNORECASE)
DET_NOUN = re.compile(r"\b(le|la|les|un|une|des|du|mon|ton|son|notre|votre|"
                      r"ce|cet|cette|ces)\s+\w", re.IGNORECASE)

def head_class(pre):
    p = pre.strip()
    if not p:
        return "ZERO"
    if DEM.search(p):
        return "DEM_TOPIC"
    if TONIC.search(p):
        return "TONIC"
    if DEM_ANY.search(p):
        return "DEM_OTHER"
    if DET_NOUN.search(p):
        return "NOUN"
    return "OTHER"

def main():
    cands, total = [], 0
    for d, f in FILES:
        p = os.path.join(d, f)
        text = open(p, encoding="utf-8", errors="replace").read()
        total += len(text)
        for cl in re.split(r"(?<=[!?])", text):
            if not cl.strip().endswith("!"):
                continue
            win = cl[-160:].strip()
            m = INF.search(win[:40])
            if not m:
                continue
            pre = win[:m.start()]
            if EXCL.search(pre):
                continue
            cands.append({
                "file": f, "head": pre.strip(),
                "inf": m.group(1), "head_class": head_class(pre),
                "window": win,
            })
    by_class = {}
    for c in cands:
        by_class[c["head_class"]] = by_class.get(c["head_class"], 0) + 1
    json.dump({"total_chars": total, "files": [f for _, f in FILES],
               "n_candidates": len(cands),
               "by_class": by_class, "candidates": cands},
              open(OUT, "w"), ensure_ascii=False, indent=1)
    print("chars:", total, "candidates:", len(cands), "by_class:", by_class)

if __name__ == "__main__":
    main()
