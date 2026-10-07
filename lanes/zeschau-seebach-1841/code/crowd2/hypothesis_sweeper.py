#!/usr/bin/env python3
"""
HYPOTHESIS SWEEPER — Work Order 5.

Tests the remaining open hypotheses (NOTES.md "Open hypotheses" H2, H3, H4),
each against >=2 independent checks, ALL rate checks against the ERA corpus
(Tocqueville 1835/1840, Tomes 1+2 — NOT Les Mis; NOTES.md F10).
For every hypothesis a RIVAL reading is actively sought and scored — no
confirmation-only scorecards (Red-Team lesson, F6).

Hypotheses:
  (a) H2: 77="pas"  (3 LesMis-based checks -> re-validate on era)
  (b) H3: 06="ne"   (3 LesMis-based checks -> re-validate on era)
  (c) H4a: 96="par" | H4b: 96="de" (license 96-87-46 x3 "parce/de ce que";
      test BOTH readings against era bigram rates + pred/follow profiles)
  (d) H4c: 41="der", 08="ni" ("derniere" @59-63)

Method note: the cipher is a syllable stream; the era reference is a word
stream. Word-bigram conditionals are used as the era proxy for syllable
bigram rates (attempt-2/3 convention); where syllable-ish stats are
computable cheaply (word-initial clusters), those are used instead.
Each check records OBS/DER/INF status in prose; the JSON records numbers.

Deterministic. No invented ciphertext or keys. Nulls are first-class.
Output -> code/crowd2/hypothesis_sweeper_results.json
"""
import json, re, collections, os, sys

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

# ---------------- era corpus ----------------
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
RANKED = [w for w, _ in WC.most_common()]
def wrank(w): return RANKED.index(w) + 1 if w in WC else None
def cnt(w): return WC.get(w, 0)
def bicnt(a, b):
    return sum(1 for x, y in zip(WORDS, WORDS[1:]) if x == a and y == b)
def tricnt(a, b, c):
    return sum(1 for x, y, z in zip(WORDS, WORDS[1:], WORDS[2:]) if x == a and y == b and z == c)

# ---------------- cipher ----------------
pairs, _, _ = load_pairs()
N = len(pairs)
FREQ = collections.Counter(pairs)
def frank(g):
    return sorted(FREQ.items(), key=lambda kv: -kv[1]).index((g, FREQ[g])) + 1 \
        if g in FREQ else None
def nb(g, d=+1):
    c = collections.Counter()
    for i, x in enumerate(pairs):
        if x == g:
            j = i + d
            if 0 <= j < N: c[pairs[j]] += 1
    return c

def within(obs, ref, lo=0.5, hi=2.0):
    return ref is not None and ref > 0 and lo * ref <= obs <= hi * ref

def within_zero(obs, ref, k=5):
    """One-sided consistency check for ~zero era rates: passes when the
    cipher rate is at most k x the era rate (both ~absent)."""
    if ref is None:
        return None
    if ref == 0:
        return obs == 0
    return obs <= k * ref

RES = {'hypotheses': {}, 'meta': {
    'pairs': N, 'era_words': NWORDS,
    'note': 'all rate checks vs Tocqueville 1835/1840 (era corpus), word-level proxy'}}

def verdict(name, checks):
    """checks: list of (passed: bool|None, text). None = informational."""
    passed = [c for c in checks if c[0] is True]
    failed = [c for c in checks if c[0] is False]
    info = [c for c in checks if c[0] is None]
    v = 'CONFIRMED' if len(passed) >= 2 and not failed else \
        ('PLAUSIBLE' if len(passed) >= 1 and not failed else
         ('REFUTED' if failed and len(passed) < 2 else 'INCONCLUSIVE'))
    RES['hypotheses'][name] = {'verdict': v,
        'passed': len(passed), 'failed': len(failed),
        'checks': [{'result': 'pass' if p else ('fail' if p is False else 'info'), 'text': t}
                   for p, t in checks]}
    log('== %s: %s (%d pass / %d fail / %d info)' % (name, v, len(passed), len(failed), len(info)))
    for p, t in checks:
        log('   [%s] %s' % ('PASS' if p else ('FAIL' if p is False else 'info'), t))
    return v

# ================= (a) H2: 77 = "pas" =================
log('\n############ (a) H2: 77 = "pas" ############')
n77, r77 = FREQ['77'], frank('77')
n06, r06 = FREQ['06'], frank('06')
fol06 = nb('06', +1); pre77 = nb('77', -1); fol77 = nb('77', +1)
pre06 = nb('06', -1)
c_06_77 = fol06['77']; p77_g06 = c_06_77 / n06
c_67_77 = pre77['67']
c_46_77 = nb('46', +1)['77']; c_46_06 = nb('46', +1)['06']

era_ne, era_pas = cnt('ne'), cnt('pas')
era_ratio = era_ne / era_pas if era_pas else None
era_p_pas_ne = bicnt('ne', 'pas') / era_ne if era_ne else None
era_p_pas_que = bicnt('que', 'pas') / cnt('que') if cnt('que') else None
era_p_ne_que = bicnt('que', 'ne') / cnt('que') if cnt('que') else None
era_p_que_ne = bicnt('ne', 'que') / era_ne if era_ne else None
era_p_plus_ne = bicnt('ne', 'plus') / era_ne if era_ne else None
era_p_ne_pas = bicnt('pas', 'ne') / era_pas if era_pas else None  # swap control

log('cipher: 77 freq=%d rank=%d | 06 freq=%d rank=%d' % (n77, r77, n06, r06))
log('cipher: 06->77 = %d/%d = %.4f | 67->77 = %d/%d = %.4f | 46->77 = %d | 46->06 = %d'
    % (c_06_77, n06, p77_g06, c_67_77, FREQ['67'], c_67_77 / FREQ['67'], c_46_77, c_46_06))
log('era: rank(ne)=%s rank(pas)=%s rank(que)=%s rank(plus)=%s'
    % (wrank('ne'), wrank('pas'), wrank('que'), wrank('plus')))
log('era: n(ne)/n(pas)=%.4f | P(pas|ne)=%.4f | P(pas|que)=%.4f | P(ne|que)=%.4f | P(que|ne)=%.4f | P(plus|ne)=%.4f | P(ne|pas)=%.5f'
    % (era_ratio, era_p_pas_ne, era_p_pas_que, era_p_ne_que, era_p_que_ne, era_p_plus_ne, era_p_ne_pas))
log('era: top-10 followers of "ne": %s'
    % collections.Counter(y for x, y in zip(WORDS, WORDS[1:]) if x == 'ne').most_common(10))
log('cipher: top-10 followers of 06: %s' % fol06.most_common(10))
log('cipher: top-10 predecessors of 77: %s' % pre77.most_common(10))

checks_pas = [
    (within(r77, wrank('pas'), 0.25, 4.0),
     'rank band: cipher rank(77)=%d vs era word rank("pas")=%s (broad 4x band)' % (r77, wrank('pas'))),
    (within(n06 / n77, era_ratio),
     'ratio: 06/77=%.3f vs era n(ne)/n(pas)=%.3f' % (n06 / n77, era_ratio)),
    (within(p77_g06, era_p_pas_ne),
     'bigram: cipher P(77|06)=%.4f vs era P(pas|ne)=%.4f' % (p77_g06, era_p_pas_ne)),
    (within_zero(c_46_77 / FREQ['46'], era_p_pas_que),
     'joint control "que->pas": cipher P(77|46)=%.4f vs era P(pas|que)=%.5f (both ~absent)'
     % (c_46_77 / FREQ['46'], era_p_pas_que or 0)),
    (within(c_46_06 / FREQ['46'], era_p_ne_que) if era_p_ne_que else None,
     'joint control "que->ne": cipher P(06|46)=%.4f vs era P(ne|que)=%.4f'
     % (c_46_06 / FREQ['46'], era_p_ne_que or 0)),
    (None, 'caveat: 67->77 = %d/37 = 16.2%% — "ne"-like predecessor; 67 unidentified (see H2/H3 joint note)'
     % c_67_77),
    (None, 'caveat: 77 heads the r1 repeat 77-78-94-82(m)-06 x2 (linguist H5: "J\'ai l\'honneur de"?) — proper-noun/word-family rival unscored, null as test'),
]
v_pas = verdict('H2 77="pas"', checks_pas)

# rivals for 77
log('\n-- rivals for 77 --')
era_p_que_que = bicnt('que', 'que') / cnt('que')
p77_g46 = c_46_77 / FREQ['46']
r_que_46_consistent = p77_g46 <= max(5 * (era_p_que_que or 0), 0.02)
log('era P(que|que)=%.5f; cipher P(77|46)=%.4f (%d/%d)'
    % (era_p_que_que, p77_g46, c_46_77, FREQ['46']))
rival_que = [
    (within(r77, wrank('que'), 0.25, 4.0),
     'RIVAL 77="que": rank band cipher rank(77)=%d vs era rank("que")=%s' % (r77, wrank('que'))),
    (within(p77_g06, era_p_que_ne),
     'RIVAL 77="que": cipher P(77|06)=%.4f as "ne->que" vs era P(que|ne)=%.4f (restrictive "ne...que" is real in prose)'
     % (p77_g06, era_p_que_ne)),
    (r_que_46_consistent,
     'RIVAL 77="que": cipher P(77|46)=%.4f vs era P(que|que)=%.5f — %s'
     % (p77_g46, era_p_que_que,
        'consistent (no contradiction)' if r_que_46_consistent
        else 'CONTRADICTION: 46=que -> 77 far too often for que->que')),
]
v_rque = verdict('RIVAL 77="que"', rival_que)

rival_plus = [
    (within(r77, wrank('plus'), 0.25, 4.0),
     'RIVAL 77="plus": rank band cipher rank(77)=%d vs era rank("plus")=%s' % (r77, wrank('plus'))),
    (within(p77_g06, era_p_plus_ne),
     'RIVAL 77="plus": cipher P(77|06)=%.4f vs era P(plus|ne)=%.4f' % (p77_g06, era_p_plus_ne)),
]
v_rplus = verdict('RIVAL 77="plus"', rival_plus)

rival_swap = [
    (era_p_ne_pas is not None and (c_06_77 / n77) < 10 * (era_p_ne_pas or 1e-9) and era_p_ne_pas < 0.01,
     'RIVAL 77="ne" (swap with 06): cipher 06->77=%.4f as "pas->ne" vs era P(ne|pas)=%.5f ~0 — ungrammatical, swap REFUTED'
     % (c_06_77 / n77, era_p_ne_pas or 0)),
]
v_rswap = verdict('RIVAL 77="ne"-swap', rival_swap)

# ================= (b) H3: 06 = "ne" =================
log('\n############ (b) H3: 06 = "ne" ############')
era_fol_ne = collections.Counter(y for x, y in zip(WORDS, WORDS[1:]) if x == 'ne').most_common(12)
era_ne_particles = ['pas', 'plus', 'point', 'jamais', 'aucun', 'guere', 'ni', 'nul',
                    'personne', 'rien', 'aucune', 'aucuns']
n_pre06 = len(pre06)
n_fol06 = len(fol06)
top06 = fol06.most_common(1)[0] if fol06 else (None, 0)
era_p_ne_de = bicnt('de', 'ne') / cnt('de') if cnt('de') else None
era_p_pas_de = bicnt('de', 'pas') / cnt('de') if cnt('de') else None
era_p_ce_de = bicnt('de', 'ce') / cnt('de') if cnt('de') else None
c_06_87 = fol06['87']
log('cipher: 06 rank=%d freq=%d | distinct preds=%d followers=%d | top follower=%s x%d'
    % (r06, n06, n_pre06, n_fol06, top06[0], top06[1]))
log('cipher: 06->87(ce) = %d (%.4f) | 06->46(que) = %d' % (c_06_87, c_06_87 / n06, fol06['46']))
log('era: rank(ne)=%s | P(pas|ne)=%.4f | P(ne|pas)=%.5f'
    % (wrank('ne'), era_p_pas_ne, era_p_ne_pas))
log('era followers of "ne" (top12): %s' % era_fol_ne)
log('cipher followers of 06 (top12): %s' % fol06.most_common(12))
log('cipher predecessors of 06 (top12): %s' % pre06.most_common(12))

checks_ne = [
    (within(r06, wrank('ne'), 0.25, 4.0),
     'rank band: cipher rank(06)=%d vs era word rank("ne")=%s (broad 4x band)' % (r06, wrank('ne'))),
    (within(n06 / n77, era_ratio),
     'ratio (shared with H2): 06/77=%.3f vs era n(ne)/n(pas)=%.3f' % (n06 / n77, era_ratio)),
    (within(p77_g06, era_p_pas_ne),
     'bigram: cipher P(77=pas|06)=%.4f vs era P(pas|ne)=%.4f' % (p77_g06, era_p_pas_ne)),
    (top06[0] == '77' and top06[1] / n06 >= 0.08,
     'particle-dominance: top follower of 06 is 77 ("pas") at %.1f%% — era "ne" is followed overwhelmingly by negation particles %s'
     % (100 * top06[1] / n06, [w for w, _ in era_fol_ne[:6]])),
    (n_pre06 >= 12,
     'predecessor diversity: 06 has %d distinct predecessors (era "ne" takes subjects/clause-initials freely)' % n_pre06),
    (within(c_06_87 / n06, era_p_ce_de),
     'era-profile probe: cipher P(87=ce|06)=%.4f vs era P(ce|de)=%.4f — neutral control (de-like vs ne-like follower mix)'
     % (c_06_87 / n06, era_p_ce_de or 0)),
]
v_ne = verdict('H3 06="ne"', checks_ne)

# rivals for 06
log('\n-- rivals for 06 --')
log('era: rank(de)=%s | P(pas|de)=%.5f | P(ne|de)=%.4f | P(ce|de)=%.4f'
    % (wrank('de'), era_p_pas_de or 0, era_p_ne_de or 0, era_p_ce_de or 0))
rival_de = [
    (within(r06, wrank('de'), 0.25, 4.0),
     'RIVAL 06="de": rank band cipher rank(06)=%d vs era rank("de")=%s' % (r06, wrank('de'))),
    (within(p77_g06, era_p_pas_de or 0),
     'RIVAL 06="de": cipher P(77|06)=%.4f as "de->pas" vs era P(pas|de)=%.5f ~0 — ungrammatical'
     % (p77_g06, era_p_pas_de or 0)),
    (within(c_06_87 / n06, era_p_ce_de or 0),
     'RIVAL 06="de": cipher P(87=ce|06)=%.4f vs era P(ce|de)=%.4f'
     % (c_06_87 / n06, era_p_ce_de or 0)),
]
v_rde = verdict('RIVAL 06="de"', rival_de)

era_p_pas_le = bicnt('le', 'pas') / cnt('le') if cnt('le') else None
rival_le = [
    (within(p77_g06, era_p_pas_le or 0),
     'RIVAL 06="le": cipher P(77|06)=%.4f as "le->pas" vs era P(pas|le)=%.5f ~0 — ungrammatical'
     % (p77_g06, era_p_pas_le or 0)),
]
v_rle = verdict('RIVAL 06="le"', rival_le)

# ================= (c) H4: 96 = "par" / "de" =================
log('\n############ (c) H4: 96="par" / 96="de" ############')
n96, r96 = FREQ['96'], frank('96')
fol96 = nb('96', +1); pre96 = nb('96', -1)
c_96_87 = fol96['87']; p87_g96 = c_96_87 / n96
pos_96_87_46 = [i for i in range(N - 2) if pairs[i] == '96' and pairs[i+1] == '87' and pairs[i+2] == '46']
era_parce = cnt('parce'); era_par = cnt('par')
era_p_parce_par = era_parce / era_par if era_par else None
era_p_que_parce = bicnt('parce', 'que') / era_parce if era_parce else None
era_p_ce_par = bicnt('par', 'ce') / era_par if era_par else None
era_p_ce_de = bicnt('de', 'ce') / cnt('de') if cnt('de') else None
era_p_que_dece = tricnt('de', 'ce', 'que') / bicnt('de', 'ce') if bicnt('de', 'ce') else None
era_p_ce_pour = bicnt('pour', 'ce') / cnt('pour') if cnt('pour') else None
era_p_ce_a = sum(1 for x, y in zip(WORDS, WORDS[1:]) if x in ('a', 'à') and y == 'ce') / sum(1 for x in WORDS if x in ('a', 'à'))
log('cipher: 96 freq=%d rank=%d | 96->87 = %d/%d = %.4f | 96-87-46 @%s'
    % (n96, r96, c_96_87, n96, p87_g96, pos_96_87_46))
log('cipher: top-10 followers of 96: %s' % fol96.most_common(10))
log('cipher: top-10 predecessors of 96: %s' % pre96.most_common(10))
log('cipher: distinct preds=%d followers=%d' % (len(pre96), len(fol96)))
log('era: rank(par)=%s rank(de)=%s rank(pour)=%s rank(a/à)=%s'
    % (wrank('par'), wrank('de'), wrank('pour'), wrank('a')))
log('era: n(parce)/n(par)=%.4f (%d/%d) | P(que|parce)=%.4f | P(ce|par)=%.5f'
    % (era_p_parce_par or 0, era_parce, era_par, era_p_que_parce or 0, era_p_ce_par or 0))
log('era: P(ce|de)=%.4f | P(que|"de ce")=%.4f (n=%d) | P(ce|pour)=%.5f | P(ce|a/à)=%.5f'
    % (era_p_ce_de or 0, era_p_que_dece or 0, bicnt('de', 'ce'), era_p_ce_pour or 0, era_p_ce_a or 0))

checks_par = [
    (within(r96, wrank('par'), 0.25, 4.0),
     '"par" rank band: cipher rank(96)=%d vs era rank("par")=%s (broad 4x band)' % (r96, wrank('par'))),
    (within(p87_g96, era_p_parce_par),
     '"parce" compound: cipher P(87=ce|96)=%.4f vs era n(parce)/n(par)=%.4f' % (p87_g96, era_p_parce_par or 0)),
    (within(len(pos_96_87_46) / c_96_87 if c_96_87 else 0, era_p_que_parce),
     '"parce que" frame: cipher P(46=que|96,87)=%d/%d=%.2f vs era P(que|parce)=%.4f'
     % (len(pos_96_87_46), c_96_87, len(pos_96_87_46) / c_96_87 if c_96_87 else 0, era_p_que_parce or 0)),
    (len(pre96) >= 8 and len(fol96) >= 8,
     'function-word diversity: 96 has %d distinct preds / %d distinct followers' % (len(pre96), len(fol96))),
]
v_par = verdict('H4a 96="par"', checks_par)

checks_de = [
    (within(r96, wrank('de'), 0.25, 4.0),
     '"de" rank band: cipher rank(96)=%d vs era rank("de")=%s (broad 4x band)' % (r96, wrank('de'))),
    (within(p87_g96, era_p_ce_de),
     '"de ce": cipher P(87=ce|96)=%.4f vs era P(ce|de)=%.4f' % (p87_g96, era_p_ce_de or 0)),
    (within(len(pos_96_87_46) / c_96_87 if c_96_87 else 0, era_p_que_dece),
     '"de ce que" frame: cipher P(46=que|96,87)=%.2f vs era P(que|"de ce")=%.4f (n=%d)'
     % (len(pos_96_87_46) / c_96_87 if c_96_87 else 0, era_p_que_dece or 0, bicnt('de', 'ce'))),
    (len(pre96) >= 8 and len(fol96) >= 8,
     'function-word diversity: 96 has %d distinct preds / %d distinct followers' % (len(pre96), len(fol96))),
]
v_de = verdict('H4b 96="de"', checks_de)

log('\n-- rivals for 96 --')
rival_pour = [
    (within(r96, wrank('pour'), 0.25, 4.0),
     'RIVAL 96="pour": rank band cipher rank(96)=%d vs era rank("pour")=%s' % (r96, wrank('pour'))),
    (within(p87_g96, era_p_ce_pour or 0),
     'RIVAL 96="pour": cipher P(87=ce|96)=%.4f vs era P(ce|pour)=%.5f ~0 — "pour ce" rare in formal prose'
     % (p87_g96, era_p_ce_pour or 0)),
]
v_rpour = verdict('RIVAL 96="pour"', rival_pour)
rival_a = [
    (within(p87_g96, era_p_ce_a or 0),
     'RIVAL 96="a/à": cipher P(87=ce|96)=%.4f vs era P(ce|a/à)=%.5f ~0 — "a ce" ungrammatical'
     % (p87_g96, era_p_ce_a or 0)),
]
v_ra = verdict('RIVAL 96="a/à"', rival_a)

# ================= (d) H4c: 41="der", 08="ni" =================
log('\n############ (d) H4c: 41="der", 08="ni" ############')
n41, r41 = FREQ['41'], frank('41')
n08, r08 = FREQ['08'], frank('08')
fol41 = nb('41', +1); pre41 = nb('41', -1); fol08 = nb('08', +1)
c_41_08 = fol41['08']; p08_g41 = c_41_08 / n41 if n41 else 0
occ_41_08 = [i for i in range(N - 1) if pairs[i] == '41' and pairs[i+1] == '08']
occ_5mer = [i for i in range(N - 4) if pairs[i:i+5] == ['41','08','34','29','40']]
ctx = pairs[55:70]
era_der_init = sum(1 for w in WORDS if w.startswith('der'))
era_derni_init = sum(1 for w in WORDS if w.startswith('derni'))
era_dernier = sum(1 for w in WORDS if w in ('dernier', 'derniere', 'dernière', 'derniers', 'dernieres', 'dernières'))
era_der_rate = era_der_init / NWORDS
era_p_derni_der = era_derni_init / era_der_init if era_der_init else None
era_ter_init = sum(1 for w in WORDS if w.startswith('ter'))
era_terni_init = sum(1 for w in WORDS if w.startswith('terni'))
era_mer_init = sum(1 for w in WORDS if w.startswith('mer'))
era_merni_init = sum(1 for w in WORDS if w.startswith('merni'))
log('cipher: 41 freq=%d rank=%d | 08 freq=%d rank=%d' % (n41, r41, n08, r08))
log('cipher: 41-08 occurrences @%s (n=%d); 41-08-34-29-40 5-mer @%s (n=%d)'
    % (occ_41_08, len(occ_41_08), occ_5mer, len(occ_5mer)))
log('cipher: P(08|41)=%d/%d=%.4f | followers of 41: %s' % (c_41_08, n41, p08_g41, fol41.most_common(8)))
log('cipher: context @55-70: %s' % ' '.join(ctx))
log('cipher: 41-08 pair rate = %d/%d = %.6f' % (len(occ_41_08), N - 1, len(occ_41_08) / (N - 1)))
log('era: "der*"-initial words = %d (%.6f of words); "derni*"-initial = %d; dernier* forms = %d'
    % (era_der_init, era_der_rate, era_derni_init, era_dernier))
log('era: P(word continues "der"+"ni" | starts "der") = %d/%d = %.4f'
    % (era_derni_init, era_der_init, era_p_derni_der or 0))
log('era rivals: terni/ter = %d/%d | derni... merni/mer = %d/%d'
    % (era_terni_init, era_ter_init, era_merni_init, era_mer_init))

checks_der = [
    (len(occ_5mer) >= 1 and pairs[occ_5mer[0]+2:occ_5mer[0]+5] == ['34','29','40'],
     'positional frame: 41-08 @%s immediately left of 34-29-40 ("-iere") @61-63, forming the full 41-08-34-29-40 "der-ni-i-er-e" frame (anchors: 34=i,29=er,40=e)'
     % (occ_41_08 if occ_41_08 else [])),
    (within(len(occ_41_08) / (N - 1), era_der_rate, 0.25, 4.0),
     'rate band: cipher 41-08 pair rate=%.6f vs era "der*"-initial word rate=%.6f (broad 4x band)'
     % (len(occ_41_08) / (N - 1), era_der_rate)),
]
if n41 >= 5:
    checks_der.append(
        (within(p08_g41, era_p_derni_der),
         'continuation: cipher P(08|41)=%.3f vs era P(word continues "derni" | starts "der")=%.4f'
         % (p08_g41, era_p_derni_der or 0)))
else:
    checks_der.append(
        (None,
         'continuation: n(41)=%d too small to rate P(08|41) (%.2f); era P("derni"|"der*")=%.4f — informational only'
         % (n41, p08_g41, era_p_derni_der or 0)))
v_der = verdict('H4c 41="der"/08="ni"', checks_der)

log('\n-- rivals for 41/08 --')
rival_ter = [
    (within(p08_g41, (era_terni_init / era_ter_init) if era_ter_init else 0),
     'RIVAL 41="ter",08="ni": cipher P(08|41)=%.3f vs era P("terni"|"ter*")=%.4f ~0'
     % (p08_g41, (era_terni_init / era_ter_init) if era_ter_init else 0)),
]
v_rter = verdict('RIVAL 41="ter"/08="ni"', rival_ter)
rival_mer = [
    (within(p08_g41, (era_merni_init / era_mer_init) if era_mer_init else 0),
     'RIVAL 41="mer",08="ni": cipher P(08|41)=%.3f vs era P("merni"|"mer*")=%.4f ~0'
     % (p08_g41, (era_merni_init / era_mer_init) if era_mer_init else 0)),
]
v_rmer = verdict('RIVAL 41="mer"/08="ni"', rival_mer)

with open(os.path.join(HERE, 'hypothesis_sweeper_results.json'), 'w') as f:
    json.dump(RES, f, indent=1, ensure_ascii=False)
log('\n[done] wrote hypothesis_sweeper_results.json')

SUMMARY = {k: {'verdict': v['verdict'], 'passed': v['passed'], 'failed': v['failed']}
           for k, v in RES['hypotheses'].items()}
print(json.dumps(SUMMARY, indent=1))
