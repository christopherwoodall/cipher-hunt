# Battery report: seg-41-08-leftedge

- Target id: `seg-41-08-leftedge`
- Verdict: **NULL** (fence executed)
- Date: 2026-10-09

## Bar (verbatim, pre-registered)

`resolve iff "41 08 ..." parses with <=1 new assumption (moves 08 off word-initial position and re-opens @60-67 segmentation); else fence @59 as residual`

Numbered clauses:

- **C1 (resolve arm):** "41 08 ..." parses with ≤1 new assumption → resolve (name 41 class/value at @59; 08 moves off word-initial position; @60–67 segmentation re-opens).
- **C2 (fence arm):** else → fence @59 as residual.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed per `code/side-keyhunt/repair_parse.py`). Asserts held: 1,847 pairs,
96 types. `canonical.py` never used.

Locus byte-confirmed (0-based, row a1_01):

| @ | group | standing |
|---|-------|----------|
| 57 | 53 | open |
| 58 | 12 | 'n' (promoted spelling letter) |
| 59 | 41 | open (§7 split candidate; no class, no value) |
| 60 | 08 | word-internal promoted, value open (N189; parent seg-08-ier-61) |
| 61 | 34 | 'i' (GT) |
| 62 | 29 | 'er' (GT) |
| 63 | 40 | 'e' (GT) |
| 64 | 12 | 'n' (promoted spelling letter) |
| 65 | 94 | 'ne' (strong lead) |
| 66 | 92 | verb (class-level) |
| 67 | 69 | open |

Registry check (`code/table-grid/table-registry.json`): **41 and 08 are both
absent** — neither banked, promoted, provisional, nor class-level. 41 is a §7
split candidate (no uniform class across standing-value contacts; split decision
pending at the red team, R20-108/R20-082). 08's value stays open (N189 killed
the 08="on" homophony; the parent battery promoted 08 word-internal with the
value unnamed).

"41 08" is a stream hapax (@59–60); "08 34" is also a hapax (@60–61).

## Window-level evidence

The claim is that "41 08" forms a word-initial unit, i.e. one word whose onset
is [41][08] and which 08 is word-internal to (the bar's parenthetical: 08 moves
off word-initial position).

The word would be `[41][08]ière`: 34='i' + 29='er' + 40='e' = "ière" (GT bytes,
fixed order). French two-letter-onset + "ière" words: première, dernière,
entière, lumière, manière, rivière, poussière, … — every candidate requires
**naming 41's letter AND naming 08's letter**.

Assumption budget:

- 41's letter content: not standing (registry-absent, split candidate). = 1 new assumption.
- 08's letter content: not standing (N189 value-open; parent promoted word-internal unnamed). = 1 new assumption.
- Minimum total: **2 new assumptions** for any concrete word-initial-unit parse.

The bar allows ≤1. No alternative parse reduces the count: 41-as-whole-word
(e.g. "une") would make "41 08" two words and leave 08 word-initial,
contradicting the bar's own parenthetical; 41-as-letter-with-unnamed-08 still
spends both assumptions the moment a word is named. Phonotactics alone does not
fix either letter (many onsets fit "…ière").

Note the parent battery (seg-08-ier-61, NULL 2026-10-09) already swept @60–67
exhaustively and fenced it as multi-residual, promoting 08 word-internal with
value unnamed; this target's resolve arm would have re-opened that fence, but
the budget blocks it.

### Per-clause results

- **C1: FAIL** — no parse of "41 08 ..." as a word-initial unit exists with ≤1
  new assumption (2 required minimum: 41's letter + 08's letter, both
  registry-open). The failure is structural (assumption budget), not a
  kill-grade falsification of 41's nature.
- **C2: FIRES** — @59 fenced as residual. The fence covers the word-initial-unit
  claim at this locus only; it does not decide 41's class/value (split venue
  stays with the red team) or 08's value.

## Scope

Locus-only fence. Untouched: 41's §7 split (red-team venue), 08's value,
the parent's @60–67 multi-residual fence, and the "53 12 41" left-edge geometry.
No standing/red-team verdict contradicted or downgraded; §7 intact. Canonicality
caveat stands (row a1_01 offset unvalidated). No adverses listed.

## Follow-ups proposed (all verified ABSENT from queue; supervisor to queue)

1. `val-41-letter-census` (P3) — census 41's 19 windows for letter-cell vs
   word-cell behavior; a letter-cell 41 re-opens the onset arm with one fewer
   assumption.
2. `val-08-letter-census` (P3) — census 08's 18 windows for a uniform letter
   value (lead with the 'h'/'f'/'b' candidates from seg-08-ier-61); a named 08
   reduces the "41 08" onset budget to 1 assumption and re-opens this target.
3. `seg-53-12-41-58` (P4) — test whether @57–59 ("53 12 41") forms a word-final
   unit ("[53]n[41]"); if 41 is word-final there, the word-initial-unit claim at
   @59–60 dies at kill grade.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-41-08-leftedge.md` (this file).
- Queue: `seg-41-08-leftedge` → `status: verdict`, `result: null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  disk re-read confirms verdict/null; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/seg-41-08-leftedge.lock`: created on start,
  deleted on completion. R5005, sealed gates, red-team adjudication queue
  untouched.
