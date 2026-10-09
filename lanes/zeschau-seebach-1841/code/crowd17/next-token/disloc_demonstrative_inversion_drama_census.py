#!/usr/bin/env python3
r"""Census for battery disloc-demonstrative-inversion-drama.

Target: POSTPOSED demonstratives ("[inf] !, cela/ceci/ça" word order) in the
ingested drama corpus (14 plays, one edition per play; same PLAYS list as
disloc_demonstrative_drama_dialogue_census.py). This is the inversion test of
the fenced pairing "dislocated demonstrative + bare exclamatory infinitive":
if the tonic head licenses the pairing from post-topic position, the bar
construction would show up in the inverted order.

Plays mark dialogue with speaker headers, not quote marks, so the census
runs over the full play text (sibling drama-dialogue battery's method):
every candidate is classified by hand with its dialogue-vs-non-dialogue
status. A confirmed zero over the full text implies a confirmed zero in
dialogue; no genuine hit can hide in a preface.

Inversion patterns (verbatim from disloc_demonstrative_inversion_census.py):
  INF:      \b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b
  DEM_POST: \b(cela|ceci|ça|ca|cel[àa]|cec[iy])\b
  For each INF match: window = INF start .. INF end + 100 chars.
  Candidate iff a DEM_POST match starts AFTER the infinitive inside the
  window AND "!" occurs between the INF start and 20 chars past the DEM
  match end. Covers: "Voler !, cela" / "Voler, cela !" / "Voler ! cela".

Output: disloc-demonstrative-inversion-drama_census.json with per-file sizes,
candidate counts, and every candidate window (+-120 char context) for manual
classification (taxonomy: finite clauses, vocatives, OCR noise, noun
false-INF excluded with cause).
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
PLAYS = [
    "dumas-antony.txt",
    "dumas-henri-iii.txt",
    "dumas-kean.txt",
    "dumas-mariage-louis-xv-1841.txt",
    "dumas-tour-de-nesle.txt",
    "hugo-burgraves.txt",
    "hugo-hernani.txt",          # Hetzel 1889 wikisource ed.
    # "hugo-hernani-1870.txt"    # EXCLUDED: second Hernani edition
    "hugo-ruy-blas.txt",
    "labiche-chapeau-de-paille.txt",
    "labiche-martin-poudre-aux-yeux.txt",
    "musset-comedies-proverbes-1850.txt",
    "scribe-bertrand-et-raton.txt",
    "scribe-verre-d-eau.txt",
    "vigny-chatterton-1835.txt",
]
FILES = [os.path.join(LANE, "code/side-period/corpus", f) for f in PLAYS]
OUT = os.path.join(LANE, "code/crowd17/next-token",
                   "disloc-demonstrative-inversion-drama_census.json")

INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)
DEM_POST = re.compile(r"\b(cela|ceci|ça|ca|cel[àa]|cec[iy])\b", re.IGNORECASE)


def windows(text, file_name):
    out = []
    for im in INF.finditer(text):
        wend = im.end() + 100
        win = text[im.start():wend]
        for dm in DEM_POST.finditer(win):
            if dm.start() < (im.end() - im.start()):
                continue  # demonstrative precedes the infinitive: not inversion
            bang_zone = win[:dm.end() + 20]
            if "!" not in bang_zone:
                continue  # exclamatory link not local to the construction
            a = max(0, im.start() - 120)
            b = min(len(text), im.end() + 220)
            out.append({
                "file": file_name,
                "inf": im.group(0).lower(),
                "inf_abs_offset": im.start(),
                "dem": dm.group(1).lower(),
                "window": text[a:b].replace("\n", " "),
            })
    return out


def main():
    files, cands, seen = [], [], set()
    for p in FILES:
        name = os.path.basename(p)
        text = open(p, encoding="utf-8", errors="replace").read()
        n_new = 0
        for w in windows(text, name):
            key = (name, w["inf_abs_offset"])
            if key in seen:
                continue
            seen.add(key)
            cands.append(w)
            n_new += 1
        print(f"{name}: {len(text)} chars, {n_new} postposed-dem candidates")
        files.append({"file": name, "chars": len(text),
                      "postposed_dem_candidates": n_new})
    json.dump({"files": files, "candidates": cands}, open(OUT, "w"),
              ensure_ascii=False, indent=1)
    print("wrote", OUT, "| total unique candidates:", len(cands))


if __name__ == "__main__":
    main()
