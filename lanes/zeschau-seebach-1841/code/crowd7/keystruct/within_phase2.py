#!/usr/bin/env python3
"""Within-phase contact-profile similarity v2.

Metrics (no heavy smoothing):
  - Jaccard on top-K contact sets (K=10; the contactor's own metric):
    J(A,B) = |topA cap topB| / |topA cup topB|, averaged over succ+pred.
  - Cosine on raw count vectors (alpha=0.1 light smoothing).
Null per phase over pairs with n>=12 (sparse groups cluster spuriously).
Candidates scored regardless of n. Also top-25 discovery (n>=12).
"""
import json, math, sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

LANE = Path('/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, str(LANE / 'code' / 'crowd7' / 'keystruct'))
from aliasing import load_stream, contact_profiles  # noqa: E402

OUT = LANE / 'code' / 'crowd7' / 'keystruct'
K = 10
MINN = 12


def topk(counter, k=K):
    return set(h for h, _ in Counter(counter).most_common(k))


def jac(a, b):
    u = a | b
    return len(a & b) / len(u) if u else 0.0


def cos_raw(c1, c2, vocab, alpha=0.1):
    v1 = [c1.get(h, 0) + alpha for h in vocab]
    v2 = [c2.get(h, 0) + alpha for h in vocab]
    dot = sum(x * y for x, y in zip(v1, v2))
    n1 = math.sqrt(sum(x * x for x in v1)); n2 = math.sqrt(sum(x * x for x in v2))
    return dot / (n1 * n2) if n1 and n2 else 0.0


def main():
    pairs = load_stream()
    c = json.load(open(OUT / 'phase_cache.json'))
    block = {int(k): v for k, v in c['block'].items()}
    prof = contact_profiles(pairs, block)
    groups = sorted(set(pairs))
    by_phase = defaultdict(list)
    for g in groups:
        if block[g] != 'R':
            by_phase[block[g]].append(g)
    out = []
    for ph, gs in by_phase.items():
        gs_n = [g for g in gs if prof[g]['n'] >= MINN]
        sims = []
        for a, b in combinations(sorted(gs), 2):
            js = jac(topk(prof[a]['succ']) | topk(prof[a]['pred']),
                     topk(prof[b]['succ']) | topk(prof[b]['pred']))
            cs = (cos_raw(prof[a]['succ'], prof[b]['succ'], groups) +
                  cos_raw(prof[a]['pred'], prof[b]['pred'], groups)) / 2
            sims.append({'a': a, 'b': b, 'jac': round(js, 4), 'cos': round(cs, 4),
                         'na': prof[a]['n'], 'nb': prof[b]['n']})
        null = [s for s in sims if s['na'] >= MINN and s['nb'] >= MINN]
        for key in ('jac', 'cos'):
            vs = [s[key] for s in null]
            mu = sum(vs) / len(vs); sd = math.sqrt(sum((v - mu) ** 2 for v in vs) / len(vs))
            for s in sims:
                s[key + '_z'] = round((s[key] - mu) / sd, 2) if sd else 0.0
            out_mu, out_sd = mu, sd
        sims.sort(key=lambda s: -s['jac_z'])
        out.append({'phase': ph, 'n_groups': len(gs), 'null_n': len(null),
                    'null_mu_jac': round(sum(s['jac'] for s in null) / len(null), 4),
                    'null_mu_cos': round(sum(s['cos'] for s in null) / len(null), 4),
                    'top25': [s for s in sims if s['na'] >= MINN and s['nb'] >= MINN][:25],
                    'all': sims})
    json.dump(out, open(OUT / 'within_phase_sim2.json', 'w'), indent=1)
    lookup = {}
    for r in out:
        for s in r['all']:
            lookup[(s['a'], s['b'])] = (r['phase'], s)
    print('candidate within-phase similarities (null: n>=12 same-phase pairs):')
    for a, b, name in [(87, 47, 'M1 ce'), (77, 0, 'M2 le'), (29, 78, 'M4 er'),
                       (16, 34, 'M7 i'), (6, 86, 'M9 allo')]:
        ph, s = lookup[tuple(sorted((a, b)))]
        print(f"  {name} ({a},{b}) phase={ph} jac={s['jac']} z={s['jac_z']} "
              f"cos={s['cos']} z={s['cos_z']} n={s['na']}/{s['nb']}")
    print()
    for r in out:
        print(f"phase {r['phase']}: null n={r['null_n']} mu_jac={r['null_mu_jac']} mu_cos={r['null_mu_cos']}")
        for s in r['top25'][:6]:
            print(f"   ({s['a']},{s['b']}) jac={s['jac']} z={s['jac_z']} cos={s['cos']} z={s['cos_z']} n={s['na']}/{s['nb']}")


if __name__ == '__main__':
    main()
