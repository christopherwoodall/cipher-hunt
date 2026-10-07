#!/usr/bin/env python3
"""rotation_r6.py — SEGMENTER executor, round 6: rotation follow-ups.

Implements the pre-registered battery in PREREG.md (this directory).
Canonical stream: code/side-keyhunt/repaired_offsets.json (1,847 pairs).
Cipher-internal only (F30-legal). No era legs. No invented values.
"""
import json, os, sys, math, collections, itertools, random
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

rng = random.Random(20261007)
np.random.seed(20261007)
OUT = {}

pairs, odd_lines, off1 = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N
GROUPS = sorted(set(pairs))
assert len(GROUPS) == 96
BANKED = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                     'phase_map_repaired.json')))
LABS4 = ('A', 'B', 'C', 'R')


# ---------------- label-stream statistics ----------------
def apply_labels(stream, lab):
    return [lab[g] for g in stream]


def fit_markov(lseq, states=LABS4, alpha=0.0):
    S = list(states)
    si = {s: i for i, s in enumerate(S)}
    m = len(S)
    C = np.zeros((m, m))
    for a, b in zip(lseq, lseq[1:]):
        C[si[a], si[b]] += 1
    M = (C + alpha) / (C.sum(axis=1, keepdims=True) + alpha * m)
    # stationary of M
    w, v = np.linalg.eig(M.T)
    pi = np.real(v[:, np.argmin(np.abs(w - 1.0))])
    pi = pi / pi.sum()
    return M, pi, C


def e1_stat(lseq):
    """F43 E1 (construction pinned down 2026-10-07): lag-3 same-phase rate over
    pairs with BOTH endpoints in ABC; Markov expectation conditioned on
    endpoints-ABC under the 4-state fitted chain."""
    n_all = len(lseq) - 3
    idx = [t for t in range(n_all) if lseq[t] in 'ABC' and lseq[t + 3] in 'ABC']
    n = len(idx)
    obs = sum(1 for t in idx if lseq[t] == lseq[t + 3]) / n
    M, pi, _ = fit_markov(lseq)  # 4-state fit on the full label stream
    M3 = np.linalg.matrix_power(M, 3)
    num = float(sum(pi[s] * M3[s, s] for s in range(3)))
    den = float(sum(pi[s] * M3[s, :3].sum() for s in range(3)))
    exp = num / den
    se = math.sqrt(exp * (1 - exp) / n)
    z = (obs - exp) / se
    return {'n': n, 'obs': obs, 'exp': exp, 'z': z}


def lag_rates(lseq, kmax=6):
    out = {}
    for k in range(1, kmax + 1):
        n = len(lseq) - k
        out[k] = sum(1 for t in range(n) if lseq[t] == lseq[t + k]) / n
    return out


# ---------------- clustering machinery (contactor's, reimplemented) ----------------
def contact_sets(stream, K=10):
    foll = collections.defaultdict(collections.Counter)
    pred = collections.defaultdict(collections.Counter)
    for a, b in zip(stream, stream[1:]):
        foll[a][b] += 1
        pred[b][a] += 1
    TOP = {g: (set(h for h, _ in foll[g].most_common(K)) |
               set(h for h, _ in pred[g].most_common(K))) for g in GROUPS}
    return foll, pred, TOP


def jac_fn(TOP):
    def jac(a, b):
        sa, sb = TOP[a], TOP[b]
        u = sa | sb
        return len(sa & sb) / len(u) if u else 0.0
    return jac


def cos_fn(foll, pred):
    G = len(GROUPS)
    idx = {g: i for i, g in enumerate(GROUPS)}
    CV = {}
    for g in GROUPS:
        v = np.zeros(2 * G)
        tp = sum(pred[g].values()) + G
        tf = sum(foll[g].values()) + G
        for h, c in pred[g].items():
            v[idx[h]] = (c + 1) / tp
        for h, c in foll[g].items():
            v[G + idx[h]] = (c + 1) / tf
        for i in range(G):
            if v[i] == 0:
                v[i] = 1.0 / tp
            if v[G + i] == 0:
                v[G + i] = 1.0 / tf
        CV[g] = v / np.linalg.norm(v)

    def cos(a, b):
        return float(np.dot(CV[a], CV[b]))
    return cos


def agglomerate(simfn):
    clusters = [{g} for g in GROUPS]
    merges = []
    while len(clusters) > 1:
        best, bi, bj = -1.0, None, None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                c1, c2 = clusters[i], clusters[j]
                s = sum(simfn(a, b) for a in c1 for b in c2) / (len(c1) * len(c2))
                if s > best:
                    best, bi, bj = s, i, j
        merges.append((sorted(clusters[bi]), sorted(clusters[bj])))
        new = clusters[bi] | clusters[bj]
        clusters = [c for k, c in enumerate(clusters)
                    if k not in (bi, bj)] + [new]
    return merges


def cut_labels(merges, k_cut):
    cs = [{g} for g in GROUPS]
    for c1l, c2l in merges:
        if len(cs) <= k_cut:
            break
        c1, c2 = set(c1l), set(c2l)
        cs = [c for c in cs if c != c1 and c != c2] + [c1 | c2]
    cs = sorted(cs, key=len, reverse=True)
    lab = {}
    for x, lbl in ((cs[0], 'A'), (cs[1], 'B'), (cs[2], 'C')):
        for g in x:
            lab[g] = lbl
    for c in cs[3:]:
        for g in c:
            lab[g] = 'R'
    return lab


def derive_labels(stream, metric='jaccard', k_cut=12, K=10):
    foll, pred, TOP = contact_sets(stream, K)
    simfn = jac_fn(TOP) if metric == 'jaccard' else cos_fn(foll, pred)
    return cut_labels(agglomerate(simfn), k_cut)


def best_perm_agreement(lab1, lab2, groups=None):
    groups = groups or GROUPS
    best = (0, None)
    for perm in itertools.permutations(LABS4):
        m = {a: b for a, b in zip(LABS4, perm)}
        ag = sum(1 for g in groups if m[lab1[g]] == lab2[g])
        if ag > best[0]:
            best = (ag, perm)
    return best


def directed_cycle_mass(lseq):
    """Mass of the two directed 3-cycles on ABC transitions."""
    fwd = {(('A', 'B'), ('B', 'C'), ('C', 'A'))}
    m_f = sum(1 for a, b in zip(lseq, lseq[1:])
              if (a, b) in {('A', 'B'), ('B', 'C'), ('C', 'A')})
    m_r = sum(1 for a, b in zip(lseq, lseq[1:])
              if (a, b) in {('A', 'C'), ('C', 'B'), ('B', 'A')})
    return m_f, m_r


# ================= GATE: re-derive F43 E1 on banked labels =================
lseq_ref = apply_labels(pairs, BANKED)
e1_ref = e1_stat(lseq_ref)
lr_ref = lag_rates(lseq_ref)
print("GATE E1: obs=%.4f exp=%.4f z=%.2f n=%d (F43: 0.4219/0.3530/+5.6)" %
      (e1_ref['obs'], e1_ref['exp'], e1_ref['z'], e1_ref['n']))
print("  lag rates:", {k: round(v, 4) for k, v in lr_ref.items()})
OUT['gate'] = {'e1': {k: round(v, 4) if isinstance(v, float) else v
                      for k, v in e1_ref.items()},
               'lag_rates': {k: round(v, 4) for k, v in lr_ref.items()},
               'note': 'E1 construction pinned: lag-3 pairs with both '
                       'endpoints in ABC; Markov exp conditioned on '
                       'endpoints-ABC (reproduces banked obs exactly)'}
gate_ok = (abs(e1_ref['obs'] - 0.4219) < 0.001 and
           abs(e1_ref['z'] - 5.6) < 0.5)
print("GATE:", "PASS" if gate_ok else "FAIL — STOP")
if not gate_ok:
    json.dump(OUT, open(os.path.join(HERE, 'rotation_r6.json'), 'w'), indent=1)
    sys.exit(2)

# ================= THREAD 1: labeling-robustness battery =================
print("\n--- THREAD 1: labeling robustness ---")
t1 = {}
variants = {}
# V_cos / V_k8 / V_k16 on the full stream
variants['V_cos'] = derive_labels(pairs, metric='cosine', k_cut=12)
variants['V_k8'] = derive_labels(pairs, metric='jaccard', k_cut=8)
variants['V_k16'] = derive_labels(pairs, metric='jaccard', k_cut=16)
# half-stream fits
for name, fit_half, eval_half in (('V_half1', pairs[:923], pairs[923:]),
                                  ('V_half2', pairs[923:], pairs[:923])):
    lab = derive_labels(fit_half, metric='jaccard', k_cut=12)
    present = set(fit_half)
    for g in GROUPS:  # groups absent from the fit half -> R
        if g not in present:
            lab[g] = 'R'
    variants[name] = (lab, eval_half)
mf_ref, mr_ref = directed_cycle_mass(lseq_ref)
print("reference dominant cycle: fwd(A->B->C->A)=%d rev=%d" % (mf_ref, mr_ref))
t1['reference'] = {'e1': OUT['gate']['e1'],
                   'cycle_fwd': mf_ref, 'cycle_rev': mr_ref}
for name, v in variants.items():
    if isinstance(v, tuple):
        lab, ev = v
    else:
        lab, ev = v, pairs
    ls = apply_labels(ev, lab)
    e1 = e1_stat(ls)
    # align to reference labels (best perm) then check dominant cycle direction
    ag, perm = best_perm_agreement(lab, BANKED)
    m = {a: b for a, b in zip(LABS4, perm)}
    ls_al = [m[x] for x in ls]
    mf, mr = directed_cycle_mass(ls_al)
    sizes = dict(collections.Counter(lab.values()))
    print("%s: obs=%.4f exp=%.4f z=%+.2f | agree-vs-ref %d/96 perm=%s | "
          "sizes=%s | cycle fwd=%d rev=%d" %
          (name, e1['obs'], e1['exp'], e1['z'], ag, ''.join(perm), sizes, mf, mr))
    t1[name] = {'e1_obs': round(e1['obs'], 4), 'e1_exp': round(e1['exp'], 4),
                'e1_z': round(e1['z'], 2),
                'agree_vs_ref': ag, 'perm': ''.join(perm),
                'sizes': sizes, 'cycle_fwd': mf, 'cycle_rev': mr}
robust = all(t1[v]['e1_z'] > 2.0 for v in
             ('V_cos', 'V_k8', 'V_k16', 'V_half1', 'V_half2'))
same_cyc = all(t1[v]['cycle_fwd'] > t1[v]['cycle_rev'] for v in
               ('V_cos', 'V_k8', 'V_k16', 'V_half1', 'V_half2'))
t1['verdict_robust'] = bool(robust)
t1['verdict_same_cycle'] = bool(same_cyc)
print("T1 verdict: lag-3 excess robust(z>2 all variants):", robust,
      "| same directed cycle post-alignment:", same_cyc)
OUT['thread1'] = t1


# ================= THREAD 3: reconcile 69/96 vs "61/96 change" =================
print("\n--- THREAD 3: label-agreement reconciliation ---")
cd = json.load(open(os.path.join(LANE, 'code', 'crowd', 'contactor_results.json')))
jc12 = cd['jaccard_clusters']['12']
cl_old = sorted([c['members'] for c in jc12], key=len, reverse=True)
old_lab = {}
for x, lbl in ((cl_old[0], 'A'), (cl_old[1], 'B'), (cl_old[2], 'C')):
    for g in x:
        old_lab[g] = lbl
rest_old = set(GROUPS) - set().union(*[set(c) for c in cl_old[:3]])
for g in rest_old:
    old_lab[g] = 'R'
print("old sizes:", dict(collections.Counter(old_lab.values())),
      "| new sizes:", dict(collections.Counter(BANKED.values())))
naive = sum(1 for g in GROUPS if old_lab[g] == BANKED[g])
ag_bp, perm_bp = best_perm_agreement(old_lab, BANKED)
abc_both = [g for g in GROUPS if old_lab[g] in 'ABC' and BANKED[g] in 'ABC']
naive_abc = sum(1 for g in abc_both if old_lab[g] == BANKED[g])
ag_bp_abc, perm_bp_abc = best_perm_agreement(old_lab, BANKED, groups=abc_both)
print("naive label-name agreement: %d/96 (change=%d)" % (naive, 96 - naive))
print("best-permutation agreement: %d/96 perm=%s" % (ag_bp, ''.join(perm_bp)))
print("ABC-both (%d groups): naive %d, best-perm %d perm=%s" %
      (len(abc_both), naive_abc, ag_bp_abc, ''.join(perm_bp_abc)))
t3 = {'old_sizes': dict(collections.Counter(old_lab.values())),
      'naive_agree': naive, 'naive_change': 96 - naive,
      'bestperm_agree': ag_bp, 'bestperm_perm': ''.join(perm_bp),
      'n_abc_both': len(abc_both), 'abc_naive_agree': naive_abc,
      'abc_bestperm_agree': ag_bp_abc,
      'abc_bestperm_perm': ''.join(perm_bp_abc)}
# Which comparison reproduces which banked number?
t3['n30_61_change_matches'] = ('naive' if t3['naive_change'] == 61 else
                               ('bestperm' if 96 - ag_bp == 61 else 'neither'))
t3['n37_69_agree_matches'] = ('bestperm' if ag_bp == 69 else
                               ('naive' if naive == 69 else 'neither'))
print("N30 '61/96 change' matches:", t3['n30_61_change_matches'],
      "| N37 '69/96 agree' matches:", t3['n37_69_agree_matches'])
OUT['thread3'] = t3

# ================= THREAD 4: column-geometry mechanism tests =================
print("\n--- THREAD 4: column-geometry mechanism ---")
# reference dominant cycle from banked labels
mf, mr = directed_cycle_mass(lseq_ref)
CYC = {'A': 'B', 'B': 'C', 'C': 'A'} if mf > mr else {'A': 'C', 'C': 'B', 'B': 'A'}
print("reference cyc:", CYC, "(fwd=%d rev=%d)" % (mf, mr))
t4 = {'cyc': CYC}

# P2a: momentum — cycle continuation more likely after a cycle step?
n1 = n0 = c1 = c0 = 0
for t in range(1, N - 1):
    a, b, c_ = lseq_ref[t - 1], lseq_ref[t], lseq_ref[t + 1]
    if not (a in 'ABC' and b in 'ABC' and c_ in 'ABC'):
        continue
    if b == CYC[a]:  # (t-1,t) is a cycle step
        n1 += 1
        c1 += (c_ == CYC[b])
    elif b != a:     # ABC non-cycle, non-self step
        n0 += 1
        c0 += (c_ == CYC[b])
r1, r0 = c1 / n1, c0 / n0
# one-sided two-proportion z
p_pool = (c1 + c0) / (n1 + n0)
se_p = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n0))
z_p = (r1 - r0) / se_p
from math import erf
p_one = 1 - 0.5 * (1 + erf(z_p / math.sqrt(2)))
print("P2a momentum: r1(after cycle)=%.4f (n=%d) r0(after non-cycle)=%.4f (n=%d) "
      "z=%+.2f one-sided p=%.4f" % (r1, n1, r0, n0, z_p, p_one))
t4['P2a'] = {'r1': round(r1, 4), 'n1': n1, 'r0': round(r0, 4), 'n0': n0,
             'z': round(z_p, 2), 'p_one_sided': round(p_one, 4),
             'verdict': 'SUPPORT' if p_one < 0.05 else 'FALSIFIED(null)'}

# P2b: held-out order selection, 1st vs 2nd order on 4-state label stream
h1, h2 = lseq_ref[:923], lseq_ref[923:]
tr1 = list(zip(h1, h1[1:]))
te1 = list(zip(h2, h2[1:]))


def order_ll(order, tr_seq, te_seq, alpha=1.0):
    m = 4
    si = {s: i for i, s in enumerate(LABS4)}
    if order == 1:
        C = np.zeros((m, m))
        for a, b in zip(tr_seq, tr_seq[1:]):
            C[si[a], si[b]] += 1
        P = (C + alpha) / (C.sum(axis=1, keepdims=True) + alpha * m)
        ll = sum(math.log(P[si[a], si[b]]) for a, b in zip(te_seq, te_seq[1:]))
        return ll, 12
    C = np.zeros((m, m, m))
    for a, b, c_ in zip(tr_seq, tr_seq[1:], tr_seq[2:]):
        C[si[a], si[b], si[c_]] += 1
    P = (C + alpha) / (C.sum(axis=2, keepdims=True) + alpha * m)
    ll = sum(math.log(P[si[a], si[b], si[c_]])
             for a, b, c_ in zip(te_seq, te_seq[1:], te_seq[2:]))
    return ll, 48


ll1, k1 = order_ll(1, h1, h2)
ll2, k2 = order_ll(2, h1, h2)
n1t, n2t = len(te1), len(h2) - 2
print("P2b order selection: 1st LL/trans=%.4f (k=%d) | 2nd LL/trans=%.4f (k=%d)" %
      (ll1 / n1t, k1, ll2 / n2t, k2))
t4['P2b'] = {'ll1_per_trans': round(ll1 / n1t, 4), 'k1': k1,
             'll2_per_trans': round(ll2 / n2t, 4), 'k2': k2,
             'verdict': 'SUPPORT(memory-2)' if ll2 / n2t > ll1 / n1t
             else 'FALSIFIED(null)'}

# P2c: fixed column order — dominant cycle in halves + thread-1 variants
def dom_cyc(lseq):
    mf_, mr_ = directed_cycle_mass(lseq)
    return 'fwd' if mf_ > mr_ else 'rev', mf_, mr_

dc_h1 = dom_cyc(lseq_ref[:923])
dc_h2 = dom_cyc(lseq_ref[923:])
print("P2c: half1 %s (%d/%d) half2 %s (%d/%d)" %
      (dc_h1[0], dc_h1[1], dc_h1[2], dc_h2[0], dc_h2[1], dc_h2[2]))
t4['P2c'] = {'half1': dc_h1[0], 'half2': dc_h2[0],
             'variants': {v: ('fwd' if t1[v]['cycle_fwd'] > t1[v]['cycle_rev']
                              else 'rev')
                          for v in ('V_cos', 'V_k8', 'V_k16',
                                    'V_half1', 'V_half2')}}
ref_dir = 'fwd' if mf > mr else 'rev'
p2c_ok = (dc_h1[0] == ref_dir and dc_h2[0] == ref_dir and
          all(d == ref_dir for d in t4['P2c']['variants'].values()))
t4['P2c']['verdict'] = 'SUPPORT' if p2c_ok else 'FALSIFIED'
print("P2c verdict:", t4['P2c']['verdict'])
OUT['thread4'] = t4


# merge thread-2 results if the background HMM run finished
_hp = os.path.join(HERE, 'hmm_test.json')
if os.path.exists(_hp):
    OUT['thread2'] = json.load(open(_hp))['thread2']
    print('merged thread2 from hmm_test.json')
else:
    OUT['thread2'] = {'status': 'pending (hmm_test.py still running)'}
json.dump(OUT, open(os.path.join(HERE, 'rotation_r6.json'), 'w'), indent=1)
print("\nwrote rotation_r6.json")
