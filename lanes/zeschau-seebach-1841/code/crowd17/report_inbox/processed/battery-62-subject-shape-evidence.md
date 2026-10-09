# Battery `62-subject-shape-evidence` — verdict: NULL (fence executed)

RED-TEAM INPUT. Evidence only for the redteam-62-split docket. No class, split,
value, or polyvalence is declared or named in this report (§7).

## Bar (verbatim, pre-registered)

"every window fits subject+'ne' with zero ungranted assumptions besides 62's
class, else the shape is fenced as distributional-only."

Numbered clauses:
- C1: every one of the 9 '62 94' windows fits subject+'ne' with zero ungranted
  assumptions besides 62's class (62 and 94 in the same clause, no boundary
  between them, a granted finite verb in 94's "ne"-scope, no granted value
  contradicting).
- C2 (else): fence the '62 94' = subject+'ne' shape as distributional-only.

## Method

Repaired 1,847-pair / 96-type stream re-derived in session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via
`repair_parse.py` (asserts held: 1847 pairs, 96 types). `canonical.py` never
used. Byte-exact census: '62 94' occurs exactly 9 times stream-wide.

Standing premises adopted (not re-litigated): 94="ne" single value (R19-167/
168 closed; 67 is the sole polyvalence); 59=est provisional finite; 24
finite/modal per R24 unless follower=85 (then "en"); 56 promoted finite;
64=qui; 46=que; 87=ce; 79=tout (A5); 77=le provisional; 70=pre (GT syllable);
06="ent" (R17-007 conditional). 62's class/value was NOT named (§7; 62="il"
killed in R19).

Per-window scope audit: for each 94, the next granted-finite verb and the next
clause-boundary marker (46=que, 64=qui) were located; a "ne"-scope is bounded
by the next 46/64 or the next 94 (two "ne"s = two clauses).

## Window-level evidence (±3 context byte-exact; 0-based @ of 62)

| # | @ | row | ±3 | 94-scope: next granted finite / bound |
|---|---|-----|----|----------------------------------------|
| W1 | 100 | a1_02 | 85 08 21 [62 94] 93 59 45 | 59=est @103 / 46 @107 |
| W2 | 508 | a3_00 | 21 67 77 [62 94] 64 98 65 | 56 @514 / 64=qui @510 (immediate) |
| W3 | 761 | a5_03 | 29 40 20 [62 94] 59 39 88 | 59=est @763 (adjacent) / none |
| W4 | 840 | a5_06 | 17 98 20 [62 94] 26 12 16 | none in 15 / 64 @854 |
| W5 | 1329 | a7_04 | 56 30 06 [62 94] 70 52 39 | none in 15 / 64 @1337 |
| W6 | 1362 | a7_06 | 35 13 92 [62 94] 79 14 60 | none in 15 / none |
| W7 | 1686 | a8_05 | 65 13 93 [62 94] 79 14 60 | none (24@1693 = "en", after 46 @1692) |
| W8 | 1704 | a8_06 | 94 30 20 [62 94] 88 26 12 | none before 2nd 94 @1713 / 64 @1717 |
| W9 | 1772 | a8_09 | 26 37 78 [62 94] 24 87 64 | 24 fin/modal @1774 (R24) / 64 @1776 |

## Per-window fit assessment

- **W1 @100 — FITS.** 62 and 94 sit inside the 46@95 que-clause; no boundary
  between them. Granted finite 59=est @103 in 94's scope ("ne [93] est"):
  whether 93 is the negated verb (then "est ce" opens the next clause) or a
  non-finite intervener (then est is the verb), the subject+ne shape holds with
  no ungranted assumption beyond 62's class. Full clause parse not demonstrated
  (not required by the bar).
- **W2 @508 — FAILS (hostile).** 94 is immediately followed by granted
  64=qui: "[62] ne qui [98]..." A relative pronoun cannot intervene between
  "ne" and its verb, so 94's "ne" cannot head a clause with 62 as subject.
  Additionally 77=le (provisional) immediately precedes 62, licensing the
  "le [62]" determiner+noun reading — a clause boundary plausibly falls between
  62 and 94. Granted values contradict the subject+ne shape here.
- **W3 @761 — FITS.** 59=est @763 adjacent to 94: "[62] ne est [39] [88]"
  ("ne est à ..."). No boundary between 62 and 94 (64 @749 is 12 cells back).
  Granted values only.
- **W4 @840 — FAILS (indeterminate).** 94's scope ("ne [26] [12] [16] pour
  [33] par ...", bounded by 64 @854) contains no granted finite verb. Naming
  the negated verb requires valuing unvalued cells — an ungranted assumption.
- **W5 @1329 — FAILS (indeterminate).** 94 followed by 70='pre' (GT syllable):
  the negated verb is the unvalued 'pre'-led word; no granted finite verb in
  scope (bounded by 64 @1337). Naming it finite is an ungranted assumption.
- **W6 @1362 — FAILS (indeterminate).** "ne tout [14] [60]..." — 94's scope
  has no granted finite verb within 15 cells (98 is verb-class, finiteness
  unresolved). 62/94 share the qui-relative clause (64 @1358), but the verb
  is unvalued.
- **W7 @1686 — FAILS (indeterminate).** 94's scope ("ne tout [14] [60] [27]",
  bounded by 46 @1692) has no granted finite verb; 24 @1693 is "en" (follower
  85, R24) and lies past the boundary.
- **W8 @1704 — FAILS (indeterminate).** A second 94 @1713 ("ne [44] est")
  bounds the first 94's scope: "ne [88] [26] [12] [06] [29] [40] [65]" must
  supply its own verb, all unvalued (06="ent" suggests a finite form but its
  word-boundary/finiteness here is ungranted). 59=est @1715 belongs to the
  second ne-clause.
- **W9 @1772 — FITS.** 24 @1774 is finite/modal per R24 (follower 87 ≠ 85):
  "[62] ne [24] [87=ce]..." Clean subject+ne+finite shape on granted values
  only. 62/94 share the qui-relative clause (64 @1768); no boundary between.

## Clause-boundary audit (62 vs 94)

No 46/64 boundary marker falls strictly between 62 and 94 in any window. The
boundaries found are: W2 — structural (granted 64=qui immediately after 94
breaks any subject+ne configuration; "le [62]" NP reading available);
W1/W3/W9 — 62 and 94 share one clause with a granted finite verb in 94's
scope; W4–W8 — 62/94 share a clause but 94's finite verb is unvalued.

## Verdict: NULL — C1 FAILS, C2 FIRES

3/9 windows fit subject+'ne' cleanly (W1, W3, W9); 1/9 (W2) is actively
hostile under granted values ("ne qui"); 5/9 (W4–W8) are indeterminate (94's
finite verb unvalued). **The '62 94' = subject+'ne' shape is hereby fenced as
distributional-only**: the 9 adjacencies do NOT uniformly evidence a
subject-62. The three fitting windows and the hostile W2 are packaged below
as evidence for the redteam-62-split docket; no adjudication is requested.

Scope: shape-level fence only. Untouched: 94="ne" (R19-167/168), 67 sole
polyvalence (§7 intact), 62's open class, all standing values. No
standing/red-team verdict contradicted or downgraded. Canonical-stream caveat
stands (rows a1_02/a3_00/a5_03/a5_06/a7_04/a7_06/a8_05/a8_06/a8_09 unvalidated).

## Follow-ups proposed (all verified ABSENT from queue)

1. `val-62-508-nominal` (P3) — test 62's class at @508: the "77 62" = "le
   [62]" determiner+noun reading vs subject reading; the hostile window is the
   most informative for the split docket. Bar: name 62's class at @508 at
   battery grade, or fence the nominal leg.
2. `ne-scope-62-indet` (P3) — for the five indeterminate windows (W4 @840,
   W5 @1329, W6 @1362, W7 @1686, W8 @1704), name the finite verb of each
   94-scope once neighboring values are granted; re-test the subject+ne fit.
   Bar: ≥1 window's verb named at battery grade re-opens C1; all five
   verb-namings failing hardens the distributional-only fence.
3. `reseg-62-94-W2` (P4) — test rival segmentations at @507–510 ("77 62 | 94
   64" boundary variants): is there any licensed parse preserving subject+ne
   at W2? Bar: produce one grammatical parse with ≤1 ungranted assumption, or
   fence W2 permanently.

## Bookkeeping

- Queue: `62-subject-shape-evidence` → status verdict, result null, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename).
- Lock created 2026-10-09T13:32:35Z, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
- Adverses: §7 honored — evidence only; no class, split, value, or
  polyvalence declared.
