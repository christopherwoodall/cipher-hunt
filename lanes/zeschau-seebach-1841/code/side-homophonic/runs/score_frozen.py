#!/usr/bin/env python3
"""Independent re-derivation of the §4 gate verdict from per-instance
control_report.json files (frozen batch). Runner's own computation —
does not rely on the harness's verdict labels.

§4 bars (pre-registered, CONTROL-DESIGN.md):
  PRIMARY:   mean >= 0.20, min >= 0.10  (chance 0.0216±0.0153, μ+5σ≈0.098)
  SECONDARY: mean >= 0.30, min >= 0.22  (chance 0.1434±0.0167, μ+5σ≈0.227)
         — true decode accuracy (truth['planted'] persisted), NOT a proxy.
"""
import json, os

SH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SEEDS = ['184101', '184102', '184103', '184104', '184105', '184106']

rows = []
for s in SEEDS:
    rep = json.load(open(os.path.join(SH, 'runs', f'frozen-ctl-{s}',
                                      'control_report.json')))
    m = rep['metrics']
    rows.append({'seed': s,
                 'primary': m['primary'], 'primary_hits': m['primary_hits'],
                 'n_nonpin': m['n_nonpin'],
                 'secondary': m['secondary'],          # TRUE decode accuracy
                 'proj_equiv': m.get('proj_equiv'),
                 'mrr': m.get('mrr'), 'pins_intact': m['pins_intact'],
                 'islets_ok': m['islets_ok'], 'n_islets': m['n_islets']})

prim = [r['primary'] for r in rows]
sec = [r['secondary'] for r in rows]
checks = {
    'primary mean >= 0.20': sum(prim)/len(prim) >= 0.20,
    'primary min >= 0.10': min(prim) >= 0.10,
    'secondary mean >= 0.30': sum(sec)/len(sec) >= 0.30,
    'secondary min >= 0.22': min(sec) >= 0.22,
    'primary mean >= μ+5σ (0.098)': sum(prim)/len(prim) >= 0.098,
    'secondary mean >= μ+5σ (0.227)': sum(sec)/len(sec) >= 0.227,
    'pins 7/7 on all 6': all(r['pins_intact'] == 7 for r in rows),
}
verdict = 'CONTROL-PASS' if all(checks.values()) else 'CONTROL-FAIL'
out = {
    'verdict': verdict,
    'registrable': verdict == 'CONTROL-PASS',
    'checks': {k: {'pass': v} for k, v in checks.items()},
    'primary_mean': round(sum(prim)/len(prim), 4),
    'primary_min': round(min(prim), 4),
    'primary_per_instance': [round(x, 4) for x in prim],
    'secondary_mean': round(sum(sec)/len(sec), 4),
    'secondary_min': round(min(sec), 4),
    'secondary_per_instance': [round(x, 4) for x in sec],
    'per_instance': rows,
    'note': 'Runner-derived verdict, independent of harness verdict labels. '
            'Bars per CONTROL-DESIGN.md §4 (pre-registered).',
}
json.dump(out, open(os.path.join(SH, 'runs', 'frozen_verdict.json'), 'w'), indent=1)
for r in rows:
    print(f"  {r['seed']}: primary {r['primary_hits']:>2}/{r['n_nonpin']} = {r['primary']:.4f}  "
          f"secondary = {r['secondary']:.4f}  mrr = {r.get('mrr')}  pins {r['pins_intact']}/7  "
          f"islets {r['islets_ok']}/{r['n_islets']}")
print(f"primary:  mean {out['primary_mean']:.4f}  min {out['primary_min']:.4f}")
print(f"secondary: mean {out['secondary_mean']:.4f}  min {out['secondary_min']:.4f}")
for k, v in checks.items():
    print(f"  [{'PASS' if v else 'FAIL'}] {k}")
print('RUNNER VERDICT:', verdict)
