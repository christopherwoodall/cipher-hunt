#!/usr/bin/env python3
"""Period-drag common engine — Seebach cipher-hunt round 6 (period drag runner).

Drags red-team-adjudicated period crib cards against the canonical 1,847-pair
repaired stream using the crib-learned F44 24-unit by-ear alphabet
(code/crowd6/inventorist/byear.py) — NOT standard-French syllabification.

Anchor-preserving controls (N34 lesson): the null for every drag is counted
against the SAME window with the SAME anchor set — lexicon words whose
by-ear tilings also fit. Anchors are never shuffled away.

Anchor statuses (STATE.md, round-6 redteam rulings):
  GT (pencil):  11=la 70=pre 82=m 34=i 29=er 40=e 46=que
  PROV:         87=ce (strengthened) 64=qui 96=par (confirmed-inheriting)
                94=ne (prov-strong)
  77=le:        provisional-CONDITIONED (F37) — the gou@1180/@1351 exception is
                FENCED, so 77 is FREE (not hard) inside the T4 windows.
  ISLETS (F33 conditioned polyvalence): 47={ce} 52={pas,so,se} 59={se}
                78={me,ver} 94={ne,en}
  06:           verb-stem-class provisional, no string; 'ent' allowed as a
                hypothesis cell only inside the fenced trigram scope
                (94-82-06 @578/@1182/@1353 — the T4 windows are two of them).
Anti-collision: never drag "premier"/"première" (red-team enforced).
"""
import json
import os
import sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'inventorist'))
from repaired_parse import load_pairs_repaired  # noqa: E402
from byear import tile as byear_tile  # noqa: E402

GT = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i', '29': 'er',
      '40': 'e', '46': 'que'}
PROV = {'87': 'ce', '64': 'qui', '96': 'par', '94': 'ne'}
# 77=le is provisional-CONDITIONED; hard everywhere EXCEPT the fenced T4 windows
LE77 = {'77': 'le'}
ISLETS = {'47': {'ce'}, '52': {'pas', 'so', 'se'}, '59': {'se'},
          '78': {'me', 'ver'}, '94': {'ne', 'en'}}

PAIRS, _, _ = load_pairs_repaired()


def fit_cells(cells, groups, hard, free=frozenset()):
    """Check one tiling (list of cell strings) against a window of groups.

    hard: dict group->required cell string. free: groups exempt from hard
    (their reading is recorded, not constrained). Islet groups may take any
    of their conditioned readings. Returns (ok, notes_dict).
    """
    notes = {'overrides': [], 'islet_reads': [], 'free_reads': {},
             'collisions': []}
    if len(cells) != len(groups):
        return False, notes
    cell_of_group = {}
    for g, cell in zip(groups, cells):
        if g in cell_of_group and cell_of_group[g] != cell:
            return False, notes  # same group, two cells in one window
        cell_of_group[g] = cell
        if g in free:
            notes['free_reads'][g] = cell
            continue
        if g in hard:
            if cell == hard[g]:
                continue
            if g in ISLETS and cell in ISLETS[g]:
                notes['islet_reads'].append((g, cell))
                continue
            notes['overrides'].append((g, hard[g], cell))
            return False, notes
        if g in ISLETS and cell not in ISLETS[g]:
            return False, notes
    # collision flag: one non-islet cell string on 2+ groups (polyvalence is
    # real in this cipher, so flag not fail)
    inv = {}
    for g, cell in cell_of_group.items():
        inv.setdefault(cell, set()).add(g)
    for cell, gs in inv.items():
        if len(gs) > 1 and not any(g in ISLETS for g in gs):
            notes['collisions'].append((cell, sorted(gs)))
    return True, notes


def drag_word(word, groups, hard, free=frozenset(), manual=()):
    """Drag one candidate word at a window.

    Tilings = by-ear tiler top-8 UNION manual fused/split variants.
    Returns list of (cells, notes) fits.
    """
    tilings = []
    seen = set()
    for cells, _score in byear_tile(word, k=8):
        t = tuple(cells)
        if t not in seen:
            seen.add(t)
            tilings.append(cells)
    for cells in manual:
        t = tuple(cells)
        if t not in seen:
            seen.add(t)
            tilings.append(list(cells))
    fits = []
    for cells in tilings:
        ok, notes = fit_cells(cells, groups, hard, free)
        if ok:
            fits.append((cells, notes))
    return fits


# ---- lexicon null (anchor-preserving) ----
LEXCACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'lexicon_tilings.json')


def load_lexicon_tilings():
    """{word: [tilings]} for the 11,870-word fleet lexicon (cached)."""
    if os.path.exists(LEXCACHE):
        return json.load(open(LEXCACHE))
    idx = json.load(open(os.path.join(
        LANE, 'code', 'crowd6', 'inventorist', 'byear_index.json')))
    out = {}
    words = [w for w, _f in idx['words']]
    for n, w in enumerate(words):
        try:
            ts = [cells for cells, _s in byear_tile(w, k=8)]
        except Exception:
            ts = []
        out[w] = ts
        if (n + 1) % 2000 == 0:
            print(f'  tiled {n + 1}/{len(words)}', flush=True)
    json.dump(out, open(LEXCACHE, 'w'))
    return out


def null_rate(groups, hard, free=frozenset(), lex=None):
    """Anchor-preserving null: #lexicon words with >=1 fitting tiling.

    Same window, same anchor set — anchors are NOT shuffled (N34).
    Returns (n_fit, n_total, fit_words_sample).
    """
    if lex is None:
        lex = load_lexicon_tilings()
    n_fit = 0
    sample = []
    for w, tilings in lex.items():
        for cells in tilings:
            ok, _ = fit_cells(cells, groups, hard, free)
            if ok:
                n_fit += 1
                if len(sample) < 12:
                    sample.append(w)
                break
    return n_fit, len(lex), sample
