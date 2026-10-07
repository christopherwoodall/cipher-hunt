#!/usr/bin/env python3
"""STEPS 1-3 attribution — score the TRUTH key under repaired components.

(1) lam_poly: re-derived in step0 (crossover on the old objective).
(2) phonetic projection: truth key's s_let on raw 7-gram vs projected 7-gram
    (expect ~+0.33/letter, the measured ear-noise cost).
(3) word bonus: per-letter S_word on the truth decode (longest-match
    deduped, spanning-only) — and, for contrast, on a degenerate
    'meme'-collapse decode to show the D2 repair working.

Writes step123_truth.json. No search; pure scoring of the sealed truth.
"""
import json
import os
import random
import sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'scorer'))
from models import get_models  # noqa: E402
from objective import RepairedModel, PINS, SEED  # noqa: E402
from phonetics import project  # noqa: E402

OUTD = os.path.join(LANE, 'code', 'crowd6', 'scorer')
OUTJ = os.path.join(OUTD, 'step123_truth.json')
RES = {'SYNTHETIC': True}


def log(*a):
    print('[step123]', *a, flush=True)


M = get_models(verbose=False)
GT = M['GT']
GS, EMITTED, GI = GT['stream'], GT['emitted'], GT['group_info']
HINTS, ISLETS = GT['hints'], GT['islets']
BLOCK = {g: v['phase'] for g, v in GI.items()}


def truth_key(m, with_poly=True):
    for g in m.groups:
        m.v1[g] = GI[g]['primary']
        if with_poly and GI[g]['secondary']:
            m.v2[g] = GI[g]['secondary']
            m.w2[g] = GI[g]['w2']
        else:
            m.v2[g] = None
            m.w2[g] = 0.0
    m.pcell = list(EMITTED)
    m._refresh_scores()
    return m


log('truth key under repaired objective (lam_poly=0, lam_conc=0)...')
m = RepairedModel(GS, BLOCK, M['LP_PROJ'], PINS, HINTS, M['CELLS'],
                  M['WEIGHTS'], M['AC'], lam_word=1.0, lam_rot=0.0,
                  lam_poly=0.0, lam_conc=0.0, rng=random.Random(SEED))
truth_key(m, True)
c = m.components()
log('truth components:', c)
RES['truth_repaired_lam0'] = c

# (2) projection gain: raw s_let (from step0) vs projected s_let (here)
# step0's truth s_let is recorded separately; the delta is computed in
# the final report. Record the projected value and the emitted-decode
# projected letter count.
RES['projection'] = {
    's_let_proj_truth': c['s_let_proj'],
    'projected_letters': m.total_letters,
    'note': 'compare vs step0 truth s_let (raw); delta ~= ear-noise cost',
}

# (3) word bonus on truth decode, and on a degenerate collapse decode
# degenerate: map every non-pin group to 'me' (the D2 attractor)
log('degenerate meme-collapse decode under the D2-repaired bonus...')
m2 = RepairedModel(GS, BLOCK, M['LP_PROJ'], PINS, HINTS, M['CELLS'],
                   M['WEIGHTS'], M['AC'], lam_word=1.0, lam_rot=0.0,
                   lam_poly=0.0, lam_conc=0.0, rng=random.Random(SEED))
for g in m2.groups:
    if g not in PINS:
        m2.v1[g] = 'me'
        m2.v2[g] = None
        m2.w2[g] = 0.0
    else:
        m2.v1[g] = PINS[g]
        m2.v2[g] = None
        m2.w2[g] = 0.0
m2._recompute_all()
c2 = m2.components()
log('meme-collapse components:', c2)
RES['meme_collapse'] = c2
# concentration that the collapse would pay (for the lam_conc calibration)
import collections
ncp = collections.Counter(project(m2.v1[g]) for g in m2.groups)
top = ncp.most_common(5)
RES['meme_collapse']['top_projected_conc'] = [(p, n) for p, n in top]
RES['meme_collapse']['sum_max0_n_minus_6_sq'] = sum(
    max(0, n - 6) ** 2 for n in ncp.values())

# what would the OLD (frozen, overlapping-hit) word bonus have paid the
# collapse? approximate: count all overlapping hits (no dedupe)
text = ''.join(project(v) for v in m2.pcell)
overlap = sum(w for _, _, w in M['AC'].scan(text)) / len(text)
RES['meme_collapse']['S_word_overlapping_frozen_style'] = round(overlap, 4)
RES['meme_collapse']['note'] = (
    'overlapping-hit style (side fleet frozen bug) vs longest-match dedupe: '
    'the dedupe must collapse the degenerate profit')

json.dump(RES, open(OUTJ, 'w'), indent=1)
log('wrote step123_truth.json')
