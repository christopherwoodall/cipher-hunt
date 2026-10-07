#!/usr/bin/env python3
"""
THE PHONOTACTICIAN — crowd executor, zeschau-seebach-1841 lane.

Constrained search over syllabary assignments with 8 anchors pinned,
scored by FRENCH SYLLABLE-STRUCTURE (syllable bigram model built from a
rule-based orthographic French syllabifier run over Les Miserables Tome I),
not letter n-grams.

Anchors pinned: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (cribs),
                87=ce (lane-inferred, 4/5 checks, provisional).
Group stream loaded via load_pairs from code/crib_attack.py — pairing NOT
re-derived here.

Method:
  1. Syllabify ~Miserables words with maximal-onset French rules (qu/ch/ph/gn
     as unit onsets; plosive+fricative+l/r clusters stay together).
  2. Inventory = top-K syllables by token frequency (+ anchors + 'm').
  3. Simulated annealing over the 88 free groups, objective = sum of log
     bigram probs of the decoded group stream. Anchors pinned.
  4. Baseline: random uniform assignments of the 88 free groups (same anchors).
  5. Stability: modal assignment per group across restarts.

Writes: code/crowd/phonotactician_results.md + .json
"""
import json, math, os, re, sys, unicodedata, collections
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))          # code/crowd
CODE = os.path.dirname(HERE)                                # code
LANE = os.path.dirname(CODE)                                # lane root
DATA = os.path.join(LANE, 'data')
sys.path.insert(0, CODE)
from crib_attack import load_pairs

ANCHORS = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i',
           '29': 'er', '40': 'e', '46': 'que', '87': 'ce'}
K_TOP = 400
ALPHA = 0.5

# ---------------- group stream ----------------
pairs, odd_lines, off1 = load_pairs()
types = sorted(set(pairs))
T = len(types)
ti = {t: i for i, t in enumerate(types)}
seq = np.array([ti[p] for p in pairs], dtype=np.int32)
freq = collections.Counter(pairs)

# verify against attempt1_results.json (VERIFICATION requirement)
a1 = json.load(open(os.path.join(DATA, 'attempt1_results.json')))['phaseA']
assert len(pairs) == a1['pairs'] == 1846, (len(pairs), a1['pairs'])
assert T == a1['distinct_groups'] == 96, (T, a1['distinct_groups'])
assert odd_lines == a1['odd_digit_lines'] == 28
assert off1 == a1['lines_with_offset1'] == 32
print(f"verified: pairs=1846 groups=96 odd_lines=28 offset1_lines=32", flush=True)

# ---------------- French orthographic syllabifier ----------------
ACC = str.maketrans({'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'à': 'a', 'â': 'a',
                     'ä': 'a', 'ç': 'c', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o',
                     'û': 'u', 'ü': 'u', 'ù': 'u', 'ÿ': 'y', 'æ': 'ae', 'œ': 'oe'})
VOW = set('aeiouy')
UNIT_ONSET = {'qu', 'ch', 'ph', 'gn'}          # digraphs treated as one consonant
ONSET2_OK = set()                               # C+l/r clusters kept together
for c1 in 'bpcdfgkptv':
    for c2 in 'lr':
        ONSET2_OK.add(c1 + c2)
ONSET2_OK |= {'bl', 'cl', 'gl', 'pl', 'fl', 'vr'}


def tokenize(word):
    """Split word into vowel chars and consonant-unit tokens."""
    toks, i = [], 0
    while i < len(word):
        if word[i:i+2] in UNIT_ONSET:
            toks.append(word[i:i+2]); i += 2
        else:
            toks.append(word[i]); i += 1
    return toks


def is_vow(tok):
    return tok in VOW


def legal_onset(cluster):
    """Can this consonant-token cluster begin a French syllable?"""
    n = len(cluster)
    if n == 0:
        return True
    if n == 1:
        return True
    if n == 2:
        return ''.join(cluster) in ONSET2_OK
    if n == 3:
        # s + 2-cluster, or cluster + s — rare; allow s+legal2
        return cluster[0] == 's' and ''.join(cluster[1:]) in ONSET2_OK
    return False


def split_cluster(cluster):
    """Maximal onset split of internal consonant cluster -> (coda, onset)."""
    for k in (3, 2, 1, 0):
        onset = cluster[len(cluster)-k:]
        if legal_onset(onset):
            return cluster[:len(cluster)-k], onset
    return cluster, []


def syllabify(word):
    toks = tokenize(word)
    # locate vowel positions
    vpos = [i for i, t in enumerate(toks) if is_vow(t)]
    if not vpos:
        return [''.join(toks)]
    syls, cur_coda = [], []
    # leading consonants -> onset of first syllable
    prev = 0
    syls_tokens = []
    for vi, v in enumerate(vpos):
        cluster = toks[prev:v]          # consonants since last vowel
        if vi == 0:
            onset = cluster
            coda_prev = []
        else:
            coda_prev, onset = split_cluster(cluster)
            # append coda to previous syllable
            syls_tokens[-1].extend(coda_prev)
        syl = onset + [toks[v]]
        syls_tokens.append(syl)
        prev = v + 1
    # trailing consonants -> coda of last syllable
    syls_tokens[-1].extend(toks[prev:])
    return [''.join(s) for s in syls_tokens]


# ---------------- build syllable bigram model ----------------
def iter_words(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.translate(ACC).lower()
            for w in re.findall(r'[a-z]+', line):
                if len(w) >= 2:
                    yield w

uni = collections.Counter()
bi = collections.Counter()
nwords = 0
for w in iter_words(os.path.join(DATA, 'gutenberg-17489-miserables1.txt')):
    nwords += 1
    ss = syllabify(w)
    for s in ss:
        uni[s] += 1
    for a, b in zip(ss, ss[1:]):
        bi[(a, b)] += 1

top = [s for s, _ in uni.most_common(K_TOP)]
cov = sum(uni[s] for s in top) / sum(uni.values())
inv = list(top)
for a in ANCHORS.values():
    if a not in inv:
        inv.append(a)
K = len(inv)
si = {s: i for i, s in enumerate(inv)}
print(f"syllabifier: {nwords} words, {len(uni)} distinct syllables; "
      f"top-{K_TOP} token coverage={cov:.4f}; inventory K={K}", flush=True)
missing_anchors = [a for a in ANCHORS.values() if a not in top]
print(f"anchors missing from top-{K_TOP}: {missing_anchors}", flush=True)

# bigram log-prob matrix with add-alpha smoothing
L = np.full((K, K), -1e9, dtype=np.float64)
log_denom = np.zeros(K)
for i, s in enumerate(inv):
    d = uni.get(s, 0) + ALPHA * K
    log_denom[i] = math.log(d)
    base = -math.log(d)
    L[i, :] = base + math.log(ALPHA)   # unseen
for (a, b), c in bi.items():
    if a in si and b in si:
        L[si[a], si[b]] = math.log(c + ALPHA) - log_denom[si[a]]

fixed = {ti[g]: si[s] for g, s in ANCHORS.items()}
free = [t for t in range(T) if t not in fixed]
assert len(free) == 88, len(free)


def decode_score(assign):
    a = assign[seq]
    return float(L[a[:-1], a[1:]].sum())


rng_global = np.random.default_rng(1841)

# ---------------- baseline: random assignments, anchors pinned ----------------
N_BASE = 500
base_scores = np.empty(N_BASE)
for n in range(N_BASE):
    asg = np.empty(T, dtype=np.int32)
    for t, s in fixed.items():
        asg[t] = s
    asg[free] = rng_global.integers(0, K, size=len(free))
    base_scores[n] = decode_score(asg)
bmean, bmax = float(base_scores.mean()), float(base_scores.max())
print(f"baseline random (n={N_BASE}): mean={bmean:.1f} max={bmax:.1f}", flush=True)

# ---------------- simulated annealing ----------------
def anneal(restart_id, iters=150000, seed=0):
    rng = np.random.default_rng(10_000 + seed)
    asg = np.empty(T, dtype=np.int32)
    for t, s in fixed.items():
        asg[t] = s
    asg[free] = rng.integers(0, K, size=len(free))
    cur = decode_score(asg)
    best, best_asg = cur, asg.copy()
    T0, T1 = 10.0, 0.1
    cool = (T1 / T0) ** (1.0 / iters)
    temp = T0
    for it in range(iters):
        g = free[rng.integers(0, len(free))]
        old = asg[g]
        new = rng.integers(0, K)
        if new == old:
            continue
        asg[g] = new
        sc = decode_score(asg)
        if sc >= cur or rng.random() < math.exp((sc - cur) / temp):
            cur = sc
            if sc > best:
                best, best_asg = sc, asg.copy()
        else:
            asg[g] = old
        temp *= cool
    return best, best_asg


N_RESTART = 12
ITERS = 150000
results = []
for r in range(N_RESTART):
    b, a = anneal(r, ITERS, seed=r)
    results.append((b, a))
    print(f"restart {r}: best={b:.1f}", flush=True)

results.sort(key=lambda x: -x[0])
best_score, best_asg = results[0]

# ---------------- stability across restarts ----------------
assign_matrix = np.array([a for _, a in results])   # (R, T)
stable = []
for t in free:
    vals, counts = np.unique(assign_matrix[:, t], return_counts=True)
    j = vals[counts.argmax()]
    frac = float(counts.max()) / N_RESTART
    stable.append({'group': types[t], 'freq': freq[types[t]],
                   'syllable': inv[j], 'frac': round(frac, 3)})
stable.sort(key=lambda x: -x['frac'])

# anchor context assignments from best key (phaseB-style evidence)
ctx = {}
after = collections.Counter()
before = collections.Counter()
for i, p in enumerate(pairs):
    if p == '82' and i + 1 < len(pairs):
        after[pairs[i+1]] += 1
    if p == '11' and i > 0:
        before[pairs[i-1]] += 1
ctx['after_82_m'] = [{'group': g, 'n': n, 'best_syll': inv[best_asg[ti[g]]]}
                     for g, n in after.most_common(6)]
ctx['before_11_la'] = [{'group': g, 'n': n, 'best_syll': inv[best_asg[ti[g]]]}
                       for g, n in before.most_common(6)]

decoded = ''.join(inv[best_asg[ti[p]]] for p in pairs)

out = {
    'method': 'simulated annealing, syllable-bigram log-likelihood, 8 anchors pinned',
    'corpus': 'gutenberg-17489-miserables1.txt (Hugo 1862; ERA CAVEAT: 21y after 1841 letter, not era-matched)',
    'syllabifier': 'rule-based maximal-onset FR orthographic; qu/ch/ph/gn unit onsets; C+l/r clusters',
    'inventory': {'K': K, 'top400_token_coverage': round(cov, 4),
                  'anchors_missing_from_top400': missing_anchors},
    'groups': T, 'free_groups': len(free), 'pairs': len(pairs),
    'annealing': {'restarts': N_RESTART, 'iters_per_restart': ITERS,
                  'T0': 10.0, 'T1': 0.1},
    'best_score': round(best_score, 1),
    'restart_scores': [round(b, 1) for b, _ in results],
    'baseline': {'n': N_BASE, 'mean': round(bmean, 1), 'max': round(bmax, 1),
                 'sd': round(float(base_scores.std()), 1)},
    'delta_vs_baseline_max': round(best_score - bmax, 1),
    'delta_vs_baseline_mean': round(best_score - bmean, 1),
    'best_key': {types[t]: inv[best_asg[t]] for t in range(T)},
    'stability': stable,
    'anchor_contexts_best_key': ctx,
    'decoded_head_400': decoded[:400],
}
with open(os.path.join(HERE, 'phonotactician_results.json'), 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print("wrote phonotactician_results.json", flush=True)
print("decoded head:", decoded[:300])
