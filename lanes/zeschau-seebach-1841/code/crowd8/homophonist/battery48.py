#!/usr/bin/env python3
"""Round-8 WO1 homophonist: dedicated 48='ne'-allophone battery.

Pre-registered in PRE-REGISTER.md (written before stream access).
Claim: homophone set {94,48}='ne' (94='ne' provisional-strong).
Frame: F33 B1-B5 + F56 interchangeability template + M1-M9 E1-E7 design.
"""
import json, math, sys
from collections import Counter
from math import comb
from pathlib import Path

LANE = Path('/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, str(LANE / 'code' / 'crowd7' / 'keystruct'))
from aliasing import load_stream, contact_profiles  # noqa: E402

OUT = LANE / 'code' / 'crowd8' / 'homophonist'
N = 1847
A, B = 94, 48  # anchor 94='ne' prov-strong; candidate 48


def fisher2x2(a, b, c, d):
    n = a + b + c + d
    if n == 0:
        return None
    r1, r2 = a + b, c + d
    c1 = a + c
    def hg(k):
        return (comb(r1, k) * comb(r2, c1 - k) / comb(n, c1)
                if 0 <= k <= r1 and 0 <= c1 - k <= r2 else 0.0)
    p0 = hg(a)
    return sum(hg(k) for k in range(n + 1) if hg(k) <= p0 + 1e-12)


def cos(u, v):
    keys = set(u) | set(v)
    dot = sum(u.get(k, 0) * v.get(k, 0) for k in keys)
    nu = math.sqrt(sum(x * x for x in u.values()))
    nv = math.sqrt(sum(x * x for x in v.values()))
    return dot / (nu * nv) if nu and nv else 0.0


def xent(obs_counts, era_ps):
    tot = sum(obs_counts.values())
    if tot == 0:
        return None
    return -sum((c / tot) * math.log(era_ps.get(k, 1e-6))
                for k, c in obs_counts.items())


def main():
    pairs = load_stream()
    assert len(pairs) == N
    freq = Counter(pairs)
    cache = json.load(open(LANE / 'code/crowd7/keystruct/phase_cache.json'))
    block = {int(k): v for k, v in cache['block'].items()}
    prof = contact_profiles(pairs, block)
    era = json.load(open(LANE / 'code/crowd7/keystruct/era_rates.json'))
    diplo = json.load(open(LANE / 'code/crowd7/closer/diplomatic_rates.json'))

    R = {'n_pairs': N, 'checks': {}}
    pa, pb = prof[A], prof[B]
    na, nb = freq[A], freq[B]
    pha, phb = pa['phase'], pb['phase']

    # ---- P0: instrument check ----
    R['checks']['P0'] = {'n94': na, 'n48': nb, 'phase94': pha, 'phase48': phb,
                         'referral_n48': 38, 'n48_match': nb == 38}
    # referral predecessor-cosine re-derivation (verification, not scored)
    pred_cos = cos(Counter(pa['pred']), Counter(pb['pred']))
    # noise floor: median predecessor-cosine of 48 vs all groups with n>=20
    big = [g for g in set(pairs) if freq[g] >= 20 and g != B]
    pre_floor = sorted(cos(Counter(pb['pred']), Counter(prof[g]['pred']))
                         for g in big)
    pre_floor_med = pre_floor[len(pre_floor) // 2]
    R['checks']['P0']['pred_cos_48_94'] = round(pred_cos, 4)
    R['checks']['P0']['pred_cos_floor_median'] = round(pre_floor_med, 4)
    R['checks']['P0']['referral_reproduced'] = pred_cos >= 0.70 and pre_floor_med <= 0.50
    print(f"P0: n94={na} n48={nb} phases {pha}/{phb} pred_cos={pred_cos:.4f} floor_med={pre_floor_med:.4f}")

    # ---- H1: F56 interchangeability (same phase B/B -> straight template) ----
    h1 = {'phase_branch': 'same' if (pha == phb and pha != 'R') else
          ('separated' if pha != phb and 'R' not in (pha, phb) else 'R-null')}
    if h1['phase_branch'] == 'same':
        # 94's top follower cell and top predecessor cell (rule, not value)
        tf = Counter(pa['succ']).most_common(1)[0]
        tp = Counter(pa['pred']).most_common(1)[0]
        cells = [('follower', tf[0], tf[1]), ('predecessor', tp[0], tp[1])]
        h1['cells'] = []
        for kind, cell, ca in cells:
            cb = (Counter(pb['succ']) if kind == 'follower'
                  else Counter(pb['pred'])).get(cell, 0)
            tot_a = na if kind == 'follower' else na  # contacts ~ n (edge effects negligible)
            # exact contact totals:
            tot_a = sum(Counter(pa['succ' if kind == 'follower' else 'pred']).values())
            tot_b = sum(Counter(pb['succ' if kind == 'follower' else 'pred']).values())
            p = fisher2x2(ca, tot_a - ca, cb, tot_b - cb)
            kill = (p is not None and p < 0.01 and ca >= 4 and cb == 0)
            h1['cells'].append({'kind': kind, 'cell': cell, 'n94': ca,
                                'n48': cb, 'fisher_p': p, 'kill': kill})
            print(f"H1 {kind} cell={cell}: 94x{ca}/{tot_a} 48x{cb}/{tot_b} p={p:.4g} kill={kill}")
        h1['verdict'] = 'KILL' if any(c['kill'] for c in h1['cells']) else 'survives'
    elif h1['phase_branch'] == 'separated':
        h1['verdict'] = 'E5-branch-not-taken'
    else:
        h1['verdict'] = 'NULL'
    R['checks']['H1'] = h1

    # ---- H2: B1 merged unigram vs diplomatic era P(ne) ----
    # primary: guizot-t5t6 (1840-42 despatches) + nesselrode-v8 (1840-46); pooled
    dp = {}
    for corp in ('guizot-t5t6', 'nesselrode-v8'):
        v = diplo[corp]
        dp[corp] = v['n_ne'] / v['n_tokens']
    n_ne_pool = sum(diplo[c]['n_ne'] for c in ('guizot-t5t6', 'nesselrode-v8'))
    n_tok_pool = sum(diplo[c]['n_tokens'] for c in ('guizot-t5t6', 'nesselrode-v8'))
    era_p_ne = n_ne_pool / n_tok_pool
    # sound-rate comparator: ne + n' (elided particle, same /n/ sound in a syllabary)
    n_snd_pool = sum(diplo[c]['n_ne'] + diplo[c]['n_n'] for c in ('guizot-t5t6', 'nesselrode-v8'))
    era_p_ne_snd = n_snd_pool / n_tok_pool
    merged = (na + nb) / N
    ratio = merged / era_p_ne
    ratio_snd = merged / era_p_ne_snd
    single94 = (na / N) / era_p_ne
    single94_snd = (na / N) / era_p_ne_snd
    # pre-registered bar runs on the word rate (00='pour' B1 precedent was word-level);
    # sound rate recorded as the fence analysis (l'-cell precedent cuts both ways)
    h2 = {'era_p_ne_diplo_word': round(era_p_ne, 5),
          'era_p_ne_diplo_sound': round(era_p_ne_snd, 5),
          'per_corp': {k: round(v, 5) for k, v in dp.items()},
          'merged_rate': round(merged, 5), 'ratio_word': round(ratio, 3),
          'ratio_sound': round(ratio_snd, 3),
          'single94_ratio_word': round(single94, 3),
          'single94_ratio_sound': round(single94_snd, 3),
          'tocqueville_uni_ne_word': round(era['uni']['ne']['p'], 5),
          'note': '94 banked at 1.025x on a syllable-level 0.01902 (morphologist); '
                  'era_rates.json uni[ne] word-level = 0.00833, agrees with diplomatic 0.00850',
          'verdict': ('PASS' if 0.5 <= ratio <= 2.0 else
                      'KILL' if ratio > 3 else 'weak-adverse'),
          'verdict_sound': ('PASS' if 0.5 <= ratio_snd <= 2.0 else
                            'KILL' if ratio_snd > 3 else 'weak-adverse')}
    R['checks']['H2'] = h2
    print(f"H2: wordP={era_p_ne:.5f} ratio={ratio:.3f} ({h2['verdict']}) | soundP={era_p_ne_snd:.5f} ratio={ratio_snd:.3f} ({h2['verdict_sound']}) | single94 {single94:.3f}/{single94_snd:.3f}")

    # ---- H3: 'ne'-frame B2/B4 ----
    ef_full = era['foll']['ne']['full']; tf_e = era['foll']['ne']['tot']
    era_foll_ne = {w: c / tf_e for w, c in ef_full.items()}
    top5_ne = sorted(era_foll_ne, key=era_foll_ne.get, reverse=True)[:5]
    f94, f48 = Counter(pa['succ']), Counter(pb['succ'])
    n94_52, n48_52 = f94.get(52, 0), f48.get(52, 0)
    # 94's observed P(52|94); expected 48->52 under it
    tot_f94, tot_f48 = sum(f94.values()), sum(f48.values())
    p52_94 = n94_52 / tot_f94 if tot_f94 else 0
    E_48_52 = p52_94 * tot_f48
    # which era top-5 followers does each take (map via KNOWN lane values)
    KNOWN = {11: 'la', 70: 'pre', 82: 'm', 34: 'i', 29: 'er', 40: 'e', 46: 'que',
             87: 'ce', 64: 'qui', 96: 'par', 77: 'le', 59: 'est', 62: 'on',
             52: 'pas', 94: 'ne', 24: 'en', 67: 'veut', 47: 'ce', 37: 'le',
             1: 'est', 21: 'me', 78: 'me', 45: 'me'}
    def known_words(counter):
        d = Counter()
        for h, c in counter.items():
            if h in KNOWN:
                d[KNOWN[h]] += c
        return d
    kw94, kw48 = known_words(f94), known_words(f48)
    # B4 rival-kill shape (pre-reg H3(ii)): licensed cells = 52 ('pas') + era top-5
    licensed = ['pas'] + top5_ne
    take94 = [w for w in licensed if kw94.get(w, 0) > 0]
    take48 = [w for w in licensed if kw48.get(w, 0) > 0]
    h3 = {'era_top5_ne_followers': top5_ne,
          'n94_52': n94_52, 'n48_52': n48_52,
          'P52_given_94': round(p52_94, 4), 'E_48_52': round(E_48_52, 2),
          'pas_check_powered': E_48_52 >= 1.5,
          'take94': take94, 'take48': take48,
          'n_take94': len(take94)}
    if E_48_52 < 1.5:
        h3['pas_cell'] = 'NULL-underpowered'
    else:
        p = fisher2x2(n94_52, tot_f94 - n94_52, n48_52, tot_f48 - n48_52)
        h3['pas_cell'] = {'fisher_p': p, 'verdict': 'PASS' if p >= 0.10 else 'adverse'}
    # B4 rival-kill shape
    if len(take94) >= 3 and len(take48) == 0:
        h3['B4'] = 'adverse'
    elif len(take48) >= 1:
        # rate within 0.25-4x of 94's rate at shared cells
        ratios = []
        for w in take48:
            if w in take94:
                r = (kw48[w] / tot_f48) / (kw94[w] / tot_f94)
                ratios.append(round(r, 3))
        h3['B4'] = {'verdict': 'PASS' if any(0.25 <= r <= 4 for r in ratios) else 'adverse',
                    'shared_rate_ratios': ratios}
    else:
        h3['B4'] = 'null'
    # B4 era-0 scan: 48 contacts with cipher>=2 and era('ne',.)==0 (Tocqueville;
    # diplomatic corpus lacks follower/pred dists — recorded limitation)
    era0_hits = []
    pred48 = Counter(pb['pred'])
    for kind, counter, emap in (('foll', f48, era['foll']['ne']['full']),
                                ('pred', pred48, era['pred']['ne']['full'])):
        for h, c in counter.items():
            if c >= 2 and h in KNOWN and emap.get(KNOWN[h], 0) == 0:
                era0_hits.append([kind, h, KNOWN[h], c])
    # Tocqueville backup already in era; diplomatic lacks dists (recorded)
    h3['era0_hits'] = era0_hits
    h3['verdict'] = ('adverse' if h3['B4'] == 'adverse' or
                     (isinstance(h3.get('pas_cell'), dict) and h3['pas_cell']['verdict'] == 'adverse')
                     else 'PASS' if h3['B4'] != 'null' and isinstance(h3['B4'], dict) and h3['B4']['verdict'] == 'PASS'
                     else 'null')
    R['checks']['H3'] = h3
    print(f"H3: top5ne={top5_ne} 94->52 x{n94_52} 48->52 x{n48_52} E={E_48_52:.2f} take94={take94} take48={take48} era0={era0_hits} -> {h3['verdict']}")

    # ---- H4: follower-profile cosine (new leg) ----
    f_cos = cos(f48, f94)
    f_floor = sorted(cos(f48, Counter(prof[g]['succ'])) for g in big)
    f_floor_med = f_floor[len(f_floor) // 2]
    h4 = {'foll_cos_48_94': round(f_cos, 4), 'floor_median': round(f_floor_med, 4),
          'verdict': 'PASS' if f_cos >= 0.60 else ('adverse' if f_cos <= f_floor_med else 'null')}
    R['checks']['H4'] = h4
    print(f"H4: foll_cos={f_cos:.4f} floor_med={f_floor_med:.4f} -> {h4['verdict']}")

    # ---- H5: 48->47 x2 tension vs 47's conditioned 'ce' rule ----
    # Q2 fragment rule: fragment reading iff suc(47)==78 or pre(47)==29; else 'ce'
    pos_48_47 = [i for i in range(N - 1) if pairs[i] == 48 and pairs[i + 1] == 47]
    wins = []
    for i in pos_48_47:
        pre47 = pairs[i]          # = 48
        suc47 = pairs[i + 2] if i + 2 < N else None
        fragment = (suc47 == 78 or pre47 == 29)
        wins.append({'pos': i, 'pre47': pre47, 'suc47': suc47,
                     'fragment_reading': fragment,
                     'forced_ce': not fragment})
    forced = sum(1 for w in wins if w['forced_ce'])
    h5 = {'n': len(pos_48_47), 'windows': wins,
          'verdict': 'fenced' if forced == 0 else 'adverse'}
    R['checks']['H5'] = h5
    print(f"H5: 48->47 x{len(pos_48_47)} forced_ce={forced} -> {h5['verdict']}")

    # ---- H6: E4 merged-vs-single era fit on 'ne' contacts ----
    ep_full = era['pred']['ne']['full']; tp_e = era['pred']['ne']['tot']
    era_pred_ne = {w: c / tp_e for w, c in ep_full.items()}
    mf = known_words(f94 + f48); mp = known_words(Counter(pa['pred']) + Counter(pb['pred']))
    af = known_words(f94); ap = known_words(Counter(pa['pred']))
    h6 = {'xent_foll_merged': xent(mf, era_foll_ne), 'xent_foll_94': xent(af, era_foll_ne),
          'xent_pred_merged': xent(mp, era_pred_ne), 'xent_pred_94': xent(ap, era_pred_ne),
          'n_known_foll': sum(mf.values()), 'n_known_pred': sum(mp.values())}
    d_f = (h6['xent_foll_94'] - h6['xent_foll_merged']) if None not in (h6['xent_foll_94'], h6['xent_foll_merged']) else None
    d_p = (h6['xent_pred_94'] - h6['xent_pred_merged']) if None not in (h6['xent_pred_94'], h6['xent_pred_merged']) else None
    h6['delta_foll'] = d_f; h6['delta_pred'] = d_p
    # PASS if merged better by >0.3 nats on either side with n_known>=5 there
    legs = []
    if d_f is not None and h6['n_known_foll'] >= 5:
        legs.append('PASS' if d_f > 0.3 else ('adverse' if d_f < -0.3 else 'null'))
    if d_p is not None and h6['n_known_pred'] >= 5:
        legs.append('PASS' if d_p > 0.3 else ('adverse' if d_p < -0.3 else 'null'))
    h6['verdict'] = ('PASS' if 'PASS' in legs else
                     'adverse' if 'adverse' in legs else 'null')
    R['checks']['H6'] = h6
    print(f"H6: dx_foll={d_f} dx_pred={d_p} n={h6['n_known_foll']}/{h6['n_known_pred']} -> {h6['verdict']}")

    # ---- verdict ----
    scored = {k: R['checks'][k]['verdict'] for k in ('H1', 'H2', 'H3', 'H4', 'H6')}
    passes = [k for k, v in scored.items() if v == 'PASS']
    adverses = [k for k, v in scored.items() if v == 'adverse']
    kills = []
    if any(c.get('kill') for c in h1.get('cells', [])):
        kills.append('H1-F56')
    if h2['verdict'] == 'KILL':
        kills.append('H2-B1')
    if h5['verdict'] == 'adverse':
        adverses.append('H5')
    R['verdict'] = {
        'passes': passes, 'adverses': adverses, 'kills': kills,
        'h5': h5['verdict'],
        'ruling': ('KILL' if kills or len(adverses) >= 2 else
                   'CONFIRM-LEAD' if len(passes) >= 2 and not kills and h5['verdict'] != 'adverse'
                   else 'HONEST-NULL')}
    print('VERDICT:', R['verdict'])
    json.dump(R, open(OUT / 'battery48_results.json', 'w'), indent=1)
    print('wrote battery48_results.json')


if __name__ == '__main__':
    main()
