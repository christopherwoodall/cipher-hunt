#!/usr/bin/env python3
"""
HYPOTHESIS SWEEPER v2 — Work Order 5.

Tests the remaining open hypotheses (NOTES.md "Open hypotheses" H2, H3, H4),
each against >=2 independent checks, ALL rate checks against the ERA corpus
(Tocqueville 1835/1840, Tomes 1+2 — NOT Les Mis; NOTES.md F10).
For every hypothesis a RIVAL reading is actively sought and scored — no
confirmation-only scorecards (Red-Team lesson, F6).

v2 fixes over v1 (self-review):
 - Elision handling: era "ne" includes "n'" (tokenized as "n"), era "que"
   includes "qu'". v1 undercounted both (tokenizer artifact, same class as
   the Red-Team ratio catch in F6/F13).
 - Frequency checks are calibrated with an empirical syllable-vs-word
   inflation factor from word-like anchors (11=la, 46=que, 87=ce, 64=qui),
   instead of comparing rank ordinals across a 96-type vs 20k-type vocabulary.
 - Small-n bigram controls use a count rule (obs <= exp + 2*sqrt(exp+.25) + 1)
   instead of a factor band, so a 0x/1x observation is not failed mechanically.
 - H3's "neutral control" (P(ce|06) vs era P(ce|de)) replaced by the honest
   era P(ce|ne) comparison.
 - H4a "parce que" frame uses qu-inclusive era P(que|qu'|parce) ("parce qu'il").
 - 41/08 rivals scored lexically ("ternière"/"mernière" are not French words),
   not by rate.

Hypotheses:
  (a) H2: 77="pas"   (b) H3: 06="ne"
  (c) H4a: 96="par" | H4b: 96="de"   (d) H4c: 41="der", 08="ni"

Deterministic. No invented ciphertext or keys. Nulls are first-class.
Output -> code/crowd2/hypothesis_sweeper_results.json
"""
import json, re, math, statistics, collections, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.dirname(HERE)
DATA = os.path.join(os.path.dirname(CODE), 'data')
sys.path.insert(0, CODE)
from crib_attack import load_pairs

T1 = os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt')
T2 = os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')

OUT = []
def log(s):
    print(s); OUT.append(s)

def load_words(path):
    text = open(path, encoding='utf-8', errors='replace').read().lower()
    m = re.search(r'\*\*\* start of.*?\*\*\*', text)
    if m: text = text[m.end():]
    m = re.search(r'\*\*\* end of.*', text)
    if m: text = text[:m.start()]
    return re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)

WORDS = load_words(T1) + load_words(T2)
NWORDS = len(WORDS)
WC = collections.Counter(WORDS)
BIGRAMS = list(zip(WORDS, WORDS[1:]))

def cntw(w): return WC.get(w, 0)
def bi(a, b): return sum(1 for x, y in BIGRAMS if x == a and y == b)

NE = ('ne', 'n')       # "n'" elides to "n" under the tokenizer
QUE = ('que', 'qu')
def cnt_ne(): return sum(cntw(w) for w in NE)
def bi_ne(b): return sum(bi(a, b) for a in NE)          # X in {ne, n'} -> b
def bi_que_ne(): return sum(bi('que', a) for a in NE)   # que -> {ne, n'}
def bi_parce_que(): return sum(bi('parce', q) for q in QUE)
def tri_de_ce_que(): return sum(1 for x, y, z in zip(WORDS, WORDS[1:], WORDS[2:])
                                if x == 'de' and y == 'ce' and z in QUE)

# ---------------- cipher ----------------
pairs, _, _ = load_pairs()
N = len(pairs)
FREQ = collections.Counter(pairs)
def frank(g):
    s = sorted(FREQ.items(), key=lambda kv: -kv[1])
    return next(i for i, (gg, _) in enumerate(s) if gg == g) + 1
def nb(g, d=+1):
    c = collections.Counter()
    for i, x in enumerate(pairs):
        if x == g:
            j = i + d
            if 0 <= j < N: c[pairs[j]] += 1
    return c

def within(obs, ref, lo=0.5, hi=2.0):
    return ref is not None and ref > 0 and lo * ref <= obs <= hi * ref

def count_ok(obs_c, n, era_rate):
    """Small-n control: pass when observed count is within ~2 sigma + 1 of
    the era-expected count. Returns (ok, expected, threshold)."""
    exp = n * (era_rate or 0.0)
    thresh = exp + 2 * math.sqrt(exp + 0.25) + 1
    return obs_c <= thresh, exp, thresh

RES = {'hypotheses': {}, 'meta': {'pairs': N, 'era_words': NWORDS,
    'note': 'all rate checks vs Tocqueville 1835/1840; elision-aware (ne/n, que/qu)'}}

def verdict(name, checks):
    # checks: list of (passed, text) or (passed, text, hard). A hard fail
    # (grammatical contradiction / lexical impossibility) REFUTES outright
    # (attempt-2 rule), regardless of passes elsewhere.
    passed = [c for c in checks if c[0] is True]
    failed = [c for c in checks if c[0] is False]
    info = [c for c in checks if c[0] is None]
    hard_fail = any(len(c) > 2 and c[2] and c[0] is False for c in checks)
    v = 'REFUTED' if hard_fail else \
        ('CONFIRMED' if len(passed) >= 2 and not failed else
         ('PLAUSIBLE' if len(passed) >= 1 and not failed else
          ('REFUTED' if failed and len(passed) < 2 else 'INCONCLUSIVE')))
    RES['hypotheses'][name] = {'verdict': v, 'passed': len(passed),
        'failed': len(failed),
        'checks': [{'result': 'pass' if p else ('fail' if p is False else 'info'), 'text': t}
                   for p, t, *_ in checks]}
    log('== %s: %s (%d pass / %d fail / %d info)' % (name, v, len(passed), len(failed), len(info)))
    for p, t, *_ in checks:
        log('   [%s] %s' % ('PASS' if p else ('FAIL' if p is False else 'info'), t))
    return v

# ---------------- inflation calibration ----------------
# word-like anchors: cipher syllable rate vs era word rate
CAL = {'11': 'la', '46': 'que', '87': 'ce', '64': 'qui'}
infl = {}
for g, w in CAL.items():
    cr, er = FREQ[g] / N, cntw(w) / NWORDS
    infl[g] = cr / er if er else None
    log('calib: %s=%s cipher_rate=%.4f era_rate=%.5f infl=%.2f'
        % (g, w, cr, er, infl[g] or 0))
INFL = statistics.median(v for v in infl.values() if v)
INFL_CORE = statistics.median([infl['11'], infl['46']])  # pencil-crib anchors only
log('calib: median inflation(all)=%.2f  (pencil-only la/que)=%.2f' % (INFL, INFL_CORE))
log('era unigram rates: ' + ' '.join('%s=%.5f' % (w, cntw(w) / NWORDS)
    for w in ['la', 'que', 'ce', 'qui', 'pas', 'ne', 'par', 'de', 'pour']))

def freq_check(g, word):
    """Is the cipher group's rate consistent with the era word's rate,
    scaled by the empirical syllable inflation? Wide (0.25, 4) band."""
    cr = FREQ[g] / N
    pred = INFL * cntw(word) / NWORDS
    ok = within(cr, pred, 0.25, 4.0)
    return ok, 'freq: cipher P(%s)=%.4f vs inflation-scaled era P("%s")=%.4f (infl=%.1f, band 4x)' % (
        g, cr, word, pred, INFL)

# ================= (a) H2: 77 = "pas" =================
log('\n############ (a) H2: 77 = "pas" ############')
n77, r77 = FREQ['77'], frank('77')
n06, r06 = FREQ['06'], frank('06')
fol06, pre77, fol77 = nb('06', +1), nb('77', -1), nb('77', +1)
c_06_77 = fol06['77']; p77_g06 = c_06_77 / n06
p06_g77 = pre77['06'] / n77
c_67_77 = pre77['67']
c_46_77 = nb('46', +1)['77']; c_46_06 = nb('46', +1)['06']

n_ne, n_pas = cnt_ne(), cntw('pas')
era_ratio = n_ne / n_pas
era_p_pas_ne = bi_ne('pas') / n_ne            # P(pas | ne/n')
era_p_ne_pas = bi_ne('pas') / n_pas           # P(ne/n' before pas)
era_p_pas_que = bi('que', 'pas') / cntw('que')
era_p_ne_que = bi_que_ne() / cntw('que')
era_p_que_ne = sum(bi(a, 'que') for a in NE) / n_ne
era_p_plus_ne = sum(bi(a, 'plus') for a in NE) / n_ne
era_p_la_pas = bi('pas', 'la') / n_pas
era_p_ce_pas = bi('pas', 'ce') / n_pas
log('cipher: 77 n=%d rank=%d | 06 n=%d rank=%d' % (n77, r77, n06, r06))
log('cipher: 06->77 %d/%d=%.4f | 77 preceded-by-06 %d/%d=%.4f | 67->77 %d/37=%.4f | 46->77 %d | 46->06 %d'
    % (c_06_77, n06, p77_g06, pre77['06'], n77, p06_g77, c_67_77, c_67_77 / 37, c_46_77, c_46_06))
log('era: n(ne/n\')=%d n(pas)=%d ratio=%.4f | P(pas|ne)=%.4f | P(ne|pas)=%.4f'
    % (n_ne, n_pas, era_ratio, era_p_pas_ne, era_p_ne_pas))
log('era: P(pas|que)=%.5f P(ne|que)=%.5f P(que|ne)=%.5f P(plus|ne)=%.4f P(la|pas)=%.4f P(ce|pas)=%.4f'
    % (era_p_pas_que, era_p_ne_que, era_p_que_ne, era_p_plus_ne, era_p_la_pas, era_p_ce_pas))
log('era: top-10 predecessors of "pas": %s'
    % collections.Counter(x for x, y in BIGRAMS if y == 'pas').most_common(10))
log('era: top-10 followers of "pas": %s'
    % collections.Counter(y for x, y in BIGRAMS if x == 'pas').most_common(10))
log('cipher predecessors of 77 (top12): %s' % pre77.most_common(12))

ok_f, txt_f = freq_check('77', 'pas')
ok_qp, exp_qp, th_qp = count_ok(c_46_77, FREQ['46'], era_p_pas_que)
ok_qn, exp_qn, th_qn = count_ok(c_46_06, FREQ['46'], era_p_ne_que)
checks_pas = [
    (ok_f, txt_f),
    (within(n06 / n77, era_ratio),
     'ratio: 06/77=%.3f vs era n(ne/n\')/n(pas)=%.3f (factor-2 band; caveat: cipher 77 also covers pas-syllable inside passe/passer/repas, depressing the cipher ratio)'
     % (n06 / n77, era_ratio)),
    (within(p77_g06, era_p_pas_ne),
     'bigram FWD: cipher P(77|06)=%.4f vs era P(pas|ne/n\')=%.4f — %.1fx %s'
     % (p77_g06, era_p_pas_ne, p77_g06 / era_p_pas_ne,
        'MISS' if not within(p77_g06, era_p_pas_ne) else 'ok')),
    (within(p06_g77, era_p_ne_pas),
     'bigram BWD: cipher P(06|77)=%.4f vs era P(ne/n\'|pas)=%.4f — %.1fx (same adjacency fact as FWD, other direction; not fully independent)'
     % (p06_g77, era_p_ne_pas, p06_g77 / era_p_ne_pas)),
    (within(fol77['11'] / n77, era_p_la_pas, 1/3, 3),
     'follower-anchor probe: cipher P(11=la|77)=%d/%d=%.3f vs era P(la|pas)=%.4f (3x band)'
     % (fol77['11'], n77, fol77['11'] / n77, era_p_la_pas)),
    (None,
     'follower-anchor probe (ce leg, n=1, info only): cipher P(87=ce|77)=%d/%d=%.3f vs era P(ce|pas)=%.4f — count rule: exp %.2f, consistent-but-weak'
     % (fol77['87'], n77, fol77['87'] / n77, era_p_ce_pas, n77 * era_p_ce_pas)),
    ((ok_qp, 'joint "que->pas"')[0],
     'joint "que->pas": cipher 46->77=%d/29 (exp %.2f, thr %.1f) vs era P(pas|que)=%.5f'
     % (c_46_77, exp_qp, th_qp, era_p_pas_que)),
    ((ok_qn, 'joint "que->ne"')[0],
     'joint "que->ne": cipher 46->06=%d/29 (exp %.2f, thr %.1f) vs era P(ne/n\'|que)=%.5f'
     % (c_46_06, exp_qn, th_qn, era_p_ne_que)),
    (None, 'caveat: 67->77 = 6/37 = 16.2%% — a "ne"-like predecessor of 77; 67 unidentified (joint 06/77 note)'),
    (None, 'caveat: 77 heads the r1 repeat 77-78-94-82(m)-06 x2 — word-family/proper-noun rival (linguist H5) unscored'),
]
v_pas = verdict('H2 77="pas"', checks_pas)

# rivals for 77
log('\n-- rivals for 77 --')
era_p_que_que = bi('que', 'que') / cntw('que')
ok_77q_06, exp_77q_06, th_77q_06 = count_ok(c_06_77, n06, era_p_que_ne)   # 06=ne -> 77=que
ok_77q_46, exp_77q_46, th_77q_46 = count_ok(c_46_77, FREQ['46'], era_p_que_que)
ok_fq, txt_fq = freq_check('77', 'que')
ok_fp, txt_fp = freq_check('77', 'plus')
log('era P(que|que)=%.5f' % era_p_que_que)
rival_que = [
    (ok_fq, 'RIVAL 77="que": ' + txt_fq),
    (ok_77q_06,
     'RIVAL 77="que": cipher 06->77=%d/46 (exp %.2f, thr %.1f) as "ne->que" vs era P(que|ne/n\')=%.5f — restrictive "ne...que" is non-adjacent in prose'
     % (c_06_77, exp_77q_06, th_77q_06, era_p_que_ne)),
    (ok_77q_46,
     'RIVAL 77="que": cipher 46->77=%d/29 (exp %.2f, thr %.1f) vs era P(que|que)=%.5f'
     % (c_46_77, exp_77q_46, th_77q_46, era_p_que_que)),
]
v_rque = verdict('RIVAL 77="que"', rival_que)
ok_77p_06, exp_77p_06, th_77p_06 = count_ok(c_06_77, n06, era_p_plus_ne)
rival_plus = [
    (ok_fp, 'RIVAL 77="plus": ' + txt_fp),
    (ok_77p_06,
     'RIVAL 77="plus": cipher 06->77=%d/46 (exp %.2f, thr %.1f) as "ne->plus" vs era P(plus|ne/n\')=%.4f'
     % (c_06_77, exp_77p_06, th_77p_06, era_p_plus_ne)),
]
v_rplus = verdict('RIVAL 77="plus"', rival_plus)
ok_sw, exp_sw, th_sw = count_ok(pre77['06'], n77, sum(bi('pas', a) for a in NE) / n_pas)
rival_swap = [
    (ok_sw,
     'RIVAL 77="ne" (swap with 06): cipher 06->77=%d/44 (exp %.2f, thr %.1f) as "pas->ne" vs era P(ne/n\'|pas)=%.5f ~0 — ungrammatical'
     % (pre77['06'], exp_sw, th_sw, sum(bi('pas', a) for a in NE) / n_pas),
     True),
]
v_rswap = verdict('RIVAL 77="ne"-swap', rival_swap)

# ================= (b) H3: 06 = "ne" =================
log('\n############ (b) H3: 06 = "ne" ############')
pre06 = nb('06', -1)
top06 = fol06.most_common(1)[0]
era_top_ne = collections.Counter(y for x, y in BIGRAMS if x in NE).most_common(8)
era_top_share_ne = era_top_ne[0][1] / n_ne
era_p_ce_ne = sum(bi(a, 'ce') for a in NE) / n_ne
era_p_er_ne = sum(1 for x, y in BIGRAMS if x in NE and y.startswith('er')) / n_ne
era_p_que_ne2 = sum(bi(a, q) for a in NE for q in QUE) / n_ne
c_06_87 = fol06['87']; c_06_46 = fol06['46']; c_06_29 = fol06['29']
log('cipher: 06 n=%d rank=%d | preds=%d followers=%d | top follower=%s x%d (%.3f)'
    % (n06, r06, len(pre06), len(fol06), top06[0], top06[1], top06[1] / n06))
log('cipher: 06->77=%d 06->29(er)=%d 06->00=%d 06->11(la)=%d 06->87(ce)=%d 06->46(que)=%d'
    % (fol06['77'], c_06_29, fol06['00'], fol06['11'], c_06_87, c_06_46))
log('era: top followers of ne/n\': %s (top share %.4f)' % (era_top_ne, era_top_share_ne))
log('era: P(ce|ne)=%.4f P(que|qu\'|ne)=%.5f P(word starts "er"|ne)=%.4f'
    % (era_p_ce_ne, era_p_que_ne2, era_p_er_ne))
log('cipher predecessors of 06 (top12): %s' % pre06.most_common(12))

ok_f06, txt_f06 = freq_check('06', 'ne')
ok_06ce, exp_06ce, th_06ce = count_ok(c_06_87, n06, era_p_ce_ne)
ok_06qu, exp_06qu, th_06qu = count_ok(c_06_46, n06, era_p_que_ne2)
ok_06er, exp_06er, th_06er = count_ok(c_06_29, n06, era_p_er_ne)
ok_46_06b, exp_4606, th_4606 = count_ok(c_46_06, FREQ['46'], era_p_ne_que)
checks_ne = [
    (ok_f06, txt_f06),
    (within(n06 / n77, era_ratio),
     'ratio (SHARED with H2, not independent): 06/77=%.3f vs era n(ne/n\')/n(pas)=%.3f' % (n06 / n77, era_ratio)),
    (within(top06[1] / n06, era_top_share_ne, 0.25, 4.0),
     'dominance profile: cipher top follower of 06 is 77 at %.1f%% vs era top follower of "ne" ("%s") at %.1f%% (4x band)'
     % (100 * top06[1] / n06, era_top_ne[0][0], 100 * era_top_share_ne)),
    (len(pre06) >= 12,
     'predecessor diversity: 06 has %d distinct predecessors (era "ne" takes subjects/clause-initials freely)' % len(pre06)),
    (ok_06ce,
     'anchor-follower "ne->ce": cipher 06->87=%d/46 (exp %.2f, thr %.1f) vs era P(ce|ne/n\')=%.4f'
     % (c_06_87, exp_06ce, th_06ce, era_p_ce_ne)),
    (ok_06qu,
     'anchor-follower "ne->que": cipher 06->46=%d/46 (exp %.2f, thr %.1f) vs era P(que|qu\'|ne/n\')=%.5f'
     % (c_06_46, exp_06qu, th_06qu, era_p_que_ne2)),
    (ok_06er,
     'ANOMALY "ne->er": cipher 06->29(er)=%d/46=%.3f (exp %.2f, thr %.1f) vs era P(word-initial "er"|ne/n\')=%.4f — %s'
     % (c_06_29, c_06_29 / n06, exp_06er, th_06er, era_p_er_ne,
        'EXCEEDS count rule: unexplained under 06="ne"' if not ok_06er else 'within rule')),
    (ok_46_06b,
     'negative "que->ne": cipher 46->06=%d/29 (exp %.2f, thr %.1f) vs era P(ne/n\'|que)=%.5f'
     % (c_46_06, exp_4606, th_4606, era_p_ne_que)),
]
v_ne = verdict('H3 06="ne"', checks_ne)

# rivals for 06
log('\n-- rivals for 06 --')
era_p_pas_de = bi('de', 'pas') / cntw('de')
era_p_ce_de = bi('de', 'ce') / cntw('de')
ok_fde, txt_fde = freq_check('06', 'de')
ok_06de_pas, exp_06de_pas, th_06de_pas = count_ok(c_06_77, n06, era_p_pas_de)
ok_06de_ce, exp_06de_ce, th_06de_ce = count_ok(c_06_87, n06, era_p_ce_de)
log('era: P(pas|de)=%.5f P(ce|de)=%.4f' % (era_p_pas_de, era_p_ce_de))
rival_de = [
    (ok_fde, 'RIVAL 06="de": ' + txt_fde),
    (ok_06de_pas,
     'RIVAL 06="de": cipher 06->77=%d/46 (exp %.2f, thr %.1f) as "de->pas" vs era P(pas|de)=%.5f ~0 — ungrammatical'
     % (c_06_77, exp_06de_pas, th_06de_pas, era_p_pas_de),
     True),
    (ok_06de_ce,
     'RIVAL 06="de": cipher 06->87=%d/46 (exp %.2f, thr %.1f) as "de->ce" vs era P(ce|de)=%.4f'
     % (c_06_87, exp_06de_ce, th_06de_ce, era_p_ce_de)),
]
v_rde = verdict('RIVAL 06="de"', rival_de)
era_p_pas_le = bi('le', 'pas') / cntw('le')
ok_fle, txt_fle = freq_check('06', 'le')
ok_06le_pas, exp_06le_pas, th_06le_pas = count_ok(c_06_77, n06, era_p_pas_le)
log('era: P(pas|le)=%.5f' % era_p_pas_le)
rival_le = [
    (ok_fle, 'RIVAL 06="le": ' + txt_fle),
    (ok_06le_pas,
     'RIVAL 06="le": cipher 06->77=%d/46 (exp %.2f, thr %.1f) as "le->pas" vs era P(pas|le)=%.5f ~0 — ungrammatical'
     % (c_06_77, exp_06le_pas, th_06le_pas, era_p_pas_le),
     True),
]
v_rle = verdict('RIVAL 06="le"', rival_le)

# ================= (c) H4: 96 = "par" / "de" =================
log('\n############ (c) H4: 96="par" / 96="de" ############')
n96, r96 = FREQ['96'], frank('96')
fol96, pre96 = nb('96', +1), nb('96', -1)
c_96_87 = fol96['87']; p87_g96 = c_96_87 / n96
pos_96_87_46 = [i for i in range(N - 2)
                if pairs[i] == '96' and pairs[i+1] == '87' and pairs[i+2] == '46']
n_par, n_parce = cntw('par'), cntw('parce')
era_p_parce_par = n_parce / n_par
era_p_que_parce = bi_parce_que() / n_parce
era_p_ce_par = bi('par', 'ce') / n_par
era_p_ce_de2 = bi('de', 'ce') / cntw('de')
era_p_que_dece = tri_de_ce_que() / bi('de', 'ce')
era_p_ce_pour = bi('pour', 'ce') / cntw('pour')
n_a = cntw('a') + cntw('à')
era_p_ce_a = (bi('a', 'ce') + bi('à', 'ce')) / n_a
log('cipher: 96 n=%d rank=%d | 96->87 %d/%d=%.4f | 96-87-46 @%s'
    % (n96, r96, c_96_87, n96, p87_g96, pos_96_87_46))
log('cipher: followers of 96 (top10): %s' % fol96.most_common(10))
log('cipher: predecessors of 96 (top10): %s' % pre96.most_common(10))
log('era: n(parce)=%d n(par)=%d ratio=%.4f | P(que|qu\'|parce)=%.4f | P(ce|par)=%.5f'
    % (n_parce, n_par, era_p_parce_par, era_p_que_parce, era_p_ce_par))
log('era: P(ce|de)=%.4f | P(que|qu\'|"de ce")=%.4f (n=%d) | P(ce|pour)=%.5f | P(ce|a/à)=%.5f'
    % (era_p_ce_de2, era_p_que_dece, bi('de', 'ce'), era_p_ce_pour, era_p_ce_a))

ok_fpar, txt_fpar = freq_check('96', 'par')
ok_fde2, txt_fde2 = freq_check('96', 'de')
ok_96ce_par = within(p87_g96, era_p_parce_par)
ok_96ce_de = within(p87_g96, era_p_ce_de2)
ok_frame_par = within(len(pos_96_87_46) / c_96_87, era_p_que_parce) if c_96_87 else None
ok_frame_de = within(len(pos_96_87_46) / c_96_87, era_p_que_dece) if c_96_87 else None
checks_par = [
    (ok_fpar, txt_fpar),
    (ok_96ce_par,
     '"parce" compound: cipher P(87=ce|96)=%.4f vs era n(parce)/n(par)=%.4f (%d/%d)'
     % (p87_g96, era_p_parce_par, n_parce, n_par)),
    (ok_frame_par,
     '"parce que" frame: cipher P(46=que|96,87)=%d/%d=%.2f vs era P(que|qu\'|parce)=%.4f (n=3, weak)'
     % (len(pos_96_87_46), c_96_87, len(pos_96_87_46) / c_96_87, era_p_que_parce)),
    ((len(pre96) >= 8 and len(fol96) >= 8),
     'function-word diversity: 96 has %d distinct preds / %d distinct followers' % (len(pre96), len(fol96))),
]
v_par = verdict('H4a 96="par"', checks_par)
checks_de = [
    (ok_fde2, txt_fde2),
    (ok_96ce_de,
     '"de ce": cipher P(87=ce|96)=%.4f vs era P(ce|de)=%.4f'
     % (p87_g96, era_p_ce_de2)),
    (ok_frame_de,
     '"de ce que" frame: cipher P(46=que|96,87)=%.2f vs era P(que|qu\'|"de ce")=%.4f (n(de,ce)=%d)'
     % (len(pos_96_87_46) / c_96_87, era_p_que_dece, bi('de', 'ce'))),
    ((len(pre96) >= 8 and len(fol96) >= 8),
     'function-word diversity: 96 has %d distinct preds / %d distinct followers' % (len(pre96), len(fol96))),
]
v_de = verdict('H4b 96="de"', checks_de)

log('\n-- rivals for 96 --')
ok_fpour, txt_fpour = freq_check('96', 'pour')
ok_96ce_pour = within(p87_g96, era_p_ce_pour)
rival_pour = [
    (ok_fpour, 'RIVAL 96="pour": ' + txt_fpour),
    (ok_96ce_pour,
     'RIVAL 96="pour": cipher P(87=ce|96)=%.4f vs era P(ce|pour)=%.5f — "pour ce" rare in formal prose'
     % (p87_g96, era_p_ce_pour)),
]
v_rpour = verdict('RIVAL 96="pour"', rival_pour)
ok_96ce_a = within(p87_g96, era_p_ce_a)
rival_a = [
    (ok_96ce_a,
     'RIVAL 96="a/à": cipher P(87=ce|96)=%.4f vs era P(ce|a/à)=%.5f ~0 — "a ce" ungrammatical'
     % (p87_g96, era_p_ce_a),
     True),
]
v_ra = verdict('RIVAL 96="a/à"', rival_a)

# ================= (d) H4c: 41="der", 08="ni" =================
log('\n############ (d) H4c: 41="der", 08="ni" ############')
n41, r41 = FREQ['41'], frank('41')
n08, r08 = FREQ['08'], frank('08')
fol41, fol08 = nb('41', +1), nb('08', +1)
c_41_08 = fol41['08']; p08_g41 = c_41_08 / n41
occ_41_08 = [i for i in range(N - 1) if pairs[i] == '41' and pairs[i+1] == '08']
occ_5mer = [i for i in occ_41_08 if pairs[i+2:i+5] == ['34', '29', '40']]
era_der_init = sum(1 for w in WORDS if w.startswith('der'))
era_derni_init = sum(1 for w in WORDS if w.startswith('derni'))
era_der_rate = era_der_init / NWORDS
era_p_derni_der = era_derni_init / era_der_init
log('cipher: 41 n=%d rank=%d | 08 n=%d rank=%d' % (n41, r41, n08, r08))
log('cipher: 41-08 @%s (n=%d); full 41-08-34-29-40 "-iere" frame n=%d'
    % (occ_41_08, len(occ_41_08), len(occ_5mer)))
log('cipher: P(08|41)=%d/%d=%.4f | followers of 41: %s | followers of 08: %s'
    % (c_41_08, n41, p08_g41, fol41.most_common(8), fol08.most_common(8)))
log('cipher: context @55-70: %s' % ' '.join(pairs[55:70]))
log('cipher: 41-08 pair rate = %d/%d = %.6f' % (len(occ_41_08), N - 1, len(occ_41_08) / (N - 1)))
log('era: "der*"-initial words=%d (rate %.6f); "derni*"-initial=%d; P(derni|der*)=%.4f'
    % (era_der_init, era_der_rate, era_derni_init, era_p_derni_der))

checks_der = [
    (len(occ_5mer) == 1 and occ_5mer[0] == 59,
     'positional frame (byte-verified): 41-08 @59 immediately left of 34-29-40 ("-iere") @61-63 — the full 41-08-34-29-40 "der-ni-i-er-e" frame; anchors 34=i,29=er,40=e ground the tail'),
    (within(len(occ_41_08) / (N - 1), era_der_rate, 0.25, 4.0),
     'rate band: cipher 41-08 pair rate=%.6f vs era "der*"-initial word rate=%.6f (4x band)'
     % (len(occ_41_08) / (N - 1), era_der_rate)),
    (within(p08_g41, era_p_derni_der),
     'continuation: cipher P(08|41)=%d/%d=%.3f vs era P(word continues "derni"|starts "der")=%.4f — vocabulary-sensitive (Tocqueville der* ~= dernier*; a despatch may use derriere/deranger)'
     % (c_41_08, n41, p08_g41, era_p_derni_der)),
    (None,
     'follower probe (info only, not scored): 08="ni" is a common syllable across many words (19x: venir/tenir/fini/...), so 34 (=i) need not dominate its followers; observed 34 x1 — no inference'),
]
v_der = verdict('H4c 41="der"/08="ni"', checks_der)

log('\n-- rivals for 41/08 --')
rival_ter = [
    (False,
     'RIVAL 41="ter"/08="ni": the @59 frame would read "ter-ni-i-er-e" = "terniere" — not a French word (lexical impossibility)',
     True),
]
v_rter = verdict('RIVAL 41="ter"/08="ni"', rival_ter)
rival_mer = [
    (False,
     'RIVAL 41="mer"/08="ni": the @59 frame would read "mer-ni-i-er-e" = "merniere" — not a French word (lexical impossibility)',
     True),
]
v_rmer = verdict('RIVAL 41="mer"/08="ni"', rival_mer)

with open(os.path.join(HERE, 'hypothesis_sweeper_results.json'), 'w') as f:
    json.dump(RES, f, indent=1, ensure_ascii=False)
log('\n[done] wrote hypothesis_sweeper_results.json')

SUMMARY = {k: {'verdict': v['verdict'], 'passed': v['passed'], 'failed': v['failed']}
           for k, v in RES['hypotheses'].items()}
print(json.dumps(SUMMARY, indent=1))
