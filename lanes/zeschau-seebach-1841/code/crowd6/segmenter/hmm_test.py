#!/usr/bin/env python3
"""hmm_test.py — THREAD 2 of rotation round 6 (split out: slow).
3-state HMM vs 96-group bigram model, held-out. See PREREG.md.
Writes hmm_test.json."""
import json, os, sys, math, collections, random
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired
rng = random.Random(20261007); np.random.seed(20261007)
OUT = {}
pairs, odd_lines, off1 = load_pairs_repaired()
N = len(pairs); GROUPS = sorted(set(pairs))
BANKED = json.load(open(os.path.join(LANE, 'code', 'crowd4', 'phase_map_repaired.json')))
LABS4 = ('A', 'B', 'C', 'R')
def apply_labels(stream, lab): return [lab[g] for g in stream]
def fit_markov(lseq, states=LABS4, alpha=0.0):
    S = list(states); si = {s: i for i, s in enumerate(S)}; m = len(S)
    C = np.zeros((m, m))
    for a, b in zip(lseq, lseq[1:]): C[si[a], si[b]] += 1
    M = (C + alpha) / (C.sum(axis=1, keepdims=True) + alpha * m)
    w, v = np.linalg.eig(M.T); pi = np.real(v[:, np.argmin(np.abs(w - 1.0))]); pi = pi / pi.sum()
    return M, pi, C
# ================= THREAD 2: 3-state HMM vs 96-group bigram, held-out =================
print('--- THREAD 2: HMM vs bigram, held-out ---', flush=True)
tr, te = pairs[:1231], pairs[1231:]
gi = {g: i for i, g in enumerate(GROUPS)}
n_tr, n_te = len(tr) - 1, len(te) - 1
t2 = {'split': 'train=pairs[0:1231] test=pairs[1231:]',
      'n_train_trans': n_tr, 'n_test_trans': n_te}

# ---- M_big: 96-state first-order Markov, Laplace(1) ----
Cb = np.zeros((96, 96))
for a, b in zip(tr, tr[1:]):
    Cb[gi[a], gi[b]] += 1
Pb = (Cb + 1.0) / (Cb.sum(axis=1, keepdims=True) + 96.0)
ll_tr_big = sum(math.log(Pb[gi[a], gi[b]]) for a, b in zip(tr, tr[1:]))
ll_te_big = sum(math.log(Pb[gi[a], gi[b]]) for a, b in zip(te, te[1:]))
k_big = 96 * 95
bic_big = -2 * ll_tr_big + k_big * math.log(n_tr)
print("M_big: trainLL=%.1f testLL/trans=%.4f BIC=%.1f (k=%d)" %
      (ll_tr_big, ll_te_big / n_te, bic_big, k_big))
t2['M_big'] = {'k': k_big, 'trainLL': round(ll_tr_big, 2),
               'testLL_per_trans': round(ll_te_big / n_te, 4),
               'BIC': round(bic_big, 1)}


# ---- M_hmm: 3-state HMM, Baum-Welch on train ----
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
    # vectorized xi: xi[t,i,j] = al[t,i] * A[i,j] * E[j,obs[t+1]] * be[t+1,j]
    EB = E[:, obs_idx[1:]].T * be[1:]          # (Tt-1, Ns)
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
            # MAP-EM with weak Dirichlet prior (eps) — numerical floor that
            # keeps emissions/transitions off exact zero (A3)
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
    best = best + (restart_lls,)
    return best


tr_idx = [gi[g] for g in tr]
te_idx = [gi[g] for g in te]
llh, pih, Ah, Eh, rstar, rlls = baum_welch(tr_idx)
k_hmm = 6 + 285 + 2
bic_hmm = -2 * llh + k_hmm * math.log(n_tr)
ll_te_hmm, _, _ = fwd_bwd(te_idx, pih, Ah, Eh)
print("M_hmm: trainLL=%.1f (restart %d) testLL/trans=%.4f BIC=%.1f (k=%d)" %
      (llh, rstar, ll_te_hmm / n_te, bic_hmm, k_hmm))
t2['M_hmm'] = {'k': k_hmm, 'trainLL': round(llh, 2), 'best_restart': rstar,
               'restart_trainLLs': rlls,
               'testLL_per_trans': round(ll_te_hmm / n_te, 4),
               'BIC': round(bic_hmm, 1),
               'A': [[round(float(x), 3) for x in row] for row in Ah],
               'pi': [round(float(x), 3) for x in pih]}

# ---- M_phm: observed-phase 3-state Markov (banked labels), Laplace(1) ----
lseq_tr = apply_labels(tr, BANKED)
lseq_te = apply_labels(te, BANKED)
ST3 = ('A', 'B', 'C')
# map R -> nearest? No: restrict transition/emission estimation to ABC tokens
# but keep the stream intact by treating R as its own emission-only state is
# complex; simpler honest choice: 4-state observed Markov (A,B,C,R).
M4, pi4, C4 = fit_markov(lseq_tr, alpha=1.0)
E4 = np.zeros((4, 96))
for s_i, s in enumerate(LABS4):
    cnt = collections.Counter(g for g, l in zip(tr, lseq_tr) if l == s)
    tot = sum(cnt.values())
    for g in GROUPS:
        E4[s_i, gi[g]] = (cnt[g] + 1.0) / (tot + 96.0)
pi4s = (C4.sum(axis=1) + 1.0)
pi4s = pi4s / pi4s.sum()
ll_tr_phm = (math.log(pi4s[LABS4.index(lseq_tr[0])]) +
             sum(math.log(M4[LABS4.index(a), LABS4.index(b)])
                 for a, b in zip(lseq_tr, lseq_tr[1:])) +
             sum(math.log(E4[LABS4.index(l), gi[g]])
                 for g, l in zip(tr, lseq_tr)))
ll_te_phm = (math.log(pi4s[LABS4.index(lseq_te[0])]) +
             sum(math.log(M4[LABS4.index(a), LABS4.index(b)])
                 for a, b in zip(lseq_te, lseq_te[1:])) +
             sum(math.log(E4[LABS4.index(l), gi[g]])
                 for g, l in zip(te, lseq_te)))
k_phm = 12 + 4 * 95 + 3
bic_phm = -2 * ll_tr_phm + k_phm * math.log(n_tr)
print("M_phm(4-state observed): trainLL=%.1f testLL/trans=%.4f BIC=%.1f (k=%d)" %
      (ll_tr_phm, ll_te_phm / n_te, bic_phm, k_phm))
t2['M_phm'] = {'k': k_phm, 'trainLL': round(ll_tr_phm, 2),
               'testLL_per_trans': round(ll_te_phm / n_te, 4),
               'BIC': round(bic_phm, 1)}
hmm_wins = (ll_te_hmm / n_te > ll_te_big / n_te) and (bic_hmm < bic_big)
t2['verdict_hmm_beats_bigram'] = bool(hmm_wins)
print("T2 verdict: HMM beats bigram (testLL AND BIC):", hmm_wins)

# Viterbi decode on full stream, agreement with banked ABC labels
# (via contingency table — state names are arbitrary, so count co-occurrence)
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

vit = viterbi([gi[g] for g in pairs], pih, Ah, Eh)
vit_lab = {g: 'S%d' % s for g, s in zip(pairs, vit)}
# state names arbitrary -> contingency of Viterbi state vs banked label
abc_groups = [g for g in GROUPS if BANKED[g] in 'ABC']
cont = collections.Counter((vit_lab[g], BANKED[g]) for g in abc_groups)
print("  contingency (viterbi_state, banked):", dict(cont))
t2['viterbi_banked_contingency'] = {'%s/%s' % k: v for k, v in cont.items()}
OUT['thread2'] = t2



json.dump(OUT, open(os.path.join(HERE, 'hmm_test.json'), 'w'), indent=1)
print('wrote hmm_test.json', flush=True)
