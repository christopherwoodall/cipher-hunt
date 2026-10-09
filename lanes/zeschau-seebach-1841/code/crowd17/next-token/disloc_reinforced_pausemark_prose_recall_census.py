#!/usr/bin/env python3
r"""Census for battery disloc-reinforced-pausemark-prose-recall.

Target: dash/parenthesis pause-mark variant of the governed-exclamatory
search on the 21-file prose corpus. The parent battery
(disloc-governed-excl-prose-recall) ran P1 with pause marks [,;:]
(231 reinforced-head-comma hits -> 4 candidates -> 0 genuine in
27,657,940 chars). This battery asks whether the zero is a separator
artifact: pause marks em-dash/en-dash/hyphen/ellipsis/open-paren.

Bar (pre-registered): "0 genuine confirms the prose zero is not a separator
artifact; any genuine re-opens the shape arm".

Patterns: P1 = DEM_REINF followed by a dash-family / ellipsis / open-paren
pause mark; P2/P3/P3b = VERBATIM copies from
disloc_governed_excl_prose_recall_census.py (P2: window must contain "!";
P3 strict "\b(?:pour|de|d'|d\u2019|\u00e0)\s+[infinitive-shaped]"; P3b
clitic-tolerant re-run with up to 2 intervening short words).

Window = text from the demonstrative through the next [!?.] (inclusive),
capped at 180 chars — same as the parent.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS1841 = os.path.join(LANE, "code/side-period/corpus")
NT = os.path.join(LANE, "code/crowd17/next-token")

_parent = json.load(open(os.path.join(NT, "disloc-demonstrative-reinforced_census.json")))
PARENT_FILES = sorted(x["file"] for x in _parent["census_1841_register"]["files"])
PARENT_TOTAL = _parent["census_1841_register"]["total_chars"]
WIDER_PARENT = _parent["census_wider_19c"]
WIDER_FILES = sorted(x["file"] for x in WIDER_PARENT["files"])
WIDER_TOTAL = WIDER_PARENT["total_chars"]

DEM = (r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[\u00e0a]|ci)|"
       r"\u00e7a[-\u2011\u2013 ]?(?:l[\u00e0a]|ci))")
# dash family (em/en/hyphen), ellipsis (3 dots or single ellipsis char),
# open parenthesis. Comma/semicolon/colon deliberately EXCLUDED: the parent
# battery already covers them; this battery is the separator-artifact test.
PM_RE = re.compile(DEM + r"\s*(?:\u2014|\u2013|-|\.\.\.|\u2026|\()\s*",
                   re.IGNORECASE)
GOV_INF = re.compile(
    r"\b(?:pour|de|d'|d\u2019|\u00e0)\s+"
    r"[a-z\u00e0\u00e2\u00e4\u00e7\u00e8\u00e9\u00ea\u00eb\u00ee\u00ef\u00f4\u00f6\u00f9\u00fb\u00fc']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)
GOV_INF_CLITIC = re.compile(
    r"\b(?:pour|de|d'|d\u2019|\u00e0)\s+"
    r"(?:[a-z\u00e0\u00e2\u00e4\u00e7\u00e8\u00e9\u00ea\u00eb\u00ee\u00ef\u00f4\u00f6\u00f9\u00fb\u00fc']{1,5}\s+){0,2}"
    r"[a-z\u00e0\u00e2\u00e4\u00e7\u00e8\u00e9\u00ea\u00eb\u00ee\u00ef\u00f4\u00f6\u00f9\u00fb\u00fc']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)


def windows(text, fname):
    out = []
    for m in PM_RE.finditer(text):
        seg = text[m.start():m.start() + 180]
        end = re.search(r"[!?.]", seg)
        win = seg[:end.end()] if end else seg
        if "!" not in win:
            continue
        g = sorted({w.group(0).lower() for w in GOV_INF.finditer(win)})
        g2 = sorted({w.group(0).lower() for w in GOV_INF_CLITIC.finditer(win)})
        if not g and not g2:
            continue
        ctx_start = max(0, m.start() - 300)
        ctx = text[ctx_start:m.start() + 380].replace("\n", "/")
        out.append({"file": fname, "offset": m.start(),
                    "dem": m.group(1).lower(), "sep": m.group(0)[len(m.group(1)):],
                    "window": win,
                    "gov_inf_strict": g, "gov_inf_clitic": g2,
                    "context": ctx})
    return out


def main():
    c1841 = [os.path.join(CORPUS1841, f) for f in PARENT_FILES]
    missing = [p for p in c1841 if not os.path.exists(p)]
    assert not missing, "GATE FAIL: parent corpus files missing: " + ", ".join(missing)
    cwider = [os.path.join(LANE, p) for p in
              ["data/gutenberg-17489-miserables1.txt",
               "data/gutenberg-30513-tocqueville-t1.txt",
               "data/gutenberg-30514-tocqueville-t2.txt"]]
    missing = [p for p in cwider if not os.path.exists(p)]
    assert not missing, "GATE FAIL: wider files missing: " + ", ".join(missing)
    got = sum(len(open(p, encoding="utf-8", errors="replace").read()) for p in c1841)
    assert got == PARENT_TOTAL, f"corpus drift (1841): {got} != {PARENT_TOTAL}"
    gotw = sum(len(open(p, encoding="utf-8", errors="replace").read()) for p in cwider)
    assert gotw == WIDER_TOTAL, f"corpus drift (wider): {gotw} != {WIDER_TOTAL}"
    print(f"corpus identity asserted: 1841 {got} chars == parent, wider {gotw} chars == parent")

    files, cands, total, nhits = [], [], 0, 0
    for p in c1841 + cwider:
        fname = os.path.basename(p)
        text = open(p, encoding="utf-8", errors="replace").read()
        total += len(text)
        n_pm = len(PM_RE.findall(text))
        nhits += n_pm
        c = windows(text, fname)
        cands.extend(c)
        files.append({"file": fname, "chars": len(text),
                      "dem_pausemark_hits": n_pm,
                      "governed_excl_candidates": len(c)})
        print(f"{fname}: {len(text)} chars, {n_pm} dem-pausemark hits, "
              f"{len(c)} governed-excl candidates")

    json.dump({"total_chars": total, "files": files,
               "total_dem_pausemark_hits": nhits,
               "total_candidates": len(cands),
               "note": "P1 = dash-family/ellipsis/open-paren pause marks after "
                       "reinforced demonstrative head (comma/semicolon/colon "
                       "deliberately excluded — parent battery covers them). "
                       "P2/P3/P3b verbatim from the parent battery.",
               "candidates": cands},
              open(os.path.join(NT, "disloc-reinforced-pausemark-prose-recall_census.json"),
                   "w"), ensure_ascii=False, indent=1)
    print(f"TOTAL: {total} chars, {nhits} dem-pausemark hits, {len(cands)} candidates")


if __name__ == "__main__":
    main()
