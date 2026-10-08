#!/usr/bin/env python3
"""Shared era instrument: clean French pool (14 files, 3,212,595 tokens),
lane tokenizer verbatim. v8-VOID rule: no v8-only OCR attestation counts."""
import re, collections
from pathlib import Path
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
C = LANE / 'code/side-period/corpus'
FR = ['nesselrode-v7.txt', 'nesselrode-v8.txt', 'nesselrode-v9.txt', 'nesselrode-v10.txt',
      'pozzo-di-borgo-correspondance-v1.txt',
      'guizot-memoires-t1-gutenberg.txt', 'guizot-memoires-t2-gutenberg.txt',
      'guizot-memoires-t3-gutenberg.txt', 'guizot-memoires-t5-t6.txt',
      'talleyrand-memoires-v1.txt',
      'revue-deux-mondes-1841-q1.txt', 'revue-deux-mondes-1841-q2.txt',
      'revue-deux-mondes-1841-q3.txt', 'revue-deux-mondes-1841-q4.txt']

def tokenize(t):
    t = t.lower()
    t = re.sub(r"[’‘`]", "'", t)
    t = re.sub(r"\b([a-zàâäéèêëîïôöùûüç]+)'([a-zàâäéèêëîïôöùûüç]+)", r"\1' \2", t)
    return re.findall(r"[a-zàâäéèêëîïôöùûüç]+'?|[a-zàâäéèêëîïôöùûüç]+", t)

_TOKS = None
def toks():
    global _TOKS
    if _TOKS is None:
        out = []
        for f in FR:
            out += tokenize(open(C / f, encoding='utf-8', errors='replace').read())
        _TOKS = out
    return _TOKS

def bigram(a, b):
    t = toks()
    return sum(1 for x, y in zip(t, t[1:]) if x == a and y == b)

def trigram_mid(a, c):
    """All (a, *, c) trigrams: returns Counter of middle tokens + total."""
    t = toks()
    mid = collections.Counter()
    for x, y, z in zip(t, t[1:], t[2:]):
        if x == a and z == c:
            mid[y] += 1
    return mid

def bigram_suc_ending(a, suffix):
    t = toks()
    n = 0
    ex = []
    for x, y in zip(t, t[1:]):
        if x == a and y.endswith(suffix):
            n += 1
            if len(ex) < 5:
                ex.append(y)
    return n, ex
