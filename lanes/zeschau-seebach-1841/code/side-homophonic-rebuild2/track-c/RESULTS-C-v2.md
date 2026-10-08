# TRACK-C v2 RESULTS — length-scaled OOV repair (2026-10-07)

Repair of the v1 degeneracy (RESULTS.md §§2–5) per operator standing order.
Spec frozen in `PREREG-C-v2.md` BEFORE execution (written, then
`score_boundaries_v2.py`, then one static-margin run). v1 `PREREG.md`
untouched. Pilot NOT run — stopped per task; red-team clears separately.

## 1. The repair (executed as specified)

v1: `logP(w) = ln(α/Z)` per word-form for w ∉ V (length-independent) →
DP minimized word count (20-char OOV chunks; B ≈ −1.34·|D|).

v2: **`logP_oov(w) = |w| · ln(p_char)`**, p_char pinned pre-registration:

- **p_char = 5/497,455 = 1.0051160406468926e-05**;
  **ln(p_char) = −11.507822466794325** nats/char.
- Calibration: 28 single-char types in V; rarest is the tie 'q'/'z' at
  count 4 (MIN_COUNT=2). (4+α)/Z with α=1.0, Z=N+αV=486,789+10,666=497,455.
  The 1-char OOV fallback now pays exactly what the rarest observed
  single-char French word pays under identical smoothing — the cheapest
  defensible rate (bias toward the null; no decode consulted).
- Scale: 1-char OOV word = −11.5078 −1.7079 (ln L(1)) −1.2611 (ln ρ) =
  −14.4768; 20-char OOV = −230.1564 −12.4025 −1.2611 = −243.82
  (v1: −26.78). OOV-20 swallowing banned by construction.
- Everything else in v1 §2 unchanged: same corpus/constants, same DP
  (window 20, i-ascending tie-break), same W_len/W_bnd. W_uni now uses
  the length-scaled OOV.

## 2. Static margin (PREREG-C-v2 §2)

| decode | chars | B_v2 | W_uni | W_len | W_bnd | n_words | mean_len | in-vocab |
|---|---|---|---|---|---|---|---|---|
| truth | 3,164 | −11,226.1 | −7,375.6 | −2,159.4 | −1,691.1 | 1,341 | 2.359 | 1,341/1,341 (1.000) |
| salad | 5,143 | −13,142.4 | −8,798.5 | −2,729.8 | −1,614.2 | 1,280 | 4.018 | 1,280/1,280 (1.000) |

**M = +1,916.4 nats** (dW_uni=+1,423.0, dW_len=+570.3, dW_bnd=−76.9).
Numeric bar (M ≥ +800): PASS.

Sample tilings (real word tilings now, not garbage):
- truth: `le|ide|U|Capitre|im|iri|el|Capitre|ii|mi|rie|l|Capitre|iii|a|pur|…`
  length histogram {1:287, 2:709, 3:172, 4:55, 5:46, 6:14, 7:56, 8:1, 9:1}
- salad: `me|ide|pre|plu|progre|ie|leur|ele|propre|ii|e|leur|…`
  length histogram {1:36, 2:388, 3:301, 4:75, 5:77, 6:226, 7:101, 8:4, 9:72}

## 3. Validity precondition (PREREG-C-v2 §2, binding)

Truth argmax: mean 2.359 ∈ [1.765, 7.059] (2× band around ref 3.529) ✓;
in-vocab fraction 1.000 ≥ 0.50 ✓ → **non-degenerate: TRUE**.
Registered-rule verdict: **PROMISING-v2**.

## 4. R3b substance analysis — the margin is still a length effect

Per-char rates (decodes differ in length: 3,164 vs 5,143):

| comp/char | truth | salad | favors |
|---|---|---|---|
| B | −3.5481 | −2.5554 | salad |
| W_uni | −2.3311 | −1.7108 | salad |
| W_len | −0.6825 | −0.5308 | salad |
| W_bnd | −0.5345 | −0.3139 | salad |

**Every component favors the salad per-char.** Length-vs-content
decomposition of M (salad per-char rates as reference):

- dW_uni = +1,423.0 = **+3,385.6 (length)** − 1,962.7 (content)
- dW_len = +570.3 = **+1,050.4 (length)** − 480.1 (content)
- dW_bnd = −76.9 = **+621.1 (length)** − 698.0 (content)
- **M = +1,916.4 = +5,057.1 (length) − 3,140.8 (content)** —
  length share 264% of |M|; content alone favors the salad.

(Reference-rate choice doesn't matter: with truth rates, length +7,022 /
content −5,106 — same conclusion.)

## 5. Verdict

- **Numeric (registered rule): PROMISING-v2** (M=+1,916.4 ≥ +800;
  validity precondition satisfied).
- **Substantive: INVALID FOR PURPOSE — second honest null.** The v2
  repair fixed the DP degeneracy (argmaxes are real word tilings), but
  B_v2 still does not measure boundary-structure separation: the margin
  is a length effect, and per unit of content the salad scores BETTER
  under every component. The §0 question ("does boundary structure
  separate truth from salad?") is answered **NO** under a word-unigram
  model.

Root cause (sharper than v1): the salad's tiles are themselves common
French word-forms by adversarial construction (100% in-vocab on BOTH
argmaxes; salad W_uni/word −6.87 vs truth −5.50/word — the salad tiles
are high-count words). A word-UNIGRAM model cannot see adversarial
boundary placement when the tiles are real words — the boundary signal
lives in word ORDER, which unigrams discard. B_v2 per-char prefers the
salad, so as a search term it would reward the salad direction
(short common-word morphemes = the original de/la-collapse direction).

## 6. Pilot recommendation: DO NOT CLEAR

Running the §6 pilot on B_v2 would arbitrate a term that per-char scores
the salad higher — the same theater RESULTS.md §5 stood down for v1.
The pilot is the behavioral arbiter (R3b), but the per-char analysis
already shows what it would arbitrate: B_v2 guides search AWAY from
truth. Recommend: no pilot on B_v2; re-register with the §7 repair.

## 7. Next repair proposal (word-bigram terms)

Add word-bigram transition log-rates to B: the salad's word ORDER is
adversarial even though its word-forms are French. Diagnostic (same
diplomatic corpus, add-1 bigram model; v2 argmax tilings):

- truth: 874/1,340 adjacent pairs seen in corpus (**0.652**),
  mean log bigram rate **−8.158**/pair
- salad: 480/1,279 adjacent pairs seen (**0.375**),
  mean log bigram rate **−9.094**/pair
- Δ ≈ **0.94 nats/pair** × ~1,300 pairs ≈ **+1,200 nats** truth-favoring,
  and pair counts are nearly equal (1,340 vs 1,279) so a bigram margin
  would be CONTENT-driven, not length-driven — the opposite of the
  unigram margin's pathology.

Boundary-placement features (per-position word-start priors) remain the
second candidate. Re-registration required before any bigram scoring.

## Artifacts

- `PREREG-C-v2.md` (frozen v2 spec; v1 `PREREG.md` untouched)
- `score_boundaries_v2.py` / `boundary_scores_v2.json` (margin + breakdown
  + validity numbers + seg heads)
- `RESULTS-C-v2.md` (this file)
