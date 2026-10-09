#!/usr/bin/env python3
r"""Census for battery disloc-demonstrative-inf.

Target: genuine dislocated demonstrative (cela/ceci/ca) + bare exclamatory
infinitive ("cela, voler !") in the wider 19th-century French register.

Search patterns (exact, verbatim):
  P1 (dislocation): r"DEM\s*[,;:]" where DEM = cela|ceci|ca|cel[àa]|cec[iy]
      (case-insensitive)
      - window = text from the demonstrative through the next [!?.] (inclusive),
        capped at 180 chars.
  P2 (exclamatory filter): the window must contain "!" before its end.
  P3 (infinitive candidate): r"\b[a-z\xe0\xe2\xe4\xe7\xe8\xe9\xea\xeb\xee\xef\xf4\xf6\xf9\xfb\xfc']{2,}(er|ir|re|oir)\b"
      on the window text; candidates are printed for MANUAL classification
      (regex cannot separate -er infinitives from nouns/adjectives in -er).

Corpus:
  - 1841-register lane corpus: code/side-period/corpus/*.txt (French files only;
    German files excluded and named in the report).
  - Wider 19th-century register: data/gutenberg-17489-miserables1.txt (1862),
    data/gutenberg-30513-tocqueville-t1.txt (1835),
    data/gutenberg-30514-tocqueville-t2.txt (1840).

Output: JSON list of candidate windows; human classification happens in the
battery report. Files named, sizes in characters, patterns exact.
"""
import json, re, sys, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS1841 = os.path.join(LANE, "code/side-period/corpus")
GERMAN = {
    "adb-zeschau-heinrich-anton-von.txt",
} | {f"allgemeine-zeitung-augsburg-1841-01-{d:02d}.txt" for d in range(11, 26)}
WIDER = [
    os.path.join(LANE, "data/gutenberg-17489-miserables1.txt"),
    os.path.join(LANE, "data/gutenberg-30513-tocqueville-t1.txt"),
    os.path.join(LANE, "data/gutenberg-30514-tocqueville-t2.txt"),
]
DEM = re.compile(r"\b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]", re.IGNORECASE)
INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)

def windows(text):
    out = []
    for m in DEM.finditer(text):
        seg = text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        if "!" not in win:
            continue
        infs = [w for w in set(INF.findall(win)) ]
        out.append({"dem": m.group(1).lower(), "window": win,
                    "inf_hits": sorted({w[0] + w[1] for w in INF.finditer(win)})})
    return out

def census(paths, label):
    total_chars = 0
    files = []
    cands = []
    for p in sorted(paths):
        name = os.path.basename(p)
        t = open(p, encoding="utf-8", errors="replace").read()
        total_chars += len(t)
        n_dem = len(DEM.findall(t))
        c = windows(t)
        files.append({"file": name, "chars": len(t),
                      "dem_comma_hits": n_dem, "excl_candidates": len(c)})
        for w in c:
            w["file"] = name
            cands.append(w)
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"{sum(f['dem_comma_hits'] for f in files)} dem-comma hits, "
          f"{len(cands)} exclamatory candidates")
    return {"files": files, "total_chars": total_chars,
            "candidates": cands}

if __name__ == "__main__":
    c1841 = [os.path.join(CORPUS1841, f) for f in os.listdir(CORPUS1841)
             if f.endswith(".txt") and f not in GERMAN]
    res = {"census_1841_register": census(c1841, "1841 register"),
           "census_wider_19c": census(WIDER, "wider 19c")}
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "disloc-demonstrative-inf_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
