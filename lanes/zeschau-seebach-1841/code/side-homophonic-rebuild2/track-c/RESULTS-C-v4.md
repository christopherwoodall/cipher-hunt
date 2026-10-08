# TRACK-C v4 RESULTS — length-neutralized boundary score B_v4(D) (2026-10-07)

Repair attempt for the v3 null (RESULTS-C-v3.md §§4–5: the raw-total
objective's LENGTH CHANNEL dominates — M = +9,239.4 length vs −6,555.6
content; per-char every component favors the 62%-longer salad). v4
neutralizes the length channel directly: B_v4(D) = B_v3(D) − r̂·|D|
with r̂ = S_R/m_R fitted on reference text only. Spec frozen in
`PREREG-C-v4.md` BEFORE execution (written, red-team signed off as
R10 GO in `redteam/RULINGS.md` — honoring R10a as a wording note, no
action; R10b as recorded hardness, reported below — then
`score_boundaries_v4.py`, then one static-margin run). v1 `PREREG.md`,
`PREREG-C-v2.md`, `PREREG-C-v3.md` untouched. **§6 joint pilot NOT run
— stopped per task; it needs a further, separate red-team clearance
after this static result is reviewed.**

## 1. Implementation (executed as specified)

`score_boundaries_v4.py` implements `PREREG-C-v4.md` §2/§4 exactly, in
the binding execution order:

- **Phase 1 (r̂ fit, REFERENCE TEXT ONLY):** the 5 diplomatic corpus
  files (`nesselrode-v7/8/9/10`, `pozzo-di-borgo-correspondance-v1`),
  natural tokenization (WORD_RE → `phonetics.project()` defaults,
  empty projections skipped), ALL v2/v3 constants verbatim
  (α=1.0, Z=497,455, ln ρ=−1.2610620550768965, ln L add-β len model,
  ln(p_char)=−11.507822466794325, add-1 bigram over V=10,666 with
  ln(1/V)=−9.2746 OOV-context fallback, λ_bi=1.0 pinned), first token
  of each file unigram-only, consecutive pairs within files only. Fit
  completed and LOGGED (`rhat_fit_v4.json`) BEFORE any decode byte
  was read — the fit path never touches `decodes.json` (`load_inputs`
  is called only in phase 2).
- **Phase 2 (drift check):** decode sha256 re-verified inside
  `v3.load_inputs()` (truth `165fa8af…` / salad `8fb3ba26…` — match);
  the v3 DP re-run VERBATIM (imported, not duplicated) and ASSERTED
  byte-identical to `boundary_scores_v3.json`: first-30-word argmax
  tilings match exactly AND all twelve recorded aggregates
  (B, W_uni, W_bi, W_len, W_bnd, n_words, n_transitions, mean_wlen,
  n_oov, n_invocab, invocab_frac, oov_share) match with exact float
  equality on both decodes. **Drift check PASSED** — no instrument
  VOID. Decode lengths re-confirmed 3,164 / 5,143, Δm = 1,979 as
  pinned.
- **Phase 3:** B_v4, M_v4, four gates, (c1) table, (c2) numbers,
  OOV shares, R3b decomposition. Deterministic, no RNG. Standing
  `grep -rniE "r5005|ct_R5005"` over `track-c/`: hits only in
  compliance prose ("no R5005 contact") — clean.

## 2. r̂ fit (phase 1, reference text only)

| file | K tokens | m chars | S_F (nats) | S_F/m | W_uni | W_bi | W_len | W_bnd | OOV |
|---|---|---|---|---|---|---|---|---|---|
| nesselrode-v7 | 78,957 | 271,250 | −1,427,925.6 | −5.2642 | −627,122.8 | −544,167.9 | −157,065.2 | −99,569.7 | 1,826 |
| nesselrode-v8 | 92,594 | 318,369 | −1,641,518.1 | −5.1560 | −714,248.0 | −625,392.9 | −185,110.5 | −116,766.8 | 1,860 |
| nesselrode-v9 | 85,246 | 296,428 | −1,511,713.5 | −5.0998 | −656,082.5 | −576,984.1 | −171,146.4 | −107,500.5 | 1,651 |
| nesselrode-v10 | 82,436 | 293,098 | −1,475,109.5 | −5.0328 | −638,647.9 | −565,196.0 | −167,308.7 | −103,956.9 | 1,526 |
| pozzo-di-borgo-correspondance-v1 | 147,556 | 538,815 | −2,568,154.0 | −4.7663 | −1,075,676.8 | −1,002,591.5 | −303,808.4 | −186,077.3 | 1,926 |
| **TOTAL** | **486,789** | **1,717,960** | **−8,624,420.7** | — | — | — | — | — | — |

**r̂ = S_R/m_R = −8,624,420.7 / 1,717,960 = −5.020152 nats/char.**
Sanity: ΣK = 486,789 = N ✓; Σm = 1,717,960 = C_letters ✓ (natural
tokenization reproduces the fitted corpus constants exactly). r̂ ∈
(−25, 0) ✓ — not VOID.

**R10b hardness (recorded, reporting where r̂ lands):** gate (a)
M_v4 ≥ +800 needs r̂ ≥ (800 − 2,683.864)/1,979 = **−0.9519** nats/char.
Fitted r̂ = **−5.0202** — the model scores genuine reference French
5.3× worse per char than the bar would require (i.e. PROMISING-v4
needed French-at-adversarial-tiling rates, −0.95 vs the −4.7/−6.7 of
the DP's best tilings). The honest prior stands recorded; the
NULL-v4 close below is the load-bearing outcome.

## 3. Static margin (PREREG-C-v4 §2)

| decode | chars | B_v3 | −r̂·\|D\| removed | B_v4 | per-char B_v4 |
|---|---|---|---|---|---|
| truth | 3,164 | −21,327.5 | +15,883.8 | **−5,443.7** | **−1.7205** |
| salad | 5,143 | −24,011.3 | +25,818.6 | **+1,807.3** | **+0.3514** |

**M_v4 = −7,251.0 nats** = M_v3 (+2,683.9) + 1,979·r̂ (−9,934.9).

Note the per-char invariance under the repair: B_v4/m = B_v3/m − r̂
shifts both sides by the identical +5.0202 nats/char, so the per-char
comparison ordering is exactly v3's gate (c) (−6.7407 vs −4.6687) —
the repair acts on the TOTAL, which is where the length channel
lived. The v4 comparison reads: truth's DP-optimum tiling sits
**1.72 nats/char BELOW** the genuine-French rate; the salad's
adversarial tiling sits **0.35 nats/char ABOVE** it. Content deviation
from French expectation favors the salad by 2.07 nats/char.

Sample argmax tilings (byte-identical to v3, carried over):
- truth: `le|ide|U|Capitre|im|iri|el|Capitre|ii|mi|rie|l|Capitre|iii|a|pur|…`
- salad: `me|ide|pre|plu|progre|ie|leur|ele|propre|ii|e|leur|ele|progre|iii|le|…`

## 4. Four-gate evaluation

- **Gate (a) — M_v4 ≥ +800 at fitted r̂:** M_v4 = **−7,251.0** → **FAILS**
  (by 8,051 nats).
- **Gate (b) — non-degenerate (carried over unchanged):** truth mean
  word length 2.439 ∈ [1.765, 7.059] ✓; truth in-vocab fraction
  0.997 ≥ 0.50 ✓ → **TRUE** (asserted-identical tilings to the v3
  PASS).
- **Gate (c1) — fit-perturbation robustness:** M_v4 ≥ +800 under
  r̂′ = 0.8·r̂ (−4.0161) → **−5,264.0 → FAILS**; under r̂′ = 1.2·r̂
  (−6.0242) → **−9,238.0 → FAILS**. The binding end is 1.2·r̂ as
  pinned (r̂ < 0 ⇒ most negative ⇒ smallest M_v4). Even the +20%-up
  (least negative) end misses by 6,064 nats — no knife-edge anywhere
  near the bar.
- **Gate (c2) — content-signal integrity:** mean per-transition log
  bigram rate truth **−7.6572** > salad **−8.5449** (strict ✓);
  seen-pair share truth **822/1,296 = 0.6343** > salad **452/1,259 =
  0.3590** (strict ✓) → **TRUE**. The confirmed per-transition
  signal survives the repair intact — the margin was not bought by
  inverting it.

**Verdict: NULL-v4** — (b)∧(c2) pass, (a) and (c1) fail. Per the
binding rule ((a)∧¬(c1∧c2) → NULL-v4, and (a)-fail alone suffices),
the length-neutralized content deviation does not favor the truth.

## 5. R3b substance lens (mandatory)

### 5.1 Component totals + per-char rates (both decodes)

| comp | truth total | salad total | truth /char | salad /char | favors |
|---|---|---|---|---|---|
| W_uni | −7,605.6 | −8,924.9 | −2.4038 | −1.7353 | salad |
| W_bi | −9,923.7 | −10,758.0 | −3.1364 | −2.0918 | salad |
| W_len | −2,162.6 | −2,739.5 | −0.6835 | −0.5327 | salad |
| W_bnd | −1,635.6 | −1,588.9 | −0.5169 | −0.3090 | salad |
| baseline −r̂·\|D\| | +15,883.8 | +25,818.6 | +5.0202 | +5.0202 | (identical shift) |
| B_v4 | −5,443.7 | +1,807.3 | −1.7205 | +0.3514 | salad |

Every content component still favors the salad per char — the
length-neutralization does not rescue any of them; it removes the
length channel as an absolute credit (+15.9k vs +25.8k nats) and the
salad wins the content comparison outright.

### 5.2 M_v4 decomposition (length channel removed as an absolute credit)

| term | nats |
|---|---|
| M_v3 (raw total) | +2,683.9 |
| ├ dW_uni | +1,319.3 |
| ├ dW_bi | +834.4 |
| ├ dW_len | +576.9 |
| └ dW_bnd | −46.7 |
| length-baseline adjustment 1,979·r̂ | −9,934.9 |
| **M_v4** | **−7,251.0** |

The v3 margin (+2,683.9) decomposes against the adjustment (−9,934.9):
the absolute content terms (incl. the +834.4-nat W_bi edge v4 was
built to protect) are real but are outweighed ~3.7× by the
length-attributable mass the salad carried. Contrast v3's gate-(c)
framing: there the salad won per-char by dilution; here it wins the
absolute length-neutralized total — the truth is farther below
French expectation (−1.7205/char) than the salad is above it
(+0.3514/char).

### 5.3 OOV word-share on both argmaxes (R9a, binding)

- truth: 4/1,297 words OOV (0.31%); 8/1,296 transitions touch an OOV word.
- salad: 0/1,260 OOV (0.00%); 0 transitions touch OOV.
- Unchanged from v3 (asserted-identical tilings): the OOV-transition
  quirk has negligible footprint; both argmaxes are effectively
  in-vocab.

### 5.4 Confirmed-signal check (v3 §4.4 parallel, on the v4 tilings)

Seen-pair share truth 0.634 vs salad 0.359; mean log bigram rate
per transition −7.657 vs −8.545. The per-transition bigram signal IS
real and IS preserved — it simply cannot overcome the absolute
content deficit once the length channel is neutralized.

## 6. Verdict and numeric diagnosis

**NULL-v4** — gates (a) and (c1) fail; (b) and (c2) pass.

Diagnosis of the failure: the mechanism the PREREG §6 pre-registered
as the honest prior is now measured end-to-end. The salad is
adversarially built from common French word-forms in corpus-plausible
transitions, so its DP-optimum tiling scores ABOVE the genuine-French
reference rate (+0.35 nats/char); the truth's ear-noise misspellings
depress its unigram/bigram rates BELOW genuine-French expectation
(−1.72 nats/char). Removing the length channel as an absolute credit
(−9,934.9 nats, 3.7× the v3 margin) exposes the content-deviation
comparison directly: M_v4 = −7,251.0. No additive per-word or
per-transition refinement can separate the two, because the model's
per-transition vocabulary is exactly the salad's construction
material while the truth pays ear-noise penalties on nearly every
token. v3's diagnosis ("adding more content terms will not help")
stands confirmed at the length-neutralized level — this is the
statistical-exhaustion boundary, not under-tuning.

## 7. Line status (PREREG-C-v4 §8)

**The statistical boundary line is CLOSED.** v1 (OOV economics),
v2 (order-blindness), v3 (length channel in the raw total), v4
(length-neutralized content deviation) — four nulls, each sharper,
each diagnosing the next repair, each honestly returned. No v5.
**Structural escalation:** dependency-parse features — the SPS
fallback family — i.e. syntactic well-formedness that morpheme salad
cannot fake and ear noise degrades but does not erase. Track C does
not re-register a fifth statistical variant.

## Artifacts

- `PREREG-C-v4.md` (frozen v4 spec; v1 `PREREG.md`, `PREREG-C-v2.md`,
  `PREREG-C-v3.md` untouched)
- `score_boundaries_v4.py` (phase-1 r̂ fit logged before any decode
  byte; phase-2 verbatim v3 DP re-run with byte-identical-tiling
  assertion; phase-3 B_v4 + four gates + R3b decomposition; no RNG)
- `rhat_fit_v4.json` (r̂ fit log: per-file S_F/m_F, S_R, m_R, r̂)
- `boundary_scores_v4.json` (B_v4 both decodes, M_v4 decomposition,
  four gates, (c1) table, (c2) numbers, OOV shares, verdict)
- `RESULTS-C-v4.md` (this file)

**§6 joint pilot: STOPPED.** Per task and PREREG-C-v4 §4 step 4, the
pilot needs a FURTHER, separate red-team clearance after this static
result is reviewed in `redteam/RULINGS.md`. A fourth honest null is
the return.
