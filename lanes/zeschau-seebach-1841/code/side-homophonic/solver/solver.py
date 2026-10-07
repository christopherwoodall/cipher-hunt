#!/usr/bin/env python3
"""Joint-inference homophonic solver for the Seebach cipher (side fleet).

METHOD (one line): simulated annealing over the FULL 96-group key, maximizing
a joint objective = character-5-gram LM on the phoneticized decode
  + word-salad bonus (Aho-Corasick over the era lexicon)
  + contact-similarity Potts prior (chi2-gated phase rhythm)
  + soft anchor priors + polyvalence (secondary values, hard E-step).
Full justification: METHOD.md. Do NOT run on R5005 until the control passes.

KEY MODEL
---------
- v1[g]: primary value (string) for each group g. MANY-TO-ONE allowed
  (homophony: no injectivity constraint) -- this is the task's "polyvalence
  (many-groups->one-syllable)".
- v2[g]: optional secondary value (or None) + w2[g] = P(use v2).
  Per-occurrence hard E-step: each occurrence decodes to argmax over
  {v1,v2} of local char-5-gram score + log weight. This is the lane's R5
  polyvalence (one group, several readings: 94=ne/en, 52=pas/so, 06=-ent/stem).
- 7 hard pins (11=la 70=pre 82=m 34=i 29=er 40=e 46=que) are NEVER moved and
  have no secondary. Soft anchors (87=ce 64=qui 96=par, provisional) enter as
  prior bonuses, disabled for synthetic controls (R5005-specific).

OBJECTIVE (to maximize)
-----------------------
J = S_char + LW*S_word + S_potts + S_soft - LP*n_poly - LC*S_conc, where
  S_conc  = sum_p max(0, n_p - conc_cap)^2, n_p = #groups whose v1
            PROJECTS to p (over projected values, so 'me'/'mê'/'mè' collude).
            Penalizes extreme many-to-one concentration (the repetition
            exploit: mapping 50+ groups to 'me' so 'me'+'me'="meme" hits the
            lexicon at every position). The true codebook spreads 89 groups
            over ~60 cells (max quota 3-5 by largest-remainder); a cap of 6
            is safe for the truth and crushes the exploit. (Added 2026-10-07
            after pilot 2/89.)
  S_char  = sum_t F(pcell[t-1], pcell[t]): interpolated char-5-gram logp of
            the PROJECTED decode (phonetics.project). F scores cb's chars
            given ca's trailing chars; t=0 uses '^'. Local in t -> exact
            delta scoring (no suffix rescore; the score is a sum over t).
  S_word  = Aho-Corasick weight sum over projected lexicon hits in the
            decode, MINUS single-value hits (see below). Overlapping allowed;
            it is a scoring function, not a parse. Exact windowed deltas,
            verified by --self-test.
            WHY minus single-value hits: a key whose VALUES are common words
            ('leur','mais',...) gets a hit at every occurrence without
            deciphering anything -- a degenerate attractor the char LM
            alone does not defeat (frequent-word salad outscores real
            register-mismatched French). Only hits SPANNING a value boundary
            (words formed by 2+ values, e.g. 'cha'+'pi'+'tre'='chapitre')
            are evidence of correct decipherment. Implemented as:
            S_word = AC_scan(chars) - sum_t single_wt[pcell[t]], where
            single_wt[p] = lexicon weight if p is a lexicon word else 0.
  S_potts = beta * sum_{J(g,h)>=0.1} J(g,h)*[v1[g]==v1[h]], beta=beta0*gate.
            Homophones emitted uniformly have identical contact profiles, so
            contact-similar groups are the natural homophone pool. Soft,
            gated, ablatable (--no-phase).
  S_soft  = w_soft * #{soft anchors matched} (R5005 only; --no-soft).
  n_poly  = #{g: v2[g] is not None}, penalized by LP (sparsity).

MOVES (Metropolis, geometric cooling, restarts, best-key retention):
  chg1  (55%): reassign v1[g] (50% freq-weighted / 30% uniform /
           20% copy a contact-neighbor's v1 -- homophone-pool proposal)
  swap  (15%): swap v1[g], v1[h]
  poly  (15%): add/drop secondary v2[g]
  chg2  (10%): change secondary v2[g]
  block ( 5%): reassign g + top-3 Jaccard neighbors together (Potts moves)
All deltas exact via snapshot/revert; --self-test checks incremental totals
against full recompute after random moves.
"""

import argparse
import bisect
import collections
import json
import math
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from phonetics import project  # noqa: E402
from phase import analyze_stream, gate_of  # noqa: E402

START = '^'
NGRAM = 5
LM_ALPHA = 0.5

DEFAULTS = {
    'restarts': 12,
    'iters': 40000,
    't0': 60.0,
    'tmin': 0.05,
    'lambda_word': 1.0,
    'beta0': 2.0,
    'w_soft': 3.0,
    'lambda_poly': 20.0,
    'lambda_conc': 5.0,   # concentration penalty weight
    'conc_cap': 6,         # max groups/value before quadratic penalty
    'jaccard_floor': 0.1,
    'inventory_mode': 'extended',   # or 'units' (strict task-brief)
    'init': 'random',               # or 'freqmatch'
    'refine': True,
    'seed': 1841,
}


# ------------------------------------------------------------------ CharLM
class CharLM:
    """Interpolated character n-gram LM over the projected alphabet."""

    def __init__(self, lm_data, alpha=LM_ALPHA, order=NGRAM):
        self.alpha = alpha
        self.order = order
        counts = lm_data['counts']
        self.c1 = counts['1']
        self.nest = {o: counts[str(o)] for o in range(2, order + 1)}
        self.tot = {}
        for o in range(2, order + 1):
            t = collections.Counter()
            for ctx, d in self.nest[o].items():
                t[ctx] = sum(d.values())
            self.tot[o] = t
        self.N1 = sum(self.c1.values())
        self._cache = {}

    def logp(self, ch, ctx):
        ctx = ctx[-(self.order - 1):] if len(ctx) > self.order - 1 else ctx
        key = (ctx, ch)
        v = self._cache.get(key)
        if v is None:
            v = self._logp(ch, ctx)
            self._cache[key] = v
        return v

    def _logp(self, ch, ctx):
        p = self.c1.get(ch, 0) / self.N1
        if p <= 0:
            p = 1e-12
        for o in range(2, self.order + 1):
            if len(ctx) < o - 1:
                break
            cc = ctx[-(o - 1):]
            d = self.nest[o].get(cc)
            num = d.get(ch, 0) if d else 0
            den = self.tot[o].get(cc, 0)
            p = (num + self.alpha * p) / (den + self.alpha)
        return math.log(max(p, 1e-300))


# ------------------------------------------------------------ Aho-Corasick
class AhoCorasick:
    """Multi-pattern string matcher summing pattern weights (overlapping)."""

    def __init__(self, patterns):
        # patterns: iterable of (string, weight)
        self.max_len = 0
        self.next = [{}]
        self.fail = [0]
        self.out = [0.0]
        for s, w in patterns:
            if len(s) > self.max_len:
                self.max_len = len(s)
            node = 0
            for ch in s:
                nxt = self.next[node].get(ch)
                if nxt is None:
                    nxt = len(self.next)
                    self.next[node][ch] = nxt
                    self.next.append({})
                    self.fail.append(0)
                    self.out.append(0.0)
                node = nxt
            self.out[node] += w
        # BFS fail links; propagate outputs
        q = collections.deque()
        for ch, nxt in self.next[0].items():
            self.fail[nxt] = 0
            q.append(nxt)
        while q:
            r = q.popleft()
            for ch, nxt in self.next[r].items():
                q.append(nxt)
                f = self.fail[r]
                while f and ch not in self.next[f]:
                    f = self.fail[f]
                self.fail[nxt] = self.next[f].get(ch, 0)
                self.out[nxt] += self.out[self.fail[nxt]]

    def scan(self, s):
        node, tot = 0, 0.0
        for ch in s:
            while node and ch not in self.next[node]:
                node = self.fail[node]
            node = self.next[node].get(ch, 0)
            tot += self.out[node]
        return tot


# --------------------------------------------------------------- inventory
def load_inventory(mode, pins, soft, lex_wt):
    """Inventory of candidate value strings.
    'units': exactly data/upstream-syll.py UNITS (task-brief literal).
    'extended' (default): UNITS + top-200 encipher_split cells from the
      Tocqueville reference (the control generator plants from encipher_split
      cells; strict UNITS misses ~20% of them -- measured in METHOD.md)."""
    import re
    lane = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
    src = open(os.path.join(lane, 'data', 'upstream-syll.py')).read()
    m = re.search(r"UNITS = list\('([^']+)'\) \+ '''(.*?)'''\.split\(\)",
                  src, re.S)
    units = list(m.group(1)) + m.group(2).split()
    inv = list(units)
    if mode == 'extended':
        sys.path.insert(0, os.path.join(lane, 'code', 'crowd2'))
        from scorer_smith import syllabify, encipher_split  # noqa: E402
        from build_lm import load_words  # noqa: E402
        cnt = collections.Counter()
        for w in load_words():
            for c in encipher_split(syllabify(w)):
                cnt[c] += 1
        for c, _ in cnt.most_common(200):
            if c not in inv:
                inv.append(c)
    for v in list(pins.values()) + list(soft.values()):
        if v not in inv:
            inv.append(v)
    weights = [1.0 + lex_wt.get(project(v), 0.0) for v in inv]
    return inv, weights


# ------------------------------------------------------------------ solver
class Solver:
    def __init__(self, pairs, pins, soft, inventory, inv_weights, lm, ac,
                 phase_info, cfg, rng, lex_wt):
        self.gs = list(pairs)
        self.N = len(pairs)
        self.pins = dict(pins)
        self.soft = dict(soft)
        self.inv = list(inventory)
        self.cfg = cfg
        self.rng = rng
        self.lm = lm
        self.ac = ac
        self.MAXW = ac.max_len if ac else 0
        self.groups = sorted(set(pairs))
        self.nonpin = [g for g in self.groups if g not in self.pins]
        self.occ = collections.defaultdict(list)
        for t, g in enumerate(self.gs):
            self.occ[g].append(t)
        # phase: adjacency + gate
        self.adj = {g: [(h, j) for h, j in phase_info['adj'].get(g, [])
                        if h in self.groups]
                    for g in self.groups}
        self.beta = cfg['beta0'] * phase_info['gate']
        self.chi2 = phase_info['chi2']
        self.gate = phase_info['gate']
        # projected values
        self.pv = {v: project(v) for v in self.inv}
        for v in self.pins.values():
            self.pv.setdefault(v, project(v))
        # sampling weights
        tot = float(sum(inv_weights))
        self._cumw = []
        acc = 0.0
        for w in inv_weights:
            acc += w / tot
            self._cumw.append(acc)
        # state
        self.v1, self.v2, self.w2 = {}, {}, {}
        self.pcell = [None] * self.N
        self.Fs = [0.0] * self.N
        self.chars = []
        self.coff = []
        self.S_char = 0.0
        self.S_ac = 0.0      # Aho-Corasick hit total (all hits)
        self.S_single = 0.0  # single-value hit total (subtracted)
        self.S_potts = 0.0
        self.S_soft = 0.0
        self.n_poly = 0
        self._fcache = {}
        # lex_wt is keyed by PROJECTED strings already, so the single-value
        # hit weight of a decoded position is lex_wt.get(pcell[t], 0.0)
        self.lex_wt = lex_wt
        # concentration counts (maintained incrementally; rebuilt by init_key)
        self.cnt_v = collections.Counter()
        self.S_conc = 0.0

    def _conc_f(self, n):
        cap = self.cfg['conc_cap']
        return (n - cap) ** 2 if n > cap else 0.0

    def _set_v1(self, g, new_v):
        """Change v1[g], maintaining cnt_v (over PROJECTED values) and
        S_conc."""
        old_v = self.v1[g]
        if old_v == new_v:
            return
        old_p, new_p = self.pv[old_v], self.pv[new_v]
        if old_p != new_p:
            # remove from old projected value
            n = self.cnt_v[old_p]
            self.S_conc += self._conc_f(n - 1) - self._conc_f(n)
            self.cnt_v[old_p] = n - 1
            if self.cnt_v[old_p] <= 0:
                del self.cnt_v[old_p]
            # add to new projected value
            n = self.cnt_v.get(new_p, 0)
            self.S_conc += self._conc_f(n + 1) - self._conc_f(n)
            self.cnt_v[new_p] = n + 1
        self.v1[g] = new_v

    def _rebuild_conc(self):
        self.cnt_v = collections.Counter(self.pv[self.v1[g]]
                                         for g in self.groups)
        cap = self.cfg['conc_cap']
        self.S_conc = sum((n - cap) ** 2 for n in self.cnt_v.values()
                          if n > cap)

    # -- scoring primitives ------------------------------------------------
    def F(self, ca, cb):
        key = (ca, cb)
        v = self._fcache.get(key)
        if v is None:
            hist = (START * (NGRAM - 1) + ca)[-(NGRAM - 1):] \
                if ca != START else START * (NGRAM - 1)
            t = 0.0
            h = hist
            for ch in cb:
                t += self.lm.logp(ch, h)
                h = (h + ch)[-(NGRAM - 1):]
            v = self._fcache[key] = t
        return v

    def choose(self, t):
        g = self.gs[t]
        o1 = self.pv[self.v1[g]]
        if self.v2[g] is None:
            return o1
        o2 = self.pv[self.v2[g]]
        ca = self.pcell[t - 1] if t > 0 else START
        cb = self.pcell[t + 1] if t + 1 < self.N else None
        s1 = self.F(ca, o1) + (self.F(o1, cb) if cb else 0.0)
        s2 = self.F(ca, o2) + (self.F(o2, cb) if cb else 0.0)
        w2 = min(max(self.w2[g], 1e-6), 1 - 1e-6)
        return o2 if s2 + math.log(w2) > s1 + math.log(1 - w2) else o1

    def total(self):
        c = self.cfg
        s_word = (self.S_ac - self.S_single) if self.ac else 0.0
        return (self.S_char + c['lambda_word'] * s_word
                + self.S_potts + self.S_soft
                - c['lambda_poly'] * self.n_poly
                - c['lambda_conc'] * self.S_conc)

    # -- init --------------------------------------------------------------
    def _sample_value(self, exclude=()):
        for _ in range(8):
            v = self.inv[bisect.bisect(self._cumw, self.rng.random())]
            if v not in exclude:
                return v
        return self.rng.choice(self.inv)

    def init_key(self):
        for g in self.groups:
            if g in self.pins:
                self.v1[g] = self.pins[g]
                self.v2[g] = None
                self.w2[g] = 0.0
            elif self.cfg['init'] == 'freqmatch':
                self.v1[g] = None  # filled below
                self.v2[g] = None
                self.w2[g] = 0.0
            else:
                self.v1[g] = self._sample_value()
                self.v2[g] = None
                self.w2[g] = 0.0
        if self.cfg['init'] == 'freqmatch':
            byfreq = sorted(self.nonpin, key=lambda g: -len(self.occ[g]))
            wts = [self._cumw[i] - (self._cumw[i - 1] if i else 0)
                   for i in range(len(self.inv))]
            order = sorted(range(len(self.inv)), key=lambda i: -wts[i])
            for g, i in zip(byfreq, order):
                self.v1[g] = self.inv[i]
            for g in byfreq[len(order):]:
                self.v1[g] = self._sample_value()
        self._rebuild_conc()
        self._full_refresh()

    def _full_refresh(self):
        self.pcell = [self.pv[self.v1[g]] for g in self.gs]
        # full E-step fixpoint (preserves polyvalent choices)
        for _ in range(10):
            moved = False
            for t in range(self.N):
                nv = self.choose(t)
                if nv != self.pcell[t]:
                    self.pcell[t] = nv
                    moved = True
            if not moved:
                break
        for g in self.groups:
            if self.v2[g] is not None:
                n2 = sum(1 for t in self.occ[g]
                         if self.pcell[t] == self.pv[self.v2[g]])
                self.w2[g] = (n2 + 1.0) / (len(self.occ[g]) + 2.0)
        self.S_char = 0.0
        for t in range(self.N):
            ca = self.pcell[t - 1] if t > 0 else START
            self.Fs[t] = self.F(ca, self.pcell[t])
            self.S_char += self.Fs[t]
        self._rebuild_chars()
        self.S_ac = self.ac.scan(self._charstr()) if self.ac else 0.0
        self.S_single = (sum(self.lex_wt.get(self.pcell[t], 0.0)
                             for t in range(self.N))
                         if self.ac else 0.0)
        self.S_potts = self._potts_all()
        self.S_soft = sum(self.cfg['w_soft'] for g, v in self.soft.items()
                          if self.v1.get(g) == v)
        self.n_poly = sum(1 for g in self.groups if self.v2[g] is not None)

    def _potts_all(self):
        s, seen = 0.0, set()
        for g in self.groups:
            for h, j in self.adj[g]:
                key = (g, h) if g < h else (h, g)
                if key in seen:
                    continue
                seen.add(key)
                if self.v1[g] == self.v1[h]:
                    s += self.beta * j
        return s

    def _potts_touched(self, touched, v1map):
        s, seen = 0.0, set()
        for g in touched:
            for h, j in self.adj[g]:
                key = (g, h) if g < h else (h, g)
                if key in seen:
                    continue
                seen.add(key)
                if v1map[g] == v1map[h]:
                    s += self.beta * j
        return s

    def _rebuild_chars(self):
        self.chars = list(''.join(self.pcell))
        self.coff = []
        o = 0
        for p in self.pcell:
            self.coff.append(o)
            o += len(p)

    def _charstr(self):
        return ''.join(self.chars)

    # -- word windows --------------------------------------------------------
    def _windows(self, R):
        spans = sorted((self.coff[t], self.coff[t] + len(self.pcell[t]))
                       for t in R)
        clusters = []
        for s0, s1 in spans:
            if clusters and s0 - clusters[-1][1] < 2 * self.MAXW:
                if s1 > clusters[-1][1]:
                    clusters[-1][1] = s1
            else:
                clusters.append([s0, s1])
        return [(max(0, c0 - self.MAXW), c1 + self.MAXW)
                for c0, c1 in clusters]

    def _scan_windows(self, windows):
        s = ''.join(self.chars)
        return sum(self.ac.scan(s[w0:w1]) for w0, w1 in windows)

    # -- snapshot / revert ---------------------------------------------------
    def _region(self, touched):
        A = set()
        for g in touched:
            A.update(self.occ[g])
        R = set(A)
        for t in A:
            if t > 0:
                R.add(t - 1)
            if t + 1 < self.N:
                R.add(t + 1)
        R2 = set(R)
        for t in R:
            if t + 1 < self.N:
                R2.add(t + 1)
        return A, R, R2

    def snapshot(self, touched, R, R2):
        return {
            'touched': touched,
            'key': {g: (self.v1[g], self.v2[g], self.w2[g]) for g in touched},
            'pcell': {t: self.pcell[t] for t in R},
            'Fs': {t: self.Fs[t] for t in R2},
            'S_char': self.S_char, 'S_ac': self.S_ac,
            'S_single': self.S_single, 'S_conc': self.S_conc,
            'cnt_v': dict(self.cnt_v),
            'S_potts': self.S_potts, 'S_soft': self.S_soft,
            'n_poly': self.n_poly,
        }

    def revert(self, snap):
        for g, (a, b, w) in snap['key'].items():
            self.v1[g], self.v2[g], self.w2[g] = a, b, w
        for t, v in snap['pcell'].items():
            self.pcell[t] = v
        for t, v in snap['Fs'].items():
            self.Fs[t] = v
        self.S_char = snap['S_char']
        self.S_ac = snap['S_ac']
        self.S_single = snap['S_single']
        self.S_conc = snap['S_conc']
        self.cnt_v = collections.Counter(snap['cnt_v'])
        self.S_potts = snap['S_potts']
        self.S_soft = snap['S_soft']
        self.n_poly = snap['n_poly']
        self._rebuild_chars()

    def _word_totals(self):
        s_word = (self.S_ac - self.S_single) if self.ac else 0.0
        return s_word

    # -- moves -----------------------------------------------------------------
    def propose_value(self, g, exclude=()):
        # 20%: copy a contact-neighbor's v1 (homophone-pool proposal)
        if self.rng.random() < 0.20 and self.adj[g]:
            cands = [h for h, _ in self.adj[g][:5] if h not in self.pins]
            if cands:
                v = self.v1[self.rng.choice(cands)]
                if v not in exclude:
                    return v
        r = self.rng.random()
        if r < 0.65:
            return self._sample_value(exclude)
        for _ in range(8):
            v = self.rng.choice(self.inv)
            if v not in exclude:
                return v
        return self.rng.choice(self.inv)

    def apply_key_change(self, touched, change):
        """change: dict g -> (v1|None, v2|None, w2|None); None = keep.
        Returns (potts_delta, soft_delta, npoly_delta)."""
        old_potts = self._potts_touched(touched, self.v1)
        old_soft = sum(self.cfg['w_soft'] for g in touched
                       if g in self.soft and self.v1[g] == self.soft[g])
        old_np = sum(1 for g in touched if self.v2[g] is not None)
        for g, (a, b, w) in change.items():
            if a is not None:
                self._set_v1(g, a)
            if b != 'keep':
                self.v2[g] = b
            if w is not None:
                self.w2[g] = w
        new_potts = self._potts_touched(touched, self.v1)
        new_soft = sum(self.cfg['w_soft'] for g in touched
                       if g in self.soft and self.v1[g] == self.soft[g])
        new_np = sum(1 for g in touched if self.v2[g] is not None)
        self.S_potts += new_potts - old_potts
        self.S_soft += new_soft - old_soft
        self.n_poly += new_np - old_np
        return new_np - old_np

    def rechoose(self, R, touched):
        for _ in range(8):
            moved = False
            for t in R:
                nv = self.choose(t)
                if nv != self.pcell[t]:
                    self.pcell[t] = nv
                    moved = True
            if not moved:
                break
        for g in touched:
            if self.v2[g] is not None:
                n2 = sum(1 for t in self.occ[g]
                         if self.pcell[t] == self.pv[self.v2[g]])
                self.w2[g] = (n2 + 1.0) / (len(self.occ[g]) + 2.0)

    def refresh_Fs(self, R2):
        for t in R2:
            ca = self.pcell[t - 1] if t > 0 else START
            new = self.F(ca, self.pcell[t])
            self.S_char += new - self.Fs[t]
            self.Fs[t] = new

    def propose_move(self, g):
        """Draw and apply one move on non-pin g. Returns (delta, snap)."""
        r = self.rng.random()
        if r < 0.55:
            branch = 'chg1'
        elif r < 0.70:
            branch = 'swap'
        elif r < 0.85:
            branch = 'poly'
        elif r < 0.95:
            branch = 'chg2'
        else:
            branch = 'block'
        touched = {g}
        change = {}
        if branch == 'chg1':
            new = self.propose_value(g, exclude=(self.v1[g],))
            if new == self.v2[g]:
                change[g] = (new, self.v1[g], self.w2[g])  # promote v2
            else:
                change[g] = (new, 'keep', None)
        elif branch == 'swap':
            h = self.rng.choice(self.nonpin)
            if h == g:
                return 0.0, None
            touched = {g, h}
            change[g] = (self.v1[h], 'keep', None)
            change[h] = (self.v1[g], 'keep', None)
        elif branch == 'poly':
            if self.v2[g] is None:
                change[g] = (None, self.propose_value(
                    g, exclude=(self.v1[g],)), 0.5)
            else:
                change[g] = (None, None, 0.0)
        elif branch == 'chg2':
            if self.v2[g] is None:
                change[g] = (None, self.propose_value(
                    g, exclude=(self.v1[g],)), 0.5)
            else:
                change[g] = (None, self.propose_value(
                    g, exclude=(self.v1[g], self.v2[g])), None)
        else:  # block
            new = self.propose_value(g)
            nb = [h for h, _ in self.adj[g][:3] if h not in self.pins]
            touched = {g} | set(nb)
            for x in touched:
                change[x] = (new, 'keep', None)
        A, R, R2 = self._region(touched)
        old_windows = self._windows(R) if self.ac else []
        old_hits = self._scan_windows(old_windows)
        snap = self.snapshot(touched, R, R2)
        self.apply_key_change(touched, change)
        self.rechoose(R, touched)
        self.refresh_Fs(R2)
        self._rebuild_chars()
        new_windows = self._windows(R) if self.ac else []
        new_hits = self._scan_windows(new_windows)
        if self.ac:
            self.S_ac += new_hits - old_hits
            old_single_R = sum(self.lex_wt.get(snap['pcell'][t], 0.0)
                               for t in R)
            new_single_R = sum(self.lex_wt.get(self.pcell[t], 0.0)
                               for t in R)
            self.S_single += new_single_R - old_single_R
        new_total = self.total()
        # delta from snapshot totals
        c = self.cfg
        old_s_word = ((snap['S_ac'] - snap['S_single'])
                      if self.ac else 0.0)
        old_total = (snap['S_char'] + c['lambda_word'] * old_s_word
                     + snap['S_potts'] + snap['S_soft']
                     - c['lambda_poly'] * snap['n_poly']
                     - c['lambda_conc'] * snap['S_conc'])
        return new_total - old_total, snap

    # -- annealing -------------------------------------------------------------
    def anneal(self, iters, t0, tmin, log_every=0):
        self.init_key()
        cur = self.total()
        best = cur
        best_state = (dict(self.v1), dict(self.v2), dict(self.w2))
        cool = (tmin / t0) ** (1.0 / iters)
        T, acc, moves = t0, 0, 0
        for it in range(iters):
            g = self.rng.choice(self.nonpin)
            delta, snap = self.propose_move(g)
            if snap is None:
                continue
            moves += 1
            if delta >= 0 or self.rng.random() < math.exp(delta / T):
                cur += delta
                acc += 1
                if cur > best:
                    best = cur
                    best_state = (dict(self.v1), dict(self.v2),
                                  dict(self.w2))
            else:
                self.revert(snap)
            T *= cool
            if log_every and (it + 1) % log_every == 0:
                print('    it %d/%d T=%.3f cur=%.1f best=%.1f acc=%.3f' %
                      (it + 1, iters, T, cur, best, acc / max(moves, 1)),
                      flush=True)
        self.v1, self.v2, self.w2 = best_state
        self._full_refresh()
        return {'best': best, 'acc_rate': acc / max(moves, 1),
                'final': self.total()}

    # -- greedy refine -----------------------------------------------------------
    def refine(self, n_sweeps=3, n_cand=25):
        for _ in range(n_sweeps):
            improved = False
            for g in self.nonpin:
                cands = set()
                cands.add(self.v1[g])
                for _ in range(n_cand - 1):
                    cands.add(self.propose_value(g))
                best_v, best_d = self.v1[g], 0.0
                for v in cands:
                    if v == self.v1[g]:
                        continue
                    A, R, R2 = self._region({g})
                    old_windows = self._windows(R) if self.ac else []
                    old_hits = self._scan_windows(old_windows)
                    snap = self.snapshot({g}, R, R2)
                    self.apply_key_change({g}, {g: (v, 'keep', None)})
                    self.rechoose(R, {g})
                    self.refresh_Fs(R2)
                    self._rebuild_chars()
                    new_hits = self._scan_windows(
                        self._windows(R) if self.ac else [])
                    if self.ac:
                        self.S_ac += new_hits - old_hits
                        self.S_single += (
                            sum(self.lex_wt.get(self.pcell[t], 0.0)
                                for t in R)
                            - sum(self.lex_wt.get(snap['pcell'][t], 0.0)
                                  for t in R))
                    old_s_word = ((snap['S_ac'] - snap['S_single'])
                                  if self.ac else 0.0)
                    d = self.total() - (
                        snap['S_char'] + self.cfg['lambda_word'] *
                        old_s_word + snap['S_potts'] + snap['S_soft']
                        - self.cfg['lambda_poly'] * snap['n_poly']
                        - self.cfg['lambda_conc'] * snap['S_conc'])
                    if d > best_d:
                        best_d, best_v = d, v
                    self.revert(snap)
                if best_d > 1e-9:
                    A, R, R2 = self._region({g})
                    old_windows = self._windows(R) if self.ac else []
                    old_hits = self._scan_windows(old_windows)
                    old_single_R = (sum(
                        self.lex_wt.get(self.pcell[t], 0.0) for t in R)
                        if self.ac else 0.0)
                    self.apply_key_change({g}, {g: (best_v, 'keep', None)})
                    self.rechoose(R, {g})
                    self.refresh_Fs(R2)
                    self._rebuild_chars()
                    new_hits = self._scan_windows(
                        self._windows(R) if self.ac else [])
                    if self.ac:
                        self.S_ac += new_hits - old_hits
                        self.S_single += (
                            sum(self.lex_wt.get(self.pcell[t], 0.0)
                                for t in R) - old_single_R)
                    improved = True
            if not improved:
                break


# ------------------------------------------------------- self-test / driver
def verify_incremental(pairs, pins, soft, inv, inv_w, lm, ac, phase_info,
                       cfg, seed=7, n_moves=300, lex_wt=None):
    """Self-test: the incrementally maintained objective components must
    equal a from-scratch recompute from the current (key, pcell) after random
    moves. Returns (ok, info)."""
    rng = random.Random(seed)
    m = Solver(pairs, pins, soft, inv, inv_w, lm, ac, phase_info, cfg, rng,
               lex_wt or {})

    def s_word_of(snap_like):
        return ((snap_like['S_ac'] - snap_like['S_single'])
                if m.ac else 0.0)

    m.init_key()
    maxerr = 0.0

    def recompute():
        s_char = 0.0
        for t in range(m.N):
            ca = m.pcell[t - 1] if t > 0 else START
            s_char += m.F(ca, m.pcell[t])
        s_ac = m.ac.scan(''.join(m.pcell)) if m.ac else 0.0
        s_single = (sum(m.lex_wt.get(m.pcell[t], 0.0)
                        for t in range(m.N)) if m.ac else 0.0)
        s_potts = m._potts_all()
        s_soft = sum(m.cfg['w_soft'] for g, v in m.soft.items()
                     if m.v1.get(g) == v)
        n_poly = sum(1 for g in m.groups if m.v2[g] is not None)
        cnt = collections.Counter(m.pv[m.v1[g]] for g in m.groups)
        cap = cfg['conc_cap']
        s_conc = sum((n - cap) ** 2 for n in cnt.values() if n > cap)
        return {'S_char': s_char, 'S_ac': s_ac, 'S_single': s_single,
                'S_conc': s_conc, 'S_potts': s_potts, 'S_soft': s_soft,
                'n_poly': n_poly}

    for i in range(n_moves):
        g = rng.choice(m.nonpin)
        delta, snap = m.propose_move(g)
        if snap is None:
            continue
        before = (snap['S_char'] + cfg['lambda_word'] * s_word_of(snap)
                  + snap['S_potts'] + snap['S_soft']
                  - cfg['lambda_poly'] * snap['n_poly']
                  - cfg['lambda_conc'] * snap['S_conc'])
        if abs((m.total() - before) - delta) > 1e-6:
            return False, {'move': i, 'kind': 'delta-mismatch',
                           'delta': delta, 'moved': m.total() - before}
        full = recompute()
        got = {'S_char': m.S_char, 'S_ac': m.S_ac, 'S_single': m.S_single,
               'S_conc': m.S_conc, 'S_potts': m.S_potts,
               'S_soft': m.S_soft, 'n_poly': m.n_poly}
        for k in full:
            err = abs(full[k] - got[k])
            maxerr = max(maxerr, err)
            if err > 1e-6:
                return False, {'move': i, 'kind': f'{k}-mismatch',
                               'full': full[k], 'inc': got[k]}
    return True, {'max_abs_err': maxerr, 'n_moves': n_moves}


def load_pairs_file(path):
    """Load a pair stream. Accepts:
    - JSON: {"pairs": [...], ...} (control instances use a .txt variant, see
      control_harness.load_synthetic)
    - text: whitespace-separated pairs, '#' comments."""
    with open(path) as f:
        txt = f.read()
    if path.endswith('.json'):
        return json.loads(txt)['pairs']
    pairs = []
    for line in txt.splitlines():
        line = line.split('#')[0].strip()
        if line:
            pairs.extend(line.split())
    return pairs


def build_solver(pairs, pins, soft, lm_path, cfg, seed, no_phase, no_word,
                 no_poly, no_soft, inventory_mode, init):
    lm_data = json.load(open(lm_path))
    lm = CharLM(lm_data)
    ac = None
    if not no_word:
        ac = AhoCorasick([(e['w'], e['wt']) for e in lm_data['lexicon']])
    lex_wt = {e['w']: e['wt'] for e in lm_data['lexicon']}
    inv, inv_w = load_inventory(inventory_mode, pins,
                               {} if no_soft else soft, lex_wt)
    phase_info = analyze_stream(pairs)
    if no_phase:
        phase_info = dict(phase_info, gate=0.0)
    cfg = dict(cfg)
    cfg['init'] = init
    if no_poly:
        cfg = dict(cfg)
    rng = random.Random(seed)
    solver = Solver(pairs, pins, {} if no_soft else soft, inv, inv_w, lm, ac,
                    phase_info, cfg, rng, lex_wt)
    solver._no_poly_flag = no_poly
    return solver, lm_data, phase_info


def run_restarts(pairs, pins, soft, lm_path, cfg, out_dir, seed,
                 no_phase=False, no_word=False, no_poly=False, no_soft=False,
                 inventory_mode=None, init=None, refine=None):
    cfg = dict(DEFAULTS, **cfg)
    inventory_mode = inventory_mode or cfg['inventory_mode']
    init = init or cfg['init']
    if refine is None:
        refine = cfg['refine']
    os.makedirs(out_dir, exist_ok=True)
    print(f'[solver] pairs={len(pairs)} groups={len(set(pairs))} '
          f'config={json.dumps({k: cfg[k] for k in ("restarts", "iters", "t0", "tmin", "lambda_word", "beta0", "w_soft", "lambda_poly")})}',
          flush=True)
    t_start = time.time()
    restarts = []
    beta0 = None
    for r in range(cfg['restarts']):
        rs = seed + 7919 * r
        solver, lm_data, phase_info = build_solver(
            pairs, pins, soft, lm_path, cfg, rs, no_phase, no_word, no_poly,
            no_soft, inventory_mode, init)
        if beta0 is None:
            beta0 = solver.beta
        if r == 0:
            print(f'[solver] inventory={len(solver.inv)} chi2={phase_info["chi2"]} '
                  f'gate={phase_info["gate"]} beta={solver.beta:.3f} '
                  f'maxw={solver.MAXW}', flush=True)
            # projection-collision diagnostic: inventory values that project
            # identically are indistinguishable to S_char/S_word
            proj = collections.Counter(solver.pv[v] for v in solver.inv)
            ncoll = sum(1 for v in solver.inv if proj[solver.pv[v]] > 1)
            print(f'[solver] inventory projection collisions: {ncoll} values '
                  f'share a projected form', flush=True)
        a = solver.anneal(cfg['iters'], cfg['t0'], cfg['tmin'],
                          log_every=0)
        if refine:
            solver.refine()
        res = {'seed': rs, 'best': a['best'], 'final': a['final'],
               'acc_rate': round(a['acc_rate'], 4),
               'assignment': {g: {'v1': solver.v1[g], 'v2': solver.v2[g],
                                  'w2': round(solver.w2[g], 4)}
                              for g in solver.groups},
               'score_parts': {
                   'S_char': round(solver.S_char, 2),
                   'S_word': round(solver._word_totals(), 2),
                   'S_ac': round(solver.S_ac, 2),
                   'S_single': round(solver.S_single, 2),
                   'S_conc': round(solver.S_conc, 2),
                   'S_potts': round(solver.S_potts, 3),
                   'S_soft': round(solver.S_soft, 3),
                   'n_poly': solver.n_poly}}
        restarts.append(res)
        print(f'[solver] restart {r}: best={a["best"]:.1f} '
              f'final={a["final"]:.1f} acc={a["acc_rate"]:.3f} '
              f'npoly={solver.n_poly} ({time.time()-t_start:.0f}s)',
              flush=True)
    restarts.sort(key=lambda d: -d['best'])
    best = restarts[0]
    # marginals: fraction of restarts with v1[g]==v (top 5)
    marginals = {}
    for g in sorted(set(pairs)):
        c = collections.Counter(r['assignment'][g]['v1'] for r in restarts)
        n = len(restarts)
        marginals[g] = [[v, round(f / n, 4)] for v, f in c.most_common(5)]
    # random-key baseline (optimization sanity)
    rb = []
    for i in range(20):
        solver, _, _ = build_solver(pairs, pins, soft, lm_path, cfg,
                                    seed + 50000 + i, no_phase, no_word,
                                    no_poly, no_soft, inventory_mode, init)
        solver.init_key()
        rb.append(solver.total())
    baseline = {'n': len(rb), 'max': round(max(rb), 1),
                'mean': round(sum(rb) / len(rb), 1)}
    result = {
        'meta': {
            'solver': 'side-homophonic/solver.py',
            'date': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'n_pairs': len(pairs), 'n_groups': len(set(pairs)),
            'pins': pins, 'soft_anchors': {} if no_soft else soft,
            'no_phase': no_phase, 'no_word': no_word, 'no_poly': no_poly,
            'inventory_mode': inventory_mode, 'init': init,
            'wall_seconds': round(time.time() - t_start, 1),
        },
        'config': cfg,
        'phase': {'chi2': phase_info['chi2'], 'gate': phase_info['gate'],
                  'beta': round(beta0, 4)},
        'baseline_random20': baseline,
        'best': best,
        'restarts': restarts,
        'marginals': marginals,
    }
    with open(os.path.join(out_dir, 'result.json'), 'w') as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    margin = best['best'] - baseline['max']
    print(f'[solver] BEST restart {best["seed"]}: {best["best"]:.1f} vs '
          f'random20 max {baseline["max"]:.1f} (margin {margin:+.1f} nats)',
          flush=True)
    print(f'[solver] wrote {out_dir}/result.json', flush=True)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pairs', required=True)
    ap.add_argument('--lm', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--config', default=os.path.join(HERE, 'config.json'))
    ap.add_argument('--anchors', default=None,
                    help='JSON {"11":"la",...} hard pins')
    ap.add_argument('--anchors-file', default=None,
                    help='JSON file with an "anchors" object (e.g. the '
                         'control crib file)')
    ap.add_argument('--soft', default=None,
                    help='JSON {"87":"ce",...} soft priors')
    ap.add_argument('--seed', type=int, default=DEFAULTS['seed'])
    ap.add_argument('--restarts', type=int, default=None)
    ap.add_argument('--iters', type=int, default=None)
    ap.add_argument('--init', default=None, choices=['random', 'freqmatch'])
    ap.add_argument('--inventory-mode', default=None,
                    choices=['units', 'extended'])
    ap.add_argument('--no-phase', action='store_true')
    ap.add_argument('--no-word', action='store_true')
    ap.add_argument('--no-poly', action='store_true')
    ap.add_argument('--no-soft', action='store_true')
    ap.add_argument('--no-refine', action='store_true')
    ap.add_argument('--self-test', action='store_true',
                    help='verify incremental scoring, then exit')
    a = ap.parse_args()
    cfg = dict(DEFAULTS)
    if os.path.exists(a.config):
        cfg.update(json.load(open(a.config)))
    if a.restarts:
        cfg['restarts'] = a.restarts
    if a.iters:
        cfg['iters'] = a.iters
    pairs = load_pairs_file(a.pairs)
    pins = json.loads(a.anchors) if a.anchors else {}
    if a.anchors_file:
        pins.update(json.load(open(a.anchors_file))['anchors'])
    soft = json.loads(a.soft) if a.soft else {}
    if a.self_test:
        lm_data = json.load(open(a.lm))
        lm = CharLM(lm_data)
        ac = AhoCorasick([(e['w'], e['wt']) for e in lm_data['lexicon']])
        lex_wt = {e['w']: e['wt'] for e in lm_data['lexicon']}
        inv, inv_w = load_inventory('units', pins, soft, lex_wt)
        phase_info = analyze_stream(pairs)
        ok, info = verify_incremental(pairs, pins, soft, inv, inv_w, lm, ac,
                                      phase_info, cfg, lex_wt=lex_wt)
        print('SELF-TEST', 'PASS' if ok else 'FAIL', info, flush=True)
        raise SystemExit(0 if ok else 1)
    run_restarts(pairs, pins, soft, a.lm, cfg, a.out, a.seed,
                 no_phase=a.no_phase, no_word=a.no_word, no_poly=a.no_poly,
                 no_soft=a.no_soft, inventory_mode=a.inventory_mode,
                 init=a.init, refine=not a.no_refine)


if __name__ == '__main__':
    main()
