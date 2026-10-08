#!/usr/bin/env python3
"""TRACK-C v4 scoring: length-neutralized boundary score B_v4(D) per PREREG-C-v4.md.

  B_v4(D) = B_v3(D) - rhat * |D|

rhat = S_R / m_R is the expected per-char B_v3 rate of genuine reference
French, fit on REFERENCE TEXT ONLY: the 5 diplomatic corpus files, natural
tokenization (WORD_RE -> phonetics.project() defaults, empty projections
skipped), v2/v3 constants verbatim, lambda_bi=1.0, first-token-per-file
unigram-only, within-file consecutive bigram pairs (no cross-file junctions).

Binding execution order (PREREG-C-v4.md section 4):
  1. Fit rhat from the 5 corpus files and LOG it BEFORE any decode byte
     is read (decode sha256 re-verified later: truth 165fa8af.. / salad
     8fb3ba26..). Assert -25 < rhat < 0, else the run is VOID (no verdict).
  2. Re-run the v3 DP verbatim (imported, not duplicated) and ASSERT
     byte-identical argmax tilings to boundary_scores_v3.json. Any
     deviation = instrument failure, run VOID, no verdict.
  3. Compute B_v4, M_v4, the four gates, the R3b per-char decomposition,
     the (c1) perturbation table, the (c2) per-transition numbers, and
     OOV word-share on both argmaxes (R9a). No RNG. STOP before the
     section 6 joint pilot (separate red-team clearance required).

Verdict: PROMISING-v4 iff (a) M_v4 >= +800 at fitted rhat, (b) non-degenerate
argmax carried over, (c1) M_v4 >= +800 under rhat' in {0.8*rhat, 1.2*rhat},
(c2) mean per-transition bigram rate truth > salad AND seen-pair share truth
> salad, both strict. Else NULL-v4 (failing gates named).

No R5005 contact (standing grep-clean requirement).
"""
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(LANE, 'code', 'side-homophonic-rebuild', 'solver'))
sys.path.insert(0, HERE)
from phonetics import project  # noqa: E402
import score_boundaries_v3 as v3  # noqa: E402  (verbatim v3 DP; no decode read at import)

CORPUS_DIR = os.path.join(LANE, 'code', 'side-period', 'corpus')
FILES = [
    'nesselrode-v7.txt',
    'nesselrode-v8.txt',
    'nesselrode-v9.txt',
    'nesselrode-v10.txt',
    'pozzo-di-borgo-correspondance-v1.txt',
]
WORD_RE = re.compile(r"[A-Za-zÀ-ÿŒœÆæ]+")

V_PINNED = 10666  # PREREG-C-v4.md section 2.1; asserted == vocab['V'] in fit_rhat
LN_1_V = math.log(1.0 / V_PINNED)  # OOV-context fallback, verbatim v3 value
assert abs(LN_1_V - (-9.2746)) < 1e-3


def fit_rhat():
    """Phase 1: fit rhat from the 5 reference corpus files ONLY.

    Called BEFORE any decode byte is read. Returns (rhat, fit_log).
    """
    stats = json.load(open(os.path.join(HERE, 'word_stats.json')))
    vocab = json.load(open(os.path.join(HERE, 'word_vocab.json')))
    N, V = stats['N_tokens'], stats['V_types_ge2']
    assert N == vocab['N'] and V == vocab['V'] == 10666, 'N/V drift'
    Z = N + v3.ALPHA * V
    assert Z == 497455.0, f'Z drift: {Z}'
    ln_rho = math.log(stats['rho_words_per_char'])
    assert abs(ln_rho - (-1.2610620550768965)) < 1e-9, 'rho drift'
    lnL = {int(k): math.log(vv) for k, vv in stats['len_dist'].items()}
    counts = vocab['counts']
    vocab_set = set(counts.keys())

    # Frozen add-1 bigram tables (reference-fitted; reuse blessed by R10(e)).
    pair_counts, ctx_counts = v3.build_bigram_model(vocab_set)
    bi_seen = {}
    bi_unseen_rate = {}
    for (u, vv), cuv in pair_counts.items():
        bi_seen[(u, vv)] = math.log((cuv + 1.0) / (ctx_counts[u] + V))
    for u in vocab_set:
        bi_unseen_rate[u] = math.log(1.0 / (ctx_counts.get(u, 0) + V))

    def logp_uni(w):
        c = counts.get(w)
        if c is not None:
            return math.log((c + v3.ALPHA) / Z)
        return len(w) * v3.LN_P_CHAR

    def logp_bi(u, vv):
        if u not in vocab_set:
            return LN_1_V
        r = bi_seen.get((u, vv))
        if r is not None:
            return r
        return bi_unseen_rate[u]

    per_file = []
    S_R, m_R = 0.0, 0
    for fn in FILES:
        raw = open(os.path.join(CORPUS_DIR, fn), encoding='utf-8',
                   errors='replace').read()
        seq = []
        for t in WORD_RE.findall(raw):
            w = project(t)          # v2/v3 tokenizer verbatim (defaults)
            if not w:
                continue
            seq.append(w)
        K = len(seq)
        uni = sum(logp_uni(w) for w in seq)
        blen = sum(lnL[len(w) if len(w) < v3.MAXWLEN else v3.MAXWLEN]
                   for w in seq)
        bnd = K * ln_rho
        bi = sum(v3.LAMBDA_BI * logp_bi(seq[k - 1], seq[k])
                 for k in range(1, K))   # k=2..K 1-indexed; first token unigram-only
        S_F = uni + blen + bnd + bi
        m_F = sum(len(w) for w in seq)
        S_R += S_F
        m_R += m_F
        per_file.append({'file': fn, 'K_tokens': K, 'm_chars': m_F,
                         'S_F': S_F, 'S_F_per_char': S_F / m_F,
                         'W_uni': uni, 'W_bi': bi, 'W_len': blen,
                         'W_bnd': bnd,
                         'n_oov': sum(1 for w in seq if w not in counts)})
    rhat = S_R / m_R
    fit_log = {'per_file': per_file, 'S_R': S_R, 'm_R': m_R, 'rhat': rhat,
               'n_seen_pairs': len(pair_counts),
               'n_pair_tokens': sum(pair_counts.values())}
    return rhat, fit_log


def main():
    # ---- Phase 1: rhat fit (REFERENCE TEXT ONLY; no decode byte read yet)
    rhat, fit_log = fit_rhat()
    print('=== PHASE 1: rhat fit (reference text only) ===')
    for pf in fit_log['per_file']:
        print(f"  {pf['file']}: K={pf['K_tokens']} m={pf['m_chars']} "
              f"S_F={pf['S_F']:.1f} S_F/m={pf['S_F_per_char']:.4f} "
              f"(W_uni={pf['W_uni']:.1f} W_bi={pf['W_bi']:.1f} "
              f"W_len={pf['W_len']:.1f} W_bnd={pf['W_bnd']:.1f} "
              f"oov={pf['n_oov']})")
    print(f"  S_R={fit_log['S_R']:.1f} m_R={fit_log['m_R']} "
          f"-> rhat = {rhat:.6f} nats/char")
    # Log the fit BEFORE any decode is loaded.
    with open(os.path.join(HERE, 'rhat_fit_v4.json'), 'w') as f:
        json.dump(fit_log, f, ensure_ascii=False, indent=1)
    if not (-25.0 < rhat < 0.0):
        void = {'status': 'VOID', 'reason': 'rhat out of band (-25, 0)',
                'rhat': rhat, 'fit_log': fit_log}
        json.dump(void, open(os.path.join(HERE, 'VOID-v4.json'), 'w'),
                  ensure_ascii=False, indent=1)
        print(f'VOID: rhat={rhat} outside (-25, 0); no verdict. See VOID-v4.json')
        sys.exit(2)
    print('  rhat in band (-25, 0): proceeding to phase 2.')

    # ---- Phase 2: load decodes (sha re-verified) + verbatim v3 DP re-run
    d, N, V, Z, ln_rho, lnL, counts = v3.load_inputs()
    vocab_set = set(counts.keys())
    pair_counts, ctx_counts = v3.build_bigram_model(vocab_set)
    reg = json.load(open(os.path.join(HERE, 'boundary_scores_v3.json')))
    print('=== PHASE 2: v3 DP re-run (verbatim) + byte-identical drift check ===')
    res = {}
    for k, head_key in (('truth', 'truth_seg_head'), ('salad', 'salad_seg_head')):
        X = d[k]['text']
        r = v3.score_decode(X, counts, vocab_set, Z, ln_rho, lnL,
                            pair_counts, ctx_counts, V)
        res[k] = r
        problems = []
        if r['words'][:30] != reg[head_key]:
            problems.append(f'seg_head mismatch (first 30 words)')
        for fld in ('B', 'W_uni', 'W_bi', 'W_len', 'W_bnd', 'n_words',
                    'n_transitions', 'mean_wlen', 'n_oov', 'n_invocab',
                    'invocab_frac', 'oov_share'):
            if r[fld] != reg[k][fld]:
                problems.append(f'{fld}: {r[fld]!r} != {reg[k][fld]!r}')
        if len(X) != reg[k + '_len']:
            problems.append(f'decode length {len(X)} != {reg[k+"_len"]}')
        if problems:
            void = {'status': 'VOID-INSTRUMENT',
                    'reason': 'v3 DP drift: tiling/score not byte-identical to '
                              'boundary_scores_v3.json',
                    'decode': k, 'problems': problems}
            json.dump(void, open(os.path.join(HERE, 'VOID-v4.json'), 'w'),
                      ensure_ascii=False, indent=1)
            print(f'INSTRUMENT VOID on {k}:')
            for p in problems:
                print(f'  {p}')
            print('Run VOID (not a verdict). See VOID-v4.json')
            sys.exit(3)
        print(f'  [{k}] byte-identical to boundary_scores_v3.json '
              f'(B={r["B"]:.4f}, n={r["n_words"]}, head ok)')
    mt, ms = len(d['truth']['text']), len(d['salad']['text'])
    assert ms - mt == 1979, f'decode-length delta drift: {ms-mt} != 1979'
    T, S = res['truth'], res['salad']
    M_v3 = T['B'] - S['B']
    assert M_v3 == reg['M'], 'M_v3 drift'

    # ---- Phase 3: B_v4, M_v4, the four gates
    B4t = T['B'] - rhat * mt
    B4s = S['B'] - rhat * ms
    M_v4 = B4t - B4s
    dm = ms - mt  # 1979, asserted above
    # cross-check the arithmetic form M_v4 = M_v3 + dm * rhat
    assert abs(M_v4 - (M_v3 + dm * rhat)) < 1e-9 * max(1.0, abs(M_v4))

    gate_a = M_v4 >= 800.0
    vc = v3.validity_check(res)  # carried over from v2/v3 unchanged
    gate_b = vc['non_degenerate']
    c1 = {}
    for frac in (0.8, 1.2):
        rp = frac * rhat
        Mp = M_v3 + dm * rp
        c1[str(frac)] = {'rhat_prime': rp, 'M_v4': Mp, 'pass': Mp >= 800.0}
    gate_c1 = all(vv['pass'] for vv in c1.values())

    # (c2): per-transition bigram rate + seen-pair share, strict, on own tilings
    c2 = {}
    for k in ('truth', 'salad'):
        r = res[k]
        words, rates = r['words'], r['bilist']
        ntr = len(rates)
        mean_rate = sum(rates) / ntr
        seen = sum(1 for i in range(ntr)
                   if pair_counts.get((words[i], words[i + 1]), 0) > 0)
        share = seen / ntr
        oov_touch = sum(1 for i in range(ntr)
                        if words[i] not in counts or words[i + 1] not in counts)
        c2[k] = {'mean_per_transition_bi_rate': mean_rate,
                 'seen_pair_share': share, 'n_transitions': ntr,
                 'n_seen': seen, 'n_oov_touching': oov_touch}
    gate_c2 = (c2['truth']['mean_per_transition_bi_rate'] >
               c2['salad']['mean_per_transition_bi_rate'] and
               c2['truth']['seen_pair_share'] > c2['salad']['seen_pair_share'])

    gates = {'a_margin_bar': gate_a, 'b_non_degenerate': gate_b,
             'c1_perturbation': gate_c1, 'c2_signal_integrity': gate_c2,
             'validity': vc, 'c1_table': c1, 'c2': c2}
    promising = gate_a and gate_b and gate_c1 and gate_c2
    verdict = 'PROMISING-v4' if promising else 'NULL-v4'

    print('=== PHASE 3: B_v4 + four gates ===')
    print(f'  rhat={rhat:.6f} nats/char; |truth|={mt} |salad|={ms} dm={dm}')
    print(f'  baseline removed: truth {-rhat*mt:+.1f} nats, '
          f'salad {-rhat*ms:+.1f} nats (net adjustment dm*rhat={dm*rhat:+.1f})')
    print(f'  B_v4(truth)={B4t:.1f}  B_v4(salad)={B4s:.1f}  M_v4={M_v4:.1f}')
    print(f'  per-char: B_v4(t)/{mt}={B4t/mt:.4f}  B_v4(s)/{ms}={B4s/ms:.4f}')
    print(f'  GATE (a) M_v4>=800: {M_v4:.1f} -> {gate_a}')
    print(f'  GATE (b) non-degenerate: {gate_b} '
          f'(meanlen={T["mean_wlen"]:.3f} in [{vc["len_band"][0]:.3f},{vc["len_band"][1]:.3f}], '
          f'invocab={T["invocab_frac"]:.4f})')
    for frac, vv in c1.items():
        print(f'  GATE (c1) rhat\'={frac}*rhat={vv["rhat_prime"]:.6f}: '
              f'M={vv["M_v4"]:.1f} >= 800 -> {vv["pass"]}')
    print(f'  GATE (c2) mean/trans bi rate truth={c2["truth"]["mean_per_transition_bi_rate"]:.4f} '
          f'> salad={c2["salad"]["mean_per_transition_bi_rate"]:.4f} '
          f'-> {c2["truth"]["mean_per_transition_bi_rate"] > c2["salad"]["mean_per_transition_bi_rate"]}; '
          f'seen-share truth={c2["truth"]["seen_pair_share"]:.4f} '
          f'> salad={c2["salad"]["seen_pair_share"]:.4f} '
          f'-> {c2["truth"]["seen_pair_share"] > c2["salad"]["seen_pair_share"]}')
    print(f'  OOV word-share: truth {T["n_oov"]}/{T["n_words"]}={T["oov_share"]:.4f}, '
          f'salad {S["n_oov"]}/{S["n_words"]}={S["oov_share"]:.4f}')
    print(f'  seg head truth: {"|".join(T["words"][:16])}')
    print(f'  seg head salad: {"|".join(S["words"][:16])}')
    print(f'VERDICT: {verdict}')

    out = {
        'model': {'v4_form': 'B_v4(D) = B_v3(D) - rhat*|D|',
                  'rhat': rhat, 'rhat_fit': fit_log,
                  'v3_inputs_byte_identical': True},
        'truth': {'B_v3': T['B'], 'B_v4': B4t, 'len': mt,
                  'W_uni': T['W_uni'], 'W_bi': T['W_bi'],
                  'W_len': T['W_len'], 'W_bnd': T['W_bnd'],
                  'n_words': T['n_words'], 'n_transitions': T['n_transitions'],
                  'mean_wlen': T['mean_wlen'], 'n_oov': T['n_oov'],
                  'invocab_frac': T['invocab_frac'],
                  'oov_share': T['oov_share'],
                  'per_char': {c: T[c] / mt for c in
                               ('W_uni', 'W_bi', 'W_len', 'W_bnd')},
                  'per_char_B_v3': T['B'] / mt, 'per_char_B_v4': B4t / mt},
        'salad': {'B_v3': S['B'], 'B_v4': B4s, 'len': ms,
                  'W_uni': S['W_uni'], 'W_bi': S['W_bi'],
                  'W_len': S['W_len'], 'W_bnd': S['W_bnd'],
                  'n_words': S['n_words'], 'n_transitions': S['n_transitions'],
                  'mean_wlen': S['mean_wlen'], 'n_oov': S['n_oov'],
                  'invocab_frac': S['invocab_frac'],
                  'oov_share': S['oov_share'],
                  'per_char': {c: S[c] / ms for c in
                               ('W_uni', 'W_bi', 'W_len', 'W_bnd')},
                  'per_char_B_v3': S['B'] / ms, 'per_char_B_v4': B4s / ms},
        'M_v3': M_v3, 'M_v4': M_v4,
        'M_v4_decomposition': {'M_v3': M_v3,
                               'length_baseline_adjustment_dm_times_rhat':
                                   dm * rhat,
                               'M_v4': M_v4,
                               'baseline_removed_truth': -rhat * mt,
                               'baseline_removed_salad': -rhat * ms},
        'gates': gates,
        'verdict': verdict,
    }
    with open(os.path.join(HERE, 'boundary_scores_v4.json'), 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print('wrote boundary_scores_v4.json, rhat_fit_v4.json')
    print('STOP: section 6 joint pilot NOT run (needs separate red-team clearance).')


if __name__ == '__main__':
    main()
