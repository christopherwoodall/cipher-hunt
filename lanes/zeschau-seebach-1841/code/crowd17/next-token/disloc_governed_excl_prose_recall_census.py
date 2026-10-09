#!/usr/bin/env python3
r"""Census for battery disloc-governed-excl-prose-recall.

Target: run the governed-exclamatory P3 search against the prose battery's
231 reinforced-head-comma hits (battery-disloc-demonstrative-reinforced,
2026-10-09: 206 hits in the 1841-register 18-file set + 25 in the wider
3-file set, 7 exclamatory candidates, 0 genuine).

Bar (pre-registered): ">=1 genuine governed exclamatory infinitive under a
reinforced head in prose re-opens the shape arm; confirmed zero hardens the
prose fence".

Patterns (same P1/P2 taxonomy as the prose parent census; P3 = the narrowed
governed-exclamatory search from disloc_reinforced_prep_inf_drama_census.py,
adapted to prose):
  P1 (dislocation): r"DEM_REINF\s*[,;:]" where DEM_REINF =
      ((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[\u00e0a]|ci)|
       \u00e7a[-\u2011\u2013 ]?(?:l[\u00e0a]|ci)) — case-insensitive.
      - window = text from the demonstrative through the next [!?.]
        (inclusive), capped at 180 chars.
  P2 (exclamatory filter): the window must contain "!" before its end.
  P3 (governed-infinitive candidate, strict):
      r"\b(?:pour|de|d'|d\u2019|\u00e0)\s+[a-z\u00e0\u00e2\u00e4\u00e7\u00e8\u00e9\u00ea\u00eb\u00ee\u00ef\u00f4\u00f6\u00f9\u00fb\u00fc']{2,}(er|ir|re|oir)\b"
      case-insensitive.
  P3b (clitic-tolerant re-run): up to 2 intervening short words between the
      preposition and the infinitive-shaped word.

Corpus gate: name-pinned to the parent battery's exact 18-file prose set
(parent total 25,670,258 chars, asserted at runtime) + the 3 wider files
(1,987,682 chars, asserted). Note: the dispatch charter says "18-file set"
but the claim's 231 hits span the parent battery's full 21-file corpus
(206 + 25); the bar is therefore run against the 21-file set with the
discrepancy recorded, not hidden. Nothing is rewritten: the 18-file
identity is still byte-asserted separately.

Output: JSON with candidates + manual-classification context. Human
classification happens in the battery report.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS1841 = os.path.join(LANE, "code/side-period/corpus")
NT = os.path.join(LANE, "code/crowd17/next-token")

# Pin to the parent battery's exact file set by name (drama ingest added
# ~15 files to this dir since the parent ran; pinning keeps byte identity).
_parent = json.load(open(os.path.join(NT, "disloc-demonstrative-reinforced_census.json")))
PARENT_FILES = sorted(x["file"] for x in _parent["census_1841_register"]["files"])
PARENT_TOTAL = _parent["census_1841_register"]["total_chars"]
WIDER_PARENT = _parent["census_wider_19c"]
WIDER_FILES = sorted(x["file"] for x in WIDER_PARENT["files"])
WIDER_TOTAL = WIDER_PARENT["total_chars"]

DEM_REINF = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]", re.IGNORECASE)
GOV_INF = re.compile(
    r"\b(?:pour|de|d'|d’|à)\s+"
    r"[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)
GOV_INF_CLITIC = re.compile(
    r"\b(?:pour|de|d'|d’|à)\s+"
    r"(?:[a-zàâäçéèêëîïôöùûü']{1,5}\s+){0,2}"
    r"[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)
CTRL = re.compile(
    r"\b(?:pour|de)\s+[a-zàâäçéèêëîïôöùûü']{2,}(?:er|ir|re|oir)\b[^!?.]{0,60}!",
    re.IGNORECASE)


def windows(text, fname):
    out = []
    for m in DEM_REINF.finditer(text):
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
                    "dem": m.group(1).lower(), "window": win,
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

    files, cands, ctrls, total, nhits = [], [], [], 0, 0
    for p in c1841 + cwider:
        fname = os.path.basename(p)
        text = open(p, encoding="utf-8", errors="replace").read()
        total += len(text)
        n_dem = len(DEM_REINF.findall(text))
        nhits += n_dem
        c = windows(text, fname)
        cands.extend(c)
        ctrl_hits = sorted({w.group(0).lower() for w in CTRL.finditer(text)})
        ctrls.append({"file": fname, "pour_de_inf_excl_hits": len(ctrl_hits),
                      "sample": ctrl_hits[:5]})
        print(f"{fname}: {len(text)} chars, {n_dem} dem-comma hits, "
              f"{len(c)} governed-excl candidates, "
              f"{len(ctrl_hits)} 'pour/de [inf] !' in register")
        files.append({"file": fname, "chars": len(text),
                      "dem_comma_hits": n_dem, "gov_excl_candidates": len(c)})
    print(f"TOTAL: {len(files)} files, {total} chars, {nhits} dem-comma hits, "
          f"{len(cands)} governed-exclamatory candidates")
    assert nhits == 231, f"hit-count drift: {nhits} != 231"
    out = os.path.join(NT, "disloc-governed-excl-prose-recall_census.json")
    json.dump({"files": files, "total_chars": total, "dem_comma_hits": nhits,
               "register_control": ctrls, "candidates": cands,
               "note": "byte-identical to battery-disloc-demonstrative-reinforced "
                       "corpus (21 files); charter said '18-file set' but the "
                       "claim's 231 hits span the full 21-file battery corpus"},
              open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)


if __name__ == "__main__":
    main()
