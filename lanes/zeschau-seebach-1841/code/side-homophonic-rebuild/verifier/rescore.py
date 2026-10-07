#!/usr/bin/env python3
"""Independent verifier rescorer for the Seebach rebuild pilot.

Written from the objective spec in solver/REBUILD.md (2026-10-07), NOT from
diag_rescore.py. Reimplements the final objective:

  J = S_char + lam_word*(S_cov - S_single) + S_potts + S_soft
      - lam_poly*n_poly - lam_conc*S_conc

  S_char = sum_t F(pcell[t-1], pcell[t])   (F = per-pair rate: raw 5-gram
           logp sum over the pair's chars DIVIDED by len(pair))
  S_cov  = sum over decode chars c of max_{lexicon hits h covering c,
           len(h)>=word_minlen} w_h/len(h)   (per-char best-hit, no overlap)
  S_single = sum_t lex_wt[pcell[t]]
  S_conc = sum_{projected values v} (n_v - conc_cap)^2 for n_v > conc_cap
  S_potts = beta * sum_{J(g,h)>=0.1} J(g,h)*[v1[g]==v1[h]], beta=beta0*gate

E-step: hard per-occurrence choice between projected v1/v2 by F-rate +
log(w2), 10-sweep fixpoint, then w2 recomputed as (n2+1)/(occ+2).
Truth rescore initializes v2 weights at 0.5 (as the diagnostic did).

READ-ONLY: never mutates Smith code, never runs the annealer, never touches
R5005. Opening the sealed 184101 truth is post-diagnostic forensics.
"""
import collections
import json
import math
import os
import re as _re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
REBUILD = os.path.abspath(os.path.join(HERE, '..'))
LANE = os.path.abspath(os.path.join(REBUILD, '..'))
INST = os.path.join(LANE, 'side-homophonic', 'control', 'instances')
RUNS = os.path.join(LANE, 'side-homophonic', 'runs')

START = '^'
NGRAM = 5
ALPHA = 0.5


# ---------------------------------------------------------------- phonetics
# Independent reimplementation of the phonetic projection pi documented in
# solver/phonetics.py (rule table + self-test cases). Applied identically to
# corpus, lexicon, and decoded values. Cross-checked against the library
# implementation on the full inventory + lexicon at import time (assert).
import re as _re

_ACCENT_MAP = {
    'à': 'a', 'â': 'a',
    'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
    'î': 'i', 'ï': 'i', 'ÿ': 'i',
    'ô': 'o',
    'û': 'u', 'ü': 'u', 'ù': 'u',
    'ç': 'S',
}
_DIGRAPHS_A = [
    ('eau', 'o'),
    ('ain', 'I'), ('ein', 'I'), ('ien', 'I'), ('yen', 'I'), ('oin', 'I'),
    ('au', 'o'), ('ai', 'e'), ('ei', 'e'), ('ou', 'u'),
    ('ch', 'C'), ('ph', 'f'), ('th', 't'), ('qu', 'k'), ('gn', 'N'),
]
_NASAL_MAP = {'an': 'A', 'en': 'A', 'am': 'A', 'em': 'A',
              'on': 'O', 'om': 'O', 'in': 'I', 'un': 'U', 'um': 'U'}
_NASAL_RE = _re.compile(r'(an|en|am|em|on|om|in|un|um)(?![aeiouynm])')
_SILENT_FINALS = set('dtsxbpgz')


def project(word, silent_finals=True):
    """Map a French word (or cipher value string) to phonetic classes."""
    w = word.lower().replace('œ', 'oe').replace('æ', 'ae')
    w = ''.join(_ACCENT_MAP.get(ch, ch) for ch in w)
    w = ''.join(c for c in unicodedata.normalize('NFD', w)
                if unicodedata.category(c) != 'Mn')
    w = _re.sub(r'[^a-z]', '', w)
    if not w:
        return w
    for pat, rep in _DIGRAPHS_A:
        w = w.replace(pat, rep)
    w = w.replace('h', '')
    w = _NASAL_RE.sub(lambda m: _NASAL_MAP[m.group(1)], w)
    w = w.replace('y', 'i').replace('w', 'v')
    w = _re.sub(r'(?<=[aeiouAEIOU])x$', '', w)
    w = w.replace('x', 'ks')
    w = w.replace('ss', 'S')
    w = _re.sub(r'(.)\1', r'\1', w)
    if silent_finals and len(w) > 1:
        w = _re.sub(r'(?<=[aeiouAEIOU])[dtsxbpgz]+$', '', w)
    if not w:
        w = _re.sub(r'[^a-z]', '', word.lower())
    return w


def _crosscheck_project():
    """Assert my reimplementation matches the library on every string that
    matters: all pilot values, truth primaries/secondaries, anchors, the
    full crib inventory, and the whole 3,546-word lexicon."""
    sys.path.insert(0, os.path.join(REBUILD, 'solver'))
    import phonetics as _ph
    lib = _ph.project
    strings = set()
    lex = json.load(open(os.path.join(REBUILD, 'solver', 'lm_ref', 'lm.json')))['lexicon']
    for e in lex:
        strings.add(e['w'])
    inv = json.load(open(os.path.join(REBUILD, 'solver', 'inventory_data.json')))
    for k in ('units', 'tier3_top200'):
        strings.update(inv[k])
    try:
        from crib_inventory import get_crib_core, get_by_ear_extended
        strings.update(get_crib_core())
        strings.update(get_by_ear_extended())
    except Exception:
        pass
    for seed in ('184101', '184102', '184103', '184104', '184105', '184106'):
        try:
            an = json.load(open(os.path.join(INST, f'SYNTHETIC-crib-{seed}.json')))['anchors']
            strings.update(an.values())
            tr = json.load(open(os.path.join(INST, f'SYNTHETIC-key-{seed}.json')))['key']
            for g in tr:
                strings.add(tr[g]['primary'])
                strings.update(tr[g].get('secondaries') or [])
        except FileNotFoundError:
            pass
    try:
        pilot = json.load(open(os.path.join(REBUILD, 'pilot', 'rebuild-pilot-final', 'result.json')))
        for rr in pilot['restarts']:
            for g, a in rr['assignment'].items():
                strings.add(a['v1'])
                if a['v2']:
                    strings.add(a['v2'])
        strings.update(pilot['meta']['pins'].values())
    except FileNotFoundError:
        pass
    bad = [(s, lib(s), project(s)) for s in strings if lib(s) != project(s)]
    assert not bad, f'project() mismatch on {len(bad)} strings: {bad[:5]}'
    return len(strings)


_N_PROJ_CHECKED = _crosscheck_project()


# ------------------------------------------------------------------ CharLM
class CharLM:
    """Interpolated char n-gram (order 5, alpha 0.5) over projected alphabet."""

    def __init__(self, lm_data):
        counts = lm_data['counts']
        self.c1 = counts['1']
        self.nest = {o: counts[str(o)] for o in range(2, NGRAM + 1)}
        self.tot = {}
        for o in range(2, NGRAM + 1):
            t = collections.Counter()
            for ctx, d in self.nest[o].items():
                t[ctx] = sum(d.values())
            self.tot[o] = t
        self.N1 = sum(self.c1.values())

    def logp(self, ch, ctx):
        ctx = ctx[-(NGRAM - 1):]
        p = self.c1.get(ch, 0) / self.N1
        if p <= 0:
            p = 1e-12
        for o in range(2, NGRAM + 1):
            if len(ctx) < o - 1:
                break
            cc = ctx[-(o - 1):]
            d = self.nest[o].get(cc)
            num = d.get(ch, 0) if d else 0
            den = self.tot[o].get(cc, 0)
            p = (num + ALPHA * p) / (den + ALPHA)
        return math.log(max(p, 1e-300))

    def F(self, ca, cb):
        """Per-pair rate: raw 5-gram logp sum over cb's chars / len(cb)."""
        if not cb:
            return 0.0
        hist = START * (NGRAM - 1) if ca == START else (START * (NGRAM - 1) + ca)[-(NGRAM - 1):]
        t = 0.0
        h = hist
        for ch in cb:
            t += self.logp(ch, h)
            h = (h + ch)[-(NGRAM - 1):]
        return t / len(cb)


# -------------------------------------------------------------------- phase
def _contact_sets(pairs, k=10):
    groups = sorted(set(pairs))
    pred = collections.defaultdict(collections.Counter)
    foll = collections.defaultdict(collections.Counter)
    for i in range(len(pairs) - 1):
        a, b = pairs[i], pairs[i + 1]
        foll[a][b] += 1
        pred[b][a] += 1
    return {g: (set(h for h, _ in foll[g].most_common(k)) |
                set(h for h, _ in pred[g].most_common(k))) for g in groups}


def analyze_stream(pairs, jaccard_floor=0.1):
    """Unsupervised contact-structure analysis (REBUILD.md spec: same
    instrument as the control generator's unsupervised_chi2). Returns
    adj {group: [(neighbor, jaccard)]} and chi2-gated rotation gate."""
    groups = sorted(set(pairs))
    N = len(pairs)
    top = _contact_sets(pairs)
    J = {}
    for i, a in enumerate(groups):
        for b in groups[i + 1:]:
            sa, sb = top[a], top[b]
            u = sa | sb
            j = len(sa & sb) / len(u) if u else 0.0
            if j > 0:
                J[(a, b)] = j
    adj = collections.defaultdict(list)
    for (a, b), j in J.items():
        if j >= jaccard_floor:
            adj[a].append((b, j))
            adj[b].append((a, j))
    # reference chi2: agglomerative average-linkage to 12 clusters,
    # 3 largest -> A/B/C, block-transition chi-square vs independence
    def jac(a, b):
        sa, sb = top[a], top[b]
        u = sa | sb
        return len(sa & sb) / len(u) if u else 0.0

    clusters = [{g} for g in groups]
    merges = []

    def avg(c1, c2):
        return sum(jac(a, b) for a in c1 for b in c2) / (len(c1) * len(c2))

    while len(clusters) > 1:
        best, bi, bj = -1.0, None, None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                s = avg(clusters[i], clusters[j])
                if s > best:
                    best, bi, bj = s, i, j
        merges.append((sorted(clusters[bi]), sorted(clusters[bj])))
        new = clusters[bi] | clusters[bj]
        clusters = [c for k, c in enumerate(clusters) if k not in (bi, bj)] + [new]
    cs = [{g} for g in groups]
    for c1l, c2l in merges:
        if len(cs) <= 12:
            break
        c1, c2 = set(c1l), set(c2l)
        cs = [c for c in cs if c != c1 and c != c2] + [c1 | c2]
    cs = sorted(cs, key=len, reverse=True)
    block = {}
    for x, lbl in zip(cs[:3], 'ABC'):
        for g in x:
            block[g] = lbl
    rest = set().union(*cs[3:]) if len(cs) > 3 else set()
    for g in rest:
        block[g] = 'R'
    trans = collections.Counter()
    for i in range(N - 1):
        trans[(block[pairs[i]], block[pairs[i + 1]])] += 1
    cnt = {(r, c): trans[(r, c)] for r in 'ABC' for c in 'ABC'}
    r3 = {r: sum(cnt[(r, c)] for c in 'ABC') for r in 'ABC'}
    c3 = {c: sum(cnt[(r, c)] for r in 'ABC') for c in 'ABC'}
    n3 = sum(cnt.values())
    chi2 = sum((cnt[(r, c)] - r3[r] * c3[c] / n3) ** 2 / (r3[r] * c3[c] / n3)
               for r in 'ABC' for c in 'ABC' if r3[r] * c3[c] > 0)
    gate = 1.0 / (1.0 + math.exp(-(chi2 - 80.0) / 12.0))
    return {'adj': {g: sorted(adj[g], key=lambda t: -t[1]) for g in groups},
            'chi2': round(chi2, 1),
            'gate': round(gate, 4)}


# ------------------------------------------------------------------ rescore
class Rescorer:
    def __init__(self, pairs, cfg):
        self.pairs = pairs
        self.cfg = cfg
        self.groups = sorted(set(pairs))
        self.occ = collections.defaultdict(list)
        for t, g in enumerate(pairs):
            self.occ[g].append(t)
        lm_data = json.load(open(os.path.join(REBUILD, 'solver', 'lm_ref', 'lm.json')))
        self.lm = CharLM(lm_data)
        self.lex = [(e['w'], e['wt']) for e in lm_data['lexicon']]
        self.lex_wt = {e['w']: e['wt'] for e in lm_data['lexicon']}
        self.phase = analyze_stream(pairs)
        self.beta = cfg['beta0'] * self.phase['gate']

    def _estep(self, v1, v2, w2):
        """Hard E-step fixpoint: per occurrence choose projected v1/v2."""
        N = len(self.pairs)
        pcell = [project(v1[g]) for g in self.pairs]
        for _ in range(10):
            moved = False
            for t in range(N):
                g = self.pairs[t]
                o1 = project(v1[g])
                if v2.get(g) is None:
                    nv = o1
                else:
                    o2 = project(v2[g])
                    ca = pcell[t - 1] if t > 0 else START
                    cb = pcell[t + 1] if t + 1 < N else None
                    s1 = self.lm.F(ca, o1) + (self.lm.F(o1, cb) if cb else 0.0)
                    s2 = self.lm.F(ca, o2) + (self.lm.F(o2, cb) if cb else 0.0)
                    w = min(max(w2[g], 1e-6), 1 - 1e-6)
                    nv = o2 if s2 + math.log(w) > s1 + math.log(1 - w) else o1
                if nv != pcell[t]:
                    pcell[t] = nv
                    moved = True
            if not moved:
                break
        return pcell

    def _cover_sum(self, s, minlen):
        """Per-char best-hit coverage: sum_c max_{hits h covering c,
        len(h)>=minlen} w_h/len(h)."""
        best = [0.0] * len(s)
        for w, wt in self.lex:
            L = len(w)
            if L < minlen:
                continue
            v = wt / L
            i = s.find(w)
            while i >= 0:
                for c in range(i, i + L):
                    if v > best[c]:
                        best[c] = v
                i = s.find(w, i + 1)
        return sum(best)

    def score(self, v1, v2, w2_init, label='key', minlen=None, verbose=False):
        cfg = self.cfg
        minlen = cfg['word_minlen'] if minlen is None else minlen
        v2 = {g: v2.get(g) for g in self.groups}
        w2 = {g: w2_init.get(g, 0.0) for g in self.groups}
        pcell = self._estep(v1, v2, w2)
        # w2 recompute after fixpoint (matches _full_refresh)
        for g in self.groups:
            if v2[g] is not None:
                o2 = project(v2[g])
                n2 = sum(1 for t in self.occ[g] if pcell[t] == o2)
                w2[g] = (n2 + 1.0) / (len(self.occ[g]) + 2.0)
        N = len(pcell)
        S_char = sum(self.lm.F(pcell[t - 1] if t > 0 else START, pcell[t])
                     for t in range(N))
        s = ''.join(pcell)
        S_cov = self._cover_sum(s, minlen)
        S_single = sum(self.lex_wt.get(pcell[t], 0.0) for t in range(N))
        pv = {g: project(v1[g]) for g in self.groups}
        cnt = collections.Counter(pv.values())
        cap = cfg['conc_cap']
        S_conc = sum((n - cap) ** 2 for n in cnt.values() if n > cap)
        seen = set()
        S_potts = 0.0
        for g in self.groups:
            for h, j in self.phase['adj'][g]:
                key = (g, h) if g < h else (h, g)
                if key in seen:
                    continue
                seen.add(key)
                if v1[g] == v1[h]:
                    S_potts += self.beta * j
        n_poly = sum(1 for g in self.groups if v2[g] is not None)
        S_word = S_cov - S_single
        total = (S_char + cfg['lambda_word'] * S_word + S_potts
                 - cfg['lambda_poly'] * n_poly - cfg['lambda_conc'] * S_conc)
        if verbose:
            print(f'[{label}] total={total:.1f} (minlen={minlen})')
            print(f'   S_char={S_char:.1f} S_cov={S_cov:.1f} '
                  f'S_single={S_single:.1f} S_word={S_word:.1f} '
                  f'S_potts={S_potts:.3f} S_conc={S_conc:.1f} n_poly={n_poly}')
            print(f'   decode len={len(s)} chars, per-pair rate='
                  f'{S_char / N:.3f}')
        return {'label': label, 'total': total, 'S_char': S_char,
                'S_cov': S_cov, 'S_single': S_single, 'S_word': S_word,
                'S_potts': S_potts, 'S_conc': S_conc, 'n_poly': n_poly,
                'decode': s, 'pcell': pcell, 'v1': v1, 'v2': v2,
                'decode_len': len(s), 'N': N}

    def quota_dist(self, v1):
        """Projected-value group counts (the 'quota distribution')."""
        return collections.Counter(project(v1[g]) for g in self.groups)


# ------------------------------------------------------------------ loaders
def load_pairs(seed):
    pairs = []
    with open(os.path.join(INST, f'SYNTHETIC-ct-{seed}.pairs.txt')) as f:
        for l in f:
            if l.startswith('#') or not l.strip():
                continue
            pairs += l.split()
    return pairs


def load_anchors(seed):
    return json.load(open(os.path.join(INST, f'SYNTHETIC-crib-{seed}.json')))['anchors']


def load_truth(seed):
    return json.load(open(os.path.join(INST, f'SYNTHETIC-key-{seed}.json')))['key']
