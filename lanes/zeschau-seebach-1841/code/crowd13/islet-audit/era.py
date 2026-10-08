#!/usr/bin/env python3
"""Era-corpus helpers for the round-13 islet audit.

Clean pool: the diplomatic-period corpus MINUS nesselrode-v8 (VOID for
phrase queries per work order — OCR word-splits) and MINUS the German
Allgemeine Zeitung issues (register-mismatched for French phrases).
"""
import collections, os, re

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
C = os.path.join(LANE, 'code', 'side-period', 'corpus')

POOL = ['nesselrode-v7.txt', 'nesselrode-v9.txt', 'nesselrode-v10.txt',
        'pozzo-di-borgo-correspondance-v1.txt',
        'levant-correspondence-1841-p3.txt',
        'guizot-memoires-t1-gutenberg.txt', 'guizot-memoires-t2-gutenberg.txt',
        'guizot-memoires-t3-gutenberg.txt', 'guizot-memoires-t5-t6.txt',
        'metternich-papiere-v4.txt', 'metternich-papiere-v6.txt',
        'talleyrand-memoires-v1.txt',
        'revue-deux-mondes-1841-q1.txt', 'revue-deux-mondes-1841-q2.txt',
        'revue-deux-mondes-1841-q3.txt', 'revue-deux-mondes-1841-q4.txt']

def era_words():
    words = []
    for fn in POOL:
        txt = open(os.path.join(C, fn), encoding='utf-8',
                   errors='replace').read().lower()
        txt = txt.replace('\u2019', "'").replace('\u2018', "'")
        txt = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])",
                     r'\1 \2', txt)
        words += re.findall(r'[a-z\u00e0-\u00ff]+', txt)
    return words

def counts(words):
    return (len(words), collections.Counter(words),
            collections.Counter(zip(words, words[1:])))
