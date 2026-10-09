#!/usr/bin/env python3
"""Pausemark-recall census: clause-initial demonstratives (cela/ceci/ca)
with NON-comma separators (!, --, ..., :, ;) in the drama corpus,
followed by a bare exclamatory infinitive.

Mirrors the drama-dialogue battery's P1-P3 logic, swapping the comma for
other pause marks. Output: candidates for hand classification.
"""
import json, os, re, sys

CORPUS = os.path.expanduser(
    "~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-period/corpus")
FILES = ["dumas-antony.txt", "dumas-henri-iii.txt", "dumas-kean.txt",
         "dumas-mariage-louis-xv-1841.txt", "dumas-tour-de-nesle.txt",
         "hugo-burgraves.txt", "hugo-hernani.txt", "hugo-ruy-blas.txt",
         "labiche-chapeau-de-paille.txt",
         "labiche-martin-poudre-aux-yeux.txt",
         "musset-comedies-proverbes-1850.txt",
         "scribe-bertrand-et-raton.txt", "scribe-verre-d-eau.txt",
         "vigny-chatterton-1835.txt"]

# demonstrative + non-comma separator
SEP = r"(?:[!?…:;]|—+|--+|\.{2,})"
DEM = re.compile(r"\b(cela|ceci|ça|ca)\s*" + SEP, re.IGNORECASE)
# infinitive-shaped word (bare): er/ir/re endings
INF = re.compile(r"\b([A-Za-zÀ-ÿ-]+(?:er|ir|re))\b")
SENT_END = re.compile(r"[.?!]")

def find_inf_after(txt, pos, limit=70):
    """First infinitive-shaped word within `limit` chars, before sentence end."""
    seg = txt[pos:pos + limit]
    m = SENT_END.search(seg)
    if m:
        seg = seg[:m.start()]
    m = INF.search(seg)
    return (m.group(1), pos + m.start()) if m else None

def main():
    out = {"files": {}, "candidates": []}
    total = 0
    for fn in FILES:
        path = os.path.join(CORPUS, fn)
        if not os.path.exists(path):
            out["files"][fn] = {"missing": True}
            continue
        txt = open(path, encoding="utf-8", errors="replace").read()
        hits = list(DEM.finditer(txt))
        total += len(hits)
        n_with_excl = 0
        for m in hits:
            win = txt[m.start():m.start() + 70]
            if "!" not in win:
                continue
            n_with_excl += 1
            inf = find_inf_after(txt, m.end())
            ctx = txt[max(0, m.start() - 150):m.end() + 250].replace("\n", " / ")
            out["candidates"].append({
                "file": fn, "offset": m.start(),
                "head": m.group(0).strip(),
                "infinitive": inf[0] if inf else None,
                "infinitive_offset": inf[1] if inf else None,
                "context": ctx,
            })
        out["files"][fn] = {"chars": len(txt), "dem_sep_hits": len(hits),
                            "with_excl_70": n_with_excl}
    out["total_dem_sep_hits"] = total
    out["total_candidates"] = len(out["candidates"])
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "disloc-demonstrative-drama-pausemark-recall_census.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(json.dumps({"total_dem_sep_hits": total,
                      "total_candidates": len(out["candidates"]),
                      "dest": dest}, indent=1))

if __name__ == "__main__":
    main()
