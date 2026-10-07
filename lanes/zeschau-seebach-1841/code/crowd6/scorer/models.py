#!/usr/bin/env python3
"""Shared model loading for the round-6 repaired-objective scripts.

Builds once per process: projected letter 7-gram (control span excluded),
projected lexicon + Aho-Corasick (span excluded), control-consistent
inventory. Call get_models() — cached in the module global.
"""
import json
import os
import sys
import time

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
for p in (os.path.join(LANE, 'code'),
          os.path.join(LANE, 'code', 'crowd2'),
          os.path.join(LANE, 'code', 'crowd4'),
          os.path.join(LANE, 'code', 'crowd6', 'scorer')):
    if p not in sys.path:
        sys.path.insert(0, p)
from scorer_smith import build_models  # noqa: E402
from joint_engine import build_inventory  # noqa: E402
from objective import (build_letter_ngram_proj, build_lexicon_proj,
                       AhoCorasick, PINS)  # noqa: E402

OUTD = os.path.join(LANE, 'code', 'crowd6', 'scorer')
SPAN = (40000, 41100)
_CACHE = {}


def get_models(verbose=True):
    if _CACHE:
        return _CACHE
    t0 = time.time()
    log = (lambda *a: print('[models]', *a, flush=True)) if verbose else (
        lambda *a: None)
    log('build_models...')
    M = build_models()
    log('projected letter 7-gram (span excluded)...')
    LP_PROJ, n_letters = build_letter_ngram_proj(M['toks'], n=7, exclude=SPAN)
    log('projected lexicon (span excluded)...')
    LEX = build_lexicon_proj(M['toks'], exclude=SPAN)
    log('Aho-Corasick over %d patterns...' % len(LEX))
    AC = AhoCorasick(LEX)
    log('inventory (top-600 rule units + letters)...')
    CELLS, WEIGHTS = build_inventory(M)
    GT = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                     'control_ground_truth.json')))
    assert GT.get('SYNTHETIC') is True
    meta = {'span_excluded': list(SPAN),
            'projected_letters_trained': n_letters,
            'lexicon_size': len(LEX),
            'lexicon_top5': [(w, round(wt, 2)) for w, wt in LEX[:5]],
            'inventory': len(CELLS),
            'elapsed_s': round(time.time() - t0, 1)}
    json.dump(meta, open(os.path.join(OUTD, 'models_meta.json'), 'w'), indent=1)
    log('done in %.0fs; lexicon=%d inventory=%d' % (
        time.time() - t0, len(LEX), len(CELLS)))
    _CACHE.update({'M': M, 'LP_PROJ': LP_PROJ, 'LEX': LEX, 'AC': AC,
                   'CELLS': CELLS, 'WEIGHTS': WEIGHTS, 'GT': GT,
                   'SPAN': SPAN, 'meta': meta})
    return _CACHE


if __name__ == '__main__':
    m = get_models()
    print(json.dumps(m['meta'], indent=1))
