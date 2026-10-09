#!/usr/bin/env python3
r"""Recall-gap census for battery gov-excl-inf-recall-drama.

Runs the prose parent's G1/G2/G3 recall-gap searches (structural
duplicate of gov_excl_inf_recall_census.py, same GOV_INF / LONG_INF /
closest-match / no-[.;]-tail rules) against the ingested drama corpus:
14 files / 14 unique plays / 2,969,582 chars, pinned by name (one
edition per play; hugo-hernani-1870.txt kept, hugo-hernani.txt
dropped as the duplicate edition).

G1 '?'-terminated windows: for every '?', 120-char lookback, parent
   GOV_INF (prep + 0-2 short tokens + infinitive-shaped word),
   closest match to '?', no [.;] between match end and '?'.
G2 long spans: for every '!', 300-char lookback, LONG_INF = prep +
   3-6 short tokens (each <=8 chars) + infinitive-shaped word,
   closest match to '!', same no-[.;]-tail rule. Pattern-disjoint
   from the parent's GOV_INF by the >=3-token floor.
G3 dash/colon-adjacent: for every '!', 120-char lookback, ALL
   GOV_INF matches; keep non-closest ones where a dash
   (em/en/hyphen) or colon lies between match end and '!' (no [.;]
   between match end and the pause mark). Diag: non-closest matches
   with no dash/colon (outside the three gaps, reported for due
   diligence).

Banding: dist = chars from infinitive-shaped word end to terminator.
Tight band dist<=40 is the discriminating band.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
NT = os.path.join(LANE, "code/crowd17/next-token")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

# Pinned drama set: parent's 14-file set, one edition per play, 2,969,582 chars.
DRAMA_FILES = [
    "dumas-antony.txt", "dumas-henri-iii.txt", "dumas-kean.txt",
    "dumas-mariage-louis-xv-1841.txt", "dumas-tour-de-nesle.txt",
    "hugo-burgraves.txt", "hugo-hernani-1870.txt", "hugo-ruy-blas.txt",
    "labiche-chapeau-de-paille.txt", "labiche-martin-poudre-aux-yeux.txt",
    "musset-comedies-proverbes-1850.txt", "scribe-bertrand-et-raton.txt",
    "scribe-verre-d-eau.txt", "vigny-chatterton-1835.txt",
]
EXPECTED_TOTAL = 2969582

GOV_INF = re.compile(
    r"\b(pour|à|a|de|d['\u2019])\s+"
    r"(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}"
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)
LONG_INF = re.compile(
    r"\b(pour|à|a|de|d['\u2019])\s+"
    r"([a-zàâäçéèêëîïôöùûü'\-]{1,8}\s+){3,6}"
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)
DASH_COLON = re.compile(r"[\u2014\u2013\-:]")

def closest_match(seg, rx):
    best = None
    for g in rx.finditer(seg):
        tail = seg[g.end():]
        if re.search(r"[.;]", tail):
            continue
        if best is None or g.end() > best[1]:
            best = (g, g.end())
    return best

def rec(g, tail, term_off, gap):
    inf = g.group(0).rsplit(None, 1)[-1].lower()
    prep = g.group(1).lower()
    toks = g.group(0).split()
    return {"gap": gap, "prep": prep,
            "intervening_tokens": len(toks) - 2,
            "infinitive_shaped": inf,
            "dist": len(tail),
            "term_offset": term_off}

def g1(text):
    out = []
    for m in re.finditer(r"\?", text):
        seg = text[max(0, m.start() - 120):m.start()]
        b = closest_match(seg, GOV_INF)
        if b is None:
            continue
        g, end = b
        tail = seg[end:]
        r = rec(g, tail, m.start(), "G1-qmark")
        r["window"] = seg + "?"
        out.append(r)
    return out

def g2(text):
    out = []
    for m in re.finditer(r"!", text):
        seg = text[max(0, m.start() - 300):m.start()]
        b = closest_match(seg, LONG_INF)
        if b is None:
            continue
        g, end = b
        tail = seg[end:]
        r = rec(g, tail, m.start(), "G2-longspan")
        r["window"] = seg + "!"
        out.append(r)
    return out

def g3(text):
    out, diag = [], []
    for m in re.finditer(r"!", text):
        seg = text[max(0, m.start() - 120):m.start()]
        matches = []
        for g in GOV_INF.finditer(seg):
            tail = seg[g.end():]
            if re.search(r"[.;]", tail):
                continue
            matches.append((g, g.end()))
        if len(matches) < 2:
            continue
        matches.sort(key=lambda x: x[1])
        for g, end in matches[:-1]:
            mid = seg[end:]
            dm = DASH_COLON.search(mid)
            if dm is None:
                r = rec(g, mid, m.start(), "G3-diag-nopause")
                r["window"] = seg + "!"
                diag.append(r)
                continue
            before = mid[:dm.start()]
            if re.search(r"[.;]", before):
                continue
            r = rec(g, mid, m.start(), "G3-dashcolon")
            r["window"] = seg + "!"
            r["pause_mark"] = dm.group(0)
            r["pause_dist"] = dm.start()
            out.append(r)
    return out, diag

files = []
all_c = []
total = 0
for fn in DRAMA_FILES:
    path = os.path.join(CORPUS, fn)
    text = open(path, encoding="utf-8", errors="replace").read()
    total += len(text)
    files.append({"file": fn, "chars": len(text),
                  "excl": text.count("!"), "qmark": text.count("?")})
    cands = []
    for r in g1(text):
        r["file"] = fn; cands.append(r)
    for r in g2(text):
        r["file"] = fn; cands.append(r)
    g3c, diag = g3(text)
    for r in g3c + diag:
        r["file"] = fn; cands.append(r)
    all_c.extend(cands)
print("total chars:", total, "(expected:", EXPECTED_TOTAL, ")")
assert total == EXPECTED_TOTAL, "corpus drift; re-pin"
for r in all_c:
    del r["window"]
out = {"files": files, "total_chars": total,
       "per_gap": {g: sum(1 for r in all_c if r["gap"] == g)
                   for g in ("G1-qmark", "G2-longspan",
                             "G3-dashcolon", "G3-diag-nopause")},
       "tight": sum(1 for r in all_c if r["dist"] <= 40),
       "candidates": all_c}
json.dump(out, open(os.path.join(NT, "gov-excl-inf-recall-drama_census.json"),
                                "w"), indent=1, ensure_ascii=False)
print("per gap:", out["per_gap"], "| tight:", out["tight"],
      "| total:", len(all_c))

wins = []
for fn in DRAMA_FILES:
    path = os.path.join(CORPUS, fn)
    text = open(path, encoding="utf-8", errors="replace").read()
    for r in g1(text):
        r["file"] = fn; wins.append((r["gap"], fn, r["term_offset"], r["window"]))
    for r in g2(text):
        r["file"] = fn; wins.append((r["gap"], fn, r["term_offset"], r["window"]))
    g3c, diag = g3(text)
    for r in g3c + diag:
        r["file"] = fn; wins.append((r["gap"], fn, r["term_offset"], r["window"]))
json.dump(wins, open(os.path.join(NT, "gov-excl-inf-recall-drama_windows.json"),
                     "w"), ensure_ascii=False)
print("windows saved:", len(wins))
