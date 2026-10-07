#!/usr/bin/env python3
"""Within-phase contact-profile similarity: the primary homophone instrument.

Contact-coherent aliasing (N43/F49): aliases dealt coherently share
phase-conditioned contact profiles. Within one phase, candidate aliases of a
cell have SIMILAR successor/predecessor distributions (same group space --
directly comparable, no alias-map circularity).

For every same-phase pair: cosine similarity of succ profiles + pred
profiles (Laplace-smoothed). Null: all same-phase pairs -> percentile/z for
each candidate. Candidates are the same-phase pairs among the case-law set;
also reports the top-20 same-phase pairs overall (discovery).
"""
import json, math, sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

LANE = Path('/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, str(LANE / 'code' / 'crowd7' / 'keystruct'))
from aliasing import load_stream, contact_profiles  # noqa: E402

OUT = LANE / 'code' / 'crowd7' / 'keystruct'


def cos_sim2(c1, c2, vocab, alpha=1.0):
    v1 = [(c1.get(h, 0) + alpha) for h in vocab]
    v2 = [(c2.get(h, 0) + alpha) for h in vocab]
    dot = sum(x * y for x, y in zip(v1, v2))
    n1 = math.sqrt(sum(x * x for x in v1)); n2 = math.sqrt(sum(x * x for x in v2))
    return dot / (n1 * n2) if n1 and n2 else 0.0


def main():
    pairs = load_stream()
    c = json.load(open(OUT / 'phase_cache.json'))
    block = {int(k): v for k, v in c['block'].items()}
    prof = contact_profiles(pairs, block)
    groups = sorted(set(pairs))
    vocab = groups
    by_phase = defaultdict(list)
    for g in groups:
        if block[g] != 'R':
            by_phase[block[g]].append(g)
    results = []
    for ph, gs in by_phase.items():
        sims = []
        for a, b in combinations(sorted(gs), 2):
            s = cos_sim2(prof[a]['succ'], prof[b]['succ'], vocab)
            p = cos_sim2(prof[a]['pred'], prof[b]['pred'], vocab)
            sims.append((a, b, round((s + p) / 2, 4), round(s, 4), round(p, 4)))
        sims.sort(key=lambda t: -t[2])
        # null stats for this phase
        vals = [t[2] for t in sims]
        mu = sum(vals) / len(vals); sd = math.sqrt(sum((v - mu) ** 2 for v in vals) / len(vals))
        results.append({'phase': ph, 'n_groups': len(gs), 'n_pairs': len(sims),
                        'mu': round(mu, 4), 'sd': round(sd, 4),
                        'top20': [{'a': a, 'b': b, 'sim': s, 'sim_s': ss, 'sim_p': sp,
                                   'z': round((s - mu) / sd, 2) if sd else 0,
                                   'na': prof[a]['n'], 'nb': prof[b]['n']}
                                  for a, b, s, ss, sp in sims[:20]],
                        'all': [{'a': a, 'b': b, 'sim': s,
                                 'z': round((s - mu) / sd, 2) if sd else 0}
                                for a, b, s, ss, sp in sims]})
    json.dump(results, open(OUT / 'within_phase_sim.json', 'w'), indent=1)
    # candidate lookup
    cand = [(87, 47), (77, 0), (29, 78), (16, 34), (6, 86)]
    lookup = {}
    for r in results:
        for e in r['all']:
            lookup[(e['a'], e['b'])] = (r['phase'], e['sim'], e['z'])
            lookup[(e['b'], e['a'])] = (r['phase'], e['sim'], e['z'])
    print('candidate within-phase similarities:')
    for a, b in cand:
        ph, s, z = lookup.get((a, b), ('?', 0, 0))
        na = sum(1 for x in pairs if x == a); nb = sum(1 for x in pairs if x == b)
        print(f'  ({a},{b}) phase={ph} sim={s} z={z} n={na}/{nb}')
    print()
    print('top-5 per phase:')
    for r in results:
        print(f" phase {r['phase']} (mu={r['mu']}, sd={r['sd']}):")
        for e in r['top20'][:5]:
            print(f"   ({e['a']},{e['b']}) sim={e['sim']} z={e['z']} n={e['na']}/{e['nb']}")


if __name__ == '__main__':
    main()
