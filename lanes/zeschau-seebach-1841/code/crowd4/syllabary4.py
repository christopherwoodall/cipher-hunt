"""syllabary4.py — shared infrastructure for round-4 executors (Seebach lane).

Recovered encipherer syllabary + F30-legal instruments.

WHAT data/upstream-syll*.py ACTUALLY IMPLEMENTS (read 2026-10-07, do not
re-derive from memory):
  * UNITS inventory (identical in syll.py/syll2.py/syll3.py): 24 single
    letters (a-z minus k,w) + 156 French syllable/function-word units =
    180 units total. Categories: 98 two-letter (CV/VC open+closed:
    la le li..., an en in..., ar er..., al el...), 47 three-letter
    (CCV onsets: pre pro pri, tra tre..., cha che..., grammatical:
    ent ant ion ons ais ait...), 11 four-letter (ment tion pour nous
    vous iere elle esse ette ance ence). Function words included as
    units: par pour con com des les ses ces mes tes nous vous que qui.
  * Cutting model: every 2-digit group -> exactly ONE unit; plaintext =
    concatenation of units. No nulls. syll.py: free assignment (annealer
    degenerates to "ment/vous/ait" per upstream-NOTES.md). syll2.py: adds
    one-cell-per-syllable + letter<=4 penalties. syll3.py: penalties
    zeroed but duplicate-syllable proposals skipped (homophony allowed
    only implicitly).
  * Scoring: French 4-gram (hsolve.score) + 2.3/len length bonus.
  * RESULT (upstream-NOTES.md, "What failed" table): all three "still no
    French". The off-the-shelf inventory + maximal-cut model does NOT
    recover the encipherer's table. It is a hypothesis, not a recovery.

RECOVERED CUTTING RULES (ground-truth + lane-verified, F30 basis):
  R1. Cells are 1-4 letters; 1-letter cells exist. Crib "la premiere"
     @1033 = 11|70|82|34|29|40 = la|pre|m|i|er|e: onset cluster (pre),
     BARE CONSONANT (82=m), BARE VOWEL (34=i), morphological ending
     (29=er), mute-e written (40=e). Any fragment leg must allow
     1-letter cells.
  R2. Cuts are by ear and INCONSISTENT: "personne" = 93|52|94
     (per|so|nne @160) vs 77|62|94 (pers|on|ne @507) — same word, two
     cuts in one cipher (frenchman ear reads, positions verified from
     pair stream). A fragment leg must never require a unique
     segmentation; test the SET of plausible cuts.
  R3. Mute -e is WRITTEN (crib: premiere -> ...|er|e with 40="e" for the
     mute final -e; "erre" = 29|40 = er|e @684/@291). Phonetic models
     that need mute-e UNWRITTEN contradict the crib (N17 killed
     06=/man/ "demand-" on exactly this). Unwritten-mute-e readings
     need their own positive evidence; written-mute-e is the default.
  R4. Morphological endings are cells: 29=er is word-final-ish (phase-C
     anchor); the table mixes letters, syllables, endings, and whole
     function words (11=la, 46=que are ground truth).

F30 (lane rule): fragment hypotheses test against THIS recovered
syllabary (R1-R4), not against rigid era syllabification. Era
word-space legs (unigrams, word bigrams, grammatical attestation on
word sequences) survive; era-syllable-conditional legs on fragments
are VOID.

Provided:
  load_pairs()            -> list of 1,846 group strings (offsets applied)
  load_era_words()        -> Tocqueville t1+t2 word tokens (lowercased)
  era_unigram(w)          -> P(word) with +0.5 smoothing note in era_p_next
  era_p_next(w2, w1)      -> P(w2|w1), Laplace-smoothed
  era_p_after(w, ending)  -> P(w | prev word ends with `ending`) word-space
  followers(pairs, g) / predecessors(pairs, g) -> Counters
  windows(pairs, g, r=3)  -> [(pos, ctx_list)]
  ngram_count(pairs, seq)  -> int
  segmentations(word, cells=None) -> plausible cut sets under R1-R4
  GT / PROV value tables (status-marked)
"""

import json
import math
import os
import re
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
DATA = os.path.join(os.path.dirname(LANE), 'data')

GT = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i', '29': 'er',
      '40': 'e', '46': 'que'}                      # pencil-crib ground truth
PROV = {'87': 'ce', '64': 'qui', '96': 'par',      # provisional values
        '94': 'ne', '06': 'verb-stem-class', '67': 'veut?'}


def load_pairs():
    off = json.load(open(os.path.join(DATA, 'upstream-offsets.json')))
    toks = []
    for l in open(os.path.join(DATA, 'upstream-ct_R5005.txt')):
        k, s = l.split()
        o = off[k]
        toks += [s[i:i + 2] for i in range(o, len(s) - 1, 2)]
    assert len(toks) == 1846, len(toks)
    return toks


def load_era_words():
    words = []
    for fn in ('gutenberg-30513-tocqueville-t1.txt',
               'gutenberg-30514-tocqueville-t2.txt'):
        text = open(os.path.join(DATA, fn), encoding='utf-8',
                    errors='replace').read().lower()
        m = re.search(r'\*\*\* start of.*?\*\*\*', text)
        if m:
            text = text[m.end():]
        m = re.search(r'\*\*\* end of.*', text)
        if m:
            text = text[:m.start()]
        words += re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)
    return words


_ERA = None          # word list
_ERA_U = None        # unigram Counter
_ERA_B = None        # bigram Counter (w1 -> Counter(w2))
_ERA_END = None      # ending -> Counter(next word)


def _era_init():
    global _ERA, _ERA_U, _ERA_B, _ERA_END
    if _ERA is not None:
        return
    _ERA = load_era_words()
    _ERA_U = collections.Counter(_ERA)
    _ERA_B = collections.defaultdict(collections.Counter)
    for a, b in zip(_ERA, _ERA[1:]):
        _ERA_B[a][b] += 1
    _ERA_END = collections.defaultdict(collections.Counter)
    for a, b in zip(_ERA, _ERA[1:]):
        for L in (2, 3):
            if len(a) >= L:
                _ERA_END[a[-L:]][b] += 1


def era_unigram(w):
    """P(word), word-space. F30-legal."""
    _era_init()
    return _ERA_U[w] / len(_ERA)


def era_p_next(w2, w1):
    """P(w2|w1) with +0.5 Laplace smoothing over observed vocab. Word-space."""
    _era_init()
    c = _ERA_B[w1][w2]
    tot = sum(_ERA_B[w1].values())
    V = len(_ERA_U)
    return (c + 0.5) / (tot + 0.5 * V)


def era_bigram_n(w1, w2):
    """Raw era bigram count (w1,w2)."""
    _era_init()
    return _ERA_B[w1][w2]


def era_p_after(w, ending):
    """P(w | previous word ends with `ending`), word-space. F30-legal.

    E.g. era_p_after('me', 'er') for the 29=er -> 47 frame.
    """
    _era_init()
    c = _ERA_END[ending][w]
    tot = sum(_ERA_END[ending].values())
    V = len(_ERA_U)
    return (c + 0.5) / (tot + 0.5 * V)


def followers(pairs, g):
    c = collections.Counter()
    for i, x in enumerate(pairs):
        if x == g and i + 1 < len(pairs):
            c[pairs[i + 1]] += 1
    return c


def predecessors(pairs, g):
    c = collections.Counter()
    for i, x in enumerate(pairs):
        if x == g and i > 0:
            c[pairs[i - 1]] += 1
    return c


def windows(pairs, g, r=3):
    out = []
    for i, x in enumerate(pairs):
        if x == g:
            out.append((i, pairs[max(0, i - r):i + r + 1]))
    return out


def ngram_count(pairs, seq):
    L = len(seq)
    return sum(1 for i in range(len(pairs) - L + 1)
               if pairs[i:i + L] == list(seq))


# ---- R1-R4 segmentation enumerator -------------------------------------
# Plausible encipherer cuts of a French word under the recovered rules:
# cells of 1-4 letters; known cells preferred; no uniqueness required.
_KNOWN_CELLS = {'la': '11', 'pre': '70', 'm': '82', 'i': '34', 'er': '29',
                'e': '40', 'que': '46', 'ce': '87', 'qui': '64',
                'par': '96', 'ne': '94'}


def segmentations(word, cells=None, max_cell=4):
    """Yield plausible cut lists for `word` under R1-R4.

    cells: dict cell-text -> group (defaults to known cells). Every
    1-4-letter chunk is a legal cell (R1); known cells are tried first
    (they are attested cuts). Returns list of (cuts, groups-or-None).
    """
    cells = cells or _KNOWN_CELLS
    word = word.lower()
    n = len(word)
    results = []

    def rec(i, acc):
        if i == n:
            results.append(list(acc))
            return
        # known cells first (attested), then generic 1-4 chunks
        cands = []
        for L in range(1, max_cell + 1):
            if i + L <= n:
                chunk = word[i:i + L]
                cands.append((chunk, 0 if chunk in cells else 1))
        cands.sort(key=lambda t: t[1])
        for chunk, _ in cands:
            acc.append((chunk, cells.get(chunk)))
            rec(i + len(chunk), acc)
            acc.pop()

    rec(0, [])
    return results


def frag_legible_as(word, seq, cells=None):
    """True if `word` can be cut (R1-R4) into a cell sequence whose known
    cells match `seq` positionally (None = any cell)."""
    for cuts in segmentations(word, cells):
        if len(cuts) != len(seq):
            continue
        ok = True
        for (chunk, g), want in zip(cuts, seq):
            if want is not None and g != want:
                ok = False
                break
        if ok:
            return True, [c for c, _ in cuts]
    return False, None
