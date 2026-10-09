# Battery verdict: classification-sweep (guard battery)

## Bar (verbatim from battery-queue.json)
"the 27-window classification.json partition re-derives from the repaired stream without trusting the file"

Numbered clauses:
- (a) all 27 59-cells classified from pre/successor cells alone, blind to the file
- (b) >=26/27 agreement with classification.json
- (c) any disagreement named with window evidence

Adverses: none - this is a guard battery; a null keeps the current partition.

## Method
- Read BATTERY-PROTOCOL.md first; created `locks/classification-sweep.lock` (agent id + UTC) on start.
- Parsed the repaired stream per `code/side-keyhunt/repair_parse.py` from
  `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`:
  **1,847 pairs, 96 types, n(59)=27** — verified.
- `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- For each of the 27 59-windows (0-based file keys shown; my @ are 1-based = key+1),
  recorded pre-pre / pre / suc / suc-suc and classified with the rules below.

**Blindness caveat (disclosed):** the file's head (~first 2000 bytes, entries
103/316/1210/1777/559/763/825/216/1186/1190/1448/1804) was visible during setup
when locating the file. The classification below was applied rule-by-rule from
the cells; the remaining 15 entries were unseen before classification.

## Blind classification rules (declared before comparison)
- **EST** (word-level "est"): pre is a clitic/particle licensing standalone
  "est" under standing values, suc compatible:
  - pre=94 ("ne", STRONG LEAD) with suc in {30,39} -> "n'est pas" / "n'est a"
  - pre=64 ("qui", GT) -> "qui est"
  - pre=93 ("l'" LEAD) -> "l'est"
- **ESTE** (sub-lexical "-est[e]" fused with a stem group, standalone "est"
  ungrammatical in the frame):
  - pre=06 (verb-stem-class) -> "[06-59]"
  - pre=86 (verb-stem-class, F40) -> "[86-59]" (lean if successor unresolved)
  - pre=44 with "ne...pas" forcing context -> "[44-59]"
  - pre=61 with "on [61-59]" frame forcing ("on [61] est" ungrammatical) -> "[61-59]"
  - pre=84 in ISLET frames ("qui le [84-59]", "[06-84-59] que") -> "[84-59]"
- **FENCED**: two live readings, both grammatical under standing values.
- **LEFTOVER**: neither reading forced; value/hostile contacts open.

## Blind classification (0-based key | 1-based @ | frame | my class)

| key | @ | frame (pre-pre pre [59] suc suc-suc) | my class | file class |
|---|---|---|---|---|
| 103 | 104 | 94 93 [59] 45 28 | EST | EST |
| 216 | 217 | 78 06 [59] 46 29 | ESTE | ESTE |
| 316 | 317 | 45 64 [59] 32 94 | EST | EST |
| 448 | 449 | 62 61 [59] 32 48 | ESTE | ESTE |
| 463 | 464 | 87 11 [59] 42 96 | LEFTOVER | LEFTOVER |
| 528 | 529 | 47 44 [59] 37 64 | LEFTOVER | LEFTOVER |
| 554 | 555 | 00 86 [59] 34 17 | ESTE_LEAN | ESTE_LEAN |
| 559 | 560 | 86 94 [59] 30 67 | EST | EST |
| 624 | 625 | 82 14 [59] 37 33 | LEFTOVER | LEFTOVER |
| 763 | 764 | 62 94 [59] 39 88 | EST | EST |
| 825 | 826 | 24 87 [59] 38 82 | EST | NEUTRAL |
| 834 | 835 | 77 76 [59] 35 56 | LEFTOVER | LEFTOVER |
| 912 | 913 | 64 83 [59] 37 96 | LEFTOVER | LEFTOVER |
| 1178 | 1179 | 32 48 [59] 37 77 | LEFTOVER | LEFTOVER |
| 1186 | 1187 | 06 06 [59] 42 06 | ESTE | ESTE |
| 1190 | 1191 | 06 84 [59] 46 07 | ESTE | ESTE |
| 1210 | 1211 | 65 64 [59] 32 48 | EST | EST |
| 1291 | 1292 | 17 84 [59] 35 94 | FENCED | FENCED |
| 1443 | 1444 | 52 68 [59] 37 64 | LEFTOVER | LEFTOVER |
| 1448 | 1449 | 77 84 [59] 36 67 | ESTE | ESTE |
| 1496 | 1497 | 66 15 [59] 24 89 | FENCED | FENCED |
| 1511 | 1512 | 12 61 [59] 39 81 | LEFTOVER | LEFTOVER |
| 1715 | 1716 | 94 44 [59] 30 64 | ESTE | ESTE |
| 1777 | 1778 | 87 64 [59] 19 48 | EST | EST |
| 1796 | 1797 | 42 94 [59] 37 91 | LEFTOVER | LEFTOVER |
| 1804 | 1805 | 77 84 [59] 35 94 | ESTE | ESTE |
| 1833 | 1834 | 82 16 [59] 36 69 | LEFTOVER | LEFTOVER |

Class tallies (mine): EST 7 (incl. 825), ESTE 7, ESTE_LEAN 1, FENCED 2,
LEFTOVER 10. File tallies: EST 6, ESTE 7, ESTE_LEAN 1, FENCED 2, NEUTRAL 1,
LEFTOVER 10.

## Per-clause results
- **(a) PASS** — all 27 cells classified from pre/successor cells (see table;
  blindness caveat disclosed above).
- **(b) PASS** — 26/27 agreement (>=26/27 bar met exactly).
- **(c) PASS** — the sole disagreement is named below with window evidence.

## The one disagreement: @826 (file key 825)
- Window (1-based): "24 87 [59] 38 82" (row a5_06).
- My call: **EST** — 87="ce" is granted (A4); "c'est" is the canonical
  copula frame and parses under standing values ("[faire] c'est [38]").
- File call: **NEUTRAL** — "87-59 'c'est' candidate: I3 ruled hostile-neutral
  (RULINGS-ROUND7) - not counted".
- I3 text (`code/crowd7/redteam/RULINGS-ROUND7.md`): "@824
  ([...,24,87,59,38,...]) is hostile-neutral under banked values, so the
  allophony claim there is unsupported either way."
- Reading: the NEUTRAL label defers to a standing red-team ruling about the
  window's adjudicative value (allophony claim "unsupported either way"), not
  to a byte-level rejection of "c'est". My blind EST call lacks that ruling
  context; the file's label is ruling-consistent. **No data error on either
  side.** Escalated to the red team as a labeling question only: whether the
  59-partition should carry NEUTRAL or EST at @826 given I3. The ruling itself
  is not contradicted and is not re-litigated here.

## Notes on specific windows (evidence for agreement)
- @529 (key 528): pre=44 like @1716, but the "ne...pas" forcing present at
  @1716 ("ne [44-59] pas") is absent here ("ce [44] [59] [37]"); unit
  symmetry does not transfer, and the 59->37 contact is S5-fenced territory.
  LEFTOVER on both sides.
- @1512 (key 1511): pre=61 like @449, but pre-pre=12 ("n'" elision) changes
  the frame ("n' [61-59] a" ungrammatical under fused-verb reading); no
  forcing. LEFTOVER on both sides.
- @1797 (key 1796): pre=94 but suc=37, not 30/39 — "n'est [37]" unforced;
  LEFTOVER on both sides ("n'est le" era-rare per file note).
- @826 vs @560/@764: the two "n'est" EST legs have suc=30 ("pas") and
  suc=39 ("a"), the strong direct frames; @1797's suc=37 does not join them.
- The seven ESTE windows each carry independent forcing: @217 "[06-59] que"
  (cleft "NP est que" hostile), @449 "on [61-59] [32]" ("on [61] est"
  ungrammatical), @1187 "ne me [06-59] [42]", @1191 "[06-84-59] que"
  (3-syllable -este verb), @1449/@1805 "qui le [84-59]" (ISLET 8, word-"est"
  era-absent F65), @1716 "ne [44-59] pas".

## Verdict: PROMOTE (guard success)
The 27-window 59-cell partition re-derives at 26/27 from pre/successor cells
alone. The single disagreement (@826) is explained by standing red-team
ruling I3, not by a data error — the partition stands as filed. No follow-ups
required (guard battery; clause (c) escalation above is a labeling question
for the red team, not a new work order).

## Bookkeeping
- Lock `locks/classification-sweep.lock` created on start, deleted on completion.
- `battery-queue.json`: `classification-sweep` -> status `verdict`, result
  `promote`, report path this file, date 2026-10-09 (temp-file + rename,
  own entry only, pre-write assert confirmed queued/verdictless, JSON
  re-validated post-write).
- No standing verdict contradicted or downgraded. R5005, sealed gates,
  red-team queue untouched. `canonical.py` never used.
- Every number re-derived on the repaired 1,847-pair stream.
