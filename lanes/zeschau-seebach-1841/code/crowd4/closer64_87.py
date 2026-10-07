#!/usr/bin/env python3
"""
CLOSER round 4 — work orders 6+7 (THE CLOSER).

WO6: adjudicate 64="meme" vs 64="qui" — symmetric battery, F30-legal legs only
     (no era-syllable-conditional legs on 29/82/34/40; era word-space legs survive;
      era unigrams as context). Attack from the 77-angle as ordered, symmetrically.
WO7: advance 87=ce via (A) register-matched corpus subset test with PRE-STATED
     falsification condition, and (B) ci/te anchor scan.
     The 87 leg must not recycle the dead 24="est" number (R1 void) nor condition
     on 96="par" (N3 circular).

Deterministic. No invented ciphertext. Every number re-derived from lane data.
Results -> code/crowd4/closer64_87_results.json
"""
import json, re, math, collections, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
DATA = os.path.join(LANE, '..', 'data')
sys.path.insert(0, LANE)  # code/ holds crib_attack.py
from crib_attack import load_pairs

pairs, odd_lines, off1 = load_pairs()
N_PAIRS = len(pairs)
FREQ = collections.Counter(pairs)
RANK = {g: i + 1 for i, (g, c) in enumerate(FREQ.most_common())}

def fol_of(g):
    return collections.Counter(pairs[i + 1] for i in range(N_PAIRS - 1) if pairs[i] == g)
def pre_of(g):
    return collections.Counter(pairs[i - 1] for i in range(1, N_PAIRS) if pairs[i] == g)

# ---------------- era corpus (Tocqueville t1+t2), attempt3 tokenizer ----------------
def load_words(path):
    text = open(path, encoding='utf-8', errors='replace').read().lower()
    m = re.search(r'\*\*\* start of.*?\*\*\*', text)
    if m:
        text = text[m.end():]
    m = re.search(r'\*\*\* end of.*', text)
    if m:
        text = text[:m.start()]
    return re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)

WORDS = (load_words(os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'))
         + load_words(os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')))
N_W = len(WORDS)
WC = collections.Counter(WORDS)
E_RANK = {w: i + 1 for i, (w, c) in enumerate(WC.most_common())}
BI = collections.Counter(zip(WORDS, WORDS[1:]))
def era_p(w): return WC[w] / N_W
def era_pcond(a, b): return BI[(a, b)] / WC[a] if WC[a] else 0.0

def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - m) / d, (c + m) / d)

def binom_ge(k, n, p):
    # P(X >= k), exact-ish via log-sum
    if p <= 0: return 0.0 if k > 0 else 1.0
    if p >= 1: return 1.0 if k <= n else 0.0
    from math import comb
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))

out = {'npairs': N_PAIRS, 'battery64': {}, 'leg87': {}}

# ============================ WO6: 64 battery ============================
# cipher-side geometry (re-derived)
f64, f87, f46 = FREQ['64'], FREQ['87'], FREQ['46']
F64, P64, F87v = fol_of('64'), pre_of('64'), fol_of('87')
bat = out['battery64']
bat['cipher'] = {
    'freq64': f64, 'rank64': RANK['64'], 'n_followers64': len(F64),
    'n_predecessors64': len(P64), 'P64_cipher': f64 / N_PAIRS,
    'n64_77': F64['77'], 'n64_29': F64['29'], 'n67_64': P64['67'],
    'n46_64': P64['46'], 'n64_46': F64['46'], 'n87_64': P64['87'],
    'P77_given64': F64['77'] / f64, 'P29_given64': F64['29'] / f64,
    'P64_given87': P64['87'] / f87,
}
# trigram identity of 64->77 x3 (methodological: n_eff for rate legs)
tri6477 = [i for i in range(N_PAIRS - 2) if pairs[i] == '64' and pairs[i+1] == '77']
bat['cipher']['trigram_64_77_X'] = [(pairs[i], pairs[i+1], pairs[i+2]) for i in tri6477]
bat['cipher']['trigram_positions'] = tri6477

# L1: unigram rate
bat['L1_unigram'] = {
    'cipher_P64': f64 / N_PAIRS,
    'era_P_qui': era_p('qui'), 'era_P_meme': era_p('même'),
    'ratio_qui': (f64 / N_PAIRS) / era_p('qui'),
    'ratio_meme': (f64 / N_PAIRS) / era_p('même'),
}
# L2: rank
bat['L2_rank'] = {'cipher_rank64': RANK['64'], 'era_rank_qui': E_RANK['qui'],
                  'era_rank_meme': E_RANK['même']}
# L3: 77-angle. verb probe set (pre-stated, common finite verbs in era top ranks)
VERBS = ['est','sont','a','ont','fait','font','dit','disent','peut','peuvent',
         'veut','veulent','doit','doivent','faut','semble','devient','reste',
         'existe','paraît','vient','viennent','prend','prennent']
VSET = set(v for v in VERBS if v in WC)
pv_qui = sum(BI[('qui', v)] for v in VSET) / WC['qui']
pv_meme = sum(BI[('même', v)] for v in VSET) / WC['même']
bat['L3_77angle'] = {
    'verb_probe_set': sorted(VSET),
    'era_Pverb_given_qui': pv_qui, 'era_Pverb_given_meme': pv_meme,
    'ratio': pv_qui / pv_meme if pv_meme else None,
    # the "meme si" escape hatch, scored symmetrically
    'era_Psi_given_meme': era_pcond('même', 'si'),
    'binom_ge_3_46_Psi_given_meme': binom_ge(3, 46, era_pcond('même', 'si')),
    'note': '77 is verb-adjacent per N21 (lead, not confirmed); '
            'grammatical: "qui"+V canonical, "meme"+V ungrammatical',
}
# L4: 64->29 x3, er-initial followers in era word-space
er_qui = sum(1 for x, y in zip(WORDS, WORDS[1:]) if x == 'qui' and y.startswith('er'))
er_meme = sum(1 for x, y in zip(WORDS, WORDS[1:]) if x == 'même' and y.startswith('er'))
bat['L4_er'] = {
    'cipher_P29_given64': F64['29'] / f64, 'n': F64['29'],
    'era_er_after_qui': er_qui, 'era_n_qui': WC['qui'],
    'era_er_after_meme': er_meme, 'era_n_meme': WC['même'],
    'era_Perin_given_qui': er_qui / WC['qui'], 'era_Perin_given_meme': er_meme / WC['même'],
    # rule-of-three upper bounds -> binomial exclusion of observed 3/46
    'binom_ge_3_46_ub_qui': binom_ge(3, 46, 3 / WC['qui']),
    'binom_ge_3_46_ub_meme': binom_ge(3, 46, 3 / WC['même']),
}
# L5: 46->64 = 0 negative control
bat['L5_queneg'] = {
    'cipher_n46_64': P64['46'], 'n46': f46,
    'era_Pqui_given_que': era_pcond('que', 'qui'),
    'era_Pmeme_given_que': era_pcond('que', 'même'),
    'expected_meme': f46 * era_pcond('que', 'même'),
}
# L6: 87->64 x5 under provisional 87=ce (marked conditional)
bat['L6_ce_follower'] = {
    'conditional_on': '87=ce (provisional)',
    'cipher_P64_given87': P64['87'] / f87,
    'era_Pqui_given_ce': era_pcond('ce', 'qui'),
    'era_Pmeme_given_ce': era_pcond('ce', 'même'),
    'ratio_qui': (P64['87'] / f87) / era_pcond('ce', 'qui'),
    'ratio_meme': (P64['87'] / f87) / era_pcond('ce', 'même'),
    'binom_ge_5_32_meme': binom_ge(5, 32, era_pcond('ce', 'même')),
    'wilson_5_32': wilson(5, 32),
}
# L7: 67->64 x2 under provisional 67="veut" (soft, qualitative)
bat['L7_veut'] = {
    'conditional_on': '67="veut" (provisional)',
    'cipher_n67_64': P64['67'],
    'era_Pmeme_given_veut': era_pcond('veut', 'même'),
    'era_Pqui_given_veut': era_pcond('veut', 'qui'),
    'era_n_veut': WC['veut'],
    'note': '"veut meme" grammatical ("il veut meme..."); "veut qui" ungrammatical',
}
# L8: 64->46 x1 (qualitative, n=1)
tri6446 = [i for i in range(N_PAIRS - 2) if pairs[i] == '64' and pairs[i+1] == '46']
bat['L8_quique'] = {
    'cipher_n64_46': F64['46'],
    'trigrams': [(pairs[i], pairs[i+1], pairs[i+2]) for i in tri6446],
    'note': '"qui que" grammatical in concessive "qui que ce soit" family; '
            '"meme que" ungrammatical',
}

# ============================ WO7: 87=ce ============================
leg = out['leg87']
# ---- (A) register-matched subset test, PRE-REGISTERED design ----
# Proxy (pre-stated BEFORE running): first-person-singular reporter voice.
# R = sentences containing je/j'/moi/m'/mon/ma/mes ; A = all other sentences.
# Metric: n("cela")/n("ce") in R vs A. Cipher target: P(11|87)=7/32=0.2188.
# Era baseline (whole corpus): 0.0414.
# FALSIFICATION (pre-stated): if R_ratio <= 0.08 -> FAIL, cela leg stays dead.
# SUCCESS (revive cela leg to provisional): R_ratio >= 0.11 (within factor 2 of 0.2188).
# 0.08 < R < 0.11 -> inconclusive. Per F26(5) this is a robustness check, not a
# confirmation instrument: success revives the leg, it cannot confirm 87=ce.
leg['A_design'] = {
    'proxy': 'first-person-singular reporter voice',
    'R_pattern': r"\bje\b|j'|moi\b|m'|\\bmon\\b|\\bma\\b|\\bmes\\b",
    'metric': 'n("cela")/n("ce")',
    'cipher_target': 7 / 32,
    'era_baseline': WC['cela'] / WC['ce'],
    'fail_bar': '<= 0.08 -> genre account FAILS, cela leg stays dead',
    'success_bar': '>= 0.11 -> cela leg revives to provisional-grade',
    'note': 'robustness check only (F26.5); cannot confirm 87=ce by itself',
}
raw = open(os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'),
           encoding='utf-8', errors='replace').read().lower() \
    + open(os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt'),
           encoding='utf-8', errors='replace').read().lower()
m = re.search(r'\*\*\* start of.*?\*\*\*', raw)
# note: two files concatenated; markers appear twice; simplest: strip Gutenberg
# boilerplate per file before concat (already handled in load_words); here redo:
def body(path):
    t = open(path, encoding='utf-8', errors='replace').read().lower()
    a = re.search(r'\*\*\* start of.*?\*\*\*', t)
    if a: t = t[a.end():]
    b = re.search(r'\*\*\* end of.*', t)
    if b: t = t[:b.start()]
    return t
text = body(os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt')) \
     + '\n' + body(os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt'))
sents = [s for s in re.split(r'[.!?…]+', text) if s.strip()]
pat = re.compile(r"\bje\b|j'|moi\b|m'|\bmon\b|\bma\b|\bmes\b")
R_sents = [s for s in sents if pat.search(s)]
A_sents = [s for s in sents if not pat.search(s)]
wrx = re.compile(r"[a-zàâäéèêëîïôöùûüÿç]+")
def cela_ce(sent_list):
    cela = ce = 0
    for s in sent_list:
        for w in wrx.findall(s):
            if w == 'cela': cela += 1
            elif w == 'ce': ce += 1
    return cela, ce
r_cela, r_ce = cela_ce(R_sents)
a_cela, a_ce = cela_ce(A_sents)
leg['A_result'] = {
    'n_sentences_total': len(sents),
    'n_sentences_R': len(R_sents), 'n_sentences_A': len(A_sents),
    'R': {'n_cela': r_cela, 'n_ce': r_ce,
          'ratio': r_cela / r_ce if r_ce else None},
    'A': {'n_cela': a_cela, 'n_ce': a_ce,
          'ratio': a_cela / a_ce if a_ce else None},
}
R_ratio = r_cela / r_ce if r_ce else None
if R_ratio is not None:
    if R_ratio <= 0.08:
        leg['A_result']['verdict'] = 'FAIL — genre account does not close the gap; cela leg stays dead'
    elif R_ratio >= 0.11:
        leg['A_result']['verdict'] = 'PASS — cela leg revives to provisional-grade (robustness check)'
    else:
        leg['A_result']['verdict'] = 'INCONCLUSIVE — between bars'

# ---- (B) ci/te anchor scan ----
# A group G adjacent to 87 whose ONLY grammatical reading given 87=ce is ci/te,
# with independent support pinning G from the other side.
# Candidates: followers of 87 (87->G = "ce"+G: ceci/cette/ceux/...) and
# predecessors (G->87: no "te ce" — ungrammatical, skip).
# Independent pins available: 34=i ground truth ("ici"=34+G); preverbal clitic
# position (V->G, G->Vfin) for "te".
BIGRAMS = collections.Counter((pairs[i], pairs[i+1]) for i in range(N_PAIRS - 1))
F87set = set(b for (a, b) in BIGRAMS if a == '87')
F34 = fol_of('34')
scan = {}
for g in sorted(F87set):
    n87g = sum(1 for i in range(N_PAIRS - 1) if pairs[i] == '87' and pairs[i+1] == g)
    scan[g] = {
        'n_87_G': n87g,
        'n_34_G_ici': F34[g],          # "ici" = 34+i ground truth
        'pre': dict(pre_of(g).most_common(6)),
        'fol': dict(fol_of(g).most_common(6)),
        'freq': FREQ[g],
    }
leg['B_scan'] = scan
# verdict logic: unique ci/te reading needs (i) 87->G bigram, (ii) G pinned as
# ci/te from the other side, (iii) no competing grammatical "ce"+G reading.
pinned_ci = [g for g in F87set if F34[g] > 0]
leg['B_result'] = {
    'ici_pins': pinned_ci,
    'verdict': ('ANCHOR FOUND' if pinned_ci else
                'NULL — no follower of 87 is pinned as ci/te from the other side '
                '(34->G = 0 for all G in fol87; "te"-clitic reads of 78 are '
                'contested by 78="me" LEAD and ungrammatical 47/37->78 under "te")'),
}

# ---- supporting observation: 87-64-77-84 joint @1800 ----
idx1800 = [i for i in range(N_PAIRS - 3)
           if pairs[i] == '87' and pairs[i+1] == '64' and pairs[i+2] == '77' and pairs[i+3] == '84']
leg['C_joint_1800'] = {
    'positions': idx1800,
    'windows': [pairs[i-2:i+5] for i in idx1800],
    'note': 'conditional on 87=ce (provisional) + 64=qui (provisional) + 77=verb-adjacent (lead): '
            'the unique fully grammatical joint parse is "ce qui [verbe] 84". '
            'Under 64="meme": "ce meme [verbe] 84" is ungrammatical. Supporting only.',
}

with open(os.path.join(HERE, 'closer64_87_results.json'), 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print(json.dumps(out, indent=1, ensure_ascii=False)[:6000])
