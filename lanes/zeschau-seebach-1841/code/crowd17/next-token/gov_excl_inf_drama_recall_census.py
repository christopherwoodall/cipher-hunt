#!/usr/bin/env python3
r"""Recall-gap census for battery gov-excl-inf-drama-recall.

Follow-up #2 of the PROMOTE battery-gov-excl-inf-register-drama
(2026-10-09: 839 candidates in the drama corpus, 1 genuine:
scribe-bertrand-et-raton "Pour conspirer !").

THIS battery closes the three fenced recall gaps of the DRAMA
battery — the same three gaps the prose battery fenced and closed
(battery-gov-excl-inf-recall, 1,874 candidates, 0 genuine):
  G1 '?' terminators, G2 long prep->infinitive spans (>2 short
  tokens), G3 dash/colon-adjacent exclamations.

Design is structural-duplicate of gov_excl_inf_recall_census.py,
corpus = the 14-file drama corpus of the parent drama battery
(byte-identical set pinned by name from its census JSON).

Bar (verbatim, pre-registered): "Close this battery's recall gaps
('?'-terminated exclamatory infinitives, preposition-to-infinitive
spans longer than two short tokens, dash/colon pause marks) - same
fenced gaps as the prose battery; >=1 genuine re-opens"

Numbered pass/fail clauses:
1. >=1 genuine attestation in the widened gap searches re-opens.
2. Confirmed zero closes the recall gap.

Cause scheme mirrors the parent (A OCR false friends, B
finite-matrix embedding, C exclaimed-NP embedding, D
quotation/interjection terminator) plus E interrogative-matrix
for '?' windows.

Output: gov-excl-inf-drama-recall_census.json with per-gap yields,
per-file sizes, and every candidate window + dist + absolute
terminator offset.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
NT = os.path.join(LANE, "code/crowd17/next-token")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

# Byte-identical 14-file drama set of the parent battery (pinned by name).
_parent = json.load(open(os.path.join(
    NT, "gov-excl-inf-register-drama_census.json")))["census_drama"]
DRAMA_FILES = sorted(f["file"] for f in _parent["files"])
PARENT_TOTAL = _parent["total_chars"]
print("drama files:", len(DRAMA_FILES), "parent total chars:", PARENT_TOTAL)

# Parent's pattern, verbatim (prep + 0-2 short tokens + infinitive-shaped)
GOV_INF = re.compile(
    r"\b(pour|à|a|de|d['\u2019])\s+"
    r"(?:[a-zàâäçéèêëîïôöùûü'\-]{1,6}\s+){0,2}"
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)
# Widened: prep + 3-6 short tokens (each <=8 chars) + infinitive-shaped.
# The >=3-token floor makes every match pattern-disjoint from GOV_INF.
LONG_INF = re.compile(
    r"\b(pour|à|a|de|d['\u2019])\s+"
    r"([a-zàâäçéèêëîïôöùûü'\-]{1,8}\s+){3,6}"
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b",
    re.IGNORECASE)
DASH_COLON = re.compile(r"[\u2014\u2013\-:]")

def closest_match(seg, rx):
    """Closest match to the terminator (segment end), no [.;] in tail."""
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
    """'?' windows: parent GOV_INF, 120-char lookback, closest to '?'."""
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
    """Long spans: LONG_INF (>=3 intervening tokens), 300-char lookback."""
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
    """Non-closest matches with dash/colon between match end and '!'.
    len(matches)>=2 required (parent kept the closest); diag = non-closest
    with no dash/colon (diagnostic, untested by parent but outside gaps)."""
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
        for g, end in matches[:-1]:  # all but the closest (parent kept it)
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
print("total chars:", total, "(parent:", PARENT_TOTAL, ")")
assert total == PARENT_TOTAL, "corpus drift; re-pin"
for r in all_c:
    del r["window"]  # windows stored separately below
cands_with_windows = []
text_cache = {}
for r in all_c:
    pass
out = {"files": files, "total_chars": total,
       "per_gap": {g: sum(1 for r in all_c if r["gap"] == g)
                   for g in ("G1-qmark", "G2-longspan",
                             "G3-dashcolon", "G3-diag-nopause")},
       "tight": sum(1 for r in all_c if r["dist"] <= 40),
       "candidates": all_c}
json.dump(out, open(os.path.join(NT, "gov-excl-inf-drama-recall_census.json"),
                                "w"), indent=1, ensure_ascii=False)
print("per gap:", out["per_gap"], "| tight:", out["tight"],
      "| total:", len(all_c))

# Save windows separately for classification reads
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
json.dump(wins, open(os.path.join(NT, "gov-excl-inf-drama-recall_windows.json"),
                     "w"), ensure_ascii=False)
print("windows saved:", len(wins))
