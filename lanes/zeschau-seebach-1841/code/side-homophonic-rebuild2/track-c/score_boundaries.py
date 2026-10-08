#!/usr/bin/env python3
"""TRACK-C scoring: boundary-aware score B(D) per PREREG §2.

Cleared by red-team R3 GO (2026-10-07); §4 hygiene gate PASSED (0 shared
15-grams, hygiene_gate.json).

B(D) = max over segmentations w_1..w_n of X=D (used as-is, already in the
projected phonetic-class alphabet):
    dp[0]=0
    dp[j] = max_{i in [max(0,j-20), j-1]} dp[i] + logP(X[i:j]) + ln L(len) + ln rho
    tie-break: i ascending, replace on strictly greater (deterministic)
    B(D) = dp[m]

logP(w) = ln((c(w)+1)/Z), Z = N+V=497455; OOV: ln(1/Z).
L(k): add-1 length distribution from word_stats.json (bin "20" = 20+).
ln rho: boundary-count log-prior per word.

Verdict: M = B(truth) - B(salad); PROMISING iff M>=+800; NEUTRAL iff
-800<M<+800; BACKFIRE iff M<=-800.
"""
import hashlib
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(LANE, 'code', 'side-homophonic-rebuild', 'solver'))
from phonetics import alphabet  # noqa: E402

ALPHA = 1.0
MAXWLEN = 20
TRUTH_SHA = '165fa8af91ae3ecf03305458a3f6204530f6e16cf52bfec66160f7848dda61f1'
SALAD_SHA = '8fb3ba26146dbc1eed2d528740ea6819a7bd0c4104adc18e75c093e316b95199'


def load_inputs():
    d = json.load(open(os.path.join(HERE, 'decodes.json')))
    for k, sha in (('truth', TRUTH_SHA), ('salad', SALAD_SHA)):
        t = d[k]['text']
        h = hashlib.sha256(t.encode()).hexdigest()
        assert h == sha, f'{k} sha mismatch: {h} != {sha}'
        assert set(t) <= set(alphabet()), f'{k} charset outside projected alphabet'
    stats = json.load(open(os.path.join(HERE, 'word_stats.json')))
    vocab = json.load(open(os.path.join(HERE, 'word_vocab.json')))
    N, V = stats['N_tokens'], stats['V_types_ge2']
    assert N == vocab['N'] and V == vocab['V']
    Z = N + ALPHA * V
    ln_rho = math.log(stats['rho_words_per_char'])
    ln_oov = math.log(ALPHA / Z)
    lnL = {int(k): math.log(v) for k, v in stats['len_dist'].items()}
    counts = vocab['counts']
    return d, N, V, Z, ln_rho, ln_oov, lnL, counts


def score_decode(X, counts, Z, ln_rho, ln_oov, lnL):
    m = len(X)
    NEG = float('-inf')
    dp = [NEG] * (m + 1)
    bp = [-1] * (m + 1)
    dp[0] = 0.0
    logp_cache = {}

    def logp(w):
        v = logp_cache.get(w)
        if v is None:
            c = counts.get(w)
            v = math.log((c + ALPHA) / Z) if c is not None else ln_oov
            logp_cache[w] = v
        return v

    for j in range(1, m + 1):
        best, bi = NEG, -1
        lo = max(0, j - MAXWLEN)
        # i ascending; strict > => ties keep smallest i (longest leftmost word)
        for i in range(lo, j):
            ln = j - i
            s = dp[i] + logp(X[i:j]) + lnL[ln if ln < MAXWLEN else MAXWLEN] + ln_rho
            if s > best:
                best, bi = s, i
        dp[j], bp[j] = best, bi
    # backtrack
    words, comps = [], []
    j = m
    while j > 0:
        i = bp[j]
        assert i >= 0, 'unreachable position in DP backtrack'
        w = X[i:j]
        words.append(w)
        ln = j - i
        comps.append((logp(w), lnL[ln if ln < MAXWLEN else MAXWLEN], ln_rho))
        j = i
    words.reverse()
    comps.reverse()
    W_uni = sum(c[0] for c in comps)
    W_len = sum(c[1] for c in comps)
    W_bnd = sum(c[2] for c in comps)
    n_oov = sum(1 for w in words if w not in counts)
    return {'B': dp[m], 'W_uni': W_uni, 'W_len': W_len, 'W_bnd': W_bnd,
            'n_words': len(words), 'mean_wlen': m / len(words),
            'n_oov': n_oov, 'words_head': words[:18]}


def main():
    d, N, V, Z, ln_rho, ln_oov, lnL, counts = load_inputs()
    print(f'model: N={N} V={V} Z={Z} ln_rho={ln_rho:.4f} ln_oov={ln_oov:.4f}')
    res = {}
    for k in ('truth', 'salad'):
        X = d[k]['text']
        r = score_decode(X, counts, Z, ln_rho, ln_oov, lnL)
        res[k] = r
        print(f"[{k}] len={len(X)} B={r['B']:.1f} "
              f"W_uni={r['W_uni']:.1f} W_len={r['W_len']:.1f} W_bnd={r['W_bnd']:.1f} "
              f"n={r['n_words']} meanlen={r['mean_wlen']:.2f} oov={r['n_oov']}")
        print(f"   seg head: {'|'.join(r['words_head'])}")
    M = res['truth']['B'] - res['salad']['B']
    dW_uni = res['truth']['W_uni'] - res['salad']['W_uni']
    dW_len = res['truth']['W_len'] - res['salad']['W_len']
    dW_bnd = res['truth']['W_bnd'] - res['salad']['W_bnd']
    verdict = 'PROMISING' if M >= 800 else ('BACKFIRE' if M <= -800 else 'NEUTRAL')
    print(f'MARGIN M = B(truth)-B(salad) = {M:.1f} nats')
    print(f'   dW_uni={dW_uni:.1f} dW_len={dW_len:.1f} dW_bnd={dW_bnd:.1f}')
    print(f'VERDICT: {verdict}')
    with open(os.path.join(HERE, 'boundary_scores.json'), 'w') as f:
        json.dump({'model': {'N': N, 'V': V, 'Z': Z, 'ln_rho': ln_rho,
                             'ln_oov': ln_oov},
                   'truth': {k: v for k, v in res['truth'].items() if k != 'words_head'},
                   'salad': {k: v for k, v in res['salad'].items() if k != 'words_head'},
                   'truth_seg_head': res['truth']['words_head'],
                   'salad_seg_head': res['salad']['words_head'],
                   'M': M, 'dW_uni': dW_uni, 'dW_len': dW_len, 'dW_bnd': dW_bnd,
                   'verdict': verdict}, f, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
