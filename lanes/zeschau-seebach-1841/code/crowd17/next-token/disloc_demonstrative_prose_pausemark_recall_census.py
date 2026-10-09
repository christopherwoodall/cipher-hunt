#!/usr/bin/env python3
"""Census for battery disloc-demonstrative-prose-pausemark-recall.

Target: extend the clause-initial demonstrative+non-comma-separator census
to the 27.66M-char prose corpus (bare demonstrative heads: cela/ceci/ca --
NOT the reinforced family, which has its own pausemark battery:
disloc-reinforced-pausemark-prose-recall).

Parent: disloc-demonstrative-drama-pausemark-recall (NULL 2026-10-09):
307 demonstrative+non-comma-separator hits -> 120 with '!' -> 0 genuine
in 14 drama plays. Its prose counterpart family: disloc-demonstrative-inf
(NULL: 447 dem-comma hits -> 15 candidates -> 0 genuine) and
disloc-demonstrative-prose-clause-initial (NULL: 447 -> 16 clause-initial
-> 0 genuine), both on this exact 21-file prose corpus.

Bar (pre-registered): "Extend the pausemark census to the 27.66M-char
prose corpus; >=1 genuine re-opens arm (a) in prose via non-comma
separators; confirmed zero confirms the prose zero is not a separator
artifact either".

Patterns (P1/P2/P3 copied VERBATIM from the drama pausemark battery):
  P1: \\b(cela|ceci|ca)\\s*(?:[!?\\u2026:;]|\\u2014+|--+|\\.{2,})  (non-comma separators)
  P2: window must contain '!' before its end
  P3: first infinitive-shaped word (er|ir|re|oir endings) within 70 chars
      before sentence end
Window = demonstrative through next [!?.], capped 70 chars for P3 context
(matching the drama battery's P2/P3 windows).
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS1841 = os.path.join(LANE, "code/side-period/corpus")
NT = os.path.join(LANE, "code/crowd17/next-token")

_parent = json.load(open(os.path.join(NT, "disloc-demonstrative-reinforced_census.json")))
PARENT_FILES = sorted(x["file"] for x in _parent["census_1841_register"]["files"])
PARENT_TOTAL = _parent["census_1841_register"]["total_chars"]
WIDER_PARENT = _parent["census_wider_19c"]
WIDER_TOTAL = WIDER_PARENT["total_chars"]
WIDER_FILES = ["data/gutenberg-17489-miserables1.txt",
               "data/gutenberg-30513-tocqueville-t1.txt",
               "data/gutenberg-30514-tocqueville-t2.txt"]

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
    c1841 = [os.path.join(CORPUS1841, f) for f in PARENT_FILES]
    missing = [p for p in c1841 if not os.path.exists(p)]
    assert not missing, "GATE FAIL: parent corpus files missing: " + ", ".join(missing)
    cwider = [os.path.join(LANE, p) for p in WIDER_FILES]
    missing2 = [p for p in cwider if not os.path.exists(p)]
    assert not missing2, "GATE FAIL: wider corpus files missing: " + ", ".join(missing2)
    def nchars(paths):
        return sum(len(open(p, encoding="utf-8", errors="replace").read()) for p in paths)
    t1841 = nchars(c1841)
    twider = nchars(cwider)
    assert t1841 == PARENT_TOTAL, f"GATE FAIL: 1841 corpus bytes {t1841} != parent {PARENT_TOTAL}"
    assert twider == WIDER_TOTAL, f"GATE FAIL: wider corpus bytes {twider} != parent {WIDER_TOTAL}"

    out = {"files": {}, "candidates": [], "by_file_counts": {}}
    total_chars = 0
    for p in c1841 + cwider:
        fn = os.path.relpath(p, LANE)
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
    dest = os.path.join(NT, "disloc-demonstrative-prose-pausemark-recall_census.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, indent=1)
    print(json.dumps({"total_chars": total_chars,
                      "total_dem_sep_hits": out["total_dem_sep_hits"],
                      "total_candidates": out["total_candidates"],
                      "dest": dest}, indent=1))


if __name__ == "__main__":
    main()
