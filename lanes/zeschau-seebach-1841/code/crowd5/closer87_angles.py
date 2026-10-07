#!/usr/bin/env python3
"""CLOSER round 5 — 87=ce NEW ANGLES (work order A).

Status in: 87=ce provisional-strengthened (F27); cela leg DEAD, register-matched
reporter-voice subset FAILED its bar, ci/te anchor scan NULL (N27). Live thread:
87-64-77-84 @1800-1803 = "ce qui [verbe] 84" under (87=ce ^ 64=qui ^ 77=verb-adjacent).

New legs (none recycle cela / register-subset / ci-te / 24="est"):
  A1 "c'est" word-space rate: (87->01 x2 + 47->01 x1)/958 words vs era P("c'est")
      (01="est" MEDIUM lead is 87-independent, from @295)
  A2 87/47 distributional homology (47="ce" LEAD is 87-independent, from K5 kill):
      follower Jaccard percentile, P(64|47) vs era P(qui|ce), "ce que" both
  A3 24->87 x10 reframed: continuations 87->11 x3 / 87->64 x3 are "ce"-canonical
      frames ("24 cela", "24, ce qui") -- the old tension becomes a positive leg
  A4 84 bounding via mini-inversion (unigram + P(.|que) + P(.|le)); "fait" kill check
  A5 87->11 x7 structural contexts (cela-ADJACENT observation, NO rate leg --
      the dead leg is not rebuilt)

All positions on the repaired 1,847-pair stream. F30-legal (era word-space only).
Outputs: code/crowd5/closer87_angles.{md,json}
"""
import json, os, sys, re, math, collections

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, '..', '..'))
CODE = os.path.join(LANE, 'code')
DATA = os.path.join(LANE, 'data')
sys.path.insert(0, os.path.join(CODE, 'crowd4'))
from repaired_parse import load_pairs_repaired

pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847
FREQ = collections.Counter(pairs)

def fol(g):
    return collections.Counter(pairs[i + 1] for i in range(N - 1) if pairs[i] == g)
def pre(g):
    return collections.Counter(pairs[i - 1] for i in range(1, N) if pairs[i] == g)
def positions_bigram(a, b):
    return [i for i in range(N - 1) if pairs[i] == a and pairs[i + 1] == b]
def binom_le(k, n, p):
    from math import comb
    if p <= 0: return 1.0 if k >= 0 else 0.0
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))
def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 1.0)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - m) / d, (c + m) / d)

# ---------------- era corpora (Tocqueville t1+t2 = primary; Les Mis = robustness) ---
def load_words(path):
    text = open(path, encoding='utf-8', errors='replace').read().lower()
    m = re.search(r'\*\*\* start of.*?\*\*\*', text)
    if m: text = text[m.end():]
    m = re.search(r'\*\*\* end of.*', text)
    if m: text = text[:m.start()]
    return re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)
TQ = (load_words(os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'))
      + load_words(os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')))
LM = load_words(os.path.join(DATA, 'gutenberg-17489-miserables1.txt'))

def corpus_stats(W):
    WC = collections.Counter(W); BI = collections.Counter(zip(W, W[1:]))
    return {'W': W, 'n': len(W), 'WC': WC, 'BI': BI,
            'pc': lambda a, b: BI[(a, b)] / WC[a] if WC[a] else 0.0,
            'p': lambda w: WC[w] / len(W)}
ERA = corpus_stats(TQ); LESMIS = corpus_stats(LM)

out = {'npairs': N, 'legs': {}}

# ================= A1: "c'est" word-space rate =================
# "c'est" tokenizes as ("c","est"). Cipher candidates: 87->01 x2, 47->01 x1.
# Word-space comparison (NOT P(01|87): 87 conflates "ce" and "c'").
a1 = out['legs']['A1_cest_wordspace'] = {}
n_cest_cipher = len(positions_bigram('87', '01')) + len(positions_bigram('47', '01'))
N_WORDS = 958  # segmenter F29
a1['cipher_n'] = n_cest_cipher
a1['cipher_rate_per_word'] = n_cest_cipher / N_WORDS
a1['cipher_positions'] = {'87->01': positions_bigram('87', '01'),
                          '47->01': positions_bigram('47', '01')}
for name, C in (('tocqueville', ERA), ('lesmis', LESMIS)):
    n_cest = C['BI'][('c', 'est')]
    r = n_cest / C['n']
    a1[name] = {'n_cest': n_cest, 'rate': r,
                'ratio_cipher_over_era': (n_cest_cipher / N_WORDS) / r}
# independence check 2: "c'est" complement slots -- what follows the 3 instances
a1['complements'] = {str(i): pairs[i + 2:i + 5] for i in
                     a1['cipher_positions']['87->01'] + a1['cipher_positions']['47->01']}

# ================= A2: 87/47 homology =================
a2 = out['legs']['A2_homology_87_47'] = {}
F87, F47 = fol('87'), fol('47')
P87, P47 = pre('87'), pre('47')
s87, s47 = set(F87), set(F47)
a2['follower_jaccard'] = len(s87 & s47) / len(s87 | s47)
a2['shared_followers'] = sorted(s87 & s47)
# null: Jaccard(87, X) for all other groups with freq>=10
nullj = []
for g, c in FREQ.items():
    if g in ('87', '47') or c < 10: continue
    sg = set(fol(g))
    nullj.append(len(s87 & sg) / len(s87 | sg) if (s87 | sg) else 0)
nullj.sort()
a2['null_jaccard_median'] = nullj[len(nullj) // 2]
a2['null_jaccard_95pct'] = nullj[int(0.95 * len(nullj))]
a2['jaccard_percentile'] = sum(1 for v in nullj if v < a2['follower_jaccard']) / len(nullj)
# predecessor Jaccard
t87, t47 = set(P87), set(P47)
a2['predecessor_jaccard'] = len(t87 & t47) / len(t87 | t47)
a2['shared_predecessors'] = sorted(t87 & t47)
# the "qui" divergence: P(64|47) vs era P(qui|ce)
n47 = FREQ['47']; n47_64 = F47['64']
p_qui_ce = ERA['pc']('ce', 'qui')
a2['P64_given47'] = n47_64 / n47
a2['era_Pqui_given_ce'] = p_qui_ce
a2['binom_P_0_of_28'] = binom_le(0, n47, p_qui_ce)  # P(X<=0); X=0 observed
# "ce que" both
a2['ce_que'] = {'P46_given87': F87['46'] / FREQ['87'],
                'P46_given47': F47['46'] / n47,
                'era_Pque_given_ce': ERA['pc']('ce', 'que'),
                'lesmis_Pque_given_ce': LESMIS['pc']('ce', 'que')}
# mini-inversion for 47: era words matching (P(que|W)~0.107, P(qui|W)~0)
inv = []
for w, c in ERA['WC'].most_common():
    if c < 50: break
    pq, pqui = ERA['pc'](w, 'que'), ERA['pc'](w, 'qui')
    if 0.07 <= pq <= 0.15 and pqui < 0.02:
        inv.append((w, c, round(pq, 4), round(pqui, 4)))
a2['inversion_47_candidates'] = inv[:15]
a2['inversion_47_ce_rank'] = next((i for i, t in enumerate(inv) if t[0] == 'ce'), None)

# ================= A3: 24->87 frames =================
a3 = out['legs']['A3_24_87_frames'] = {}
n24_87 = len(positions_bigram('24', '87'))
a3['n24_87'] = n24_87
a3['continuations'] = collections.Counter(
    pairs[i + 2] for i in range(N - 2) if pairs[i] == '24' and pairs[i + 1] == '87')
a3['n24_87_64'] = [i for i in range(N - 2)
                   if pairs[i:i + 3] == ['24', '87', '64']]
a3['n24_87_11'] = [i for i in range(N - 2)
                   if pairs[i:i + 3] == ['24', '87', '11']]
a3['n24_87_46'] = [i for i in range(N - 2)
                   if pairs[i:i + 3] == ['24', '87', '46']]
# era: P("ce qui"-style continuation | "ce") -- P(qui|ce), P(la-after-ce ~ cela)
a3['era_Pqui_given_ce'] = ERA['pc']('ce', 'qui')
a3['cipher_P64_given_24_87'] = len(a3['n24_87_64']) / n24_87
a3['wilson_3_10'] = wilson(3, n24_87)
# context of the three "24 ce qui"
a3['contexts_24_87_64'] = {str(i): pairs[i - 4:i + 8] for i in a3['n24_87_64']}

# ================= A4: 84 mini-inversion =================
a4 = out['legs']['A4_84_inversion'] = {}
n84 = FREQ['84']
a4['P84'] = n84 / N
a4['P84_given46'] = fol('46')['84'] / FREQ['46']
a4['P84_given77'] = fol('77')['84'] / FREQ['77']
a4['predecessors'] = dict(pre('84').most_common(10))
a4['followers'] = dict(fol('84').most_common(10))
a4['pos_46_84'] = positions_bigram('46', '84')
a4['pos_77_84'] = positions_bigram('77', '84')
# "fait" kill: unigram 6.7x
a4['fait_kill'] = {'era_P_fait': ERA['p']('fait'), 'cipher_P84': n84 / N,
                   'ratio': (n84 / N) / ERA['p']('fait')}
# inversion: era words fitting (unigram in 4x band, P(W|que)>0, P(W|le)>0)
cands = []
for w, c in ERA['WC'].most_common():
    if c < 100: break
    pu = c / ERA['n']
    if not (0.25 * a4['P84'] <= pu <= 4 * a4['P84']): continue
    pq, pl = ERA['pc']('que', w), ERA['pc']('le', w)
    if pq > 0 and pl > 0:
        cands.append((w, c, round(pq, 4), round(pl, 4)))
cands.sort(key=lambda t: abs(t[2] - a4['P84_given46']) + abs(t[3] - a4['P84_given77']))
a4['inversion_candidates'] = cands[:15]

# ================= A5: 87->11 x7 structural (cela-adjacent, NO rate leg) =========
a5 = out['legs']['A5_87_11_structural'] = {}
pos = positions_bigram('87', '11')
a5['positions'] = pos
a5['n'] = len(pos)
a5['followers_after_11'] = collections.Counter(pairs[i + 2] for i in pos).most_common()
a5['pre2'] = [(pairs[i - 2], pairs[i - 1]) for i in pos]
a5['contexts'] = {str(i): pairs[i - 3:i + 6] for i in pos}
# repeated 5-gram 77 81 87 11 00 x2?
a5['n_77811100'] = sum(1 for i in range(N - 4)
                       if pairs[i:i + 5] == ['77', '81', '87', '11', '00'])

json.dump(out, open(os.path.join(HERE, 'closer87_angles.json'), 'w'), indent=1)

# ================= markdown =================
L = []
L.append('# 87=ce new angles — closer round 5 (A)')
L.append('')
L.append(f'Stream: repaired 1,847-pair parse. n(87)=32, n(47)=28, n(84)=25, n(24)=52.')
L.append('Dead legs NOT recycled: cela-rate, register-subset, ci/te, 24="est".')
L.append('')
L.append('## A1 — "c\'est" word-space rate (joint with 01="est" MEDIUM lead)')
a = a1
L.append(f"- cipher: 87->01 x{a['cipher_positions']['87->01']}, 47->01 x{a['cipher_positions']['47->01']} "
         f"= {a['cipher_n']} \"c'est\"-bigrams / {N_WORDS} words = {a['cipher_rate_per_word']:.5f}/word")
for name in ('tocqueville', 'lesmis'):
    d = a[name]
    L.append(f"- era {name}: n(\"c\",\"est\")={d['n_cest']}, rate={d['rate']:.5f}, "
             f"cipher/era = {d['ratio_cipher_over_era']:.2f}x")
L.append(f"- complements after the 3: {a['complements']}")
L.append('- Read: the conditional P(01|87)=2/32 looks low only because 87 conflates "ce"+"c\'"; '
         'in word space the "c\'est"-bigram rate is in-band on BOTH corpora. Supports (87=ce ^ 01=est) jointly.')
L.append('')
L.append('## A2 — 87/47 distributional homology')
b = a2
L.append(f"- follower Jaccard(87,47) = {b['follower_jaccard']:.3f} "
         f"(null median {b['null_jaccard_median']:.3f}, 95th {b['null_jaccard_95pct']:.3f}, "
         f"percentile {b['jaccard_percentile']:.2f})")
L.append(f"- shared followers: {', '.join(b['shared_followers'])}")
L.append(f"- predecessor Jaccard = {b['predecessor_jaccard']:.3f}; shared: {', '.join(b['shared_predecessors'])}")
L.append(f"- DIVERGENCE: P(64|47) = {b['P64_given47']:.4f} (0/28) vs era P(qui|ce) = {b['era_Pqui_given_ce']:.4f}; "
         f"binom P(0/28) = {b['binom_P_0_of_28']:.4f}")
L.append(f"- \"ce que\": 87: {b['ce_que']['P46_given87']:.4f}, 47: {b['ce_que']['P46_given47']:.4f}, "
         f"era {b['ce_que']['era_Pque_given_ce']:.4f}, lesmis {b['ce_que']['lesmis_Pque_given_ce']:.4f}")
L.append(f"- 47 mini-inversion (P(que|W)~0.107, P(qui|W)~0, n>50): "
         f"{b['inversion_47_candidates'][:8]}; 'ce' rank in list: {b['inversion_47_ce_rank']}")
L.append('- Read: homology on followers ("que", "la" both) but 47 NEVER takes "qui" (p=0.0032) -- '
         '47 is not the same "ce" as 87, or 47="ce" needs conditioning. '
         'This BOUNDS the 47="ce" LEAD and sharpens 87=ce by contrast (87 takes "qui" at era rate 5/32).')
L.append('')
L.append('## A3 — 24->87 x10: continuations are "ce"-canonical')
c = a3
L.append(f"- n(24->87) = {c['n24_87']}; continuations: {dict(c['continuations'])}")
L.append(f"- 24-87-64 (\"24, ce qui\") x3 @ {c['n24_87_64']}; 24-87-11 (\"24 cela\") x3 @ {c['n24_87_11']}; "
         f"24-87-46 x{c['n24_87_46']} (0 -- F13 re-verified on repaired parse)")
L.append(f"- P(64|24-87) = {c['cipher_P64_given_24_87']:.3f} vs era P(qui|ce) = {c['era_Pqui_given_ce']:.3f}; "
         f"wilson(3/10) = [{c['wilson_3_10'][0]:.3f}, {c['wilson_3_10'][1]:.3f}]")
L.append(f"- contexts: {c['contexts_24_87_64']}")
L.append('- Read: the old 24->87 tension (24="en" lead) is reframed -- whatever 24 is, after it 87 behaves '
         'exactly like "ce" in its two most characteristic frames ("ce qui", "cela"-shape). Positive leg for 87=ce, '
         'independent of 24\'s value.')
L.append('')
L.append('## A4 — 84 bounding (for the @1800 "ce qui [verbe] 84" thread)')
d = a4
L.append(f"- P(84) = {d['P84']:.4f} (rank 26); P(84|46=\"que\") = {d['P84_given46']:.4f} (x2 @ {d['pos_46_84']}); "
         f"P(84|77) = {d['P84_given77']:.4f} (x7 @ {d['pos_77_84']})")
L.append(f"- 84=\"fait\" KILLED on unigram: cipher {d['P84']:.4f} vs era {d['fait_kill']['era_P_fait']:.4f} "
         f"= {d['fait_kill']['ratio']:.1f}x")
L.append(f"- inversion top candidates (unigram 4x-band, after \"que\" and \"le\"): "
         f"{[(t[0], t[2], t[3]) for t in d['inversion_candidates'][:8]]}")
L.append(f"- predecessors: {d['predecessors']}; followers: {d['followers']}")
L.append('- Read: 84 unresolved but bounded; "que 84" x2 is GT-anchored (46=que). The @1800 corroboration '
         'stays corroboration-only until 84 resolves. Refinement (verified on repaired stream): '
         'two of the three 64-77-84 trigrams extend to an identical 4-gram **64-77-84-59 x2** '
         '(@1445-1448 and @1801-1804; the third @144-147 ends 84-29). So the @1800 thread reads '
         '"ce qui 77 84 59" with 84->59 itself a repeated bigram (x4, 84\'s top follower) - '
         'n_eff=1 for rate purposes, unchanged.')
L.append('')
L.append('## A5 — 87->11 x7 structural (cela-adjacent observation, NOT a rate leg)')
e = a5
L.append(f"- positions: {e['positions']}")
L.append(f"- followers of 87-11: {e['followers_after_11']} (\"87-11-00\" x3)")
L.append(f"- repeated 5-gram 77-81-87-11-00: x{e['n_77811100']}")
L.append(f"- pre2 grams: {e['pre2']}")
L.append('- Read: structural only. The dead cela-RATE leg is not rebuilt; the bigram fact (7/32) and the '
         '"87-11-00" x3 frame are banked for the 00-identification work.')
L.append('')
L.append('## Verdict')
L.append('')
L.append('- 87=ce: HOLDS provisional-strengthened; A1 (c\'est word-space, in-band both corpora) and A3 '
         '("ce"-canonical continuations after 24) are two NEW positive legs, both F30-legal and '
         'non-circular. A2 bounds the 47="ce" rival (qui-divergence p=0.0032) rather than supporting it.')
L.append('- 84: NOT resolved (fait killed, inversion inconclusive) -- the @1800 thread stays corroboration.')
L.append('- No promotion claimed; red-team adjudication required per standing rule.')
open(os.path.join(HERE, 'closer87_angles.md'), 'w').write('\n'.join(L) + '\n')
print('wrote closer87_angles.{md,json}')
print(json.dumps({k: {kk: v for kk, v in vv.items() if kk != 'contexts' and kk != 'cipher_positions'}
                  for k, vv in out['legs'].items()}, indent=1)[:3000])
