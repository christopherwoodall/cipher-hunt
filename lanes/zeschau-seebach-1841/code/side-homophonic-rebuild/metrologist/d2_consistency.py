#!/usr/bin/env python3
"""Metrologist task 3: D2 (S_word-dominance) consistency across the 6 ORIGINAL
instances (seeds 184101-184106).

Re-runs the FROZEN solver's scoring (no annealing -- installs assignments and
recomputes the objective decomposition exactly) for, per instance:
  A: the frozen batch's ANNEALED best assignment (degenerate decode)
  P: the PLANTED truth key (sealed; scoring/diagnosis only, per protocol)

D2 holds on an instance iff:
  (i)  total(P) << total(A)   -- objective misalignment (truth scores worse
       than the degenerate optimum under the solver's own objective)
  (ii) S_ac(A) >> S_ac(P)     -- the Aho-Corasick word term rewards degenerate
       repetition far above real French (the scoring-function exploit)
Also recorded (D3 bonus): n_poly(A) >> 6 planted islets (polyvalence runaway).

Official annealed outputs:
  184101-184104: side-homophonic/runs/frozen-ctl-<seed>/result.json
  184105-184106: side-homophonic/runs/run3-<seed>/result.json
(RUN-REPORT.md: run3 reports adopted after rescore-match verification.)

Solver construction mirrors runs/diag_planted_score.py exactly (frozen code,
read-only). --phase-ref additionally re-scores the 184101 annealed assignment
under no_phase / no_contact to quantify the frozen family's dependence on
phase machinery (task-2 reference).
"""
import json
import os
import sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code')
SH = os.path.join(LANE, 'side-homophonic')
sys.path.insert(0, os.path.join(SH, 'solver'))
from solver import build_solver, DEFAULTS  # noqa: E402
from phonetics import project as _proj  # noqa: E402

SEEDS = ['184101', '184102', '184103', '184104', '184105', '184106']
RESULT_PATH = {
    '184101': 'runs/frozen-ctl-184101/result.json',
    '184102': 'runs/frozen-ctl-184102/result.json',
    '184103': 'runs/frozen-ctl-184103/result.json',
    '184104': 'runs/frozen-ctl-184104/result.json',
    '184105': 'runs/run3-184105/result.json',
    '184106': 'runs/run3-184106/result.json',
}
HERE = os.path.dirname(os.path.abspath(__file__))


def load_pairs(path):
    pairs = []
    for line in open(path):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        pairs.extend(line.split())
    return pairs


def make_solver(pairs, anchors, no_phase=False, no_contact=False):
    cfg = dict(DEFAULTS)
    cfg.update(json.load(open(os.path.join(SH, 'solver', 'config.json'))))
    solver, _, _ = build_solver(
        pairs, anchors, {}, os.path.join(SH, 'solver', 'lm_ref', 'lm.json'),
        cfg, 1841, no_phase=no_phase, no_word=False, no_poly=False,
        no_soft=True, inventory_mode='crib', init=cfg['init'],
        no_contact=no_contact)
    return solver, cfg


def install_assignment(solver, assignment):
    for g in solver.groups:
        a = assignment[g]
        solver.v1[g] = a['v1']
        solver.v2[g] = a['v2']
        solver.w2[g] = a['w2']
    solver._rebuild_conc()
    solver._full_refresh()


def install_planted(solver, key, anchors):
    inv_by_proj = {}
    for v in solver.inv:
        inv_by_proj.setdefault(_proj(v), v)
    assignment = {}
    for g in solver.groups:
        if g in anchors:
            assignment[g] = {'v1': anchors[g], 'v2': None, 'w2': 0.0}
        else:
            p1 = key[g]['primary']
            v1 = p1 if p1 in solver.pv else (
                inv_by_proj.get(_proj(p1)) or 're')
            sec = key[g].get('secondaries') or []
            if sec:
                v2 = sec[0] if sec[0] in solver.pv else (
                    inv_by_proj.get(_proj(sec[0])) or 're')
                assignment[g] = {'v1': v1, 'v2': v2, 'w2': 0.5}
            else:
                assignment[g] = {'v1': v1, 'v2': None, 'w2': 0.0}
    install_assignment(solver, assignment)


def decompose(solver, cfg):
    s_word = solver.S_ac - solver.S_single
    return {
        'total': solver.total(),
        'S_char': solver.S_char,
        'S_ac': solver.S_ac,
        'S_single': solver.S_single,
        'S_word_raw': s_word,
        'S_word_weighted': cfg['lambda_word'] * s_word,
        'S_potts': solver.S_potts,
        'S_soft': solver.S_soft,
        'n_poly': solver.n_poly,
        'poly_penalty': cfg['lambda_poly'] * solver.n_poly,
        'S_conc': solver.S_conc,
        'conc_penalty': cfg['lambda_conc'] * solver.S_conc,
    }


def score_seed(seed):
    pairs = load_pairs(os.path.join(
        SH, 'control', 'instances', f'SYNTHETIC-ct-{seed}.pairs.txt'))
    anchors = json.load(open(os.path.join(
        SH, 'control', 'instances', f'SYNTHETIC-crib-{seed}.json')))['anchors']
    truth = json.load(open(os.path.join(
        SH, 'control', 'instances', f'SYNTHETIC-key-{seed}.json')))
    res = json.load(open(os.path.join(SH, RESULT_PATH[seed])))

    solver, cfg = make_solver(pairs, anchors)
    install_assignment(solver, res['best']['assignment'])
    d_annealed = decompose(solver, cfg)

    # verify the re-derivation against the batch's recorded score_parts
    sp = res['best']['score_parts']
    rederivation_ok = (
        abs(d_annealed['total'] - res['best']['best']) < 1.0
        and abs(d_annealed['S_ac'] - sp['S_ac']) < 1.0)

    solver2, cfg2 = make_solver(pairs, anchors)
    install_planted(solver2, truth['key'], anchors)
    d_planted = decompose(solver2, cfg2)

    gap = d_planted['total'] - d_annealed['total']
    ac_ratio = (d_annealed['S_ac'] / d_planted['S_ac']
                if d_planted['S_ac'] else float('inf'))
    return {
        'seed': seed,
        'annealed_total_recorded': res['best']['best'],
        'rederivation_ok': bool(rederivation_ok),
        'annealed': {k: round(v, 2) for k, v in d_annealed.items()},
        'planted': {k: round(v, 2) for k, v in d_planted.items()},
        'gap_planted_minus_annealed': round(gap, 1),
        'S_ac_ratio_annealed_over_planted': round(ac_ratio, 2),
        'D2_i_misaligned': bool(gap < -1000.0),
        'D2_ii_word_dominance': bool(ac_ratio > 5.0),
        'D3_poly_runaway': bool(d_annealed['n_poly'] > 20),
    }


def phase_ref():
    """How much of the frozen 184101 degenerate optimum needs phase machinery."""
    seed = '184101'
    pairs = load_pairs(os.path.join(
        SH, 'control', 'instances', f'SYNTHETIC-ct-{seed}.pairs.txt'))
    anchors = json.load(open(os.path.join(
        SH, 'control', 'instances', f'SYNTHETIC-crib-{seed}.json')))['anchors']
    res = json.load(open(os.path.join(SH, RESULT_PATH[seed])))
    out = {}
    for name, kw in [('default', {}), ('no_phase', {'no_phase': True}),
                     ('no_contact', {'no_contact': True})]:
        solver, cfg = make_solver(pairs, anchors, **kw)
        install_assignment(solver, res['best']['assignment'])
        d = decompose(solver, cfg)
        out[name] = {k: round(v, 2) for k, v in d.items()}
    return out


def main():
    rows = []
    for seed in SEEDS:
        print(f'[d2] scoring {seed} ...', flush=True)
        rows.append(score_seed(seed))
        r = rows[-1]
        print(f"  {seed}: gap={r['gap_planted_minus_annealed']:+.0f} nats, "
              f"S_ac ratio={r['S_ac_ratio_annealed_over_planted']:.1f}x, "
              f"n_poly_ann={r['annealed']['n_poly']}, "
              f"rederive_ok={r['rederivation_ok']}, "
              f"D2(i)={r['D2_i_misaligned']} D2(ii)={r['D2_ii_word_dominance']} "
              f"D3={r['D3_poly_runaway']}", flush=True)
    print('[d2] phase reference (184101 annealed assignment) ...', flush=True)
    pref = phase_ref()
    for name, d in pref.items():
        print(f"  {name}: total={d['total']:.1f} S_ac={d['S_ac']:.1f} "
              f"S_potts={d['S_potts']:.2f} conc_pen={d['conc_penalty']:.1f}",
              flush=True)
    json.dump({'rows': rows, 'phase_ref_184101': pref},
              open(os.path.join(HERE, 'd2_consistency_results.json'), 'w'),
              indent=1)
    d2_all = all(r['D2_i_misaligned'] and r['D2_ii_word_dominance']
                 for r in rows)
    print(f"\nD2 HOLDS ON ALL 6: {d2_all}", flush=True)


if __name__ == '__main__':
    main()
