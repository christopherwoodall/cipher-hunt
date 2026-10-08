#!/usr/bin/env python3
"""TRACK-C v3 post-run diagnostics (NOT a re-run of the registered margin).

Re-derives the v3 argmax tilings with the EXACT deterministic code path of
score_boundaries_v3.py (imported, not duplicated) and asserts byte-identical
B values against boundary_scores_v3.json. Extra diagnostics for RESULTS-C-v3:
  - seen-pair share on the v3 argmaxes (v2 §7 parallel)
  - per-transition mean bigram rates
  - first-word values (R9b edge-effect check)
  - length histograms
  - OOV-transition footprint (R9a)
No scoring model change; no pilot; deterministic.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import score_boundaries_v3 as v3

d, N, V, Z, ln_rho, lnL, counts = v3.load_inputs()
vocab_set = set(counts.keys())
pair_counts, ctx_counts = v3.build_bigram_model(vocab_set)

reg = json.load(open(os.path.join(HERE, 'boundary_scores_v3.json')))
print('=== diagnostics (B must match registered run exactly) ===')
tilings = {}
for k in ('truth', 'salad'):
    X = d[k]['text']
    r = v3.score_decode(X, counts, vocab_set, Z, ln_rho, lnL,
                        pair_counts, ctx_counts, V)
    assert abs(r['B'] - reg[k]['B']) < 1e-9, f'B drift on {k}'
    tilings[k] = r
    words = r['words']
    n = len(words)
    # seen-pair share: fraction of transitions with c(u,v) > 0
    seen = 0
    rates = r['bilist']
    for i in range(n - 1):
        if pair_counts.get((words[i], words[i + 1]), 0) > 0:
            seen += 1
    mean_rate = sum(rates) / len(rates) if rates else float('nan')
    print(f'[{k}] B match ok ({r["B"]:.1f}); n={n}, transitions={n-1}')
    print(f'  seen-pair share: {seen}/{n-1} = {seen/(n-1):.4f}')
    print(f'  mean log bigram rate /transition: {mean_rate:.4f} '
          f'(per-char W_bi={r["W_bi"]/len(X):.4f})')
    print(f'  W_bi/transition = {r["W_bi"]/(n-1):.4f} nats')
    # first-word edge effect (R9b): first word is unigram-only
    w0 = words[0]
    c = counts.get(w0)
    lp = math.log((c + v3.ALPHA) / Z) if c is not None else len(w0) * v3.LN_P_CHAR
    ln = len(w0)
    s0 = lp + lnL[ln if ln < v3.MAXWLEN else v3.MAXWLEN] + ln_rho
    print(f'  first word: {w0!r} (len {len(w0)}), s(w0)={s0:.2f} '
          f'= {100*s0/r["B"]:.2f}% of B; mean |transition|={-mean_rate:.2f} '
          f'nats -> first word ~= {abs(s0/mean_rate):.1f} transitions')
    # OOV-transition footprint (R9a): transitions touching an OOV word
    oov_idx = {i for i, w in enumerate(words) if w not in counts}
    touch = sum(1 for i in range(n - 1)
                if i in oov_idx or (i + 1) in oov_idx)
    print(f'  OOV words: {len(oov_idx)} ({100*len(oov_idx)/n:.2f}%), '
          f'transitions touching OOV: {touch}/{n-1}')
    # length histogram
    from collections import Counter
    hist = Counter(len(w) for w in words)
    print(f'  len hist: {dict(sorted(hist.items()))}')
    # top first-16 sample already in main run; print words 30-45 too
    print(f'  seg 30-46: {"|".join(words[30:46])}')
