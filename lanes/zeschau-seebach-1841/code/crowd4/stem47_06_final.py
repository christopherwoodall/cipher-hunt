"""Round-4 STEM HUNTER final numbers: 47 battery (raw ratios) + 06 stem profile.

Re-derives every number from data/upstream-ct_R5005.txt + upstream-offsets.json
(R5005 only). Era: Tocqueville t1+t2, WORD-SPACE legs only (F30).
Raw ratios: cipher_P / era_P (unsmoothed); era n<5 flagged weak.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import syllabary4 as S
from syllabary4 import load_pairs, followers, predecessors, ngram_count

pairs = load_pairs()
N = len(pairs)
S._era_init()
U, B, E = S._ERA_U, S._ERA_B, S._ERA_END
Nw = len(S._ERA)


def P2(w2, w1):
    t = sum(B[w1].values())
    return B[w1][w2] / t if t else 0.0


def Pend(w, end):
    t = sum(E[end].values())
    return E[end][w] / t if t else 0.0


out = {'N_pairs': N, 'N_era_words': Nw}

# ---------------- 47 ----------------
n47 = pairs.count('47')
F47, P47 = followers(pairs, '47'), predecessors(pairs, '47')
out['47'] = {
    'n': n47,
    'windows': [[i, pairs[max(0, i - 3):i + 4]] for i, g in enumerate(pairs) if g == '47'],
    'followers': dict(F47), 'predecessors': dict(P47),
    'c96_47': ngram_count(pairs, ['96', '47']),
    'c47_78': ngram_count(pairs, ['47', '78']),
    'c37_78': ngram_count(pairs, ['37', '78']),
    'c96_87_46': ngram_count(pairs, ['96', '87', '46']),
    'c96_47_46': ngram_count(pairs, ['96', '47', '46']),
    'c87_11': ngram_count(pairs, ['87', '11']),
    'c47_11': ngram_count(pairs, ['47', '11']),
}
# 802x recompute (word-space)
n96 = pairs.count('96')
c96_21 = ngram_count(pairs, ['96', '21'])
out['47']['x802_recompute'] = {
    'n96': n96, 'c96_21': c96_21,
    'cipher_P21_given_96': c96_21 / n96,
    'cipher_P47_given_96': out['47']['c96_47'] / n96,
    'era_P_me_given_par': P2('me', 'par'),
    'era_n_par_me': B['par']['me'],
    'era_n_par_ce': B['par']['ce'],
    'ratio_96_21_as_par_me': (c96_21 / n96) / P2('me', 'par') if P2('me', 'par') else None,
    'ratio_96_47_as_par_me': (out['47']['c96_47'] / n96) / P2('me', 'par') if P2('me', 'par') else None,
}
# candidate battery, RAW
cands = ['me', 'mes', 'met', 'mais', 'ce', 'le', 'les', 'en', 'ne', 'se',
         'même', 'dans', 'plus', 'bien', 'tout', 'on', 'il', 'elle', 'nous',
         'vous', 'lui', 'leur', 'y', 'de', 'est', 'sont', 'fait', 'dit', 'pas']
bat = []
for w in cands:
    eu = U[w] / Nw
    bat.append({
        'w': w,
        'A_uni': (n47 / N) / eu if eu else None,
        'B1_que': (F47['46'] / n47) / P2('que', w) if P2('que', w) else None,
        'B2_la': (F47['11'] / n47) / P2('la', w) if P2('la', w) else None,
        'B3_me': (F47['78'] / n47) / P2('me', w) if P2('me', w) else None,
        'C1_w_given_par': (P47['96'] / n47) / P2(w, 'par') if P2(w, 'par') else None,
        'C2_w_after_erv': (P47['29'] / n47) / Pend(w, 'er') if Pend(w, 'er') else None,
        'era_n': U[w],
    })
out['47']['battery_raw'] = bat
out['47']['era_P_que_given_ce'] = P2('que', 'ce')
out['47']['era_n_ce_que'] = B['ce']['que']
out['47']['era_n_ce'] = U['ce']

# ---------------- 06 ----------------
n06 = pairs.count('06')
F06, P06 = followers(pairs, '06'), predecessors(pairs, '06')
w0629 = [i for i in range(N - 1) if pairs[i] == '06' and pairs[i + 1] == '29']
w0611 = [i for i in range(N - 1) if pairs[i] == '06' and pairs[i + 1] == '11']
w0600 = [i for i in range(N - 1) if pairs[i] == '06' and pairs[i + 1] == '00']
w0677 = [i for i in range(N - 1) if pairs[i] == '06' and pairs[i + 1] == '77']
w8206 = [i for i in range(N - 2) if pairs[i] == '82' and pairs[i + 1] == '06']
out['06'] = {
    'n': n06,
    'windows': [[i, pairs[max(0, i - 2):i + 3]] for i, g in enumerate(pairs) if g == '06'],
    'followers': dict(F06), 'predecessors': dict(P06),
    'f06_29': {'pos': w0629,
               'ctx': [[i, pairs[i - 4:i + 5]] for i in w0629]},
    'f06_11': {'pos': w0611, 'ctx': [[i, pairs[i - 4:i + 5]] for i in w0611]},
    'f06_00': {'pos': w0600}, 'f06_77': {'pos': w0677},
    'f82_06': {'pos': w8206},
    'c06_29_40': ngram_count(pairs, ['06', '29', '40']),
    'c06_40': F06['40'],
    'c70_06': P06['70'],
}
# 86 second stem
n86 = pairs.count('86')
F86, P86 = followers(pairs, '86'), predecessors(pairs, '86')
out['86'] = {
    'n': n86, 'followers': dict(F86), 'predecessors': dict(P86),
    'c00_86': P86['00'], 'c00_06': P06['00'],
    'c86_29': F86['29'],
    'c67_86_29': ngram_count(pairs, ['67', '86', '29']),
    'c06_29_67_86': ngram_count(pairs, ['06', '29', '67', '86']),
}
# era stem frequencies (all word-forms with stem prefix, per 1000 words)
stems = ['demand', 'command', 'parl', 'donn', 'port', 'charg', 'assur',
         'trouv', 'pass', 'pri', 'rest', 'pens', 'mont']
out['era_stem_rates'] = {s: round(sum(n for w, n in U.items()
                                      if w.startswith(s)) / Nw * 1000, 3)
                         for s in stems}

fn = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   'stem47_06_results.json')
json.dump(out, open(fn, 'w'), indent=1, ensure_ascii=False)
print('wrote', fn)
print('47 battery (raw) head:')
for r in bat[:12]:
    print('  %(w)6s A=%(A_uni).2f B1=%(B1_que)s B2=%(B2_la)s C1=%(C1_w_given_par)s C2=%(C2_w_after_erv)s' % {
        'w': r['w'], 'A_uni': r['A_uni'] or -1,
        'B1_que': round(r['B1_que'], 2) if r['B1_que'] else None,
        'B2_la': round(r['B2_la'], 2) if r['B2_la'] else None,
        'C1_w_given_par': round(r['C1_w_given_par'], 2) if r['C1_w_given_par'] else None,
        'C2_w_after_erv': round(r['C2_w_after_erv'], 2) if r['C2_w_after_erv'] else None})
