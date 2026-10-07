#!/usr/bin/env python3
"""
THE CLOSER — resolve crib-surgeon H1: 24 = "est".

Job: CONFIRM or REFUTE 24="est", re-validating every rate check against the
ERA-MATCHED corpus (Tocqueville 1835/1840, formal prose — NOT Les Miserables),
score named rivals ("c'est", "sont", "ont") plus one of my own ("de",
demanded by the rank-1 frequency), and recompute the 24-87-46 joint
contradiction under era rates.

Lane bar: >=2 INDEPENDENT checks to promote; a grammatical contradiction
refutes. Independence here: A=unigram, B=follower bigram, C=predecessor
bigram, D=trigram que-rate, E=negative-control bigram — five different
n-gram slots, no shared counts.

Deterministic. No invented ciphertext. Results -> closer_results.json/.md
"""
import json, re, collections, os, sys, math

HERE = os.path.dirname(os.path.abspath(__file__))          # code/crowd2
CODE = os.path.dirname(HERE)                               # code
LANE = os.path.dirname(CODE)                               # lane root
DATA = os.path.join(LANE, 'data')
sys.path.insert(0, CODE)
from crib_attack import load_pairs

T1 = os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt')
T2 = os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')

res = {'meta': {'worker': 'closer', 'target': '24="est" (crib-surgeon H1)',
                'corpus': 'tocqueville-1835-1840 (era-matched, formal prose)'}}

# ============================ CIPHER SIDE ============================
pairs, _, _ = load_pairs()
N = len(pairs)
freq = collections.Counter(pairs)
ranked = sorted(freq.items(), key=lambda kv: -kv[1])
rank_of = {g: i + 1 for i, (g, _) in enumerate(ranked)}   # 1-based

def bi(a, b):
    return sum(1 for x, y in zip(pairs, pairs[1:]) if x == a and y == b)

def tri(a, b, c):
    return sum(1 for x, y, z in zip(pairs, pairs[1:], pairs[2:])
               if x == a and y == b and z == c)

def quad(a, b, c, d):
    return sum(1 for w, x, y, z in zip(pairs, pairs[1:], pairs[2:], pairs[3:])
               if (w, x, y, z) == (a, b, c, d))

def followers(g):
    return collections.Counter(pairs[i + 1] for i, gg in enumerate(pairs[:-1]) if gg == g)

def predecessors(g):
    return collections.Counter(pairs[i - 1] for i, gg in enumerate(pairs) if gg == g and i > 0)

def fol_of_bigram(a, b):
    return collections.Counter(pairs[i + 2] for i in range(N - 2)
                               if pairs[i] == a and pairs[i + 1] == b)

def positions_of(seq):
    L = len(seq)
    return [i for i in range(N - L + 1) if pairs[i:i + L] == seq]

def context(i, L, w=3):
    return pairs[max(0, i - w):i + L + w]

n24, n87, n46 = freq['24'], freq['87'], freq['46']
c = res['cipher'] = {
    'n_pairs': N,
    'freq_24': n24, 'rank_24': rank_of['24'], 'share_24': round(n24 / N, 5),
    'freq_87': n87, 'freq_46': n46,
    'top12_groups': [(g, f) for g, f in ranked[:12]],
    # check B
    'n_24_87': bi('24', '87'),
    'p_87_given_24': round(bi('24', '87') / n24, 4),
    'p_87_base': round(n87 / N, 5),
    # check C
    'n_46_24': bi('46', '24'),
    'p_24_given_46': round(bi('46', '24') / n46, 4),
    # check D / joint contradiction
    'n_24_87_46': tri('24', '87', '46'),
    'p_46_given_87_pre24': round(tri('24', '87', '46') / bi('24', '87'), 4),
    'n_96_87_46': tri('96', '87', '46'),
    'p_46_given_87_pre96': round(tri('96', '87', '46') / bi('96', '87'), 4),
    # anomaly "est cela"
    'n_24_87_11': tri('24', '87', '11'),
    'pos_24_87_11': positions_of(['24', '87', '11']),
    # 24-87-64
    'n_24_87_64': tri('24', '87', '64'),
    'pos_24_87_64': positions_of(['24', '87', '64']),
    # check E negative control
    'n_24_46': bi('24', '46'),
    'p_46_given_24': round(bi('24', '46') / n24, 4),
    # S1: is 46-24 followed by 87-64? ("qu'est-ce qui")
    'pos_46_24': positions_of(['46', '24']),
    'n_46_24_87_64': quad('46', '24', '87', '64'),
    'n_46_24_87': tri('46', '24', '87'),   # "qu'est-ce": era 7/7, cipher ?
    # predecessor "la"->24 under homophony readings
    'n_11_24': bi('11', '24'),
    'pos_11_24': positions_of(['11', '24']),
    # profiles
    'followers_24_87': fol_of_bigram('24', '87').most_common(),
    'followers_24_top10': followers('24').most_common(10),
    'n_followers_24': len(followers('24')),
    'predecessors_24_top10': predecessors('24').most_common(10),
    'n_predecessors_24': len(predecessors('24')),
}
c['ctx_24_87_11'] = [context(i, 3) for i in c['pos_24_87_11']]
c['ctx_24_87_64'] = [context(i, 3) for i in c['pos_24_87_64']]
c['ctx_46_24'] = [context(i, 2) for i in c['pos_46_24']]

print("[C] 24: freq=%d rank=%d share=%.4f" % (n24, rank_of['24'], n24 / N))
print("[C] P(87|24)=%.4f (n=%d) base P(87)=%.5f | P(24|46)=%.4f (n=%d)"
      % (c['p_87_given_24'], c['n_24_87'], c['p_87_base'], c['p_24_given_46'], c['n_46_24']))
print("[C] 24-87-46=%d  24-87-11=%d  24-87-64=%d  24-46=%d  46-24-87-64=%d"
      % (c['n_24_87_46'], c['n_24_87_11'], c['n_24_87_64'], c['n_24_46'], c['n_46_24_87_64']))
print("[C] followers of 24-87: %s" % c['followers_24_87'])
print("[C] followers of 24 (top10): %s  distinct=%d" % (c['followers_24_top10'], c['n_followers_24']))
print("[C] predecessors of 24 (top10): %s  distinct=%d" % (c['predecessors_24_top10'], c['n_predecessors_24']))

# ============================ ERA SIDE ============================
def load_words(path):
    text = open(path, encoding='utf-8', errors='replace').read().lower()
    m = re.search(r'\*\*\* start of.*?\*\*\*', text)
    if m:
        text = text[m.end():]
    m = re.search(r'\*\*\* end of.*', text)
    if m:
        text = text[:m.start()]
    return re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)

words = load_words(T1) + load_words(T2)
NW = len(words)
wc = collections.Counter(words)
wrank = {w: i + 1 for i, (w, _) in enumerate(wc.most_common())}  # 1-based

def e1(w):
    return wc[w]

def e2(a, b):
    return sum(1 for x, y in zip(words, words[1:]) if x == a and y == b)

def e3(a, b, dd):
    return sum(1 for x, y, z in zip(words, words[1:], words[2:])
               if x == a and y == b and z == dd)

def e4(a, b, dd, e):
    return sum(1 for w, x, y, z in zip(words, words[1:], words[2:], words[3:])
               if (w, x, y, z) == (a, b, dd, e))

def efol2(a, b, k=12):
    return collections.Counter(z for x, y, z in zip(words, words[1:], words[2:])
                               if x == a and y == b).most_common(k)

def epre(w, k=10):
    return collections.Counter(x for x, y in zip(words, words[1:]) if y == w).most_common(k)

def efol(w, k=10):
    return collections.Counter(y for x, y in zip(words, words[1:]) if x == w).most_common(k)

# "c'est" is tokenized by load_words as c + est (apostrophe splits).
n_cest = e2('c', 'est')                      # pseudo-count of "c'est"
era = res['era'] = {
    'n_words': NW,
    'rank_est': wrank.get('est'), 'share_est': round(e1('est') / NW, 5),
    'rank_de': wrank.get('de'), 'share_de': round(e1('de') / NW, 5),
    'rank_sont': wrank.get('sont'), 'share_sont': round(e1('sont') / NW, 6),
    'rank_ont': wrank.get('ont'), 'share_ont': round(e1('ont') / NW, 6),
    'n_cest_pseudo': n_cest, 'share_cest': round(n_cest / NW, 6),
    # check B rates: P(ce | V)
    'p_ce_given_est': round(e2('est', 'ce') / e1('est'), 4),
    'n_est_ce': e2('est', 'ce'), 'n_est': e1('est'),
    'p_ce_given_de': round(e2('de', 'ce') / e1('de'), 4),
    'n_de_ce': e2('de', 'ce'),
    'p_ce_given_cest': round(e3('c', 'est', 'ce') / n_cest, 4) if n_cest else None,
    'n_cest_ce': e3('c', 'est', 'ce'),
    'p_ce_given_sont': round(e2('sont', 'ce') / e1('sont'), 5) if e1('sont') else None,
    'n_sont_ce': e2('sont', 'ce'),
    'p_ce_given_ont': round(e2('ont', 'ce') / e1('ont'), 5) if e1('ont') else None,
    'n_ont_ce': e2('ont', 'ce'),
    # check C rates: P(V | que/qu)
    'p_est_given_quequ': round((e2('que', 'est') + e2('qu', 'est')) / (e1('que') + e1('qu')), 4),
    'n_quequ_est': e2('que', 'est') + e2('qu', 'est'),
    'p_de_given_que': round(e2('que', 'de') / e1('que'), 4),
    'p_cest_given_que': round(e3('que', 'c', 'est') / e1('que'), 5),
    'n_que_cest': e3('que', 'c', 'est'),
    'p_sont_given_que': round(e2('que', 'sont') / e1('que'), 5),
    'p_ont_given_quequ': round((e2('que', 'ont') + e2('qu', 'ont')) / (e1('que') + e1('qu')), 5),
    # check D rates: P(que | V, ce)
    'p_que_given_est_ce': round(e3('est', 'ce', 'que') / e2('est', 'ce'), 4) if e2('est', 'ce') else None,
    'n_est_ce_que': e3('est', 'ce', 'que'),
    'p_que_given_de_ce': round(e3('de', 'ce', 'que') / e2('de', 'ce'), 4) if e2('de', 'ce') else None,
    'n_de_ce_que': e3('de', 'ce', 'que'),
    'p_que_given_cest_ce': (round(e4('c', 'est', 'ce', 'que') / e3('c', 'est', 'ce'), 4)
                            if e3('c', 'est', 'ce') else None),
    'n_cest_ce_que': e4('c', 'est', 'ce', 'que'),
    # check E rates: P(que | V) negative control
    'p_que_given_est': round(e2('est', 'que') / e1('est'), 5),
    'n_est_que': e2('est', 'que'),
    'p_que_given_de': round(e2('de', 'que') / e1('de'), 5),
    'n_de_que': e2('de', 'que'),
    'p_que_given_cest': (round(e3('c', 'est', 'que') / n_cest, 4) if n_cest else None),
    'n_cest_que': e3('c', 'est', 'que'),
    # S2: follower profiles of "V ce"
    'fol_est_ce': efol2('est', 'ce'),
    'fol_de_ce': efol2('de', 'ce'),
    'fol_cest_ce': collections.Counter(
        z for w, x, y, z in zip(words, words[1:], words[2:], words[3:])
        if (w, x, y) == ('c', 'est', 'ce')).most_common(12),
    'pre_est': epre('est'), 'fol_est': efol('est'),
    'pre_de': epre('de'),
    # "est cela" anomaly: la vs là after "est ce"
    'n_est_ce_la': e3('est', 'ce', 'la'), 'n_est_ce_là': e3('est', 'ce', 'là'),
    # "en" rival (formula-hunter's "[pour|en] ce qui" for 24-87-64)
    'rank_en': wrank.get('en'), 'share_en': round(e1('en') / NW, 5),
    'n_en': e1('en'),
    'p_ce_given_en': round(e2('en', 'ce') / e1('en'), 4),
    'n_en_ce': e2('en', 'ce'),
    'p_en_given_quequ': round((e2('que', 'en') + e2('qu', 'en')) / (e1('que') + e1('qu')), 4),
    'n_quequ_en': e2('que', 'en') + e2('qu', 'en'),
    'n_qu_en': e2('qu', 'en'),
    'p_que_given_en_ce': round(e3('en', 'ce', 'que') / e2('en', 'ce'), 4) if e2('en', 'ce') else None,
    'n_en_ce_que': e3('en', 'ce', 'que'),
    'n_en_ce_qui': e3('en', 'ce', 'qui'),
    'p_que_given_en': round(e2('en', 'que') / e1('en'), 5),
    'n_en_que': e2('en', 'que'),
    # 11-homophony: la / là / l' before candidate Vs
    'n_la_est': e2('la', 'est'), 'n_là_est': e2('là', 'est'),
    'n_la_en': e2('la', 'en'), 'n_l_en': e2('l', 'en'), 'n_là_en': e2('là', 'en'),
    'n_la_de': e2('la', 'de'),
    # qu'est-ce kill-shot: era P(ce | qu'est)
    'n_qu_est': e2('qu', 'est'), 'n_qu_est_ce': e3('qu', 'est', 'ce'),
}
print("[E] words=%d rank: est=%s de=%s sont=%s ont=%s c'est(pseudo)=%d (share %.5f)"
      % (NW, era['rank_est'], era['rank_de'], era['rank_sont'], era['rank_ont'],
         n_cest, era['share_cest']))
print("[E] B: P(ce|est)=%.4f P(ce|de)=%.4f P(ce|c'est)=%.4f P(ce|sont)=%.5f P(ce|ont)=%.5f"
      % (era['p_ce_given_est'], era['p_ce_given_de'], era['p_ce_given_cest'] or -1,
         era['p_ce_given_sont'] or -1, era['p_ce_given_ont'] or -1))
print("[E] C: P(est|que,qu)=%.4f P(de|que)=%.4f P(c'est|que)=%.5f P(sont|que)=%.5f P(ont|que,qu)=%.5f"
      % (era['p_est_given_quequ'], era['p_de_given_que'], era['p_cest_given_que'],
         era['p_sont_given_que'], era['p_ont_given_quequ']))
print("[E] D: P(que|est,ce)=%.4f (n=%d) P(que|de,ce)=%.4f (n=%d) P(que|c'est,ce)=%s (n=%d)"
      % (era['p_que_given_est_ce'], era['n_est_ce'], era['p_que_given_de_ce'],
         era['n_de_ce'], era['p_que_given_cest_ce'], era['n_cest_ce']))
print("[E] E: P(que|est)=%.5f P(que|de)=%.5f P(que|c'est)=%.4f"
      % (era['p_que_given_est'], era['p_que_given_de'], era['p_que_given_cest'] or -1))
print("[E] fol('est','ce'): %s" % era['fol_est_ce'])
print("[E] fol('de','ce'): %s" % era['fol_de_ce'][:8])
print("[E] 'est ce la'=%d 'est ce là'=%d" % (era['n_est_ce_la'], era['n_est_ce_là']))

# ---- inversion sweeps: which V actually matches the cipher profile? ----
FUNC = ['de', 'la', 'le', 'les', 'et', 'est', 'que', 'qui', 'il', 'ne', 'se',
        'en', 'un', 'une', 'des', 'du', 'au', 'dans', 'pour', 'par', 'sur',
        'pas', 'plus', 'tout', 'ce', 'cette', 'ces', 'son', 'sa', 'mon', 'ma',
        'nous', 'vous', 'je', 'on', 'y', 'même', 'comme', 'avec', 'sans',
        'mais', 'donc', 'aussi', 'encore', 'bien']
inv_ce, inv_que = {}, {}
for v in FUNC:
    nv = e1(v)
    if nv >= 50:
        inv_ce[v] = round(e2(v, 'ce') / nv, 4)
        inv_que[v] = round((e2('que', v) + e2('qu', v)) / (e1('que') + e1('qu')), 4)
era['inversion_p_ce_given_V'] = sorted(inv_ce.items(), key=lambda kv: -kv[1])[:12]
era['inversion_p_V_given_quequ'] = sorted(inv_que.items(), key=lambda kv: -kv[1])[:12]
print("[E] inversion P(ce|V) top12: %s" % era['inversion_p_ce_given_V'])
print("[E] inversion P(V|que,qu) top12: %s" % era['inversion_p_V_given_quequ'])
print("[E] en: rank=%s share=%.4f P(ce|en)=%.4f P(en|que,qu)=%.4f P(que|en,ce)=%s n(en,ce,qui)=%d"
      % (era['rank_en'], era['share_en'], era['p_ce_given_en'],
         era['p_en_given_quequ'], era['p_que_given_en_ce'], era['n_en_ce_qui']))
print("[E] la/là/l'+V: n(la,est)=%d n(là,est)=%d | n(la,en)=%d n(l,en)=%d n(là,en)=%d | n(la,de)=%d"
      % (era['n_la_est'], era['n_là_est'], era['n_la_en'], era['n_l_en'],
         era['n_là_en'], era['n_la_de']))
print("[E] qu'est-ce kill-shot: n(qu,est)=%d n(qu,est,ce)=%d ; cipher n(46,24,87)=%d of 3"
      % (era['n_qu_est'], era['n_qu_est_ce'], c['n_46_24_87']))

# ---- register-gap characterization (DIAGNOSTIC ONLY — verdict uses era) ----
LES = os.path.join(DATA, 'gutenberg-17489-miserables1.txt')
lw = load_words(LES)
lwc = collections.Counter(lw)
NL = len(lw)
def l2(a, b):
    return sum(1 for x, y in zip(lw, lw[1:]) if x == a and y == b)
def l3(a, b, dd):
    return sum(1 for x, y, z in zip(lw, lw[1:], lw[2:]) if x == a and y == b and z == dd)
def lfol2(a, b, k=10):
    return collections.Counter(z for x, y, z in zip(lw, lw[1:], lw[2:])
                               if x == a and y == b).most_common(k)
gap = res['register_gap_diagnostic'] = {
    'note': 'DIAGNOSTIC ONLY: explains why H1 passed under Les Mis. Verdict uses era.',
    'n_words': NL,
    'lesmis_p_ce_given_est': round(l2('est', 'ce') / lwc['est'], 4),
    'lesmis_n_est_ce': l2('est', 'ce'), 'lesmis_n_est': lwc['est'],
    'lesmis_p_est_given_quequ': round((l2('que', 'est') + l2('qu', 'est')) /
                                      (lwc['que'] + lwc['qu']), 4),
    'lesmis_fol_est_ce': lfol2('est', 'ce'),
    'lesmis_n_est_ce_la': l3('est', 'ce', 'la'),
    'lesmis_n_est_ce_là': l3('est', 'ce', 'là'),
    'lesmis_n_est_ce_qui': l3('est', 'ce', 'qui'),
    'lesmis_n_est_ce_que': l3('est', 'ce', 'que'),
    'register_gap_p_ce_given_est': round((l2('est', 'ce') / lwc['est']) /
                                         (e2('est', 'ce') / e1('est')), 1),
}
print("[GAP] lesmis P(ce|est)=%.4f (n=%d) vs era %.4f -> %.1fx register gap"
      % (gap['lesmis_p_ce_given_est'], gap['lesmis_n_est_ce'],
         era['p_ce_given_est'], gap['register_gap_p_ce_given_est']))
print("[GAP] lesmis P(est|que,qu)=%.4f vs era %.4f"
      % (gap['lesmis_p_est_given_quequ'], era['p_est_given_quequ']))
print("[GAP] lesmis fol('est','ce'): %s" % gap['lesmis_fol_est_ce'])
print("[GAP] lesmis 'est ce la'=%d 'est ce là'=%d 'est ce qui'=%d 'est ce que'=%d"
      % (gap['lesmis_n_est_ce_la'], gap['lesmis_n_est_ce_là'],
         gap['lesmis_n_est_ce_qui'], gap['lesmis_n_est_ce_que']))
# concordances for the era ('est','ce') and ('qu','est') bigrams
def conc(biga, bigb, k=6):
    out = []
    for i in range(len(words) - 2):
        if words[i] == biga and words[i + 1] == bigb:
            out.append(' '.join(words[max(0, i - 3):i + 3]))
            if len(out) >= k:
                break
    return out
res['concordances'] = {'era_est_ce': conc('est', 'ce'),
                       'era_qu_est': conc('qu', 'est', k=7)}
print("[GAP] era 'est ce' e.g.: %s" % res['concordances']['era_est_ce'][:3])

# ============================ SCORING ============================
def within2(obs, ref):
    return ref is not None and ref > 0 and 0.5 * ref <= obs <= 2.0 * ref

def binom_p0(n, p):
    return (1 - p) ** n if p is not None and 0 <= p <= 1 else None

CANDS = {
    'est':   dict(rank=era['rank_est'], share=era['share_est'],
                   B=era['p_ce_given_est'], C=era['p_est_given_quequ'],
                   D=era['p_que_given_est_ce'], E=era['p_que_given_est']),
    "c'est": dict(rank=None, share=era['share_cest'],
                   B=era['p_ce_given_cest'], C=era['p_cest_given_que'],
                   D=era['p_que_given_cest_ce'], E=era['p_que_given_cest']),
    'de':    dict(rank=era['rank_de'], share=era['share_de'],
                   B=era['p_ce_given_de'], C=era['p_de_given_que'],
                   D=era['p_que_given_de_ce'], E=era['p_que_given_de']),
    'en':    dict(rank=era['rank_en'], share=era['share_en'],
                   B=era['p_ce_given_en'], C=era['p_en_given_quequ'],
                   D=era['p_que_given_en_ce'], E=era['p_que_given_en'],
                   needs_l_apocope=True),
    'sont':  dict(rank=era['rank_sont'], share=era['share_sont'],
                   B=era['p_ce_given_sont'], C=era['p_sont_given_que'],
                   D=None, E=None),
    'ont':   dict(rank=era['rank_ont'], share=era['share_ont'],
                   B=era['p_ce_given_ont'], C=era['p_ont_given_quequ'],
                   D=None, E=None),
}
obs = {'B': c['p_87_given_24'], 'C': c['p_24_given_46'], 'E': c['p_46_given_24']}
score = {}
for v, r in CANDS.items():
    checks, detail = [], {}
    # A: unigram — cipher rank 1 share 2.817%: era rank<=3 and share within 2x
    a_pass = (r['rank'] is not None and r['rank'] <= 3
              and r['share'] and 0.5 * r['share'] <= c['share_24'] <= 2.0 * r['share'])
    if v == "c'est":
        # pseudo-rank n/a; grade on share only
        a_pass = bool(r['share'] and 0.5 * r['share'] <= c['share_24'] <= 2.0 * r['share'])
    checks.append(bool(a_pass)); detail['A_unigram'] = bool(a_pass)
    # B: P(87|24)=0.1923 vs P(ce|V), factor-2
    b = within2(obs['B'], r['B']); checks.append(b); detail['B_follower'] = b
    # C: P(24|46)=0.1034 vs P(V|que[,qu]), factor-2
    cc = within2(obs['C'], r['C']); checks.append(cc); detail['C_predecessor'] = cc
    # D: trigram — 0/10 consistent with era P(que|V,ce)? pass if binom P(X=0)>=0.05
    if r['D'] is None:
        checks.append(None); detail['D_trigram'] = None
    else:
        p0 = binom_p0(10, r['D'])
        d = p0 is not None and p0 >= 0.05
        checks.append(d); detail['D_trigram'] = d; detail['D_binom_p0'] = round(p0, 6) if p0 else None
    # E: negative control — cipher 24->46 = 0/52; era P(que|V): pass if era ~0 (<0.005)
    if r['E'] is None:
        checks.append(None); detail['E_negcontrol'] = None
    else:
        e = r['E'] < 0.005 and c['n_24_46'] == 0
        # also fail if era says high but cipher 0
        if r['E'] >= 0.05 and c['n_24_46'] == 0:
            e = False
        checks.append(e); detail['E_negcontrol'] = e
    npass = sum(1 for x in checks if x is True)
    nfail = sum(1 for x in checks if x is False)
    score[v] = {'checks': detail, 'pass': npass, 'fail': nfail,
                'n_decided': npass + nfail}
    print("[S] %-6s A=%s B=%s C=%s D=%s E=%s -> pass %d/%d"
          % (v, detail['A_unigram'], detail['B_follower'], detail['C_predecessor'],
             detail['D_trigram'], detail['E_negcontrol'], npass, npass + nfail))

res['scores'] = score

# ---- the four original H1 checks, re-graded vs era ----
h1 = res['h1_regrade'] = [
    {'check': '1. rank-1 frequency band',
     'cipher': 'freq 52, rank 1/96, share 2.817%',
     'era': 'rank(est)=%s, share=%.4f%%; rank(de)=%s share=%.4f%%' %
            (era['rank_est'], 100 * era['share_est'], era['rank_de'], 100 * era['share_de']),
     'verdict': 'DOWNGRADED' if not score['est']['checks']['A_unigram'] else 'PASS',
     'note': 'cipher rank 1 matches "de" (era rank 1), not "est" (era rank %s); '
             'share 2.82%% is %.1fx the era "est" word rate' %
             (era['rank_est'], c['share_24'] / era['share_est'])},
    {'check': '2. P(ce|24)=0.192 vs 1.7% base',
     'cipher': 'P(87|24)=10/52=0.1923, base P(87)=32/1846=0.01733 (11.1x)',
     'era': 'P(ce|est)=%.4f (n=%d/%d)' % (era['p_ce_given_est'], era['n_est_ce'], era['n_est']),
     'verdict': 'PASS' if score['est']['checks']['B_follower'] else 'FAIL',
     'note': 'factor-2 band vs era rate'},
    {'check': "3. qu'est elision x3 (46->24)",
     'cipher': '46->24 = 3/29 = 0.1034 @%s' % c['pos_46_24'],
     'era': 'P(est|que,qu)=%.4f (n=%d)' % (era['p_est_given_quequ'], era['n_quequ_est']),
     'verdict': 'PASS' if score['est']['checks']['C_predecessor'] else 'FAIL',
     'note': 'factor-2 band vs era rate'},
    {'check': '4. P(ce|est) within 2x (was Les Mis 0.118)',
     'cipher': 'same as check 2',
     'era': 'era P(ce|est)=%.4f replaces Les Mis 0.118' % era['p_ce_given_est'],
     'verdict': 'PASS' if score['est']['checks']['B_follower'] else 'FAIL',
     'note': 'era-matched re-validation of the old Les Mis leg'},
]
for h in h1:
    print("[H1] %s -> %s" % (h['check'], h['verdict']))

# ---- joint contradiction, era recompute ----
p_era_est = era['p_que_given_est_ce']
p_era_de = era['p_que_given_de_ce']
res['joint_contradiction'] = {
    'cipher': 'P(46|87,pre=24)=0/10; P(46|87,pre=96)=3/3',
    'era_p_que_given_est_ce': p_era_est,
    'binom_p0_n10_est': round(binom_p0(10, p_era_est), 6),
    'era_p_que_given_de_ce': p_era_de,
    'binom_p0_n10_de': round(binom_p0(10, p_era_de), 6),
    'note': 'under 24=est AND 87=ce, "est-ce" should be followed by "que" at the '
            'era rate; 0/10 observed. Under 24=de AND 87=ce, "de ce" -> "que" is '
            'even more expected ("de ce que").',
}
print("[J] joint: P(que|est,ce)=%.4f -> P(0/10)=%.6f | P(que|de,ce)=%.4f -> P(0/10)=%.6f"
      % (p_era_est, binom_p0(10, p_era_est), p_era_de, binom_p0(10, p_era_de)))

# ---- "est cela" anomaly ----
res['est_cela_anomaly'] = {
    'cipher_trigram': '24-87-11 x3 @%s' % c['pos_24_87_11'],
    'contexts': c['ctx_24_87_11'],
    'era_n_est_ce_la': era['n_est_ce_la'],
    'era_n_est_ce_là': era['n_est_ce_là'],
    'era_n_est_ce': era['n_est_ce'],
    'reading_if_est': '"est cela" (ungrammatical declarative) OR "est-ce là" '
                      '(requires 11=la/là homophony)',
    'reading_if_cest': '"c\'est cela" x3 (idiomatic)',
}
print("[A!] est-cela anomaly: era 'est ce la'=%d 'est ce là'=%d of n(est,ce)=%d"
      % (era['n_est_ce_la'], era['n_est_ce_là'], era['n_est_ce']))

with open(os.path.join(HERE, 'closer_results.json'), 'w') as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
print("[done] wrote code/crowd2/closer_results.json")
