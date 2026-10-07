"""SEGMENTER (round 3, crowd3) — word-boundary hypothesis over the 1,846-pair stream.

Semi-Markov forward-backward. For a word spanning pairs j..i-1 (k=i-j groups):

  score(j->i) = logP_len(k)                       [S2: era word-length prior]
              + sum_{t=j}^{i-1} w(edge_t)         [within-edge weight]
              + s(edge_{i-1})   (if i<N)          [rotation-break bonus on
                                                   the word-final edge]

Signals:
  S1-STRUCT (PRIMARY, unsupervised): w(e)=log(M(e)*16), s(e)=log(Pb(e)/M(e)),
      M = full-stream block-transition matrix (Laplace-smoothed per row),
      Pb(a->b) = column marginal of b ("boundary resets the phase").
      Rotation-following edges get negative s (within-favoring);
      rotation-violating edges get positive s. NO anchor data touches S1.
  S1-ANCHOR (comparison only): same form with pw/pb from anchor-word
      instances (in-sample; overfit-prone). FULL = all three anchor words,
      STRICT = ground-truth word only.
  S2: P(#syllables) from Tocqueville 1835/1840 (R1 maximal-onset,
      SPLIT_RE tokens, Laplace-smoothed), KMAX=12.
  S3 (control): prior only (w=0, s=0).

Anchor-word spans (linguistically correct multi-word reads):
  "la premiere"  = "la"@(1033,1034) + "premiere"@(1034,1039)   [ground truth]
  "cela"         = (i,i+2) x7  [provisional 87=ce; "ce la" alternative noted]
  "parce" + "que"= (i,i+2)+(i+2,i+3) x3  [provisional 96=par,87=ce]

Validation is FULLY OUT-OF-SAMPLE for PRIMARY (anchors used only to score).
For S1-ANCHOR variants validation is in-sample (stated).

Caveats carried: tuner NULL verdict (phase != word-position class) — the
model assumes only that boundaries *break* the rotation, never that a phase
labels a word position. "cela"/"parce" reads are provisional.
"""
import collections, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CROWD = os.path.join(os.path.dirname(HERE), 'crowd')
DATA = os.path.join(os.path.dirname(HERE), '..', 'data')
sys.path.insert(0, CROWD)
sys.path.insert(0, os.path.dirname(HERE))
from crib_attack import load_pairs
from anneal import syllabify_word as syllabify_R1

KMAX = 12
ALPHA = 1.0

# ---------------- 1. pair stream ----------------
pairs, odd_lines, off1 = load_pairs()
N = len(pairs)
assert N == 1846, N
freq = collections.Counter(pairs)
assert len(freq) == 96, len(freq)

# ---------------- 2. phase map (re-derived from contactor k=12 cut) ----------------
cj = json.load(open(os.path.join(CROWD, 'contactor_results.json')))
cs12 = cj['jaccard_clusters']['12']
A_, B_, C_ = (set(x['members']) for x in cs12[:3])
REST = set().union(*[set(x['members']) for x in cs12[3:]])
PHASE = {}
for g in A_: PHASE[g] = 'A'
for g in B_: PHASE[g] = 'B'
for g in C_: PHASE[g] = 'C'
for g in REST: PHASE[g] = 'R'
assert len(PHASE) == 96
assert PHASE['11'] == 'A' and PHASE['70'] == 'A' and PHASE['82'] == 'B'
assert PHASE['29'] == 'C' and PHASE['96'] == 'C' and PHASE['87'] == 'B'

def edge(i):
    return PHASE[pairs[i]] + '->' + PHASE[pairs[i + 1]]

ALL_EDGES = ['%s->%s' % (a, b) for a in 'ABCR' for b in 'ABCR']

# ---------------- 3. anchor-word spans ----------------
# spans: list of (start_pair, end_pair_exclusive) word spans
cela_pos = [i for i in range(N - 1) if pairs[i] == '87' and pairs[i + 1] == '11']
pce_pos = [i for i in range(N - 2)
           if pairs[i] == '96' and pairs[i + 1] == '87' and pairs[i + 2] == '46']
assert pairs[1033:1039] == ['11', '70', '82', '34', '29', '40']
SPANS = {
    'la_premiere': {'spans': [(1033, 1034), (1034, 1039)], 'status': 'ground-truth'},
    'cela':        {'spans': [(i, i + 2) for i in cela_pos], 'status': 'provisional'},
    'parce_que':   {'spans': [(i, i + 2) for i in pce_pos] +
                             [(i + 2, i + 3) for i in pce_pos],
                    'status': 'provisional'},
}
assert len(cela_pos) == 7 and len(pce_pos) == 3

def anchor_edge_samples(wordset):
    """within: Counter of edges strictly inside spans;
       boundary: Counter of edges crossing a span edge (deduped by position)."""
    within, bpos = collections.Counter(), set()
    for w in wordset:
        for (s, e) in SPANS[w]['spans']:
            for t in range(s, e - 1):
                within[PHASE[pairs[t]] + '->' + PHASE[pairs[t + 1]]] += 1
            if s > 0:
                bpos.add(s - 1)          # edge s-1 -> s enters the word
            if e < N:
                bpos.add(e - 1)          # edge e-1 -> e leaves the word
    boundary = collections.Counter(edge(t) for t in bpos)
    return within, boundary

# ---------------- 4. edge models ----------------
# 4a. STRUCTURAL-EM (primary, unsupervised): decontaminate the mixture.
#   M(b|a)   = (1-pi_a) * P_within(b|a) + pi_a * Pb(b)   (per row a)
#   Pb(b)    = column marginal ("boundary resets the phase")
#   pi_a     = P(edge is boundary | from-phase a), fit by EM on the
#              forward-backward posteriors (damped, 20 iters max).
#   w(e)     = log(P_within(e)/M(e))   (background = mixture)
#   s(e)     = log(Pb(e)/P_within(e))  (rotation-break bonus)
full = collections.Counter(edge(t) for t in range(N - 1))
rowsum = collections.Counter(edge(t)[0] for t in range(N - 1))
colsum = collections.Counter(edge(t)[3] for t in range(N - 1))
M, Pb = {}, {}
for e in ALL_EDGES:
    a, b = e[0], e[3]
    M[e] = (full[e] + ALPHA) / (rowsum[a] + 4 * ALPHA)
    Pb[e] = (colsum[b] + ALPHA) / ((N - 1) + 4 * ALPHA)
EPS = 1e-6
from_phase = [PHASE[pairs[t]] for t in range(N - 1)]  # edge t leaves phase[t]
row_n = collections.Counter(a for a in from_phase)

def em_weights(pi):
    Pw = {}
    for e in ALL_EDGES:
        a = e[0]
        v = (M[e] - pi[a] * Pb[e]) / max(1e-9, 1 - pi[a])
        Pw[e] = max(v, EPS)
    w = {e: math.log(Pw[e] / M[e]) for e in ALL_EDGES}
    s = {e: math.log(Pb[e] / Pw[e]) for e in ALL_EDGES}
    return w, s, Pw

# run() is defined in section 6; EM loop runs after it (see below).

# 4b. ANCHOR-trained (comparison; in-sample)
def anchor_model(wordset):
    within, boundary = anchor_edge_samples(wordset)
    nw, nb = sum(within.values()), sum(boundary.values())
    w, s = {}, {}
    for e in ALL_EDGES:
        pw = (within[e] + ALPHA) / (nw + 16 * ALPHA)
        pb = (boundary[e] + ALPHA) / (nb + 16 * ALPHA)
        w[e] = math.log(pw * 16)
        s[e] = math.log(pb / pw)
    return w, s, within, boundary, nw, nb

w_full, s_full, within_full, boundary_full, NW_F, NB_F = anchor_model(
    ['la_premiere', 'cela', 'parce_que'])
w_strict, s_strict, within_strict, boundary_strict, NW_S, NB_S = anchor_model(
    ['la_premiere'])

w_zero = {e: 0.0 for e in ALL_EDGES}
s_zero = {e: 0.0 for e in ALL_EDGES}

# ---------------- 5. era word-length prior ----------------
SPLIT_RE = re.compile(r"[\s'\-\xe2\x80\x93\xe2\x80\x94\xc2\xab\xc2\xbb\".,;:!?()\[\]0-9]+")
corpus_paths = [os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'),
                os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')]
len_counts = collections.Counter()
n_words = 0
for path in corpus_paths:
    with open(path, encoding='utf-8', errors='replace') as f:
        for line in f:
            for frag in SPLIT_RE.split(line):
                if not frag:
                    continue
                syls = syllabify_R1(frag)
                if not syls:
                    continue
                n_words += 1
                len_counts[min(len(syls), KMAX)] += 1
assert n_words > 200000, n_words
tot = sum(len_counts.values())
logP_len = {k: math.log((len_counts.get(k, 0) + 1) / (tot + KMAX))
            for k in range(1, KMAX + 1)}
era_mean = sum(k * len_counts[k] for k in len_counts) / tot

# ---------------- 6. forward-backward + viterbi ----------------
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
    V = [NEG] * (N + 1)
    back = [0] * (N + 1)
    V[0] = 0.0
    for i in range(1, N + 1):
        lo = max(0, i - KMAX)
        best, bj = NEG, lo
        for j in range(lo, i):
            sc = V[j] + word_score(j, i)
            if sc > best:
                best, bj = sc, j
        V[i], back[i] = best, bj
    bounds, i = [], N
    while i > 0:
        bounds.append(i)
        i = back[i]
    bounds.append(0)
    bounds.reverse()
    return conf, bounds

# EM for the structural model: iterate pi_a (per-row boundary rate).
pi = {a: 1 - 1 / era_mean for a in 'ABCR'}   # init from era mean word length
em_traj = []
for it in range(20):
    w_em, s_em, Pw_em = em_weights(pi)
    conf_em, vit_em = run(w_em, s_em)
    pi_new = {}
    for a in 'ABCR':
        num = sum(conf_em[t + 1] for t in range(N - 1) if from_phase[t] == a)
        pi_new[a] = num / max(1, row_n[a])
    em_traj.append({a: round(pi_new[a], 4) for a in 'ABCR'})
    delta = max(abs(pi_new[a] - pi[a]) for a in 'ABCR')
    pi = {a: 0.5 * pi[a] + 0.5 * pi_new[a] for a in 'ABCR'}  # damped
    if delta < 1e-4:
        break
w_struct, s_struct, Pw_struct = em_weights(pi)
conf_struct, vit_struct = run(w_struct, s_struct)
em_iters = len(em_traj)

conf_full, vit_full = run(w_full, s_full)
conf_strict, vit_strict = run(w_strict, s_strict)
conf_prior, vit_prior = run(w_zero, s_zero)

# ---------------- 7. validation (out-of-sample for STRUCT) ----------------
def validation_sets(wordset):
    bset, iset = set(), set()
    for w in wordset:
        for (s, e) in SPANS[w]['spans']:
            if s > 0:
                bset.add(s)
            if e < N:
                bset.add(e)
            for t in range(s + 1, e):
                iset.add(t)
    return bset, iset

def validate(conf, label, wordset):
    bset, iset = validation_sets(wordset)
    bb = sorted((t, conf[t]) for t in bset)
    bi = sorted((t, conf[t]) for t in iset)
    return {
        'label': label,
        'n_boundary': len(bb), 'n_internal': len(bi),
        'mean_conf_boundary': sum(c for _, c in bb) / len(bb),
        'mean_conf_internal': sum(c for _, c in bi) / len(bi),
        'boundary_ge_0.5': sum(1 for _, c in bb if c >= 0.5),
        'internal_lt_0.5': sum(1 for _, c in bi if c < 0.5),
        'boundary_detail': [(t, round(c, 3)) for t, c in bb],
        'internal_detail': [(t, round(c, 3)) for t, c in bi],
    }

GT = ['la_premiere']
ALLW = ['la_premiere', 'cela', 'parce_que']
val_struct_gt = validate(conf_struct, 'STRUCT vs ground-truth spans', GT)
val_struct_all = validate(conf_struct, 'STRUCT vs all anchor spans', ALLW)
val_full_all = validate(conf_full, 'ANCHOR-FULL (in-sample)', ALLW)
val_strict_gt = validate(conf_strict, 'ANCHOR-STRICT (in-sample)', GT)
val_prior_all = validate(conf_prior, 'PRIOR-ONLY', ALLW)

# ---------------- 8. implied word-length distribution (MAP) ----------------
def wordlen_stats(bounds):
    lens = [bounds[i + 1] - bounds[i] for i in range(len(bounds) - 1)]
    c = collections.Counter(lens)
    n = len(lens)
    exp = {k: n * (len_counts.get(k, 0) + 1) / (tot + KMAX) for k in range(1, KMAX + 1)}
    chi2 = sum((c.get(k, 0) - exp[k]) ** 2 / exp[k] for k in range(1, KMAX + 1))
    return {'n_words': n, 'mean': round(sum(lens) / n, 3),
            'median': sorted(lens)[n // 2],
            'dist': {str(k): c.get(k, 0) for k in range(1, KMAX + 1)},
            'chi2_vs_era': round(chi2, 1)}

stats_struct = wordlen_stats(vit_struct)
stats_full = wordlen_stats(vit_full)
stats_strict = wordlen_stats(vit_strict)
stats_prior = wordlen_stats(vit_prior)

# ---------------- 9. la premiere checkpoint ----------------
chk = {
    'context_pairs_1028_1043': pairs[1028:1044],
    'boundary_in_1033': round(conf_struct[1033], 4),
    'boundary_la_premiere_1034': round(conf_struct[1034], 4),
    'internal_premiere_1035_1038': [round(conf_struct[t], 4) for t in range(1035, 1039)],
    'boundary_out_1039': round(conf_struct[1039], 4),
}

# ---------------- 10. crib-drag targets (PRIMARY MAP) ----------------
READ = {'11', '70', '82', '34', '29', '40', '87', '64', '96', '46'}
known = set()
for w in ALLW:
    for (s, e) in SPANS[w]['spans']:
        known.add((s, e))

def targets(bounds, conf):
    out = []
    for bi in range(len(bounds) - 1):
        j, i = bounds[bi], bounds[bi + 1]
        k = i - j
        if k < 2 or (j, i) in known:
            continue
        gs = pairs[j:i]
        if any(g in READ for g in gs):
            continue
        flank = (conf[j] if j > 0 else 1.0, conf[i] if i < N else 1.0)
        inner = max([conf[t] for t in range(j + 1, i)], default=0.0)
        out.append({'start_pair': j, 'end_pair': i - 1, 'n_groups': k,
                    'groups': gs, 'phases': ''.join(PHASE[g] for g in gs),
                    'flank_conf': [round(x, 3) for x in flank],
                    'max_inner_conf': round(inner, 3),
                    'score': round(min(flank) * (1 - inner), 4)})
    out.sort(key=lambda d: -d['score'])
    return out

targets_struct = targets(vit_struct, conf_struct)

results = {
    'counts_verified': {
        'pairs': N, 'distinct_groups': len(freq), 'odd_lines': odd_lines,
        'off1': off1, 'phase_map': {'A': len(A_), 'B': len(B_), 'C': len(C_),
                                    'R': len(REST)},
        'era_corpus_words': n_words,
        'cela_instances': len(cela_pos), 'cela_at': cela_pos,
        'parceque_instances': len(pce_pos), 'parceque_at': pce_pos,
    },
    'era_wordlen_prior': {
        'dist': {str(k): len_counts.get(k, 0) for k in range(1, KMAX + 1)},
        'mean': round(era_mean, 3),
        'rule': 'R1 maximal-onset (crowd/anneal.py), SPLIT_RE tokens, Laplace-smoothed',
    },
    'struct_edge_model': {
        'transition_matrix_rowsum': {a: rowsum[a] for a in 'ABCR'},
        'rotation_enrichment_M_over_Pb': {
            e: round(M[e] / Pb[e], 3) for e in
            ['A->C', 'C->B', 'B->A', 'A->A', 'B->B', 'C->C']},
        'em_iters': em_iters,
        'em_pi_trajectory': em_traj,
        'em_pi_final': {a: round(pi[a], 4) for a in 'ABCR'},
        'P_within_sample': {e: round(Pw_struct[e], 4) for e in
                            ['A->C', 'C->B', 'B->A', 'A->A', 'B->B', 'C->C',
                             'C->A', 'B->C', 'A->B']},
        's_top_boundary': sorted(((round(v, 3), e) for e, v in s_struct.items()),
                                 reverse=True)[:6],
        's_top_within': sorted(((round(v, 3), e) for e, v in s_struct.items()))[:6],
    },
    'anchor_edge_model': {
        'FULL_within_n': NW_F, 'FULL_boundary_n': NB_F,
        'STRICT_within_n': NW_S, 'STRICT_boundary_n': NB_S,
        'FULL_within': dict(within_full), 'FULL_boundary': dict(boundary_full),
    },
    'validation': {
        'STRUCT_gt': val_struct_gt, 'STRUCT_all': val_struct_all,
        'ANCHOR_FULL': val_full_all, 'ANCHOR_STRICT': val_strict_gt,
        'PRIOR_ONLY': val_prior_all,
    },
    'la_premiere_checkpoint': chk,
    'implied_wordlen': {'STRUCT_MAP': stats_struct, 'ANCHOR_FULL_MAP': stats_full,
                        'ANCHOR_STRICT_MAP': stats_strict, 'PRIOR_ONLY_MAP': stats_prior},
    'boundary_confidence_STRUCT': [round(conf_struct[p], 4) for p in range(1, N)],
    'viterbi_bounds_STRUCT': vit_struct,
    'crib_drag_targets_STRUCT': targets_struct[:25],
    'method_caveats': [
        'STRUCT edge signal is unsupervised (full-stream matrix); validation on anchors is out-of-sample.',
        'ANCHOR-trained variants are in-sample on the validation spans (circular); shown for comparison only.',
        '"cela" could be two words "ce la"; "parce"+"que" split assumed from the provisional reads.',
        'Phase=word-position labeling NOT assumed (tuner NULL verdict holds); only rotation-break is used.',
        'Word-length prior is orthographic Tocqueville French; cipher syllabary uncalibrated vs it.',
    ],
}
with open(os.path.join(HERE, 'segmenter_results.json'), 'w') as f:
    json.dump(results, f)

md = []
A = md.append
A('# SEGMENTER — word-boundary hypothesis (round 3, crowd3)\n')
A('Semi-Markov forward-backward. score(j->i) = logP_len(k) + sum within-edge '
  'weights + rotation-break bonus on the word-final edge.\n')
cv = results['counts_verified']
A(f"Counts: {cv['pairs']} pairs / {cv['distinct_groups']} groups; era corpus "
  f"{cv['era_corpus_words']} words (mean {results['era_wordlen_prior']['mean']} "
  f"syll/word); cela x{cv['cela_instances']}, parce-que x{cv['parceque_instances']}.\n")
A('## Rotation-break edge signal (STRUCT, unsupervised)')
for v, e in results['struct_edge_model']['s_top_boundary']:
    A(f'- {e}: s={v:+.2f} (boundary-favoring)')
A('...')
for v, e in results['struct_edge_model']['s_top_within']:
    A(f'- {e}: s={v:+.2f} (within-favoring)')
A('\n## Validation: boundary precision on anchor spans')
for key in ('STRUCT_gt', 'STRUCT_all', 'ANCHOR_FULL', 'ANCHOR_STRICT', 'PRIOR_ONLY'):
    v = results['validation'][key]
    A(f"- {v['label']}: boundary {v['boundary_ge_0.5']}/{v['n_boundary']}>=0.5 "
      f"(mean {v['mean_conf_boundary']:.3f}); internal {v['internal_lt_0.5']}/"
      f"{v['n_internal']}<0.5 (mean {v['mean_conf_internal']:.3f})")
A('\n## la premiere checkpoint @1033 (STRUCT)')
A(f"- in @1033: {chk['boundary_in_1033']}, la|premiere @1034: "
  f"{chk['boundary_la_premiere_1034']}")
A(f"- premiere internals @1035-1038: {chk['internal_premiere_1035_1038']}")
A(f"- out @1039: {chk['boundary_out_1039']}")
A('\n## Implied word-length distribution (MAP) vs era')
ep = results['era_wordlen_prior']
A(f"- era: mean {ep['mean']}, dist(1..6)={[ep['dist'][str(k)] for k in range(1, 7)]}")
for key in ('STRUCT_MAP', 'ANCHOR_FULL_MAP', 'ANCHOR_STRICT_MAP', 'PRIOR_ONLY_MAP'):
    s = results['implied_wordlen'][key]
    A(f"- {key}: n={s['n_words']}, mean {s['mean']}, median {s['median']}, "
      f"chi2 {s['chi2_vs_era']}, dist(1..6)={[s['dist'][str(k)] for k in range(1, 7)]}")
A('\n## Top unread high-confidence words (STRUCT MAP — crib-drag targets)')
for t in targets_struct[:12]:
    A(f"- @{t['start_pair']}-{t['end_pair']} ({t['n_groups']}g): "
      f"{' '.join(t['groups'])} [{t['phases']}] flank={t['flank_conf']} "
      f"inner={t['max_inner_conf']} score={t['score']}")
with open(os.path.join(HERE, 'segmenter_results.md'), 'w') as f:
    f.write('\n'.join(md) + '\n')
print('OK')
for key in ('STRUCT_gt', 'STRUCT_all', 'ANCHOR_FULL', 'ANCHOR_STRICT', 'PRIOR_ONLY'):
    v = results['validation'][key]
    print(f"{v['label']}: bnd {v['boundary_ge_0.5']}/{v['n_boundary']} "
          f"(m={v['mean_conf_boundary']:.3f}) int {v['internal_lt_0.5']}/{v['n_internal']} "
          f"(m={v['mean_conf_internal']:.3f})")
for key in ('STRUCT_MAP', 'ANCHOR_FULL_MAP', 'ANCHOR_STRICT_MAP', 'PRIOR_ONLY_MAP'):
    s = results['implied_wordlen'][key]
    print(key, 'n=', s['n_words'], 'mean=', s['mean'], 'med=', s['median'],
          'chi2=', s['chi2_vs_era'])
print('checkpoint:', chk)
