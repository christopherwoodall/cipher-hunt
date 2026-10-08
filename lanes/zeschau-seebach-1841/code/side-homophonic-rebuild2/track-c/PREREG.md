# TRACK-C PREREG — word-boundary-informed scoring diagnostic

**Track:** C (boundary-informed scoring), round-2 fleet. **Date:** 2026-10-07.
**Status:** PRE-REGISTERED — no scored truth/salad comparison has run.
**Awaits:** red-team sign-off in `../redteam/RULINGS.md` before any scoring.

## 0. Question

The rebuilt solver's likelihood (Tocqueville char-5-gram S_char + lexicon
coverage S_word) is Goodharted by morpheme salad: the converged pilot's
salad beats planted truth by 2,601 nats (−2,352.3 vs −4,953.3, verifier
numbers in `../redteam/RULINGS.md`). Neither S_char nor S_cov models WORD
structure — real French word boundaries, word-length distribution, word
unigram rates. The salad tiles morphemes into pseudo-words, but its
word-boundary placement is adversarial, not French. This track tests
whether a boundary-aware word-level score separates planted truth from the
frozen salad.

## 1. Verdict rule (binding)

Let `B(D)` be the boundary-aware score defined in §2, computed IDENTICALLY
on the two frozen decode strings:

- `truth`: 184101 sealed-truth decode (forensics-class; 184101 opened per
  round-1 CLOSING-VERIFICATION caveats), 3,164 chars, sha256
  `165fa8af91ae3ecf03305458a3f6204530f6e16cf52bfec66160f7848dda61f1`
- `salad`: frozen morpheme-salad winner (`pilot/rebuild-pilot-final/result.json`,
  best.assignment), 5,143 chars, sha256
  `8fb3ba26146dbc1eed2d528740ea6819a7bd0c4104adc18e75c093e316b95199`

Both strings frozen in `track-c/decodes.json` (built by
`track-c/build_decodes.py`; decode plumbing only, no scoring).

Margin: **M = B(truth) − B(salad)** (nats; higher = more French-like).

- **PROMISING** iff M ≥ +800 nats → unlocks the §6 joint pilot (and only then).
- **NEUTRAL** iff −800 < M < +800 → no pilot; report as null result.
- **BACKFIRE** iff M ≤ −800 nats (salad wins by ≥800) → no pilot; report.

**Explicit NOT-PROMISING rule:** if M < +800 (NEUTRAL or BACKFIRE), the
300-cell joint pilot in §6 does NOT run. There is no third option and no
re-registration of the bar after seeing M.

The 800-nat bar ≈ 31% of the 2,601-nat salad margin under the current
objective: a boundary term must recover roughly a third of the gap on its
own to be worth joint-inference machinery.

## 2. The boundary-aware score B(D) — exact definition

B(D) is a PURE word-boundary score (no S_char). It composes with the solver
by REPLACING S_word as the word-level term; the diagnostic comparison in §1
scores B alone to isolate the boundary signal.

### 2.1 Input

D = decode string, used **as-is**. Both decodes are already in the lane's
projected phonetic-class alphabet (charsets verified ⊆
`phonetics.alphabet()`; no spaces, all-alpha). NO re-projection is applied
(`project()` is not idempotent on class symbols — it would destroy `C/A/O/U`).

### 2.2 Word model (single source: diplomatic French)

Reference corpus — French diplomatic correspondence, all pre-1862
(Les Mis, 1862, temporally impossible; §4 mechanical check):

| file | sha256 | coverage |
|---|---|---|
| `code/side-period/corpus/nesselrode-v7.txt` | `6879f818…14b8a53` | Nesselrode letters ~1817–1831 |
| `code/side-period/corpus/nesselrode-v8.txt` | `699d5afa…3301ca` | Nesselrode letters 1840–46 (full 1841) |
| `code/side-period/corpus/nesselrode-v9.txt` | `078a771c…3364de5ed` | Nesselrode letters ~1847–1856 |
| `code/side-period/corpus/nesselrode-v10.txt` | `74dc194f…a5bd51ec` | Nesselrode letters ~1847–1849 |
| `code/side-period/corpus/pozzo-di-borgo-correspondance-v1.txt` | `79f4c483…102df6e7a0dcf` | Pozzo di Borgo corresp. 1814–1818 |

(full hashes in `track-c/word_stats.json`)

Tokenization: regex `[A-Za-zÀ-ÿŒœÆæ]+` runs → `phonetics.project()`
(defaults, `silent_finals=True` — the lane's shared phonetic space; the
same function the solver applies to corpus/lexicon). Empty projections
dropped.

Fitted constants (deterministic; `track-c/word_stats.py`, no RNG):

- N = 486,789 word tokens; C = 1,717,960 projected letters
- V = 10,666 types with count ≥ 2 (`MIN_COUNT=2`)
- α = 1.0 (add-α); β = 1.0 (add-β); MAXWLEN = 20
- ρ = N/C = **0.283353** expected words per projected char
  (mean projected word length 3.529 chars)
- Z = N + α·V = 497,455
- log ρ = ln(0.283353) = **−1.2612** nats/word (boundary-count log-prior)
- OOV log-rate = ln(α/Z) = ln(1/497455) = **−13.1169** nats/word
- L(k), k=1..19: (len_count[k]+β)/(N+β·20); L(20) = overflow bin (len ≥ 20):
  (len_count[20]+β)/(N+β·20). Raw len counts in `word_stats.json`.

Word log-rate: `logP(w) = ln((c(w)+α)/Z)` if w ∈ V else `ln(α/Z)`.

### 2.3 DP recurrence (identical code path for truth and salad)

Let X = D, m = |X|.

```
dp[0] = 0.0
for j = 1..m:
    dp[j] = max over i in [max(0, j-20), j-1] of:
        dp[i] + logP(X[i:j]) + ln L(len) + ln ρ
        where len = j-i (bin 20 if len == 20)
    tie-break: iterate i ASCENDING, replace on STRICTLY greater
               (deterministic; ties → smallest i = longest leftmost word)
B(D) = dp[m]
```

Backpointers recover the argmax segmentation w_1..w_n.

Named components (reported with the verdict, re-derivable):

- `W_uni = Σ_i logP(w_i)` — word unigram log-rate sum
- `W_len = Σ_i ln L(|w_i|)` — word-length log-prior sum
- `W_bnd = n · ln ρ` — boundary-count log-prior (n = # words)
- `B = W_uni + W_len + W_bnd`; also report `n`, mean word length `m/n`.

Complexity O(m·20); m ≤ 5,143.

### 2.4 Worked scale intuition (not a prediction)

OOV word ≈ −13.12 + ln L(len) − 1.26 ≈ −16 to −23 nats depending on length;
typical in-vocab word ≈ −6 to −12 nats. Truth (3,164 chars) segments into
real projected French words; salad (5,143 chars) must tile morpheme salad
into corpus words or pay OOV rates. The margin M is whatever the DP finds —
no hand-tuning after seeing it.

## 3. Anti-gaming provisions

1. **No truth-peeking:** the scorer never sees the Les Mis slice, its
   spaces, or its true word boundaries. The DP segmentation is inferred
   from the decode string alone, identically for both decodes.
2. **No Les-Mis-trained weights:** every fitted constant (N, V, α, ρ, L,
   logP) comes from the §2.2 corpus only. Tocqueville is NOT used anywhere
   in Track C. Les Mis in ANY weight source = KILL per standing constraint.
3. **Frozen inputs:** truth/salad strings frozen in `decodes.json` with
   sha256; any re-derivation must reproduce the hashes first.
4. **No bar movement:** §1 rule is binding; M is computed once.

## 4. Les-Mis hygiene gate (pre-scoring KILL vector)

Before scoring: extract projected 15-grams from the §2.2 corpus token
stream; count distinct 15-grams also present in
`data/gutenberg-17489-miserables1.txt` (projected identically).

- 0 matches → proceed.
- 1–5 matches → report the matching 15-grams; proceed only if all are
  generic short-phrase collisions (red-team judges from the report).
- \>5 distinct matches → KILL: do not score; report to red team.

(Temporal argument: all corpus files predate 1862, so Les Mis text is
impossible; this check is belt-and-braces against mislabeled files.)

## 5. Determinism & re-derivation

- `word_stats.py`: no RNG. `score_boundaries.py` (to be written AFTER
  sign-off): no RNG; DP tie-break per §2.3.
- Re-derivation standard: independent implementation from this PREREG must
  match each named component to ≤0.1 nats (same bar as the red-team
  reference numbers).
- No R5005 contact: Track C touches only synthetic 184101 pairs, the
  sealed 184101 key (forensics-class), pilot artifacts, and public-domain
  corpus. (`no_contact=False` in build_decodes.py is the annealer's
  contact-move flag, not a data path — R2 UPHELD.)

## 6. Joint-pilot spec (GATED: runs ONLY if §1 verdict is PROMISING)

**Purpose:** test whether the boundary term guides search toward
truth-like decodes when jointly inferred with the assignment.

### 6.1 Slice (pre-registered, fixed)

- Instance 184101, pairs **0–299** (first 300 cells). 62 distinct groups;
  **55 non-pinned** (pins 11, 70, 82, 34, 29, 40, 46 fixed to anchor values).
- Chance-level primary recovery on slice ≈ 55/296 ≈ 0.19 groups.

### 6.2 Objectives (both on the slice only)

- `J_blind = S_char_slice + S_word_slice − 50·n_poly − 5·S_conc`
  (rebuild objective: per-pair length-normalized S_char; S_word = S_cov −
  S_single with word_minlen=6, λ_word=1.0; conc cap 6; S_potts/S_soft
  omitted in BOTH arms — the pilot isolates the word-level term.)
- `J_joint = S_char_slice + B(D_slice) − 50·n_poly − 5·S_conc`
  (B replaces S_word; B from §2 with the §2.2 constants.)

### 6.3 Search protocol (identical for both arms; only the objective differs)

- Moves: single-group v1 reassignment to any of the 296 inventory values;
  7 pins respected; **n_poly ≡ 0** (v1-only; recovery is measured on
  primaries only, so v2 is out of scope for the prototype).
- Simulated annealing: 4 restarts × 10,000 iterations, geometric cooling
  T0=2.0 → Tend=0.02, seeds **7001, 7002, 7003, 7004**; seeded random init.
  Best-by-objective retained per restart; reported = best of 4.
- Deterministic given seeds; wall-time logged.

### 6.4 Metric and bar

Primary recovery on slice =
(# of the 55 non-pinned slice groups with v1 == planted-truth primary)
/ 55. Truth key read for EVALUATION only (diagnostic; 184101 opened).

- **Pilot PASS** iff recovery(joint best) ≥ 0.15 (≥9/55 groups)
  **AND** recovery(blind best) ≤ 0.05 (≤2/55 groups).
- If blind best > 0.05, the comparison is uninformative (slice too easy for
  the baseline) — report, do not claim.
- If joint best < 0.15 → pilot NEGATIVE.
- Report for both arms: recovery, J components, B(D) of best decode.

## 7. Compliance

- Control/diagnostic only. Never touches R5005.
- No scored comparison (truth vs salad) runs before red-team sign-off in
  `../redteam/RULINGS.md`.
- If verdict is NEUTRAL or BACKFIRE: no pilot; the track reports the margin
  with the §2.3 component breakdown and stops.
- If PROMISING: the §6 pilot is built exactly as specified above; no
  parameter is changed after seeing M.

## 8. Pre-sign-off state (for the reviewer)

Done (no scoring): `build_decodes.py` + `decodes.json` (frozen decode
strings + provenance), `word_stats.py` + `word_stats.json` +
`word_vocab.json` (reference corpus statistics, public-domain text only).
NOT done: `score_boundaries.py` (will be written after sign-off), the
§4 hygiene check, any truth-vs-salad numeric comparison, any pilot code.
