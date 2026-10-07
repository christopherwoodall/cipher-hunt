#!/usr/bin/env python3
"""Synthetic calibration for the key-structure (aliasing) analyst.

Builds 2 generator instances with OWN seeds (known key) and measures, for
TRUE alias pairs (same primary cell, >=2 groups) vs RANDOM different-phase
pairs, the candidate discriminator statistics:

  E1  phase separation (different Jaccard-cluster phases)
  E2  individual coherence (contacts concentrated in expected blocks)
  E3  follower/pred Jaccard (label-free disjointness)
  E4f merged follower distribution vs true cell follower distribution (key known)
  E4p merged follower distribution vs "era" on anchor-cells only (partial)
  E5  phase-explained split: falsifier count of the dealing rule
  M1  delta block-chi2 after merging b->a (labels recomputed)
  M2  delta label-free lag-3 z after merging b->a

Goal: learn which statistics discriminate and the null distributions, so the
R5005 battery is calibrated, not improvised.
"""
import json, math, sys
from collections import Counter, defaultdict
from pathlib import Path

LANE = Path('/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, str(LANE / 'code' / 'side-homophonic' / 'control'))
sys.path.insert(0, str(LANE / 'code' / 'crowd7' / 'keystruct'))
from generator import (PARAMS, build_instance, load_lesmis_tokens,
                       real_group_labels, unsupervised_chi2)  # noqa: E402
from aliasing import phase_labels, contact_profiles  # noqa: E402

OUT = LANE / 'code' / 'crowd7' / 'keystruct'


def lag3_z(pairs):
    """Label-free lag-3 group-equality excess z vs independence null."""
    n = len(pairs) - 3
    obs = sum(1 for i in range(n) if pairs[i] == pairs[i + 3])
    f = Counter(pairs)
    N = len(pairs)
    exp_p = sum((c / N) ** 2 for c in f.values())
    exp = n * exp_p
    se = math.sqrt(n * exp_p * (1 - exp_p))
    return (obs - exp) / se if se else 0.0


def build_pair_stats(pairs, block, prof, a, b, nxt, prv):
    """All discriminator stats for ordered pair (a,b)."""
    fa, fb = set(prof[a]['succ']), set(prof[b]['succ'])
    pa, pb = set(prof[a]['pred']), set(prof[b]['pred'])
    j_succ = len(fa & fb) / len(fa | fb) if fa | fb else 0.0
    j_pred = len(pa & pb) / len(pa | pb) if pa | pb else 0.0
    # E2: individual coherence
    def coh(g):
        pr = prof[g]; ph = pr['phase']
        if ph == 'R':
            return None
        s = pr['succ_phase'].get(nxt[ph], 0.0)
        p = pr['pred_phase'].get(prv[ph], 0.0)
        return (s + p) / 2
    # E5: phase-explained split falsifiers (token-level)
    fals = 0; tot = 0
    for g, ph in ((a, block[a]), (b, block[b])):
        if ph == 'R':
            continue
        for h, c in prof[g]['succ'].items():
            tot += c
            if block.get(h) != nxt[ph]:
                fals += c
        for h, c in prof[g]['pred'].items():
            tot += c
            if block.get(h) != prv[ph]:
                fals += c
    return {
        'sep': block[a] != block[b] and 'R' not in (block[a], block[b]),
        'coh_a': coh(a), 'coh_b': coh(b),
        'j_succ': round(j_succ, 4), 'j_pred': round(j_pred, 4),
        'fals_rate': round(fals / tot, 4) if tot else None,
        'fals': fals, 'tot': tot,
    }


def main():
    tokens = load_lesmis_tokens()
    glabels = real_group_labels()
    p = dict(PARAMS)
    my_seeds = [184201, 184202]
    p['seeds'] = my_seeds
    rng = __import__('random').Random(77)
    rows = []
    for seed in my_seeds:
        inst = build_instance(seed, tokens, glabels, p, T=56)
        pairs = [int(g) for g in inst['pairs']]
        key = {int(g): v for g, v in inst['key'].items()}
        planted = inst['planted']
        print(f'seed {seed}: pairs={len(pairs)} unsup_chi2={inst["chi2"]} '
              f'occ phases planted ok', flush=True)
        # true alias pairs: same primary cell, >=2 groups, both freq>=8
        bycell = defaultdict(list)
        for g, v in key.items():
            bycell[v['primary']].append(g)
        freq = Counter(pairs)
        true_pairs = []
        for cell, gs in bycell.items():
            gs = [g for g in gs if freq[g] >= 8]
            for i in range(len(gs)):
                for j in range(i + 1, len(gs)):
                    true_pairs.append((gs[i], gs[j], cell))
        print(f'  true alias pairs (freq>=8): {len(true_pairs)}', flush=True)

        block, chi2, info = phase_labels(pairs)
        prof = contact_profiles(pairs, block)
        # cycle direction from block counts
        cnt = info['cnt']
        cyc = [('A', 'B'), ('B', 'C'), ('C', 'A')]
        s1 = sum(cnt[f'{r}{c}'] for r, c in cyc)
        cyc2 = [('A', 'C'), ('C', 'B'), ('B', 'A')]
        s2 = sum(cnt[f'{r}{c}'] for r, c in cyc2)
        if s1 >= s2:
            nxt = {'A': 'B', 'B': 'C', 'C': 'A'}
        else:
            nxt = {'A': 'C', 'C': 'B', 'B': 'A'}
        prv = {v: k for k, v in nxt.items()}
        print(f'  cycle: {nxt} (s1={s1}, s2={s2})', flush=True)

        # random different-phase pairs matched on frequency band
        cand = [g for g in set(pairs) if freq[g] >= 8 and block[g] != 'R']
        true_set = set()
        for a, b, _ in true_pairs:
            true_set.add((a, b)); true_set.add((b, a))
        rand_pairs = []
        tries = 0
        while len(rand_pairs) < min(60, len(true_pairs) * 3) and tries < 20000:
            tries += 1
            a, b = rng.sample(cand, 2)
            if block[a] == block[b]:
                continue
            ka, kb = key[a]['primary'], key[b]['primary']
            if ka == kb:
                continue
            if (a, b) in true_set:
                continue
            # frequency match: both within factor 2 of a true pair's geomean? just take any
            rand_pairs.append((a, b, f'{ka}/{kb}'))
        print(f'  random pairs: {len(rand_pairs)}', flush=True)

        z0 = lag3_z(pairs)
        for tag, plist in (('TRUE', true_pairs), ('RAND', rand_pairs)):
            for a, b, cell in plist:
                st = build_pair_stats(pairs, block, prof, a, b, nxt, prv)
                # M1: merge b->a, recompute labels+chi2
                merged = [a if x == b else x for x in pairs]
                _, chi2m, _ = phase_labels(merged)
                # M2: label-free lag-3 z after merge
                zm = lag3_z(merged)
                rows.append({
                    'seed': seed, 'tag': tag, 'a': a, 'b': b, 'cell': cell,
                    'na': freq[a], 'nb': freq[b],
                    'pha': block[a], 'phb': block[b],
                    'chi2_0': chi2, 'chi2_m': chi2m, 'd_chi2': round(chi2m - chi2, 1),
                    'z0': round(z0, 3), 'zm': round(zm, 3), 'd_z': round(zm - z0, 3),
                    **st,
                })
    (OUT / 'calibration_pairs.json').write_text(json.dumps(rows, indent=1))
    # summary
    for tag in ('TRUE', 'RAND'):
        sel = [r for r in rows if r['tag'] == tag]
        def m(k):
            vs = [r[k] for r in sel if r[k] is not None]
            return round(sum(vs) / len(vs), 4) if vs else None
        print(f"{tag} n={len(sel)} sep={m('sep')} coh_a={m('coh_a')} coh_b={m('coh_b')} "
              f"j_succ={m('j_succ')} j_pred={m('j_pred')} fals={m('fals_rate')} "
              f"d_chi2={m('d_chi2')} d_z={m('d_z')}")
    print('wrote calibration_pairs.json', len(rows))


if __name__ == '__main__':
    main()
