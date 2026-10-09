#!/usr/bin/env python3
r"""Census for battery disloc-comedy-bare-heads-extension.

Runs the bare-demonstrative-head P1/P2/P3 taxonomy (copied verbatim from
disloc_demonstrative_drama_reissue_census.py) over the 6 newly ingested
Scribe/Labiche comedy files. The comedy register was never covered for the
bare-head (ce/cela/ça) inventory.

Search patterns (verbatim, same as the reissue battery):
  P1 (dislocation): r"\b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]" (case-insensitive)
      window = text from the demonstrative through the next [!?.] (inclusive),
      capped at 180 chars.
  P2 (exclamatory filter): the window must contain "!" before its end.
  P3 (infinitive candidate): r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b"
      on the window text; candidates printed for MANUAL classification.

Pass B (bare "ce", per the target claim "(ce/cela/ça)"):
  B1: r"\bce\b\s*[,;:]" (case-insensitive); same windowing + P2 + P3.
  "ce" alone is excluded from the standard DEM because it is overwhelmingly
  the determiner/clitic; Pass B runs it separately so genuine dislocated
  "ce, [inf] !" would still surface (manual classification decides).

Cross-check (from the ingest battery): STRICT and LOOSE regexes over the
6 comedy files for the cela/ceci/ça shape.

Corpus: the 6 comedy-extension files in code/side-period/corpus/.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

COMEDY_FILES = [
    "labiche-29-degres-ombre.txt",
    "labiche-affaire-rue-lourcine.txt",
    "labiche-la-cagnotte.txt",
    "labiche-voyage-perrichon.txt",
    "scribe-le-lorgnon.txt",
    "scribe-le-savant.txt",
]

DEM = re.compile(r"\b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]", re.IGNORECASE)
CE = re.compile(r"\bce\b\s*[,;:]", re.IGNORECASE)
INF = re.compile(r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)

STRICT = re.compile(
    r"\b(cela|ceci|ça)\b\s*[,;:…]\s*(?:\S+\s+)?[a-zàâäçéèêëîïôöùûü']{2,}"
    r"(er|ir|re)\s*!", re.IGNORECASE)
LOOSE = re.compile(
    r"\b(cela|ceci|ça)\b\s*.{0,35}?[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re)\b"
    r".{0,35}!", re.IGNORECASE)


def p123_windows(text, dem_re):
    out = []
    for m in dem_re.finditer(text):
        seg = text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        if "!" not in win:
            continue
        out.append({"dem": m.group(1).lower(), "start": m.start(),
                    "window": win,
                    "inf_hits": sorted({w.group(0).lower()
                                        for w in INF.finditer(win)})})
    return out


def cross_windows(text):
    strict = [{"window": m.group(0), "start": m.start()} for m in
              STRICT.finditer(text)]
    loose = [{"window": m.group(0)[:80].replace("\n", " "),
              "context": text[max(0, m.start() - 90):m.end() + 90]
              .replace("\n", " "),
              "start": m.start()} for m in LOOSE.finditer(text)]
    return strict, loose


def census():
    total = 0
    files = []
    cands = []
    cross = []
    for name in sorted(COMEDY_FILES):
        p = os.path.join(CORPUS, name)
        assert os.path.exists(p), f"missing corpus file: {p}"
        t = open(p, encoding="utf-8", errors="replace").read()
        total += len(t)
        wa = p123_windows(t, DEM)
        wb = p123_windows(t, CE)
        strict, loose = cross_windows(t)
        files.append({"file": name, "chars": len(t),
                      "dem_comma_hits": len(DEM.findall(t)),
                      "ce_comma_hits": len(CE.findall(t)),
                      "excl_candidates": len(wa) + len(wb),
                      "strict_hits": len(strict),
                      "loose_hits": len(loose)})
        for c in wa:
            c["file"] = name
            c["pass"] = "A"
            cands.append(c)
        for c in wb:
            c["file"] = name
            c["pass"] = "B"
            cands.append(c)
        for c in loose:
            c["file"] = name
            cross.append(c)
    print(f"=== comedy bare-heads: {len(files)} files, {total} chars, "
          f"{sum(f['dem_comma_hits'] for f in files)} dem-comma hits, "
          f"{sum(f['ce_comma_hits'] for f in files)} ce-comma hits, "
          f"{len(cands)} excl candidates, "
          f"{sum(f['strict_hits'] for f in files)} strict, "
          f"{sum(f['loose_hits'] for f in files)} loose")
    return {"files": files, "total_chars": total,
            "candidates": cands, "loose_cross_hits": cross}


if __name__ == "__main__":
    res = census()
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "disloc-comedy-bare-heads-extension_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
