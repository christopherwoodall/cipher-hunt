#!/usr/bin/env python3
"""
Red Team (crowd round 2) — adversarial re-derivation of the two claims most
likely to be promoted: H1 24="est" (the Closer) and F9 64="qui" (the Formula
Tester's dependency), plus a kill-review of H5 "J'ai l'honneur de" and an
audit of the factor-2 era-rate methodology itself.

Independent re-derivation: every cipher count recomputed from load_pairs();
every era rate recomputed from the Tocqueville corpus with attempt3's
tokenizer. No trust in prior prose — only in bytes.

Writes: code/crowd2/red_team_results.json (numbers), .md (verdicts).
"""
import json, re, os, sys, math, collections

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.join(HERE, '..', '..')
DATA = os.path.join(LANE, 'data')
sys.path.insert(0, os.path.join(LANE, 'code'))
from crib_attack import load_pairs

T1 = os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt')
T2 = os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')

out = {'checks': {}, 'verdicts': {}, 'numbers': {}}

# ---------------- cipher stream ----------------
pairs, odd_lines, off1 = load_pairs()
N = len(pairs)
freq = collections.Counter(pairs)
ranked = sorted(freq.items(), key=lambda kv: -kv[1])
rank_of = {g: i + 1 for i, (g, _) in enumerate(ranked)}  # 1-based

def fol(g):
    return collections.Counter(pairs[i + 1] for i, x in enumerate(pairs[:-1]) if x == g)

def pre(g):
    return collections.Counter(pairs[i - 1] for i, x in enumerate(pairs) if x == g and i > 0)

def occ(seq):
    n = len(seq)
    return [i for i in range(N - n + 1) if pairs[i:i + n] == seq]

def P_bigram(a, b):
    return fol(a)[b] / freq[a] if freq[a] else 0.0

out['numbers']['cipher'] = {
    'pairs': N, 'distinct': len(freq),
    'freq_24': freq['24'], 'rank_24': rank_of['24'],
    'freq_87': freq['87'], 'rank_87': rank_of['87'],
    'freq_64': freq['64'], 'rank_64': rank_of['64'],
    'freq_46': freq['46'], 'freq_11': freq['11'],
}

# ---------------- era corpus (attempt3 tokenizer) ----------------
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
erank = [w for w, _ in wc.most_common()]
erank_of = {w: i + 1 for i, w in enumerate(erank)}

def ecnt(w):
    return wc[w]

def ebicnt(a, b):
    return sum(1 for x, y in zip(words, words[1:]) if x == a and y == b)

def etricnt(a, b, c):
    return sum(1 for x, y, z in zip(words, words[1:], words[2:]) if x == a and y == b and z == c)

def Pera(b, a):
    """P(word b | word a) in era corpus."""
    na = ecnt(a)
    return ebicnt(a, b) / na if na else None

out['numbers']['era'] = {'words': NW}

# =====================================================================
# PART A — 24 = "est" (re-derive the surgeon's 4 checks, era-matched)
# =====================================================================
A = {}
c24_87 = fol('24')['87']
p_ce_given_24 = c24_87 / freq['24']
A['check1_rank'] = {'freq_24': freq['24'], 'rank_24': rank_of['24'],
                    'era_rank_est': erank_of.get('est'), 'era_rank_en': erank_of.get('en'),
                    'era_rank_de': erank_of.get('de'),
                    'era_share_est': ecnt('est') / NW, 'era_share_en': ecnt('en') / NW,
                    'cipher_share_24': freq['24'] / N}
# surgeon's check 2/3, era-matched (surgeon used Les Mis; methodology demands era)
A['check2_bigram'] = {
    'cipher_P87_given_24': round(p_ce_given_24, 4), 'n': '%d/%d' % (c24_87, freq['24']),
    'era_Pce_given_est': round(Pera('ce', 'est'), 4),
    'era_Pce_given_en': round(Pera('ce', 'en'), 4),
    'era_Pce_given_de': round(Pera('ce', 'de'), 4),
}
for k in ('era_Pce_given_est', 'era_Pce_given_en', 'era_Pce_given_de'):
    ref = A['check2_bigram'][k]
    A['check2_bigram']['ratio_vs_' + k.split('_')[-1]] = round(p_ce_given_24 / ref, 3)

# surgeon's check 4: "qu'est" elision x3 = 46->24
pos_46_24 = occ(['46', '24'])
A['check4_elision'] = {
    'count_46_24': len(pos_46_24), 'positions': pos_46_24,
    'contexts': [[' '.join(pairs[max(0, i - 3):i]), '46', '24', ' '.join(pairs[i + 2:i + 5])] for i in pos_46_24],
    # era: "qu'est" -> tokens ("qu","est"); "qu'en" -> ("qu","en")
    'era_n_qu': ecnt('qu'),
    'era_P_est_given_qu': round(ebicnt('qu', 'est') / ecnt('qu'), 4) if ecnt('qu') else None,
    'era_P_en_given_qu': round(ebicnt('qu', 'en') / ecnt('qu'), 4) if ecnt('qu') else None,
    'cipher_P24_given_46': round(fol('46')['24'] / freq['46'], 4),
}
# --- discriminator: 87->24. Under 24="est" this is "c'est" (should be COMMON).
# Under rival 24="en" this is "ce en" (ungrammatical, should be ~0).
c87_24 = fol('87')['24']
A['discriminator_87_24'] = {
    'cipher_87_24': c87_24, 'cipher_P24_given_87': round(c87_24 / freq['87'], 4),
    'era_P_est_given_ce': round(Pera('est', 'ce'), 4),
    'era_n_ce_est': ebicnt('ce', 'est'),
    'era_n_ce': ecnt('ce'),
    'era_P_en_given_ce': round(Pera('en', 'ce'), 4),
    'era_n_ce_en': ebicnt('ce', 'en'),
}
# --- the "est cela" anomaly: 24-87-11 x3. Under 24="est": "est cela".
# Under 24="en": "en cela" (idiomatic). Era rates decide.
pos_24_87_11 = occ(['24', '87', '11'])
A['anomaly_est_cela'] = {
    'count_24_87_11': len(pos_24_87_11), 'positions': pos_24_87_11,
    'cipher_P11_given_24': round(fol('24')['11'] / freq['24'], 4),
    'cipher_P11_given_24_87': round(len(pos_24_87_11) / c24_87, 4) if c24_87 else None,
    'era_P_cela_given_est': round(Pera('cela', 'est'), 5),
    'era_P_cela_given_en': round(Pera('cela', 'en'), 5),
    'era_n_est_cela': ebicnt('est', 'cela'), 'era_n_est': ecnt('est'),
    'era_n_en_cela': ebicnt('en', 'cela'), 'era_n_en': ecnt('en'),
}
# --- the "est-ce que" miss: 24-87-46 = 0. Era-matched expectation.
pos_24_87_46 = occ(['24', '87', '46'])
era_p_que_given_estce = etricnt('est', 'ce', 'que') / ebicnt('est', 'ce') if ebicnt('est', 'ce') else None
A['miss_est_ce_que'] = {
    'count_24_87_46': len(pos_24_87_46),
    'era_n_est_ce': ebicnt('est', 'ce'), 'era_n_est_ce_que': etricnt('est', 'ce', 'que'),
    'era_P_que_given_est_ce': round(era_p_que_given_estce, 4) if era_p_que_given_estce else None,
    'binom_P0_of_10': round((1 - era_p_que_given_estce) ** 10, 4) if era_p_que_given_estce else None,
    # same under the "en" rival: "en ce que" is ungrammatical -> expect ~0
    'era_n_en_ce': ebicnt('en', 'ce'), 'era_n_en_ce_que': etricnt('en', 'ce', 'que'),
}
# --- rival 24="de": "de ce que" should then be common; it is 0x.
A['rival_de_refutation'] = {
    'era_n_de_ce': ebicnt('de', 'ce'), 'era_n_de_ce_que': etricnt('de', 'ce', 'que'),
    'era_P_que_given_de_ce': round(etricnt('de', 'ce', 'que') / ebicnt('de', 'ce'), 4) if ebicnt('de', 'ce') else None,
}
# --- 24-87-64 x3: "en ce qui" vs "est ce qui"
pos_24_87_64 = occ(['24', '87', '64'])
A['frame_24_87_64'] = {
    'count': len(pos_24_87_64), 'positions': pos_24_87_64,
    'era_n_en_ce_qui': etricnt('en', 'ce', 'qui'),
    'era_n_est_ce_qui': etricnt('est', 'ce', 'qui'),
    'era_n_de_ce_qui': etricnt('de', 'ce', 'qui'),
}
# --- followers of 24 vs era followers of est/en
A['followers_24_top10'] = fol('24').most_common(10)
A['era_followers_est_top10'] = collections.Counter(y for x, y in zip(words, words[1:]) if x == 'est').most_common(10)
A['era_followers_en_top10'] = collections.Counter(y for x, y in zip(words, words[1:]) if x == 'en').most_common(10)
out['checks']['A_24_est'] = A

# =====================================================================
# PART B — 64 = "qui" (full adversarial treatment)
# =====================================================================
B = {}
c87_64 = fol('87')['64']
p_64_given_87 = c87_64 / freq['87']
B['check_a_rank'] = {'freq_64': freq['64'], 'rank_64': rank_of['64'],
                     'cipher_share_64': round(freq['64'] / N, 4),
                     'era_rank_qui': erank_of.get('qui'), 'era_share_qui': round(ecnt('qui') / NW, 4),
                     'era_rank_qu': erank_of.get('qu'), 'era_share_qu': round(ecnt('qu') / NW, 4)}
B['check_b_bigram'] = {'cipher_P64_given_87': round(p_64_given_87, 4), 'n': '%d/%d' % (c87_64, freq['87']),
                       'era_P_qui_given_ce': round(Pera('qui', 'ce'), 4),
                       'era_P_qu_given_ce': round(Pera('qu', 'ce'), 4),
                       'era_P_n_given_ce': round(Pera('n', 'ce'), 4),
                       'era_top_followers_of_ce': collections.Counter(y for x, y in zip(words, words[1:]) if x == 'ce').most_common(10)}
lo, hi = 0.5 * p_64_given_87, 2.0 * p_64_given_87
B['check_b_bigram']['band'] = [round(lo, 4), round(hi, 4)]
for w, lbl in (('qui', 'qui'), ('qu', 'qu_elided_que'), ('n', 'n_elided_ne')):
    r = Pera(w, 'ce')
    B['check_b_bigram']['in_band_' + lbl] = (lo <= r <= hi) if r else None
# rival "ci": attempt3's P(87|64) argument vs era P(ce|qui)
c64_87 = fol('64')['87']
B['rival_ci'] = {'cipher_P87_given_64': round(pre('64')['87'] / freq['64'], 4),
                 'era_P_ce_given_qui': round(Pera('ce', 'qui'), 4) if Pera('ce', 'qui') else None,
                 'era_P_ci_given_ce': None}
# check c: 46=que -> 64 = 0, vs era rates for each rival
B['check_c_negcontrol'] = {
    'cipher_46_64': fol('46')['64'],
    'era_P_qui_given_que': round(Pera('qui', 'que'), 5),
    'era_P_qu_given_que': round(Pera('qu', 'que'), 5),
    'era_P_n_given_que': round(Pera('n', 'que'), 5),
    'era_n_que': ecnt('que'),
}
# check d: free-word distribution — is it discriminating? control groups.
def spread(g):
    f = fol(g); p = pre(g)
    tot = sum(f.values())
    return {'n_fol': len(f), 'n_pre': len(p), 'top_share': round(max(f.values()) / tot, 3) if tot else None,
            'n': freq[g]}
B['check_d_spread'] = {'64_qui': spread('64'),
                       'controls': {g: spread(g) for g in ['06', '77', '24', '87', '11', '46', '16', '01']}}
# dependency: every check that conditions on 87
B['dependency'] = {'checks_conditioning_on_87': ['b (P(64|87) vs P(qui|ce))'],
                   'anchor_87_status': 'provisional (F6: best-tested reading, cela-leg register-dependent)',
                   'anchor_independent_checks': ['a (rank)', 'c (46->64=0, ground truth)', 'd (spread)']}
# 64's followers under rival readings (verbs vs pronouns vs vowel-verbs) — recorded, anchors too sparse to decide
B['followers_64'] = fol('64').most_common(12)
B['predecessors_64'] = pre('64').most_common(12)
out['checks']['B_64_qui'] = B

# =====================================================================
# PART C — methodology audit: the factor-2 band
# =====================================================================
C = {}
# C1: calibrate the band on GROUND-TRUTH anchor pairs (word-level: 11=la, 46=que)
C['calibration_ground_truth'] = {
    'cipher_P11_given_46': round(P_bigram('46', '11'), 4), 'era_P_la_given_que': round(Pera('la', 'que'), 4),
    'cipher_P46_given_11': round(P_bigram('11', '46'), 4), 'era_P_que_given_la': round(Pera('que', 'la'), 4),
    'cipher_P46_given_46': round(P_bigram('46', '46'), 4), 'era_P_que_given_que': round(Pera('que', 'que'), 4),
}
for ck, ek in (('cipher_P11_given_46', 'era_P_la_given_que'), ('cipher_P46_given_11', 'era_P_que_given_la')):
    o, r = C['calibration_ground_truth'][ck], C['calibration_ground_truth'][ek]
    C['calibration_ground_truth']['band_pass_' + ck] = (0.5 * r <= o <= 2.0 * r) if r else None
# C2: band-edge distances for every rate check behind CONFIRMED/provisional claims
def edge(obs, ref):
    return {'obs': round(obs, 4), 'ref': round(ref, 4), 'ratio': round(obs / ref, 3),
            'dist_to_edge': round(min(obs / (0.5 * ref), (2.0 * ref) / obs), 3)}
C['band_edges'] = {
    '87ce_Pque_given_87': edge(fol('87')['46'] / freq['87'], Pera('que', 'ce')),
    '64qui_P64_given_87': edge(p_64_given_87, Pera('qui', 'ce')),
    '64qui_rival_qu': edge(p_64_given_87, Pera('qu', 'ce')),
    '64qui_rival_n': edge(p_64_given_87, Pera('n', 'ce')),
    '24est_Pce_given_24_vs_est': edge(p_ce_given_24, Pera('ce', 'est')),
    '24est_Pce_given_24_vs_en': edge(p_ce_given_24, Pera('ce', 'en')),
}
# C3: the cela-leg flip — verdict as a function of band width (87=ce)
obs_cela = fol('87')['11'] / freq['87']
C['cela_leg_band_sensitivity'] = {
    'obs_P11_given_87': round(obs_cela, 4),
    'lesmis_unigram_ratio': 0.278, 'era_unigram_ratio': round(ecnt('cela') / ecnt('ce'), 4),
    'band_halfwidth_needed_lesmis': round(obs_cela / 0.278, 2),
    'band_halfwidth_needed_era': round(obs_cela / (ecnt('cela') / ecnt('ce')), 2),
}
out['checks']['C_band_audit'] = C

# =====================================================================
# PART D — H5 "J'ai l'honneur de" kill checks
# =====================================================================
D = {}
pos_r1 = occ(['77', '78', '94', '82', '06'])
D['r1_repeat'] = {'count_pair_aligned': len(pos_r1), 'positions': pos_r1,
                  'upstream_claimed': 5, 'raw_substring_claimed': 4,
                  'position4_group': '82', 'position4_ground_truth': 'm (pencil crib)',
                  'phrase_position4_required': 'neur (j-ai/l/hon/NEUR/de)'}
D['opening_zone'] = {'r1_in_opening_100': [p for p in pos_r1 if p < 100]}
out['checks']['D_honneur'] = D

json.dump(out, open(os.path.join(HERE, 'red_team_results.json'), 'w'), indent=1, default=str)

# ---------------- console summary ----------------
print("=== A: 24=est re-derivation ===")
print("rank24=%d freq=%d | era rank est=%s en=%s de=%s" % (rank_of['24'], freq['24'], erank_of.get('est'), erank_of.get('en'), erank_of.get('de')))
print("P(87|24)=%.4f | era P(ce|est)=%.4f P(ce|en)=%.4f P(ce|de)=%.4f" % (p_ce_given_24, Pera('ce','est'), Pera('ce','en'), Pera('ce','de')))
print("46->24 x%d @%s | era P(est|qu)=%.4f P(en|qu)=%.4f | cipher P(24|46)=%.4f" % (len(pos_46_24), pos_46_24, ebicnt('qu','est')/ecnt('qu'), ebicnt('qu','en')/ecnt('qu'), fol('46')['24']/freq['46']))
print("87->24 (c'est test) = %d | era P(est|ce)=%.4f (n=%d) P(en|ce)=%.4f (n=%d)" % (c87_24, Pera('est','ce'), ebicnt('ce','est'), Pera('en','ce'), ebicnt('ce','en')))
print("24-87-11 x%d | era P(cela|est)=%.5f (n=%d) P(cela|en)=%.5f (n=%d)" % (len(pos_24_87_11), Pera('cela','est'), ebicnt('est','cela'), Pera('cela','en'), ebicnt('en','cela')))
print("24-87-46 x%d | era P(que|est,ce)=%.4f -> binom P(0/10)=%.4f | era n(en,ce,que)=%d" % (len(pos_24_87_46), era_p_que_given_estce, (1-era_p_que_given_estce)**10, etricnt('en','ce','que')))
print("rival de: era P(que|de,ce)=%.4f (n_de_ce=%d)" % (etricnt('de','ce','que')/ebicnt('de','ce'), ebicnt('de','ce')))
print("24-87-64 x%d | era en-ce-qui=%d est-ce-qui=%d de-ce-qui=%d" % (len(pos_24_87_64), etricnt('en','ce','qui'), etricnt('est','ce','qui'), etricnt('de','ce','qui')))
print("followers 24:", fol('24').most_common(10))
print()
print("=== B: 64=qui ===")
print("rank64=%d | P(64|87)=%.4f | era P(qui|ce)=%.4f P(qu|ce)=%.4f P(n|ce)=%.4f | band=[%.4f,%.4f]" % (rank_of['64'], p_64_given_87, Pera('qui','ce'), Pera('qu','ce'), Pera('n','ce'), lo, hi))
print("46->64=%d | era P(qui|que)=%.5f P(qu|que)=%.5f P(n|que)=%.5f" % (fol('46')['64'], Pera('qui','que'), Pera('qu','que'), Pera('n','que')))
print("P(87|64)=%.4f | era P(ce|qui)=%.4f" % (pre('64')['87']/freq['64'], Pera('ce','qui')))
print("spread64:", spread('64'))
print()
print("=== C: band audit ===")
print("ground-truth calibration:", C['calibration_ground_truth'])
print("band edges:", json.dumps(C['band_edges'], indent=1))
print("cela-leg:", C['cela_leg_band_sensitivity'])
print()
print("=== D: honneur ===")
print("r1 pair-aligned count:", len(pos_r1), "positions:", pos_r1)
