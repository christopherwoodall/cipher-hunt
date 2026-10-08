# Missing-mass inventory — analysis (round 13, council WO-6)

## Headline

**The missing mass is NOT in second cells for identified syllables. It is in
first cells for uncovered syllables.** No identified syllable clears the
pre-registered FLAG bar (deficit ≥ 19.2 occ AND z < −2), on the 14-file
diplomatic mix or on genre-matched Nesselrode v8. The 1690 homophone budget is
concentrated in the uncovered vocabulary — de, en, ne, les, te, et, ou, tion —
not in la/que/ce.

## The deficit table (pre-registered method; `DEFICIT.md`, `deficit_table.json`)

Stream: repaired 1,847 pairs, 96 groups, mean cell rate 19.24.
Corpus: 14 French files, 3,210,279 words, 6,597,106 syllables (lane syllabifier
from `code/side-keyhunt/build_syll_model.py` — reused, not hand-rolled).

- 11 STRONG deficits, all in syllables with **zero** identified coverage:
  u (3.0 cells), de (2.9), a (2.8), qu (2.5), re (1.5), en (1.3), et (1.3),
  ti (1.3), ne (1.2), les (1.1), te (1.1).
- All 9 syllabic identified values: ok or surplus. la 45 vs 30.4 expected;
  le 44 vs 40.0; que 29 vs 11.7; ce 32 vs 19.0; qui 47 vs 8.3; par 21 vs 9.1;
  est 27 vs 7.7; pre 15 vs 1.8; er 45 vs 5.3.
- Aggregate: identified cells carry 20.4% of stream traffic vs 7.0% era budget
  for their syllables (2.9× hot). The despatch is function-word dense vs the
  corpus, or the cipher's cells are coarser than the comparators, or both.

## Corrections and sensitivity (post-registration, clearly labeled)

1. **Fragment re-bundling.** The lane syllabifier fragments coarse cipher units:
   que→qu+e, qui→qu+i, ou→o+u, tion→ti+on. ~58% of the "qu" deficit (47.7 occ)
   is que/qui/qu' already covered by 46/64 → qu-remainder ≈ 20 occ (1.0 cell).
   "re" is covered by 29's coarse {er,re,é} bundle (v8: +7.8 occ, z=−1.08,
   balanced). "i"/"e" syllables (2.7%/2.6%) are fragment hubs (qui→i, que→e,
   lui, roi, -ue words) in the by-ear-spelling domain — comparator unresolved,
   excluded from mass accounting.
2. **Nesselrode v8 genre check** (`v8_counts.json`, `v8_deficit.json`; v8 =
   92,594 words of actual 1840–46 diplomatic letters). Same pattern: no
   identified syllable flags. Notable: 29={er,re,é} balances on v8; 46=que
   balances on v8 (−2.1 occ, z=+0.40); 87={ce,se} near-misses (+12.0, z=−1.83,
   does NOT clear the bar — the only identified-syllable positive deficit).
3. **Corrected missing-mass aggregate:** naive 385.6 occ → 20.0 cells;
   fragment-corrected ≈ 330 occ → **~17 cells** (range 17–20). Sub-threshold:
   on (0.9), des (0.7), ou/nous/vous-words (~1) → total expected first-cells
   ≈ 19–22 among the 84 unidentified groups.

## What this means for the 1690 order (§d)

Prediction 2 ("no un-split giants") is INVERTED by the data: the identified
syllables show no giants needing splits — the giants are the UNCOVERED
syllables (de alone wants ~3 cells). The homophone budget, if the 1690 order
holds, is spent on de/en/ne/les/te/et/ou/tion — i.e., the unidentified groups
are mostly FIRST cells for frequent syllables, with a smaller homophone
tail. The per-syllable cell counts in the table (de 2.9, en 1.3, ne 1.2…)
are the quantitative form of "which unidentified groups must be homophones
by elimination."

## Tensions the council must adjudicate

1. **P1c conflicts (§C of CANDIDATES.md):** 48 (ne) and 52 (est) are P1 on
   contact but their syllables' era budgets don't need second cells (94 alone
   1.55× ne budget; 59 alone 2–3.5× est budget). Three live resolutions:
   wrong known-cell value, despatch-density, or broader coarse class. The
   47/87 positional-allophone precedent suggests testing complementary
   distribution before free homophony.
2. **{33,86} phase discrepancy** (CANDIDATES.md §B): reconstructor's B,B vs
   lane maps' A,B → demoted to WATCH; {76,78} becomes strongest surviving set.
3. **00 anomaly:** 00 (n=55, pour-LEAD) is 9× the era "pour" word budget
   (5.9 occ). Either extreme despatch concentration or 00's class is broader
   than "pour" (pour+par+pas? p-initial bundles?). Flagged for the 00 lane.
4. **24 anomaly:** 24 (n=52, "en"-local) is 2× the en budget — same tension
   shape as §C.

## Methodological caveat (carried, not hidden)

The z-scores treat the despatch as a random sample of era French; it is a
single topic-concentrated text, so exact z-values overstate confidence. The
v8 sensitivity reproduces the DIRECTION (uncovered ≫ identified), which is
what the council conclusions rest on — not the exact z-values.

## Files

- `PREREG.md` — pre-registration (thresholds fixed before computation)
- `missing_mass.py` — main script (stream, corpus, deficit table, candidates, digits)
- `analysis2.py` — v8 sensitivity, coarse bundles, §b validation, centroid ranking
- `corpus_counts.json` / `v8_counts.json` — cached corpus counts
- `deficit_table.json` / `DEFICIT.md` — the per-syllable table
- `v8_deficit.json` — genre-matched variant
- `set_validation.json` — independent §b re-verification
- `ne_candidates.json` / `fw_centroid_ranking.json` — ranked priors
- `CANDIDATES.md` — ranked candidate lists with evidence grades
- `digit_hunt.json` / `DIGITS.md` — digit hunt (verdict: negative, see below)

## Digit-hunt verdict: NEGATIVE (falsifier fired)

The 8 groups with n<5 (04, 22, 27, 54, 57, 90, 95, 99 — all phase R, the
residual/outlier bin, as the reconstructor's R-note predicts for rare-use
cells):
- T1 (digit-digit adjacency): 0 observed vs null mean 0.10 / max 2 — no
  clustering signal either way (power ~nil at n=1–3; uninformative, not
  exculpatory).
- T2/T4 (contact with top-20 core; syllable-like profiles — the falsifier):
  **FIRED.** 95 sits between 11=la/40=e and 46=que — a grammatical frame slot,
  not a digit. 22 touches 64=qui; 27 feeds 46=que; 57 feeds 64=qui; 54 touches
  64=qui; 04 touches 62="on"-fenced. These are hapax-vocabulary cells embedded
  in grammar, not isolated digit cells.
- T3 (date-position clustering): 2/15 occurrences in stream edges (04@1809,
  22@1837) — chance-consistent, no date clustering.
- Residual thread (not a finding): 27 and 90 share predecessor 60
  (60→27→46, 60→90→19); 60 (n=18) unidentified — worth one look by the
  60-lane, nothing more.
**Recommendation: retire the digit hunt.** Reclassify the 8 as rare-vocabulary
cells. If the despatch carries dates, they are likelier spelled out
("dix-huit janvier") than digit-encoded — and no digit-shaped evidence
survived the falsifier.
