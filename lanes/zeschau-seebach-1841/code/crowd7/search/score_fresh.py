#!/usr/bin/env python3
"""Score search outputs on the fresh control against the sealed keys.

Implements the PRE-REGISTERED 6-check gate (CONTROL-DESIGN.md §4,
code/side-homophonic/solver/control_harness.py::gate_6instance):
  PRIMARY   = exact v1[g] == planted primary, 89 non-pin groups
  SECONDARY = per-position decode accuracy, 1846 pairs
              (pins auto-correct; v1[g]==planted[t] or v2[g]==planted[t])
  6 checks: primary mean>=0.20, primary min>=0.10,
            secondary mean>=0.30, secondary min>=0.22,
            primary mean>=0.098 (mu+5sigma), secondary mean>=0.227 (mu+5sigma)
Diagnostics: proj_equiv, pins_intact, islets.

Usage: python3 score_fresh.py <rundir-tag>   (e.g. baseline, prototype)
Reads: runs/<tag>/asg-<seed>.json (+ asg-noramp-<seed>.json for the noramp tag)
Writes: runs/<tag>/GATE.json
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'side-homophonic', 'solver'))
from phonetics import project  # noqa: E402  (diagnostic only)

FRESH = json.load(open(os.path.join(HERE, 'fresh', 'build_summary.json')))
SEEDS = [str(s) for s in FRESH['seeds']]
INST = os.path.join(HERE, 'fresh', 'instances')
PINS = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i',
        '29': 'er', '40': 'e', '46': 'que'}

BARS = {'primary_mean': 0.20, 'primary_min': 0.10,
        'secondary_mean': 0.30, 'secondary_min': 0.22,
        'primary_5sigma': 0.098, 'secondary_5sigma': 0.227}


def load_pairs(seed):
    pairs = []
    for ln in open(os.path.join(INST, 'SYNTHETIC-ct-%s.pairs.txt' % seed)):
        if ln.startswith('#') or not ln.strip():
            continue
        pairs.extend(ln.split())
    return pairs


def score_one(seed, asg):
    key = json.load(open(os.path.join(INST, 'SYNTHETIC-key-%s.json' % seed)))
    planted = key['planted']
    pairs = load_pairs(seed)
    assert len(planted) == len(pairs) == 1846
    kkey, v1, v2 = key['key'], asg['v1'], asg.get('v2', {})
    nonpin = [g for g in kkey if g not in PINS]

    prim_hit = {g: 1 if v1.get(g) == kkey[g]['primary'] else 0 for g in nonpin}
    primary = sum(prim_hit.values()) / len(nonpin)
    proj_equiv = sum(1 for g in nonpin
                     if project(v1.get(g) or '') == project(kkey[g]['primary'])
                     ) / len(nonpin)
    tot, hit = 0, 0
    for t, g in enumerate(pairs):
        tot += 1
        if g in PINS:
            hit += 1
        elif v1.get(g) == planted[t] or (v2.get(g) == planted[t]
                                         and v2.get(g) is not None):
            hit += 1
    secondary = hit / tot
    islets = [g for g in nonpin if kkey[g].get('secondaries')]
    isl_ok = sum(1 for g in islets
                 if v1.get(g) == kkey[g]['primary']
                 and v2.get(g) == (kkey[g]['secondaries'][0]
                                   if kkey[g]['secondaries'] else None))
    pins_ok = sum(1 for g, c in PINS.items() if v1.get(g) == c)
    return {'seed': seed, 'n_nonpin': len(nonpin),
            'primary': round(primary, 4),
            'primary_hits': sum(prim_hit.values()),
            'proj_equiv': round(proj_equiv, 4),
            'proj_equiv_hits': sum(1 for g in nonpin
                                   if project(v1.get(g) or '') ==
                                   project(kkey[g]['primary'])),
            'secondary': round(secondary, 4),
            'pins_intact': pins_ok, 'n_islets': len(islets),
            'islets_ok': isl_ok}


def main(tag):
    rundir = os.path.join(HERE, 'runs', tag)
    per = []
    for seed in SEEDS:
        # noramp variant files are asg-noramp-<seed>.json under tag 'noramp'
        pat = 'asg-%s.json' % seed
        p = os.path.join(rundir, pat)
        if not os.path.exists(p):
            # prototype files carry the method tag
            cands = [f for f in os.listdir(rundir)
                     if f.endswith('-%s.json' % seed)]
            assert len(cands) == 1, (seed, cands)
            p = os.path.join(rundir, cands[0])
        asg = json.load(open(p))
        per.append(score_one(seed, asg))
    prim = [m['primary'] for m in per]
    sec = [m['secondary'] for m in per]
    checks = [
        ('primary mean >= 0.20', sum(prim) / 6 >= BARS['primary_mean']),
        ('primary min >= 0.10', min(prim) >= BARS['primary_min']),
        ('secondary mean >= 0.30', sum(sec) / 6 >= BARS['secondary_mean']),
        ('secondary min >= 0.22', min(sec) >= BARS['secondary_min']),
        ('primary mean >= mu+5sigma (0.098)',
         sum(prim) / 6 >= BARS['primary_5sigma']),
        ('secondary mean >= mu+5sigma (0.227)',
         sum(sec) / 6 >= BARS['secondary_5sigma']),
    ]
    out = {'tag': tag, 'SYNTHETIC': True,
           'verdict': 'CONTROL-PASS' if all(c[1] for c in checks)
                      else 'CONTROL-FAIL',
           'checks': [{'check': c[0], 'pass': bool(c[1])} for c in checks],
           'primary_mean': round(sum(prim) / 6, 4),
           'primary_min': round(min(prim), 4),
           'primary_per_instance': [round(x, 4) for x in prim],
           'secondary_mean': round(sum(sec) / 6, 4),
           'secondary_min': round(min(sec), 4),
           'secondary_per_instance': [round(x, 4) for x in sec],
           'proj_equiv_mean': round(sum(m['proj_equiv'] for m in per) / 6, 4),
           'proj_equiv_per_instance': [m['proj_equiv'] for m in per],
           'pins_intact': [m['pins_intact'] for m in per],
           'islets_ok': [m['islets_ok'] for m in per],
           'per_instance': per}
    json.dump(out, open(os.path.join(rundir, 'GATE.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in out.items()
                      if k != 'per_instance'}, indent=1))


if __name__ == '__main__':
    main(sys.argv[1])
