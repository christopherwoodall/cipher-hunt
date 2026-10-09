#!/usr/bin/env python3
r"""Census for battery reinforced-head-narrative-uncapped-drama.

Closes the residual deep-narrative recall gap flagged by
reinforced-pour-inf-drama-recall: one window (dumas-tour-de-nesle.txt
@79885) had NO sentence-end inside the 400-char cap, so the window was
truncated at 400 chars and any attestation beyond was invisible.

Pass B (verbatim reproduction): DEM_B separator class [,;:\-—()],
400-char cap, "!" filter, GOV_INF on after-separator text. Identifies
all windows still uncapped at 400.

Pass C (the new work): punctuation-aware windows — dem hit to the NEXT
sentence-end [!?.], uncapped (5000-char safety cap only). Same "!"
filter and GOV_INF. Every pass-B uncapped window is resolved
individually; the pass-B vs pass-C candidate sets are diffed.

Corpus: the 14-play drama list from reinforced-pour-inf-drama-recall
(one Hernani edition: hugo-hernani-1870.txt; hugo-hernani.txt run
separately as the excluded edition).
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

DRAMA = [
    "dumas-mariage-louis-xv-1841.txt",
    "vigny-chatterton-1835.txt",
    "musset-comedies-proverbes-1850.txt",
    "hugo-hernani-1870.txt",
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
EXCLUDED_EDITION = "hugo-hernani.txt"

DEM_B = re.compile(
    r"\b((?:celui|ceux|celle|celles)[-\u2011\u2013 ]?(?:l[àa]|ci)|"
    r"ça[-\u2011\u2013 ]?(?:l[àa]|ci))\s*[,;:\-\u2013\u2014()]", re.IGNORECASE)

GOV_INF = re.compile(
    r"\b(pour|à|a|de|d['’])\s+"
    r"(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}"
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)

SENT_END = re.compile(r"[!?.]")


def window_b(text, m):
    seg = text[m.start():m.start() + 400]
    end = SENT_END.search(seg)
    win = seg[:end.end()] if end else seg
    return win, end is None


def window_c(text, m):
    seg = text[m.start():m.start() + 5000]
    end = SENT_END.search(seg)
    win = seg[:end.end()] if end else seg
    return win, end is None


def candidates(text, m, win):
    if "!" not in win:
        return []
    after = win[m.end() - m.start():]
    return sorted({(g.group(1).lower() + " + " + g.group(0).lower())
                   for g in GOV_INF.finditer(after)})


def census(paths, label):
    total_chars, files, hits, cands = 0, [], [], []
    for name in paths:
        t = open(os.path.join(CORPUS, name), encoding="utf-8",
                 errors="replace").read()
        total_chars += len(t)
        f_cands_b, f_cands_c, uncapped_b, still_uncapped_c = 0, 0, 0, 0
        for m in DEM_B.finditer(t):
            wb, uncapped = window_b(t, m)
            wc, still = window_c(t, m)
            if uncapped:
                uncapped_b += 1
            if still:
                still_uncapped_c += 1
                # resolve individually: note how far the next sentence end is
            gb = candidates(t, m, wb)
            gc = candidates(t, m, wc)
            hits.append({"file": name, "off": m.start(),
                         "dem": m.group(1).lower(), "uncapped_b": uncapped,
                         "still_uncapped_c": still,
                         "len_wb": len(wb), "len_wc": len(wc),
                         "cands_b": gb, "cands_c": gc})
            if gb:
                f_cands_b += 1
                cands.append({"file": name, "off": m.start(), "pass": "B",
                              "window": wb, "gov_inf_hits": gb})
            if gc:
                f_cands_c += 1
                cands.append({"file": name, "off": m.start(), "pass": "C",
                              "window": wc, "gov_inf_hits": gc})
        files.append({"file": name, "chars": len(t),
                      "uncapped_at_400": uncapped_b,
                      "still_uncapped_c": still_uncapped_c,
                      "passB_candidate_windows": f_cands_b,
                      "passC_candidate_windows": f_cands_c})
    # diff: candidate windows that appear ONLY in pass C
    b_ids = {(c["file"], c["off"]) for c in cands if c["pass"] == "B"}
    c_ids = {(c["file"], c["off"]) for c in cands if c["pass"] == "C"}
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"{len(hits)} dem hits, uncapped@400: {sum(1 for h in hits if h['uncapped_b'])}, "
          f"still uncapped in C: {sum(1 for h in hits if h['still_uncapped_c'])}, "
          f"passB cand windows: {len(b_ids)}, passC cand windows: {len(c_ids)}, "
          f"C-only: {len(c_ids - b_ids)}")
    return {"files": files, "total_chars": total_chars, "hits": hits,
            "candidates": cands}


if __name__ == "__main__":
    res = {
        "census_drama": census(DRAMA, "drama register (14 plays, 1 ed/play, 1870 Hernani)"),
        "excluded_edition": census([EXCLUDED_EDITION], "excluded Hernani edition (Hetzel 1889)"),
    }
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "reinforced-head-narrative-uncapped-drama_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
