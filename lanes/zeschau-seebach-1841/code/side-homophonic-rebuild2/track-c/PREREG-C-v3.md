# TRACK-C PREREG v3 — word-bigram boundary score B_v3(D)

**Track:** C (boundary-informed scoring), round-2 fleet. **Date:** 2026-10-07.
**Status:** PRE-REGISTERED v3 — written BEFORE any v3 scoring code or run.
**Re-registration context:** v1 (`PREREG.md`, frozen, DO NOT MODIFY) was
numeric-PROMISING but degenerate (OOV length-independent rate). v2
(`PREREG-C-v2.md`, frozen, DO NOT MODIFY) repaired the degeneracy
(length-scaled OOV) and was again numeric-PROMISING (M = +1,916.4 ≥ +800,
validity precondition passed) but substantively NULL: the margin decomposed
to +5,057.1 (length) − 3,140.8 (content); per-char EVERY component favored
the salad (RESULTS-C-v2.md §4). Root cause, sharper than v1: the salad's
tiles are themselves common French word-forms BY ADVERSARIAL CONSTRUCTION
(100% in-vocab on both v2 argmaxes; salad W_uni/word −6.87 vs truth −5.50).
A word-UNIGRAM model cannot see adversarial boundary placement — the signal
lives in word ORDER, which unigrams discard. §0 ("does boundary structure
separate truth from salad?") answered NO under B_v2.

v3 adds word-bigram transition terms. Motivation (diagnostic, not a
prediction — RESULTS-C-v2.md §7): on the v2 argmax tilings, truth has 65.2%
of adjacent word pairs seen in the diplomatic corpus vs 37.5% for salad;
mean log bigram rate −8.158/pair (truth) vs −9.094/pair (salad) →
Δ ≈ 0.94 nats/pair × ~1,300 pairs ≈ +1,200 nats truth-favoring, with pair
counts nearly equal (1,340 vs 1,279) — i.e. a bigram margin would be
CONTENT-driven, the opposite of the unigram margin's pathology.

**v2 sections carried forward unchanged:** §0 question; input handling
(decode strings as-is, no re-projection); corpus + tokenizer + fitted
constants (N=486,789, C=1,717,960, V=10,666, α=1.0, β=1.0, MAXWLEN=20,
ρ=0.283353, Z=497,455, ln ρ=−1.2612, L(k) add-β length model,
p_char=5/497,455, ln(p_char)=−11.507822466794325); the v2 length-scaled
unigram word rate `logP_uni(w) = ln((c(w)+α)/Z)` if w ∈ V else
`|w|·ln(p_char)`; anti-gaming provisions (no truth-peeking, no Les-Mis
weights, frozen decodes with sha256 re-verification, no R5005 contact);
§4 hygiene gate (already PASSED under v1: 0 shared 15-grams; same corpus,
no re-run); determinism (no RNG); §6 joint-pilot spec (slice, objectives,
seeds, protocol) with the §6 bar unchanged below.

## 1. B_v3(D) — exact definition

Let D be a decode string of length m chars. Words are substrings
w = D[j:i], 0 ≤ j < i ≤ m, i−j ≤ MAXWLEN (=20).

**1.1 Per-word score (v2 pieces, unchanged).**
`s(w) = logP_uni(w) + ln L(|w|) + ln ρ`, where logP_uni is the v2
length-scaled unigram rate and L, ρ are the v2 length/boundary priors.

**1.2 Bigram transition rate (NEW).** Fit from the SAME diplomatic corpus,
same tokenizer as v2. Tokenize the corpus; count consecutive token pairs
c(u,v) (both tokens in V, MIN_COUNT=2 vocab) and context counts
c(u) = Σ_v c(u,v). Add-1 smoothing over the vocabulary:

`logP_bi(u,v) = ln( (c(u,v) + 1) / (c(u) + V) )`, V = 10,666.

**OOV-bigram fallback (pinned):** the rule above applies mechanically to
all pairs. OOV words have zero corpus counts by construction, so:
c(u)=0 for u ∉ V → uniform follower rate ln(1/V) = ln(1/10666) ≈ −9.2746
for any v; c(u,v)=0 whenever either word is OOV. Justification: this is the
literal add-1 bigram over the fitted corpus — no decode consulted, no extra
parameter introduced. OOV words already pay the v2 length-scaled unigram
OOV rate; an additional OOV transition penalty would double-count the OOV
event. Recorded quirk for red-team scrutiny: OOV-context transitions
(−9.2746) are CHEAPER than garbled transitions from common in-vocab
contexts (e.g. u='de': ≈ −ln(c(de)+V) ≈ −10.5). Moot in practice under the
v2 validity precondition (v2 argmaxes were 100% in-vocab on BOTH decodes),
but it is on the record.

**1.3 λ_bi = 1.0 (pinned, hard-coded constant).** Justification:
(1) the transition term is in the same nat units as the unigram term —
1.0 is the parameter-free default; (2) any tuned λ would be fit on the
truth/salad decodes = hypothesis contamination (v1 §3 anti-gaming);
(3) the motivating v2 §7 diagnostic (+1,200 nats, 65.2% vs 37.5% seen-pair
rates) was computed at effective λ=1, so the motivation corresponds to
this value. λ_bi is NOT tuned after seeing any v3 number.

**1.4 First word (pinned): unigram-only.** The first word of the tiling
receives NO bigram term (T = 0). Justification: a start-symbol rate would
require a fitted sentence-initial distribution the corpus spec does not
provide; the first word is one transition in ~1,300, immaterial either way;
unigram-only adds no unregistered parameters.

**1.5 DP recurrence (deterministic).**
State dp[i][w] = best score of a tiling of prefix D[0:i] ending with word
w = D[j:i], for i ∈ [1,m], j ∈ [max(0,i−MAXWLEN), i−1].

- If j = 0 (first word): `dp[i][w] = s(w)`.
- Else: `dp[i][w] = s(w) + max_{u ∈ states(j)} [ dp[j][u] + λ_bi·logP_bi(u,w) ]`,
  where states(j) = { D[k:j] : k ∈ [max(0,j−MAXWLEN), j−1] }.
- **Tie-break (pinned):** iterate j ascending, and for fixed j iterate u in
  ascending lexicographic order of the word string; keep the FIRST
  candidate that is strictly greater (exact float `>` comparison, no
  tolerance). Backpointers follow the same order for argmax recovery.
- `B_v3(D) = max_w dp[m][w]`; argmax tiling recovered via backpointers.

Complexity: ≤ 20·20 transitions per position × m ≤ 5,143 → ≈ 2M
transition evaluations; bigram log-rates precomputed in a dict keyed by
seen (u,v) pairs, fallback computed on the fly. No RNG anywhere.

**1.6 Component reporting (R3b lens, mandatory).** The v3 report decomposes
the static margin into per-component sums AND per-char rates for BOTH
decodes: W_uni (Σ s-uni pieces), W_bi (Σ λ_bi·logP_bi transition pieces),
W_len (Σ ln L(|w|)), W_bnd (Σ ln ρ), each reported as total and per-char
(·/|D|). The length-vs-content decomposition of M (v2 §4 method, salad
per-char rates as reference, truth rates as robustness check) is also
reported. Gate (c) below is evaluated on the totals' per-char rates.

## 2. v3 verdict rule (binding) — THREE gates

Margin: **M = B_v3(truth) − B_v3(salad)** (nats; higher = more French-like),
same frozen decodes and sha256 as v1/v2. The +800 bar is kept identical to
v1/v2 for cross-version comparability — it does not move after seeing M.

- **Gate (a) — margin bar:** M ≥ +800 nats.
- **Gate (b) — validity precondition (carried over from v2):** on the DP
  argmax tilings of the static margin: (1) truth argmax mean word length
  ∈ [1.765, 7.059] (2× band around reference 3.529); **AND** (2) ≥50% of
  truth argmax words in-vocab. Salad argmax reported as diagnostic.
- **Gate (c) — content-drivenness gate (NEW, binding):**
  **B_v3(truth)/|truth| > B_v3(salad)/|salad|** (strict inequality).
  The margin may not be length-dominated.

**Verdict:** PROMISING-v3 iff (a) AND (b) AND (c) all hold. **NULL-v3**
otherwise. **Explicitly: if (a) passes but (c) fails, the verdict is
NULL-v3 regardless of M** — a length-dominated margin is not PROMISING,
it is the v2 pathology recurring, and it reports as NULL-v3 with the
failing component diagnosed by the R3b decomposition. No third option;
no re-registration of any bar after seeing the numbers.

## 3. Execution order (binding)

1. This file (PREREG-C-v3.md) — the v3 spec is frozen here.
2. `score_boundaries_v3.py` — v3 scorer implementing §1 exactly (bigram
   table built from the corpus at build time, no decode input; decode
   sha256 re-verified; full W_uni/W_bi/W_len/W_bnd breakdown + per-char
   rates per §1.6; no RNG).
3. Run the static margin ONCE; report M, the three gates, components,
   the R3b per-char decomposition, and sample argmax tilings.
4. **STOP. The §6 joint pilot does NOT run here** — a red-team reviewer
   clears it separately AFTER the static result. If v3 is NULL-v3, the
   report diagnoses precisely which term/gate failed (numbers) and
   proposes the next repair; a third honest null is a valid return.

## 4. §6 joint pilot (spec unchanged; gated)

Pilot slice, objectives, seeds, and protocol are exactly v1 §6 (carried
through v2). The pilot bar is unchanged: **pilot PASS iff joint ≥ 0.15
AND blind ≤ 0.05**; blind > 0.05 → uninformative, no claim; joint < 0.15 →
NEGATIVE. The pilot itself stays gated on red-team clearance AFTER the
v3 static result is reviewed.

## 5. Pre-registered residual risks (not gate adjustments)

- The +1,200 nat diagnostic (v2 §7) was computed on the **v2** argmax
  tilings. Under B_v3 the salad's argmax re-optimizes and may discover
  tilings rich in common-word bigrams (le|de, de|la adjacencies) that
  recover bigram mass the v2 tiling left on the table. The diagnostic is
  motivation, not a prediction; gate (c) is the honest arbiter either way.
- Bigram dynamic range: for common contexts c(u) is large, so the
  unseen-pair rate −ln(c(u)+V) can sit close to mediocre seen rates —
  the seen/unseen separation may be narrower than the v2 diagnostic's
  mean-rate comparison suggests.
- λ_bi=1.0 is untuned by design. If the unigram mass still dominates M,
  the margin may stay length-driven — which gate (c) converts to NULL-v3,
  the honest outcome, not a tuning invitation.
