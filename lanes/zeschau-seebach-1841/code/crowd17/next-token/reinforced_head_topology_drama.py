#!/usr/bin/env python3
r"""Extraction script for battery reinforced-head-topology-drama.

Reproduces the 41 dem-comma windows (reinforced demonstrative + [,;:])
in the 14-play drama corpus with 500-char context for hand classification.
Verbatim DEM_REINF inventory and drama file list from
reinforced_pour_inf_drama_census.py (parent battery).

Output: reinforced-head-topology-drama_windows.json in this directory.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

DRAMA = [
    "dumas-mariage-louis-xv-1841.txt",
    "vigny-chatterton-1835.txt",
    "musset-comedies-proverbes-1850.txt",
    "hugo-hernani.txt",
    "hugo-ruy-blas.txt",
    "hugo-burgraves.txt",
    "dumas-antony.txt",
    "dumas-tour-de-nesle.txt",
    "dumas-henri-iii.txt",
    "dumas-kean.txt",
    "scribe-bertrand-et-raton.txt",
    "scribe-verre-d-eau.txt",
    "labiche-chapeau-de-paille.txt",
    "labiche-martin-poudre-aux-yeux.txt",
]

DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]", re.IGNORECASE)

def main():
    wins = []
    for name in DRAMA:
        t = open(os.path.join(CORPUS, name), encoding="utf-8",
                 errors="replace").read()
        for m in DEM_REINF.finditer(t):
            wins.append({"file": name, "off": m.start(),
                         "dem": m.group(1).lower(),
                         "ctx": t[m.start():m.start() + 500]})
    assert len(wins) == 41, f"expected 41 dem-comma hits, got {len(wins)}"
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "reinforced-head-topology-drama_windows.json")
    json.dump(wins, open(out, "w"), ensure_ascii=False, indent=1)
    print(f"{len(wins)} windows -> {out}")

if __name__ == "__main__":
    main()
