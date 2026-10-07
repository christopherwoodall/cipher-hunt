#!/usr/bin/env python3
"""TRACK-C: build word statistics from the diplomatic-French reference corpus.

REFERENCE-ONLY step (public-domain corpus; no sealed data, no truth/salad
comparison). Produces word_stats.json consumed by the boundary-aware score
defined in PREREG.md. Deterministic.

Corpus (French diplomatic correspondence, all pre-1862 => Les Mis
impossible):
  nesselrode-v7/v8/v9/v10.txt, pozzo-di-borgo-correspondance-v1.txt
Tokenization: regex letter-runs -> phonetics.project() (the lane's shared
phonetic-class space; decode strings are already projected inventory values,
so they are used AS-IS).
"""
import hashlib
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(LANE, 'code', 'side-homophonic-rebuild', 'solver'))
from phonetics import project  # noqa: E402

CORPUS_DIR = os.path.join(LANE, 'code', 'side-period', 'corpus')
FILES = [
    'nesselrode-v7.txt',
    'nesselrode-v8.txt',
    'nesselrode-v9.txt',
    'nesselrode-v10.txt',
    'pozzo-di-borgo-correspondance-v1.txt',
]
WORD_RE = re.compile(r"[A-Za-zÀ-ÿŒœÆæ]+")
MIN_COUNT = 2          # types kept in V
ALPHA = 1.0            # add-alpha for P_uni
BETA = 1.0             # add-beta for L(len)
MAXWLEN = 20           # DP word-length cap; bin 20 = 20+


def main():
    files = []
    tok_counts = Counter()
    len_counts = Counter()
    n_raw = 0
    for fn in FILES:
        p = os.path.join(CORPUS_DIR, fn)
        raw = open(p, encoding='utf-8', errors='replace').read()
        h = hashlib.sha256(raw.encode('utf-8')).hexdigest()
        toks = WORD_RE.findall(raw)
        n_raw += len(toks)
        for t in toks:
            w = project(t)
            if not w:
                continue
            tok_counts[w] += 1
            if len(w) <= MAXWLEN:
                len_counts[len(w)] += 1
            else:
                len_counts[MAXWLEN] += 1  # overflow bin 20 = 20+
        files.append({'file': fn, 'sha256': h, 'bytes': len(raw.encode('utf-8')),
                      'raw_tokens': len(toks)})
    N = sum(tok_counts.values())
    V_full = len(tok_counts)
    vocab = {w: c for w, c in tok_counts.items() if c >= MIN_COUNT}
    V = len(vocab)
    C_letters = sum(len(w) * c for w, c in tok_counts.items())
    rho = N / C_letters  # expected words per projected char
    # length distribution (add-beta over bins 1..20)
    L = {k: (len_counts.get(k, 0) + BETA) / (N + BETA * MAXWLEN)
         for k in range(1, MAXWLEN + 1)}
    out = {
        'provenance': {
            'corpus_dir': 'code/side-period/corpus',
            'files': files,
            'tokenizer': 'regex [A-Za-zÀ-ÿŒœÆæ]+ -> phonetics.project() (defaults, silent_finals=True)',
            'note': 'all files pre-1862 (Les Mis, 1862, temporally impossible in corpus)',
            'seeds': 'deterministic (no RNG)',
        },
        'params': {'min_count': MIN_COUNT, 'alpha': ALPHA, 'beta': BETA,
                   'max_word_len': MAXWLEN},
        'N_tokens': N,
        'C_letters': C_letters,
        'V_types_ge2': V,
        'V_types_ge1': V_full,
        'rho_words_per_char': rho,
        'mean_word_len': 1 / rho,
        'top20': tok_counts.most_common(20),
        'len_dist': {str(k): L[k] for k in range(1, MAXWLEN + 1)},
        'len_counts_raw': {str(k): len_counts.get(k, 0) for k in range(1, MAXWLEN + 1)},
    }
    with open(os.path.join(HERE, 'word_stats.json'), 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    # also stash the vocab counts for the scorer (separate file, keeps stats readable)
    with open(os.path.join(HERE, 'word_vocab.json'), 'w') as f:
        json.dump({'N': N, 'V': V, 'alpha': ALPHA, 'counts': vocab}, f, ensure_ascii=False)
    print(f'N={N} tokens, V(>=2)={V}, V(>=1)={V_full}')
    print(f'rho={rho:.6f} words/char, mean_len={1/rho:.3f}')
    print('top20:', [(w, c) for w, c in tok_counts.most_common(20)])
    print('len dist 1..10:', {k: round(L[k], 4) for k in range(1, 11)})


if __name__ == '__main__':
    main()
