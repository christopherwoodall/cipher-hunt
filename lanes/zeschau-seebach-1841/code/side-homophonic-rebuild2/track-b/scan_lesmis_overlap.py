#!/usr/bin/env python3
"""Les Mis overlap scan for Track B training manifest (R5a provenance).

Deterministic. Builds the word-8-gram set of the Les Mis body
(data/gutenberg-17489-miserables1.txt, Gutenberg boilerplate stripped via
*** START/END *** markers, NFD accent-stripped, lowercased, [a-z]+ words)
and counts hits on each manifest file's trainable body.

Run: python3 scan_lesmis_overlap.py [lane_dir]
Expected (2026-10-07): 13 hits total, all generic pre-1862 French idioms
(see track-b/PREREG.md Amendment A1 for the verbatim list).
"""
import os
import re
import sys
import unicodedata

LANE = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser(
    '~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')

CORPUS = os.path.join(LANE, 'code/side-period/corpus')
DATA = os.path.join(LANE, 'data')

MANIFEST = [
    'guizot-memoires-t5-t6.txt', 'nesselrode-v7.txt', 'nesselrode-v8.txt',
    'nesselrode-v9.txt', 'nesselrode-v10.txt',
    'revue-deux-mondes-1841-q1.txt', 'revue-deux-mondes-1841-q2.txt',
    'revue-deux-mondes-1841-q3.txt', 'revue-deux-mondes-1841-q4.txt',
    'metternich-papiere-v4.txt', 'metternich-papiere-v6.txt',
    'talleyrand-memoires-v1.txt',
]
GUTENBERG = [
    'gutenberg-30513-tocqueville-t1.txt', 'gutenberg-30514-tocqueville-t2.txt',
]
LESMIS = 'gutenberg-17489-miserables1.txt'


def body(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    m1 = re.search(r'\*\*\* START OF.*?\*\*\*', t, re.S)
    m2 = re.search(r'\*\*\* END OF.*?\*\*\*', t, re.S)
    if m1 and m2:
        return t[m1.end():m2.start()]
    return t


def norm_words(txt):
    txt = unicodedata.normalize('NFD', txt.lower())
    txt = ''.join(c for c in txt if unicodedata.category(c) != 'Mn')
    return re.findall(r'[a-z]+', txt)


def eight_grams(words):
    return set(' '.join(words[i:i + 8]) for i in range(len(words) - 7))


def main():
    lesmis_w = norm_words(body(os.path.join(DATA, LESMIS)))
    grams = eight_grams(lesmis_w)
    print(f'lesmis body words: {len(lesmis_w)}, 8-grams: {len(grams)}')
    total = 0
    rows = []
    for f in MANIFEST:
        w = norm_words(body(os.path.join(CORPUS, f)))
        hits = sum(1 for i in range(len(w) - 7)
                   if ' '.join(w[i:i + 8]) in grams)
        rows.append((f, len(w), hits))
        total += hits
    for f in GUTENBERG:
        w = norm_words(body(os.path.join(DATA, f)))
        hits = sum(1 for i in range(len(w) - 7)
                   if ' '.join(w[i:i + 8]) in grams)
        rows.append((f, len(w), hits))
        total += hits
    for f, nw, h in rows:
        print(f'{f:42s} body-words={nw:7d} lesmis-8gram-hits={h}')
    print(f'TOTAL hits on trainable bodies: {total}')
    return total


if __name__ == '__main__':
    main()
