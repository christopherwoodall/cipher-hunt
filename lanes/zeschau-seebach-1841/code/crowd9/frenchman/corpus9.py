#!/usr/bin/env python3
"""Round-9 FRENCHMAN shared corpus loader. Era standard: Nesselrode v8
despatches_primary (nesselrode-v8.txt + levant-correspondence-1841-p3.txt),
elision-split tokenizer per F53. diplomatic_all available for collocations."""
import re, glob, os, collections
from pathlib import Path

LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
CORP = LANE / 'code/side-period/corpus'
PRIMARY = ['nesselrode-v8.txt', 'levant-correspondence-1841-p3.txt']

def tokenize_elision(text):
    text = text.replace('-\n', '').replace('-\r\n', '')
    text = text.lower()
    text = re.sub(r"[’‘`]", "'", text)
    text = re.sub(r"\b([a-zàâäéèêëîïôöùûüçœæ]+)'([a-zàâäéèêëîïôöùûüçœæ]+)", r"\1' \2", text)
    return re.findall(r"[a-zàâäéèêëîïôöùûüçœæ]+'?|[a-zàâäéèêëîïôöùûüçœæ]+", text)

_cache = {}
def load(names='primary'):
    key = names
    if key in _cache:
        return _cache[key]
    if names == 'primary':
        files = [CORP / f for f in PRIMARY]
    elif names == 'all':
        files = [f for f in sorted(CORP.glob('*.txt'))]
    toks = []
    for f in files:
        toks.extend(tokenize_elision(open(f, encoding='utf-8', errors='replace').read()))
    _cache[key] = toks
    return toks

def counters(names='primary'):
    t = load(names)
    return collections.Counter(t), collections.Counter(zip(t, t[1:])), \
           collections.Counter(zip(t, t[1:], t[2:]))

def ngram_count(names, *words):
    t = load(names)
    n = len(words)
    return sum(1 for i in range(len(t)-n+1) if tuple(t[i:i+n]) == tuple(words))

def kwic(names, word, width=6, limit=25):
    t = load(names)
    out = []
    for i, w in enumerate(t):
        if w == word and len(out) < limit:
            out.append(' '.join(t[max(0,i-width):i+width+1]))
    return out
