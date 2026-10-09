#!/usr/bin/env python3
"""Census for battery disloc-demonstrative-epistolary-pausemark.

Target: the same bare-head pausemark census on the EPISTOLARY sub-corpus
(Nesselrode v7/v8/v9/v10, Talleyrand memoires v1, Guizot memoires
t1/t2/t3/t5-t6, Metternich papiere v4/v6, Pozzo-di-Borgo correspondance v1,
Levant correspondence 1841 p3) -- NOT the 1,847-pair stream, per target
charter. Bare demonstrative heads (cela/ceci/ca) only; reinforced family
has its own batteries. German files and drama texts excluded with cause
(register is French epistolary prose).

Parent: disloc-demonstrative-prose-pausemark-recall (NULL 2026-10-09:
156 dem+separator hits -> 38 with '!' -> 0 genuine in 27.66M chars
19th-century French prose). This battery's bar: ">=1 genuine
(cela/ceci/ça) + non-comma pause separator + bare exclamatory infinitive
re-opens the epistolary register; confirmed zero fences it".

Patterns (P1/P2/P3 copied VERBATIM from the parent prose pausemark
battery, which copied them from the drama pausemark battery):
  P1: \\b(cela|ceci|ca)\\s*(?:[!?\\u2026:;]|\\u2014+|--+|\\.{2,}) (bare demonstrative + non-comma separator)
  P2: window (dem..dem+70) must contain '!'
  P3: [a-zA-Z\u00c0-\u00ff-]+(?:er|ir|re|oir) infinitive-shaped word in window (hand-classified)
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS1841 = os.path.join(LANE, "code/side-period/corpus")
NT = os.path.join(LANE, "code/crowd17/next-token")

# Name-pinned epistolary sub-corpus (12 files), per target evidence field.
EPISTOLARY_FILES = [
    "nesselrode-v7.txt",
    "nesselrode-v8.txt",
    "nesselrode-v9.txt",
    "nesselrode-v10.txt",
    "talleyrand-memoires-v1.txt",
    "guizot-memoires-t1-gutenberg.txt",
    "guizot-memoires-t2-gutenberg.txt",
    "guizot-memoires-t3-gutenberg.txt",
    "guizot-memoires-t5-t6.txt",
    "metternich-papiere-v4.txt",
    "metternich-papiere-v6.txt",
    "pozzo-di-borgo-correspondance-v1.txt",
    "levant-correspondence-1841-p3.txt",
]

# P1/P2/P3 verbatim from the parent battery.
SEP = r"(?:[!?\u2026:;]|\u2014+|--+|\.{2,})"
DEM = re.compile(r"\b(cela|ceci|\u00e7a|ca)\s*" + SEP, re.IGNORECASE)
INF = re.compile(r"\b([A-Za-z\u00c0-\u00ff-]+(?:er|ir|re|oir))\b")
SENT_END = re.compile(r"[.?!]")


def find_inf_after(txt, pos, limit=70):
    seg = txt[pos:pos + limit]
    m = SENT_END.search(seg)
    if m:
        seg = seg[:m.start()]
    m = INF.search(seg)
    return (m.group(1), pos + m.start()) if m else None


def windows(text, fname):
    out = []
    for m in DEM.finditer(text):
        seg = text[m.start():m.start() + 70]
        if "!" not in seg:
            continue
        inf = find_inf_after(text, m.end())
        ctx_start = max(0, m.start() - 200)
        ctx = text[ctx_start:m.end() + 300].replace("\n", " / ")
        out.append({"file": fname, "offset": m.start(),
                    "dem": m.group(1).lower(),
                    "separator": m.group(0)[len(m.group(1)):].strip(),
                    "infinitive": inf[0] if inf else None,
                    "infinitive_offset": inf[1] if inf else None,
                    "context": ctx})
    return out


def main():
    paths = [os.path.join(CORPUS1841, f) for f in EPISTOLARY_FILES]
    missing = [p for p in paths if not os.path.exists(p)]
    assert not missing, "GATE FAIL: epistolary corpus files missing: " + ", ".join(missing)

    out = {"files": {}, "candidates": [], "by_file_counts": {}}
    total_chars = 0
    for p, fn in zip(paths, EPISTOLARY_FILES):
        txt = open(p, encoding="utf-8", errors="replace").read()
        total_chars += len(txt)
        hits = list(DEM.finditer(txt))
        cands = windows(txt, fn)
        out["files"][fn] = {"chars": len(txt),
                            "dem_sep_hits": len(hits),
                            "candidates_with_excl": len(cands)}
        out["candidates"].extend(cands)
    out["total_chars"] = total_chars
    out["total_dem_sep_hits"] = sum(v["dem_sep_hits"] for v in out["files"].values())
    out["total_candidates"] = len(out["candidates"])
    dest = os.path.join(NT, "disloc-demonstrative-epistolary-pausemark_census.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(json.dumps({"total_chars": total_chars,
                      "total_dem_sep_hits": out["total_dem_sep_hits"],
                      "total_candidates": out["total_candidates"],
                      "dest": dest}, indent=1))


if __name__ == "__main__":
    main()
