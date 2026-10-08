# CALIBRATION.md — Seebach next-token predictor (DRAFT: numbers pending)

> Status: DB rebuilt 2026-10-07 after the 2026-10-07 builder died in a daemon
> restart leaving an empty DB (all tables created, zero rows, stale `-journal`;
> `build.py` commits only after a full mode finished, so the kill lost
> everything before the first commit). Diagnosis: **empty model, not a query
> bug** — `predict.py` was correct; with an empty unigram table the backoff
> distribution is empty and the beam dies, hence `[]`.
> Fix: `build.py` now upserts per source file and commits after every file
> (a kill loses at most one file; rerun starts clean because `build.py`
> deletes the DB first). Pruning stays global (delete-after-load on summed
> counts), so the model is identical to the original accumulate-then-insert
> design. `calibrate.py` fixes: `mismatch_quant` no longer holds all TRAIN
> streams in memory (streams per file) and the cells/word denominator now
> counts every training word (the original divided total TRAIN cells by the
> 200k-word *sample* count, inflating cells/word ~17x); targeted-context beam
> work capped at the first 120 occurrences per phrase so the run finishes
> (cell-level ranks still use every occurrence).
>
> Calibration run: PENDING — sections A–D below will be filled from
> `calibrate.py` JSON output once the build finishes.

## Method (what was measured)

- **Held-out = 3 whole documents, never counted in training** (no leakage):
  `guizot-memoires-t2-gutenberg.txt`, `revue-deux-mondes-1841-q4.txt`,
  `talleyrand-memoires-v1.txt`. The build's `HELDOUT` list is excluded from
  every n-gram count; calibration re-segments them with the same
  `tokenize.segment_stream` pipeline used in training.
- **Scoring**: stupid backoff (weight 0.4), orders 1–6, longest-match; rank of
  the true next cell is optimistic (`1 + #{w: P(w) > P(true)}`), ties favor
  the model.
- **A. Global next-cell accuracy**: 20,000 sampled positions (stratified by
  document length, seed 7), top-1/3/5 + MRR, broken down by available context
  length. Separately for `standard` and `--byear`.
- **B. Targeted solved contexts**: every held-out occurrence of
  "la première", "par ce que", "par le", "qui", "que", "ce qui", "en ce",
  "m'en", "ne" (+ the 25 most frequent "ne X" bigrams → rank of "pas"):
  rank of the true next cell (all occurrences) and rank of the true next
  word 1–3 cells via the beam (first ≤120 occurrences/phrase).
- **C. Verb stems**: top-30 stems mined from TRAINING word counts; rank of
  the true cell following each stem in held-out.
- **D. By-ear mismatch quantification**: segmentation disagreement rate on a
  200k-word sample, cells/word, vocab overlap (Jaccard), by-ear-only vs
  standard-only cells, banked-cell rank shifts.

## A. Global next-cell accuracy (held-out, n=20,000)

PENDING — table will show top-1 / top-3 / top-5 / MRR per mode, plus
accuracy by context length (1..5 cells).

## B. Targeted solved contexts (held-out)

PENDING — per-phrase: segmentation in each mode, occurrence count,
next-cell top-1/3/5, next-word (beam, ≤120 occ) top-1/3/5, plus 3 examples
each with the model's top-5 beam vs the true continuation.

### "ne X" → "pas" frames (25 most frequent held-out bigrams)

PENDING.

## C. Verb-stem inflection prediction (held-out)

PENDING — per stem: occurrences, top-1/3/5, MRR.

## D. By-ear mismatch quantification (TRAIN)

PENDING — word disagreement rate, cells/word per mode, vocab sizes,
Jaccard overlap, mode-exclusive cells, banked-cell ranks/counts.

### Known by-ear divergences (by design, not bugs)

- `prend` → `pren` (R3: silent -d/-t dropped after nasal). The frenchman's
  ear reads `pre` — the model emits `pren`; the applier must map both.
  Documented in `byear.py`; the banked cell `est` is exempted.
- `-ment` → `m|ent` (attested 82-06), `-erre` → `er|e` (R4/R8), glide splits
  (`mienne` → `m|i|ne`), `-ne`/`-me` tails (`personne` → `per|so|ne`,
  `dame` → `dam|e`).
- R2 (inconsistent cutting) is NOT simulated: `byear_cut` is one
  deterministic canonical cut. The clerk is not deterministic; query both
  modes when a `--byear` context looks dead.

## Corpus inventory

TRAIN (11 docs, French only):

PENDING — per-file bytes / raw words / cells per mode (from build log).

HELDOUT (3 whole documents, never trained on):

PENDING.

EXCLUDED from both (per the language audit in `build.py`): the 15
Allgemeine-Zeitung January-1841 issues (German, Fraktur OCR), the ADB
Zeschau entry, the 2 Metternich volumes (Fraktur OCR + German editorial),
and the mixed English/French Levant volume. Rationale: the cipher is
French diplomatic prose; German OCR noise would pollute the cell
inventory. (Trade-off recorded under weaknesses: German proper nouns
appearing in the French text are learned only insofar as French authors
wrote them.)

## Smoke tests (exact CLI contract)

PENDING — outputs of the 4 README contract queries will be pasted here.

## Honest weaknesses

PENDING — to be written from the numbers, but the structural ones are:

1. **Stupid backoff, no smoothing beyond the unigram floor**: unseen
   contexts collapse to 0.4^5-scaled unigrams; the model is confident about
   frequent bigrams and vague everywhere else.
2. **No word-boundary or sentence markers**: the stream is flat cells, so
   the model cannot learn "word-initial" vs "word-internal" distributions —
   deliberate (the cipher is a continuous pair stream), but it costs
   accuracy at word onsets.
3. **OCR noise in TRAIN**: archive.org `_djvu.txt` OCR (especially the
   Revue des Deux Mondes scans) injects garbage cells into the vocab;
   tokens >30 chars and digit-tokens are dropped, but mid-word OCR errors
   survive as rare cells.
4. **By-ear mode is a single canonical cut** (R2 not simulated); the
   clerk's inconsistency means some true contexts will miss in both modes.
5. **Whole-document holdout is only 3 documents** (one author-heavy:
   Talleyrand); genre shift (memoirs vs correspondence vs periodical) is
   only partially covered.
6. **Never tested against the cipher stream** — all numbers above are
   French-text perplexity-style ranks, not group-mapping accuracy.
   Calibrate mapping thresholds on the banked cribs, not on these probs.
7. `prob` is a joint stupid-backoff score, not renormalized over the
   returned set; do not compare raw probs across contexts or modes.
