#!/usr/bin/env python3
"""Diagnosis: score the PLANTED truth key under the frozen solver's OWN
objective function, vs the annealed best. Distinguishes:
  (A) planted scores HIGHER than annealed best -> optimizer failed to find it
  (B) planted scores LOWER -> the objective itself is misaligned with truth
Uses frozen solver.py unmodified (diagnosis only, post-control).
"""
import json, os, sys

SH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.join(SH, 'solver'))
from solver import build_solver, DEFAULTS  # noqa: E402

SEED = '184101'
INST = os.path.join(SH, 'control', 'instances')


def load_pairs(path):
    pairs = []
    for l in open(path):
        if l.startswith('#') or not l.strip():
            continue
        pairs += l.split()
    return pairs


def main():
    pairs = load_pairs(os.path.join(INST, f'SYNTHETIC-ct-{SEED}.pairs.txt'))
    anchors = json.load(open(os.path.join(INST, f'SYNTHETIC-crib-{SEED}.json')))['anchors']
    truth = json.load(open(os.path.join(INST, f'SYNTHETIC-key-{SEED}.json')))
    cfg = dict(DEFAULTS)
    cfg.update(json.load(open(os.path.join(SH, 'solver', 'config.json'))))
    solver, lm_data, phase_info = build_solver(
        pairs, anchors, {}, os.path.join(SH, 'solver', 'lm_ref', 'lm.json'),
        cfg, 1841, no_phase=False, no_word=False, no_poly=False,
        no_soft=True, inventory_mode='crib', init=cfg['init'], no_contact=False)
    key = truth['key']
    missing = [g for g in key if g not in anchors and key[g]['primary'] not in solver.pv]
    print(f'[diag] truth primaries not in solver inventory/projector: {len(missing)} of {len(key)}')
    for g in missing:
        print(f'[diag]   group {g}: planted primary {key[g]["primary"]!r}')
    # install planted assignment (proj-equivalent fallback for the 6
    # missing: inventory lacks accented by-ear forms; pv maps them to
    # unaccented projections, e.g. 'né'->'ne')
    from phonetics import project as _proj
    inv_by_proj = {}
    for v in solver.inv:
        inv_by_proj.setdefault(_proj(v), v)
    for g in solver.groups:
        if g in anchors:
            solver.v1[g] = anchors[g]; solver.v2[g] = None; solver.w2[g] = 0.0
        else:
            p1 = key[g]['primary']
            if p1 in solver.pv:
                solver.v1[g] = p1
            else:
                fb = inv_by_proj.get(_proj(p1)) or "re"
                solver.v1[g] = fb
                print(f'[diag] fallback: group {g} planted {p1!r} -> inventory {fb!r}')
            sec = key[g].get('secondaries') or []
            if sec:
                solver.v2[g] = sec[0] if sec[0] in solver.pv else (inv_by_proj.get(_proj(sec[0])) or "re")
                solver.w2[g] = 0.5
            else:
                solver.v2[g] = None; solver.w2[g] = 0.0
    solver._rebuild_conc()
    solver._full_refresh()
    planted_total = solver.total()
    print(f'[diag] PLANTED key objective total = {planted_total:.1f}')
    print(f'[diag]   S_char={solver.S_char:.1f} S_word={solver._word_totals():.1f} '
          f'S_potts={solver.S_potts:.3f} S_soft={solver.S_soft:.3f} '
          f'n_poly={solver.n_poly} S_conc={solver.S_conc:.1f}')
    print(f'[diag]   -lambda_poly*n_poly = {-cfg["lambda_poly"]*solver.n_poly:.1f}, '
          f'-lambda_conc*S_conc = {-cfg["lambda_conc"]*solver.S_conc:.1f}')
    res = json.load(open(os.path.join(SH, 'runs', f'run2-{SEED}', 'result.json')))
    best = res['best']['best']
    print(f'[diag] ANNEALED best (frozen run) = {best:.1f}')
    print(f'[diag] planted - annealed = {planted_total - best:+.1f} nats')
    print('[diag] verdict:', 'A: optimizer failed (planted higher)' if planted_total > best
          else 'B: objective misaligned (planted lower)')


if __name__ == '__main__':
    main()
