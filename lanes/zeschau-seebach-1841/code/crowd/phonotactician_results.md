# Phonotactician results — Zeschau→Seebach syllabary (R5005)

Date: 2026-10-07. Executor: THE PHONOTACTICIAN (crowd lane). Script: `code/crowd/phonotactician.py`.

## Verdict: NULL (with numbers)

A pure French-syllable-bigram objective, with 8 anchors pinned, is **gameable**:
the annealer beats random baselines by a wide margin but does so by collapsing
to a degenerate key — not by recovering the true syllabary. No crack claim.
Null results are first-class: the numbers below are the result.

## Method

1. **Group stream**: `load_pairs` from `code/crib_attack.py` (pairing not re-derived).
   Verified against `data/attempt1_results.json`: 1846 pairs, 96 distinct groups,
   28 odd-digit lines, 32 offset-1 lines. All match.
2. **Phonotactic model**: rule-based maximal-onset French orthographic syllabifier
   (`qu/ch/ph/gn` as unit onsets; plosive/fricative + `l/r` clusters kept together),
   run over 112,257 words of *Les Misérables* Tome I → 1,731 distinct syllables.
   Inventory = top-400 by token frequency (94.79% token coverage) + anchors
   (`'m'` was the only anchor missing from top-400; appended, K=401).
   Objective = Σ log P(syll_{i+1} | syll_i) over the 1845 decoded transitions,
   add-0.5 smoothing. **Era caveat**: Hugo 1862, not era-matched 1841 diplomatic
   French (the attempt-3 worker is building the era corpus; this lane used what
   was on disk).
3. **Search**: simulated annealing over the 88 free groups, 8 anchors pinned
   (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que, 87=ce), 12 restarts × 150k
   iterations, T 10.0→0.1 geometric. **No unicity constraint** (groups may share
   syllables) — this turned out to be the fatal design choice.

## Numbers

| measure | value |
|---|---|
| best anneal score (restart 8) | −9504.1 |
| restart score band (12) | −9504.1 … −10328.7 |
| uniform-random baseline (n=500, anchors pinned) | mean −12703.9, max −12302.7, sd 125.6 |
| Δ anneal vs uniform max | **+2798.6** |
| unigram-frequency-matched baseline (n=300) | mean −13525.2, max −13082.7, sd 187.9 |
| Δ anneal vs freq-matched max | **+3578.6 (19.0 sd)** |
| rank corr(group freq ↔ assigned-syllable unigram freq) | −0.106 (no frequency-matching) |
| distinct syllables in best key | **4** for 88 free groups (mat×34, hi×27, champ×21, ver×3) |
| decoded stream (best key) | `champmatmatchamphihihimatmat…` — repetitive syllable soup, not French |
| groups stable ≥0.75 across 12 restarts | **1/88** (95→`ve`, frac 0.917 — freq-2 group, likely noise) |
| groups stable ≥0.50 | 7/88 |
| anchor contexts, best key | everything after 82=`m` → `hi`; before 11=`la` → `ce`(87, pinned)/`mat`/`hi` — degenerate |

## Why the big Δ is not signal

- The 19σ beat over the frequency-matched baseline is real optimization, but of
  the wrong thing: with no unicity/dispersion penalty, the optimal policy is to
  reuse a tiny set of mutually high-bigram syllables (`mat→hi→mat→champ…`).
- Stability is absent: restarts land in different degenerate optima; no group
  earns a trustworthy assignment (the lone 0.917-stable group has freq 2).
- The decoded stream fails the eyeball test completely — a genuine key would
  decode to segmentable French, not `matmatmat`.
- The anchors did not save it: only 8/96 groups constrained, and the objective
  routes around them (e.g. 82=`m` followed everywhere by `hi`).

## Stable groups

Effectively none. Sole candidate 95→`ve` (11/12 restarts) is a freq-2 group and
is not trusted — treat as noise unless corroborated by another lane.

## What I'd try next

1. **Unicity/dispersion constraint**: cap syllable reuse (or anneal a permutation
   over a 96-syllable subset) so the optimizer cannot collapse; re-run — if the
   Δ over baselines survives, it is real phonotactic signal.
2. **Lexical grounding**: score decoded streams on segmentation into real French
   words (word-unigram/bigram model), not just syllable bigrams; or use
   phonotactics only as a tiebreaker on top of attempt-2/attempt-3 partial keys.
3. **Era-matched corpus**: re-fit the syllable model on the 1830s–40s corpus
   once the attempt-3 worker finishes it (per the 1841-register steer).
4. **Unigram prior**: add Σ log P(syllable) so rare-syllable assignments pay
   their true cost; combined with (1) this kills the collapse mode.

## Provenance

- Ciphertext: `data/upstream-ct_R5005.txt` + `data/upstream-offsets.json` (unchanged).
- Anchors: pencil cribs (7) + lane-inferred 87=`ce` (provisional, 4/5 checks).
- No ciphertext or keys invented; no files outside `code/crowd/` touched;
  `NOTES.md`/`STATE.md` untouched (curator's).
