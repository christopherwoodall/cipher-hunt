#!/usr/bin/env python3
"""Synthetic polyvalence breakdown: 'more of the same' stress test.

Adds K synthetic islets, each modeled like the known ones: one cipher group
covering two phonetically similar syllables (same rhyme class, mirroring
06:/ma~ vs /a~/ and 94:ne vs en). Penetration q=0.5. Measures:
  - naive pattern survival (overall, at-risk, repetition-words)
  - smart inflation for repetition cipher patterns
over K = 0, 3, 10, 30 with 3 random seeds.

Rationale: the lane holds polyvalence is the cipher's general mechanism
(96 groups << ~700 French syllables; 06 verb-stem provisional) but only
three islets are identified. This bounds how much MORE of the same the
instrument tolerates before breaking.
"""
import json, random, itertools, math, sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from polyvalence_test import survival_curve, pattern, POLY_PHON

LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
LEX = LANE / 'code' / 'side-wordpattern' / 'lexicon' / 'lexicon.jsonl'
OUT = Path(__file__).parent
Q = 0.5


def load():
    entries = [json.loads(l) for l in open(LEX, encoding='utf-8')]
    idx = defaultdict(list)
    for e in entries:
        idx[(e['nsyl'], e['ppat'])].append(e['w'])
    return entries, idx


def rhyme_classes(entries):
    sylls = set()
    for e in entries:
        sylls.update(e['phon'])
    rc = defaultdict(list)
    for s in sylls:
        rc[s[-2:] if len(s) >= 2 else s].append(s)
    # only classes with >=2 members, excluding already-polyvalent syllables
    known = set(POLY_PHON)
    return [[s for s in v if s not in known] for v in rc.values() if len(v) >= 2]


def run(K, seed, entries, idx, rcl):
    rng = random.Random(seed)
    poly = {s: list(v) for s, v in POLY_PHON.items()}
    classes = rng.sample(rcl, K) if K else []
    for i, cl in enumerate(classes):
        a, b = rng.sample(cl, 2)
        g = f"SYN{i}"
        poly.setdefault(a, []).append((g, 1.0))
        poly.setdefault(b, []).append((g, 1.0))
    # survival over all words containing any polyvalent syllable
    test = [e for e in entries if any(s in poly for s in e['phon'])]
    surv_all, surv_rep, n_rep = [], [], 0
    rep_words = [e for e in test if e['ppat'] != ''.join(chr(65 + i) for i in range(len(e['phon'])))]
    for e in test:
        c, _ = survival_curve(e['phon'], e['ppat'], poly, qgrid=[Q])
        if c is not None:
            surv_all.append(c[Q])
    for e in rep_words:
        c, _ = survival_curve(e['phon'], e['ppat'], poly, qgrid=[Q])
        if c is not None:
            surv_rep.append(c[Q])
    # smart inflation for repetition cipher patterns (sample: compute closure)
    reach_extra = defaultdict(set)
    for e in test:
        _, reach = survival_curve(e['phon'], e['ppat'], poly, qgrid=[Q])
        if reach:
            for cp in reach:
                reach_extra[(e['nsyl'], cp)].add(e['w'])
    infls = []
    for (n, cp), ws in reach_extra.items():
        if cp == ''.join(chr(65 + i) for i in range(n)):
            continue
        naive = set(idx.get((n, cp), []))
        if naive:
            infls.append(len(naive | ws) / len(naive))
    infls.sort(reverse=True)
    return {
        'K': K, 'seed': seed, 'n_test': len(test), 'n_rep': len(rep_words),
        'mean_survival_all': sum(surv_all) / len(surv_all) if surv_all else None,
        'mean_survival_rep': sum(surv_rep) / len(surv_rep) if surv_rep else None,
        'min_survival_rep': min(surv_rep) if surv_rep else None,
        'max_smart_inflation': infls[0] if infls else None,
        'p95_smart_inflation': infls[int(0.05 * len(infls))] if infls else None,
        'n_rep_patterns': len(infls),
    }


def main():
    entries, idx = load()
    rcl = rhyme_classes(entries)
    print(f"rhyme classes available: {len(rcl)}")
    out = []
    for K in [0, 3, 10, 30]:
        for seed in [11, 22, 33]:
            r = run(K, seed, entries, idx, rcl)
            out.append(r)
            print(f"K={K:3d} seed={seed}: n_test={r['n_test']:5d} "
                  f"surv_all={r['mean_survival_all']:.3f} "
                  f"surv_rep={r['mean_survival_rep']:.3f} (min {r['min_survival_rep']:.3f}) "
                  f"max_infl={r['max_smart_inflation']:.1f}x p95={r['p95_smart_inflation']:.1f}x")
    with open(OUT / 'synthetic_breakdown.json', 'w') as f:
        json.dump(out, f, indent=1)
    print('wrote', OUT / 'synthetic_breakdown.json')


if __name__ == '__main__':
    main()
