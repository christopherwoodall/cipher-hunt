#!/usr/bin/env python3
"""JOINT DECIPHERMENT ENGINE — round 4, scorer-smith work order 8.

Lane: zeschau-seebach-1841.

ARCHITECTURE (why this, not round 3 again)
------------------------------------------
Round 3 (N16) proved per-group consistency scoring is real-but-not-distinctive:
bigram contexts underdetermine one cell at a time. The missing ingredient is
JOINT inference: every group's value must satisfy ALL of its occurrences'
contexts SIMULTANEOUSLY, under one key, with the groups constraining each
other. This engine does simulated annealing over the FULL 96-group key.

F30 COMPLIANCE (rigid syllabification is dead):
  The engine NEVER scores era syllable-bigram conditionals on morphological
  fragments. The sequential plaintext model is at the LETTER level: the
  encipherer "spells by ear and cuts inconsistently" (frenchman, F30), so the
  letters are the reliable level — whatever the cutting, the concatenated
  letters approximate French spelling. Era letter trigram log-probs score the
  decoded letter stream. The rule syllabifier is used ONLY to build the
  CANDIDATE cell inventory (a word list, not a conditional model).

STATE SPACE
-----------
Key K: for each group g in 96: v1[g] (primary cell, str), v2[g] (secondary
cell or None = polyvalence), w2[g] (P(use v2), M-step closed form).
Pins: 7 ground-truth anchors have v1 fixed, v2=None fixed (hard).
Per-occurrence decoding pcell[t]: single groups -> v1; polyvalent groups ->
per-occurrence argmax over {v1,v2} of local trigram score + log weight
(hard E-step; the "conditioned weights" of the work order).

SCORE (to maximize)
-------------------
S(K) = S_letter + LAM_ROT * S_phase + S_prior - LAM_POLY * n_poly, where
  S_letter = sum_t F(pcell[t-1], pcell[t])   [era letter trigram log-probs;
             F(ca,cb) scores cb's letters given ca's last 2 letters; t=0 uses
             a start sentinel]
  S_phase  = sum_{v,phi} n(v,phi) * log((n(v,phi)+a)/(n(v)+4a))
             [rotation-aware transition prior: profile log-likelihood of the
             group phase given the decoded cell. Phases are the banked
             Jaccard-k12 contactor blocks (A->C->B->A, chi2=181.3). Anchors
             have coherent phase signatures (29=er: prev-A .77/next-B .89);
             this term rewards keys whose cells do too. Cipher-side geometry,
             no era conditionals.]
  S_prior  = BETA_PROV * #{g: v1[g] == provisional hint}   [soft priors]
  n_poly   = #{g: v2[g] is not None}                      [sparsity penalty]

All terms maintained incrementally; a move touching group g re-scores only
g's occurrences (+ neighbor relaxation for adjacent polyvalent groups).

MOVES: change v1 (freq-weighted/uniform inventory sample), swap v1 with
another group, add/drop/change v2 (polyvalence).
ANNEALING: geometric T0->T1 over S sweeps (one move per non-pin group/sweep),
R restarts, keep best. MARGINALS: low-T sampling sweeps from the best key,
recording per-occurrence decoded cells -> P(cell|g).

Deterministic given seed. No invented ciphertext: real stream via
crib_attack.load_pairs; the only synthetic stream is the labelled control
(synth_control.py).
"""

import bisect
import collections
import json
import math
import os
import random
import sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd2'))
from crib_attack import load_pairs  # noqa: E402 (verified loader, 1846 pairs)
from scorer_smith import build_models  # noqa: E402

DATA = os.path.join(LANE, 'data')
OUTD = os.path.join(LANE, 'code', 'crowd4')

SEED = 1841
ALPHA_TRI = 0.1      # add-alpha for the letter trigram
ALPHA_PH = 1.0       # add-alpha for the phase profile
BETA_PROV = 3.0      # soft-prior bonus per matched provisional (nats)
LAM_ROT = 1.0        # default; ablated on the control
LAM_POLY = 15.0      # default; ablated on the control
INVENTORY_TOP = 600  # top-N corpus syllable units in the candidate inventory

PINS = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i',
        '29': 'er', '40': 'e', '46': 'que'}
# provisional soft priors for the R5005 run (NOT pins)
PROVISIONAL = {'87': 'ce', '64': 'qui', '96': 'par', '94': 'ne', '62': 'on'}

START = '^'  # letter-stream start sentinel


# ---------------------------------------------------------------- models
def build_letter_trigram(M):
    """Era letter trigram log-probs from the running letter stream of
    Tocqueville t1+t2 (same tokenization as crowd2). add-alpha smoothed."""
    letters = ''.join(M['toks'])
    tri = collections.Counter()
    bi = collections.Counter()
    nV = len(set(letters)) + 1  # + START sentinel
    p0 = START + START + letters
    for a, b, c in zip(p0, p0[1:], p0[2:]):
        tri[(a, b, c)] += 1
        bi[(a, b)] += 1

    def lp(a, b, c):
        n = tri.get((a, b, c), 0)
        return math.log((n + ALPHA_TRI) / (bi.get((a, b), 0) + ALPHA_TRI * nV))
    return lp, len(letters)


def build_inventory(M, extra_cells=()):
    """Candidate cell inventory: top-INVENTORY_TOP corpus syllable units
    (rule syllabifier = candidate word list ONLY, never a conditional model)
    + single letters + pins/extra ensured present.
    Returns (cells list, freq-weight list)."""
    cnt = collections.Counter()
    for w in M['toks']:
        for u in M['segs'](w):
            cnt[u] += 1
    top = [u for u, _ in cnt.most_common(INVENTORY_TOP)]
    letters = sorted(set(''.join(M['toks'])))
    seen, cells, weights = set(), [], []
    for u in top + letters:
        if u not in seen:
            seen.add(u)
            cells.append(u)
            weights.append(cnt.get(u, 1))
    for c in list(PINS.values()) + list(extra_cells):
        if c and c not in seen:
            seen.add(c)
            cells.append(c)
            weights.append(cnt.get(c, 1))
    return cells, weights


def load_phase_map():
    """Banked Jaccard-k12 contactor blocks: A/B/C = 3 largest clusters,
    R = rest. From code/crowd/contactor_results.json (lane artifact)."""
    d = json.load(open(os.path.join(LANE, 'code', 'crowd',
                                    'contactor_results.json')))
    jc = d['jaccard_clusters']['12']
    block = {}
    for x, lbl in ((jc[0]['members'], 'A'), (jc[1]['members'], 'B'),
                   (jc[2]['members'], 'C')):
        for g in x:
            block[g] = lbl
    for c in jc[3:]:
        for g in c['members']:
            block[g] = 'R'
    assert len(block) == 96, len(block)
    return block


# ---------------------------------------------------------------- joint key + incremental scorer
class JointModel:
    """Incremental joint scorer over the full key."""

    def __init__(self, stream, phase, lp_tri, pins, provisional, cells,
                 weights, lam_rot=LAM_ROT, lam_poly=LAM_POLY, rng=None):
        self.gs = list(stream)
        self.N = len(stream)
        self.phase = dict(phase)
        self.lp = lp_tri
        self.pins = dict(pins)
        self.prov = dict(provisional)
        self.cells = list(cells)
        self.weights = list(weights)
        self.lam_rot = lam_rot
        self.lam_poly = lam_poly
        self.rng = rng or random.Random(SEED)
        self.groups = sorted(set(stream))
        self.nonpin = [g for g in self.groups if g not in self.pins]
        self.occ = collections.defaultdict(list)
        for t, g in enumerate(self.gs):
            self.occ[g].append(t)
        self._lets = {}
        self.v1, self.v2, self.w2 = {}, {}, {}
        self.pcell = [None] * self.N
        self.lscore = [0.0] * self.N
        self.n_vphi = collections.Counter()
        self.n_v = collections.Counter()
        self.n_poly = 0
        self.S_prior = 0.0
        self._cumw = None

    # -- inventory sampling ------------------------------------------------
    def sample_cell(self, exclude=()):
        if self.rng.random() < 0.7:
            if self._cumw is None:
                tot = float(sum(self.weights))
                acc, self._cumw = 0.0, []
                for w in self.weights:
                    acc += w / tot
                    self._cumw.append(acc)
            c = self.cells[bisect.bisect(self._cumw, self.rng.random())]
        else:
            c = self.rng.choice(self.cells)
        if c in exclude:
            return self.sample_cell(exclude)
        return c

    def _letters(self, c):
        v = self._lets.get(c)
        if v is None:
            v = self._lets[c] = list(c)
        return v

    # -- F: letter-trigram score of cell cb given cell ca -------------------
    def F(self, ca, cb):
        lp = self.lp
        if ca == START:
            p1, p2 = START, START
        else:
            la = self._letters(ca)
            p1 = la[-2] if len(la) >= 2 else START
            p2 = la[-1] if la else START
        t = 0.0
        for ch in self._letters(cb):
            t += lp(p1, p2, ch)
            p1, p2 = p2, ch
        return t

    # -- decode / recompute --------------------------------------------------
    def init_key(self):
        for g in self.groups:
            if g in self.pins:
                self.v1[g], self.v2[g], self.w2[g] = self.pins[g], None, 0.0
            else:
                self.v1[g] = self.sample_cell()
                self.v2[g], self.w2[g] = None, 0.0
        self._recompute_all()

    def _recompute_all(self):
        """Full recompute of pcell/lscore/counts from (v1,v2,w2).
        Single-valued decode (v1); caller re-runs E-step for polyvalence."""
        self.pcell = [self.v1[g] for g in self.gs]
        self._refresh_scores()

    def _refresh_scores(self):
        self.lscore = [0.0] * self.N
        for t in range(self.N):
            ca = self.pcell[t - 1] if t > 0 else START
            self.lscore[t] = self.F(ca, self.pcell[t])
        self.n_vphi = collections.Counter()
        self.n_v = collections.Counter()
        for t, g in enumerate(self.gs):
            v, ph = self.pcell[t], self.phase[g]
            self.n_vphi[(v, ph)] += 1
            self.n_v[v] += 1
        self.n_poly = sum(1 for g in self.groups if self.v2[g] is not None)
        self.S_prior = sum(BETA_PROV for g, c in self.prov.items()
                           if self.v1.get(g) == c)

    def _phase_score(self):
        a = ALPHA_PH
        t = 0.0
        for (v, ph), n in self.n_vphi.items():
            t += n * math.log((n + a) / (self.n_v[v] + 4 * a))
        return t

    def total(self):
        return (sum(self.lscore) + self.lam_rot * self._phase_score()
                + self.S_prior - self.lam_poly * self.n_poly)

    # -- per-occurrence polyvalent choice (hard E-step) ----------------------
    def _choose(self, t):
        g = self.gs[t]
        v1, v2 = self.v1[g], self.v2[g]
        if v2 is None:
            return v1
        ca = self.pcell[t - 1] if t > 0 else START
        cb = self.pcell[t + 1] if t + 1 < self.N else None
        s1 = self.F(ca, v1) + (self.F(v1, cb) if cb else 0.0)
        s2 = self.F(ca, v2) + (self.F(v2, cb) if cb else 0.0)
        w2 = min(max(self.w2[g], 1e-6), 1 - 1e-6)
        return v2 if s2 + math.log(w2) > s1 + math.log(1 - w2) else v1

    def _set_pcell(self, t, v):
        old = self.pcell[t]
        if old == v:
            return False
        g = self.gs[t]
        ph = self.phase[g]
        self.n_vphi[(old, ph)] -= 1
        self.n_v[old] -= 1
        self.n_vphi[(v, ph)] += 1
        self.n_v[v] += 1
        self.pcell[t] = v
        ca = self.pcell[t - 1] if t > 0 else START
        self.lscore[t] = self.F(ca, v)
        if t + 1 < self.N:
            self.lscore[t + 1] = self.F(v, self.pcell[t + 1])
        return True

    def _rescore_group(self, g, relax=True):
        for t in self.occ[g]:
            self._set_pcell(t, self._choose(t))
        if relax:
            cands = set()
            for t in self.occ[g]:
                for u in (t - 1, t + 1):
                    if 0 <= u < self.N and self.v2[self.gs[u]] is not None:
                        cands.add(u)
            for _ in range(3):
                moved = False
                for u in sorted(cands):
                    if self._set_pcell(u, self._choose(u)):
                        moved = True
                if not moved:
                    break
        if self.v2[g] is not None:
            n2 = sum(1 for t in self.occ[g] if self.pcell[t] == self.v2[g])
            self.w2[g] = (n2 + ALPHA_PH) / (len(self.occ[g]) + 2 * ALPHA_PH)

    # -- snapshot / revert (exact; covers swap partners) --------------------
    def _aff_positions(self, groups):
        aff = set()
        for g in groups:
            for t in self.occ[g]:
                aff.add(t)
                if t - 1 >= 0:
                    aff.add(t - 1)
                if t + 1 < self.N:
                    aff.add(t + 1)
        return aff

    def snapshot(self, groups):
        aff = self._aff_positions(groups)
        return {'groups': list(groups),
                'key': {g: (self.v1[g], self.v2[g], self.w2[g])
                        for g in groups},
                'pcell': {t: self.pcell[t] for t in aff},
                'n_vphi': dict(self.n_vphi), 'n_v': dict(self.n_v),
                'n_poly': self.n_poly, 'S_prior': self.S_prior}

    def revert(self, snap):
        for g, (a, b, w) in snap['key'].items():
            self.v1[g], self.v2[g], self.w2[g] = a, b, w
        for t, v in snap['pcell'].items():
            self.pcell[t] = v
        aff = set(snap['pcell'])
        # lscore[t] depends on pcell[t-1],pcell[t]; lscore[t+1] on pcell[t]
        for t in aff:
            ca = self.pcell[t - 1] if t > 0 else START
            self.lscore[t] = self.F(ca, self.pcell[t])
            if t + 1 < self.N:
                self.lscore[t + 1] = self.F(self.pcell[t],
                                            self.pcell[t + 1])
        self.n_vphi = collections.Counter(snap['n_vphi'])
        self.n_v = collections.Counter(snap['n_v'])
        self.n_poly = snap['n_poly']
        self.S_prior = snap['S_prior']

    # -- moves ---------------------------------------------------------------
    def propose_move(self, g, rng=None):
        """Propose one move on non-pin group g. Draws the branch (and swap
        partner) FIRST, snapshots exactly the touched groups, then applies.
        Returns (move_name, touched_set, snapshot_or_None)."""
        rng = rng or self.rng
        r = rng.random()
        if r < 0.55:
            branch, touched = 'chg1', {g}
        elif r < 0.70:
            h = rng.choice(self.nonpin)
            if h == g:
                return 'noop', {g}, None
            branch, touched = 'swap', {g, h}
        elif r < 0.85:
            branch, touched = 'poly', {g}
        else:
            if self.v2[g] is None:
                return 'noop', {g}, None
            branch, touched = 'chg2', {g}
        snap = self.snapshot(touched)
        if branch == 'chg1':
            new = self.sample_cell(exclude=(self.v1[g], self.v2[g]))
            if new == self.v2[g]:
                self.v1[g], self.v2[g] = self.v2[g], self.v1[g]
            else:
                if self.v1[g] == self.prov.get(g):
                    self.S_prior -= BETA_PROV
                self.v1[g] = new
                if new == self.prov.get(g):
                    self.S_prior += BETA_PROV
            mv = 'chg1'
        elif branch == 'swap':
            h = next(x for x in touched if x != g)
            for gg in (g, h):
                if self.v1[gg] == self.prov.get(gg):
                    self.S_prior -= BETA_PROV
            self.v1[g], self.v1[h] = self.v1[h], self.v1[g]
            for gg in (g, h):
                if self.v1[gg] == self.prov.get(gg):
                    self.S_prior += BETA_PROV
            mv = 'swap'
        elif branch == 'poly':
            if self.v2[g] is None:
                self.v2[g] = self.sample_cell(exclude=(self.v1[g],))
                self.w2[g] = 0.5
                self.n_poly += 1
                mv = 'addpoly'
            else:
                self.v2[g] = None
                self.w2[g] = 0.0
                self.n_poly -= 1
                mv = 'droppoly'
        else:  # chg2
            self.v2[g] = self.sample_cell(exclude=(self.v1[g], self.v2[g]))
            mv = 'chg2'
        for gg in touched:
            self._rescore_group(gg, relax=(gg == g))
        return mv, touched, snap

    # -- annealing -----------------------------------------------------------
    def anneal(self, sweeps=1200, T0=2.0, T1=0.02, seed=None, log_every=0):
        rng = random.Random(seed) if seed is not None else self.rng
        old_rng, self.rng = self.rng, rng
        self.init_key()
        best = self.total()
        best_state = (dict(self.v1), dict(self.v2), dict(self.w2),
                      list(self.pcell))
        cur = best
        cooling = (T1 / T0) ** (1.0 / sweeps)
        T, acc, moves = T0, 0, 0
        for sw in range(sweeps):
            order = self.nonpin[:]
            rng.shuffle(order)
            for g in order:
                mv, touched, snap = self.propose_move(g)
                if mv == 'noop':
                    continue
                new = self.total()
                d = new - cur
                moves += 1
                if d >= 0 or rng.random() < math.exp(d / T):
                    cur = new
                    acc += 1
                    if new > best:
                        best = new
                        best_state = (dict(self.v1), dict(self.v2),
                                      dict(self.w2), list(self.pcell))
                else:
                    self.revert(snap)
            T *= cooling
            if log_every and (sw + 1) % log_every == 0:
                print('    sweep %d/%d T=%.4f cur=%.1f best=%.1f acc=%.3f' %
                      (sw + 1, sweeps, T, cur, best, acc / max(moves, 1)),
                      flush=True)
        self.v1, self.v2, self.w2 = best_state[0], best_state[1], best_state[2]
        self.pcell = best_state[3]
        self._refresh_scores()
        self.rng = old_rng
        return {'best': best, 'acc_rate': acc / max(moves, 1)}

    # -- marginals -------------------------------------------------------------
    def marginals(self, sweeps=400, T=0.3, seed=None):
        """Low-T sampling from the current key -> P(cell|g) per group."""
        rng = random.Random(seed) if seed is not None else self.rng
        old_rng, self.rng = self.rng, rng
        counts = collections.Counter()
        cur = self.total()
        for sw in range(sweeps):
            order = self.nonpin[:]
            rng.shuffle(order)
            for g in order:
                mv, touched, snap = self.propose_move(g)
                if mv == 'noop':
                    continue
                new = self.total()
                d = new - cur
                if d >= 0 or rng.random() < math.exp(d / T):
                    cur = new
                else:
                    self.revert(snap)
            for t, g in enumerate(self.gs):
                counts[(g, self.pcell[t])] += 1
        self.rng = old_rng
        marg = {}
        for g in self.groups:
            tot = sum(c for (gg, _), c in counts.items() if gg == g)
            marg[g] = sorted(
                ((v, c / tot) for (gg, v), c in counts.items() if gg == g),
                key=lambda x: -x[1])
        return marg


def random_key_baseline(gs, phase, lp_tri, pins, provisional, cells, weights,
                        lam_rot, lam_poly, n=20, seed=999):
    """Best total over n random keys (sanity floor for annealing)."""
    best = float('-inf')
    for i in range(n):
        m = JointModel(gs, phase, lp_tri, pins, provisional, cells, weights,
                       lam_rot, lam_poly, rng=random.Random(seed + i))
        m.init_key()
        best = max(best, m.total())
    return best


def verify_incremental(gs, phase, lp_tri, pins, provisional, cells, weights,
                       seed=7, n_moves=300):
    """Self-test: incremental total() must equal full recompute after every
    accepted move. Returns (ok, max_abs_err)."""
    rng = random.Random(seed)
    m = JointModel(gs, phase, lp_tri, pins, provisional, cells, weights,
                   rng=random.Random(seed))
    m.init_key()
    maxerr = 0.0
    for i in range(n_moves):
        g = rng.choice(m.nonpin)
        mv, touched, snap = m.propose_move(g)
        if mv == 'noop':
            continue
        inc = m.total()
        m._refresh_scores()  # full recompute from pcell
        full = m.total()
        err = abs(inc - full)
        maxerr = max(maxerr, err)
        if err > 1e-6:
            return False, (i, mv, inc, full)
    return True, maxerr
