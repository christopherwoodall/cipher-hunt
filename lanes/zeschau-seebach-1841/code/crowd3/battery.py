#!/usr/bin/env python3
"""Attempt-2/3 check battery for the bigram closer. Importable; run() executes."""
import sys, os, json, re, collections, math, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join(HERE, '..')
DATA = os.path.join(CODE, '..', 'data')
sys.path.insert(0, CODE)
from crib_attack import load_pairs

ANCH = {'11':'la','46':'que','40':'e','70':'pre'}          # rate-usable GT anchors
ANCH_PROV = {'87':'ce','64':'qui','96':'par','94':'ne'}   # provisional (secondary legs only)
ANCH_EXCL = {'29':'er','82':'m','34':'i'}                  # syllabification mismatch, excluded
VOWELS = set('aeiouy')
LIQ = {'bl','cl','fl','gl','pl','br','cr','dr','fr','gr','pr','tr','vr'}
DIG = {'ch','ph','th','gn'}

def strip_acc(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def syllabify(word):
    w = strip_acc(word.lower())
    if not w: return []
    toks = []; i, n = 0, len(w)
    while i < n:
        if w[i] in VOWELS:
            j = i
            while j < n and w[j] in VOWELS: j += 1
            toks.append(('V', w[i:j])); i = j
        else:
            j = i
            while j < n and w[j] not in VOWELS: j += 1
            toks.append(('C', w[i:j])); i = j
    syls, cur, idx = [], '', 0
    if toks and toks[0][0] == 'C': cur, idx = toks[0][1], 1
    while idx < len(toks):
        typ, val = toks[idx]
        if typ != 'V': cur += val; idx += 1; continue
        if idx + 1 < len(toks) and toks[idx+1][0] == 'C':
            cc = toks[idx+1][1]
            if idx + 2 < len(toks) and toks[idx+2][0] == 'V':
                onset = cc[-1]
                if len(cc) >= 2 and (cc[-2:] in LIQ or cc[-2:] in DIG): onset = cc[-2:]
                cur += val + cc[:-len(onset)]
                syls.append(cur); cur = onset; idx += 2
            else: cur += val + cc; idx += 2
        else: cur += val; idx += 1; syls.append(cur); cur = ''
    if cur: syls.append(cur)
    return [s for s in syls if s]

def load_words(path):
    text = open(path, encoding='utf-8', errors='replace').read().lower()
    m = re.search(r'\*\*\* start of.*?\*\*\*', text)
    if m: text = text[m.end():]
    m = re.search(r'\*\*\* end of.*', text)
    if m: text = text[:m.start()]
    return re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)

class Models:
    def __init__(self):
        self.pairs, _, _ = load_pairs()
        self.N = len(self.pairs)
        self.cf = collections.Counter(self.pairs)
        self.cbi = collections.Counter(zip(self.pairs, self.pairs[1:]))
        self.cN1 = self.N - 1
        stream = []
        for p in (os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'),
                  os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')):
            for w in load_words(p):
                stream.extend(syllabify(w))
        self.eu = collections.Counter(stream)
        self.eb = collections.Counter(zip(stream, stream[1:]))
        self.eN = len(stream); self.eN1 = len(stream) - 1

    def cP(self, g): return self.cf[g] / self.N
    def eP(self, s): return self.eu.get(s, 0) / self.eN
    def cPfol(self, f, g):  # P(f|g)
        return self.cbi.get((g, f), 0) / self.cf[g] if self.cf[g] else 0.0
    def cPpre(self, p, g):  # P(g|p)
        return self.cbi.get((p, g), 0) / self.cf[p] if self.cf[p] else 0.0
    def ePfol(self, s2, s1):
        return self.eb.get((s1, s2), 0) / self.eu[s1] if self.eu.get(s1) else 0.0
    def ePpre(self, s1, s2):
        return self.eb.get((s1, s2), 0) / self.eu[s2] if self.eu.get(s2) else 0.0
    def fol_counter(self, g):
        return collections.Counter(f for (gg, f) in self.cbi for _ in [0] if gg == g for _ in range(self.cbi[(gg, f)]))
    def followers(self, g):
        c = collections.Counter()
        for i, x in enumerate(self.pairs):
            if x == g and i + 1 < self.N: c[self.pairs[i+1]] += 1
        return c
    def predecessors(self, g):
        c = collections.Counter()
        for i, x in enumerate(self.pairs):
            if x == g and i - 1 >= 0: c[self.pairs[i-1]] += 1
        return c
    def e_followers(self, s):
        c = collections.Counter()
        for (a, b), n in self.eb.items():
            if a == s: c[b] = n
        return c

def inband(r): return 0.5 <= r <= 2.0

def run_battery(M, g, hyps):
    """hyps: list of (reading, tag). Returns dict of leg results per reading."""
    out = {}
    cg = M.cf[g]
    fol = M.followers(g); pre = M.predecessors(g)
    for h, tag in hyps:
        er = M.eP(h); cr = cg / M.N
        L1 = {'cipher_rate': round(cr, 5), 'era_rate': round(er, 5),
              'ratio': round(cr / er, 3) if er else None,
              'in_band': inband(cr / er) if er else False}
        # L2: conditional rates vs usable GT anchors
        rows = []
        for a, r in ANCH.items():
            n_f = M.cbi.get((g, a), 0); n_p = M.cbi.get((a, g), 0)
            if n_f >= 2:
                cp, ep = M.cPfol(a, g), M.ePfol(r, h)
                rows.append({'dir': f'{g}->{a}', 'n': n_f, 'cipher': round(cp, 4),
                             'era': round(ep, 5), 'ratio': round(cp / ep, 3) if ep else None,
                             'in_band': inband(cp / ep) if ep else False,
                             'era_zero': ep == 0})
            if n_p >= 2:
                cp, ep = M.cPpre(a, g), M.ePpre(r, h)
                rows.append({'dir': f'{a}->{g}', 'n': n_p, 'cipher': round(cp, 4),
                             'era': round(ep, 5), 'ratio': round(cp / ep, 3) if ep else None,
                             'in_band': inband(cp / ep) if ep else False,
                             'era_zero': ep == 0})
        inb = sum(1 for r_ in rows if r_['in_band'])
        L2 = {'rows': rows, 'n_tested': len(rows), 'n_in_band': inb}
        # L2b: concentration (structural): top-3 follower share
        fvals = sorted(fol.values(), reverse=True)
        c_top3 = sum(fvals[:3]) / cg if cg else 0
        ef = M.e_followers(h); evals = sorted(ef.values(), reverse=True)
        e_top3 = sum(evals[:3]) / M.eu[h] if M.eu.get(h) else 0
        L2b = {'cipher_top3_share': round(c_top3, 3), 'era_top3_share': round(e_top3, 3),
               'ratio': round(c_top3 / e_top3, 3) if e_top3 else None,
               'in_band': inband(c_top3 / e_top3) if e_top3 else False}
        # L3a: grammatical attestation kills (usable anchors, cipher n>=3)
        kills = []
        for a, r in ANCH.items():
            if M.cbi.get((g, a), 0) >= 3 and M.eb.get((h, r), 0) == 0:
                kills.append(f'{g}->{a}={r} x{M.cbi[(g,a)]} but era "{h}-{r}" unattested')
            if M.cbi.get((a, g), 0) >= 3 and M.eb.get((r, h), 0) == 0:
                kills.append(f'{a}={r}->{g} x{M.cbi[(a,g)]} but era "{r}-{h}" unattested')
        L3a = {'kills': kills, 'pass': not kills}
        out[h] = {'tag': tag, 'L1': L1, 'L2': L2, 'L2b': L2b, 'L3a': L3a,
                  'top_fol': fol.most_common(6), 'top_pre': pre.most_common(6)}
    return out
