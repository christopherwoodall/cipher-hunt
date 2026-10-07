#!/usr/bin/env python3
"""Shared harness for the Round-7 search-family prototype (work order 8).

Builds the REPAIRED joint objective (code/crowd6/scorer/objective.py —
owned by the Scorer Smith; imported, never modified) over FRESH synthetic
control instances (fresh/, seeds 184207-184212, same certified design as
code/side-homophonic/control/).

The search scripts import this module. NOTHING here reads
SYNTHETIC-key-*.json (sealed). Scoring lives in score_fresh.py.

Frozen objective hyperparameters (from code/crowd6/scorer/step4_calibrated.json):
  LAM_POLY=0.05, LAM_CONC=3.58e-4, LAM_WORD=1.0, LAM_ROT=0.0 (phase held out),
  CONC_CAP=3 (raw cells), N_GRAM=7, inventory=top-600 rule units + letters.
  prov={} (the side-homophonic controls have no soft hints; their solver
  disabled soft priors on controls too).
"""
import collections
import json
import math
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
for p in (os.path.join(LANE, 'code'),
          os.path.join(LANE, 'code', 'crowd2'),
          os.path.join(LANE, 'code', 'crowd4'),
          os.path.join(LANE, 'code', 'crowd6', 'scorer')):
    if p not in sys.path:
        sys.path.insert(0, p)

from scorer_smith import build_models  # noqa: E402
from joint_engine import build_inventory  # noqa: E402
from objective import (build_letter_ngram_proj, build_lexicon_proj,  # noqa: E402
                       AhoCorasick, RepairedModel, PINS, CONC_CAP, N_GRAM)

FRESH = json.load(open(os.path.join(HERE, 'fresh', 'build_summary.json')))
FRESH_SEEDS = FRESH['seeds']
INST = os.path.join(HERE, 'fresh', 'instances')
SPAN = (40000, 41100)  # control span excluded from the letter model/lexicon
# (same exclusion as the lane scorer; fresh plaintext is Les Mis — no overlap)

CAL = json.load(open(os.path.join(LANE, 'code', 'crowd6', 'scorer',
                                  'step4_calibrated.json')))
LAM_POLY = CAL['LAM_POLY']
LAM_CONC = CAL['LAM_CONC']
assert LAM_POLY > 0 and LAM_CONC > 0, 'calibration missing'

_CACHE = {}


def get_models(verbose=True):
    """Letter 7-gram (projected, span-excluded), projected lexicon + AC,
    cell inventory. Cached per process."""
    if _CACHE:
        return _CACHE
    t0 = time.time()
    log = (lambda *a: print('[harness]', *a, flush=True)) if verbose else (
        lambda *a: None)
    log('build_models...')
    M = build_models()
    log('projected letter 7-gram (span excluded)...')
    LP_PROJ, n_letters = build_letter_ngram_proj(M['toks'], n=N_GRAM,
                                                 exclude=SPAN)
    log('projected lexicon (span excluded)...')
    LEX = build_lexicon_proj(M['toks'], exclude=SPAN)
    log('Aho-Corasick over %d patterns...' % len(LEX))
    AC = AhoCorasick(LEX)
    log('inventory (top-600 rule units + letters)...')
    CELLS, WEIGHTS = build_inventory(M)
    _CACHE.update({'LP_PROJ': LP_PROJ, 'LEX': LEX, 'AC': AC, 'CELLS': CELLS,
                   'WEIGHTS': WEIGHTS, 'n_letters': n_letters,
                   'elapsed_s': round(time.time() - t0, 1)})
    log('done in %.0fs; lexicon=%d inventory=%d letters=%d'
        % (time.time() - t0, len(LEX), len(CELLS), n_letters))
    return _CACHE


def load_instance(seed):
    """Solver-visible instance data ONLY: pair stream + crib anchors."""
    seed = str(seed)
    assert seed in [str(s) for s in FRESH_SEEDS], 'not a fresh seed'
    lines = open(os.path.join(INST, 'SYNTHETIC-ct-%s.pairs.txt' % seed)).read().splitlines()
    pairs = []
    for ln in lines:
        if ln.startswith('#') or not ln.strip():
            continue
        pairs.extend(ln.split())
    crib = json.load(open(os.path.join(INST, 'SYNTHETIC-crib-%s.json' % seed)))
    return {'seed': seed, 'stream': pairs, 'anchors': crib['anchors']}


def make_model(stream, seed=0, lam_word=1.0, lam_rot=0.0,
               lam_poly=None, lam_conc=None, verbose=False):
    """RepairedModel on a stream. Phase term held out (LAM_ROT=0.0) per the
    frozen config — phases passed as a dummy uniform map."""
    M = get_models(verbose=verbose)
    phase = {g: 'A' for g in set(stream)}  # dummy; term held out
    return RepairedModel(
        stream, phase, M['LP_PROJ'], PINS, {}, M['CELLS'], M['WEIGHTS'],
        M['AC'], lam_poly=LAM_POLY if lam_poly is None else lam_poly,
        lam_conc=LAM_CONC if lam_conc is None else lam_conc,
        lam_word=lam_word, lam_rot=lam_rot, conc_cap=CONC_CAP, n=N_GRAM,
        rng=random.Random(seed))


def decode_key(v1):
    """Best-key primary map -> JSON-serializable dict."""
    return {g: v for g, v in v1.items()}


if __name__ == '__main__':
    # smoke: load models, one instance, one total() timing
    t0 = time.time()
    M = get_models()
    inst = load_instance(FRESH_SEEDS[0])
    m = make_model(inst['stream'], seed=1)
    m.init_key()
    t1 = time.time()
    s = m.total()
    t2 = time.time()
    print('init+total: %.2fs; total() recompute: %.2fs; score=%.3f'
          % (t1 - t0, t2 - t1, s))
    print('stream=%d pairs, %d groups' % (len(inst['stream']),
                                          len(set(inst['stream']))))
