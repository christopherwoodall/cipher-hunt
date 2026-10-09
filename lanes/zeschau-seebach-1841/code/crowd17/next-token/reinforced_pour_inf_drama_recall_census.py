#!/usr/bin/env python3
r"""Census for battery reinforced-pour-inf-drama-recall.

Closes the recall gap flagged in battery-reinforced-pour-inf-drama:
(1) 6/41 dem-comma windows had no sentence-end inside the 180-char cap;
(2) the separator class was comma-only (the report's recall note also
    covers dash/parenthesis pause marks after the head).

Pass A (baseline, verbatim prior settings): DEM_REINF with separators
[,;:] only, 180-char cap, "!" filter, GOV_INF on after-separator text.
Identifies the 41 hits and the 6 uncapped windows by identity.

Pass B (recall repair): separator class extended to [,;:\-—()]
(em-dash, hyphen, parentheses), 400-char window (400-char cap), same
"!" filter and GOV_INF. Every pass-A uncapped window is re-searched
individually and its resolution recorded.

Corpus: code/side-period/corpus/, 14 distinct plays, ONE Hernani
edition (hugo-hernani-1870.txt kept, hugo-hernani.txt excluded per
the supervisor's corpus note). The excluded edition is ALSO run with
pass-B settings so the edition choice cannot hide an attestation.

Candidates printed for MANUAL classification.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

DRAMA = [
    "dumas-mariage-louis-xv-1841.txt",
    "vigny-chatterton-1835.txt",
    "musset-comedies-proverbes-1850.txt",
    "hugo-hernani-1870.txt",             # one Hernani edition (per task brief)
    "hugo-ruy-blas.txt",
    "hugo-burgraves.txt",
    "dumas-antony.txt",
    "dumas-tour-de-nesle.txt",
    "dumas-henri-iii.txt",
    "dumas-kean.txt",
    "scribe-bertrand-et-raton.txt",
    "scribe-verre-d-eau.txt",
    "labiche-chapeau-de-paille.txt",
    "labiche-martin-poudre-aux-yeux.txt",
]
EXCLUDED_EDITION = "hugo-hernani.txt"     # second Hernani edition; run separately

DEM_A = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:]", re.IGNORECASE)

DEM_B = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:\-\u2013\u2014()]", re.IGNORECASE)

GOV_INF = re.compile(
    r"\b(pour|à|a|de|d['’])\s+"
    r"(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}"
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)


def windows(text, dem_re, cap):
    hits, cands = [], []
    for m in dem_re.finditer(text):
        seg = text[m.start():m.start() + cap]
        end = re.search(r"[!?.]", seg)
        win = seg[: end.end()] if end else seg
        uncapped = end is None
        hits.append({"offset": m.start(), "dem": m.group(1).lower(),
                     "sep": m.group(0)[len(m.group(1)):].strip(),
                     "uncapped": uncapped, "win_preview": win[:200]})
        if "!" not in win:
            continue
        after = win[m.end() - m.start():]
        gov_hits = sorted({(g.group(1).lower() + " + " + g.group(0).lower())
                           for g in GOV_INF.finditer(after)})
        if not gov_hits:
            continue
        cands.append({"offset": m.start(), "dem": m.group(1).lower(),
                      "sep": m.group(0)[len(m.group(1)):].strip(),
                      "window": win, "gov_inf_hits": gov_hits})
    return hits, cands


def census(paths, label):
    total_chars, files, all_hits, all_cands = 0, [], [], []
    for name in paths:
        p = os.path.join(CORPUS, name)
        t = open(p, encoding="utf-8", errors="replace").read()
        total_chars += len(t)
        ha, ca = windows(t, DEM_A, 180)
        hb, cb = windows(t, DEM_B, 400)
        uncapped_a = [h for h in ha if h["uncapped"]]
        files.append({"file": name, "chars": len(t),
                      "passA_hits": len(ha), "passA_uncapped": len(uncapped_a),
                      "passB_hits": len(hb),
                      "passA_candidates": len(ca), "passB_candidates": len(cb)})
        for h in ha:
            h.update({"file": name, "pass": "A"}); all_hits.append(h)
        for h in hb:
            h.update({"file": name, "pass": "B"}); all_hits.append(h)
        for w in ca:
            w.update({"file": name, "pass": "A"}); all_cands.append(w)
        for w in cb:
            w.update({"file": name, "pass": "B"}); all_cands.append(w)
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"passA {sum(1 for h in all_hits if h['pass']=='A')} hits "
          f"({sum(1 for h in all_hits if h['pass']=='A' and h['uncapped'])} uncapped), "
          f"passB {sum(1 for h in all_hits if h['pass']=='B')} hits, "
          f"{len(all_cands)} total candidates")
    return {"files": files, "total_chars": total_chars,
            "hits": all_hits, "candidates": all_cands}


if __name__ == "__main__":
    res = {"census_drama": census(DRAMA, "drama register (14 plays, 1 ed/play, 1870 Hernani)"),
           "excluded_edition": census([EXCLUDED_EDITION], "excluded Hernani edition (Hetzel 1889)")}
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "reinforced-pour-inf-drama-recall_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
