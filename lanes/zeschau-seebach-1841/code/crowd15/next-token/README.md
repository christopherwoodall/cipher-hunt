# Next-token predictor — Seebach R5005 lane

Syllable-level P(next cell(s) | context) trained on the 1840s French
diplomatic corpus, for the applier agent that maps predicted syllables to
cipher groups. Two segmentations (see `CALIBRATION.md` for numbers):

- **standard**: the lane syllabifier `code/side-period/syllabify.py`
  (maximal-onset French syllabification), accents stripped from cells.
- **by-ear** (`--byear`): `byear.py`, a deterministic fine-cut variant
  reproducing the clerk's attested habits from
  `code/sidepath/phonetic_rules.md`:
  `première` → `pre|m|i|er|e` (crib-exact), `erre` → `er|e`,
  `personne` → `per|so|ne`, `-ment` → `m|ent`, `prend` → `pren`
  (silent -d/-t after nasal; the frenchman's ear reads `pre` — known
  divergence, documented), glide splits (`mienne` → `m|i|ne`),
  mute `-e` handling (`dame` → `dam|e`, `-re` → `er|e`).

## CLI contract

```
predict.py --context "syll1 syll2 ..." --k 10 [--byear] [--words]
           [--beam 60] [--maxlen 3] [--db PATH]
```

- `--context`: space-separated syllable cells in the model's segmentation.
  Only the last 5 cells are used (model order 6). With `--words`, the
  context is segmented as French words instead.
- `--k`: candidates returned (default 10). `--byear`: by-ear model.
- `--beam`: beam width (default 60). `--maxlen`: 1..3 syllables per
  candidate (default 3).
- Output: JSON array `[{"syllables": [...], "prob": float}]`, prob
  descending. `prob` = model joint probability P(s1..sm | context)
  under stupid backoff — a ranking score, NOT renormalized over the
  returned set (beam truncates the tail).

Examples:

```bash
# standard: what follows "par ce" ?
python3 predict.py --context "par ce" --k 5
# by-ear: what follows the crib cut "la pre m i er e" ?
python3 predict.py --byear --context "la pre m i er e" --k 5
# word input, by-ear:
python3 predict.py --byear --words --context "par ce que" --k 5 --maxlen 2
```

## Model

- Stupid backoff (weight 0.4), orders 1..6, over syllable cells.
  Pruning: all 1/2-grams kept; orders ≥3 kept iff count ≥ 2.
- Training: 11 whole French documents (~2.5M words); held-out: 3 whole
  documents (guizot-t2, RdM-q4, talleyrand-v1) — see `CALIBRATION.md`.
- DB: `models/seebach_nexttoken.db` (SQLite, read-only queries).
  Rebuild: `python3 build.py` (~15-25 min; corpus paths in `build.py`).

## Files

- `byear.py` — by-ear fine-cut segmenter (the by-ear rules live here).
- `tokenize.py` — text → cell streams (elision/hyphen handling, filters).
- `build.py` — corpus → SQLite n-gram DB.
- `predict.py` — the CLI.
- `calibrate.py` — held-out evaluation → JSON on stdout.
- `CALIBRATION.md` — calibration numbers, corpus inventory, by-ear
  mismatch quantification, known weaknesses.
- `models/seebach_nexttoken.db` — the built model.

## For the applier

- Query in the SAME segmentation as the model mode: standard cells for
  the default model (`la pre mie re`), clerk-style cells with `--byear`
  (`la pre m i er e`). `--words` does the segmentation for you.
- The clerk cuts inconsistently (R2): if a `--byear` query looks dead,
  retry the same context in standard mode (and vice versa).
- Candidates are 1-3 cells long; filter by length if you need exactly the
  next cipher group (1 cell) vs the next word (1-3 cells).
- `prob` values are comparable within one query (ranking); do not compare
  raw probs across different contexts or modes.
- Never tested against the cipher stream — calibrate your group-mapping
  thresholds on the banked cribs, not on these probs.
