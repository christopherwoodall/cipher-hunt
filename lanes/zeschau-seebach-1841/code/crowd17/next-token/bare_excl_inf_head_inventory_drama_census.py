#!/usr/bin/env python3
"""Bare exclamatory infinitive head-inventory census, drama dialogue.

Target: bare-excl-inf-head-inventory-drama (battery, crowd17 next-token).
Bar: Census of bare exclamatory infinitives in drama dialogue lands with a
head-type table (topic-demonstrative vs other); >=1 demonstrative-headed hit
re-opens arm (a) of ce87-1028-role.

Corpus: same 14-file drama corpus as disloc-demonstrative-drama-dialogue
(Hugo/Dumas/Vigny/Musset; Hetzel 1889 Hernani; hugo-hernani-1870.txt excluded
per the one-edition rule).

Pass: for each '!' clause (window up to 160 chars), find an infinitive-shaped
word within the first 40 chars of the clause; exclude if a subject
pronoun/finite-verb/governor/que appears before it. Classify the head text
before the infinitive:
  DEM_TOPIC  - demonstrative as fronted topic (cela/ceci/ca/celui...)
  TONIC      - tonic pronoun (moi/toi/lui...)
  NOUN       - other nominal material
  ZERO       - zero topic (infinitive first)
  OTHER      - residual
"""
import os, re, json

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
PLAYS = [
    "dumas-antony.txt",
    "dumas-henri-iii.txt",
    "dumas-kean.txt",
    "dumas-mariage-louis-xv-1841.txt",
    "dumas-tour-de-nesle.txt",
    "hugo-burgraves.txt",
    "hugo-hernani.txt",          # Hetzel 1889 wikisource ed.
    "hugo-ruy-blas.txt",
    "labiche-chapeau-de-paille.txt",
    "labiche-martin-poudre-aux-yeux.txt",
    "musset-comedies-proverbes-1850.txt",
    "scribe-bertrand-et-raton.txt",
    "scribe-verre-d-eau.txt",
    "vigny-chatterton-1835.txt",
]
OUT = os.path.join(LANE, "code/crowd17/next-token",
                   "bare-excl-inf-head-inventory-drama_census.json")

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
    for f in PLAYS:
        p = os.path.join(LANE, "code/side-period/corpus", f)
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
    json.dump({"total_chars": total, "plays": PLAYS, "n_candidates": len(cands),
               "by_class": by_class, "candidates": cands},
              open(OUT, "w"), ensure_ascii=False, indent=1)
    print("chars:", total, "candidates:", len(cands), "by_class:", by_class)

if __name__ == "__main__":
    main()
