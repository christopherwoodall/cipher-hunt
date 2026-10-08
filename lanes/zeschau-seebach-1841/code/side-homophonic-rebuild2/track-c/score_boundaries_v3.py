#!/usr/bin/env python3
"""TRACK-C v3 scoring: word-bigram boundary score B_v3(D) per PREREG-C-v3.md.

REPAIR of the v2 null (RESULTS-C-v2.md §§4-5): a word-UNIGRAM model cannot
see adversarial boundary placement when the salad's tiles are themselves
common French word-forms by construction. v3 adds word-bigram transition
log-rates so word ORDER (the boundary signal) is scored.

Frozen spec (PREREG-C-v3.md §1):
  s(w) = logP_uni(w) + ln L(|w|) + ln rho      (v2 pieces, unchanged)
  logP_uni(w) = ln((c(w)+alpha)/Z) if w in V else |w|*ln(p_char)
  logP_bi(u,v) = ln((c(u,v)+1)/(c(u)+V)), V=10,666, add-1 over the SAME
      diplomatic corpus / same tokenizer as v2 (pairs with either token
      OOV are mechanically c(u,v)=0; c(u)=0 for u not in V).
  lambda_bi = 1.0 (pinned, hard-coded).
  First word of a tiling: unigram-only (no bigram term).
  DP: state dp[i][w] = best score of tiling of D[0:i] ending with
      w = D[j:i]; window MAXWLEN=20.
      j=0: dp[i][w] = s(w).
      else: dp[i][w] = s(w) + max_u [ dp[j][u] + lambda_bi*logP_bi(u,w) ],
            u ranges over D[k:j], k in [max(0,j-20), j-1].
      Tie-break (pinned): j ascending; for fixed j, u in ascending
      lexicographic word-string order; keep the FIRST candidate that is
      strictly greater (exact float `>`, no tolerance). Backpointers
      follow the same order. B_v3(D) = max_w dp[m][w] (j ascending).
  Deterministic. No RNG. Never touches R5005.

Verdict: M = B_v3(truth)-B_v3(salad); PROMISING-v3 iff
  (a) M >= +800, (b) non-degenerate (truth argmax mean len in
  [1.765,7.059] AND >=50% in-vocab), (c) STRICT per-char inequality
  B_v3(truth)/|truth| > B_v3(salad)/|salad|. Else NULL-v3.

STOP before the §6 pilot: no pilot code here; the pilot needs a second
red-team clearance after the static result.
"""
import hashlib
import json
import math
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(LANE, 'code', 'side-homophonic-rebuild', 'solver'))
from phonetics import alphabet, project  # noqa: E402

ALPHA = 1.0
MAXWLEN = 20
P_CHAR = 5.0 / 497455.0
LN_P_CHAR = math.log(P_CHAR)  # -11.507822466794325
assert abs(LN_P_CHAR - (-11.507822466794325)) < 1e-9, 'p_char drift'

LAMBDA_BI = 1.0  # pinned (PREREG-C-v3.md §1.3); NOT tuned after any number

TRUTH_SHA = '165fa8af91ae3ecf03305458a3f6204530f6e16cf52bfec66160f7848dda61f1'
SALAD_SHA = '8fb3ba26146dbc1eed2d528740ea6819a7bd0c4104adc18e75c093e316b95199'

REF_MEAN_LEN = 3.529167668127258
VALID_LEN_LO = REF_MEAN_LEN / 2.0
VALID_LEN_HI = REF_MEAN_LEN * 2.0

CORPUS_DIR = os.path.join(LANE, 'code', 'side-period', 'corpus')
FILES = [
    'nesselrode-v7.txt',
    'nesselrode-v8.txt',
    'nesselrode-v9.txt',
    'nesselrode-v10.txt',
    'pozzo-di-borgo-correspondance-v1.txt',
]
WORD_RE = re.compile(r"[A-Za-zÀ-ÿŒœÆæ]+")


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
    assert N == vocab['N'] and V == vocab['V'] == 10666, 'N/V drift'
    Z = N + ALPHA * V
    assert Z == 497455.0, f'Z drift: {Z}'
    ln_rho = math.log(stats['rho_words_per_char'])
    lnL = {int(k): math.log(v) for k, v in stats['len_dist'].items()}
    counts = vocab['counts']
    return d, N, V, Z, ln_rho, lnL, counts


def build_bigram_model(vocab_set):
    """Fit add-1 word-bigram counts from the SAME corpus / tokenizer as v2.

    Method choice on the record (PREREG §1.2 says "Tokenize the corpus;
    count consecutive token pairs" without a file-junction rule): each
    file is tokenized independently (WORD_RE -> phonetics.project(),
    skipping empty projections, mirroring word_stats.py) and pairs are
    counted WITHIN files only — no cross-file junction pairs. Only 4
    junction pairs out of ~486k are affected; immaterial either way.
    Only pairs with both tokens in V (MIN_COUNT=2 vocab) are kept;
    c(u) = sum_v c(u,v) over kept pairs.
    """
    pair_counts = Counter()
    ctx_counts = Counter()
    seqs = []
    for fn in FILES:
        raw = open(os.path.join(CORPUS_DIR, fn), encoding='utf-8',
                   errors='replace').read()
        seq = []
        for t in WORD_RE.findall(raw):
            w = project(t)
            if not w:
                continue
            seq.append(w)
        seqs.append(seq)
    for seq in seqs:
        for u, v in zip(seq, seq[1:]):
            if u in vocab_set and v in vocab_set:
                pair_counts[(u, v)] += 1
                ctx_counts[u] += 1
    return pair_counts, ctx_counts


def score_decode(X, counts, vocab_set, Z, ln_rho, lnL,
                 pair_counts, ctx_counts, V):
    m = len(X)
    # s(w) cache: v2 pieces
    s_cache = {}

    def s_of(w):
        v = s_cache.get(w)
        if v is None:
            c = counts.get(w)
            if c is not None:
                lp = math.log((c + ALPHA) / Z)
            else:
                lp = len(w) * LN_P_CHAR
            ln = len(w)
            v = lp + lnL[ln if ln < MAXWLEN else MAXWLEN] + ln_rho
            s_cache[w] = v
        return v

    # bigram log-rate tables (precomputed, PREREG §1.5)
    bi_seen = {}
    bi_unseen_rate = {}   # per in-vocab context u: ln(1/(c(u)+V))
    for (u, v), cuv in pair_counts.items():
        bi_seen[(u, v)] = math.log((cuv + 1.0) / (ctx_counts[u] + V))
    for u in vocab_set:
        bi_unseen_rate[u] = math.log(1.0 / (ctx_counts.get(u, 0) + V))
    LN_1_V = math.log(1.0 / V)  # OOV-context fallback (-9.2746), on record

    def logp_bi(u, v):
        if u not in vocab_set:
            return LN_1_V                      # OOV context: c(u)=0
        r = bi_seen.get((u, v))
        if r is not None:
            return r
        return bi_unseen_rate[u]               # in-vocab u, unseen pair

    NEG = float('-inf')
    # last[i]: dict j -> best tiling score of D[0:i] ending with word D[j:i]
    # bp[i]:   dict j -> (k, u_str) predecessor (start k of prev word, its string)
    last = [dict() for _ in range(m + 1)]
    bp = [dict() for _ in range(m + 1)]

    for i in range(1, m + 1):
        lo = max(0, i - MAXWLEN)
        # j ascending (PREREG pinned tie-break outer order)
        for j in range(lo, i):
            w = X[j:i]
            sw = s_of(w)
            if j == 0:
                last[i][j] = sw
                bp[i][j] = None
                continue
            best, bestu = NEG, None
            # predecessors u = D[k:j], k in window; iterate u STRINGS
            # lexicographic-ascending; keep first strictly-greater
            uwords = sorted({X[k:j] for k in range(max(0, j - MAXWLEN), j)})
            for u in uwords:
                k = j - len(u)  # start of this u (string determines k)
                cand = last[j][k] + LAMBDA_BI * logp_bi(u, w) + sw
                if cand > best:  # exact float >, no tolerance
                    best, bestu = cand, (k, u)
            last[i][j] = best
            bp[i][j] = bestu

    # B_v3(D) = max_w dp[m][w], j ascending, first strictly-greater
    B, Bj = NEG, None
    for j in sorted(last[m].keys()):
        if last[m][j] > B:
            B, Bj = last[m][j], j

    # backtrack
    words, uni, bilist, lens = [], [], [], []
    i, j = m, Bj
    assert j is not None
    while True:
        w = X[j:i]
        words.append(w)
        c = counts.get(w)
        uni.append(math.log((c + ALPHA) / Z) if c is not None else len(w) * LN_P_CHAR)
        ln = len(w)
        lens.append(lnL[ln if ln < MAXWLEN else MAXWLEN])
        pre = bp[i][j]
        if pre is None:
            break
        k, u = pre
        bilist.append(logp_bi(u, w))  # transition u -> w
        i, j = j, k
    words.reverse()
    uni.reverse()
    bilist.reverse()
    lens.reverse()

    W_uni = sum(uni)
    W_bi = sum(bilist) * LAMBDA_BI
    W_len = sum(lens)
    n = len(words)
    W_bnd = n * ln_rho
    n_oov = sum(1 for w in words if w not in counts)
    # sanity: component sums reconstruct B
    recon = W_uni + W_bi + W_len + W_bnd
    assert abs(recon - B) < 1e-6 * max(1.0, abs(B)), f'component drift: {recon} vs {B}'
    return {'B': B, 'W_uni': W_uni, 'W_bi': W_bi, 'W_len': W_len, 'W_bnd': W_bnd,
            'n_words': n, 'n_transitions': len(bilist),
            'mean_wlen': m / n,
            'n_oov': n_oov, 'n_invocab': n - n_oov,
            'invocab_frac': (n - n_oov) / n,
            'oov_share': n_oov / n,
            'words': words,
            'bilist': bilist}


def validity_check(res):
    t = res['truth']
    len_ok = VALID_LEN_LO <= t['mean_wlen'] <= VALID_LEN_HI
    vocab_ok = t['invocab_frac'] >= 0.50
    return {'len_ok': len_ok, 'vocab_ok': vocab_ok,
            'non_degenerate': len_ok and vocab_ok,
            'len_band': [VALID_LEN_LO, VALID_LEN_HI]}


def main():
    d, N, V, Z, ln_rho, lnL, counts = load_inputs()
    vocab_set = set(counts.keys())
    print(f'model v3: N={N} V={V} Z={Z} ln_rho={ln_rho:.4f} '
          f'lambda_bi={LAMBDA_BI} (pinned)')
    pair_counts, ctx_counts = build_bigram_model(vocab_set)
    print(f'bigram: {len(pair_counts)} distinct seen pairs, '
          f'{sum(pair_counts.values())} pair tokens, '
          f'{len(ctx_counts)} contexts with counts; '
          f'unseen-fallback ln(1/V)={math.log(1.0/V):.4f}')
    res = {}
    for k in ('truth', 'salad'):
        X = d[k]['text']
        r = score_decode(X, counts, vocab_set, Z, ln_rho, lnL,
                         pair_counts, ctx_counts, V)
        res[k] = r
        m = len(X)
        print(f"[{k}] len={m} B_v3={r['B']:.1f} "
              f"W_uni={r['W_uni']:.1f} W_bi={r['W_bi']:.1f} "
              f"W_len={r['W_len']:.1f} W_bnd={r['W_bnd']:.1f} "
              f"n={r['n_words']} ntrans={r['n_transitions']} meanlen={r['mean_wlen']:.3f} "
              f"invocab={r['n_invocab']}/{r['n_words']} ({r['invocab_frac']:.3f}) "
              f"oov_share={r['oov_share']:.4f}")
        print(f"   per-char B={r['B']/m:.4f} W_uni={r['W_uni']/m:.4f} "
              f"W_bi={r['W_bi']/m:.4f} W_len={r['W_len']/m:.4f} "
              f"W_bnd={r['W_bnd']/m:.4f}")
        print(f"   seg head: {'|'.join(r['words'][:16])}")

    T, S = res['truth'], res['salad']
    mt, ms = len(d['truth']['text']), len(d['salad']['text'])
    M = T['B'] - S['B']
    comps = ['W_uni', 'W_bi', 'W_len', 'W_bnd']
    dcomp = {c: T[c] - S[c] for c in comps}
    assert abs(sum(dcomp.values()) - M) < 1e-6 * max(1.0, abs(M))

    vc = validity_check(res)
    bar_ok = M >= 800
    perchar_ok = (T['B'] / mt) > (S['B'] / ms)  # STRICT inequality
    promising = bar_ok and vc['non_degenerate'] and perchar_ok
    verdict = 'PROMISING-v3' if promising else 'NULL-v3'

    print('MARGIN M = B_v3(truth)-B_v3(salad) = %.1f nats' % M)
    for c in comps:
        print(f'   d{c}={dcomp[c]:+.1f}')
    print(f"GATES: (a) M>=800: {bar_ok}  "
          f"(b) non-degenerate: {vc['non_degenerate']} "
          f"(len_ok={vc['len_ok']}, vocab_ok={vc['vocab_ok']})  "
          f"(c) per-char B truth {T['B']/mt:.4f} > salad {S['B']/ms:.4f}: {perchar_ok}")
    print(f'VERDICT: {verdict}')

    with open(os.path.join(HERE, 'boundary_scores_v3.json'), 'w') as f:
        json.dump({'model': {'N': N, 'V': V, 'Z': Z, 'ln_rho': ln_rho,
                             'lambda_bi': LAMBDA_BI,
                             'p_char': P_CHAR, 'ln_p_char': LN_P_CHAR,
                             'oov_model': '|w| * ln(p_char)',
                             'bigram': 'add-1 ln((c(u,v)+1)/(c(u)+V)), '
                                       'pairs within-file, both-in-V only',
                             'n_seen_pairs': len(pair_counts),
                             'n_pair_tokens': sum(pair_counts.values()),
                             'ref_mean_len': REF_MEAN_LEN},
                   'truth': {k: v for k, v in T.items() if k not in ('words', 'bilist')},
                   'salad': {k: v for k, v in S.items() if k not in ('words', 'bilist')},
                   'truth_seg_head': T['words'][:30],
                   'salad_seg_head': S['words'][:30],
                   'truth_len': mt, 'salad_len': ms,
                   'M': M, 'dcomp': dcomp,
                   'gate_a_bar': bar_ok, 'gate_b_validity': vc,
                   'gate_c_perchar': {'truth_rate': T['B'] / mt,
                                      'salad_rate': S['B'] / ms,
                                      'strict_inequality': perchar_ok},
                   'verdict': verdict}, f, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
