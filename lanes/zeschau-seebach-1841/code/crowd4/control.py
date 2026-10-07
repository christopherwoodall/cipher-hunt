"""SEGMENTER round 4 — synthetic control (per pre-registered spec segmenter_control.md).

Builds a synthetic syllabary cipher from Tocqueville text with known word
boundaries, rotation-break structure (A->C->B->A cycle), and ear-cutting noise
(merge/split/alt-spelling). Runs the EXACT crowd3/segmenter.py STRUCT procedure
(unsupervised EM) on the synthetic stream and evaluates M1/M2/M3.

PASS = all three hold; FAIL = stop, no drag.
"""
import collections, json, math, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CROWD = os.path.join(os.path.dirname(HERE), 'crowd')
DATA = os.path.join(os.path.dirname(HERE), '..', 'data')
sys.path.insert(0, CROWD)
from anneal import syllabify_word

RNG = random.Random(20261007)
KMAX = 12
ALPHA = 1.0
Q_BREAK = 0.70   # prob rotation breaks at a true word boundary (jump to R)
Q_MID = 0.04     # prob spurious mid-word rotation break per syllable
P_MERGE = 0.08   # prob two adjacent syllables merge (ear-cutting)
P_SPLIT = 0.04   # prob a syllable splits into two groups
P_ALT = 0.06     # prob alternate spelling of a syllable
CYCLE = {'A': 'C', 'C': 'B', 'B': 'A', 'R': 'A'}  # R resets to A

SPLIT_RE = re.compile(r"[\s'\-\xe2\x80\x93\xe2\x80\x94\xc2\xab\xc2\xbb\".,;:!?()\[\]0-9]+")

def tokenize(path):
    toks = []
    with open(path, encoding='utf-8', errors='replace') as f:
        for line in f:
            for frag in SPLIT_RE.split(line):
                if frag:
                    toks.append(frag.lower())
    return toks

t1 = tokenize(os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'))
t2 = tokenize(os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt'))
SLICE_START, SLICE_END = 50000, 51100   # control slice in t1
slice_words = t1[SLICE_START:SLICE_END]

# ---- era word-length prior, control slice EXCLUDED ----
prior_toks = t1[:SLICE_START] + t1[SLICE_END:] + t2
len_counts = collections.Counter()
n_words = 0
for frag in prior_toks:
    syls = syllabify_word(frag)
    if not syls:
        continue
    n_words += 1
    len_counts[min(len(syls), KMAX)] += 1
tot = sum(len_counts.values())
logP_len = {k: math.log((len_counts.get(k, 0) + 1) / (tot + KMAX))
            for k in range(1, KMAX + 1)}
era_mean = sum(k * len_counts[k] for k in len_counts) / tot
print(f'prior words={n_words} era_mean={era_mean:.3f} (control slice excluded)')

# ---- syllabary: top-96 syllables of the control slice ----
def syls_of(w):
    return syllabify_word(w)

syl_counter = collections.Counter()
slice_syls = []
for w in slice_words:
    s = syls_of(w)
    if not s:
        continue
    slice_syls.append(s)
    syl_counter.update(s)
top96 = [s for s, _ in syl_counter.most_common(96)]
TOPSET = set(top96)
print(f'slice words={len(slice_syls)} distinct_syllables={len(syl_counter)}')

# keep only words fully inside the top-96 inventory
kept = [s for s in slice_syls if all(x in TOPSET for x in s)]
print(f'kept words={len(kept)} ({len(kept)/len(slice_syls):.2%})')

# ---- variant codes: 4 tracks per syllable + on-the-fly pools ----
code_of = {}   # (syllable_string, track) -> code string
_counter = [0]
def code_for(syl, track):
    key = (syl, track)
    if key not in code_of:
        code_of[key] = 'c%04d' % _counter[0]
        _counter[0] += 1
    return code_of[key]

def alt_spelling(syl):
    if syl.endswith('e') and len(syl) > 2:
        return syl[:-1]
    if syl.endswith('s') and len(syl) > 2:
        return syl[:-1]
    return syl + 'e'

# ---- encipher the stream with rotation + ear-cutting noise ----
pairs = []        # synthetic group stream
phases = []       # synthetic track labels (control phase map)
true_bounds = []  # group-level word-boundary positions (ground truth)
cur = 'A'
for wi, s in enumerate(kept):
    s = list(s)
    # ear-cutting: merge
    i = 0
    while i < len(s) - 1:
        if RNG.random() < P_MERGE:
            s[i] = s[i] + s[i + 1]
            del s[i + 1]
        else:
            i += 1
    # ear-cutting: split
    i = 0
    while i < len(s):
        if RNG.random() < P_SPLIT and len(s[i]) >= 4:
            k = len(s[i]) // 2
            s[i:i + 1] = [s[i][:k], s[i][k:]]
            i += 2
        else:
            i += 1
    # ear-cutting: alternate spelling
    s = [alt_spelling(x) if RNG.random() < P_ALT else x for x in s]
    # rotation + tracks
    for k, syl in enumerate(s):
        if k == 0:
            # word-initial: boundary break or cycle continuation
            cur = 'R' if RNG.random() < Q_BREAK else CYCLE[cur]
        else:
            if RNG.random() < Q_MID:
                pairs.append(code_for(syl, 'R'))
                phases.append('R')
                cur = 'R'
                continue
            cur = CYCLE[cur]
        pairs.append(code_for(syl, cur))
        phases.append(cur)
    true_bounds.append(len(pairs))
N = len(pairs)
print(f'synthetic stream: {len(kept)} words, {N} groups, {len(code_of)} distinct codes')

PHASE = {p: ph for p, ph in zip(pairs, phases)}
assert len(set(PHASE.values())) <= 4

def edge(i):
    return PHASE[pairs[i]] + '->' + PHASE[pairs[i + 1]]
ALL_EDGES = ['%s->%s' % (a, b) for a in 'ABCR' for b in 'ABCR']

# ---- STRUCT edge model: unsupervised EM (exact copy of segmenter.py 4a) ----
full = collections.Counter(edge(t) for t in range(N - 1))
rowsum = collections.Counter(edge(t)[0] for t in range(N - 1))
colsum = collections.Counter(edge(t)[3] for t in range(N - 1))
M = {e: (full[e] + ALPHA) / (rowsum[e[0]] + 4 * ALPHA) for e in ALL_EDGES}
Pb = {e: (colsum[e[3]] + ALPHA) / ((N - 1) + 4 * ALPHA) for e in ALL_EDGES}
EPS = 1e-6
from_phase = [PHASE[pairs[t]] for t in range(N - 1)]
row_n = collections.Counter(from_phase)

def em_weights(pi):
    Pw = {}
    for e in ALL_EDGES:
        a = e[0]
        v = (M[e] - pi[a] * Pb[e]) / max(1e-9, 1 - pi[a])
        Pw[e] = max(v, EPS)
    w = {e: math.log(Pw[e] / M[e]) for e in ALL_EDGES}
    s = {e: math.log(Pb[e] / Pw[e]) for e in ALL_EDGES}
    return w, s, Pw

def run(w, s):
    NEG = float('-inf')
    pre = [0.0] * N
    for t in range(N - 1):
        pre[t + 1] = pre[t] + w[edge(t)]
    def word_score(j, i):
        sc = logP_len[min(i - j, KMAX)] + (pre[i - 1] - pre[j])
        if i < N:
            sc += s[edge(i - 1)]
        return sc
    def logsumexp(vals):
        m = max(vals)
        return NEG if m == NEG else m + math.log(sum(math.exp(v - m) for v in vals))
    F = [NEG] * (N + 1)
    F[0] = 0.0
    for i in range(1, N + 1):
        lo = max(0, i - KMAX)
        F[i] = logsumexp([F[j] + word_score(j, i) for j in range(lo, i)])
    Bk = [NEG] * (N + 1)
    Bk[N] = 0.0
    for i in range(N - 1, -1, -1):
        hi = min(N, i + KMAX)
        Bk[i] = logsumexp([word_score(i, j) + Bk[j] for j in range(i + 1, hi + 1)])
    logZ = F[N]
    conf = [0.0] * (N + 1)
    for p in range(1, N):
        conf[p] = math.exp(F[p] + Bk[p] - logZ)
    return conf

pi = {a: 1 - 1 / era_mean for a in 'ABCR'}
for it in range(20):
    w_em, s_em, Pw_em = em_weights(pi)
    conf_em = run(w_em, s_em)
    pi_new = {}
    for a in 'ABCR':
        num = sum(conf_em[t + 1] for t in range(N - 1) if from_phase[t] == a)
        pi_new[a] = num / max(1, row_n[a])
    delta = max(abs(pi_new[a] - pi[a]) for a in 'ABCR')
    pi = {a: 0.5 * pi[a] + 0.5 * pi_new[a] for a in 'ABCR'}
    if delta < 1e-4:
        break
w_struct, s_struct, Pw_struct = em_weights(pi)
conf = run(w_struct, s_struct)

# ---- evaluate M1/M2/M3 vs synthetic ground truth ----
bset = set(true_bounds[:-1])          # final stream end is not a boundary
iset = set(range(1, N)) - bset
M1 = sum(1 for t in bset if conf[t] >= 0.5) / len(bset)
M2 = sum(1 for t in iset if conf[t] < 0.5) / len(iset)
mb = sum(conf[t] for t in bset) / len(bset)
mi = sum(conf[t] for t in iset) / len(iset)
M3 = mb - mi
PASS = (M1 >= 0.60) and (M2 >= 0.70) and (M3 >= 0.10)

s_sorted = sorted(((round(v, 3), e) for e, v in s_struct.items()), reverse=True)

results = {
    'spec': 'code/crowd4/segmenter_control.md',
    'params': {'rng': 20261007, 'q_break': Q_BREAK, 'q_mid': Q_MID,
               'p_merge': P_MERGE, 'p_split': P_SPLIT, 'p_alt': P_ALT,
               'slice': [SLICE_START, SLICE_END], 'n_words': len(kept),
               'n_groups': N, 'n_codes': len(code_of)},
    'prior': {'words': n_words, 'era_mean': round(era_mean, 3),
              'control_slice_excluded': True},
    'em_pi_final': {a: round(pi[a], 4) for a in 'ABCR'},
    's_top_boundary': s_sorted[:6],
    's_top_within': s_sorted[-6:],
    'metrics': {
        'M1_boundary_recall_ge0.5': round(M1, 4), 'M1_n': len(bset),
        'M2_internal_lt0.5': round(M2, 4), 'M2_n': len(iset),
        'M3_mean_diff': round(M3, 4),
        'mean_boundary_conf': round(mb, 4), 'mean_internal_conf': round(mi, 4),
    },
    'thresholds': {'M1': 0.60, 'M2': 0.70, 'M3': 0.10},
    'PASS': PASS,
}
with open(os.path.join(HERE, 'control_results.json'), 'w') as f:
    json.dump(results, f)
print(json.dumps(results['metrics'], indent=1))
print('PASS' if PASS else 'FAIL')
