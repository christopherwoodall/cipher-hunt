#!/usr/bin/env python3
r"""Census for battery disloc-reinforced-comedy-extension.

Target: extend the reinforced-head census (disloc-demonstrative-drama-
reinforced, null 2026-10-09) to the NEW Scribe/Labiche comedy texts fetched
from fr.wikisource — the register where the parent battery found its only
infinitive-rich near-misses (Scribe, Le Verre d'eau).

Search patterns (verbatim, same taxonomy as
disloc_demonstrative_drama_reinforced_census.py):
  P1 (dislocation): r"DEM_REINF\s*[,;:]" where DEM_REINF =
      ((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|
       ça[-\u2011\u2013 ]?(?:l[àa]|ci)) — case-insensitive, hyphen or space.
      - window = text from the demonstrative through the next [!?.]
        (inclusive), capped at 180 chars.
  P2 (exclamatory filter): the window must contain "!" before its end.
  P3 (infinitive candidate): r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b"
      on the window text; candidates are printed for MANUAL classification
      (regex cannot separate -er infinitives from nouns/adjectives in -er).

Corpus: the 6 new comedy files in code/side-period/corpus/ fetched 2026-10-09.
Output: JSON list of candidate windows; human classification in the report.
Files named, sizes in characters, patterns exact.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
DRAMADIR = os.path.join(LANE, "code/side-period/corpus")
FILES = [
    "scribe-le-savant.txt",            # Scribe, Le Savant (1832)
    "scribe-le-lorgnon.txt",           # Scribe, Le Lorgnon (1833)
    "labiche-voyage-perrichon.txt",    # Labiche & É. Martin, Perrichon (1860)
    "labiche-la-cagnotte.txt",         # Labiche & Delacour, La Cagnotte (1864)
    "labiche-29-degres-ombre.txt",     # Labiche, 29 degrés à l'ombre (1873)
    "labiche-affaire-rue-lourcine.txt",  # Labiche & al., rue de Lourcine (1857)
]
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
        raise SystemExit("GATE FAIL: missing comedy files: " + ", ".join(missing))
    for f in FILES:
        text = open(os.path.join(DRAMADIR, f), encoding="utf-8",
                    errors="replace").read()
        total += len(text)
        n_dem = len(DEM_REINF.findall(text))
        c = windows(text)
        for w in c:
            w["file"] = f
            cands.append(w)
        print(f"{f}: {len(text)} chars, {n_dem} dem-comma hits, "
              f"{len(c)} exclamatory candidates")
        files.append({"file": f, "chars": len(text),
                      "dem_comma_hits": n_dem, "excl_candidates": len(c)})
    print(f"TOTAL: {len(files)} new comedy texts, {total} chars, "
          f"{sum(f['dem_comma_hits'] for f in files)} dem-comma hits, "
          f"{len(cands)} exclamatory candidates")
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "disloc-reinforced-comedy-extension_census.json")
    json.dump({"files": files, "total_chars": total, "candidates": cands},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)

if __name__ == "__main__":
    main()
