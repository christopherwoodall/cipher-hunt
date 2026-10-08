#!/usr/bin/env python3
"""TRACK-C v2 scoring: boundary-aware score B_v2(D) per PREREG-C-v2.md.

REPAIR of the v1 degeneracy (RESULTS.md §§2-5): the OOV log-rate
ln(alpha/Z) = -13.12 per word-form, independent of length, let the DP
minimize word count (20-char OOV chunks; B(D) ~= -1.34*|D|, a length
penalty in disguise). v2: logP_oov(w) = |w| * ln(p_char) with p_char pinned
(pre-registered): p_char = 5/497455 = 1.0051160406468926e-05, anchored to
the unigram rate of the rarest in-vocab single-char word ('q'/'z', count 4,
add-alpha alpha=1.0, Z=N+alpha*V=497455). ln(p_char) = -11.507822466794325.

Everything else in v1 PREREG §2 unchanged: same corpus constants
(N,V,Z,rho,L), same DP recurrence (window 20, i-ascending tie-break),
same W_len/W_bnd.

Verdict: M = B_v2(truth) - B_v2(salad); PROMISING-v2 iff M>=+800 AND the
validity precondition holds (truth argmax mean len in [1.765,7.059] AND
>=50% of truth argmax words in-vocab). Otherwise NULL-v2. STOP before the
§6 pilot: no pilot code runs here.

Control/diagnostic only. Never touches R5005. No RNG.
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
# Pre-registered v2 constant (PREREG-C-v2.md §1.1): (rarest-1char-count + alpha)/Z
# rarest 1-char types: 'q','z' count 4; alpha=1.0; Z=N+alpha*V=486789+10666=497455
P_CHAR = 5.0 / 497455.0
LN_P_CHAR = math.log(P_CHAR)  # -11.507822466794325
assert abs(LN_P_CHAR - (-11.507822466794325)) < 1e-9, 'p_char drift'

TRUTH_SHA = '165fa8af91ae3ecf03305458a3f6204530f6e16cf52bfec66160f7848dda61f1'
SALAD_SHA = '8fb3ba26146dbc1eed2d528740ea6819a7bd0c4104adc18e75c093e316b95199'

REF_MEAN_LEN = 3.529167668127258  # word_stats.json mean_word_len
VALID_LEN_LO = REF_MEAN_LEN / 2.0
VALID_LEN_HI = REF_MEAN_LEN * 2.0


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
    assert Z == 497455.0, f'Z drift: {Z}'
    ln_rho = math.log(stats['rho_words_per_char'])
    lnL = {int(k): math.log(v) for k, v in stats['len_dist'].items()}
    counts = vocab['counts']
    return d, N, V, Z, ln_rho, lnL, counts


def score_decode(X, counts, Z, ln_rho, lnL):
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
            if c is not None:
                v = math.log((c + ALPHA) / Z)
            else:
                # v2 REPAIR: length-scaled OOV, not per-form ln(alpha/Z)
                v = len(w) * LN_P_CHAR
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
    n = len(words)
    return {'B': dp[m], 'W_uni': W_uni, 'W_len': W_len, 'W_bnd': W_bnd,
            'n_words': n, 'mean_wlen': m / n,
            'n_oov': n_oov, 'n_invocab': n - n_oov,
            'invocab_frac': (n - n_oov) / n,
            'words': words}


def validity_check(res):
    t = res['truth']
    len_ok = VALID_LEN_LO <= t['mean_wlen'] <= VALID_LEN_HI
    vocab_ok = t['invocab_frac'] >= 0.50
    return {'len_ok': len_ok, 'vocab_ok': vocab_ok,
            'non_degenerate': len_ok and vocab_ok,
            'len_band': [VALID_LEN_LO, VALID_LEN_HI]}


def main():
    d, N, V, Z, ln_rho, lnL, counts = load_inputs()
    print(f'model v2: N={N} V={V} Z={Z} ln_rho={ln_rho:.4f} '
          f'ln_p_char={LN_P_CHAR:.4f} (OOV = |w|*ln_p_char)')
    res = {}
    for k in ('truth', 'salad'):
        X = d[k]['text']
        r = score_decode(X, counts, Z, ln_rho, lnL)
        res[k] = r
        print(f"[{k}] len={len(X)} B={r['B']:.1f} "
              f"W_uni={r['W_uni']:.1f} W_len={r['W_len']:.1f} W_bnd={r['W_bnd']:.1f} "
              f"n={r['n_words']} meanlen={r['mean_wlen']:.3f} "
              f"invocab={r['n_invocab']}/{r['n_words']} ({r['invocab_frac']:.3f})")
        print(f"   seg head: {'|'.join(r['words'][:16])}")
    M = res['truth']['B'] - res['salad']['B']
    dW_uni = res['truth']['W_uni'] - res['salad']['W_uni']
    dW_len = res['truth']['W_len'] - res['salad']['W_len']
    dW_bnd = res['truth']['W_bnd'] - res['salad']['W_bnd']
    vc = validity_check(res)
    bar_ok = M >= 800
    promising = bar_ok and vc['non_degenerate']
    verdict = 'PROMISING-v2' if promising else 'NULL-v2'
    print(f'MARGIN M = B_v2(truth)-B_v2(salad) = {M:.1f} nats')
    print(f'   dW_uni={dW_uni:.1f} dW_len={dW_len:.1f} dW_bnd={dW_bnd:.1f}')
    print(f'VALIDITY: bar_ok={bar_ok} len_ok={vc["len_ok"]} '
          f'(truth mean {res["truth"]["mean_wlen"]:.3f} in [{vc["len_band"][0]:.3f},{vc["len_band"][1]:.3f}]) '
          f'vocab_ok={vc["vocab_ok"]} (truth invocab frac {res["truth"]["invocab_frac"]:.3f}) '
          f'-> non_degenerate={vc["non_degenerate"]}')
    print(f'VERDICT: {verdict}')
    with open(os.path.join(HERE, 'boundary_scores_v2.json'), 'w') as f:
        json.dump({'model': {'N': N, 'V': V, 'Z': Z, 'ln_rho': ln_rho,
                             'p_char': P_CHAR, 'ln_p_char': LN_P_CHAR,
                             'oov_model': '|w| * ln(p_char)',
                             'ref_mean_len': REF_MEAN_LEN},
                   'truth': {k: v for k, v in res['truth'].items() if k != 'words'},
                   'salad': {k: v for k, v in res['salad'].items() if k != 'words'},
                   'truth_seg_head': res['truth']['words'][:30],
                   'salad_seg_head': res['salad']['words'][:30],
                   'M': M, 'dW_uni': dW_uni, 'dW_len': dW_len, 'dW_bnd': dW_bnd,
                   'validity': vc, 'bar_ok': bar_ok,
                   'verdict': verdict}, f, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
