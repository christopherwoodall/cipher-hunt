# TRACK-C v3 RESULTS — word-bigram boundary score B_v3(D) (2026-10-07)

Repair attempt for the v2 null (RESULTS-C-v2.md §§4–5: a word-UNIGRAM
model cannot see adversarial boundary placement — the signal lives in
word ORDER). Spec frozen in `PREREG-C-v3.md` BEFORE execution (written,
red-team signed off as R9 GO in `redteam/RULINGS.md`, then
`score_boundaries_v3.py`, then one static-margin run). v1 `PREREG.md`
and `PREREG-C-v2.md` untouched. **§6 joint pilot NOT run — stopped per
task; it needs a second red-team clearance after this static result.**

## 1. Implementation (executed as specified)

`score_boundaries_v3.py` implements `PREREG-C-v3.md` §1 exactly:
- s(w) = logP_uni(w) + ln L(|w|) + ln ρ — the v2 pieces verbatim
  (same corpus constants N=486,789, C=1,717,960, V=10,666, α=1.0, β=1.0,
  MAXWLEN=20, ρ=0.283353, p_char, Z=497,455; v2 word_stats/vocab reused,
  NOT re-run — hygiene already passed, carried forward).
- Word-bigram table fit from the SAME diplomatic corpus, same tokenizer
  (WORD_RE → phonetics.project(), empty projections skipped), pairs
  counted within files (no cross-file junctions; 4 junctions/486k —
  immaterial, recorded choice), both tokens required in V
  (MIN_COUNT=2), c(u)=Σ_v c(u,v). Result: 145,715 distinct seen pairs /
  469,672 pair tokens / 10,647 contexts; OOV-bigram fallback add-1 as
  pinned (OOV-context rate ln(1/V)=−9.2748, computed on the fly).
- λ_bi=1.0 hard-coded. First word unigram-only. DP window 20, pinned
  tie-break (j ascending; u lexicographic ascending; first
  strictly-greater on exact float `>`; backpointers same order).
  Component sums asserted to reconstruct B to <1e-6 relative.
- Decode sha256 re-verified before running (truth `165fa8af…` /
  salad `8fb3ba26…` — match the PREREG). No RNG. R5005 untouched.

## 2. Static margin (PREREG-C-v3 §2)

| decode | chars | B_v3 | W_uni | W_bi | W_len | W_bnd | n_words | mean_len | in-vocab | OOV share |
|---|---|---|---|---|---|---|---|---|---|---|
| truth | 3,164 | −21,327.5 | −7,605.6 | −9,923.7 | −2,162.6 | −1,635.6 | 1,297 | 2.439 | 1,293/1,297 (0.997) | 0.0031 |
| salad | 5,143 | −24,011.3 | −8,924.9 | −10,758.0 | −2,739.5 | −1,588.9 | 1,260 | 4.082 | 1,260/1,260 (1.000) | 0.0000 |

**M = +2,683.9 nats** (dW_uni=+1,319.3, dW_bi=+834.4, dW_len=+576.9,
dW_bnd=−46.7; components sum to M exactly).

Sample argmax tilings (real word tilings, not degenerate):
- truth: `le|ide|U|Capitre|im|iri|el|Capitre|ii|mi|rie|l|Capitre|iii|a|pur|…`
  → `i|Capitre|le|parla|lA|a|Capitre|Capitre|de|ce|k|il|ce|k|il|la|…`
  (words 30–46)
  len hist {1:281, 2:617, 3:204, 4:71, 5:52, 6:14, 7:56, 8:1, 9:1}
- salad: `me|ide|pre|plu|progre|ie|leur|ele|propre|ii|e|leur|ele|progre|iii|le|…`
  → `ii|plu|propre|rere|la|tre|guverne|de|ele|propre|ele|propre|tre|me|d|etre|…`
  (words 30–46)
  len hist {1:64, 2:321, 3:281, 4:112, 5:70, 6:236, 7:100, 8:4, 9:72}

## 3. Three-gate evaluation

- **Gate (a) — M ≥ +800:** M = +2,683.9 → **PASS**.
- **Gate (b) — non-degenerate:** truth mean word length 2.439 ∈
  [1.765, 7.059] ✓; truth in-vocab fraction 0.997 ≥ 0.50 ✓ →
  **TRUE**.
- **Gate (c) — STRICT per-char inequality:**
  B_v3(truth)/3,164 = **−6.7407** vs B_v3(salad)/5,143 = **−4.6687**:
  −6.7407 > −4.6687 is **FALSE** → gate (c) **FAILS**.

**Verdict: NULL-v3** — (a)∧(b) pass, (c) fails; per the binding rule
((a)∧¬(c) → NULL-v3) the margin is the v2 pathology recurring.

## 4. R3b substance lens (mandatory)

### 4.1 Component totals + per-char rates (both decodes)

| comp/char | truth | salad | favors |
|---|---|---|---|
| B | −6.7407 | −4.6687 | salad |
| W_uni | −2.4038 | −1.7353 | salad |
| W_bi | −3.1364 | −2.0918 | salad |
| W_len | −0.6835 | −0.5327 | salad |
| W_bnd | −0.5169 | −0.3090 | salad |

**Every component, including the new W_bi, favors the salad per-char.**

### 4.2 Length-vs-content decomposition of M (v2 §4 method, salad reference)

| comp | d | length | content |
|---|---|---|---|
| W_uni | +1,319.3 | +3,434.2 | −2,115.0 |
| W_bi | +834.4 | +4,139.6 | −3,305.3 |
| W_len | +576.9 | +1,054.1 | −477.2 |
| W_bnd | −46.7 | +611.4 | −658.1 |
| **M** | **+2,683.9** | **+9,239.4** | **−6,555.6** |

Length share = 344% of |M|. Truth-reference robustness check: M =
+13,339.8 (length) − 10,655.9 (content) — same conclusion: content
alone favors the salad by −6.6k nats.

### 4.3 OOV word-share on both argmaxes (R9a, binding)

- truth: 4/1,297 words OOV (0.31%); 8/1,296 transitions touch an OOV word.
- salad: 0/1,260 OOV (0.00%); 0 transitions touch OOV.
- The OOV-transition quirk (OOV-context rate −9.2746 cheaper than
  garbled in-vocab transitions) has negligible practical footprint:
  ≤8/1,296 truth transitions, 0 on the salad. Both argmaxes are
  effectively in-vocab; the quirk did not decide the margin.

### 4.4 Bigram-signal diagnostic (v2 §7 parallel, on the v3 argmaxes)

- Seen-pair share: truth 822/1,296 = **0.634**, salad 452/1,259 =
  **0.359** (cf. v2-tiling diagnostic: 0.652 vs 0.375 — essentially
  unchanged).
- Mean log bigram rate /transition: truth **−7.657**, salad **−8.545**.
- **The per-transition bigram signal IS there** — truth's word order is
  markedly more corpus-like per transition. It dies in the per-char
  conversion: the salad's decode is 62% longer in chars with nearly the
  same word count (1,260 vs 1,297; salad mean word 4.082 vs 2.439), so
  every per-word and per-transition penalty dilutes on the salad side.
  W_bi per-char: −3.1364 (truth) vs −2.0918 (salad).

### 4.5 First-word edge check (R9b)

truth first word `le`: s(w₀)=−5.76 = 0.03% of B (≈0.8 transitions);
salad first word `me`: −7.42 = 0.03% of B (≈0.9 transitions). No
edge-effect concentration — the unigram-only first word is immaterial
as anticipated.

## 5. Verdict and numeric diagnosis

**NULL-v3** — gate (c) fails: per-char, the salad wins under every
component, including the bigram term that motivated v3.

Diagnosis of the failure: the §5 pre-registered residual risk
materialized exactly as warned. The v2 §7 diagnostic (+1,200 nats
content-driven bigram advantage) was computed on the FIXED v2
argmaxes; under B_v3 the salad's argmax re-optimized and recovered
the bigram mass — the biggest content-loss term is now W_bi itself
(−3,305.3 nats of content, vs the diagnostic's expected +1,200).
The deeper mechanism: B_v3 is still a raw total, and the truth/salad
LENGTH difference (3,164 vs 5,143 chars) dominates the per-char
conversion. The truth wins the margin by being SHORTER (length share
+9,239.4) while losing on content at −6,555.6. Note the irony:
per-transition, the bigram term favors truth (−7.657 vs −8.545); the
v2-pathology is no longer "unigrams can't see order" — it is "per-char
normalization rewards the longer salad," and gate (c) catches it,
which is exactly what it was built for. The §0 question ("does
boundary structure separate truth from salad?") is answered **NO**
under B_v3 as a raw total vs a longer adversarial decode.

## 6. Next-repair proposal (for red-team review, NOT executed)

A v4 would have to neutralize the length channel rather than add
more content terms: the winning move for the salad is being longer.
Candidates: (a) a length-normalized objective B/|D| as the DP
objective itself (not just a gate); (b) joint modeling of word-count
as a fitted function of |D| rather than the fixed ρ per word. Any
v4 needs its own PREREG + sign-off before scoring — no code written
here.

## Artifacts

- `PREREG-C-v3.md` (frozen v3 spec; v1 `PREREG.md`, `PREREG-C-v2.md`
  untouched)
- `score_boundaries_v3.py` / `boundary_scores_v3.json` (margin +
  breakdown + gates + validity numbers + seg heads; components asserted
  to sum to B)
- `analyze_v3.py` (post-run diagnostics only: B asserted byte-identical
  to the registered run; seen-pair share, per-transition rates,
  first-word check, length histograms)
- `RESULTS-C-v3.md` (this file)

**§6 joint pilot: STOPPED.** Per task and PREREG-C-v3 §3 step 4, the
pilot needs a SECOND, separate red-team clearance after this static
result is reviewed in `redteam/RULINGS.md`. A third honest null is the
return.
