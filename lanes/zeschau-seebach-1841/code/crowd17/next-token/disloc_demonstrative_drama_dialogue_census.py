#!/usr/bin/env python3
r"""Census for battery disloc-demonstrative-drama-dialogue.

Runs the dislocated-demonstrative + bare exclamatory infinitive census
on the ingested drama corpus PLAYS ONLY (14 files; one edition per play:
Hernani in the Hetzel 1889 wikisource edition `hugo-hernani.txt`; the
Jenkins 1870 edition `hugo-hernani-1870.txt` EXCLUDED).

Because plays mark dialogue with speaker headers (not quote marks), the
RDM D1-D3 quoted-span extractor (disloc_demonstrative_quoted_drama_census.py)
catches almost no play dialogue. So the census runs over the full play
text with the same P1-P3 patterns, and EVERY candidate is classified by
hand with its dialogue-vs-non-dialogue status (preface/title-page/cast-
list/stage-direction vs spoken speech). A confirmed zero over the full
text implies a confirmed zero in dialogue; no genuine hit can hide in a
preface.

Patterns (verbatim from disloc_demonstrative_census.py, P1-P3):
  P1: \b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]  case-insensitive.
      Window = demonstrative through next [!?.], capped at 180 chars.
  P2: window must contain "!" before its end.
  P3: \b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b in the window.

Controls:
  C1: cedilla-less "ca" + comma + "!" + infinitive-shaped word in dialogue.
  C2: loose pass — any cela|ceci|ça|ca where an infinitive-shaped word
      follows within 40 chars and "!" within 70 chars (catches shapes the
      comma rule misses).

Output: disloc-demonstrative-drama-dialogue_census.json with per-file
sizes, dem-comma hits, candidates with @offsets and +/-120-char context,
and control-pass hits.
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
                   "disloc-demonstrative-drama-dialogue_census.json")

DEM = re.compile(r"\b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]", re.IGNORECASE)
INF = re.compile(r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)
DEM_LOOSE = re.compile(r"\b(cela|ceci|ça|ca)\b", re.IGNORECASE)
CA_NOCED = re.compile(r"\bca\s*[,;:](?![a-zàâäçéèêëîïôöùûü])", re.IGNORECASE)

def window_of(text, m):
    seg = text[m.start():m.start() + 180]
    end = re.search(r"[!?.]", seg)
    return seg[: end.end()] if end else seg

def main():
    files, cands, controls = [], [], []
    for p in FILES:
        name = os.path.basename(p)
        text = open(p, encoding="utf-8", errors="replace").read()
        dem_hits = len(DEM.findall(text))
        # Pass A: P1/P2/P3 verbatim
        for m in DEM.finditer(text):
            win = window_of(text, m)
            if "!" not in win:
                continue
            cands.append({
                "pass": "A",
                "file": name,
                "offset": m.start(),
                "dem": m.group(1).lower(),
                "window": win,
                "inf_hits": sorted({w[0] + w[1]
                                    for w in INF.finditer(win)}),
                "context": text[max(0, m.start() - 120):
                                m.start() + len(win) + 120],
            })
        # Control C1: cedilla-less "ca" + comma + ! + infinitive
        for m in CA_NOCED.finditer(text):
            win = window_of(text, m)
            if "!" not in win:
                continue
            hits = sorted({w[0] + w[1] for w in INF.finditer(win)})
            if not hits:
                continue
            controls.append({
                "pass": "C1-ca-nocedilla",
                "file": name,
                "offset": m.start(),
                "window": win,
                "inf_hits": hits,
                "context": text[max(0, m.start() - 120):
                                m.start() + len(win) + 120],
            })
        # Control C2: loose — dem ... inf (<=40 chars) ... ! (<=70 chars)
        for m in DEM_LOOSE.finditer(text):
            seg = text[m.start():m.start() + 70]
            inf = INF.search(seg)
            if not inf or inf.start() > 40:
                continue
            tail = seg[inf.start():inf.start() + 60]
            if "!" not in tail:
                continue
            win = window_of(text, m)
            controls.append({
                "pass": "C2-loose",
                "file": name,
                "offset": m.start(),
                "dem": m.group(1).lower(),
                "window": win,
                "context": text[max(0, m.start() - 120):
                                m.start() + len(win) + 120],
            })
        pa = sum(1 for c in cands if c["file"] == name)
        print(f"{name}: {len(text)} chars, {dem_hits} dem-comma hits, "
              f"{pa} P1-P3 candidates")
        files.append({"file": name, "chars": len(text),
                      "dem_comma_hits": dem_hits, "passA_candidates": pa})
    json.dump({"files": files, "candidates": cands, "controls": controls},
              open(OUT, "w"), ensure_ascii=False, indent=1)
    print("wrote", OUT,
          f"| {len(cands)} pass-A candidates, {len(controls)} control hits")

if __name__ == "__main__":
    main()
