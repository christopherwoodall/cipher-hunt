#!/usr/bin/env python3
"""Pattern index for the Seebach word-pattern re-drive (crowd6/inventorist).

Re-syllabifies the 11,870-word lexicon with the by-ear tiler (byear.py),
builds the (n_cells, pattern) index over ALL contiguous cell subsequences
(tolerates segmenter mis-cuts; implements R7's "tolerate n-mismatch" with an
explicit mechanism), with SMART polyvalence expansion only (R1/R2).

By-ear polyvalence model (F33/F38/F41, re-derived on the repaired 1,847-pair
parse; old 06=/mA~/ model dead per N17, 06 now verb-stem-class + restricted
"ent"):
  cell 'ne'  -> {94} U {G_ne}     (94="ne" prov-strong)
  cell 'en'  -> {94} U {G_en}     (94="en" conditioned islet)
  cell 'pas' -> {52} U {G_pas}    (52="pas" iff negation frame)
  cell 'so'  -> {52} U {G_so}     (52="so" word-internal)
  cell 'se'  -> {52,59} U {G_se}  (52/59="se" split)
  cell 'ent' -> {06} U {G_ent}    (06="ent" restricted to 94-82-06 trigrams)
  cell 'me'  -> {78} U {G_me}     (78="me" syllable LEAD)
  cell 'ver' -> {78} U {G_ver}    (78="ver" iff next=94, conditioned islet)
  cell 'ce'  -> {87,47} U {G_ce}  (87/47="ce" allophony: 1 sound -> 2 groups)
  other cell c -> {G_c}           (unique canonical placeholder per string)

Reachable cipher patterns: all equality-structures obtainable by choosing one
group option per cell. Canonical placeholders for distinct strings are assumed
distinct (unknown further homophony = residual risk, disclosed; same
limitation as the old tester §7).

R8: the by-ear alphabet is orth-based (letter cells, mute-e written per R3);
no phonetic alphabet is built -- R8 satisfied by construction.

Output: index.json (key "n|pattern" -> entries) + meta. Stdlib only.
"""
import json
import os
import itertools
import collections

from byear import tile, load_lexicon, KNOWN

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
OUTD = os.path.join(LANE, 'code', 'crowd6', 'inventorist')

# cell -> set of group options (real group ids as strings; placeholders 'G:<cell>')
POLY = {
    'ne': {'94'},
    'en': {'94'},
    'pas': {'52'},
    'so': {'52'},
    'se': {'52', '59'},
    'ent': {'06'},
    'me': {'78'},
    'ver': {'78'},
    'ce': {'87', '47'},
}


def group_options(cell):
    opts = set(POLY.get(cell, ()))
    opts.add('G:' + cell)
    return opts


def reachable_patterns(cells):
    """All distinct repetition patterns this cell sequence can produce."""
    # per-position group-option lists
    opt_lists = [sorted(group_options(c)) for c in cells]
    # cap blowup: if product too large, sample is NOT allowed (exact only);
    # poly cells are rare, so enumerate fully but guard.
    total = 1
    for o in opt_lists:
        total *= len(o)
    assert total <= 4096, f'combinatorial blowup: {cells} -> {total}'
    pats = set()
    for combo in itertools.product(*opt_lists):
        seen = {}
        out = []
        for g in combo:
            if g not in seen:
                seen[g] = len(seen)
            out.append(chr(65 + seen[g]))
        pats.add(''.join(out))
    return pats


def pattern_of(seq):
    seen = {}
    out = []
    for x in seq:
        if x not in seen:
            seen[x] = len(seen)
        out.append(chr(65 + seen[x]))
    return ''.join(out)


def build(k_tilings=5, min_len=2, max_len=12):
    lex = load_lexicon()
    # word index for compact entries
    words = []          # idx -> (word, freq)
    tilings = []        # idx -> list of cell-lists (top-k)
    for e in lex:
        w = e['w']
        words.append((w, e['freq']))
        ts = tile(w, k=k_tilings)
        tilings.append([c for c, s in ts])

    index = collections.defaultdict(list)  # (n,pattern) -> [(widx, cells, start)]
    n_subseq = 0
    n_reachable_extra = 0
    for widx, tls in enumerate(tilings):
        seen_sub = set()  # dedupe identical (cells,start,n) across tilings
        for cells in tls:
            m = len(cells)
            for start in range(m):
                for end in range(start + min_len, min(m, start + max_len) + 1):
                    sub = tuple(cells[start:end])
                    key0 = (sub, start)
                    if key0 in seen_sub:
                        continue
                    seen_sub.add(key0)
                    n = end - start
                    naive = pattern_of(sub)
                    reach = reachable_patterns(sub)
                    n_subseq += 1
                    n_reachable_extra += len(reach) - 1
                    for pat in reach:
                        index[(n, pat)].append((widx, sub, start))
    print(f'[index] {len(words)} words, {n_subseq} subsequences, '
          f'{n_reachable_extra} extra reachable-pattern filings, '
          f'{len(index)} keys')
    return words, index


def main():
    words, index = build()
    # serialize: keys as "n|pattern"
    ser = {}
    for (n, pat), entries in index.items():
        # entries: (widx, cells_tuple, start) -> [widx, cells_list, start]
        ser[f'{n}|{pat}'] = [[widx, list(cells), start]
                             for widx, cells, start in entries]
    meta = {
        'n_words': len(words),
        'n_keys': len(ser),
        'alphabet': 'by-ear (F44 24-unit inventory + R1-R4 shapes)',
        'subsequence_index': True,
        'polyvalence': 'smart reachable-sets only (R1/R2); naive expansion never',
        'note': 'canonical 1,847-pair parse assumed; R6: rebuild on model/parse/inventory change',
    }
    with open(os.path.join(OUTD, 'byear_index.json'), 'w') as f:
        json.dump({'meta': meta, 'words': words, 'index': ser}, f,
                  ensure_ascii=False)
    print('[wrote] byear_index.json')


if __name__ == '__main__':
    main()
