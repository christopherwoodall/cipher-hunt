#!/usr/bin/env python3
"""PROTOTYPE search: island-population SA + alias-block moves + graduated
word-bonus ramp. (Round-7 search-family prototype, work order 8.)

Different search family from the baseline (single-chain SA, single-group
moves) in three orthogonal ways:

1. ALIAS-BLOCK MOVES. In a homophonic cipher the natural unit of key
   change is the alias SET (all groups sharing a cell), not the group.
   Single-group moves must cross a valley to reassign an alias set
   (each moved group temporarily splits its block); block moves jump it.
   Two new proposals:
     - block: B(g) = {h : v1[h] == v1[g]} all move to a new cell at once;
     - merge: v1[g] <- v1[h] (g joins h's alias block).
   The concentration penalty (raw-cell cap 3, in the objective) bounds
   block growth automatically.

2. ISLAND POPULATION with migration. P=6 islands run SA in parallel;
   every 60 sweeps the worst island copies the best island's key plus
   perturbation (8 random reassignments). Restarts-with-memory instead of
   independent restarts.

3. GRADUATED word bonus (coarse-to-fine in objective space). lam_word
   ramps 0 -> 1 over the first 100 sweeps: the projected letter 7-gram is
   the smooth term, the spanning word bonus the rugged one. Start smooth
   to find the projection-level basin, then sharpen.

FAIR BUDGET: 6 islands x 300 sweeps x 89 groups = 160,200 proposals,
exactly the baseline's 3 x 600 x 89. Same frozen objective hyperparameters.

Usage: python3 prototype.py <seed> [--no-ramp]
Output: runs/prototype/asg-<seed>.json  {v1, v2, ...}
Key files are NEVER read here.
"""
import json
import math
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from harness import get_models, load_instance, make_model  # noqa: E402
from objective import RepairedModel  # noqa: E402

OUTD = os.path.join(HERE, 'runs', 'prototype')
os.makedirs(OUTD, exist_ok=True)

P_ISLANDS = 6
SWEEPS = 300          # per island; 6*300*89 = 160200 = baseline budget
T0, T1 = 2.0, 0.02
RAMP_SWEEPS = 100     # lam_word 0->1 over the first RAMP_SWEEPS sweeps
MIG_EVERY = 60
PERTURB_K = 8
BASE_SEED = 918200


class BlockModel(RepairedModel):
    """RepairedModel + alias-block / merge proposals."""

    def propose_move(self, g, rng=None):
        rng = rng or self.rng
        r = rng.random()
        if r < 0.40:
            return self._single(g, rng, 'chg1')
        elif r < 0.50:
            return self._swap(g, rng)
        elif r < 0.60:
            return self._poly(g, rng)
        elif r < 0.65:
            return self._chg2(g, rng)
        elif r < 0.85:
            return self._block(g, rng)
        else:
            return self._merge(g, rng)

    # -- single-group branches (mirror the parent's, minus branch draw) --
    def _single(self, g, rng, _):
        snap = self.snapshot({g})
        new = self.sample_cell(exclude=(self.v1[g], self.v2[g]))
        if new == self.v2[g]:
            old_a, old_b = self.v1[g], self.v2[g]
            self._move_v1(g, old_b)
            self.v2[g] = old_a
        else:
            self._move_v1(g, new)
        self._rescore_group(g, relax=True)
        return 'chg1', {g}, snap

    def _swap(self, g, rng):
        h = rng.choice(self.nonpin)
        if h == g:
            return 'noop', {g}, None
        snap = self.snapshot({g, h})
        vg, vh = self.v1[g], self.v1[h]
        self._move_v1(g, vh)
        self._move_v1(h, vg)
        self._rescore_group(g, relax=True)
        self._rescore_group(h, relax=False)
        return 'swap', {g, h}, snap

    def _poly(self, g, rng):
        snap = self.snapshot({g})
        if self.v2[g] is None:
            self.v2[g] = self.sample_cell(exclude=(self.v1[g],))
            self.w2[g] = 0.5
            mv = 'addpoly'
        else:
            self.v2[g] = None
            self.w2[g] = 0.0
            mv = 'droppoly'
        self._rescore_group(g, relax=True)
        return mv, {g}, snap

    def _chg2(self, g, rng):
        if self.v2[g] is None:
            return 'noop', {g}, None
        snap = self.snapshot({g})
        self.v2[g] = self.sample_cell(exclude=(self.v1[g], self.v2[g]))
        self._rescore_group(g, relax=True)
        return 'chg2', {g}, snap

    # -- block branches (the new family) --
    def _block(self, g, rng):
        """Move the whole current alias block of g to a new cell."""
        cell = self.v1[g]
        block = [h for h in self.nonpin if self.v1[h] == cell]
        new = self.sample_cell(exclude=(cell,))
        snap = self.snapshot(block)
        for h in block:
            self._move_v1(h, new)
        for h in block:
            self._rescore_group(h, relax=(h == g))
        return 'block%d' % len(block), set(block), snap

    def _merge(self, g, rng):
        """g joins h's alias block."""
        h = rng.choice(self.nonpin)
        if h == g or self.v1[h] == self.v1[g]:
            return 'noop', {g}, None
        snap = self.snapshot({g})
        self._move_v1(g, self.v1[h])
        self._rescore_group(g, relax=True)
        return 'merge', {g}, snap


def full_total(m):
    """Total on the FULL objective (lam_word=1), exact resync."""
    lw = m.lam_word
    m.lam_word = 1.0
    m._sword_dirty = True
    s = m.total()
    m.lam_word = lw
    m._sword_dirty = True
    return s


def perturb_copy(dst, src, k, rng):
    dst.v1 = dict(src.v1)
    dst.v2 = dict(src.v2)
    dst.w2 = dict(src.w2)
    tgt = rng.sample(dst.nonpin, k)
    for g in tgt:
        dst.v1[g] = dst.sample_cell(exclude=(dst.v1[g],))
        dst.v2[g], dst.w2[g] = None, 0.0
    dst._recompute_all()
    dst._refresh_scores()


def run(seed, no_ramp=False):
    t0 = time.time()
    get_models(verbose=False)
    inst = load_instance(seed)
    stream = inst['stream']
    rng_master = random.Random(BASE_SEED + int(seed))

    islands = []
    for i in range(P_ISLANDS):
        m = make_model(stream, seed=BASE_SEED + int(seed) * 10 + i)
        m.__class__ = BlockModel  # same calibrated hyperparams, new moves
        m.rng = random.Random(BASE_SEED + int(seed) * 10 + i)
        m.init_key()
        islands.append(m)

    cooling = (T1 / T0) ** (1.0 / SWEEPS)
    n_nonpin = len(islands[0].nonpin)
    proposals = 0
    migr_log = []

    for sw in range(SWEEPS):
        lam = 1.0 if no_ramp else min(1.0, sw / RAMP_SWEEPS)
        T = T0 * (cooling ** sw)
        for m in islands:
            m.lam_word = lam
            order = m.nonpin[:]
            m.rng.shuffle(order)
            cur = m.total()
            for g in order:
                mv, touched, snap = m.propose_move(g, m.rng)
                proposals += 1
                if mv == 'noop':
                    continue
                new = m.total()
                d = new - cur
                if d >= 0 or m.rng.random() < math.exp(d / T):
                    cur = new
                else:
                    m.revert(snap)
        if (sw + 1) % MIG_EVERY == 0 or sw == SWEEPS - 1:
            scored = [(full_total(m), i) for i, m in enumerate(islands)]
            scored.sort(reverse=True)
            best_s, best_i = scored[0]
            worst_s, worst_i = scored[-1]
            migr_log.append({'sweep': sw + 1, 'best_full': round(best_s, 4),
                             'worst_full': round(worst_s, 4)})
            print('[proto %s] sweep %d/%d lam=%.2f T=%.3f best_full=%.4f '
                  'worst_full=%.4f' % (seed, sw + 1, SWEEPS, lam, T,
                                       best_s, worst_s), flush=True)
            if sw < SWEEPS - 1:
                perturb_copy(islands[worst_i], islands[best_i], PERTURB_K,
                             rng_master)

    # final: best island on the full objective, exact resync
    scored = [(full_total(m), i) for i, m in enumerate(islands)]
    scored.sort(reverse=True)
    best_s, best_i = scored[0]
    best_m = islands[best_i]
    best_m.lam_word = 1.0
    best_m._refresh_scores()
    exact = best_m.total()
    out = {'method': 'proto-island-block-ramp', 'seed': str(seed),
           'SYNTHETIC': True,
           'islands': P_ISLANDS, 'sweeps_per_island': SWEEPS,
           'T0': T0, 'T1': T1, 'ramp_sweeps': 0 if no_ramp else RAMP_SWEEPS,
           'mig_every': MIG_EVERY, 'perturb_k': PERTURB_K,
           'base_seed': BASE_SEED, 'proposals': proposals,
           'migration_log': migr_log,
           'best_full': round(best_s, 4), 'best_exact_resync': round(exact, 4),
           'components': best_m.components(),
           'v1': dict(best_m.v1),
           'v2': {g: v for g, v in best_m.v2.items() if v is not None},
           'elapsed_min': round((time.time() - t0) / 60, 1)}
    tag = 'noramp' if no_ramp else 'proto'
    json.dump(out, open(os.path.join(OUTD, 'asg-%s-%s.json' % (tag, seed)),
                        'w'))
    print('[proto %s] wrote asg-%s.json best_full=%.4f exact=%.4f in %.1f min'
          % (seed, seed, best_s, exact, out['elapsed_min']), flush=True)


if __name__ == '__main__':
    no_ramp = '--no-ramp' in sys.argv
    run(sys.argv[1], no_ramp=no_ramp)
