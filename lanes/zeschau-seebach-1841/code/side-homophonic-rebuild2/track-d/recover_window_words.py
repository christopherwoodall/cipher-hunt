#!/usr/bin/env python3
"""TRACK-D: recover the exact Les Mis word list behind each truth decode.

Replicates the generator's deterministic prefix (tokens -> scrub -> crib
plant -> cell pipeline -> inventory fixpoint -> kept words), then locates
the 1846-pair window via the unique crib cell sequence
[la,pre,m,i,er,e]: w0 = crib_cell_idx - crib_pair_offset.
Pair offsets == kept-cell-stream offsets (1 pair per cell).

Outputs window_words_<seed>.txt (original words, one per line) for the
operator's paraphrase step. Diagnostic only; no scoring.
"""
import collections
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(LANE, 'code', 'side-homophonic', 'control'))
import generator as G  # noqa: E402  (module-level is import-safe)

SEEDS = ['184101', '184102', '184103', '184104', '184105', '184106']
T = 56


def window_words(seed):
    crib = json.load(open(os.path.join(
        LANE, 'code', 'side-homophonic', 'control', 'instances',
        f'SYNTHETIC-crib-{seed}.json')))
    co = crib['crib_word_offset']
    crib_pair_offset = crib['crib_pair_offset']
    p = dict(G.PARAMS)
    tokens = G.load_lesmis_tokens()
    idx = SEEDS.index(seed)
    sl = p['slice_words']
    words = tokens[idx * sl:(idx + 1) * sl]
    words = [w for w in words if w != 'première']
    words = words[:co] + ['la', 'première'] + words[co:]
    crib_word_idx = co

    rng = random.Random(int(seed) * 31 + co)
    word_cells = []
    for wi, w in enumerate(words):
        if wi == crib_word_idx + 1:
            cells = list(G.CRIB_CELLS[1:])
        else:
            if (len(w) > 3 and w.endswith('er')
                    and rng.random() < p['p_er_free']):
                cells = G.syllabify(w[:-2]) + ['er']
            else:
                cells = G.syllabify(w)
            if rng.random() < p['p_letter_split']:
                cells = G.encipher_split(cells)
            if wi != crib_word_idx:
                cells = G.ear_noise(cells, rng, p)
        if cells:
            word_cells.append((wi, cells))

    cfreq = collections.Counter(c for _, cells in word_cells for c in cells)
    for a in G.ANCHOR_CELLS:
        assert cfreq[a] > 0
    ranked = [c for c, _ in cfreq.most_common() if c not in G.ANCHOR_CELLS]
    inv_nonanchor = ranked[:T]
    for _round in range(10):
        inventory = set(inv_nonanchor) | G.ANCHOR_CELLS
        kept = []
        for wi, cells in word_cells:
            ok = all(c in inventory for c in cells) or \
                wi in (crib_word_idx, crib_word_idx + 1)
            if ok:
                kept.append((wi, cells))
        kc = collections.Counter(c for _, cells in kept for c in cells)
        drop = [c for c in inv_nonanchor if kc[c] == 0]
        if not drop:
            break
        inv_nonanchor = [c for c in inv_nonanchor if c not in drop]

    # full kept-cell stream with word index per cell
    stream = []  # (wi, cell)
    for wi, cells in kept:
        for c in cells:
            stream.append((wi, c))
    cells_only = [c for _, c in stream]
    # locate the unique crib cell sequence
    want = G.CRIB_CELLS
    hits = [i for i in range(len(cells_only) - 5)
            if cells_only[i:i + 6] == want]
    assert len(hits) == 1, f'{seed}: crib seq hits={len(hits)}'
    w0 = hits[0] - crib_pair_offset
    assert w0 >= 0, f'{seed}: w0={w0} negative'
    win = stream[w0:w0 + 1846]
    assert len(win) == 1846
    wis = sorted(set(wi for wi, _ in win))
    return words, wis, w0, len(stream)


def main():
    for seed in SEEDS:
        words, wis, w0, nstream = window_words(seed)
        out = os.path.join(HERE, f'window_words_{seed}.txt')
        with open(out, 'w') as f:
            f.write(' '.join(words[wi] for wi in wis))
        print(f'{seed}: w0={w0} stream={nstream} words=[{wis[0]}..{wis[-1]}] '
              f'nwords={len(wis)} -> {out}')


if __name__ == '__main__':
    main()
