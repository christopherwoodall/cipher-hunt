#!/usr/bin/env python3
"""BIGRAM CLOSER (round 3, crowd3): anchor factory via the attempts-2/3 check battery.

Battery per candidate group g with reading hypothesis h (French syllable):
 (1) frequency/rank band: cipher P(g) vs era P(h) [context, never promotion alone]
 (2) conditional bigram rates vs era corpus: P(a|g)/P(g|a) for anchors a vs era P(r_a|h)/P(h|r_a)
 (3) grammatical coherence of resulting bigrams/trigrams built with anchors
 (4) negative controls: rival readings that must fail
Promotions need >=2 independent checks; near-misses are leads. Rate band is
UNCALIBRATED: no promotion on rates alone.
"""
import json, re, collections, os, sys, math, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join(HERE, '..')
DATA = os.path.join(CODE, '..', 'data')
sys.path.insert(0, CODE)
from crib_attack import load_pairs

ANCHORS_GT = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i', '29': 'er', '40': 'e', '46': 'que'}
PROV = {'87': 'ce', '64': 'qui', '96': 'par'}
ANCHORS_ALL = dict(ANCHORS_GT, **PROV)

VOWELS = set('aeiouy')
LIQUID_ONSETS = {'bl','cl','fl','gl','pl','br','cr','dr','fr','gr','pr','tr','vr'}
DIGRAPHS = {'ch','ph','th','gn'}

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def syllabify(word):
    """Morphologist's documented orthographic syllabifier:
    lowercase+strip accents; nuclei=maximal vowel-letter runs; maximal onset
    (last consonant right) except liquid onsets and digraphs stay together;
    leading/trailing consonants attach; final mute -e is its own nucleus."""
    w = strip_accents(word.lower())
    if not w: return []
    # split into nuclei and consonant clusters
    toks = []
    i, n = 0, len(w)
    while i < n:
        if w[i] in VOWELS:
            j = i
            while j < n and w[j] in VOWELS: j += 1
            toks.append(('V', w[i:j])); i = j
        else:
            j = i
            while j < n and w[j] not in VOWELS: j += 1
            toks.append(('C', w[i:j])); i = j
    # final mute -e: lone trailing 'e' vowel token is its own nucleus (keep as syllable)
    syls, cur = [], ''
    idx = 0
    if toks and toks[0][0] == 'C':
        cur = toks[0][1]; idx = 1
    while idx < len(toks):
        typ, val = toks[idx]
        if typ != 'V':
            cur += val; idx += 1; continue
        # have vowel val at idx
        if idx + 1 < len(toks) and toks[idx+1][0] == 'C':
            cc = toks[idx+1][1]
            if idx + 2 < len(toks) and toks[idx+2][0] == 'V':
                # intervocalic: maximal onset to the right
                onset = cc[-1]
                if len(cc) >= 2:
                    last2 = cc[-2:]
                    if last2 in LIQUID_ONSETS or last2 in DIGRAPHS:
                        onset = last2
                cur += val + cc[:-len(onset)]
                syls.append(cur); cur = onset; idx += 2
            else:
                cur += val + cc; idx += 2
                if idx < len(toks):  # more vowel tokens follow? shouldn't happen
                    pass
        else:
            cur += val; idx += 1
            syls.append(cur); cur = ''
    if cur: syls.append(cur)
    return [s for s in syls if s]

def load_words(path):
    text = open(path, encoding='utf-8', errors='replace').read().lower()
    m = re.search(r'\*\*\* start of.*?\*\*\*', text)
    if m: text = text[m.end():]
    m = re.search(r'\*\*\* end of.*', text)
    if m: text = text[:m.start()]
    return re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)

def neighbours(pairs, anchor, direction=+1):
    c = collections.Counter()
    for i, g in enumerate(pairs):
        if g == anchor:
            j = i + direction
            if 0 <= j < len(pairs): c[pairs[j]] += 1
    return c

def ngram_count(pairs, seq):
    L = len(seq); c = 0
    for i in range(len(pairs) - L + 1):
        if pairs[i:i+L] == seq: c += 1
    return c

def load_corpus_syllables():
    syl_uni, syl_bi = collections.Counter(), collections.Counter()
    n_words = 0
    for p in (os.path.join(DATA,'gutenberg-30513-tocqueville-t1.txt'),
              os.path.join(DATA,'gutenberg-30514-tocqueville-t2.txt')):
        for w in load_words(p):
            n_words += 1
            syls = syllabify(w)
            for s in syls: syl_uni[s] += 1
            for a, b in zip(syls, syls[1:]): syl_bi[(a, b)] += 1
    return syl_uni, syl_bi, n_words

if __name__ == '__main__':
    su, sb, nw = load_corpus_syllables()
    print('era words', nw, 'syllable tokens', sum(su.values()), 'distinct', len(su))
    for s, c in su.most_common(50):
        print(f'{s:10s} {c:6d} {c/sum(su.values()):.5f}')
