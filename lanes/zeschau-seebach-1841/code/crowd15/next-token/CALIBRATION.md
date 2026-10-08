# CALIBRATION.md — Seebach next-token predictor

## Build & repair history (read first)

- **2026-10-07, first builder**: died in a daemon restart mid-build, leaving an
  EMPTY `models/seebach_nexttoken.db` (tables created, zero rows, stale
  `-journal`). `build.py` committed only after a full mode finished, so the
  kill lost everything before the first commit.
- **Diagnosis (2026-10-07)**: the empty query results (`predict.py --context
  "pre m i er e" --k 5 --byear` → `[]`) were an **empty model, not a query
  bug**. `predict.py` was correct; with an empty unigram table the stupid-
  backoff distribution is empty and the beam search dies immediately.
- **2026-10-07, rebuild v2** (per-file `ON CONFLICT` upserts): killed by me —
  upserts against the growing PK degraded steeply (file 3's ~2.8M-row upsert
  still running after 15 min).
- **2026-10-07, rebuild v3** (staging design): per-file counts append into a
  separate `stage.db` (no indexes, commit per file), then one `GROUP BY`
  aggregation per mode into the indexed final tables. Pruning stays GLOBAL
  (delete-after-load on summed counts) — the model is identical to the
  original accumulate-then-insert design. **A VM reboot killed v3 mid-staging**;
  the straggler `stage.db` had no file markers so its completeness was
  unverifiable and it was discarded.
- **2026-10-08, rebuild v4 (final)**: staging records the filename, commits
  per file, **resumes** after a kill/reboot (skips staged files, verifies all
  TRAIN files staged before aggregating, wipes staging if TRAIN changes).
  Built clean in ~18 min: `built_utc=2026-10-08T01:32:26Z`.
  Also dropped the redundant `idx_ngram_lookup` — `(mode,ord,ctx)` is a
  leftmost prefix of the ngram PK, verified with `EXPLAIN QUERY PLAN`.
- **2026-10-08, calibration**: the builder's `calibrate.py` never ran.
  Fixes applied before running: (1) progress prints moved to stderr so
  stdout stays pure JSON; (2) `mismatch_quant` rewritten to stream per file
  and fixed a denominator bug (it divided total TRAIN cells by the 200k-word
  *sample* count, inflating cells/word ~17x); (3) removed an unbounded
  per-context full-distribution cache that OOM-killed the first attempt
  (5-cell contexts are ~all distinct; 16.7k-entry dict × 20k contexts);
  (4) bounded `Model._cand_cache` at 8192 entries (FIFO); (5) targeted-
  context beam work capped at first 40 occurrences/phrase (was 400, then
  120 — each beam predict costs ~8s under machine contention); cell-level
  ranks still use EVERY occurrence. (6) After a second VM reboot killed a
  135-min calibration run with zero output (JSON is written only at the
  end), added **checkpointing**: per-section and per-phrase results persist
  to `calibrate_checkpoint.json` (validated against the DB's `built_utc`);
  reruns resume where they left off.

## Method

- **Held-out = 3 whole documents, never counted in training** (no leakage):
  `guizot-memoires-t2-gutenberg.txt`, `revue-deux-mondes-1841-q4.txt`,
  `talleyrand-memoires-v1.txt`. Re-segmented with the same
  `tokenize.segment_stream` pipeline used in training.
- **Scoring**: stupid backoff (weight 0.4), orders 1–6, longest-match; rank
  of the true next cell is optimistic (`1 + #{w: P(w) > P(true)}`), ties
  favor the model.
- **A. Global next-cell accuracy**: 20,000 sampled positions (stratified by
  document length, seed 7), top-1/3/5 + MRR, per mode.
- **B. Targeted solved contexts**: every held-out occurrence of
  "la première", "par ce que", "par le", "qui", "que", "ce qui", "en ce",
  "m'en", "ne" (+ the 25 most frequent "ne X" bigrams → rank of "pas"):
  rank of the true next cell (all occurrences) and rank of the true next
  word 1–3 cells via the beam (first ≤40 occurrences/phrase).
- **C. Verb stems**: top-30 stems mined from TRAINING word counts; rank of
  the true cell following each stem in held-out (capped at 600 occurrences
  per stem).
- **D. By-ear mismatch quantification**: segmentation disagreement on a
  200k-word sample, cells/word, vocab overlap (Jaccard), banked-cell ranks.

## A. Global next-cell accuracy (held-out)

| mode | n | top-1 | top-3 | top-5 | MRR |
|---|---|---|---|---|---|
| standard | 19,998 | 32.1% | 45.8% | 52.2% | 0.418 |
| byear | 19,999 | 33.4% | 47.2% | 53.7% | 0.432 |

**Byear beats standard by ~1.3 points top-1.** The fine-cut cells are
slightly more predictable in aggregate — plausible: by-ear splits expose
morphological boundaries (mute -e, -ment) that carry signal.

**Caveat — the by-context-length breakdown is degenerate**: 100% of sampled
positions have the full 5-cell context (positions are sampled at i≥1 in
million-cell documents, so i≥5 almost always). The builder intended to show
backoff degradation at short contexts, but the sampler never produces them.
Backoff behavior at 1–4 cell contexts is therefore UNMEASURED here; the
numbers above are effectively order-6 (5-cell context) accuracy only.

## B. Targeted solved contexts (held-out)

| phrase | mode | cells | occ | next-cell top-1/3/5 | next-word top-1/3/5 (beam, n=40) |
|---|---|---|---|---|---|
| la première | standard | la\|pre\|mie\|re | 198 | 26.3%/35.9%/41.9% | 32.5%/45.0%/47.5% |
| la première | byear | la\|pre\|m\|i\|er\|e | 198 | 24.2%/33.3%/38.4% | 30.0%/32.5%/35.0% |
| par ce que | standard | par\|ce\|que | 77 | 13.0%/31.2%/51.9% | 15.0%/37.5%/62.5% |
| par ce que | byear | par\|ce\|que | 77 | 14.3%/31.2%/50.6% | 15.0%/40.0%/57.5% |
| par le | standard | par\|le | 820 | 24.5%/31.2%/35.4% | 22.5%/25.0%/35.0% |
| par le | byear | par\|le | 820 | 24.8%/32.0%/35.9% | 22.5%/25.0%/35.0% |
| qui | standard | qui | 7,359 | 10.6%/21.9%/30.7% | 5.0%/20.0%/32.5% |
| qui | byear | qui | 7,363 | 10.8%/22.1%/30.8% | 5.0%/20.0%/32.5% |
| que | standard | que | 17,027 | 17.5%/32.9%/42.1% | 22.5%/35.0%/55.0% |
| que | byear | que | 17,030 | 17.5%/32.9%/42.2% | 22.5%/35.0%/55.0% |
| ce qui | standard | ce\|qui | 637 | 14.1%/26.8%/34.2% | 15.0%/20.0%/30.0% |
| ce qui | byear | ce\|qui | 637 | 14.8%/27.9%/35.6% | 17.5%/22.5%/32.5% |
| en ce | standard | en\|ce | 117 | 29.9%/48.7%/54.7% | 35.0%/50.0%/57.5% |
| en ce | byear | en\|ce | 117 | 29.9%/48.7%/53.8% | 35.0%/47.5%/57.5% |
| m'en | standard | m\|en | 95 | 8.4%/17.9%/24.2% | 17.5%/20.0%/22.5% |
| m'en | byear | m\|en | 93 | 8.6%/18.3%/24.7% | 17.5%/20.0%/22.5% |
| ne | standard | ne | 12,585 | 32.0%/42.9%/48.4% | 40.0%/52.5%/60.0% |
| ne | byear | ne | 15,609 | 23.6%/35.1%/41.9% | 30.0%/45.0%/55.0% |

Notes:
- "la première" → the model's top beam is `fois` in both modes (see
  examples below); top-1 24–26% because the true continuation varies
  ("lettre", "dépêche", "tenue", "pensée", …).
- "m'en" is the hardest solved context (8–9% top-1): the verb after
  "m'en" is genuinely unpredictable from 2 cells.
- "ne": byear has 24% MORE "ne" occurrences (15,609 vs 12,585) because the
  -ne/-me splits expose extra "ne" cells — and its top-1 is 8 points LOWER
  (23.6% vs 32.0%), because those extra "ne" cells sit in more diverse
  following contexts. The by-ear segmentation buys crib-cell frequency at
  the cost of noisier "ne" conditionals.
- "que"/"qui"/"ce qui"/"par le"/"en ce": modes agree within noise.

### Examples — "la première" (true next 3 cells vs model top-5 beam)

standard:
- true `nou|vel|le` → beam: `fois`, `de`, `re`, `fois|que`, `et`
- true `te|nue|le` → beam: `par`, `par|tie`, `par|tie|de`, `an`, `e`
- true `pen|see|du` → beam: `fois`, `de`, `re`, `fois|que`, `et`

byear:
- true `nou|vel|le` → beam: `fois`, `de`, `et`, `re`, `par`
- true `te|nue|le` → beam: `fois`, `de`, `et`, `re`, `par`
- true `pen|see|du` → beam: `fois`, `de`, `et`, `re`, `par`

("la première tenue" → the model offers `par|tie` ("partie") at beam#2 in
standard mode — the n-gram memory reaching for the right word through the
wrong segmentation.)

### Examples — "par ce que" (true next 3 cells vs model top-5 beam)

both modes:
- true `la|re|for|me` → beam: `les`, `la`, `nous`, `le`, `l`
- true `nous|a|vons` → beam: `les`, `la`, `nous`, `le`, `l`
- true `j|y|vois` → beam: `les`, `la`, `nous`, `le`, `l`

### "ne X" → "pas" frames (25 most frequent held-out bigrams; rank of "pas")

| mode | ne X | count | rank of "pas" |
|---|---|---|---|
| standard | ne\|ment | 1,249 | 69 |
| standard | ne\|ral | 513 | 63 |
| standard | ne\|ces | 469 | 145 |
| standard | ne\|se | 453 | 20 |
| standard | ne\|ra | 363 | 10 |
| standard | ne\|de | 330 | 14 |
| standard | ne\|a | 302 | 60 |
| standard | ne\|pou | 276 | 116 |
| standard | ne\|go | 237 | 135 |
| standard | ne\|s | 235 | 93 |
| standard | ne\|peut | 232 | **1** |
| standard | ne\|pas | 227 | 176 |
| standard | ne\|en | 216 | 102 |
| standard | ne\|re | 216 | 127 |
| standard | ne\|l | 194 | 120 |
| standard | ne\|le | 194 | 121 |
| standard | ne\|et | 159 | 108 |
| standard | ne\|raux | 159 | 128 |
| standard | ne\|sont | 149 | **1** |
| standard | ne\|con | 143 | 246 |
| standard | ne\|sau | 140 | 103 |
| standard | ne\|lui | 132 | 179 |
| standard | ne\|mens | 129 | 281 |
| standard | ne\|pour | 121 | 115 |
| standard | ne\|ments | 114 | 50 |
| byear | ne\|m | 1,538 | 55 |
| byear | ne\|de | 811 | 35 |
| byear | ne\|a | 586 | 66 |
| byear | ne\|et | 491 | 159 |
| byear | ne\|se | 488 | 24 |
| byear | ne\|ces | 473 | 147 |
| byear | ne\|pou | 354 | 126 |
| byear | ne\|en | 349 | 127 |
| byear | ne\|le | 308 | 67 |
| byear | ne\|s | 256 | 99 |
| byear | ne\|re | 249 | 140 |
| byear | ne\|l | 242 | 128 |
| byear | ne\|pas | 239 | 178 |
| byear | ne\|peut | 238 | **1** |
| byear | ne\|go | 237 | 133 |
| byear | ne\|son | 206 | **1** |
| byear | ne\|la | 176 | 41 |
| byear | ne\|d | 170 | 142 |
| byear | ne\|les | 152 | 97 |
| byear | ne\|par | 150 | 250 |
| byear | ne\|sau | 141 | 101 |
| byear | ne\|lui | 140 | 184 |
| byear | ne\|des | 139 | 111 |
| byear | ne\|e | 131 | 111 |
| byear | ne\|con | 127 | 282 |

**"pas" is generally NOT rankable from ("ne", X):** median rank ~115. The
("ne", X) bigram does not determine "pas" — "pas" follows the verb phrase,
1+ cells later, so a 2-cell context is the wrong window. The rank-1 hits
("ne peut" → "pas", "ne sont"/"ne son" → "pas") are the frozen collocations
where the verb is a single cell. Applier takeaway: do NOT use this model to
predict "pas" placement from "ne X"; the negation frame needs a wider
window than bigrams.

## C. Verb-stem inflection prediction (held-out)

Top-30 stems mined from TRAINING word counts; rank of the true cell
following each stem in held-out (≤600 occurrences/stem).

| stem | mode | cells | occ | top-1 | top-3 | top-5 | MRR |
|---|---|---|---|---|---|---|---|
| enco | standard | en\|co | 602 | 99.0% | 99.0% | 99.2% | 0.991 |
| not | standard | not | 42 | 78.6% | 78.6% | 81.0% | 0.794 |
| fai | standard | fai | 602 | 78.1% | 87.9% | 91.9% | 0.845 |
| quelqu | standard | quel\|qu | 42 | 73.8% | 100.0% | 100.0% | 0.845 |
| avo | standard | a\|vo | 90 | 67.8% | 80.0% | 90.0% | 0.760 |
| vot | standard | vot | 5 | 60.0% | 60.0% | 60.0% | 0.605 |
| éta | standard | e\|ta | 335 | 58.2% | 79.7% | 86.6% | 0.694 |
| cell | standard | cell | 2 | 50.0% | 50.0% | 50.0% | 0.501 |
| ser | standard | ser | 602 | 42.5% | 57.6% | 62.6% | 0.520 |
| port | standard | port | 134 | 34.3% | 53.7% | 54.5% | 0.452 |
| ent | standard | ent | 20 | 25.0% | 25.0% | 25.0% | 0.265 |
| ava | standard | a\|va | 58 | 20.7% | 29.3% | 55.2% | 0.320 |
| grand | standard | grand | 601 | 16.6% | 25.1% | 30.3% | 0.242 |
| tout | standard | tout | 602 | 15.9% | 36.0% | 46.7% | 0.298 |
| franc | standard | franc | 54 | 3.7% | 11.1% | 11.1% | 0.079 |
| cett | standard | cett | 1 | 0.0% | 0.0% | 0.0% | 0.111 |
| comm | standard | comm | 2 | 0.0% | 0.0% | 0.0% | 0.004 |
| aut | standard | aut | 3 | 0.0% | 0.0% | 0.0% | 0.009 |
| mond | standard | mond | 12 | 0.0% | 16.7% | 16.7% | 0.110 |
| cont | standard | cont | 1 | 0.0% | 0.0% | 0.0% | 0.021 |
| autr | standard | autr | 1 | 0.0% | 0.0% | 0.0% | 0.004 |
| ell | standard | ell | 1 | 0.0% | 0.0% | 0.0% | 0.077 |
| trouv | standard | trouv | 1 | 0.0% | 100.0% | 100.0% | 0.333 |
| dev | standard | dev | 1 | 0.0% | 0.0% | 0.0% | 0.067 |
| homm | byear | homm | 576 | 100.0% | 100.0% | 100.0% | 1.000 |
| comm | byear | comm | 602 | 99.7% | 99.7% | 99.7% | 0.997 |
| enco | byear | en\|co | 602 | 97.7% | 97.8% | 97.8% | 0.979 |
| fai | byear | fai | 602 | 78.4% | 88.2% | 91.9% | 0.847 |
| not | byear | not | 37 | 78.4% | 78.4% | 81.1% | 0.793 |
| quelqu | byear | quel\|qu | 42 | 73.8% | 100.0% | 100.0% | 0.845 |
| avo | byear | a\|vo | 90 | 67.8% | 76.7% | 86.7% | 0.746 |
| vot | byear | vot | 5 | 60.0% | 60.0% | 60.0% | 0.605 |
| éta | byear | e\|ta | 344 | 55.5% | 77.0% | 84.3% | 0.670 |
| cell | byear | cell | 2 | 50.0% | 50.0% | 50.0% | 0.500 |
| grand | byear | gran | 602 | 49.3% | 62.3% | 66.3% | 0.579 |
| ser | byear | ser | 602 | 43.9% | 58.8% | 63.5% | 0.532 |
| mond | byear | mon | 602 | 37.4% | 47.5% | 51.8% | 0.448 |
| port | byear | port | 134 | 35.1% | 53.7% | 54.5% | 0.456 |
| cont | byear | con | 603 | 35.0% | 53.1% | 59.5% | 0.467 |
| ava | byear | a\|va | 58 | 24.1% | 32.8% | 58.6% | 0.354 |
| ent | byear | en | 603 | 19.4% | 29.7% | 36.7% | 0.283 |
| donn | byear | don | 602 | 15.6% | 34.1% | 52.0% | 0.309 |
| tout | byear | tout | 602 | 15.4% | 35.7% | 46.8% | 0.295 |
| franc | byear | franc | 54 | 3.7% | 11.1% | 11.1% | 0.077 |
| cett | byear | cett | 1 | 0.0% | 100.0% | 100.0% | 0.500 |
| aut | byear | aut | 3 | 0.0% | 0.0% | 0.0% | 0.009 |
| autr | byear | autr | 1 | 0.0% | 0.0% | 0.0% | 0.004 |
| ell | byear | ell | 1 | 0.0% | 0.0% | 0.0% | 0.167 |
| trouv | byear | trouv | 1 | 0.0% | 0.0% | 100.0% | 0.250 |
| dev | byear | dev | 1 | 0.0% | 0.0% | 0.0% | 0.067 |

Notes:
- High-predictability stems ("enco"→"re" 99%, "fai"→"re/t" 78%,
  "not"→"re" 79%) are frozen collocations ("encore", "faire", "notre").
  The model is memorizing, not inflecting — the "verb stem" framing
  oversells it; several top stems are not verbs at all.
- The 0% rows are n≤3 occurrences — noise, not signal. Ignore them.
- **By-ear R3 conflation warning**: "cont"→`con` (603 occ in byear vs 1 in
  standard), "mond"→`mon` (602 vs 12), "grand"→`gran` (602 vs 601 as
  "grand"). R3's silent-t/d drop merges distinct stems into one cell
  ("con" covers contre/contrat/connaître…), which inflates occurrence
  counts and mixes conditionals. The byear verb-stem numbers for
  R3-affected stems measure the CONFLATED cell, not the stem.
- "donn" appears only in byear's list (standard has "donn…" presumably
  under a different mined stem) — the stem miner runs on raw words, so
  the two modes' stem lists differ slightly. Cross-mode stem comparisons
  are approximate.

## D. By-ear mismatch quantification (TRAIN)

- Word disagreement rate (200k-word sample, TRAIN[:4]): **11.1%** — the two
  segmenters agree on 89% of words; the fine cut is a perturbation, not a
  rewrite.
- Cells/word: standard **1.659**, byear **1.700** — byear is only 2.5%
  finer. (The original `mismatch_quant` divided by the 200k sample instead
  of all training words, reporting ~28; fixed 2026-10-07.)
- Vocab: standard 16,742, byear 16,754, **Jaccard 0.887**.
- Mode-exclusive cells: by-ear-only **1,006**, standard-only **994** —
  symmetric churn, mostly OCR-junk and rare R3/R4 products.

| banked cell | std rank (count) | byear rank (count) |
|---|---|---|
| la | 5 (79,722) | 6 (79,732) |
| pre | 57 (13,581) | 62 (13,514) |
| m | 71 (10,492) | **18** (39,762) |
| i | 82 (9,518) | **16** (42,764) |
| er | 731 (544) | **14** (48,759) |
| e | 9 (55,181) | **2** (130,524) |
| que | 10 (53,466) | 10 (53,472) |
| ce | 11 (52,965) | 11 (52,965) |
| qui | 28 (23,536) | 30 (23,571) |
| par | 27 (24,448) | 28 (24,375) |
| est | 34 (21,680) | 35 (21,680) |
| le | 3 (101,406) | 4 (101,311) |

**The by-ear segmentation promotes every crib cell into the top-20**:
"m" 71→18, "i" 82→16, "er" 731→14, "e" 9→2. In standard space "er" is
rank 731 (544 occurrences) — nearly invisible; in byear space it is rank
14 (48,759). This is the quantitative case for the `--byear` mode: the
clerk's cell inventory is frequent *in by-ear space*, so backoff has
something to grip. Stable function cells ("que", "ce", "qui", "par",
"est", "le", "la", "pre") barely move.

### Known by-ear divergences (by design, not bugs)

- `prend` → `pren` (R3: silent -d/-t dropped after nasal). The frenchman's
  ear reads `pre` — the model emits `pren`; the applier must map both.
  The banked cell `est` is exempted from R3.
- `-ment` → `m|ent` (attested 82-06), `-erre` → `er|e` (R4/R8), glide
  splits (`mienne` → `m|i|ne`), `-ne`/`-me` tails (`personne` →
  `per|so|ne`, `dame` → `dam|e`).
- R2 (inconsistent cutting) is NOT simulated: `byear_cut` is one
  deterministic canonical cut. The clerk is not deterministic; query both
  modes when a `--byear` context looks dead.
- R3 conflates stems (`cont`/`con`, `mond`/`mon`, `grand`/`gran`) — see
  section C.

## Corpus inventory

TRAIN (11 docs, French only; raw words counted pre-filter):

| file | bytes | raw words |
|---|---|---|
| guizot-memoires-t1-gutenberg.txt | 805,355 | 121,572 |
| guizot-memoires-t3-gutenberg.txt | 892,268 | 132,604 |
| guizot-memoires-t5-t6.txt | 2,043,767 | 277,393 |
| nesselrode-v7.txt | 533,520 | 74,138 |
| nesselrode-v8.txt | 627,848 | 86,825 |
| nesselrode-v9.txt | 515,743 | 80,393 |
| nesselrode-v10.txt | 569,508 | 77,591 |
| pozzo-di-borgo-correspondance-v1.txt | 1,029,046 | 137,597 |
| revue-deux-mondes-1841-q1.txt | 3,087,127 | 425,374 |
| revue-deux-mondes-1841-q2.txt | 3,037,263 | 415,805 |
| revue-deux-mondes-1841-q3.txt | 3,129,322 | 429,585 |
| **train total** | **~15.6 MB** | **~2.16 M** |

Segmented: standard **4,037,445** cells, byear **4,136,570** cells.
Kept n-grams (orders 2–6, ord≥3 iff count≥2): standard **1,561,980**,
byear **1,589,159**. Unigrams: 16,742 / 16,754. DB 1,001 MB.

HELD-OUT (3 whole documents, never trained on):

| file | bytes | raw words |
|---|---|---|
| guizot-memoires-t2-gutenberg.txt | 869,256 | 130,883 |
| revue-deux-mondes-1841-q4.txt | 3,244,434 | 441,394 |
| talleyrand-memoires-v1.txt | 954,364 | 146,148 |
| **held-out total** | **~5.1 MB** | **~718 k** |

EXCLUDED from both (per the language audit in `build.py`): the 15
Allgemeine-Zeitung January-1841 issues (German, Fraktur OCR), the ADB
Zeschau entry, the 2 Metternich volumes (Fraktur OCR + German editorial),
and the mixed English/French Levant volume. Rationale: the cipher is
French diplomatic prose; German OCR noise would pollute the cell
inventory. Trade-off (see weaknesses): German proper nouns in the French
text are learned only insofar as French authors wrote them.

## Smoke tests (exact CLI contract, 2026-10-08)

All four README contract queries return non-empty, sane rankings
(~4–7 s/query on the 1 GB DB):

```
$ python3 predict.py --context "pre m i er e" --k 5 --byear
[{"syllables": ["fois"], "prob": 0.1669},
 {"syllables": ["de"], "prob": 0.0477},
 {"syllables": ["et"], "prob": 0.0424},
 {"syllables": ["re"], "prob": 0.0397},
 {"syllables": ["par"], "prob": 0.0358}]

$ python3 predict.py --byear --context "la pre m i er e" --k 5
(same as above — only the last 5 cells are used: pre|m|i|er|e;
 top continuation "fois" = "la première fois")

$ python3 predict.py --context "par ce" --k 5
[{"syllables": ["qu"], "prob": 0.4630},
 {"syllables": ["que"], "prob": 0.3958},
 {"syllables": ["qu", "il"], "prob": 0.1941},
 {"syllables": ["qu", "el"], "prob": 0.1099},
 {"syllables": ["qu", "el", "le"], "prob": 0.0865}]
("par|ce" + "qu…" = "parce que…" via the elision split)

$ python3 predict.py --byear --words --context "par ce que" --k 5 --maxlen 2
[{"syllables": ["les"], "prob": 0.1271},
 {"syllables": ["la"], "prob": 0.1204},
 {"syllables": ["nous"], "prob": 0.0836},
 {"syllables": ["le"], "prob": 0.0803},
 {"syllables": ["l"], "prob": 0.0669}]
(--words segments the context for you; all candidates ≤2 cells)
```

## Honest weaknesses

1. **Stupid backoff, no real smoothing**: unseen contexts collapse to
   0.4⁵-scaled unigrams. The model is confident about frequent n-grams
   and vague everywhere else; there is no Kneser-Ney-style handling of
   novel contexts.
2. **No word-boundary or sentence markers**: the stream is flat cells, so
   the model cannot learn word-initial vs word-internal distributions —
   deliberate (the cipher is a continuous pair stream), but it costs
   accuracy at word onsets.
3. **OCR noise in TRAIN**: archive.org `_djvu.txt` OCR (especially the
   Revue des Deux Mondes scans) injects garbage cells into the vocab;
   tokens >30 chars and digit-tokens are dropped, but mid-word OCR errors
   survive as rare cells (~1k mode-exclusive cells each way).
4. **By-ear mode is a single canonical cut** (R2 not simulated); the
   clerk's inconsistency means some true contexts will miss in both modes.
   R3 additionally conflates distinct stems (`con`, `mon`, `gran`).
5. **Whole-document holdout is only 3 documents**, one of them
   author-heavy (Talleyrand) and one a periodical (RdM q4); genre shift
   (memoirs vs correspondence vs periodical) is only partially covered.
6. **Never tested against the cipher stream** — all numbers above are
   French-text next-cell ranks, not group-mapping accuracy. Calibrate
   mapping thresholds on the banked cribs, not on these probs.
7. `prob` is a joint stupid-backoff score, NOT renormalized over the
   returned set; do not compare raw probs across contexts or modes.
8. **The by-context-length breakdown is uninformative** (all samples had
   the full 5-cell context); backoff degradation at short contexts is
   unmeasured.
9. **"pas" placement is not predictable from ("ne", X) bigrams**
   (median rank ~115); the negation frame needs a wider window.
10. **Verb-stem section oversells**: top "stems" include non-verbs
    ("encore", "notre", "quelque"); high scores are frozen collocations,
    not inflectional generalization. Rows with n≤3 are noise.
11. **Latency**: ~4–9 s per query on the 1 GB DB (beam search sorts the
    full 16.7k distribution per expansion). Fine for interactive applier
    use, too slow for bulk scoring without batching.
12. **Compute cost of calibration**: ~3 h wall-clock under contention,
    dominated by per-occurrence full-distribution scoring; checkpointed
    per phrase/section in `calibrate_checkpoint.json` so reruns resume.

## Reproduction

- Build: `python3 build.py` (~18 min; resumable via `models/.build-tmp/stage.db`).
- Calibrate: `python3 calibrate.py > calibrate.json` (~1–3 h depending on
  machine contention; resumable via `calibrate_checkpoint.json`).
- Tables: `python3 render_calibration.py` renders `calibrate.json` →
  markdown tables (stdout).
- Raw numbers: `calibrate.json` (this run); checkpoint:
  `calibrate_checkpoint.json`.
- DB: `models/seebach_nexttoken.db` (SQLite, read-only queries),
  `built_utc=2026-10-08T01:32:26Z`.
