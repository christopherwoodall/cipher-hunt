#!/usr/bin/env python3
r"""Census for battery disloc-demonstrative-reinforced.

Target: genuine dislocated REINFORCED demonstrative head (celui-là, ceux-là,
ça-là, celle-là, celles-là, celui-ci, ceux-ci, celle-ci, celles-ci) + bare
exclamatory infinitive ("celui-là, voler !") in the 27.66M-char 19th-century
French corpus used by battery disloc-demonstrative-inf.

Search patterns (exact, verbatim):
  P1 (dislocation): r"DEM_REINF\s*[,;:]" where DEM_REINF =
      celui|ceux|celle|celles followed by [- ]?(là|ci), OR ça followed by
      [- ]?(là|ci) — case-insensitive, hyphen or space.
      - window = text from the demonstrative through the next [!?.]
        (inclusive), capped at 180 chars.
  P2 (exclamatory filter): the window must contain "!" before its end.
  P3 (infinitive candidate): r"\b[a-z\xe0\xe2\xe4\xe7\xe8\xe9\xea\xeb\xee\xef\xf4\xf6\xf9\xfb\xfc']{2,}(er|ir|re|oir)\b"
      on the window text; candidates are printed for MANUAL classification
      (regex cannot separate -er infinitives from nouns/adjectives in -er).

Corpus (identical to disloc-demonstrative-inf, 21 files, 27.66M chars):
  - 1841-register lane corpus: code/side-period/corpus/*.txt (French files
    only; German files excluded and named in the report).
  - Wider 19th-century register: data/gutenberg-17489-miserables1.txt (1862),
    data/gutenberg-30513-tocqueville-t1.txt (1835),
    data/gutenberg-30514-tocqueville-t2.txt (1840).

Output: JSON list of candidate windows; human classification happens in the
battery report. Files named, sizes in characters, patterns exact.
"""
import json, re, os

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
# Reinforced demonstrative heads: celui-là, ceux-là, celle-là, celles-là,
# celui-ci, ceux-ci, celle-ci, celles-ci, ça-là, ça-ci — hyphen or space,
# case-insensitive.
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

def census(paths, label):
    total_chars = 0
    files = []
    cands = []
    for p in sorted(paths):
        name = os.path.basename(p)
        t = open(p, encoding="utf-8", errors="replace").read()
        total_chars += len(t)
        n_dem = len(DEM_REINF.findall(t))
        c = windows(t)
        files.append({"file": name, "chars": len(t),
                      "dem_comma_hits": n_dem, "excl_candidates": len(c)})
        for w in c:
            w["file"] = name
            cands.append(w)
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"{n_dem_total(files)} dem-comma hits, "
          f"{len(cands)} exclamatory candidates")
    return {"files": files, "total_chars": total_chars,
            "candidates": cands}

def n_dem_total(files):
    return sum(f["dem_comma_hits"] for f in files)

if __name__ == "__main__":
    c1841 = [os.path.join(CORPUS1841, f) for f in os.listdir(CORPUS1841)
             if f.endswith(".txt") and f not in GERMAN]
    res = {"census_1841_register": census(c1841, "1841 register"),
           "census_wider_19c": census(WIDER, "wider 19c")}
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "disloc-demonstrative-reinforced_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
