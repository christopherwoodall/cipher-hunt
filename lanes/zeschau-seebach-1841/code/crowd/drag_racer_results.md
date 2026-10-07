# DRAG RACER — syllable-level function-word drag v2 (Seebach R5005)

**Verdict: PARTIAL — discriminates where letter-quadgrams tied, but the discrimination is word-prior, not placement. As a crib-placement tool at 8-anchor sparsity the drag remains effectively null; the real anchor-coincidence evidence comes from exact-count / model-free analyses.**

## Setup (verified)

- Group stream via `load_pairs` from `code/crib_attack.py`: **1846 pairs, 96 distinct groups** — matches `data/attempt1_results.json` phaseA exactly.
- Anchors (8): 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que, 87=ce (87=ce provisional, attempt-2 4/5).
- Anchor coverage: 236/1846 = **12.8%** of stream positions.
- Syllable model: Tocqueville t1+t2 (1835/1840 formal French prose), reused from the attempt-3 worker's cache (`data/PROVENANCE-tocqueville.txt`; not a duplicate build — own syllable model on the cached artifact). pyphen-fr syllabifier. Corpus: 215,246 tokens / 11,936 distinct words / 5,513 syllable units / 313,102 stream syllables. Add-α (α=0.1) smoothing → no floor ties.
- **v2 fix:** v1 used within-word syllable bigrams only, producing artifact z-scores (er-e z=+101) because the cipher stream runs *across* word boundaries. v2 builds both: within-word bigrams for candidate chain priors, **cross-word** (running-stream) bigrams for window scoring and expectation tests.
- Drag list: top-5000 Tocqueville words → 55 words with 2–4 syllable units and ≥1 anchor-coincident unit. All 55 have ≥1 min1 (≥1 anchor coincidence) position.

## Results

**D1 — adjacent anchored pairs (cross-word model):** 42 adjacencies, 18 distinct pairs. Mean bigram logprob −7.50 vs null (64 ordered anchor pairs) −8.65, **z=+4.18**. Top: er-e×9, ce-la×7, er-ce×3, ce-que×3, er-m×3.

**D1b — exact pair counts vs cross-word expectation** (only pairs with both units ≥300 model counts and E≥0.5 are interpretable; the rest are flagged uncalibrated in the JSON, z nulled):

| pair | groups | obs | E | z | reading |
|---|---|---|---|---|---|
| ce-la | 87-11 | 7 | 0.70 | **+7.59** | cela ×7 |
| ce-que | 87-46 | 3 | 1.75 | +0.97 | "ce que" consistent |
| que-la | 46-11 | 1 | 2.76 | −1.11 | consistent-ish |

Pairs involving er/m/i/e: **uncalibrated** — pyphen barely emits these units (counts per 313k stream syllables: er 52, m 125, e 24, i 17) while the cipher uses them as frequent cells (29=er is rank 3 at 47×). The model's unit inventory ≠ the cipher's cell inventory; no expectation computable. v1's z=+33..+101 for these pairs was pure model artifact, retracted.

**Drag ranking (best window per candidate, cross-word syllable-bigram score):** 54/55 distinct best values — **no floor degeneracy** (vs −7.714 tie for every candidate in attempts 1/2). Range −4.76 (`relative`) to −3.06 (`législation`). Baseline (anchors-only random windows): −6.96 ± 2.05 (n=634). Top margin ≈ **+1.9σ** — but see diagnosis: the margin is word-prior, not placement.

**Placement null:** best window == chain prior for 26/55 candidates (best window = the word sitting isolated, zero mapped neighbors). Top-25: 14 equal, 11 above; max lift +1.72 is `delaware` (ENGLISH word — Tocqueville's America vocabulary) at a fluke `pre` neighbor; next lifts ≤+0.51. **Min2 (≥2 anchor coincidences) placements exist for exactly one candidate: `cela` (7/7 exact 87-11).** Everything else is min1 "consistent-with".

**Model-free anchor-coincidence evidence:**
- **87 is the #1 predecessor of 11** across all groups: P(11|87)=7/32=0.219 vs next-best 0.167 (n=12). Supports 87-11 = "cela" without any model.
- 87→46 ("ce que") 3/32=0.094, ranks #3 predecessor of 46 — within noise, consistent.
- `cela` contexts (2 before | 87 11 | 3 after): `14 24|87 11|00 11`, `94 24|87 11|24 82`, `67 76|87 11|92 63`, `02 79|87 11|59 42`, `01 24|87 11|77 76`, `77 81|87 11|00 33`, `77 81|87 11|00 11`. **Group 24 precedes 87-11 in 3/7**; `77 81` precedes twice (both followed by 00).
- Cross-lane note (no duplication): 64 follows 87 at 5/32=0.156 — if attempt-3's 64="qui" holds, that is "ce qui"×5, a top French bigram. Consistent, not tested here.

## Diagnosis

1. **Why the letter drag was degenerate:** ±6-group window → ~13 groups → ~1.7 anchored → decoded string of ~2–8 letters; the quadgram model needs ≥4 letters and nearly every quadgram was unseen → every candidate scored the floor −7.714. Zero variance, zero discrimination. A scorer problem *and* a sparsity problem.
2. **Why the syllable drag discriminates but doesn't place:** add-α smoothing removes the floor (finite distinct values → 54/55 distinct scores), but at 12.8% anchor coverage the decoded window is still ~87% gaps. The score is therefore dominated by the candidate word's own chain prior; positional neighbor evidence contributes ≤+0.5 (one +1.7 fluke). Ranking candidates by "how French-typical is this word" ≠ placing them in the stream.
3. **Granularity mismatch (the deep problem):** the cipher's cells include single letters (m, i, e) and a hyper-frequent "er" (rank 3); pyphen's TeX-hyphenation units almost never emit these (and it under-splits finals: parceque→par-ceque, puisque/cette unsplit). The scorer's vocabulary and the cipher's cell inventory are different segmentations of French. Any bigram expectation involving er/m/i/e is uncalibrated — flagged, not quoted.
4. **Register contamination of the prior:** the chain prior ranks Tocqueville's vocabulary top — `législation`, `législateur`, `delaware`. An 1841 Dresden→St Petersburg diplomatic despatch needs diplomatic-French priors, not *De la démocratie en Amérique*.
5. **Sparsity math:** with 8 anchors, `cela` is the *only* candidate with ≥2 anchored syllables, hence the only exact placement. Every other candidate is min1. More anchors (not a better scorer) is what unlocks placement — the attempt-3 64="qui" test matters more than any rescoring.
6. **Correction to attempt-2:** its "P(cela|ce)=0.278" was `count("cela")/count("ce")` — a count ratio, not the conditional P(next syllable=la | ce). The correct cross-word conditional in Tocqueville is **P(la|ce)=0.022**, so the cipher (≈0.219) is ~10× cela-denser than the reference. Register note, not an anchor refutation; the 87=ce support now rests on the model-free #1-predecessor ranking instead.

## Next steps (for the coordinator)

1. Re-run this drag if/when 64="qui" (or any 9th anchor) confirms — min2 placements become possible for more words.
2. Invert the follower analysis: top followers of frequent unassigned groups (00→86 @0.222, 24→87 @0.192, 82=m→16 @0.289) are syllable-assignment proposals; score them against the cross-word model.
3. Replace pyphen with a cipher-calibrated unit inventory (letter-cells + coarse syllables per the pencil cribs' granularity) and/or a diplomatic-register corpus (1840s French diplomatic correspondence) to decontaminate the prior.
4. `cela`×7 contexts: chase group 24 (precedes 3/7) — candidate for a preceding word ("de" ? "à" ? — note "de cela" is ungrammatical; check "24"=ce? no, 87=ce… flag for the coordinator).

## Artifacts

- `code/crowd/drag_racer_results.json` — full numbers (D1, D1b with interpretability flags, baseline, top-25 drag, follow-ups).
- Method script (v2) appended below for audit. Only the two result files were written to the lane; the runner lived in /tmp.

## Appendix — drag_racer.py (v2, as run)

```python
#!/usr/bin/env python3
"""DRAG RACER v2 — syllable-level function-word drag, Seebach R5005.

v2 fixes a v1 modeling error: the cipher's group stream runs ACROSS word
boundaries, so the syllable bigram model must too. v1 used within-word
bigrams only, which made cross-boundary transitions (ce|la, er|e) look
impossibly rare (z=+7.7..+101 artifacts). v2 builds BOTH:
  - within-word bigrams: for candidate words' internal chain priors
  - cross-word bigrams (concatenated running syllable stream): for scoring
    decoded windows and for expected-count tests of adjacent anchor pairs.
Also flags: attempt-2's "P(cela|ce)=0.278" was count(cela)/count(ce), a
count ratio, not a conditional probability — not comparable to P(11|87).

Corpus: Tocqueville t1+t2 (1835/1840 formal French prose), reused from the
attempt-3 worker's cache (data/PROVENANCE-tocqueville.txt). Syllabifier:
pyphen fr. Caveats: (1) pyphen under-splits final syllables
(parceque->par-ceque, puisque/cette unsplit); (2) cipher cells include single
letters m/i/e which pyphen never emits as units -> those bigrams sit at the
smoothing floor, attenuating D1 (conservative).
"""
import json, math, re, os, sys, collections, statistics, random

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code'))
from crib_attack import load_pairs  # noqa

DATA = os.path.join(LANE, 'data')
OUTD = os.path.join(LANE, 'code', 'crowd')
os.makedirs(OUTD, exist_ok=True)

ANCHORS = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i',
           '29': 'er', '40': 'e', '46': 'que', '87': 'ce'}  # 87=ce provisional 4/5
SYL2GRP = {v: k for k, v in ANCHORS.items()}
ANCHOR_GROUPS = set(ANCHORS)
ALPHA = 0.1
W = 4  # window half-width (groups)


def build_models():
    import pyphen
    dph = pyphen.Pyphen(lang='fr')
    toks = []
    for fn in ['gutenberg-30513-tocqueville-t1.txt', 'gutenberg-30514-tocqueville-t2.txt']:
        txt = open(os.path.join(DATA, fn), encoding='utf-8', errors='replace').read()
        m1 = re.search(r'\*\*\* START OF.*?\*\*\*', txt)
        m2 = re.search(r'\*\*\* END OF.*?\*\*\*', txt)
        if m1: txt = txt[m1.end():]
        if m2: txt = txt[:m2.start()]
        toks += re.findall(r"[a-zàâäéèêëîïôöùûüÿçœæ]+", txt.lower())
    seg_cache = {}
    def segs(w):
        return seg_cache.setdefault(w, dph.inserted(w).split('-'))
    uni = collections.Counter()          # over running stream
    bi_in = collections.Counter()        # within-word bigrams
    bi_x = collections.Counter()         # cross-word (running stream) bigrams
    wfreq = collections.Counter()
    stream = []
    for w in toks:
        wfreq[w] += 1
        ss = segs(w)
        for a, b in zip(ss, ss[1:]): bi_in[(a, b)] += 1
        stream.extend(ss)
    for s in stream: uni[s] += 1
    for a, b in zip(stream, stream[1:]): bi_x[(a, b)] += 1
    V = len(uni); Z = len(stream)

    def mk(bi):
        den = {s: uni[s] + ALPHA * V for s in uni}
        def logp(b, a):
            return math.log((bi.get((a, b), 0) + ALPHA) / den.get(a, ALPHA * V))
        def p(b, a):
            return (bi.get((a, b), 0) + ALPHA) / den.get(a, ALPHA * V)
        return logp, p
    logp_in, p_in = mk(bi_in)
    logp_x, p_x = mk(bi_x)

    def logp_uni(s):
        return math.log((uni.get(s, 0) + ALPHA) / (Z + ALPHA * V))

    def chain_prior(ss):  # within-word: a candidate word's internal chain
        t = logp_uni(ss[0])
        for a, b in zip(ss, ss[1:]): t += logp_in(b, a)
        return t / len(ss)

    def run_score(run):  # cross-word: a decoded window across boundaries
        run = [s for s in run if s]
        if not run: return float('-inf')
        t = logp_uni(run[0])
        for a, b in zip(run, run[1:]): t += logp_x(b, a)
        return t / len(run)

    return dict(V=V, Z=Z, ntok=len(toks), nwords=len(wfreq), segs=segs,
                wfreq=wfreq, logp_in=logp_in, p_in=p_in, logp_x=logp_x,
                p_x=p_x, logp_uni=logp_uni, chain_prior=chain_prior,
                run_score=run_score, uni=uni)


def main():
    pairs, odd, off1 = load_pairs()
    assert len(pairs) == 1846 and len(set(pairs)) == 96
    freq = collections.Counter(pairs)
    M = build_models()
    segs, wfreq = M['segs'], M['wfreq']
    logp_x, p_x, chain_prior, run_score = M['logp_x'], M['p_x'], M['chain_prior'], M['run_score']
    print(f"[corpus] tokens={M['ntok']} words={M['nwords']} syll_vocab={M['V']} stream_sylls={M['Z']}")
    print("[anchor unit counts in model]",
          {s: M['uni'].get(s, 0) for s in ANCHORS.values()})

    # ---- candidate drag list
    cands = []
    for w, _ in wfreq.most_common(5000):
        ss = segs(w)
        if 2 <= len(ss) <= 4 and any(s in SYL2GRP for s in ss):
            cands.append((w, ss))
    print(f"[cands] {len(cands)}")

    # ---- D1: adjacent anchored pairs vs null (cross-word model)
    obs_pairs = collections.Counter(); n_adj = 0
    for i in range(len(pairs) - 1):
        if pairs[i] in ANCHOR_GROUPS and pairs[i + 1] in ANCHOR_GROUPS:
            obs_pairs[(ANCHORS[pairs[i]], ANCHORS[pairs[i + 1]])] += 1
            n_adj += 1
    obs_scores = [logp_x(b, a) for (a, b), c in obs_pairs.items() for _ in range(c)]
    null_scores = [logp_x(b, a) for a in ANCHORS.values() for b in ANCHORS.values()]
    mu_o = statistics.mean(obs_scores); mu_n = statistics.mean(null_scores)
    sd_n = statistics.pstdev(null_scores)
    z1 = (mu_o - mu_n) / (sd_n / math.sqrt(len(obs_scores)))
    D1 = {'n_adjacent_anchored': n_adj, 'distinct_pairs': len(obs_pairs),
          'top_pairs': [[a, b, c] for (a, b), c in obs_pairs.most_common(12)],
          'mean_logp_obs': round(mu_o, 4), 'mean_logp_null64': round(mu_n, 4),
          'z_vs_null': round(z1, 3),
          'note': 'cross-word model; m/i/e out-of-vocabulary in pyphen (floor), conservative'}

    # ---- D1b: exact adjacent-pair counts vs cross-word expectation
    D1b = []
    for (a, b), c in obs_pairs.most_common():
        ga, gb = SYL2GRP[a], SYL2GRP[b]
        na = freq[ga]
        p = p_x(b, a); E = na * p
        z = (c - E) / math.sqrt(na * p * (1 - p)) if 0 < p < 1 else float('nan')
        D1b.append({'pair': f'{a}-{b}', 'groups': f'{ga}-{gb}', 'obs': c,
                    'n_first': na, 'P_model': round(p, 4), 'E': round(E, 2),
                    'z': round(z, 2)})

    # ---- D2: candidate drag
    results = []
    for w, ss in cands:
        k = len(ss)
        anch_idx = [i for i, s in enumerate(ss) if s in SYL2GRP]
        pos1, pos2 = [], []
        for p in range(len(pairs) - k + 1):
            ok, conflict, nanch = True, False, 0
            for i, s in enumerate(ss):
                g = pairs[p + i]
                if s in SYL2GRP:
                    if g != SYL2GRP[s]: ok = False; break
                    nanch += 1
                elif g in ANCHOR_GROUPS: conflict = True; break
            if not ok or conflict: continue
            pos1.append(p)
            if nanch >= 2: pos2.append(p)
        exact = 0
        if len(anch_idx) == k:
            pat = [SYL2GRP[s] for s in ss]
            exact = sum(1 for p in range(len(pairs) - k + 1) if pairs[p:p + k] == pat)
        best, tot, cnt, bestp = float('-inf'), 0.0, 0, None
        for p in pos1:
            table = dict(ANCHORS)
            for i, s in enumerate(ss):
                if s not in SYL2GRP: table[pairs[p + i]] = s
            win = pairs[max(0, p - W):p + k + W]
            dec = [table.get(g) for g in win]
            off = p - max(0, p - W)
            l, r = off, off + k - 1
            while l - 1 >= 0 and dec[l - 1]: l -= 1
            while r + 1 < len(dec) and dec[r + 1]: r += 1
            sc = run_score(dec[l:r + 1])
            tot += sc; cnt += 1
            if sc > best: best, bestp = sc, p
        results.append({'word': w, 'syllables': ss, 'k': k,
                        'chain_prior': round(chain_prior(ss), 4),
                        'n_pos_min1': len(pos1), 'n_pos_min2': len(pos2),
                        'n_exact': exact,
                        'mean_win': round(tot / cnt, 4) if cnt else None,
                        'best_win': round(best, 4) if cnt else None,
                        'best_p': bestp})
    results.sort(key=lambda r: (r['best_win'] if r['best_win'] is not None else -99,
                                r['chain_prior']), reverse=True)

    # ---- baseline: anchors-only random windows (cross-word scorer)
    rng = random.Random(1841)
    base = []
    for _ in range(2000):
        p = rng.randrange(len(pairs))
        win = pairs[max(0, p - W):p + W + 1]
        dec = [ANCHORS.get(g) for g in win]
        off = p - max(0, p - W)
        l = r = off
        while l - 1 >= 0 and dec[l - 1]: l -= 1
        while r + 1 < len(dec) and dec[r + 1]: r += 1
        sc = run_score(dec[l:r + 1])
        if sc != float('-inf'): base.append(sc)
    mu_b = statistics.mean(base); sd_b = statistics.pstdev(base)

    bw = [r['best_win'] for r in results if r['best_win'] is not None]
    n_eq_prior = sum(1 for r in results
                     if r['best_win'] is not None and abs(r['best_win'] - r['chain_prior']) < 1e-9)
    out = {
        'meta': {'pairs': 1846, 'distinct_groups': 96, 'anchors': ANCHORS,
                 'anchor_coverage': round(sum(freq[g] for g in ANCHORS) / 1846, 4),
                 'corpus': 'Tocqueville t1+t2 (1835/1840), pyphen-fr; WITHIN-word chain priors, CROSS-word window/bigram model (v2 fix)',
                 'syll_vocab': M['V'], 'corpus_tokens': M['ntok'],
                 'note': '87=ce provisional (attempt2 4/5). pyphen under-splits finals; m/i/e OOV (floor).'},
        'D1_adjacent_anchor_pairs': D1,
        'D1b_pair_counts_vs_model': D1b,
        'baseline': {'n': len(base), 'mean': round(mu_b, 4), 'sd': round(sd_b, 4)},
        'drag_top25': results[:25],
        'n_candidates': len(cands),
        'n_with_positions': sum(1 for r in results if r['n_pos_min1']),
        'n_best_eq_chain_prior': n_eq_prior,
        'degeneracy': {'distinct_best_win': len(set(round(x, 6) for x in bw)),
                       'n_scored': len(bw)},
    }
    with open(os.path.join(OUTD, 'drag_racer_results.json'), 'w') as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print('[D1]', json.dumps(D1)[:400])
    print('[D1b top]')
    for r in D1b[:8]: print('  ', r)
    print('[baseline] mean=%.4f sd=%.4f n=%d' % (mu_b, sd_b, len(base)))
    print('[top12]')
    for r in results[:12]:
        print('  %-12s %s prior=%.3f pos1=%d pos2=%d exact=%d mean=%.3f best=%.3f'
              % (r['word'], '/'.join(r['syllables']), r['chain_prior'],
                 r['n_pos_min1'], r['n_pos_min2'], r['n_exact'],
                 r['mean_win'] or -99, r['best_win'] or -99))
    print('[best==chain_prior]:', n_eq_prior, '/', len(results))
    print('[done]')


if __name__ == '__main__':
    main()
```
