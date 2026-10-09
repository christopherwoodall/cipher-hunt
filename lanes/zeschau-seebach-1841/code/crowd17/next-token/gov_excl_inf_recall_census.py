#!/usr/bin/env python3
r"""Recall-gap census for battery gov-excl-inf-recall.

Closes the three fenced recall gaps of battery-gov-excl-inf-register
(2026-10-09: 859 candidates, 0 genuine) in the SAME 27.66M-char
19th-century French corpus. Targets ONLY windows the parent census
did not search (novelty is structural, not assumed):

G1 '?'-terminated windows: the parent keyed ONLY on "!". For every "?"
   in the corpus, take the 120 chars before it and run the parent's
   GOV_INF pattern (prep + 0-2 short tokens + infinitive-shaped word);
   keep the match closest to the "?", require no [.;] between match
   end and "?" (same sentence-internal rule as the parent). ALL G1
   candidates are novel by construction (parent never keyed "?").

G2 longer preposition->infinitive spans: the parent's GOV_INF allowed
   at most 2 short tokens between prep and infinitive. For every "!",
   take a 300-char lookback and run LONG_INF: prep + 3-6 short tokens
   (each <=8 chars) + infinitive-shaped word; closest match to "!",
   same no-[.;]-in-tail rule. Novelty: the >=3-token requirement makes
   G2 matches pattern-disjoint from the parent's (the parent's regex
   can never match them), so every G2 candidate is untested by the
   parent regardless of which "!" it sits before.

G3 dash/colon-adjacent exclamations: the parent kept only the CLOSEST
   match per "!" (its candidates() keeps max g.end()). For every "!",
   take the 120-char lookback, find ALL GOV_INF matches, and keep the
   non-closest ones where a dash (em/en/hyphen: \u2014\u2013-) or colon
   lies between the match end and the "!" (no [.;] between match end
   and that pause mark). These pause-mark-adjacent exclamations were
   never tested: the parent's closest-match rule discarded them.
   (Also reported as a diagnostic: non-closest matches with NO
   dash/colon between match and "!" -- untested by the parent too, but
   outside this battery's three named gaps.)

Banding: dist = chars from the end of the infinitive-shaped word to
the terminator. Tight band dist<=40 is the discriminating band (the
exclaimed element is the infinitive phrase itself). All candidates are
printed for MANUAL classification (regex cannot separate -er
infinitives from nouns/adjectives in -er; unaccented "a" is
verb-avoir noise; the terminator may belong to a matrix clause).
Cause scheme mirrors the parent (A OCR false friends, B finite-matrix
embedding, C exclaimed-NP embedding, D quotation/interjection
terminator) plus E interrogative-matrix for '?' windows.

Corpus (identical to the parent diagnostic; sizes recomputed
in-session):
  - 1841-register lane corpus: code/side-period/corpus/*.txt (French
    files only; German files excluded).
  - Wider 19th-century register: data/gutenberg-17489-miserables1.txt
    (1862), data/gutenberg-30513-tocqueville-t1.txt (1835),
    data/gutenberg-30514-tocqueville-t2.txt (1840).

Output: gov-excl-inf-recall_census.json with per-gap yields, per-file
sizes, and every candidate window + dist + absolute terminator offset.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
NT = os.path.join(LANE, "code/crowd17/next-token")
CORPUS1841 = os.path.join(LANE, "code/side-period/corpus")
# EXACT 18-file set of the parent battery (gov-excl-inf-register), read from
# its census JSON. The corpus directory has grown since (drama ingest);
# pinning by name guarantees the identical corpus (parent total 25,670,258
# chars, asserted at runtime).
_parent = json.load(open(os.path.join(
    NT, "gov-excl-inf-register_census.json")))["census_1841_register"]
PARENT_FILES = sorted(x["file"] for x in _parent["files"])
PARENT_TOTAL = _parent["total_chars"]
WIDER = [
    os.path.join(LANE, "data/gutenberg-17489-miserables1.txt"),
    os.path.join(LANE, "data/gutenberg-30513-tocqueville-t1.txt"),
    os.path.join(LANE, "data/gutenberg-30514-tocqueville-t2.txt"),
]

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
            "window": (g.string if False else "") or None,
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
    """Non-closest matches with dash/colon between match end and '!'."""
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
                r = rec(g, mid, m.start(), "G3-nocloset-nopause-DIAG")
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

def census(paths, label):
    total_chars, n_bang, n_q = 0, 0, 0
    files = []
    g1c, g2c, g3c, g3d = [], [], [], []
    for p in sorted(paths):
        name = os.path.basename(p)
        t = open(p, encoding="utf-8", errors="replace").read()
        total_chars += len(t)
        nb, nq = t.count("!"), t.count("?")
        n_bang += nb
        n_q += nq
        a = g1(t); b = g2(t); c, d = g3(t)
        files.append({"file": name, "chars": len(t), "bang_count": nb,
                      "qmark_count": nq, "G1": len(a), "G2": len(b),
                      "G3": len(c), "G3_diag": len(d)})
        for r in a + b + c + d:
            r["file"] = name
        g1c += a; g2c += b; g3c += c; g3d += d
    tight = lambda xs: sum(1 for x in xs if x["dist"] <= 40)
    print(f"=== {label}: {len(files)} files, {total_chars} chars, "
          f"{n_bang} '!', {n_q} '?'; "
          f"G1={len(g1c)} (tight {tight(g1c)}), "
          f"G2={len(g2c)} (tight {tight(g2c)}), "
          f"G3={len(g3c)} (tight {tight(g3c)}), "
          f"G3-diag(non-closest, no pause)={len(g3d)} (tight {tight(g3d)})")
    return {"files": files, "total_chars": total_chars,
            "bang_count": n_bang, "qmark_count": n_q,
            "G1_qmark": g1c, "G2_longspan": g2c,
            "G3_dashcolon": g3c, "G3_diag_nopause": g3d}

if __name__ == "__main__":
    c1841 = [os.path.join(CORPUS1841, f) for f in PARENT_FILES]
    missing = [p for p in c1841 if not os.path.exists(p)]
    assert not missing, f"parent corpus files missing: {missing}"
    res = {"census_1841_register": census(c1841, "1841 register"),
           "census_wider_19c": census(WIDER, "wider 19c")}
    got = res["census_1841_register"]["total_chars"]
    assert got == PARENT_TOTAL, f"corpus drift: {got} != parent {PARENT_TOTAL}"
    print(f"corpus identity asserted: 1841-register total {got} chars == parent")
    out = os.path.join(NT, "gov-excl-inf-recall_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
