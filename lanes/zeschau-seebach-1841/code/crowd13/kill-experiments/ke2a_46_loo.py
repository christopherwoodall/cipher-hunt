#!/usr/bin/env python3
"""KE2 Part A — 46=que leave-one-out. Implements PREREG.md (locked 2026-10-07).

Gate G: 87=ce without any 46-involving leg (>=2 of G1,G2,G3 + 64=qui).
Then R1 (follower profile) + R2 (predecessor profile) re-derive 46.
Writes ke2a_results.json
"""
import json, math, os, re, sys
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
sys.path.insert(0, os.path.join(LANE, 'code', 'council', 'drag'))
from repaired_parse import load_pairs_repaired
from common import CORPUS, tok_elision

pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847

def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - m) / d, (c + m) / d)

def followers(g):
    return Counter(pairs[i + 1] for i in range(N - 1) if pairs[i] == g)

def predecessors(g):
    return Counter(pairs[i - 1] for i in range(1, N) if pairs[i] == g)

def bigram_count(a, b):
    return sum(1 for i in range(N - 1) if pairs[i] == a and pairs[i + 1] == b)

def trigram_count(a, b, c):
    return sum(1 for i in range(N - 2) if pairs[i] == a and pairs[i+1] == b and pairs[i+2] == c)

# ---------------- cipher side ----------------
f87, p87 = followers('87'), predecessors('87')
f46, p46 = followers('46'), predecessors('46')
f64 = followers('64')
n87 = sum(1 for g in pairs if g == '87')
n46 = sum(1 for g in pairs if g == '46')

cipher = {
    'n87': n87, 'n46': n46,
    'f87_top': f87.most_common(8), 'p87_top': p87.most_common(8),
    'n_f87_distinct': len(f87), 'n_p87_distinct': len(p87),
    'f46_top': f46.most_common(8), 'p46_top': p46.most_common(8),
    'rank_64_in_f87': sorted(f87.values(), reverse=True).index(f87['64']) + 1,
    'rank_46_in_f87': sorted(f87.values(), reverse=True).index(f87['46']) + 1,
    'rank_87_in_p46': sorted(p46.values(), reverse=True).index(p46['87']) + 1,
    'k_64_given_87': f87['64'], 'k_46_given_87': f87['46'],
    'k_87_given_46pre': p46['87'],
    'n_87_11': bigram_count('87', '11'),
    'n_24_87_64': trigram_count('24', '87', '64'),
    'wilson_64_given_87': wilson(f87['64'], n87),
}

# ---------------- corpus side ----------------
CORE = ['nesselrode-v7.txt', 'nesselrode-v9.txt', 'nesselrode-v10.txt',
        'guizot-memoires-t5-t6.txt', 'levant-correspondence-1841-p3.txt']
EXTRA = ['revue-deux-mondes-1841-q1.txt', 'revue-deux-mondes-1841-q2.txt',
         'revue-deux-mondes-1841-q3.txt', 'revue-deux-mondes-1841-q4.txt',
         'metternich-papiere-v4.txt', 'metternich-papiere-v6.txt',
         'talleyrand-memoires-v1.txt', 'pozzo-di-borgo-correspondance-v1.txt']
W = []
for fn in CORE + EXTRA:
    W += tok_elision(open(os.path.join(CORPUS, fn), encoding='utf-8', errors='replace').read())
NW = len(W)
fol = {}
pre = {}
for i in range(NW - 1):
    fol.setdefault(W[i], Counter())[W[i + 1]] += 1
for i in range(1, NW):
    pre.setdefault(W[i], Counter())[W[i - 1]] += 1

def rank_of(word, dist):
    vals = sorted(dist.values(), reverse=True)
    return vals.index(dist[word]) + 1

f_ce = fol.get('ce', Counter()); p_que = pre.get('que', Counter())
era = {
    'NW': NW,
    'f_ce_top': f_ce.most_common(10),
    'p_que_top': p_que.most_common(10),
    'rank_qui_in_f_ce': rank_of('qui', f_ce),
    'rank_que_in_f_ce': rank_of('que', f_ce),
    'rank_ce_in_p_que': rank_of('ce', p_que),
    'P_qui_given_ce': f_ce['qui'] / sum(f_ce.values()),
    'P_que_given_ce': f_ce['que'] / sum(f_ce.values()),
    'P_ce_given_pre_que': p_que['ce'] / sum(p_que.values()),
}
RIVALS = ['se', 'ne', 'le', 'je', 'on', 'en']
era['rivals'] = {r: {'P_qui': fol.get(r, Counter())['qui'] / max(1, sum(fol.get(r, Counter()).values())),
                     'n': sum(fol.get(r, Counter()).values())} for r in RIVALS}

# ---------------- GATE ----------------
lo, hi = cipher['wilson_64_given_87']
g1 = (all(era['rivals'][r]['P_qui'] == 0.0 for r in RIVALS)
      and era['rivals']['le']['n'] > 100
      and lo <= era['P_qui_given_ce'] <= hi)
g2 = cipher['n_f87_distinct'] >= 20 and cipher['n_p87_distinct'] >= 20
g3 = cipher['n_87_11'] >= 5
gate_legs = {'G1_qui_rival_kill': g1, 'G2_diversity': g2, 'G3_cela': g3}

q_a = cipher['k_64_given_87'] / n87 / era['P_qui_given_ce']
qui64 = ((1/3 <= q_a <= 3)
         and era['rank_qui_in_f_ce'] == 1
         and cipher['n_24_87_64'] >= 3)
gate = {'legs': gate_legs, 'n_hold': sum(gate_legs.values()),
        'qui64_holds': qui64,
        'P64_given_87': cipher['k_64_given_87'] / n87,
        'era_P_qui_given_ce': era['P_qui_given_ce'],
        'ratio': q_a}
gate['PROMOTES'] = gate['n_hold'] >= 2 and qui64

# ---------------- R1 / R2 ----------------
r1 = (cipher['rank_64_in_f87'] == 1 and cipher['rank_46_in_f87'] <= 3
      and era['rank_qui_in_f_ce'] == 1 and era['rank_que_in_f_ce'] <= 3)
p87_given_46 = cipher['k_87_given_46pre'] / n46
ratio_r2 = p87_given_46 / era['P_ce_given_pre_que']
r2 = (era['rank_ce_in_p_que'] <= 5 and cipher['rank_87_in_p46'] <= 5
      and 1/3 <= ratio_r2 <= 3)

out = {'cipher': cipher, 'era': era, 'gate': gate,
       'R1_follower': {'pass': r1,
                       'cipher_rank64': cipher['rank_64_in_f87'],
                       'cipher_rank46': cipher['rank_46_in_f87'],
                       'era_rank_qui': era['rank_qui_in_f_ce'],
                       'era_rank_que': era['rank_que_in_f_ce']},
       'R2_predecessor': {'pass': r2,
                          'era_rank_ce_in_pque': era['rank_ce_in_p_que'],
                          'cipher_rank87_in_p46': cipher['rank_87_in_p46'],
                          'P87_given_46': p87_given_46,
                          'era_P_ce_given_preque': era['P_ce_given_pre_que'],
                          'ratio': ratio_r2},
       'verdict_46': 'RE-DERIVED' if (gate['PROMOTES'] and r1 and r2)
                     else ('GATE-FAILED-ESCALATE' if not gate['PROMOTES'] else 'DEMOTE-single-gloss-GT')}
json.dump(out, open(os.path.join(HERE, 'ke2a_results.json'), 'w'), indent=1, default=str)
print(json.dumps({'gate': gate, 'R1': out['R1_follower'], 'R2': out['R2_predecessor'],
                  'verdict': out['verdict_46']}, indent=1, default=str))
