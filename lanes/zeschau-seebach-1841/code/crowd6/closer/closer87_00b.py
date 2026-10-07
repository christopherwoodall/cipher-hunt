#!/usr/bin/env python3
"""Round-6 CLOSER part 2: E-legs for 84="en", S-legs for 59="est".

Merges into code/crowd6/closer/closer87_00_results.json under
work_orders['WO-A_84']['legs_E'] and work_orders['WO-A_59est'].
All cipher numbers re-derived on the repaired 1,847-pair parse.
Era: Tocqueville t1+t2 elision-split word model (round-5 convention).
"""

import collections, json, os, re, sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
DATA = os.path.join(LANE, 'data')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847
cf = collections.Counter(pairs)
cbi = collections.Counter(zip(pairs, pairs[1:]))


def load_era():
    words = []
    for fn in ('gutenberg-30513-tocqueville-t1.txt',
               'gutenberg-30514-tocqueville-t2.txt'):
        txt = open(os.path.join(DATA, fn), encoding='utf-8').read().lower()
        txt = txt.replace('\u2019', "'").replace('\u2018', "'")
        txt = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])",
                     r'\1 \2', txt)
        words += re.findall(r'[a-z\u00e0-\u00ff]+', txt)
    return words


words = load_era()
wu = collections.Counter(words)
wN = len(words)
we = collections.defaultdict(collections.Counter)
for a, b in zip(words, words[1:]):
    we[a][b] += 1

E = {}
# E1 unigram
E['E1_unigram'] = {'cipher_P84': cf['84'] / N, 'era_Pen': wu['en'] / wN,
                   'ratio': (cf['84'] / N) / (wu['en'] / wN)}
# E2 qu'en: cipher 46->84 unelided <-> era qu->en elided
E['E2_quen'] = {'cipher_n': cbi[('46', '84')], 'cipher_P': cbi[('46', '84')] / cf['46'],
                'era_n': we['qu']['en'], 'era_P': we['qu']['en'] / wu['qu'],
                'ratio': (cbi[('46', '84')] / cf['46']) / (we['qu']['en'] / wu['qu'])}
# E3 n'en: cipher 94->84 <-> era n->en
E['E3_nen'] = {'cipher_n': cbi[('94', '84')],
               'era_n': we['n']['en'], 'era_P': we['n']['en'] / wu['n']}
# E4 l'en: cipher 77->84 (77="le" provisional) <-> era l->en
E['E4_len'] = {'cipher_n': cbi[('77', '84')], 'cipher_P': cbi[('77', '84')] / cf['77'],
               'era_n': we['l']['en'], 'era_P': we['l']['en'] / wu['l'],
               'ratio': (cbi[('77', '84')] / cf['77']) / (we['l']['en'] / wu['l'])}
# E4' s'en alternative (for the 77-side; NOT claimed here)
E['E4prime_sen'] = {'era_n': we['s']['en'], 'era_P': we['s']['en'] / wu['s'],
                    'ratio_vs_cipher': (cbi[('77', '84')] / cf['77']) / (we['s']['en'] / wu['s']),
                    'note': '77-side alternative only; touches promoted 77="le"'}
# E5 m'en: cipher 82->84 (82=m GT) <-> era m->en
E['E5_men'] = {'cipher_n': cbi[('82', '84')],
               'era_n': we['m']['en'], 'era_P': we['m']['en'] / wu['m']}
# E6 qui l'en
n_qle = sum(1 for i in range(len(words) - 2)
            if words[i] == 'qui' and words[i + 1] == 'l' and words[i + 2] == 'en')
E['E6_qui_len'] = {'cipher_n': 3, 'cipher_n_eff': 1,
                   'era_n': n_qle}
# rival plus: P(84|77) vs era P(plus|le)
E['rival_plus'] = {'cipher_P84g77': cbi[('77', '84')] / cf['77'],
                   'era_Pplusgle': we['le']['plus'] / wu['le'],
                   'ratio': (cbi[('77', '84')] / cf['77']) / (we['le']['plus'] / wu['le']),
                   'plus_est_era': sum(1 for i in range(len(words) - 1)
                                       if words[i] == 'plus' and words[i + 1] == 'est')}
# rival a: unigram + "a est" grammar
E['rival_a'] = {'unigram_ratio': (cf['84'] / N) / (wu['a'] / wN)}
# rival y
E['rival_y'] = {'unigram_ratio': (cf['84'] / N) / (wu['y'] / wN),
                'era_Pygll': we['l']['y'] / wu['l']}

S = {}
n59 = cf['59']
S['n59'] = n59
S['S1_unigram'] = {'cipher_P59': n59 / N, 'era_Pest': wu['est'] / wN,
                   'ratio': (n59 / N) / (wu['est'] / wN)}
S['S2_qui_est'] = {'cipher_n': cbi[('64', '59')], 'era_n': we['qui']['est']}
S['S3_nest'] = {'cipher_n': cbi[('94', '59')],
                'era_n': we['n']['est'], 'era_P': we['n']['est'] / wu['n']}
S['S4_est_que'] = {'cipher_n': cbi[('59', '46')], 'cipher_P': cbi[('59', '46')] / n59,
                   'era_P': we['est']['que'] / wu['est'],
                   'ratio': (cbi[('59', '46')] / n59) / (we['est']['que'] / wu['est'])}
S['S4_positions'] = [i for i in range(N - 1)
                     if pairs[i] == '59' and pairs[i + 1] == '46']
S['rivals_rate'] = {w0: {'era_P': wu[w0] / wN,
                         'ratio': (n59 / N) / (wu[w0] / wN)}
                    for w0 in ('doute', 'dit', 'fait', 'veut', 'peut', 'doit')}
S['pos_87_59'] = [i for i in range(N - 1)
                  if pairs[i] == '87' and pairs[i + 1] == '59']
S['pred59'] = dict(collections.Counter(
    pairs[i - 1] for i in range(1, N) if pairs[i] == '59').most_common())
S['foll59'] = dict(collections.Counter(
    pairs[i + 1] for i in range(N - 1) if pairs[i] == '59').most_common())

p = os.path.join(LANE, 'code', 'crowd6', 'closer', 'closer87_00_results.json')
R = json.load(open(p))
R['work_orders']['WO-A_84']['legs_E'] = E
R['work_orders']['WO-A_59est'] = S
json.dump(R, open(p, 'w'), indent=1, ensure_ascii=False)
print('merged E/S legs into JSON')
print('E1 ratio=%.2f E2 ratio=%.2f E4 ratio=%.1f' % (
    E['E1_unigram']['ratio'], E['E2_quen']['ratio'], E['E4_len']['ratio']))
print('S1 ratio=%.2f S4 ratio=%.2f' % (S['S1_unigram']['ratio'], S['S4_est_que']['ratio']))
