#!/usr/bin/env python3
r"""Census for battery disloc-demonstrative-drama-reissue.

Re-runs the disloc-demonstrative-drama bars against the ingested drama
corpus: >=1 genuine 'cela/ceci/ca, [bare inf] !' in 19th-century French drama
promotes arm (a); confirmed zero fences it at drama-register level.

Search patterns (exact, verbatim) — copied unchanged from
disloc_demonstrative_census.py (the disloc-demonstrative-inf battery):
  P1 (dislocation): r"\b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]" (case-insensitive)
      window = text from the demonstrative through the next [!?.] (inclusive),
      capped at 180 chars.
  P2 (exclamatory filter): the window must contain "!" before its end.
  P3 (infinitive candidate): r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b"
      on the window text; candidates are printed for MANUAL classification
      (regex cannot separate -er infinitives from nouns/adjectives in -er).

Corpus (drama files only, ONE edition per play):
  - 4 archive.org files from the disloc-demonstrative-drama-ingest Family 9
    batch (hugo-hernani-1870.txt, dumas-mariage-louis-xv-1841.txt,
    vigny-chatterton-1835.txt, musset-comedies-proverbes-1850.txt).
  - 10 wikisource files from the second drama ingest batch, MINUS
    hugo-hernani.txt (second Hernani edition; hugo-hernani-1870.txt kept —
    it is the edition the ingest battery's census used).
  All files: code/side-period/corpus/.

Second pass (cross-check, from the ingest battery's inline census):
  strict: (cela|ceci|ca) [,;:…] (<=1 short word) [infinitive-er/ir/re] !
  within 50 chars; loose fallback: (cela|ceci|ca) ...[infinitive] ...!
  within 35 chars; all loose hits printed with +/-90 chars context for
  manual classification.

Output: JSON list of candidate windows; human classification happens in the
battery report. Files named, sizes in characters, patterns exact.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

# Drama census set: one edition per play. hugo-hernani.txt excluded with
# cause (second Hernani edition; hugo-hernani-1870.txt retained).
DRAMA_FILES = [
    "dumas-antony.txt",
    "dumas-henri-iii.txt",
    "dumas-kean.txt",
    "dumas-mariage-louis-xv-1841.txt",
    "dumas-tour-de-nesle.txt",
    "hugo-burgraves.txt",
    "hugo-hernani-1870.txt",
    "hugo-ruy-blas.txt",
    "labiche-chapeau-de-paille.txt",
    "labiche-martin-poudre-aux-yeux.txt",
    "musset-comedies-proverbes-1850.txt",
    "scribe-bertrand-et-raton.txt",
    "scribe-verre-d-eau.txt",
    "vigny-chatterton-1835.txt",
]

DEM = re.compile(r"\b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]", re.IGNORECASE)
INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)

STRICT = re.compile(
    r"\b(cela|ceci|ça)\b\s*[,;:…]\s*(?:\S+\s+)?[a-zàâäçéèêëîïôöùûü']{2,}"
    r"(er|ir|re)\s*!", re.IGNORECASE)
LOOSE = re.compile(
    r"\b(cela|ceci|ça)\b\s*.{0,35}?[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re)\b"
    r".{0,35}!", re.IGNORECASE)

def p123_windows(text):
    out = []
    for m in DEM.finditer(text):
        seg = text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        if "!" not in win:
            continue
        out.append({"dem": m.group(1).lower(), "window": win,
                    "inf_hits": sorted({w.group(0).lower()
                                        for w in INF.finditer(win)})})
    return out

def cross_windows(text):
    out = []
    strict = []
    for m in STRICT.finditer(text):
        seg = text[m.start():m.start() + 50]
        if "!" in seg:
            strict.append({"strict": True, "window": m.group(0),
                           "context": text[max(0, m.start()-90):m.end()+90]
                           .replace("\n", " ")})
    loose = []
    for m in LOOSE.finditer(text):
        loose.append({"window": m.group(0)[:80].replace("\n", " "),
                      "context": text[max(0, m.start()-90):m.end()+90]
                      .replace("\n", " ")})
    return {"strict_hits": strict, "loose_hits": loose}

def census():
    total = 0
    files = []
    cands = []
    cross = []
    for name in sorted(DRAMA_FILES):
        p = os.path.join(CORPUS, name)
        assert os.path.exists(p), f"missing corpus file: {p}"
        t = open(p, encoding="utf-8", errors="replace").read()
        total += len(t)
        w = p123_windows(t)
        x = cross_windows(t)
        files.append({"file": name, "chars": len(t),
                      "dem_comma_hits": len(DEM.findall(t)),
                      "excl_candidates": len(w),
                      "strict_hits": len(x["strict_hits"]),
                      "loose_hits": len(x["loose_hits"])})
        for c in w:
            c["file"] = name
            cands.append(c)
        for c in x["loose_hits"]:
            c["file"] = name
            cross.append(c)
    print(f"=== drama reissue: {len(files)} files, {total} chars, "
          f"{sum(f['dem_comma_hits'] for f in files)} dem-comma hits, "
          f"{len(cands)} excl candidates, "
          f"{sum(f['strict_hits'] for f in files)} strict, "
          f"{sum(f['loose_hits'] for f in files)} loose")
    return {"files": files, "total_chars": total,
            "candidates": cands, "loose_cross_hits": cross}

if __name__ == "__main__":
    res = census()
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "disloc-demonstrative-drama-reissue_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
