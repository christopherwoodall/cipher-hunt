#!/usr/bin/env python3
"""Control harness for the Seebach homophonic solver (side fleet).

Interface (for the Runner + Control Designer):
  load_synthetic(path) -> (pairs, meta)
      Reads the Designer's SYNTHETIC-ct-<seed>.pairs.txt: '#' comment lines
      skipped, the rest whitespace-split into pair labels.
  run(...) -> result dict
      Runs solver.run_restarts on the synthetic pairs. The solver NEVER sees
      the ground truth: truth is loaded only in score(), after the solver
      output is written.
  score_assignment(result, truth, pairs, pins) -> metrics dict
      PRIMARY   = exact primary-cell recovery on non-anchor groups
      SECONDARY = true decode accuracy, all 1846 pairs (anchors given;
                  auto-correct: v1[g]==planted[t] or v2[g]==planted[t]).
                  Requires truth['planted'] (per-position, persisted by
                  generator.py KILL-2 fix 2026-10-07).
      ISLET     = secondary recovery on polyvalent islet groups (diagnostic)
      MRR       = mean reciprocal rank of truth primary in restart marginals
                  (diagnostic)
      PROJ-EQUIV = projection-equivalent primary recovery (diagnostic;
                  DEMOTE-2: ceiling ~0.53-0.60, not 1.0)
  gate_6instance(per_instance_metrics) -> (verdict, checklist)
      The REGISTERED §4 bars (CONTROL-DESIGN.md §4, 2026-10-07):
        PRIMARY   mean >= 0.20, min >= 0.10
        SECONDARY mean >= 0.30, min >= 0.22
        both means >= μ_chance + 5σ (0.098 / 0.227)
      All six -> CONTROL-PASS. Else CONTROL-FAIL.
      Islets/MRR/baseline-margin are DIAGNOSTICS, not gates (KILL-1).

Separation of duties: this harness never invents ciphertext; the only
synthetic data it touches is the Designer's labelled control. The sealed key
file is read here (Runner's eyes only), never passed to the solver.
"""

import collections
import json
import math
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from solver import run_restarts, DEFAULTS  # noqa: E402
from phonetics import project  # noqa: E402

# Registered §4 bars (CONTROL-DESIGN.md §4). THE registration; the harness's
# earlier 0.50 proposal is superseded (KILL-1, red-team 2026-10-07).
BARS_4 = {
    'primary_mean': 0.20,
    'primary_min': 0.10,
    'secondary_mean': 0.30,
    'secondary_min': 0.22,
    'primary_5sigma': 0.098,    # μ_chance + 5σ
    'secondary_5sigma': 0.227,  # μ_chance + 5σ
}


def load_synthetic(path):
    """Parse a SYNTHETIC-ct-<seed>.pairs.txt into (pairs, meta)."""
    pairs = []
    header = []
    with open(path) as f:
        for line in f:
            if line.startswith('#'):
                header.append(line.strip('# \n'))
                continue
            line = line.strip()
            if line:
                pairs.extend(line.split())
    seed = None
    for h in header:
        if h.startswith('seed='):
            seed = h.split()[0].split('=')[1]
    meta = {'path': path, 'seed': seed, 'header': header,
            'n_pairs': len(pairs), 'n_groups': len(set(pairs)),
            'synthetic': True}
    return pairs, meta


def _load_truth_robust(path):
    """Read the SEALED key file (Runner's eyes only)."""
    return json.load(open(path))


def run(pairs, anchors, lm_path, cfg, out_dir, seed, **solver_opts):
    return run_restarts(pairs, anchors, {}, lm_path, cfg, out_dir, seed,
                        no_soft=True, **solver_opts)


def score_assignment(result, truth, pairs, pins):
    """Score a solver result against the sealed truth. No solver input.

    SECONDARY is the TRUE decode accuracy (KILL-2): per-position planted
    cells from truth['planted'], anchors auto-correct, v1-or-v2 match.
    """
    key = truth['key']
    planted = truth.get('planted')
    if planted is None:
        raise RuntimeError(
            "truth['planted'] missing: run control/persist_planted.py "
            "(KILL-2 fix) before scoring")
    assert len(planted) == len(pairs), 'planted/pairs length mismatch'
    nonpin = [g for g in key if g not in pins]
    asg = result['best']['assignment']
    marg = result['marginals']

    # pins intact
    pins_ok = sum(1 for g, v in pins.items()
                  if asg.get(g, {}).get('v1') == v)

    # PRIMARY: exact primary recovery (non-anchor groups)
    prim_hit = {}
    for g in nonpin:
        prim_hit[g] = 1 if asg.get(g, {}).get('v1') == key[g]['primary'] \
            else 0
    primary = sum(prim_hit.values()) / len(nonpin)

    # PROJ-EQUIV (diagnostic, DEMOTE-2): projection-equivalent recovery.
    # Counts a hit if project(v1[g]) == project(true_primary[g]).
    proj_hit = {}
    for g in nonpin:
        proj_hit[g] = 1 if project(asg.get(g, {}).get('v1') or '') == \
            project(key[g]['primary']) else 0
    proj_equiv = sum(proj_hit.values()) / len(nonpin)

    # SECONDARY: true decode accuracy, all positions.
    # Anchors are given (auto-correct). Non-anchor: v1[g]==planted[t] or
    # v2[g]==planted[t] (exercises the polyvalent E-step machinery).
    tot, hit = 0, 0
    for t, g in enumerate(pairs):
        tot += 1
        if g in pins:
            hit += 1
        else:
            v1 = asg.get(g, {}).get('v1')
            v2 = asg.get(g, {}).get('v2')
            if v1 == planted[t] or (v2 is not None and v2 == planted[t]):
                hit += 1
    secondary = hit / tot

    # MRR of truth primary in restart marginals (diagnostic)
    rrs = []
    for g in nonpin:
        tv = key[g]['primary']
        ranked = [v for v, _ in marg.get(g, [])]
        rrs.append(1.0 / (ranked.index(tv) + 1) if tv in ranked else 0.0)
    mrr = sum(rrs) / len(rrs) if rrs else 0.0

    # ISLETS: groups with secondaries in the truth (diagnostic)
    islets = [g for g in nonpin if key[g].get('secondaries')]
    isl_detail = []
    isl_ok = 0
    for g in islets:
        tv1 = key[g]['primary']
        tv2 = key[g]['secondaries'][0] if key[g]['secondaries'] else None
        ranked = [v for v, _ in marg.get(g, [])]
        prim_rank1 = bool(ranked) and ranked[0] == tv1
        v2 = asg.get(g, {}).get('v2')
        sec_found = (v2 == tv2) or (tv2 in ranked[:3])
        ok = prim_rank1 and sec_found
        isl_ok += 1 if ok else 0
        isl_detail.append({'group': g, 'true_primary': tv1,
                           'true_secondary': tv2,
                           'solver_v1': asg.get(g, {}).get('v1'),
                           'solver_v2': v2, 'primary_rank1': prim_rank1,
                           'secondary_found': sec_found, 'ok': ok})

    # truth-in-inventory (diagnostic, DEMOTE-3)
    # (computed by the Runner from the inventory; placeholder here)
    return {
        'n_nonpin': len(nonpin),
        'pins_intact': pins_ok,
        'primary': round(primary, 4),
        'primary_hits': sum(prim_hit.values()),
        'proj_equiv': round(proj_equiv, 4),
        'proj_equiv_hits': sum(proj_hit.values()),
        'secondary': round(secondary, 4),
        'mrr': round(mrr, 4),
        'n_islets': len(islets),
        'islets_ok': isl_ok,
        'islet_detail': isl_detail,
        'per_group_primary': prim_hit,
    }


def gate_6instance(per_instance):
    """Apply the REGISTERED §4 bars with 6-instance aggregation.

    per_instance: list of 6 metrics dicts from score_assignment().
    Returns (verdict, checklist). Islets/MRR/baseline-margin are
    diagnostics only (KILL-1).
    """
    assert len(per_instance) == 6, \
        f'§4 requires 6 instances, got {len(per_instance)}'
    primaries = [m['primary'] for m in per_instance]
    secondaries = [m['secondary'] for m in per_instance]
    p_mean = sum(primaries) / 6
    p_min = min(primaries)
    s_mean = sum(secondaries) / 6
    s_min = min(secondaries)
    b = BARS_4
    checks = [
        ('primary mean >= 0.20', p_mean >= b['primary_mean'],
         f'{p_mean:.4f}'),
        ('primary min >= 0.10', p_min >= b['primary_min'],
         f'{p_min:.4f}'),
        ('secondary mean >= 0.30', s_mean >= b['secondary_mean'],
         f'{s_mean:.4f}'),
        ('secondary min >= 0.22', s_min >= b['secondary_min'],
         f'{s_min:.4f}'),
        ('primary mean >= μ+5σ (0.098)', p_mean >= b['primary_5sigma'],
         f'{p_mean:.4f}'),
        ('secondary mean >= μ+5σ (0.227)', s_mean >= b['secondary_5sigma'],
         f'{s_mean:.4f}'),
    ]
    # diagnostics (not gates)
    diag = {
        'primary_per_instance': [round(x, 4) for x in primaries],
        'secondary_per_instance': [round(x, 4) for x in secondaries],
        'proj_equiv_per_instance': [m['proj_equiv'] for m in per_instance],
        'pins_intact_per_instance': [m['pins_intact'] for m in per_instance],
        'islets_ok_per_instance': [m['islets_ok'] for m in per_instance],
        'mrr_per_instance': [m['mrr'] for m in per_instance],
    }
    verdict = 'CONTROL-PASS' if all(c[1] for c in checks) else 'CONTROL-FAIL'
    return verdict, checks, diag


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--ct', help='SYNTHETIC-ct-<seed>.pairs.txt (single)')
    ap.add_argument('--truth', help='SEALED SYNTHETIC-key file (single)')
    ap.add_argument('--crib', default=None,
                    help='SYNTHETIC-crib file (anchors)')
    ap.add_argument('--anchors', default=None,
                    help='JSON pins (alt. to --crib)')
    ap.add_argument('--lm', help='LM json (single-instance mode)')
    ap.add_argument('--out', help='output dir (single-instance mode)')
    ap.add_argument('--config', default=os.path.join(HERE, 'config.json'))
    ap.add_argument('--seed', type=int, default=1841)
    ap.add_argument('--restarts', type=int, default=None)
    ap.add_argument('--iters', type=int, default=None)
    ap.add_argument('--no-phase', action='store_true')
    ap.add_argument('--no-word', action='store_true')
    ap.add_argument('--no-poly', action='store_true')
    ap.add_argument('--no-contact', action='store_true',
                    help='DEMOTE-1/CONCERN-4: uniform proposals, no block '
                         'moves (isolates the Jaccard contact machinery)')
    ap.add_argument('--aggregate', nargs=6, metavar='REPORT',
                    help='6 per-instance control_report.json files; apply '
                         'the §4 gate with 6-instance aggregation')
    a = ap.parse_args()

    # ---- 6-instance aggregation mode (KILL-1) ----
    if a.aggregate:
        per_instance = []
        for rp in a.aggregate:
            rep = json.load(open(rp))
            per_instance.append(rep['metrics'])
        verdict, checks, diag = gate_6instance(per_instance)
        print('[harness] §4 gate (6-instance aggregation):', flush=True)
        for name, ok, val in checks:
            print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {val}",
                  flush=True)
        print('[harness] diagnostics (not gates):', flush=True)
        for k, v in diag.items():
            print(f'  {k}: {v}', flush=True)
        print(f'[harness] VERDICT: {verdict}', flush=True)
        out = {'bars': BARS_4, 'verdict': verdict,
               'checks': [{'bar': c[0], 'pass': c[1], 'value': c[2]}
                          for c in checks],
               'diagnostics': diag,
               'date': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
        opath = 'control_verdict.json'
        json.dump(out, open(opath, 'w'), ensure_ascii=False, indent=1)
        print(f'[harness] wrote {opath}', flush=True)
        return

    # ---- single-instance mode: run + score ----
    assert a.ct and a.truth and a.lm and a.out, \
        'single-instance mode needs --ct, --truth, --lm, --out'
    cfg = dict(DEFAULTS)
    if os.path.exists(a.config):
        cfg.update(json.load(open(a.config)))
    if a.restarts:
        cfg['restarts'] = a.restarts
    if a.iters:
        cfg['iters'] = a.iters

    pairs, meta = load_synthetic(a.ct)
    print(f"[harness] synthetic control: {meta['n_pairs']} pairs, "
          f"{meta['n_groups']} groups, seed={meta['seed']}", flush=True)
    assert meta['n_pairs'] == 1846 and meta['n_groups'] == 96, \
        'control shape differs from R5005; refusing (report to Designer)'
    if a.crib:
        anchors = json.load(open(a.crib))['anchors']
    else:
        anchors = json.loads(a.anchors) if a.anchors else {}
    assert len(anchors) == 7, 'expected the 7 pinned anchors'
    # LM independence: the control plaintext (Les Mis) must not be in the LM
    lm_meta = json.load(open(a.lm))['meta']
    assert 'mis' not in ' '.join(lm_meta['corpus']).lower(), \
        'LM corpus overlaps control plaintext'

    # ---- run the solver (no truth in scope) ----
    result = run(pairs, anchors, a.lm, cfg, a.out, a.seed,
                 no_phase=a.no_phase, no_word=a.no_word, no_poly=a.no_poly,
                 no_contact=a.no_contact)
    # ---- score (truth enters only here) ----
    truth = _load_truth_robust(a.truth)
    assert truth.get('synthetic'), 'truth file not labelled synthetic'
    metrics = score_assignment(result, truth, pairs, anchors)
    # optimization sanity (diagnostic, not a gate)
    bl = result['baseline_random20']
    margin = result['best']['best'] - bl['max']
    report = {
        'meta': {**meta, 'bars': 'CONTROL-DESIGN.md §4 (see gate_6instance)',
                 'date': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())},
        'metrics': metrics,
        'baseline_margin_nats': round(margin, 1),
        'note': 'per-instance metrics; apply gate_6instance (--aggregate) '
                'for the §4 verdict',
    }
    with open(os.path.join(a.out, 'control_report.json'), 'w') as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    print(f"[harness] primary={metrics['primary']:.4f} "
          f"proj_equiv={metrics['proj_equiv']:.4f} "
          f"secondary={metrics['secondary']:.4f} "
          f"mrr={metrics['mrr']:.4f} islets={metrics['islets_ok']}/"
          f"{metrics['n_islets']} margin={margin:+.1f}nats", flush=True)
    print(f"[harness] wrote {a.out}/control_report.json", flush=True)
    print('[harness] no verdict at instance level; use --aggregate for §4',
          flush=True)


if __name__ == '__main__':
    main()
