#!/usr/bin/env python3
r"""Census for battery disloc-demonstrative-drama-clause-initial.

Restricts the drama demonstrative census to CLAUSE-INITIAL demonstratives,
eliminating the preposition/verb-object confound class (the three nearest
near-misses of disloc-demonstrative-drama-reissue all had 'cela' governed
by a preceding preposition/verb: 'compromettre tout cela', 'apres tout
cela', 'Pour cela').

P1 (dislocation), P2 (exclamatory filter), P3 (infinitive candidate) are
copied VERBATIM from disloc_demonstrative_drama_reissue_census.py, not
modified after seeing data.

Clause-initial gate (pre-registered in the target charter): the
demonstrative counts as clause-initial iff the text immediately preceding
it (mod whitespace) ends with one of:
  - start of text
  - a sentence terminator [. ! ? ...]  (also a closing quote ">>" right
    after a terminator)
  - a speaker-label line end (the preceding non-empty line is an all-caps
    speaker label)
  - a paragraph break (blank line = start of a new speech turn)
  - a colon introducing the turn
Anything else (mid-clause, i.e. preceded by word characters, prepositions,
verbs) is the confound class and is excluded from the candidates — but is
counted and listed separately for honesty. The speaker-label and
paragraph-break rules only apply when the demonstrative starts its own line
(a label two lines above a mid-speech 'cela' does not promote it). Turn
initiality after an em-dash or opening guillemet counts as clause-initial
(start of a speech turn).

Corpus: same 14 files as the reissue (one edition per play).
All files: code/side-period/corpus/.
"""
import json, re, os

LANE = os.path.expanduser("~/workspace/cipher-hunt/lanes/zeschau-seebach-1841")
CORPUS = os.path.join(LANE, "code/side-period/corpus")

DRAMA_FILES = [
    "dumas-antony.txt",
    "dumas-henri-iii.txt",
    "dumas-kean.txt",
    "dumas-mariage-louis-xv-1841.txt",
    "dumas-tour-de-nesle.txt",
    "hugo-burgraves.txt",
    "hugo-hernani-1870.txt",
    "hugo-ruy-blas.txt",
    "labiche-chapeau-de-paille.txt",
    "labiche-martin-poudre-aux-yeux.txt",
    "musset-comedies-proverbes-1850.txt",
    "scribe-bertrand-et-raton.txt",
    "scribe-verre-d-eau.txt",
    "vigny-chatterton-1835.txt",
]

DEM = re.compile(r"\b(cela|ceci|ça|cel[àa]|cec[iy])\s*[,;:]", re.IGNORECASE)
INF = re.compile(
    r"\b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b", re.IGNORECASE)

TERMINATORS = ".!?…"


def _is_speaker_label(line):
    """Heuristic: an all-caps line ending a speaker label in a play text."""
    s = line.strip()
    if len(s) < 3 or len(s) > 60:
        return False
    letters = re.sub(r"[^A-Za-zÀÂÄÇÉÈÊËÎÏÔÖÙÛÜ]", "", s)
    if len(letters) < 3:
        return False
    if letters != letters.upper():
        return False
    # A label typically ends with . or , or ; and contains no lowercase-run
    # words; bare caps fragments like scene headers also match, which is
    # harmless (they are still turn boundaries).
    return True


def gate_position(text, m_start):
    """Return (is_clause_initial: bool, reason: str)."""
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
    # The match must be at the start of its own line for the label /
    # paragraph rules to mean "start of a speech turn" (otherwise a label
    # two lines up would wrongly promote a mid-speech 'cela').
    cur_line_start = not lines[-1].strip()
    if last in "—–«":
        return True, "turn-initial dash/opening-quote"
    if cur_line_start:
        if len(lines) >= 3 and not lines[-3].strip() and not lines[-2].strip():
            return True, "paragraph-break-turn-start"
        nonempty = [l for l in lines[:-1] if l.strip()]
        if nonempty and _is_speaker_label(nonempty[-1]):
            return True, f"speaker-label-line '{nonempty[-1].strip()[:40]}'"
    # Otherwise: mid-clause -> confound class (preposition/verb-governed).
    return False, "mid-clause (preceded by running text)"


def window_from(text, m_start):
    seg = text[m_start:m_start + 180]
    end = re.search(r"[!?.]", seg)
    return seg[: end.end()] if end else seg


def census():
    total = 0
    files = []
    ci_candidates = []      # clause-initial + P2 + P3
    confound = []           # mid-clause + P2 + P3 (the confound class)
    ci_hits = 0
    for name in sorted(DRAMA_FILES):
        p = os.path.join(CORPUS, name)
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
            rec = {"file": name, "offset": m.start(),
                   "dem": m.group(1).lower(), "window": win,
                   "inf_hits": inf, "gate_reason": reason}
            if ci:
                ci_candidates.append(rec)
            else:
                confound.append(rec)
        files.append({"file": name, "chars": len(t),
                      "dem_comma_hits": dem_hits})
    print(f"=== clause-initial census: {len(files)} files, {total} chars, "
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
                       "disloc-demonstrative-drama-clause-initial_census.json")
    json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
    print("wrote", out)
