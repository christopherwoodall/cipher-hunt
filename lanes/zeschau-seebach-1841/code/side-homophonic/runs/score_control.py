#!/usr/bin/env python3
"""Apply the PRE-REGISTERED CONTROL-DESIGN.md §4 bars to harness outputs.

Bars (finalized by CONTROL-DESIGN.md, not the harness's stale proposed BARS):
  PRIMARY:   mean >= 0.20, min >= 0.10  (chance 0.0216±0.0153, μ+5σ≈0.098)
  SECONDARY: mean >= 0.30, min >= 0.22  (chance 0.1434±0.0167, μ+5σ≈0.227)

SECONDARY here = harness 'secondary_proxy' (frequency-weighted primary
agreement per position; per-position planted cells are not persisted by the
generator — CONTROL-DESIGN.md §4's exact decode metric is unattainable from
write_instance output; the proxy is the closest computable quantity and is
documented as such).
"""
import json, os, sys

SH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SEEDS = ['184101', '184102', '184103', '184104', '184105', '184106']

rows = []
for s in SEEDS:
    rep = json.load(open(os.path.join(SH, 'runs', f'ctl-{s}', 'control_report.json')))
    m = rep['metrics']
    rows.append({'seed': s,
                 'primary': m['primary'], 'primary_hits': m['primary_hits'],
                 'n_nonpin': m['n_nonpin'],
                 'secondary_proxy': m['secondary_proxy'],
                 'mrr': m['mrr'], 'pins': m['pins_intact'],
                 'islets_ok': m['islets_ok'], 'n_islets': m['n_islets']})

prim = [r['primary'] for r in rows]
sec = [r['secondary_proxy'] for r in rows]
checks = {
    'primary_mean>=0.20': sum(prim)/len(prim) >= 0.20,
    'primary_min>=0.10': min(prim) >= 0.10,
    'secondary_mean>=0.30': sum(sec)/len(sec) >= 0.30,
    'secondary_min>=0.22': min(sec) >= 0.22,
    'pins_7/7_all': all(r['pins'] == 7 for r in rows),
}
verdict = 'CONTROL-PASS' if all(checks.values()) else 'CONTROL-FAIL'
out = {'verdict': verdict, 'checks': checks,
       'primary_mean': round(sum(prim)/len(prim), 4),
       'primary_min': round(min(prim), 4),
       'secondary_mean': round(sum(sec)/len(sec), 4),
       'secondary_min': round(min(sec), 4),
       'per_instance': rows}
json.dump(out, open(os.path.join(SH, 'runs', 'control_verdict.json'), 'w'), indent=1)
print(json.dumps(out, indent=1))
