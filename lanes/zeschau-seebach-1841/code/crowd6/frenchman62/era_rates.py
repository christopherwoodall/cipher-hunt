#!/usr/bin/env python3
"""Era word-space rates for the 62 three-way (on/il/qui). Same tokenizer as the round-5 red-team audit."""
import re, collections, math
from pathlib import Path
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
DATA = LANE / 'data'

def words(path):
    t = open(path, encoding='utf-8', errors='replace').read().lower()
    t = re.sub(r"[']", "'", t)
    t = re.sub(r"\b([a-zàâäéèêëîïôöùûüç]+)'([a-zàâäéèêëîïôöùûüç]+)", r"\1' \2", t)
    return re.findall(r"[a-zàâäéèêëîïôöùûüç]+(?:'[a-zàâäéèêëîïôöùûüç]+)?", t)

toks = words(DATA/'gutenberg-30513-tocqueville-t1.txt') + words(DATA/'gutenberg-30514-tocqueville-t2.txt')
N = len(toks); uni = collections.Counter(toks)
bi = collections.Counter(zip(toks, toks[1:]))
print('era tokens:', N)

def Pfol(fol, w):
    """P(follower in fol-set | word w). fol may be a set."""
    nw = uni[w]
    c = sum(bi[(w, f)] for f in fol)
    return nw, c, c/nw

def Ppre(w, pres):
    """P(word w | predecessor in pres-set) = P(pre in pres, w)/P(pre in pres)... no: P(w|pre in S)."""
    npre = sum(uni[p] for p in pres)
    c = sum(bi[(p, w)] for p in pres)
    return npre, c, c/npre

def Ppre_is(w, pset):
    """P(predecessor in pset | word w)."""
    nw = uni[w]
    c = sum(bi[(p, w)] for p in pset)
    return nw, c, c/nw

NE = {'ne','n'}
QUE = {'que','qu'}
for w in ['on','il','ils','qui','je','nous']:
    nw, c, p = Pfol(NE, w); print(f'P(ne|{w}) = {c}/{nw} = {p:.4f}')
print()
for w in ['on','il','qui']:
    nw, c, p = Pfol(QUE, w); print(f'P(que|{w}) follower = {c}/{nw} = {p:.5f}')
    nw, c, p = Ppre_is(w, QUE); print(f'P(que-pre|{w}) = {c}/{nw} = {p:.5f}')
    nw, c, p = Ppre_is(w, {'l'}); print(f'P(l-pre|{w}) = {c}/{nw} = {p:.5f}')
    nw, c, p = Ppre_is(w, {'s','si'}); print(f'P(s/si-pre|{w}) = {c}/{nw} = {p:.5f}')
    nw, c, p = Pfol({'me'}, w); print(f'P(me|{w}) follower = {c}/{nw} = {p:.5f}')
    print()
for w in ['on','il','qui']:
    npre, c, p = Ppre(w, {'par'}); print(f'P({w}|par) = {c}/{npre} = {p:.5f}')
    npre, c, p = Ppre(w, {'ce'}); print(f'P({w}|ce) = {c}/{npre} = {p:.5f}')
print()
for w in ['on','il','qui']:
    print(f'P({w}) = {uni[w]}/{N} = {uni[w]/N:.6f}')
