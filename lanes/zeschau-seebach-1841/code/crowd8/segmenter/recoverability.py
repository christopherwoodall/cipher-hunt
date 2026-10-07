#!/usr/bin/env python3
"""recoverability.py — SEGMENTER round 8, Thread T (PREREG8.md).

Inverts the Geometer's instrument-validity result: the lane's contact-
clustering pipeline is blind to arbitrary columns (ARI~0). A refuge class X
the instrument CANNOT recover from a plaintext syllable stream cannot be
what the cipher's clustering found. Per candidate X (pre-registered):
  1. SIGNATURE: C1-style lag-3 + momentum on the plaintext X-class stream
     (Tocqueville primary; Les Mis register check).
  2. RECOVERABILITY: Jaccard top-10 contact sets + average linkage, k=3 cut,
     ARI vs true X; 200 size-matched random partitions as null.
  3. S2 (secondary): cipher A/B/C 3x3 transition matrix vs corpus X 3x3
     matrix, best-permutation cosine, random-partition calibrated.
Writes recoverability.json."""
import json, os, sys, math, re, random, collections, itertools
import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
DATA = os.path.join(LANE, 'data')
OUT = {}
rng = random.Random(20261007)
np.random.seed(20261007)

# ---------------- syllabifier (copied verbatim from code/crowd/phonotactician.py
#                  via code/crowd7/segmenter/columns_refuge.py) ----------------
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


def syl_parts(syl):
    """-> (onset_tokens, nucleus_str, coda_str) for an orthographic syllable."""
    toks = tokenize(syl)
    vpos = [i for i, t in enumerate(toks) if is_vow(t)]
    if not vpos:
        return toks, '', ''.join(toks)  # lone consonant(s)
    first, last = vpos[0], vpos[-1]
    onset = toks[:first]
    nucleus = ''.join(toks[first:last + 1])
    coda = ''.join(toks[last + 1:])
    return onset, nucleus, coda


# ---------------- candidate class definitions (pre-registered) ----------------
def x1_coda3(syl):
    s = syl.lower()
    lv = max((j for j, ch in enumerate(s) if ch in VOW), default=-1)
    coda = s[lv + 1:]
    if not coda:
        return 'OPEN'
    return 'SON' if coda[-1] in 'nmlr' else 'OBS'


VLESS_FIRST = {'p', 't', 'k', 'qu', 'c', 'ch', 'ph', 'f', 's', 'x'}


def x2_onset(syl):
    onset, _, _ = syl_parts(syl)
    if not onset:
        return 'VINIT'
    return 'VLESS' if onset[0] in VLESS_FIRST else 'VOICED'


NASAL_PAT = ('an', 'en', 'on', 'in', 'un', 'ain', 'ein', 'oin')


def x3_nucleus(syl):
    _, nucleus, coda = syl_parts(syl)
    if not nucleus:
        return 'FRONT'  # lone consonant
    # nasal digraph = vowel(+i)+n/m with no vowel or n/m following in-syllable
    # (orthographic approximation; "anne" correctly excluded via double-n)
    s2 = nucleus + coda
    nasal = False
    for p in NASAL_PAT:
        i = s2.find(p)
        while i != -1:
            rest = s2[i + len(p):]
            if rest == '' or (rest[0] not in VOW and rest[0] not in 'nm'):
                nasal = True
                break
            i = s2.find(p, i + 1)
        if nasal:
            break
    if nasal:
        return 'NASAL'
    if 'ou' in nucleus or 'au' in nucleus or 'eau' in nucleus or \
            'oi' in nucleus or 'o' in nucleus or 'u' in nucleus:
        return 'ROUNDED'
    return 'FRONT'


def x4_shape(syl):
    onset, nucleus, coda = syl_parts(syl)
    if not onset and not coda:
        return 'V'
    if coda or not nucleus:
        return 'CX'
    return 'CV'


CANDIDATES = {
    'X1_coda3': (x1_coda3, ('OPEN', 'SON', 'OBS')),
    'X2_onset': (x2_onset, ('VINIT', 'VLESS', 'VOICED')),
    'X3_nucleus': (x3_nucleus, ('NASAL', 'ROUNDED', 'FRONT')),
    'X4_shape': (x4_shape, ('V', 'CV', 'CX')),
}


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


def load_syllables(paths):
    words = []
    for p in paths:
        words.extend(load_words(p))
    syls = []
    for w in words:
        if len(w) >= 2:
            syls.extend(syllabify(w))
    return words, syls


# ---------------- signature tests (C1 construction, generalized) ----------------
def fit_markov_k(cseq, states):
    si = {s: i for i, s in enumerate(states)}
    k = len(states)
    C = np.zeros((k, k))
    for a, b in zip(cseq, cseq[1:]):
        C[si[a], si[b]] += 1
    M = C / C.sum(axis=1, keepdims=True)
    w, v = np.linalg.eig(M.T)
    pi = np.real(v[:, np.argmin(np.abs(w - 1.0))])
    pi = pi / pi.sum()
    return M, pi


def e1_k(cseq, states):
    n = len(cseq) - 3
    obs = sum(1 for t in range(n) if cseq[t] == cseq[t + 3]) / n
    M, pi = fit_markov_k(cseq, states)
    M3 = np.linalg.matrix_power(M, 3)
    exp = float(sum(pi[s] * M3[s, s] for s in range(len(states))))
    se = math.sqrt(exp * (1 - exp) / n)
    return {'n': n, 'obs': round(obs, 4), 'exp': round(exp, 4),
            'z': round((obs - exp) / se, 2)}


def momentum_k(cseq, states):
    si = {s: i for i, s in enumerate(states)}
    k = len(states)
    C = np.zeros((k, k))
    for a, b in zip(cseq, cseq[1:]):
        C[si[a], si[b]] += 1
    # dominant directed 3-cycle from the data
    best, cyc = -1, None
    for perm in itertools.permutations(range(k), 3):
        a, b, c = perm
        mass = C[a, b] + C[b, c] + C[c, a]
        rev = C[a, c] + C[c, b] + C[b, a]
        if mass - rev > best:
            best, cyc = mass - rev, {a: b, b: c, c: a}
    CYC = cyc
    n1 = n0 = c1 = c0 = 0
    idx = [si[s] for s in cseq]
    for t in range(1, len(idx) - 1):
        a, b, cc = idx[t - 1], idx[t], idx[t + 1]
        if b == CYC[a]:
            n1 += 1
            c1 += (cc == CYC[b])
        elif b != a:
            n0 += 1
            c0 += (cc == CYC[b])
    if n1 == 0 or n0 == 0:
        return {'r1': 0.0, 'n1': n1, 'r0': 0.0, 'n0': n0, 'z': 0.0,
                'p_one_sided': 1.0, 'degenerate': True}
    r1, r0 = c1 / n1, c0 / n0
    p_pool = (c1 + c0) / (n1 + n0)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n0))
    z = (r1 - r0) / se
    p_one = 1 - 0.5 * (1 + math.erf(z / math.sqrt(2)))
    cyc_names = [states[a] for a in sorted(CYC, key=lambda x: 0)]
    return {'r1': round(r1, 4), 'n1': n1, 'r0': round(r0, 4), 'n0': n0,
            'z': round(z, 2), 'p_one_sided': round(p_one, 6)}


# ---------------- ARI ----------------
def ari(labels_true, labels_pred):
    t = np.asarray(labels_true)
    p = np.asarray(labels_pred)
    _, ti = np.unique(t, return_inverse=True)
    _, pi = np.unique(p, return_inverse=True)
    ct = np.zeros((ti.max() + 1, pi.max() + 1))
    for a, b in zip(ti, pi):
        ct[a, b] += 1
    def c2(x):
        return x * (x - 1) / 2
    s = c2(ct).sum()
    sa = c2(ct.sum(axis=1)).sum()
    sb = c2(ct.sum(axis=0)).sum()
    n = len(t)
    expected = sa * sb / c2(n)
    denom = 0.5 * (sa + sb) - expected
    return (s - expected) / denom if denom > 0 else 0.0


# ---------------- corpus load ----------------
TOC = [os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'),
       os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')]
LES = [os.path.join(DATA, 'gutenberg-17489-miserables1.txt')]
print("loading Tocqueville...", flush=True)
toc_words, toc_syls = load_syllables(TOC)
print("loading Les Mis...", flush=True)
les_words, les_syls = load_syllables(LES)
print("toc: %d words %d syllables %d distinct" %
      (len(toc_words), len(toc_syls), len(set(toc_syls))), flush=True)

# ---------------- 1+2. signature + recoverability per X (Tocqueville) ----------------
# contact sets on the syllable stream (mirror rotation_r6.contact_sets, K=10)
print("building contact sets...", flush=True)
inv = sorted(set(toc_syls))
n = len(inv)
si = {s: i for i, s in enumerate(inv)}
foll = [collections.Counter() for _ in range(n)]
pred = [collections.Counter() for _ in range(n)]
for a, b in zip(toc_syls, toc_syls[1:]):
    ia, ib = si[a], si[b]
    foll[ia][ib] += 1
    pred[ib][ia] += 1
TOP = [set(h for h, _ in foll[i].most_common(10)) |
       set(h for h, _ in pred[i].most_common(10)) for i in range(n)]
print("Jaccard matrix (%d items)..." % n, flush=True)
B = np.zeros((n, n), dtype=np.uint8)
for i, s in enumerate(TOP):
    for j in s:
        B[i, j] = 1
Bi = B.astype(np.int32)
inter = Bi @ Bi.T
rs = Bi.sum(axis=1).astype(np.int32)
union = rs[:, None] + rs[None, :] - inter
with np.errstate(divide='ignore', invalid='ignore'):
    sim = np.where(union > 0, inter / union, 0.0)
np.fill_diagonal(sim, 1.0)
dist = 1.0 - sim
print("linkage...", flush=True)
Z = linkage(squareform(dist, checks=False), method='average')
cl3 = fcluster(Z, 3, criterion='maxclust') - 1  # 0-based cluster ids
print("clustering done; cluster sizes:", collections.Counter(cl3), flush=True)

# cipher A/B/C transition matrix (population-level; R-tokens dropped)
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired
pairs, _, _ = load_pairs_repaired()
assert len(pairs) == 1847, len(pairs)
BANKED = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                     'phase_map_repaired.json')))
ABC = ('A', 'B', 'C')
lab_stream = [BANKED[g] for g in pairs]
lab_stream = [l for l in lab_stream if l in ABC]
ai = {l: i for i, l in enumerate(ABC)}
CM = np.zeros((3, 3))
for a, b in zip(lab_stream, lab_stream[1:]):
    CM[ai[a], ai[b]] += 1
CM = CM / CM.sum(axis=1, keepdims=True)


def transmat_3(cseq, states):
    si3 = {s: i for i, s in enumerate(states)}
    M = np.zeros((3, 3))
    for a, b in zip(cseq, cseq[1:]):
        M[si3[a], si3[b]] += 1
    return M / M.sum(axis=1, keepdims=True)


def best_perm_cosine(M1, M2):
    v1 = M1.flatten()
    n1 = np.linalg.norm(v1)
    best = -1
    for perm in itertools.permutations(range(3)):
        v2 = M2[np.ix_(list(perm), list(perm))].flatten()
        c = float(np.dot(v1, v2) / (n1 * np.linalg.norm(v2)))
        best = max(best, c)
    return best


results = {}
for xname, (xfn, states) in CANDIDATES.items():
    print("=== %s ===" % xname, flush=True)
    r = {}
    xs_toc = [xfn(s) for s in toc_syls]
    xs_les = [xfn(s) for s in les_syls]
    dist_t = dict(collections.Counter(xs_toc))
    # 1. signature
    e1 = e1_k(xs_toc, states)
    mo = momentum_k(xs_toc, states)
    e1l = e1_k(xs_les, states)
    mol = momentum_k(xs_les, states)
    r['class_dist_toc'] = dist_t
    r['signature_toc'] = {'lag3': e1, 'momentum': mo}
    r['signature_lesmis'] = {'lag3': e1l, 'momentum': mol}
    lag_ok = e1['z'] > 2.0
    mom_ok = mo['p_one_sided'] < 0.05 and mo['r1'] > mo['r0']
    r['signature_hit_toc'] = bool(lag_ok and mom_ok)
    print("  toc lag3 z=%+.2f  momentum r1=%.4f r0=%.4f z=%+.2f p=%.5f  hit=%s" %
          (e1['z'], mo['r1'], mo['r0'], mo['z'], mo['p_one_sided'],
           r['signature_hit_toc']), flush=True)
    print("  lesmis lag3 z=%+.2f  momentum r1=%.4f r0=%.4f z=%+.2f p=%.5f" %
          (e1l['z'], mol['r1'], mol['r0'], mol['z'], mol['p_one_sided']),
          flush=True)
    # 2. recoverability
    true_lab = np.array([states.index(xfn(s)) for s in inv])
    a = ari(true_lab, cl3)
    sizes = [int((true_lab == i).sum()) for i in range(3)]
    null_aris = np.empty(200)
    for rep in range(200):
        perm = rng.sample(range(n), n)
        rl = np.zeros(n, dtype=int)
        pos = 0
        for ci, sz in enumerate(sizes):
            rl[perm[pos:pos + sz]] = ci
            pos += sz
        null_aris[rep] = ari(rl, cl3)
    p95 = float(np.percentile(null_aris, 95))
    pct = float((null_aris <= a).mean())
    p_emp = float((null_aris >= a).mean())
    r['recoverability'] = {
        'ari': round(float(a), 4),
        'null_mean': round(float(null_aris.mean()), 4),
        'null_p95': round(p95, 4),
        'null_max': round(float(null_aris.max()), 4),
        'percentile': round(pct, 4),
        'p_empirical': round(p_emp, 4),
        'recoverable': bool(a >= p95),
        'class_sizes': sizes,
    }
    print("  ARI=%.4f  null p95=%.4f max=%.4f  pct=%.3f p_emp=%.4f  recoverable=%s" %
          (a, p95, null_aris.max(), pct, p_emp,
           r['recoverability']['recoverable']), flush=True)
    # 3. S2 transition-matrix geometry (secondary) — vectorized null
    Mx = transmat_3(xs_toc, states)
    cosx = best_perm_cosine(CM, Mx)
    sidx = np.array([si[s] for s in toc_syls])  # syllable-index stream
    null_cos = np.empty(200)
    for rep in range(200):
        perm = rng.sample(range(n), n)
        rl = np.zeros(n, dtype=np.int64)
        pos = 0
        for ci, sz in enumerate(sizes):
            rl[perm[pos:pos + sz]] = ci
            pos += sz
        rs_ = rl[sidx]
        prs = rs_[:-1] * 3 + rs_[1:]
        C_ = np.bincount(prs, minlength=9).reshape(3, 3).astype(float)
        Mr = C_ / C_.sum(axis=1, keepdims=True)
        null_cos[rep] = best_perm_cosine(CM, Mr)
    p95c = float(np.percentile(null_cos, 95))
    r['S2'] = {
        'cosine': round(float(cosx), 4),
        'null_p95': round(p95c, 4),
        'percentile': round(float((null_cos <= cosx).mean()), 4),
    }
    print("  S2 cosine=%.4f  null p95=%.4f  pct=%.3f" %
          (cosx, p95c, (null_cos <= cosx).mean()),
          flush=True)
    # verdict
    if r['recoverability']['recoverable'] and r['signature_hit_toc']:
        v = 'LIVE'
    else:
        v = 'DEAD'
    r['verdict'] = v
    print("  VERDICT: %s" % v, flush=True)
    results[xname] = r

OUT['candidates'] = results
OUT['notes'] = {
    'n_syllables_distinct': n,
    'n_syllables_toc': len(toc_syls),
    'contact_K': 10,
    'linkage': 'average',
    'cut': 'k=3',
    'null_reps': 200,
    'bars': 'LIVE iff ARI>=p95(null) AND lag3 z>2 AND momentum p<0.05 r1>r0 (Tocqueville)',
}
json.dump(OUT, open(os.path.join(HERE, 'recoverability.json'), 'w'), indent=1)
print("wrote recoverability.json", flush=True)
