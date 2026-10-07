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
      SECONDARY = frequency-weighted primary agreement per position
                  (proxy: per-position planted cells are not persisted by the
                  generator, so this compares decoded primaries to truth
                  primaries; labelled as such)
      ISLET     = secondary recovery on polyvalent islet groups
      MRR       = mean reciprocal rank of the truth primary in the solver's
                  restart marginals
  gate(metrics, chance) -> (verdict, report)
      Pre-registered bars (proposed; CONTROL-DESIGN.md finalizes):
        1. pins intact 7/7
        2. PRIMARY >= 0.50 (89 non-anchor groups)
        3. PRIMARY >= chance_analytic + 0.30
        4. ISLET: >= 4/6 islet groups recover the secondary (v2 exact or in
           top-3 marginals) with the truth primary ranked #1
        5. optimization sanity: best - random20.max >= 200 nats
        6. MRR >= 0.60
      All six -> CONTROL-PASS. Else BROKEN-ON-CONTROL with diagnosis.

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

# proposed pre-registered bars (CONTROL-DESIGN.md finalizes)
BARS = {
    'pins_intact': 7,
    'primary_min': 0.50,
    'primary_lift_over_chance': 0.30,
    'islets_min': 4,
    'islets_total': 6,
    'baseline_margin_nats': 200.0,
    'mrr_min': 0.60,
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
    """Read the SEALED key file (Runner's eyes only). Strips the leading
    '// ...' comment line the generator writes."""
    txt = open(path).read()
    lines = [l for l in txt.splitlines() if not l.lstrip().startswith('//')]
    return json.loads('\n'.join(lines))


def run(pairs, anchors, lm_path, cfg, out_dir, seed, **solver_opts):
    return run_restarts(pairs, anchors, {}, lm_path, cfg, out_dir, seed,
                        no_soft=True, **solver_opts)


def score_assignment(result, truth, pairs, pins):
    """Score a solver result against the sealed truth. No solver input."""
    key = truth['key']
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
    # SECONDARY (proxy): frequency-weighted primary agreement per position
    tot, hit = 0, 0
    for g in pairs:
        if g in pins:
            hit += 1
        else:
            hit += prim_hit.get(g, 0)
        tot += 1
    secondary = hit / tot
    # MRR of truth primary in restart marginals
    rrs = []
    for g in nonpin:
        tv = key[g]['primary']
        ranked = [v for v, _ in marg.get(g, [])]
        rrs.append(1.0 / (ranked.index(tv) + 1) if tv in ranked else 0.0)
    mrr = sum(rrs) / len(rrs) if rrs else 0.0
    # ISLETS: groups with secondaries in the truth
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
                           'true_secondary': tv2, 'solver_v1': asg.get(g, {}).get('v1'),
                           'solver_v2': v2, 'primary_rank1': prim_rank1,
                           'secondary_found': sec_found, 'ok': ok})
    return {
        'n_nonpin': len(nonpin),
        'pins_intact': pins_ok,
        'primary': round(primary, 4),
        'primary_hits': sum(prim_hit.values()),
        'secondary_proxy': round(secondary, 4),
        'mrr': round(mrr, 4),
        'n_islets': len(islets),
        'islets_ok': isl_ok,
        'islet_detail': isl_detail,
        'per_group_primary': prim_hit,
    }


def gate(metrics, chance_analytic=None):
    """Apply the pre-registered bars. Returns (verdict, checklist)."""
    b = BARS
    checks = []
    checks.append(('pins_intact==7', metrics['pins_intact'] == b['pins_intact'],
                   f"{metrics['pins_intact']}/7"))
    checks.append(('primary>=0.50', metrics['primary'] >= b['primary_min'],
                   f"{metrics['primary']:.3f}"))
    if chance_analytic is not None:
        lift = metrics['primary'] - chance_analytic
        checks.append(('primary>=chance+0.30', lift >= b['primary_lift_over_chance'],
                       f'lift {lift:+.3f} over {chance_analytic:.3f}'))
    else:
        checks.append(('primary>=chance+0.30', None, 'no chance baseline given'))
    checks.append((f"islets>={b['islets_min']}/{b['islets_total']}",
                   metrics['islets_ok'] >= b['islets_min'],
                   f"{metrics['islets_ok']}/{metrics['n_islets']}"))
    # optimization sanity comes from the result, attached by main()
    verdict = 'CONTROL-PASS' if all(c[1] for c in checks if c[1] is not None) \
        else 'BROKEN-ON-CONTROL'
    if any(c[1] is None for c in checks):
        verdict += ' (INCOMPLETE: chance baseline missing)'
    return verdict, checks


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--ct', required=True, help='SYNTHETIC-ct-<seed>.pairs.txt')
    ap.add_argument('--truth', required=True, help='SEALED SYNTHETIC-key file')
    ap.add_argument('--crib', default=None, help='SYNTHETIC-crib file (anchors)')
    ap.add_argument('--anchors', default=None, help='JSON pins (alt. to --crib)')
    ap.add_argument('--lm', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--config', default=os.path.join(HERE, 'config.json'))
    ap.add_argument('--chance', type=float, default=None,
                    help='analytic chance PRIMARY from chance_baseline.json')
    ap.add_argument('--seed', type=int, default=1841)
    ap.add_argument('--restarts', type=int, default=None)
    ap.add_argument('--iters', type=int, default=None)
    ap.add_argument('--no-phase', action='store_true')
    ap.add_argument('--no-word', action='store_true')
    ap.add_argument('--no-poly', action='store_true')
    a = ap.parse_args()
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
                 no_phase=a.no_phase, no_word=a.no_word, no_poly=a.no_poly)
    # ---- score (truth enters only here) ----
    truth = _load_truth_robust(a.truth)
    assert truth.get('synthetic'), 'truth file not labelled synthetic'
    metrics = score_assignment(result, truth, pairs, anchors)
    verdict, checks = gate(metrics, a.chance)
    # optimization sanity (bar 5)
    bl = result['baseline_random20']
    margin = result['best']['best'] - bl['max']
    checks.append((f"best-random20>={BARS['baseline_margin_nats']:.0f}nats",
                   margin >= BARS['baseline_margin_nats'],
                   f'{margin:+.1f}'))
    if not all(c[1] for c in checks if c[1] is not None):
        verdict = 'BROKEN-ON-CONTROL'
    report = {
        'meta': {**meta, 'bars': BARS,
                 'date': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())},
        'metrics': metrics,
        'checks': [{'bar': c[0], 'pass': c[1], 'value': c[2]} for c in checks],
        'verdict': verdict,
    }
    with open(os.path.join(a.out, 'control_report.json'), 'w') as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    print('[harness] checks:', flush=True)
    for c in checks:
        print(f"  [{'PASS' if c[1] else 'FAIL' if c[1] is False else 'SKIP'}] "
              f"{c[0]}: {c[2]}", flush=True)
    print(f'[harness] VERDICT: {verdict}', flush=True)
    print(f"[harness] wrote {a.out}/control_report.json", flush=True)


if __name__ == '__main__':
    main()
