# TRACK-C PREREG v2 — length-scaled OOV repair of B(D)

**Track:** C (boundary-informed scoring), round-2 fleet. **Date:** 2026-10-07.
**Status:** PRE-REGISTERED v2 — written BEFORE the v2 static margin runs.
**Re-registration context:** v1 (`PREREG.md`, frozen, DO NOT MODIFY) executed
under red-team R3 GO; the static margin was numerically PROMISING
(M = +2,648.4) but substantively degenerate (RESULTS.md §§2–5): the OOV
log-rate ln(α/Z) = −13.12 per word-form, independent of length, let the DP
minimize word count (≈20-char OOV chunks on both decodes; B(D) ≈ −1.34·|D|,
a length penalty in disguise — the R3b mechanism confirmed). The §6 joint
pilot was stood down deliberately (RESULTS.md §5). Per operator standing
order ("a null is not a stop — diagnose, repair, re-register, continue"),
this v2 re-registers a length-scaled OOV model and adds a binding validity
precondition so a degenerate PROMISING cannot recur.

**v1 sections carried forward unchanged:** §0 question, §2.1 input handling
(decode strings used as-is, no re-projection), §2.2 corpus + tokenizer +
fitted constants (N=486,789, C=1,717,960, V=10,666, α=1.0, β=1.0,
MAXWLEN=20, ρ=0.283353, Z=497,455, ln ρ=−1.2612, L(k) add-β), §2.3 DP
recurrence verbatim (window 20, i-ascending tie-break, B=dp[m]), W_len and
W_bnd definitions, §3 anti-gaming provisions (no truth-peeking, no Les-Mis
weights anywhere, frozen decodes with sha256 re-verification, no R5005
contact), §4 hygiene gate (already PASSED under v1: 0 shared 15-grams;
same corpus/weights, no re-run needed), §5 determinism, §6 joint-pilot
spec (slice, objectives, protocol, bar) — with the v2 OOV model substituted
into B(D) and the §2 validity precondition added below.

## 1. The repair (exact)

v1 word log-rate: `logP(w) = ln((c(w)+α)/Z)` if w ∈ V, else `ln(α/Z)`
(length-independent — the degenerate term).

v2 word log-rate: `logP(w) = ln((c(w)+α)/Z)` if w ∈ V, else
**`logP_oov(w) = |w| · ln(p_char)`** — the OOV rate scales with word length.

### 1.1 p_char (pinned exactly, pre-registered)

The v1 OOV fallback for a 1-char word paid ln(1/Z) = −13.1169. v2 anchors
the per-char OOV rate to the unigram rate of a **rare in-vocab single-char
word**:

- 28 single-char types exist in V (word_vocab.json); rarest is a tie:
  `'q'` and `'z'`, each count **4** (MIN_COUNT=2 gate applies).
- With the same add-α smoothing as the whole model (α=1.0, Z=N+αV=497,455):
  **p_char = (4 + 1)/497,455 = 5/497,455 = 1.0051160406468926e-05**;
  **ln(p_char) = −11.507822466794325** nats/char.
- In the v2 scorer, `P_CHAR = 5.0/497455.0` is a hard-coded constant
  (recomputed NOT from the vocab at scoring time).

**Calibration justification (binding):** the DP's OOV fallback for a single
char now pays exactly what the rarest observed single-char French word pays
under identical smoothing. This is the *cheapest defensible* per-char rate:
any anchor rarer than the rarest observed type would be ungrounded; any
more-punitive anchor (e.g. mean 1-char rate) would tilt the DP harder
against OOV and inflate truth–salad separation. The bias is toward the null
(conservative against PROMISING-v2). No decode string was consulted in
setting this value.

**Scale check (not a prediction):** 1-char OOV word now costs
−11.5078 (uni) − 1.7079 (ln L(1)) − 1.2611 (ln ρ) = −14.4768 nats/word;
20-char OOV costs −230.1564 − 12.4025 − 1.2611 = −243.82 — OOV-20
swallowing is banned by construction. Real in-vocab words are unchanged
(≈ −6 to −12 nats/word; reference mean ≈ −11.4/word ≈ −3.2/char).

## 2. v2 verdict rule (binding) — replaces v1 §1, adds VALIDITY PRECONDITION

Margin: **M = B_v2(truth) − B_v2(salad)** (nats; higher = more French-like),
same frozen decodes and sha256 as v1 §1.

- **PROMISING-v2** iff M ≥ +800 nats **AND** the VALIDITY PRECONDITION holds.
- **NULL-v2** iff M < +800, **OR** the validity precondition fails
  (a degenerate ≥+800 is explicitly NOT PROMISING — it reports as NULL-v2
  with the degeneracy diagnosed, no pilot).

**VALIDITY PRECONDITION (binding, non-degenerate argmax):** computed on the
DP argmax tilings of the static margin (the same tilings the margin is
derived from):

1. truth argmax mean word length ∈ [3.529/2, 3.529×2] = **[1.765, 7.059]**
   (reference mean projected word length 3.529; RESULTS.md §3 records v1
   truth mean 19.90 — the degenerate signature this excludes); **AND**
2. **majority (≥50%) of truth argmax words in-vocab** (v1 truth: 1/159 —
   the degenerate signature this excludes).

The truth decode is the known-French reference; its argmax is the binding
check. The salad argmax's mean length and in-vocab fraction are reported as
diagnostics alongside.

## 3. Execution order (binding)

1. This file (PREREG-C-v2.md) — the v2 spec is frozen here.
2. `score_boundaries_v2.py` — v2 scorer (v1 recurrence + length-scaled
   OOV; decode sha256 re-verified; full W_uni/W_len/W_bnd breakdown per
   R3b reporting requirement; no RNG).
3. Run the static margin ONCE; report M, components, and the validity
   check (mean lengths, in-vocab fractions, sample tilings).
4. **STOP. The §6 joint pilot does NOT run here** — a red-team reviewer
   clears it separately. If v2 is NULL-v2 (fails bar or precondition),
   the report diagnoses precisely which term still degenerates (numbers)
   and proposes the next repair; a second honest null is a valid return.

No bar movement after seeing M (§1 of v1 still applies: no re-registration
of the bar). The pilot, if ever cleared, uses B_v2 with the v1 §6 spec
otherwise unchanged.

## 4. Next-repair candidates (pre-registered, not executed)

If v2 is NULL-v2, the standing-order candidates are: (a) word-bigram
transition terms (boundary-adjacent word collocations); (b) boundary-
placement features (e.g. per-position word-start priors from the reference
corpus). The diagnosis will name which component still degenerates with
numbers before any further re-registration.
