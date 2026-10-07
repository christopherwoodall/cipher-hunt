#!/usr/bin/env python3
"""R5005 candidate homophone-set battery.

For each candidate pair: E1 phase separation, E2 individual coherence,
E3 label-free follower/pred disjointness, E4 merged-vs-single era fit
(the key discriminator), E5 phase-explained split (F33-form rule +
falsifiers), E6 merged unigram vs era, E7 raw top contacts for the report.

Writes battery.json. Reads era_rates.json.
"""
import json, math, sys
from collections import Counter, defaultdict
from pathlib import Path

LANE = Path('/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, str(LANE / 'code' / 'crowd7' / 'keystruct'))
from aliasing import load_stream, phase_labels, contact_profiles  # noqa: E402

OUT = LANE / 'code' / 'crowd7' / 'keystruct'
N = 1847

# candidate: (name, a, b, reading, kind)  kind: word|syll|frag|allo
CANDIDATES = [
    ('M1', 87, 47, 'ce', 'word'),
    ('M2', 77, 0, 'le', 'word'),      # 00 polyvalent pour/le -- conditioned
    ('M3', 78, 45, 'me', 'syll'),     # 78 polyvalent me/ver -- conditioned
    ('M4', 29, 78, 'er', 'frag'),     # 78 er-islet only @1180/@1351; F30: no rate leg
    ('M5', 1, 59, 'est', 'word'),
    ('M6', 37, 77, 'le', 'word'),
    ('M7', 16, 34, 'i', 'frag'),      # 16='i' unconfirmed; F30: no rate leg
    ('M8', 43, 21, 'me', 'word'),
    ('M9', 6, 86, 'stem-allomorph', 'allo'),  # F40 M1 positive control (grammatical, not phase)
]

# cipher group -> word reading (GT + provisional + leads), for E4 known set
KNOWN = {11: 'la', 70: 'pre', 82: 'm', 34: 'i', 29: 'er', 40: 'e', 46: 'que',
         87: 'ce', 64: 'qui', 96: 'par', 77: 'le', 59: 'est', 62: 'on',
         52: 'pas', 94: 'ne', 24: 'en', 67: 'veut', 47: 'ce', 37: 'le',
         1: 'est', 21: 'me', 78: 'me', 45: 'me'}


def xent(obs_counts, era_ps):
    """Cross-entropy of observed distribution vs era probs (nats/token)."""
    tot = sum(obs_counts.values())
    if tot == 0:
        return None
    h = 0.0
    for k, c in obs_counts.items():
        p = era_ps.get(k, 1e-6)
        h -= (c / tot) * math.log(p)
    return h


def main():
    pairs = load_stream()
    cache = OUT / 'phase_cache.json'
    if cache.exists():
        c = json.load(open(cache))
        block = {int(k): v for k, v in c['block'].items()}
        nxt, prv = c['nxt'], c['prv']
    else:
        block, chi2, info = phase_labels(pairs)
        cnt = info['cnt']
        s1 = sum(cnt[f'{r}{c}'] for r, c in [('A', 'B'), ('B', 'C'), ('C', 'A')])
        s2 = sum(cnt[f'{r}{c}'] for r, c in [('A', 'C'), ('C', 'B'), ('B', 'A')])
        nxt = {'A': 'B', 'B': 'C', 'C': 'A'} if s1 >= s2 else {'A': 'C', 'C': 'B', 'B': 'A'}
        prv = {v: k for k, v in nxt.items()}
        json.dump({'block': block, 'nxt': nxt, 'prv': prv, 'chi2': chi2}, open(cache, 'w'))
    prof = contact_profiles(pairs, block)
    era = json.load(open(OUT / 'era_rates.json'))
    freq = Counter(pairs)
    big = Counter(zip(pairs[:-1], pairs[1:]))

    results = []
    for name, a, b, reading, kind in CANDIDATES:
        pa, pb = prof[a], prof[b]
        pha, phb = pa['phase'], pb['phase']
        # E1
        e1_sep = pha != phb and 'R' not in (pha, phb)
        # E2 coherence
        def coh(g):
            pr = prof[g]; ph = pr['phase']
            if ph == 'R':
                return None
            return round((pr['succ_phase'].get(nxt[ph], 0) + pr['pred_phase'].get(prv[ph], 0)) / 2, 3)
        # E3 disjointness (label-free)
        fa, fb = set(pa['succ']), set(pb['succ'])
        ra, rb = set(pa['pred']), set(pb['pred'])
        j_s = len(fa & fb) / len(fa | fb) if fa | fb else 0
        j_p = len(ra & rb) / len(ra | rb) if ra | rb else 0
        # E4: merged vs single era fit on known followers/preds
        e4 = None
        if kind in ('word', 'syll') and reading in era['foll']:
            ef_full = era['foll'][reading]['full']; tf = era['foll'][reading]['tot']
            ep_full = era['pred'][reading]['full']; tp = era['pred'][reading]['tot']
            ef = {w: c / tf for w, c in ef_full.items()}
            ep = {w: c / tp for w, c in ep_full.items()}
            # map known cipher follower groups to words
            def known_dist(counter):
                d = Counter()
                for h, c in counter.items():
                    if h in KNOWN:
                        d[KNOWN[h]] += c
                return d
            mf = known_dist(Counter(pa['succ']) + Counter(pb['succ']))
            mp = known_dist(Counter(pa['pred']) + Counter(pb['pred']))
            af = known_dist(Counter(pa['succ'])); bf = known_dist(Counter(pb['succ']))
            ap = known_dist(Counter(pa['pred'])); bp = known_dist(Counter(pb['pred']))
            e4 = {
                'xent_foll_merged': xent(mf, ef), 'xent_foll_a': xent(af, ef),
                'xent_foll_b': xent(bf, ef),
                'xent_pred_merged': xent(mp, ep), 'xent_pred_a': xent(ap, ep),
                'xent_pred_b': xent(bp, ep),
                'n_known_foll': sum(mf.values()), 'n_known_pred': sum(mp.values()),
            }
        # E5: phase-explained split -- Fisher-style 2x2 + falsifier rate
        # rows: alias a/b; cols: follower-phase == expected vs other
        tab = [[0, 0], [0, 0]]
        fals = tot = 0
        for ri, g in enumerate((a, b)):
            ph = prof[g]['phase']
            if ph == 'R':
                continue
            for h, c in prof[g]['succ'].items():
                tot += c
                ok = block.get(h) == nxt[ph]
                tab[ri][0 if ok else 1] += c
                if not ok:
                    fals += c
            for h, c in prof[g]['pred'].items():
                tot += c
                ok = block.get(h) == prv[ph]
                tab[ri][0 if ok else 1] += c
                if not ok:
                    fals += c
        # Fisher exact on tab (2x2)
        def fisher(t):
            [[x1, y1], [x2, y2]] = t
            from math import comb
            n = x1 + y1 + x2 + y2
            if n == 0:
                return None
            # two-sided via enumeration over x1'
            lo = max(0, x1 + x2 - (y1 + y2) - 0)  # careful margins
            # use hypergeometric pmf directly
            r1, r2 = x1 + y1, x2 + y2
            c1 = x1 + x2
            def hg(k):
                return comb(r1, k) * comb(r2, c1 - k) / comb(n, c1) if 0 <= k <= r1 and 0 <= c1 - k <= r2 else 0
            p0 = hg(x1)
            return sum(hg(k) for k in range(0, n + 1) if hg(k) <= p0 + 1e-12)
        e5 = {'table': tab, 'fisher_p': fisher(tab),
              'fals_rate': round(fals / tot, 4) if tot else None,
              'fals': fals, 'tot': tot}
        # E6 merged unigram vs era
        e6 = None
        if kind in ('word', 'syll'):
            erap = era['uni'][reading]['p'] if reading in era['uni'] else None
            if erap:
                mrate = (freq[a] + freq[b]) / N
                e6 = {'merged_rate': round(mrate, 5), 'era_p': round(erap, 5),
                      'ratio': round(mrate / erap, 3),
                      'single_a_ratio': round((freq[a] / N) / erap, 3),
                      'single_b_ratio': round((freq[b] / N) / erap, 3)}
        # E7 raw tops
        def top5(c):
            return [[h, cnt] for h, cnt in Counter(c).most_common(5)]
        res = {
            'name': name, 'a': a, 'b': b, 'reading': reading, 'kind': kind,
            'na': freq[a], 'nb': freq[b], 'pha': pha, 'phb': phb,
            'E1_sep': e1_sep, 'E2_coh_a': coh(a), 'E2_coh_b': coh(b),
            'E3_j_succ': round(j_s, 4), 'E3_j_pred': round(j_p, 4),
            'E4': e4, 'E5': e5, 'E6': e6,
            'top_succ_a': top5(pa['succ']), 'top_succ_b': top5(pb['succ']),
            'top_pred_a': top5(pa['pred']), 'top_pred_b': top5(pb['pred']),
            'shared_succ': sorted(fa & fb), 'shared_pred': sorted(ra & rb),
        }
        results.append(res)
        print(f"{name} ({a},{b})={reading} [{kind}]: phases {pha}/{phb} sep={e1_sep} "
              f"coh={coh(a)}/{coh(b)} j_s={j_s:.3f} j_p={j_p:.3f} "
              f"fals={e5['fals_rate']} fisherp={e5['fisher_p'] and round(e5['fisher_p'],4)} "
              f"E6={e6 and e6['ratio']}")
    json.dump(results, open(OUT / 'battery.json', 'w'), indent=1)
    print('wrote battery.json')


if __name__ == '__main__':
    main()
