#!/usr/bin/env python3
"""Round-7 frenchman shared utils: repaired parse + era (Tocqueville) word space."""
import json, re, collections
from pathlib import Path
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
DATA = LANE / 'data'

def load_repaired():
    rows = []
    for line in open(DATA / 'upstream-ct_R5005.txt'):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        rows.append((lid, re.sub(r'\D', '', digits)))
    off = json.loads((LANE / 'code/side-keyhunt/repaired_offsets.json').read_text())
    pairs = []
    for lid, digits in rows:
        o = off[lid]
        pairs += [digits[i:i+2] for i in range(o, len(digits)-1, 2)]
    p = [int(g) for g in pairs]
    assert len(p) == 1847
    return p

PAIRS = load_repaired()
N = len(PAIRS)
UNI = collections.Counter(PAIRS)
BIG = collections.Counter(zip(PAIRS[:-1], PAIRS[1:]))
GT = {11: 'la', 70: 'pre', 82: 'm', 34: 'i', 29: 'er', 40: 'e', 46: 'que'}

def positions(g):
    return [i for i in range(N) if PAIRS[i] == g]

def followers(g):
    return collections.Counter(PAIRS[i+1] for i in positions(g) if i+1 < N)

def predecessors(g):
    return collections.Counter(PAIRS[i-1] for i in positions(g) if i > 0)

def window(i, w=3, mark=None):
    lo, hi = max(0, i-w), min(N, i+w+1)
    out = []
    for j in range(lo, hi):
        lab = GT.get(PAIRS[j], '?')
        tok = f'{PAIRS[j]}={lab}'
        if j == i:
            tok = f'[{tok}]'
        out.append(tok)
    return ' '.join(out)

# ---------- era: Tocqueville T1+T2, audit tokenizer ----------
def era_tokens():
    t = ''
    for fn in ['gutenberg-30513-tocqueville-t1.txt', 'gutenberg-30514-tocqueville-t2.txt']:
        t += open(DATA / fn, encoding='utf-8', errors='replace').read().lower() + '\n'
    t = re.sub(r"[’‘`]", "'", t)
    # split elisions: "l'on" -> "l'" "on"  (keep the elided particle as its own token)
    t = re.sub(r"\b([a-zàâäéèêëîïôöùûüç]+)'([a-zàâäéèêëîïôöùûüç]+)", r"\1' \2", t)
    return re.findall(r"[a-zàâäéèêëîïôöùûüç]+'?|[a-zàâäéèêëîïôöùûüç]+", t)

_TOKS = None
def toks():
    global _TOKS
    if _TOKS is None:
        _TOKS = era_tokens()
    return _TOKS

_EU, _EB = None, None
def era_counters():
    global _EU, _EB
    if _EU is None:
        t = toks()
        _EU = collections.Counter(t)
        _EB = collections.Counter(zip(t, t[1:]))
    return _EU, _EB

def era_Pfol(word, followers):
    eu, eb = era_counters()
    nw = eu[word]
    if nw == 0:
        return 0.0
    return sum(eb[(word, f)] for f in followers) / nw

def era_Ppre(word, pres):
    eu, eb = era_counters()
    nw = eu[word]
    if nw == 0:
        return 0.0
    return sum(eb[(p, word)] for p in pres) / nw
