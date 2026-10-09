#!/usr/bin/env python3
"""Boosted census for ordinal-ellipsis-final particle discrimination.

Frame: a clause-initial particle (mais/or/donc/cependant) whose immediately
preceding clause ends with a nominalized ordinal ("la première", "le second",
"sa première", "les derniers", "premier" variants incl. unaccented spellings,
possessive+ordinal, "une première", etc.).

Goal: power the 5-0-0-0 mais-exclusive observation from
battery-particle-20-value-rivals to n>=20 mais with rivals at zero, or abandon
the frame as a discriminator.
"""
import json, os, re, sys

CORP = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus")
OUT = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd17/next-token/ordinal_particle_boost.json")

PARTICLES = ["mais", "or", "donc", "cependant"]

def strip_acc(s):
    return (s.replace("é","e").replace("è","e").replace("ê","e").replace("ë","e")
             .replace("à","a").replace("â","a").replace("î","i").replace("ï","i")
             .replace("ô","o").replace("ù","u").replace("û","u").replace("ç","c"))

# ordinal stems (accent-insensitive matching done on stripped text)
ORD = (r"premi[eè]re?s?|premiers?|second(e?s)?|troisi[eè]me?s?|"
       r"quatri[eè]me?s?|cinqui[eè]me?s?|sixi[eè]me?s?|"
       r"derni[eè]re?s?|derniers?|ultimes?")

DET = (r"(?:l[ae]|les|un|une|des|sa|son|ses|ma|mon|mes|ta|ton|tes|"
       r"ce|cette|cet|ces|notre|votre|leur)")

ORDINAL_END = re.compile(r"\b" + DET + r"\s+(" + ORD + r")\s*$", re.I)

def clauses(text):
    parts = re.split(r"[.;:!?…]+|\n\s*\n", text)
    return [p.strip(" \t\"'«»'()") for p in parts if p.strip(" \t\"'«»'()")]

def first_word(cl):
    m = re.match(r"[\"'«»(\s]*([A-Za-zÀ-ÿ]+)", cl)
    return m.group(1) if m else ""

def ordinal_final(cl):
    return bool(ORDINAL_END.search(cl))

def ordinal_match_text(cl):
    m = ORDINAL_END.search(cl)
    return m.group(0) if m else ""

def census():
    rows = []
    files = sorted(f for f in os.listdir(CORP) if f.endswith(".txt"))
    for fn in files:
        text = open(os.path.join(CORP, fn), encoding="utf-8", errors="replace").read()
        cls = [c for c in clauses(text) if c]
        for i, cl in enumerate(cls):
            fw = strip_acc(first_word(cl)).lower()
            if fw in PARTICLES and i > 0:
                prev = cls[i-1]
                if ordinal_final(prev):
                    rows.append({
                        "file": fn, "particle": fw,
                        "ordinal_span": ordinal_match_text(prev),
                        "prev": prev[-200:],
                        "cur": cl[:180],
                    })
    agg = {p: {"n": 0} for p in PARTICLES}
    for r in rows:
        agg[r["particle"]]["n"] += 1
    json.dump({"agg": agg, "files": len(files), "rows": rows},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("files:", len(files))
    for p in PARTICLES:
        print(f"  {p}: {agg[p]['n']}")
    print("rows written:", len(rows), "->", OUT)

if __name__ == "__main__":
    census()
