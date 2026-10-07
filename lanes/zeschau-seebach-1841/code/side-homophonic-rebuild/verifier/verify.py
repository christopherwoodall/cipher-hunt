#!/usr/bin/env python3
"""CLOSING VERIFIER driver: independent confirmation of the pilot FAIL.

Usage: python3 verify.py  (reads data files + preserved pilot artifacts only)
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rescore import (Rescorer, load_pairs, load_anchors, load_truth,
                     project, REBUILD, RUNS)

SEED = '184101'
cfg = json.load(open(os.path.join(REBUILD, 'solver', 'config.json')))
print(f'[verifier] config: lambda_poly={cfg["lambda_poly"]} '
      f'lambda_word={cfg["lambda_word"]} word_minlen={cfg["word_minlen"]} '
      f'lambda_conc={cfg["lambda_conc"]} conc_cap={cfg["conc_cap"]}')

pairs = load_pairs(SEED)
anchors = load_anchors(SEED)
truth = load_truth(SEED)
print(f'[verifier] pairs={len(pairs)} groups={len(set(pairs))} anchors={len(anchors)}')

r = Rescorer(pairs, cfg)
print(f'[verifier] phase: chi2={r.phase["chi2"]} gate={r.phase["gate"]} beta={r.beta:.3f}')

# ---- planted truth (post-diagnostic forensics; sealed key opened for verification)
v1t, v2t, w2t = {}, {}, {}
for g in r.groups:
    if g in anchors:
        v1t[g] = anchors[g]
        v2t[g] = None
    else:
        v1t[g] = truth[g]['primary']
        sec = truth[g].get('secondaries') or []
        v2t[g] = sec[0] if sec else None
        w2t[g] = 0.5 if sec else 0.0
pt = r.score(v1t, v2t, w2t, label='TRUTH (planted)', verbose=True)
truth_nsec = sum(1 for g in r.groups if v2t[g])
print(f'[verifier] truth: {truth_nsec} secondaries planted')

# ---- pilot winner (restart 199939, from preserved artifact)
pilot = json.load(open(os.path.join(REBUILD, 'pilot', 'rebuild-pilot-final', 'result.json')))
bw = pilot['best']
v1s = {g: bw['assignment'][g]['v1'] for g in r.groups}
v2s = {g: bw['assignment'][g]['v2'] for g in r.groups}
ps = r.score(v1s, v2s, {}, label='SALAD (pilot winner 199939)', verbose=True)
print(f'[verifier] pilot-recorded parts: S_char={bw["score_parts"]["S_char"]} '
      f'S_cov={bw["score_parts"]["S_cov"]} S_single={bw["score_parts"]["S_single"]} '
      f'S_conc={bw["score_parts"]["S_conc"]} S_potts={bw["score_parts"]["S_potts"]} '
      f'n_poly={bw["score_parts"]["n_poly"]} total={bw["best"]:.1f}')

margin = ps['total'] - pt['total']
print(f'[verdict-a] salad total {ps["total"]:.1f} vs truth {pt["total"]:.1f}: '
      f'salad wins by {margin:+.1f} nats '
      f'({"CONFIRM ~2577" if abs(margin - 2577) < 15 else "MISMATCH"})')

# ---- primary recovery of the salad
hit = sum(1 for g in r.groups if g not in anchors and v1s[g] == truth[g]['primary'])
nnp = sum(1 for g in r.groups if g not in anchors)
rec = hit / nnp
print(f'[verdict-b] primary recovery: {hit}/{nnp} = {rec:.4f} '
      f'({"CONFIRM ~0.0112" if abs(rec - 0.0112) < 0.002 else "MISMATCH"})')

# ---- morpheme composition (projected values)
comp = collections.Counter(project(v) for v in v1s.values())
print('[verdict-c] salad composition (projected value x groups):')
for v, n in comp.most_common(15):
    print(f'    {v!r} x{n}')
print(f'[verifier] distinct values: {len(comp)}')

# ---- R2 discrepancy: word_minlen=0 (gate off) vs 6 (shipped)
print()
print('=== R2: frozen degenerate under gate OFF (minlen=0) vs shipped (minlen=6) ===')
fdeg = json.load(open(os.path.join(RUNS, 'run2-184101', 'result.json')))
v1d = {g: fdeg['best']['assignment'][g]['v1'] for g in r.groups}
v2d = {g: fdeg['best']['assignment'][g]['v2'] for g in r.groups}
w2d = {g: fdeg['best']['assignment'][g]['w2'] for g in r.groups}
pd0 = r.score(v1d, v2d, w2d, label='DEGEN minlen=0', minlen=0, verbose=True)
pt0 = r.score(v1t, v2t, w2t, label='TRUTH minlen=0', minlen=0, verbose=True)
pd6 = r.score(v1d, v2d, w2d, label='DEGEN minlen=6', minlen=6, verbose=True)
print(f'[verdict-r2] minlen=0: degen {pd0["total"]:.1f} vs truth {pt0["total"]:.1f}')
print(f'   R2 reported: degen -4585.6 vs truth -7215.7')
r2ok = abs(pd0['total'] - (-4585.6)) < 15 and abs(pt0['total'] - (-7215.7)) < 15
print(f'   -> {"REPRODUCES (gate-off explains R2)" if r2ok else "DOES NOT REPRODUCE"}')
print(f'[verdict-r2] minlen=6: degen {pd6["total"]:.1f} vs truth {pt["total"]:.1f}: '
      f'margin {pt["total"] - pd6["total"]:+.1f} (shipped config flips optimum: '
      f'{"CONFIRM" if pt["total"] > pd6["total"] else "REFUTE"})')

# ---- quota distributions (conc-penalty separability), incl. other seeds
print()
print('=== quota distributions: max projected-value group-count ===')
for seed in ['184101', '184102', '184103', '184104', '184105', '184106']:
    pr = load_pairs(seed)
    an = load_anchors(seed)
    tr = load_truth(seed)
    vv = {g: (an[g] if g in an else tr[g]['primary']) for g in sorted(set(pr))}
    q = collections.Counter(project(x) for x in vv.values())
    print(f'   truth-{seed}: max quota={max(q.values())} '
          f'(top: {q.most_common(3)})')
qs = r.quota_dist(v1s)
qt = r.quota_dist(v1t)
print(f'   salad-184101: max quota={max(qs.values())} (top: {qs.most_common(5)})')
print(f'   truth-184101: max quota={max(qt.values())} (top: {qt.most_common(5)})')
for cap in (6, 4, 2):
    cs = sum((n - cap) ** 2 for n in qs.values() if n > cap)
    ct = sum((n - cap) ** 2 for n in qt.values() if n > cap)
    cd = sum((n - cap) ** 2 for n in collections.Counter(
        project(v1d[g]) for g in r.groups).values() if n > cap)
    print(f'   S_conc cap={cap}: salad={cs} truth={ct} frozen-degen={cd}')

json.dump({'truth': pt, 'salad': ps, 'degen0': pd0, 'truth0': pt0, 'degen6': pd6},
          open(os.path.join(HERE, 'parts.json'), 'w'), indent=1,
          default=lambda o: None)
print('[verifier] parts saved to verifier/parts.json (decode stripped)')
