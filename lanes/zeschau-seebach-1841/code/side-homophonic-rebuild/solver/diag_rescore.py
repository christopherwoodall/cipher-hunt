#!/usr/bin/env python3
"""Diagnostic proof for the rebuild (2026-10-07). DIAGNOSIS ONLY -- reads the
sealed 184101 truth the same way runs/diag_planted_score.py did; never used
in any scoring/training loop.

Rescores, under the NEW objective, the two keys from the frozen diagnosis:
  (a) the PLANTED truth key (184101 sealed truth)
  (b) the frozen run's DEGENERATE best key (runs/run2-184101/result.json)

Required outcomes:
  1. truth total > degenerate total by a clear margin (D1+D2 fixed)
  2. on the degenerate key, polyvalence now HURTS: stripping its 60
     secondaries must RAISE the total (D3 fixed)
  3. inventory: all 96 planted primaries present, zero fallbacks (D4 fixed)

Also reports per-secondary S_char gains (truth vs degenerate) as the
lambda_poly=50 rationale.
"""
import hashlib
import json
import os
import sys

REBUILD = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(REBUILD, '..', '..'))
sys.path.insert(0, REBUILD)
from solver import build_solver  # noqa: E402
from phonetics import project as _proj  # noqa: E402

SEED = '184101'
INST = os.path.join(LANE, 'side-homophonic', 'control', 'instances')
RUNS = os.path.join(LANE, 'side-homophonic', 'runs')


def load_pairs(path):
    pairs = []
    for l in open(path):
        if l.startswith('#') or not l.strip():
            continue
        pairs += l.split()
    return pairs


def parts(solver):
    c = solver.cfg
    s_word = solver.S_cov - solver.S_single
    return {
        'S_char': solver.S_char,
        'S_cov': solver.S_cov,
        'S_single': solver.S_single,
        'S_word': s_word,
        'S_potts': solver.S_potts,
        'S_soft': solver.S_soft,
        'n_poly': solver.n_poly,
        'poly_pen': -c['lambda_poly'] * solver.n_poly,
        'S_conc': solver.S_conc,
        'conc_pen': -c['lambda_conc'] * solver.S_conc,
        'total': solver.total(),
    }


def show(name, p):
    print(f'[{name}] total={p["total"]:.1f}')
    print(f'   S_char={p["S_char"]:.1f} S_cov={p["S_cov"]:.1f} '
          f'S_single={p["S_single"]:.1f} S_word(net)={p["S_word"]:.1f} '
          f'S_potts={p["S_potts"]:.3f}')
    print(f'   n_poly={p["n_poly"]} poly_pen={p["poly_pen"]:.1f} '
          f'S_conc={p["S_conc"]:.1f} conc_pen={p["conc_pen"]:.1f}')


def _frozen_objective(pairs, anchors, asg):
    """Score an assignment under the FROZEN solver's objective (cross-check
    that the reconstructed key is the frozen run's best)."""
    import importlib.util
    frozen_dir = os.path.join(LANE, 'side-homophonic', 'solver')
    for p in (os.path.join(LANE, 'code'),
              os.path.join(LANE, 'code', 'crowd2'),
              frozen_dir):
        if p not in sys.path:
            sys.path.insert(0, p)
    spec = importlib.util.spec_from_file_location(
        'frozen_solver', os.path.join(frozen_dir, 'solver.py'))
    fs = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fs)
    fcfg = dict(fs.DEFAULTS)
    fcfg.update(json.load(open(os.path.join(frozen_dir, 'config.json'))))
    solver, _, _ = fs.build_solver(
        pairs, anchors, {}, os.path.join(frozen_dir, 'lm_ref', 'lm.json'),
        fcfg, 1841, no_phase=False, no_word=False, no_poly=False,
        no_soft=True, inventory_mode='crib', init=fcfg['init'],
        no_contact=False)
    for g in solver.groups:
        a = asg[g]
        solver.v1[g] = a['v1']
        solver.v2[g] = a['v2']
        solver.w2[g] = a['w2']
    solver._rebuild_conc()
    solver._full_refresh()
    return solver.total()


def main():
    pairs = load_pairs(os.path.join(INST, f'SYNTHETIC-ct-{SEED}.pairs.txt'))
    anchors = json.load(open(os.path.join(INST, f'SYNTHETIC-crib-{SEED}.json')))['anchors']
    truth = json.load(open(os.path.join(INST, f'SYNTHETIC-key-{SEED}.json')))
    cfg = json.load(open(os.path.join(REBUILD, 'config.json')))
    print(f'[diag] lambda_poly={cfg["lambda_poly"]} '
          f'lambda_word={cfg["lambda_word"]} '
          f'word_minlen={cfg.get("word_minlen")}')

    solver, lm_data, phase_info = build_solver(
        pairs, anchors, {}, os.path.join(REBUILD, 'lm_ref', 'lm.json'),
        cfg, 1841, no_phase=False, no_word=False, no_poly=False,
        no_soft=True, inventory_mode='crib', init=cfg['init'],
        no_contact=False)
    print(f'[diag] inventory={len(solver.inv)} (frozen was 291)')

    # ---- (a) planted truth ----
    key = truth['key']
    missing = [g for g in key if g not in anchors
               and key[g]['primary'] not in solver.pv]
    print(f'[diag] truth primaries missing from inventory: {len(missing)}')
    assert not missing, f'D4 NOT FIXED: {missing}'
    for g in solver.groups:
        if g in anchors:
            solver.v1[g] = anchors[g]
            solver.v2[g] = None
            solver.w2[g] = 0.0
        else:
            solver.v1[g] = key[g]['primary']
            sec = key[g].get('secondaries') or []
            if sec:
                solver.v2[g] = sec[0]
                solver.w2[g] = 0.5
            else:
                solver.v2[g] = None
                solver.w2[g] = 0.0
    solver._rebuild_conc()
    solver._full_refresh()
    p_truth = parts(solver)
    show('TRUTH (planted)', p_truth)
    truth_decode = ''.join(solver.pcell)
    print(f'[diag] truth decode: len={len(truth_decode)} chars, '
          f'sha256={hashlib.sha256(truth_decode.encode()).hexdigest()[:16]}')
    print(f'[diag] truth decode head: {truth_decode[:80]!r}')

    # truth without secondaries -> per-secondary S_char gain (lambda rationale)
    for g in solver.groups:
        solver.v2[g] = None
        solver.w2[g] = 0.0
    solver.n_poly = 0
    solver._full_refresh()
    p_truth_nopoly = parts(solver)
    gain_truth = (p_truth['S_char'] - p_truth_nopoly['S_char']) / max(p_truth['n_poly'], 1)
    print(f'[diag] truth: 6 real secondaries buy '
          f'{p_truth["S_char"]-p_truth_nopoly["S_char"]:.1f} S_char '
          f'({gain_truth:.1f} nats/secondary)')

    # ---- (b) frozen degenerate best ----
    res = json.load(open(os.path.join(RUNS, 'run2-184101', 'result.json')))
    asg = res['best']['assignment']
    for g in solver.groups:
        a = asg[g]
        assert a['v1'] in solver.pv, f'degenerate v1 {a["v1"]!r} not in rebuild inventory'
        solver.v1[g] = a['v1']
        v2 = a['v2']
        assert v2 is None or v2 in solver.pv, f'degenerate v2 {v2!r} missing'
        solver.v2[g] = v2
        solver.w2[g] = a['w2']
    solver._rebuild_conc()
    solver._full_refresh()
    p_deg = parts(solver)
    show('DEGENERATE (frozen best)', p_deg)
    deg_decode = ''.join(solver.pcell)
    print(f'[diag] degenerate decode: len={len(deg_decode)} chars, '
          f'sha256={hashlib.sha256(deg_decode.encode()).hexdigest()[:16]}')
    print(f'[diag] degenerate decode head: {deg_decode[:80]!r}')
    # NOTE: RUN-REPORT D2 quotes the RAW (unprojected) decode
    # ("titdeemenirereiemeprend..."); pcell here is projected, so the
    # strings differ by projection. The authoritative check that this is
    # the frozen run's best key: it must score 4127.4 under the FROZEN
    # objective (runs/run2-184101/result.json best.best).
    frozen_total = _frozen_objective(pairs, anchors, asg)
    # result.json best.best=4127.4 is the annealer's INCREMENTAL best;
    # best.final=3934.7 is the _full_refresh recompute -- the comparable
    # number for this install-and-refresh reconstruction (w2 rounded to 4dp
    # in the JSON accounts for the residual ~1 nat).
    print(f'[diag] degenerate key under FROZEN objective: {frozen_total:.1f} '
          f'(run2-184101 best.final=3934.7, best.best=4127.4 incremental)')
    assert abs(frozen_total - 3934.7) < 5.0, \
        f'reconstruction is not the frozen best key! got {frozen_total:.1f}'

    # degenerate without secondaries -> does polyvalence hurt now?
    for g in solver.groups:
        solver.v2[g] = None
        solver.w2[g] = 0.0
    solver.n_poly = 0
    solver._full_refresh()
    p_deg_nopoly = parts(solver)
    show('DEGENERATE stripped of secondaries', p_deg_nopoly)
    gain_deg = (p_deg['S_char'] - p_deg_nopoly['S_char']) / max(p_deg['n_poly'], 1)
    print(f'[diag] degenerate: {p_deg["n_poly"]} spurious secondaries buy '
          f'{p_deg["S_char"]-p_deg_nopoly["S_char"]:.1f} S_char '
          f'({gain_deg:.1f} nats/secondary)')

    # ---- verdicts ----
    print()
    margin = p_truth['total'] - p_deg['total']
    print(f'[verdict-1] truth total {p_truth["total"]:.1f} vs degenerate '
          f'{p_deg["total"]:.1f}: margin {margin:+.1f} nats -> '
          f'{"PASS (truth wins)" if margin > 0 else "FAIL"}')
    poly_hurts = p_deg_nopoly['total'] - p_deg['total']
    print(f'[verdict-2] degenerate with {p_deg["n_poly"]} secondaries vs '
          f'stripped: {poly_hurts:+.1f} nats -> '
          f'{"PASS (polyvalence hurts)" if poly_hurts > 0 else "FAIL"}')
    print(f'[verdict-3] inventory: 0 missing primaries -> PASS (D4 fixed)')
    print(f'[lambda_poly rationale] real secondaries gain ~{gain_truth:.0f} '
          f'nats each; spurious gain ~{gain_deg:.0f} each; '
          f'lambda_poly={cfg["lambda_poly"]} sits between -> real islets '
          f'survive, runaway pays '
          f'{cfg["lambda_poly"]*p_deg["n_poly"]:.0f} nats on the degenerate key')

    # ---- R4: lambda_poly insensitivity ----
    # The verdict must not hinge on the exact lambda value: rescore both
    # keys at lambda_poly in {30, 50, 70}. Only the poly term moves.
    print()
    print('[r4] lambda_poly insensitivity (truth vs degenerate totals):')
    base_truth = p_truth['total'] - p_truth['poly_pen']
    base_deg = p_deg['total'] - p_deg['poly_pen']
    r4_ok = True
    for lam in (30.0, 50.0, 70.0):
        t_truth = base_truth - lam * p_truth['n_poly']
        t_deg = base_deg - lam * p_deg['n_poly']
        m = t_truth - t_deg
        r4_ok &= m > 0
        print(f'   lambda_poly={lam:4.0f}: truth {t_truth:8.1f} vs '
              f'degenerate {t_deg:8.1f} -> margin {m:+7.1f} '
              f'{"PASS" if m > 0 else "FAIL"}')
    print(f'[verdict-4] lambda_poly insensitivity -> '
          f'{"PASS (truth wins at 30/50/70)" if r4_ok else "FAIL"}')


if __name__ == '__main__':
    main()
