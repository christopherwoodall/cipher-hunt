#!/usr/bin/env python3
"""TRACK-C §4 hygiene gate: Les-Mis contamination check.

Extracts projected 15-grams (token stream) from the §2.2 reference corpus
and counts distinct 15-grams also present in data/gutenberg-17489-miserables1.txt
(projected identically).

Gate (PREREG §4):
  0 matches        -> proceed to scoring
  1-5 matches      -> report the matches; proceed only if all generic
  >5 distinct      -> KILL: do not score; report to red team

Deterministic; no RNG. Exit code 0 = proceed, 2 = KILL, 3 = needs review.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(LANE, 'code', 'side-homophonic-rebuild', 'solver'))
from phonetics import project  # noqa: E402

CORPUS_DIR = os.path.join(LANE, 'code', 'side-period', 'corpus')
FILES = ['nesselrode-v7.txt', 'nesselrode-v8.txt', 'nesselrode-v9.txt',
         'nesselrode-v10.txt', 'pozzo-di-borgo-correspondance-v1.txt']
MISERABLES = os.path.join(LANE, 'data', 'gutenberg-17489-miserables1.txt')
WORD_RE = re.compile(r"[A-Za-zÀ-ÿŒœÆæ]+")
K = 15


def token_stream(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    toks = []
    for t in WORD_RE.findall(raw):
        w = project(t)
        if w:
            toks.append(w)
    return toks


def ngrams(toks, k):
    return {' '.join(toks[i:i + k]) for i in range(len(toks) - k + 1)}


def main():
    corp_toks = []
    for fn in FILES:
        corp_toks += token_stream(os.path.join(CORPUS_DIR, fn))
    print(f'corpus tokens: {len(corp_toks)}')
    corp_grams = ngrams(corp_toks, K)
    print(f'corpus distinct {K}-grams: {len(corp_grams)}')
    mis_toks = token_stream(MISERABLES)
    print(f'les-mis tokens: {len(mis_toks)}')
    mis_grams = ngrams(mis_toks, K)
    print(f'les-mis distinct {K}-grams: {len(mis_grams)}')
    shared = corp_grams & mis_grams
    print(f'shared distinct {K}-grams: {len(shared)}')
    out = {'corpus_tokens': len(corp_toks),
           'corpus_distinct_15grams': len(corp_grams),
           'miserables_tokens': len(mis_toks),
           'shared_distinct_15grams': len(shared),
           'shared': sorted(shared)[:50]}
    with open(os.path.join(HERE, 'hygiene_gate.json'), 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    for g in sorted(shared)[:20]:
        print('  SHARED:', g)
    if len(shared) == 0:
        print('GATE: PASS (0 matches) -> proceed to scoring')
        return 0
    if len(shared) <= 5:
        print('GATE: REVIEW (1-5 matches) -> manual generic-phrase check required')
        return 3
    print('GATE: KILL (>5 matches) -> DO NOT SCORE')
    return 2


if __name__ == '__main__':
    sys.exit(main())
