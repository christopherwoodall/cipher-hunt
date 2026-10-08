# TRACK-C PREREG v4 — length-neutralized boundary score B_v4(D)

**Track:** C (boundary-informed scoring), round-2 fleet. **Date:** 2026-10-07.
**Status:** PRE-REGISTERED v4 — written BEFORE any v4 scoring code or run.
**Re-registration context:** v1 (`PREREG.md`, frozen, DO NOT MODIFY) was
numeric-PROMISING but degenerate (OOV length-independent rate). v2
(`PREREG-C-v2.md`, frozen, DO NOT MODIFY) repaired the degeneracy
(length-scaled OOV) and was again numeric-PROMISING (M = +1,916.4 ≥ +800)
but substantively NULL: M decomposed to +5,057.1 (length) − 3,140.8
(content); per-char every component favored the salad — a word-unigram
model cannot see adversarial boundary placement. v3 (`PREREG-C-v3.md`,
frozen, DO NOT MODIFY) added word-bigram transition terms: M = +2,683.9
≥ +800 (gate (a) PASS), non-degenerate argmax (gate (b) PASS), but gate
(c) FAILED — per-char, every component including W_bi favored the salad
(−6.7407 vs −4.6687); M = +9,239.4 (length) − 6,555.6 (content)
(RESULTS-C-v3.md §§3–4). The v3 diagnosis, confirmed by the R3b lens: the
per-transition bigram content signal IS real (mean log bigram rate
−7.657/pair truth vs −8.545/pair salad; seen-pair share 0.634 vs 0.359),
but the raw-total objective's LENGTH CHANNEL dominates — the salad is
62% longer (5,143 vs 3,164 chars) with nearly the same word count
(1,260 vs 1,297), so per-char conversion dilutes every per-word and
per-transition penalty. Adding more content terms will not help; the
length channel must be neutralized directly. This is the last
statistical repair in the line (see §8).

**v3 sections carried forward unchanged:** the §0 question (sharpened
below); input handling (decode strings as-is, no re-projection); corpus
+ tokenizer + all fitted constants (N=486,789, C=1,717,960, V=10,666,
α=1.0, β=1.0, MAXWLEN=20, ρ=0.283353, ln ρ=−1.2612, L(k) add-β length
model, p_char, ln(p_char)=−11.507822466794325, Z=497,455); the v2
length-scaled unigram word rate; the v3 add-1 bigram table
(OOV-context fallback ln(1/V)≈−9.2746, mechanical); λ_bi=1.0 (pinned,
NOT tuned after seeing any number); first-word unigram-only;
the v3 DP recurrence + deterministic tie-break (j ascending,
u lexicographic ascending, first strictly-greater on exact float `>`,
backpointers same order); anti-gaming provisions (no truth-peeking,
no Les-Mis weights — R3 DP bias probe standing, frozen decodes with
sha256 re-verification: truth `165fa8af…` / salad `8fb3ba26…`,
no R5005 contact — standing grep-clean requirement); §4 hygiene gate
(already PASSED under v1, carried forward, no re-run); determinism
(no RNG); §6 joint-pilot spec (slice, objectives, seeds 7001–7004,
protocol) with the §6 bar unchanged below.

## §0 Question (sharpened)

v1–v3 asked "does boundary structure separate truth from salad?" v4
asks the length-neutralized form: **does boundary structure separate
truth from salad once the expected score mass of length itself is
removed?** The comparison is content-deviation-from-French-expectation,
not raw total and not per-char rate.

## §1 Form selection — (ii) chosen, (i) rejected (with proof)

Two candidate repairs were evaluated. **Form (ii) is selected.** Form
(i) is rejected, and the rejection is load-bearing — it is proven,
not asserted, that (i) is not a repair at all.

**Form (i) — length-normalized DP objective, REJECTED.** For a fixed
decode D, |D| = m is a constant. In IEEE-754 arithmetic, division by a
positive constant is strictly order-preserving: for all finite floats
a, b and c > 0, a > b ⟺ a/c > b/c and a = b ⟺ a/c = b/c. The v3 DP's
argmax is determined entirely by strict-`>` comparisons under the
pinned tie-break (exact-equality cases keep the first candidate, and
equality is likewise preserved under positive scaling). Therefore

  argmax_tiling B_v3(D)/|D| = argmax_tiling B_v3(D)   **exactly**,

and a DP "re-run under the normalized objective" recovers byte-identical
tilings — the v4 spec asserts this as a check (§4 step 2), it is not a
new optimization. The only change form (i) makes is comparing in
per-char units: B_v3(truth)/3164 vs B_v3(salad)/5143 — which is
**precisely v3's gate (c)**, already evaluated on the frozen artifacts
as −6.7407 vs −4.6687 → FAIL (RESULTS-C-v3.md §3). Re-registering it as
"v4" would re-run a settled verdict under a new name; under the R3/R9
falsifiability standard (no re-registration of bars or verdicts after
seeing numbers, no evasion paths) that is not a repair. Worse, (i) is
the worst possible frame for the confirmed content signal: the truth's
**+834.4-nat absolute W_bi edge** (RESULTS-C-v3.md §2) becomes the
−3.1364 vs −2.0918 per-char deficit, because the salad spreads a
comparable transition count (1,259 vs 1,296) over 62% more characters.
Form (i) IS the dilution channel — it cannot cure it.

**Form (ii) — fitted length baseline, SELECTED.** B_v4(D) = B_v3(D) −
f(|D|), f fitted on reference text only. Numerical justification:

1. The length channel is removed as an absolute credit, not a divisor.
   M_v4 = M_v3 + (m_salad − m_truth)·r̂ keeps every absolute content
   term at full weight — the +834.4-nat W_bi margin, the unigram/bigram
   content terms — instead of dividing the salad side's penalties by
   5,143. The confirmed per-transition signal (mean −7.657 vs −8.545
   nats/pair; seen-pair share 0.634 vs 0.359 — RESULTS-C-v3.md §4.4)
   enters the verdict at its true absolute magnitude.
2. The removed term is exactly the §4.2 decomposition's length
   component (+9,239.4 nats, salad-reference): f(|D|) = r̂·|D| with r̂
   the expected per-char B_v3 rate of genuine reference French
   subtracts the length-attributable mass from both decodes, leaving
   content deviations. Nothing in the content terms is redefined,
   retuned, or rescaled — λ_bi stays 1.0, all tables frozen.
3. r̂ is a fitted constant from reference text (same class as ρ: fitted,
   decode-blind, zero degrees of freedom at verdict time) — not a
   tuned parameter. Any tuned alternative would be fit on truth/salad =
   hypothesis contamination (v1 §3 anti-gaming).

## §2 B_v4(D) — exact definition

**2.1 Reference rate r̂ (fit procedure, pinned; REFERENCE TEXT ONLY —
no decode byte is read before r̂ is computed and logged).**

Let F range over the 5 diplomatic corpus files (sha256 per
word_stats.json — the same files v1/v2/v3 fit on). For each file,
take the v2/v3 tokenizer's token sequence
(t_{F,1}, …, t_{F,K_F}) (WORD_RE → phonetics.project() defaults
(word, silent_finals=True); empty projections skipped). Define,
with ALL v2/v3 constants and fallbacks verbatim
(logP_uni length-scaled: in-V ln((c(w)+α)/Z), α=1.0, Z=497,455;
OOV |w|·ln(p_char), ln(p_char)=−11.507822466794325; ln L(|w|) add-β,
β=1.0; ln ρ=−1.2612; logP_bi add-1 over V=10,666 with mechanical
OOV-context fallback ln(1/V)≈−9.2746; λ_bi=1.0; first token of each
file unigram-only — mirroring v3 §1.4; bigram pairs within files
only, no cross-file junctions — mirroring v3's pinned choice):

  S_R = Σ_F [ Σ_{k=1..K_F} (logP_uni(t_{F,k}) + ln L(|t_{F,k}|) + ln ρ)
            + Σ_{k=2..K_F} λ_bi · logP_bi(t_{F,k−1}, t_{F,k}) ]

  m_R = Σ_F Σ_{k=1..K_F} |t_{F,k}|      (chars; spaceless token lengths)

  **r̂ = S_R / m_R**   (nats/char; asserted −25 < r̂ < 0, else the run
  is VOID — reported to red team, no verdict; rates are negative
  log-probs, so r̂ ≥ 0 is impossible and r̂ ≤ −25/char is absurd).

Why the natural tokenization, not the DP optimum: the DP optimum
measures best-adversarial-tiling quality — the salad's own game. The
natural tiling measures genuine French text under the model, which is
the correct "expected French" estimand for a length baseline. It is
also conservative by construction: the natural tiling is feasible for
the DP, so r̂_DP-opt ≥ r̂_natural; using the more-negative value biases
M_v4 downward (M_v4 = M_v3 + 1979·r̂, r̂<0), i.e. AGAINST PROMISING —
the safe direction for a fitted baseline. The ±20% perturbation gate
(§3(c1)) covers the remaining fit uncertainty symmetrically.

**2.2 The v4 score.**

  f(m) = r̂ · m

  **B_v4(D) = B_v3(D) − f(|D|)**

where B_v3(D) is the v3 DP optimum on decode D, re-run under the
verbatim v3 DP (§4 step 2 asserts byte-identical argmax tilings to
boundary_scores_v3.json — f(|D|) is constant per decode, so the
argmax is provably unchanged; the re-run is a drift check, not a new
optimization).

**2.3 Margin.** **M_v4 = B_v4(truth) − B_v4(salad)** (nats; higher =
more French-like), same frozen decodes and sha256 as v1–v3.

## §3 v4 verdict rule (binding) — FOUR gates

- **Gate (a) — margin bar:** M_v4 ≥ +800 nats, evaluated at the fitted
  r̂. The +800 bar is kept identical to v1/v2/v3 for cross-version
  comparability — it does not move after seeing M_v4. A total-margin
  bar (not a per-char δ) is chosen deliberately: M_v4 is already
  length-neutralized, so the bar no longer smuggles the length channel
  — the pathology that forced v3's gate (c) is structurally removed,
  and a per-char δ would reintroduce the (i)-flavored dilution frame
  rejected in §1.
- **Gate (b) — validity precondition (carried over from v2/v3
  unchanged):** on the DP argmax tilings: (1) truth argmax mean word
  length ∈ [1.765, 7.059] (2× band around reference 3.529); **AND**
  (2) ≥50% of truth argmax words in-vocab. Salad argmax reported as
  diagnostic.
- **Gate (c1) — fit-perturbation robustness (NEW, binding):** M_v4 ≥
  +800 under r̂′ = 0.8·r̂ AND under r̂′ = 1.2·r̂
  (M_v4(r̂′) = M_v3 + (m_salad − m_truth)·r̂′, m_salad − m_truth = 1979
  per the frozen decode lengths). Since r̂ < 0, the binding end is
  1.2·r̂. The winning margin must survive ±20% perturbation of the
  length-baseline fit — the normalization must not be a knife-edge.
- **Gate (c2) — content-signal integrity (NEW, binding):** on the v4
  argmax tilings, the confirmed per-transition bigram signal must
  still favor truth: mean per-transition log bigram rate truth >
  salad (strict; less negative wins) AND seen-pair share truth > salad
  (strict). The repair may not achieve its margin by destroying the
  signal that motivated it.

**Verdict:** PROMISING-v4 iff (a) AND (b) AND (c1) AND (c2) all hold.
**NULL-v4** otherwise. **Explicitly: if (a) passes but (c1) or (c2)
fails, the verdict is NULL-v4 regardless of M_v4** — a margin that
depends on a fragile length fit, or one bought by inverting the
confirmed content signal, is not PROMISING. No third option; no
re-registration of any bar after seeing the numbers. (On the
carried-forward tilings (c2) is expected to hold — RESULTS-C-v3.md
§4.4: −7.657 vs −8.545; 0.634 vs 0.359 — it is pinned as a guard so
the claim "the repair leaves the confirmed signal intact" is
checkable, not assumed.)

## §4 Execution order (binding)

1. This file (PREREG-C-v4.md) — the v4 spec is frozen here; red-team
   sign-off required before any v4 code or run.
2. `score_boundaries_v4.py` — implements §2 exactly: (i) fit r̂ from
   the 5 corpus files and LOG it BEFORE any decode is loaded (decode
   sha256 re-verified: truth `165fa8af…` / salad `8fb3ba26…`);
   (ii) re-run the v3 DP verbatim and ASSERT byte-identical argmax
   tilings to `boundary_scores_v3.json` — any deviation = instrument
   failure, run VOID; (iii) compute B_v4, M_v4, all four gates, the
   R3b per-char decomposition (totals + per-char rates, both decodes),
   the (c1) perturbation table, the (c2) per-transition numbers, and
   OOV word-share on both argmaxes (R9a carried over). No RNG.
   Standing `grep -rniE "r5005|ct_R5005"` clean required.
3. Run the static margin ONCE; report r̂, M_v4, the four gates, the
   decomposition, and sample argmax tilings.
4. **STOP. The §6 joint pilot does NOT run here** — a red-team
   reviewer clears it separately AFTER the static result. If v4 is
   NULL-v4, the report diagnoses precisely which term/gate failed
   (numbers) and §8 states the line's disposition; a fourth honest
   null is a valid return.

## §5 §6 joint pilot (spec unchanged; gated)

Pilot slice, objectives, seeds 7001–7004, and protocol are exactly
v1 §6 (carried through v2/v3). The pilot bar is unchanged: **pilot
PASS iff joint ≥ 0.15 AND blind ≤ 0.05**; blind > 0.05 →
uninformative, no claim; joint < 0.15 → NEGATIVE. The pilot itself
stays gated on red-team clearance AFTER the v4 static result is
reviewed.

## §6 Pre-registered residual risks (not gate adjustments)

- **Honest prior is NULL-v4 (motivation, not a prediction).** Genuine
  diplomatic French is expected to tile at a better (less negative)
  per-char rate than the ear-noised truth, and the frozen v3 §4.2
  decomposition already showed content-alone favoring the salad
  (−6,555.6 nats, salad-reference). The spec is built to make either
  verdict airtight, not to manufacture PROMISING-v4.
- **r̂ conservatism.** The natural-tiling r̂ is more negative than the
  DP-optimum rate; the bias direction is NULL-leaning (recorded
  above); the (c1) ±20% gate covers fit uncertainty in both
  directions. r̂ is fitted, not tuned: procedure pinned, zero decode
  input, zero degrees of freedom at verdict time.
- **Linearity.** f(m) = r̂·m assumes B_v3 scales with |D| through
  per-word terms (word count ∝ chars at fixed mean word length).
  Pinned; the per-char rate absorbs reference word-length
  distribution by construction.
- **(i)-rejection proof** rests on IEEE-754 strict monotonicity of
  division by a positive constant — exact, no float hazard; the
  byte-identical-tiling assertion in §4 step 2 is its empirical check.
- v4 still cannot see order beyond adjacent bigrams. If the verdict is
  NULL-v4, that boundary is the finding (§7), not a tuning invitation.

## §7 Assessment — what the verdicts mean

**NULL-v4 means the statistical boundary line is exhausted.** After
neutralizing the length channel directly — with a reference-fitted
baseline, absolute content terms at full weight, perturbation-robust
and signal-preserving gates — the length-neutralized content
deviation still does not favor the truth (or a gate fails). The
mechanism is then understood end-to-end: the salad is adversarially
built from common French word-forms in corpus-plausible transitions
(RESULTS-C-v3.md §4.4), while the truth's ear-noise misspellings
depress its unigram/bigram rates below genuine-French expectation —
so no additive per-word/per-transition refinement can separate them.
v3's diagnosis ("adding more content terms will not help") stands
confirmed. **The next step is STRUCTURAL, not v5**: dependency-parse
features — the SPS fallback family — i.e. syntactic well-formedness
that morpheme salad cannot fake and ear noise degrades but does not
erase. Track C does not re-register a fifth statistical variant.

**PROMISING-v4 unlocks a REQUEST for red-team clearance to run the §6
joint pilot** — nothing more. The pilot does NOT run under this spec;
its slice, objectives, seeds, protocol, and bar (§5) are unchanged and
it remains behind its own separate clearance. A PROMISING-v4 would
mean boundary structure DOES separate truth from salad once the
length channel is removed — a claim the static margin alone cannot
carry, which is why the behavioral arbiter (§6) exists.

## §8 Line status

- **v1 — OOV economics:** repaired the length-independent OOV rate.
  Numeric-PROMISING, substantively degenerate.
- **v2 — order-blindness:** repaired the degeneracy (length-scaled
  OOV). Numeric-PROMISING (M=+1,916.4), substantively NULL: a
  word-unigram model cannot see adversarial boundary placement;
  M = +5,057.1 (length) − 3,140.8 (content).
- **v3 — length channel in the raw total:** added word-bigram order
  signal. M=+2,683.9 passed the +800 bar with a non-degenerate
  argmax, but gate (c) caught the recurring pathology as designed:
  per-char every component favored the salad;
  M = +9,239.4 (length) − 6,555.6 (content). The per-transition
  content signal was confirmed real and the length channel indicted
  as the sole remaining enemy.
- **v4 — neutralize the length channel (this spec):** fitted
  reference-text baseline f(|D|)=r̂·|D| subtracted at the comparison
  level; absolute content terms untouched; four binding gates. The
  last statistical repair in this line.
- **If v4 nulls:** the statistical boundary line is CLOSED. No v5.
  Escalate to structural methods — dependency-parse features (SPS
  fallback family). The four nulls, each sharper, are the evidence
  that the boundary is statistical-exhaustion, not under-tuning.
