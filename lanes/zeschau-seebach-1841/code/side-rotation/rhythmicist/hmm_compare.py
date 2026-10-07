#!/usr/bin/env python3
"""WO3 -- 3-state HMM vs flat 96-group bigram. Fresh Baum-Welch implementation.

Pre-registered: train = tokens[0:923], test = tokens[923:1847] (contiguous).
M1: HMM-3, 11 restarts (10 random seeded 20261007+i, 1 phase-informed),
    200 EM iters or dLL<1e-6; eps-floor 1e-6 on A,B post-EM. k=2+6+285=293.
M2: bigram-96 with Laplace alpha=1. k=96*95=9120.
Metrics: held-out mean loglik per next-token on test (HMM via forward);
         BIC on train with n=922 transitions.
HMM wins decisively iff held-out LL/pos(HMM) > LL/pos(bigram) AND
dBIC = BIC_bigram - BIC_HMM > 10.
"""
import json
import os
import sys

import numpy as np

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

EPS = 1e-6


def forward_scaled(A, B, pi, obs):
    T, S = len(obs), A.shape[0]
    alpha = np.zeros((T, S))
    c = np.zeros(T)
    alpha[0] = pi * B[:, obs[0]]
    c[0] = alpha[0].sum()
    alpha[0] /= c[0]
    for t in range(1, T):
        alpha[t] = (alpha[t - 1] @ A) * B[:, obs[t]]
        c[t] = alpha[t].sum()
        alpha[t] /= c[t]
    return alpha, c


def baum_welch(obs, S, O, seed, init_B=None, max_iter=200, tol=1e-6):
    rng = np.random.default_rng(seed)
    T = len(obs)
    pi = rng.dirichlet(np.ones(S))
    A = np.vstack([rng.dirichlet(np.ones(S)) for _ in range(S)])
    if init_B is None:
        B = np.vstack([rng.dirichlet(np.ones(O)) for _ in range(S)])
    else:
        B = init_B.copy()
    prev_ll = -np.inf
    for it in range(max_iter):
        alpha, c = forward_scaled(A, B, pi, obs)
        beta = np.zeros((T, S))
        beta[-1] = 1.0 / c[-1]
        for t in range(T - 2, -1, -1):
            beta[t] = (A * B[:, obs[t + 1]][None, :]) @ beta[t + 1] / c[t]
        gamma = alpha * beta
        gamma /= gamma.sum(1, keepdims=True)
        xi = np.zeros((T - 1, S, S))
        for t in range(T - 1):
            xi[t] = (alpha[t][:, None] * A *
                     B[:, obs[t + 1]][None, :] * beta[t + 1][None, :])
            xi[t] /= xi[t].sum()
        pi = gamma[0] / gamma[0].sum()
        A = xi.sum(0) / xi.sum(0).sum(1, keepdims=True)
        for s in range(S):
            w = gamma[:, s]
            for o in range(O):
                B[s, o] = w[obs == o].sum()
            B[s] /= B[s].sum()
        ll = float(np.log(c).sum())
        if abs(ll - prev_ll) < tol:
            break
        prev_ll = ll
    return A, B, pi, float(np.log(forward_scaled(A, B, pi, obs)[1]).sum())


def main():
    pairs = load_pairs_repaired()[0]
    groups = sorted(set(pairs))
    g2i = {g: i for i, g in enumerate(groups)}
    toks = np.array([g2i[g] for g in pairs])
    train, test = toks[:923], toks[923:]
    n_train_trans = len(train) - 1  # 922
    O = len(groups)  # 96 -- pinned to the full inventory, not train max

    # ---- M1: HMM-3 ----
    labels = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                         'phase_map_repaired.json')))
    train_phases = np.array([labels[pairs[i]] for i in range(923)])
    init_B_phase = np.zeros((3, O))
    for s, ph in enumerate('ABC'):
        for o in range(O):
            init_B_phase[s, o] = ((train == o) & (train_phases == ph)).sum() + 0.01
        init_B_phase[s] /= init_B_phase[s].sum()

    best = None
    inits = [('random', 20261007 + i, None) for i in range(10)]
    inits.append(('phase-informed', 999, init_B_phase))
    for name, seed, ib in inits:
        A, B, pi, ll = baum_welch(train, 3, O, seed, init_B=ib)
        tag = '%s/%d' % (name, seed)
        print('restart %-18s train LL=%.2f' % (tag, ll), flush=True)
        if best is None or ll > best[0]:
            best = (ll, A, B, pi, tag)
    ll_tr, A, B, pi, tag = best
    print('best restart:', tag, 'LL=%.2f' % ll_tr)
    A = np.maximum(A, EPS)
    A /= A.sum(1, keepdims=True)
    B = np.maximum(B, EPS)
    B /= B.sum(1, keepdims=True)
    _, c_tr = forward_scaled(A, B, pi, train)
    ll_train = float(np.log(c_tr).sum())
    _, c_te = forward_scaled(A, B, pi, test)
    ll_test = float(np.log(c_te).sum())
    hmm_held = ll_test / (len(test) - 1)
    k_hmm = 2 + 6 + 3 * 95
    bic_hmm = -2 * ll_train + k_hmm * np.log(n_train_trans)
    print('HMM-3: train LL=%.2f held-out LL/pos=%.4f k=%d BIC=%.1f'
          % (ll_train, hmm_held, k_hmm, bic_hmm))

    # ---- M2: bigram-96, Laplace alpha=1 ----
    cnt = np.zeros((O, O))
    np.add.at(cnt, (train[:-1], train[1:]), 1)
    Pbg = (cnt + 1) / (cnt.sum(1, keepdims=True) + O)
    llb_tr = float(np.log(Pbg[train[:-1], train[1:]]).sum())
    llb_te = float(np.log(Pbg[test[:-1], test[1:]]).sum())
    bg_held = llb_te / (len(test) - 1)
    k_bg = O * (O - 1)
    bic_bg = -2 * llb_tr + k_bg * np.log(n_train_trans)
    print('bigram-96: train LL=%.2f held-out LL/pos=%.4f k=%d BIC=%.1f'
          % (llb_tr, bg_held, k_bg, bic_bg))

    d_held = hmm_held - bg_held
    d_bic = bic_bg - bic_hmm
    win = d_held > 0 and d_bic > 10
    print('delta held-out LL/pos (HMM-big): %+.4f' % d_held)
    print('delta BIC (big-HMM): %+.1f -> %s'
          % (d_bic, 'HMM WINS DECISIVELY' if win else 'no decisive HMM win'))

    # hidden-state <-> phase alignment (descriptive)
    post = np.zeros((3, 4))
    alpha, _ = forward_scaled(A, B, pi, train)
    gamma = alpha  # scaled alpha ~ posterior up to constant per t
    ph_idx = {'A': 0, 'B': 1, 'C': 2, 'R': 3}
    for t in range(len(train)):
        post[:, ph_idx[train_phases[t]]] += gamma[t]
    post /= post.sum(1, keepdims=True)
    print('hidden-state x phase posterior mass:')
    for s in range(3):
        print('  state%d:' % s,
              {p: round(float(post[s, ph_idx[p]]), 3) for p in 'ABCR'})

    json.dump({'hmm': {'best_restart': tag, 'train_LL': ll_train,
                       'held_LL_per_pos': hmm_held, 'k': k_hmm,
                       'BIC': bic_hmm},
               'bigram': {'train_LL': llb_tr, 'held_LL_per_pos': bg_held,
                          'k': k_bg, 'BIC': bic_bg},
               'delta_held': d_held, 'delta_BIC': d_bic,
               'hmm_wins_decisively': bool(win),
               'state_phase_posterior': post.tolist()},
              open('hmm_results.json', 'w'), indent=1)
    print('wrote hmm_results.json')


if __name__ == '__main__':
    main()
