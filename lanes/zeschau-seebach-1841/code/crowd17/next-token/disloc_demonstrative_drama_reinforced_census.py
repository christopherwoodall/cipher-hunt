#!/usr/bin/env python3
r"""Census for battery disloc-demonstrative-drama-reinforced.

Target: extend the reinforced-head census (battery-disloc-demonstrative-
reinforced, null 2026-10-09) to the ingested drama corpus: genuine
dislocated REINFORCED demonstrative head (celui-la, ceux-la, celle-la,
celles-la, celui-ci, ceux-ci, celle-ci, celles-ci) + bare exclamatory
infinitive ("celui-la, voler !") in 19th-century French drama.

Search patterns (verbatim, same taxonomy as
disloc_demonstrative_reinforced_census.py):
  P1 (dislocation): r"DEM_REINF\s*[,;:]" where DEM_REINF =
      ((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|
       ça[-\u2011\u2013 ]?(?:l[àa]|ci)) — case-insensitive, hyphen or space.
      - window = text from the demonstrative through the next [!?.]
        (inclusive), capped at 180 chars.
  P2 (exclamatory filter): the window must contain "!" before its end.
  P3 (infinitive candidate): r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b"
      on the window text; candidates are printed for MANUAL classification
      (regex cannot separate -er infinitives from nouns/adjectives in -er).

Corpus: the drama ingest at code/side-period/corpus/ (per the gate note in
the queue: 11 files ingested). Hernani is present in TWO editions
(hugo-hernani-1870.txt, Jenkins 1870 archive.org OCR; hugo-hernani.txt,
Hetzel 1889 wikisource) — the queue note and PROVENANCE.md require ONE
edition per play, so hugo-hernani.txt is EXCLUDED (kept: the
hugo-hernani-1870.txt gate-ingest file used by the sibling batteries).
Census runs on 10 unique plays.

Output: JSON list of candidate windows; human classification happens in
the battery report. Files named, sizes in characters, patterns exact.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
DRAMADIR = os.path.join(LANE, "code/side-period/corpus")
# 10 unique plays: all drama ingest files except the duplicate Hernani
# edition (hugo-hernani.txt — Hetzel 1889; hugo-hernani-1870.txt is the
# gate-ingest edition and stays).
EXCLUDE = {"hugo-hernani.txt"}
FILES = [
    "hugo-hernani-1870.txt",      # Victor Hugo, Hernani (Jenkins 1870)
    "hugo-burgraves.txt",         # Victor Hugo, Les Burgraves
    "hugo-ruy-blas.txt",          # Victor Hugo, Ruy Blas (1839 ed.)
    "dumas-mariage-louis-xv-1841.txt",  # Dumas père, Un mariage sous Louis XV
    "dumas-antony.txt",           # Dumas père, Antony
    "dumas-henri-iii.txt",        # Dumas père, Henri III
    "dumas-kean.txt",             # Dumas père, Kean
    "dumas-tour-de-nesle.txt",    # Dumas père, La Tour de Nesle
    "scribe-bertrand-et-raton.txt",    # Eugène Scribe, Bertrand et Raton
    "scribe-verre-d-eau.txt",          # Eugène Scribe, Le Verre d'eau (éd. 1861)
    "labiche-chapeau-de-paille.txt",   # Labiche & Marc-Michel, Chapeau de paille
    "labiche-martin-poudre-aux-yeux.txt",  # Labiche & É. Martin, Poudre aux yeux
    "vigny-chatterton-1835.txt",  # Alfred de Vigny, Chatterton
    "musset-comedies-proverbes-1850.txt",  # Musset, Comédies et proverbes (10 plays)
]
# Reinforced demonstrative heads: celui-la, ceux-la, celle-la, celles-la,
# celui-ci, ceux-ci, celle-ci, celles-ci, ca-la, ca-ci — hyphen or space,
# case-insensitive (same taxonomy as the parent census).
DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]", re.IGNORECASE)
INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)

def windows(text):
    out = []
    for m in DEM_REINF.finditer(text):
        seg = text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        if "!" not in win:
            continue
        out.append({"dem": m.group(1).lower(), "window": win,
                    "inf_hits": sorted({w.group(0).lower()
                                        for w in INF.finditer(win)})})
    return out

def main():
    files, cands = [], []
    total = 0
    on_disk = {f for f in os.listdir(DRAMADIR) if f.endswith(".txt")}
    missing = [f for f in FILES if f not in on_disk]
    if missing:
        raise SystemExit("GATE FAIL: missing drama files: " + ", ".join(missing))
    assert "hugo-hernani.txt" in on_disk, \
        "GATE FAIL: expected duplicate Hernani edition absent"
    for f in FILES:
        p = os.path.join(DRAMADIR, f)
        text = open(p, encoding="utf-8", errors="replace").read()
        total += len(text)
        n_dem = len(DEM_REINF.findall(text))
        c = windows(text)
        for w in c:
            w["file"] = f
            cands.append(w)
        print(f"{f}: {len(text)} chars, {n_dem} dem-comma hits, "
              f"{len(c)} exclamatory candidates")
        files.append({"file": f, "chars": len(text),
                      "dem_comma_hits": n_dem,
                      "excl_candidates": len(c)})
    print(f"TOTAL: {len(files)} unique plays, {total} chars, "
          f"{sum(f['dem_comma_hits'] for f in files)} dem-comma hits, "
          f"{len(cands)} exclamatory candidates")
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "disloc-demonstrative-drama-reinforced_census.json")
    json.dump({"files": files, "total_chars": total,
               "candidates": cands,
               "note": "hugo-hernani.txt (Hetzel 1889) excluded: duplicate "
                       "Hernani edition; ONE edition per play per queue gate"},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)

if __name__ == "__main__":
    main()
