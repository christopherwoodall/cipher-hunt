# TRACK-C RESULTS — boundary-aware scoring diagnostic (2026-10-07)

Red-team R3 GO received; §4 hygiene gate run first, then `score_boundaries.py`
(written after sign-off, per PREREG §8). PREREG.md is otherwise frozen
(R3a typo fix applied: C = 1,717,960).

## 1. Hygiene gate: PASS

`hygiene_gate.py` → `hygiene_gate.json`: 486,019 distinct projected
15-grams in the diplomatic corpus, 122,466 in Les Misérables,
**0 shared**. Scoring proceeded.

## 2. Static margin (PREREG §1)

| decode | chars | B | W_uni | W_len | W_bnd | n_words | mean_len | n_oov |
|---|---|---|---|---|---|---|---|---|
| truth | 3,164 | −4,241.7 | −2,079.4 | −1,961.8 | −200.5 | 159 | 19.90 | 158 |
| salad | 5,143 | −6,890.1 | −3,378.7 | −3,184.7 | −326.6 | 259 | 19.86 | 256 |

**M = B(truth) − B(salad) = +2,648.4 nats** (dW_uni=+1,299.3, dW_len=+1,223.0,
dW_bnd=+126.1). Numeric rule (M ≥ +800) → **PROMISING**.

## 3. The verdict is VACUOUS — B(D) as specified is degenerate

The DP argmax segmentation is not a word segmentation:

- Truth: 158/159 "words" OOV, mean length **19.90** chars (reference: 3.53).
  Salad: 256/259 OOV, mean 19.86. Both tilings are ~20-char garbage chunks,
  e.g. truth: `leideUCapitreimiriel|CapitreiimirielCapit|reiiiapurvekeCapitre|…`
- Per-char rates are **identical**: truth B/char = −1.34060,
  salad B/char = −1.33970 (Δ = 0.0009 nats/char). The +2,648.4 margin is
  99.9% decode length (5,143 vs 3,164 chars), 0.1% content.
- dW_bnd = +126.106 = **exactly** −(Δn)·ln ρ — pure word-count arithmetic.
  dW_uni ≈ Δn_oov·ln(α/Z) — same story. Every component is a length proxy.

**Root cause (spec flaw, not implementation bug):** the OOV log-rate
ln(α/Z) = −13.12 is *per word-form*, independent of length. A 20-char OOV
"word" costs −13.12 −12.40 (ln L(20); only 1 reference token ≥20 chars) −1.26
= −26.78 for 20 chars (−1.34/char), while real projected French words cost
≈ −11.4/word ≈ −3.2/char at mean length 3.5. The DP therefore minimizes word
count instead of finding word boundaries — the length prior is orders of
magnitude too weak to stop OOV-20 swallowing. `score_boundaries.py`
implements the PREREG recurrence exactly; the economics are the spec's.

This is precisely the R3b caveat's mechanism, confirmed arithmetically:
B(D) ≈ −1.34·|D| — a length penalty in disguise, not a boundary score.

## 4. Verdict

- **Numeric (binding rule): PROMISING** (M = +2,648.4 ≥ +800).
- **Substantive: INVALID FOR PURPOSE.** B(D) does not measure word-boundary
  structure; the margin carries zero information about French word
  placement. The track's §0 question ("does boundary structure separate
  truth from salad?") is NOT answered by this M.

## 5. §6 joint pilot: NOT RUN — deliberate, with justification

Running the pilot on this B would maximize
J_joint = S_char + B(D) − penalties ≈ S_char − 1.34·|D| − penalties:
a length penalty that rewards short morpheme values (the original
frozen de/la-collapse direction), not truth-like decodes. The pilot's
behavioral bar would be arbitrating a broken term — theater, not evidence.
Per PREREG §6's stated purpose ("the boundary term guides search toward
truth-like decodes"), the pilot is stood down until B is re-registered.

## 6. Re-registration proposal (not executed; needs red-team sign-off)

The OOV cost must scale with length. Minimal fix: for w ∉ V,
`logP_oov(w) = |w| · ln(p_char)` with a fixed per-char rate p_char
(exact value + justification to be pinned in the re-registration; candidate:
calibrate so a 1-char OOV ≈ the unigram rate of a rare in-vocab
single-char word). Everything else in PREREG §2 unchanged. Then re-run the
static margin; run the §6 pilot ONLY if the new M ≥ +800 coincides with a
non-degenerate argmax (mean word length within 2× of reference 3.53,
majority in-vocab words) — to be written into the re-registration as a
validity precondition, so a degenerate PROMISING cannot recur.

## 7. Lesson for the lane

Any segmentation-based score with a per-form (length-independent) OOV rate
collapses to word-count minimization and becomes a length meter. This
applies to any future word-level proposal: the OOV model needs a per-char
cost, or the DP optimum is degenerate by construction. (Track B's neural
char LM does not segment — unaffected.)

## Artifacts

- `PREREG.md` (frozen spec + R3a fix), `RULINGS.md` R3 GO (redteam dir)
- `hygiene_gate.py` / `hygiene_gate.json` (PASS, 0 shared 15-grams)
- `score_boundaries.py` / `boundary_scores.json` (margin + breakdown)
- `word_stats.py` / `word_stats.json` / `word_vocab.json` (reference model)
- `build_decodes.py` / `decodes.json` (frozen decode strings + sha256)
- `RESULTS.md` (this file)
