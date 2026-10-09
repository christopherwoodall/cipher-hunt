#!/usr/bin/env python3
r"""Census for battery reinforced-pour-inf-diagnostic.

Follow-up #3 of the NULL disloc-demonstrative-reinforced (2026-10-09).
Parent census tested REINFORCED demonstrative heads + BARE exclamatory
infinitive and fenced the family (0/7 genuine). Its near-misses were
preposition-governed infinitives (pour/a/de). THIS battery tests the
governed shape: "celui-là, pour rire !" — reinforced head + governed
exclamatory infinitive.

Search patterns (exact, verbatim):
  P1 (dislocation): same DEM_REINF as disloc_demonstrative_reinforced_census.py:
      r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]" — case-insensitive.
      Window = text from the demonstrative through the next [!?.]
      (inclusive), capped at 180 chars.
  P2 (exclamatory filter): window must contain "!" before its end.
  P3 (governed-infinitive candidate): r"\b(pour|à|a|de|d['’])\s+(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b"
      applied to the window text AFTER the comma (case-insensitive):
      prep (pour / à / a / de / d') + up to two short tokens
      (clitics, articles, pronouns like m', l', en, y) + infinitive-shaped
      word. Candidates are printed for MANUAL classification (regex cannot
      separate -er infinitives from nouns/adjectives in -er; "a" is
      unaccented in some sources).

Corpus (identical to disloc-demonstrative-inf/-reinforced, 21 files,
27.66M chars):
  - 1841-register lane corpus: code/side-period/corpus/*.txt (French files
    only; German files excluded and named in the report).
  - Wider 19th-century register: data/gutenberg-17489-miserables1.txt (1862),
    data/gutenberg-30513-tocqueville-t1.txt (1835),
    data/gutenberg-30514-tocqueville-t2.txt (1840).

Output: JSON list of candidate windows with per-file sizes, hit counts;
human classification happens in the battery report.
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

DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]", re.IGNORECASE)

GOV_INF = re.compile(
    r"\b(pour|à|a|de|d['’])\s+"
    r"(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}"
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)

def windows(text):
    out = []
    for m in DEM_REINF.finditer(text):
        seg = text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        if "!" not in win:
            continue
        after_comma = win[m.end() - m.start():]
        gov_hits = [(g.group(1).lower(), g.group(0).lower())
                    for g in GOV_INF.finditer(after_comma)]
        if not gov_hits:
            continue
        out.append({"dem": m.group(1).lower(), "window": win,
                    "gov_inf_hits": sorted({h[0] + " + " + h[1] for h in gov_hits})})
    return out

def n_dem_total(files):
    return sum(f["dem_comma_hits"] for f in files)

def census(paths, label):
    total_chars = 0
    files, cands = [], []
    for p in sorted(paths):
        name = os.path.basename(p)
        t = open(p, encoding="utf-8", errors="replace").read()
        total_chars += len(t)
        n_dem = len(DEM_REINF.findall(t))
        c = windows(t)
        files.append({"file": name, "chars": len(t),
                      "dem_comma_hits": n_dem, "gov_inf_candidates": len(c)})
        for w in c:
            w["file"] = name
            cands.append(w)
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"{n_dem_total(files)} dem-comma hits, "
          f"{len(cands)} governed-inf exclamatory candidates")
    return {"files": files, "total_chars": total_chars, "candidates": cands}

if __name__ == "__main__":
    c1841 = [os.path.join(CORPUS1841, f) for f in os.listdir(CORPUS1841)
             if f.endswith(".txt") and f not in GERMAN]
    res = {"census_1841_register": census(c1841, "1841 register"),
           "census_wider_19c": census(WIDER, "wider 19c")}
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "reinforced-pour-inf-diagnostic_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
