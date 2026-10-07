#!/usr/bin/env python3
"""columns_refuge.py — SEGMENTER round 7, Thread C: make the columns refuge
concrete or kill it.

Standing (cited, not re-derived): arbitrary-column form KILLED by the
side-rotation fleet (instrument-validity: contact clustering never recovers
arbitrary columns, ARI~0; no clerk simulation reaches chi2-class strength).

Concretization C0 (stated in PREREG7.md BEFORE testing): 96 cells = 3 columns
x ~32 rows. Columns = CODA-SONORITY class: OPEN / SON-CLOSED / OBS-CLOSED.
Rows ~ onset. Mechanism: French prose syllable streams alternate opens with
codas; contact-coherent homophonic aliasing (F49) preserves the class
sequence at group level.

C1 (decisive): the plaintext coda-class stream must show lag-3 excess (z>2)
AND momentum (r1>r0, p<0.05). Syllabifier copied from
code/crowd/phonotactician.py (credited; module runs corpus code on import so
the functions are copied, not imported).
C2 (consistency only): 16 valued groups -> coda class -> phase x class Fisher
exact MC vs banked phases.
Writes columns_refuge.json."""
import json, os, sys, math, re, random, collections
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
OUT = {}
rng = random.Random(20261007)

# ---------------- syllabifier (copied from code/crowd/phonotactician.py) ----
ACC = str.maketrans({'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'à': 'a', 'â': 'a',
                     'ä': 'a', 'ç': 'c', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o',
                     'û': 'u', 'ü': 'u', 'ù': 'u', 'ÿ': 'y', 'æ': 'ae', 'œ': 'oe'})
VOW = set('aeiouy')
UNIT_ONSET = {'qu', 'ch', 'ph', 'gn'}
ONSET2_OK = set()
for c1 in 'bpcdfgkptv':
    for c2 in 'lr':
        ONSET2_OK.add(c1 + c2)
ONSET2_OK |= {'bl', 'cl', 'gl', 'pl', 'fl', 'vr'}


def tokenize(word):
    toks, i = [], 0
    while i < len(word):
        if word[i:i + 2] in UNIT_ONSET:
            toks.append(word[i:i + 2]); i += 2
        else:
            toks.append(word[i]); i += 1
    return toks


def is_vow(tok):
    return tok in VOW


def legal_onset(cluster):
    n = len(cluster)
    if n == 0:
        return True
    if n == 1:
        return True
    if n == 2:
        return ''.join(cluster) in ONSET2_OK
    if n == 3:
        return cluster[0] == 's' and ''.join(cluster[1:]) in ONSET2_OK
    return False


def split_cluster(cluster):
    for k in (3, 2, 1, 0):
        onset = cluster[len(cluster) - k:]
        if legal_onset(onset):
            return cluster[:len(cluster) - k], onset
    return cluster, []


def syllabify(word):
    toks = tokenize(word)
    vpos = [i for i, t in enumerate(toks) if is_vow(t)]
    if not vpos:
        return [''.join(toks)]
    prev = 0
    syls_tokens = []
    for vi, v in enumerate(vpos):
        cluster = toks[prev:v]
        if vi == 0:
            onset = cluster
        else:
            coda_prev, onset = split_cluster(cluster)
            syls_tokens[-1].extend(coda_prev)
        syl = onset + [toks[v]]
        syls_tokens.append(syl)
        prev = v + 1
    syls_tokens[-1].extend(toks[prev:])
    return [''.join(s) for s in syls_tokens]
# ---------------- end syllabifier copy ----------------


def coda_class(syl):
    """Orthographic coda -> OPEN / SON / OBS. Pre-registered classes.
    Coda = consonant letters after the syllable's LAST vowel."""
    s = syl.lower()
    lv = max((j for j, ch in enumerate(s) if ch in VOW), default=-1)
    coda = s[lv + 1:]
    if not coda:
        return 'OPEN'
    last = coda[-1]
    if last in 'nmlr':
        return 'SON'
    return 'OBS'


def load_words(path):
    text = open(path, encoding='utf-8', errors='replace').read()
    m = re.search(r'\*\*\* start of.*?\*\*\*', text, re.S | re.I)
    if m:
        text = text[m.end():]
    m = re.search(r'\*\*\* end of.*', text, re.S | re.I)
    if m:
        text = text[:m.start()]
    text = text.translate(ACC).lower()
    return re.findall(r'[a-z]+', text)


def class_stream(words):
    out = []
    for w in words:
        if len(w) < 2:
            continue
        for s in syllabify(w):
            out.append(coda_class(s))
    return out


def fit_markov3(cseq):
    S = ('OPEN', 'SON', 'OBS')
    si = {s: i for i, s in enumerate(S)}
    C = np.zeros((3, 3))
    for a, b in zip(cseq, cseq[1:]):
        C[si[a], si[b]] += 1
    M = C / C.sum(axis=1, keepdims=True)
    w, v = np.linalg.eig(M.T)
    pi = np.real(v[:, np.argmin(np.abs(w - 1.0))])
    pi = pi / pi.sum()
    return M, pi


def e1_3(cseq):
    n = len(cseq) - 3
    obs = sum(1 for t in range(n) if cseq[t] == cseq[t + 3]) / n
    M, pi = fit_markov3(cseq)
    M3 = np.linalg.matrix_power(M, 3)
    exp = float(sum(pi[s] * M3[s, s] for s in range(3)))
    se = math.sqrt(exp * (1 - exp) / n)
    return {'n': n, 'obs': round(obs, 4), 'exp': round(exp, 4),
            'z': round((obs - exp) / se, 2)}


def momentum_3(cseq):
    S = ('OPEN', 'SON', 'OBS')
    si = {s: i for i, s in enumerate(S)}
    C = np.zeros((3, 3))
    for a, b in zip(cseq, cseq[1:]):
        C[si[a], si[b]] += 1
    fwd = [(0, 1), (1, 2), (2, 0)]
    rev = [(0, 2), (2, 1), (1, 0)]
    mf = sum(C[a, b] for a, b in fwd)
    mr = sum(C[a, b] for a, b in rev)
    CYC = {0: 1, 1: 2, 2: 0} if mf >= mr else {0: 2, 2: 1, 1: 0}
    n1 = n0 = c1 = c0 = 0
    idx = [si[s] for s in cseq]
    for t in range(1, len(idx) - 1):
        a, b, c_ = idx[t - 1], idx[t], idx[t + 1]
        if b == CYC[a]:
            n1 += 1
            c1 += (c_ == CYC[b])
        elif b != a:
            n0 += 1
            c0 += (c_ == CYC[b])
    r1, r0 = c1 / n1, c0 / n0
    p_pool = (c1 + c0) / (n1 + n0)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n0))
    z = (r1 - r0) / se
    p_one = 1 - 0.5 * (1 + math.erf(z / math.sqrt(2)))
    return {'cycle': 'OPEN->SON->OBS->OPEN' if mf >= mr else 'OPEN->OBS->SON->OPEN',
            'r1': round(r1, 4), 'n1': n1, 'r0': round(r0, 4), 'n0': n0,
            'z': round(z, 2), 'p_one_sided': round(p_one, 6)}


# ---- C1: corpus tests ----
DATA = os.path.join(LANE, 'data')
corpora = {
    'tocqueville': [os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'),
                    os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')],
    'lesmis': [os.path.join(DATA, 'gutenberg-17489-miserables1.txt')],
}
c1 = {}
for name, paths in corpora.items():
    words = []
    for p in paths:
        words.extend(load_words(p))
    cs = class_stream(words)
    dist = dict(collections.Counter(cs))
    e1 = e1_3(cs)
    mo = momentum_3(cs)
    c1[name] = {'n_words': len(words), 'n_syllables': len(cs),
                'class_dist': dist, 'lag3': e1, 'momentum': mo}
    print("%s: words=%d syllables=%d dist=%s" %
          (name, len(words), len(cs), dist))
    print("  lag-3: obs=%.4f exp=%.4f z=%+.2f" % (e1['obs'], e1['exp'], e1['z']))
    print("  momentum %s: r1=%.4f (n=%d) r0=%.4f (n=%d) z=%+.2f p=%.6f" %
          (mo['cycle'], mo['r1'], mo['n1'], mo['r0'], mo['n0'],
           mo['z'], mo['p_one_sided']))
OUT['C1_corpus'] = c1

# C1 verdict (pre-registered bars on the PRIMARY corpus = tocqueville)
t = c1['tocqueville']
lag_ok = t['lag3']['z'] > 2.0
mom_ok = t['momentum']['p_one_sided'] < 0.05 and t['momentum']['r1'] > t['momentum']['r0']
if lag_ok and mom_ok:
    c1v = 'CONCRETE'
elif abs(t['lag3']['z']) <= 2.0 and t['momentum']['p_one_sided'] >= 0.05:
    c1v = 'WEAKENED'
else:
    c1v = 'INCONCLUSIVE'
OUT['C1_verdict'] = {'verdict': c1v, 'lag3_z_gt_2': bool(lag_ok),
                     'momentum_hit': bool(mom_ok)}
print("C1 verdict:", c1v)

# ---- C2: anchor probe (consistency only) ----
BANKED = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                     'phase_map_repaired.json')))
# (group, value, orthographic coda class, status note)
anchors = [
    ('11', 'la', 'OPEN', 'GT'), ('70', 'pre', 'OPEN', 'GT'),
    ('82', 'm', 'SON', 'GT lone-consonant edge'), ('34', 'i', 'OPEN', 'GT'),
    ('29', 'er', 'SON', 'GT'), ('40', 'e', 'OPEN', 'GT'),
    ('46', 'que', 'OPEN', 'GT'), ('87', 'ce', 'OPEN', 'provisional'),
    ('64', 'qui', 'OPEN', 'provisional'), ('96', 'par', 'SON', 'provisional'),
    ('77', 'le', 'OPEN', 'provisional-conditioned'), ('59', 'est', 'OBS', 'STRONG LEAD'),
    ('00', 'pour', 'SON', 'STRONG LEAD'), ('16', 'i', 'OPEN', 'LEAD'),
    ('78', 'me', 'OPEN', 'LEAD F51-conditional'), ('62', 'on', 'SON', 'STRONG LEAD ear-only'),
]
rows = [(BANKED[g], cc) for g, _, cc, _ in anchors]
phases = ('A', 'B', 'C', 'R')
classes = ('OPEN', 'SON', 'OBS')
pi_ = {p: i for i, p in enumerate(phases)}
ci_ = {c: i for i, c in enumerate(classes)}
T = np.zeros((4, 3))
for p, c in rows:
    T[pi_[p], ci_[c]] += 1
row_sum = T.sum(axis=1, keepdims=True)
col_sum = T.sum(axis=0, keepdims=True)
E = row_sum @ col_sum / T.sum()
chi2_obs = float(((T - E) ** 2 / np.where(E > 0, E, 1)).sum())
# Monte Carlo: permute class labels, fix margins
cnt = 0
NPERM = 10000
cls = [c for _, c in rows]
for _ in range(NPERM):
    rng.shuffle(cls)
    Tp = np.zeros((4, 3))
    for (p, _), c in zip(rows, cls):
        Tp[pi_[p], ci_[c]] += 1
    chi2_p = float(((Tp - E) ** 2 / np.where(E > 0, E, 1)).sum())
    cnt += (chi2_p >= chi2_obs)
p_mc = cnt / NPERM
OUT['C2_anchor_probe'] = {
    'n': len(rows),
    'contingency': {p: {c: int(T[pi_[p], ci_[c]]) for c in classes} for p in phases},
    'chi2_obs': round(chi2_obs, 3),
    'p_mc_10k': round(p_mc, 4),
    'rows': [{'group': g, 'value': v, 'coda': cc, 'phase': BANKED[g], 'note': n}
             for g, v, cc, n in anchors],
}
print("\nC2 anchor probe: n=%d chi2=%.3f p_mc=%.4f" % (len(rows), chi2_obs, p_mc))
print("contingency (phase x class):")
for p in phases:
    print("  %s: %s" % (p, {c: int(T[pi_[p], ci_[c]]) for c in classes}))
c2v = 'consistent-with (weak support)' if p_mc < 0.05 else 'inconclusive'
OUT['C2_verdict'] = c2v
print("C2 verdict:", c2v)

# ---- overall Thread C verdict ----
if c1v == 'CONCRETE':
    overall = ('CONCRETE — coda-sonority columns survive as a live refuge: the '
               'plaintext coda-class stream carries both the lag-3 rhythm and '
               'momentum; mechanism demonstrated in the plaintext domain.')
elif c1v == 'WEAKENED':
    overall = ('WEAKENED — French prose coda-class streams do NOT carry the '
               'rhythm/momentum package; columns=coda-class survives only via '
               'register/cut-mismatch escape hatches. Full kill needs key recovery '
               '(phase-perp-coda-class at n>>).')
else:
    overall = ('INCONCLUSIVE — mixed corpus signals; refuge neither concretized '
               'nor weakened.')
OUT['threadC_verdict'] = overall
print("\nThread C verdict:", overall)
json.dump(OUT, open(os.path.join(HERE, 'columns_refuge.json'), 'w'), indent=1)
print("wrote columns_refuge.json")
