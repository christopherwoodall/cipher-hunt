#!/usr/bin/env python3
"""momentum_labelfree.py — SEGMENTER round 7, Thread B: does the P2a momentum
signal survive WITHOUT the fragile banked labels?

Instrument: 3-state HMM (Baum-Welch code copied verbatim from round-6
hmm_test.py), fit on train pairs[0:1231] only, seed 20261007. Viterbi-decode
the HELD-OUT test split pairs[1231:] with frozen parameters. Cycle direction
from the frozen transition matrix (not from banked labels). P2a-analog
momentum on the decoded test stream. NO banked labels used at any step.
See PREREG7.md. Writes momentum_labelfree.json."""
import json, os, sys, math, random
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

rng = random.Random(20261007)
np.random.seed(20261007)
OUT = {}

pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N
GROUPS = sorted(set(pairs))
gi = {g: i for i, g in enumerate(GROUPS)}

tr, te = pairs[:1231], pairs[1231:]
n_tr, n_te = len(tr) - 1, len(te) - 1


# ---- copied verbatim from code/crowd6/segmenter/hmm_test.py ----
def fwd_bwd(obs_idx, pi, A, E):
    Tt, Ns, No = len(obs_idx), A.shape[0], E.shape[1]
    al = np.zeros((Tt, Ns))
    c = np.zeros(Tt)
    al[0] = pi * E[:, obs_idx[0]]
    c[0] = al[0].sum()
    al[0] /= c[0]
    for t in range(1, Tt):
        al[t] = (al[t - 1] @ A) * E[:, obs_idx[t]]
        c[t] = al[t].sum()
        al[t] /= max(c[t], 1e-300)
    be = np.zeros((Tt, Ns))
    be[-1] = 1.0 / max(c[-1], 1e-300)
    for t in range(Tt - 2, -1, -1):
        be[t] = (A @ (E[:, obs_idx[t + 1]] * be[t + 1])) / max(c[t], 1e-300)
    gam = al * be
    gam /= gam.sum(axis=1, keepdims=True)
    EB = E[:, obs_idx[1:]].T * be[1:]
    xi = al[:-1][:, :, None] * A[None, :, :] * EB[:, None, :]
    xi /= xi.sum(axis=(1, 2), keepdims=True)
    ll = float(np.log(np.maximum(c, 1e-300)).sum())
    return ll, gam, xi


def baum_welch(obs_idx, n_states=3, iters=150, restarts=10):
    No = 96
    obs_arr = np.array(obs_idx)
    best = None
    restart_lls = []
    for r in range(restarts):
        rs = np.random.RandomState(20261007 + r)
        pi = rs.dirichlet(np.ones(n_states))
        A = np.vstack([rs.dirichlet(np.ones(n_states)) for _ in range(n_states)])
        E = np.vstack([rs.dirichlet(np.ones(No)) for _ in range(n_states)])
        prev = -1e18
        for it in range(iters):
            ll, gam, xi = fwd_bwd(obs_idx, pi, A, E)
            pi = gam[0] / gam[0].sum()
            eps = 1e-4
            A = (xi.sum(axis=0) + eps)
            A /= A.sum(axis=1, keepdims=True)
            for s in range(n_states):
                E[s] = np.bincount(obs_arr, weights=gam[:, s],
                                   minlength=No) + eps
            E /= E.sum(axis=1, keepdims=True)
            if abs(ll - prev) < 1e-6 * max(1.0, abs(ll)):
                break
            prev = ll
        if best is None or ll > best[0]:
            best = (ll, pi.copy(), A.copy(), E.copy(), r)
        restart_lls.append(round(float(ll), 2))
    return best[0], best[1], best[2], best[3], best[4]


def viterbi(obs_idx, pi, A, E):
    Tt, Ns = len(obs_idx), A.shape[0]
    lp, lA, lE = np.log(pi), np.log(A), np.log(E)
    d = np.zeros((Tt, Ns))
    ptr = np.zeros((Tt, Ns), dtype=int)
    d[0] = lp + lE[:, obs_idx[0]]
    for t in range(1, Tt):
        cand = d[t - 1][:, None] + lA
        ptr[t] = cand.argmax(axis=0)
        d[t] = cand.max(axis=0) + lE[:, obs_idx[t]]
    st = np.zeros(Tt, dtype=int)
    st[-1] = d[-1].argmax()
    for t in range(Tt - 2, -1, -1):
        st[t] = ptr[t + 1, st[t + 1]]
    return st
# ---- end verbatim copy ----


tr_idx = [gi[g] for g in tr]
te_idx = [gi[g] for g in te]
llh, pih, Ah, Eh, rstar = baum_welch(tr_idx)
print("fit: trainLL=%.2f restart=%d" % (llh, rstar))
print("A =\n", np.round(Ah, 3))
OUT['fit'] = {'trainLL': round(llh, 2), 'best_restart': rstar,
              'A': [[round(float(x), 4) for x in row] for row in Ah]}

# Gate B0: instrument reproduction vs round-6 A
r6A = np.array(json.load(open(os.path.join(
    LANE, 'code', 'crowd6', 'segmenter', 'rotation_r6.json')))
    ['thread2']['M_hmm']['A'])
maxdiff = float(np.abs(Ah - r6A).max())
OUT['gate_B0'] = {'max_abs_diff_vs_round6': round(maxdiff, 6),
                  'pass': bool(maxdiff < 1e-3)}
print("Gate B0: max|A - round6 A| = %.2e -> %s" %
      (maxdiff, "PASS" if maxdiff < 1e-3 else "FAIL — STOP"))
assert maxdiff < 1e-3, "HMM instrument not reproduced"

# Guard B1: dominant directed 3-cycle in the frozen A
# the two directed 3-cycles on states {0,1,2}
fwd_cyc = [(0, 1), (1, 2), (2, 0)]
rev_cyc = [(0, 2), (2, 1), (1, 0)]
mf = sum(Ah[a, b] for a, b in fwd_cyc)
mr = sum(Ah[a, b] for a, b in rev_cyc)
if mf >= mr:
    CYC = {0: 1, 1: 2, 2: 0}
    cyc_name, fwd_mass, rev_mass = "0->1->2->0", mf, mr
else:
    CYC = {0: 2, 2: 1, 1: 0}
    cyc_name, fwd_mass, rev_mass = "0->2->1->0", mr, mf
ratio = fwd_mass / rev_mass
OUT['guard_B1'] = {'cycle': cyc_name, 'fwd_mass': round(float(fwd_mass), 3),
                   'rev_mass': round(float(rev_mass), 3),
                   'ratio': round(float(ratio), 2),
                   'pass': bool(ratio >= 2.0)}
print("Guard B1: dominant cycle %s fwd=%.3f rev=%.3f ratio=%.2f -> %s" %
      (cyc_name, fwd_mass, rev_mass, ratio,
       "PASS" if ratio >= 2.0 else "UNTESTABLE — STOP"))
assert ratio >= 2.0, "no definable cycle"


def momentum(sseq, cyc):
    n1 = n0 = c1 = c0 = 0
    for t in range(1, len(sseq) - 1):
        a, b, c_ = sseq[t - 1], sseq[t], sseq[t + 1]
        if b == cyc[a]:
            n1 += 1
            c1 += (c_ == cyc[b])
        elif b != a:
            n0 += 1
            c0 += (c_ == cyc[b])
    r1 = c1 / n1 if n1 else float('nan')
    r0 = c0 / n0 if n0 else float('nan')
    if n1 and n0:
        p_pool = (c1 + c0) / (n1 + n0)
        se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n0))
        z = (r1 - r0) / se if se > 0 else 0.0
        p_one = 1 - 0.5 * (1 + math.erf(z / math.sqrt(2)))
    else:
        z, p_one = float('nan'), float('nan')
    return {'r1': r1, 'n1': n1, 'r0': r0, 'n0': n0, 'z': z,
            'p_one_sided': p_one}


# Decode the HELD-OUT test split only
vit_te = viterbi(te_idx, pih, Ah, Eh)
print("decoded test states:", {int(s): int((vit_te == s).sum())
                               for s in range(3)})
m = momentum(vit_te, CYC)
OUT['momentum_heldout'] = {k: (round(v, 4) if isinstance(v, float) else v)
                           for k, v in m.items()}
print("Held-out momentum: r1=%.4f (n=%d) r0=%.4f (n=%d) z=%+.2f p=%.4f" %
      (m['r1'], m['n1'], m['r0'], m['n0'], m['z'], m['p_one_sided']))

# Guard B2: power
b2 = (m['n1'] >= 100 and m['n0'] >= 50)
OUT['guard_B2'] = {'n1': m['n1'], 'n0': m['n0'], 'pass': bool(b2)}
print("Guard B2 (n1>=100, n0>=50):", "PASS" if b2 else "INCONCLUSIVE — underpowered")

# Secondary: permutation null on the decoded test order
prng = random.Random(20261007)
diffs = []
base = vit_te.tolist()
obs_diff = m['r1'] - m['r0']
for _ in range(2000):
    prng.shuffle(base)
    mm = momentum(np.array(base), CYC)
    if mm['n1'] and mm['n0']:
        diffs.append(mm['r1'] - mm['r0'])
emp_p = sum(1 for d in diffs if d >= obs_diff) / len(diffs)
OUT['permutation_null'] = {'n_perm': len(diffs),
                           'empirical_p_one_sided': round(emp_p, 4),
                           'obs_diff': round(obs_diff, 4)}
print("Permutation null (2000): empirical one-sided p=%.4f" % emp_p)

# Reference (not verdict-driving): labeled P2a on the test split only.
# Reuse the R-safe construction (skip non-ABC triples) via inline code.
BANKED = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                     'phase_map_repaired.json')))
lseq_te = [BANKED[g] for g in te]
mfL = sum(1 for a, b in zip(lseq_te, lseq_te[1:])
          if (a, b) in {('A', 'B'), ('B', 'C'), ('C', 'A')})
mrL = sum(1 for a, b in zip(lseq_te, lseq_te[1:])
          if (a, b) in {('A', 'C'), ('C', 'B'), ('B', 'A')})
CYCL = {'A': 'B', 'B': 'C', 'C': 'A'} if mfL > mrL else {'A': 'C', 'C': 'B', 'B': 'A'}
n1 = n0 = c1 = c0 = 0
for t in range(1, len(lseq_te) - 1):
    a, b, c_ = lseq_te[t - 1], lseq_te[t], lseq_te[t + 1]
    if not (a in 'ABC' and b in 'ABC' and c_ in 'ABC'):
        continue
    if b == CYCL[a]:
        n1 += 1
        c1 += (c_ == CYCL[b])
    elif b != a:
        n0 += 1
        c0 += (c_ == CYCL[b])
r1, r0 = c1 / n1, c0 / n0
pp = (c1 + c0) / (n1 + n0)
se = math.sqrt(pp * (1 - pp) * (1 / n1 + 1 / n0))
zz = (r1 - r0) / se
p1 = 1 - 0.5 * (1 + math.erf(zz / math.sqrt(2)))
ml = {'r1': r1, 'n1': n1, 'r0': r0, 'n0': n0, 'z': zz, 'p_one_sided': p1}
OUT['labeled_reference_testsplit'] = {
    k: (round(v, 4) if isinstance(v, float) else v) for k, v in ml.items()}
print("Labeled P2a on test split (reference): r1=%.4f (n=%d) r0=%.4f (n=%d) "
      "z=%+.2f p=%.4f" % (ml['r1'], ml['n1'], ml['r0'], ml['n0'],
                          ml['z'], ml['p_one_sided']))

# Verdict
if not b2:
    verdict = 'INCONCLUSIVE (underpowered)'
elif m['p_one_sided'] < 0.05 and m['r1'] > m['r0']:
    verdict = 'SURVIVES — momentum confirmed without banked labels'
else:
    verdict = 'DOES NOT SURVIVE — momentum is label-dependent'
OUT['verdict'] = verdict
print("\nThread B verdict:", verdict)
json.dump(OUT, open(os.path.join(HERE, 'momentum_labelfree.json'), 'w'), indent=1)
print("wrote momentum_labelfree.json")
