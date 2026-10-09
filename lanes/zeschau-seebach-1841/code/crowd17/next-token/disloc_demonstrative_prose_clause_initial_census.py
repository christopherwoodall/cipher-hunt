#!/usr/bin/env python3
r"""Census for battery disloc-demonstrative-prose-clause-initial.

Applies the STRICT clause-initial gate (from
disloc_demonstrative_drama_clause_initial_census.py, verbatim) to the
demonstrative-comma census on the 27.66M-char PROSE corpus, eliminating
the preposition/verb-object confound class.

Parent: disloc-demonstrative-inf (NULL) — 385 dem-comma hits in the 1841
register -> 6 excl candidates, 62 hits wider -> 9 excl candidates, 0
genuine. Parent follow-up #1 of that battery is disloc-demonstrative-drama;
this target is the prose-register counterpart of the drama clause-initial
battery.

P1 (dislocation), P2 (exclamatory filter), P3 (infinitive candidate) are
copied VERBATIM from disloc_demonstrative_census.py, not modified after
seeing data. Gate rules copied VERBATIM from
disloc_demonstrative_drama_clause_initial_census.py.

Clause-initial gate (pre-registered in the target charter): the
demonstrative counts as clause-initial iff the text immediately preceding
it (mod whitespace) ends with one of:
  - start of text
  - a sentence terminator [. ! ? ...] (also a closing quote ">>" right
    after a terminator)
  - a speaker-label line end (the preceding non-empty line is an all-caps
    speaker label)
  - a paragraph break (blank line = start of a new speech turn)
  - a colon introducing the turn
  - turn-initial em-dash or opening guillemet
The speaker-label and paragraph-break rules only apply when the
demonstrative starts its own line. Verse line breaks do not count as
clause boundaries. Anything else is the confound class (counted and
listed separately for honesty).

Corpus: 18 French 1841-register prose files + 3 wider 19th-century
prose files = 21 files, 27,657,940 chars (same set as
disloc-demonstrative-inf). German files excluded with cause (register is
French).
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")
GUTENBERG = os.path.join(LANE, "data")

PROSE_FILES = [
    os.path.join(CORPUS, "guizot-memoires-t1-gutenberg.txt"),
    os.path.join(CORPUS, "guizot-memoires-t2-gutenberg.txt"),
    os.path.join(CORPUS, "guizot-memoires-t3-gutenberg.txt"),
    os.path.join(CORPUS, "guizot-memoires-t5-t6.txt"),
    os.path.join(CORPUS, "nesselrode-v10.txt"),
    os.path.join(CORPUS, "nesselrode-v7.txt"),
    os.path.join(CORPUS, "nesselrode-v8.txt"),
    os.path.join(CORPUS, "nesselrode-v9.txt"),
    os.path.join(CORPUS, "revue-deux-mondes-1841-q1.txt"),
    os.path.join(CORPUS, "revue-deux-mondes-1841-q2.txt"),
    os.path.join(CORPUS, "revue-deux-mondes-1841-q3.txt"),
    os.path.join(CORPUS, "revue-deux-mondes-1841-q4.txt"),
    os.path.join(CORPUS, "metternich-papiere-v4.txt"),
    os.path.join(CORPUS, "metternich-papiere-v6.txt"),
    os.path.join(CORPUS, "talleyrand-memoires-v1.txt"),
    os.path.join(CORPUS, "pozzo-di-borgo-correspondance-v1.txt"),
    os.path.join(CORPUS, "levant-correspondence-1841-p3.txt"),
    os.path.join(GUTENBERG, "gutenberg-17489-miserables1.txt"),
    os.path.join(GUTENBERG, "gutenberg-30513-tocqueville-t1.txt"),
    os.path.join(GUTENBERG, "gutenberg-30514-tocqueville-t2.txt"),
]

DEM = re.compile(r"\b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]", re.IGNORECASE)
INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)

TERMINATORS = ".!?…"


def _is_speaker_label(line):
    s = line.strip()
    if len(s) < 3 or len(s) > 60:
        return False
    letters = re.sub(r"[^A-Za-zÀÂÄÇÉÈÊËÎÏÔÖÙÛÜ]", "", s)
    if len(letters) < 3:
        return False
    if letters != letters.upper():
        return False
    return True


def gate_position(text, m_start):
    prev = text[max(0, m_start - 300):m_start]
    stripped = prev.rstrip()
    if not stripped:
        return True, "start-of-text"
    last = stripped[-1]
    if last in TERMINATORS:
        return True, f"sentence-terminator '{last}'"
    if last == "\u00bb":
        return True, "closing-quote-after-terminator"
    if last == ":":
        return True, "colon-introduced-turn"
    lines = prev.split("\n")
    cur_line_start = not lines[-1].strip()
    if last in "—–«":
        return True, "turn-initial dash/opening-quote"
    if cur_line_start:
        if len(lines) >= 3 and not lines[-3].strip() and not lines[-2].strip():
            return True, "paragraph-break-turn-start"
        nonempty = [l for l in lines[:-1] if l.strip()]
        if nonempty and _is_speaker_label(nonempty[-1]):
            return True, f"speaker-label-line '{nonempty[-1].strip()[:40]}'"
    return False, "mid-clause (preceded by running text)"


def window_from(text, m_start):
    seg = text[m_start:m_start + 180]
    end = re.search(r"[!?.]", seg)
    return seg[: end.end()] if end else seg


def census():
    total = 0
    files = []
    ci_candidates = []
    confound = []
    ci_hits = 0
    for p in PROSE_FILES:
        assert os.path.exists(p), f"missing corpus file: {p}"
        t = open(p, encoding="utf-8", errors="replace").read()
        total += len(t)
        dem_hits = 0
        for m in DEM.finditer(t):
            dem_hits += 1
            ci, reason = gate_position(t, m.start())
            if ci:
                ci_hits += 1
            win = window_from(t, m.start())
            if "!" not in win:
                continue
            inf = sorted({w.group(0).lower() for w in INF.finditer(win)})
            if not inf:
                continue
            rec = {"file": os.path.basename(p), "offset": m.start(),
                   "dem": m.group(1).lower(), "window": win,
                   "inf_hits": inf, "gate_reason": reason}
            if ci:
                ci_candidates.append(rec)
            else:
                confound.append(rec)
        files.append({"file": os.path.basename(p), "chars": len(t),
                      "dem_comma_hits": dem_hits})
    print(f"=== prose clause-initial census: {len(files)} files, {total} chars, "
          f"{sum(f['dem_comma_hits'] for f in files)} dem-comma hits, "
          f"{ci_hits} clause-initial, "
          f"{len(ci_candidates)} clause-initial excl candidates, "
          f"{len(confound)} confound-class excl candidates")
    return {"files": files, "total_chars": total,
            "clause_initial_dem_hits": ci_hits,
            "clause_initial_candidates": ci_candidates,
            "confound_candidates": confound}


if __name__ == "__main__":
    res = census()
    out = os.path.join(LANE, "code/crowd17/next-token",
                       "disloc-demonstrative-prose-clause-initial_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
