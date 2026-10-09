# Battery neque-verb-slot-wide — report

## Bar (verbatim, pre-registered)

> "if the verb slot is empty in all 16 under standing values, fence the 'ne...que'-bracket family as a systematic residual rather than a per-window accident"

## Bar restated (numbered, before testing)

- C1: the 16 nearest-46 '94...46' windows are censused byte-exact on the repaired stream.
- C2: in every window, the cell immediately after 94 (the 'ne...que' verb slot) is empty of a finite verb under standing values.
- C3: if C2 passes, fence the 'ne...que'-bracket family as a systematic residual.

Adverses: none listed.

## Method

Stream re-derived in-session: 1,847 pairs / 96 types from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(asserts held: 1,847 pairs, 96 distinct groups). `canonical.py` never used.

Window definition (finder wider set, operationalized): for each distinct 46
that is some 94's nearest following 46, the window runs from the nearest
preceding 94 to that 46. n(94)=37, n(46)=29, distinct nearest-46 brackets = 16.

The 'ne...que' restrictive frame is `ne + FINITE-VERB + que`, so the verb slot
is the cell immediately after 94. Finite standing under current law:
- 24: R24 (red-team declared, kill-grade byte evidence) — finite/modal verb
  except at the five declared 24-85 windows (0-based @732/@955/@1438/@1693/@1754),
  where 24='en'. Follower of a 24 must be 85 for the 'en' arm.
- All other verb cells (92/93/98/63/38 = verb-class; 85 = verb-stem;
  86 = INF-class; 80/89 = A8 verb-frames/infinitive; 88 = gov-class) carry no
  general finite grant at battery grade; locus-level finiteness grants
  (e.g. 93-fin @1541) are not transferable to the slot test.

## Census (all 16, 0-based, byte-exact)

| # | 94@ | 46@ | rows | slot (94+1) | standing | finite? |
|---|-----|-----|------|-------------|----------|---------|
| W01 | 65 | 95 | a1_01/a1_02 | 92 | verb(cls) | no |
| W02 | 101 | 107 | a1_02/a1_03 | 93 | verb(cls) | no |
| W03 | 161 | 217 | a1_05/a2_01 | 24 | finite/modal (R24) | **YES** |
| W04 | 250 | 309 | a2_02/a2_04 | 65 | noun(cls) | no |
| W05 | 349 | 419 | a2_05/a2_08 | 74 | unvalued | no |
| W06 | 509 | 546 | a3_00/a3_01 | 64 | qui(prom) | no |
| W07 | 578 | 636 | a3_02/a4_01 | 82 | m(gt) | no |
| W08 | 688 | 694 | a5_00/a5_01 | 29 | er(gt, letter) | no |
| W09 | 785 | 792 | a5_04/a5_04 | 74 | unvalued | no |
| W10 | 841 | 865 | a5_06/a5_07 | 26 | noun(lead) | no |
| W11 | 1182 | 1191 | a6_10/a7_00 | 82 | m(gt) | no |
| W12 | 1363 | 1408 | a7_06/a7_07 | 79 | tout(prom) | no |
| W13 | 1576 | 1625 | a8_01/a8_03 | 76 | noun(prom) | no |
| W14 | 1664 | 1681 | a8_04/a8_05 | 84 | on(prom) | no |
| W15 | 1687 | 1692 | a8_05/a8_05 | 79 | tout(prom) | no |
| W16 | 1742 | 1744 | a8_07/a8_07 | 82 | m(gt) | no |

W03 detail: 94@161 → 24@162 → 46@217 (span 55). Follower of 24@162 is 87
(not 85), and 162 is not among the five R24-85 windows, so R24 declares
24@162 finite/modal verb. Head shape: `94 24 87 ... 46` =
"ne [24-finite/modal] ce ... que".

## Per-clause results

- C1 PASS — 16/16 windows byte-confirmed (offsets, rows, spans in table above).
- C2 FAIL — the verb slot is filled at W03 (24@162, R24 finite/modal).
  15/16 windows have an empty verb slot; the bar's "all 16" condition fails.
- C3 does not fire — the systematic-residual fence cannot be executed on this
  test. The W03 exception is a genuine 'ne...que'-shaped head
  ("ne [modal] ... que" is the canonical restrictive mold, e.g. "ne pouvoir que").

Scope note: no full restrictive parse is demonstrated at W03 either — the
55-cell span contains three more 24s plus 98/88/63, and naming a restrictive
parse needs 24's value and a complete clause. The family is therefore
undecided, not killed: 15 windows cannot host the frame (empty slot), 1 window
can (filled slot, parse unproven).

## Verdict: NULL

The fence condition is not met. Nulls regenerate work:

1. `neque-W3-parse` (P3) — parse the full restrictive "ne [24] ... que" frame
   at @161–217; sharpest test of a genuine 'ne...que' window once 24's value
   is named. Bar: complete clause parse with ≤1 new assumption, else fence W03.
2. `neque-15slot-fence` (P3) — fence the remaining 15 windows individually as
   'ne...que'-incapable on the empty-verb-slot ground, with the W3 exception
   recorded. Bar: slot-empty confirmed at each, else re-open.
3. `val-24-162-modal` (P4) — gated re-fire: name 24's value at @162; a named
   modal licenses the W3 restrictive head at battery grade.

## Standing state

No standing/red-team verdict contradicted or downgraded. R24 (R19-191),
R19-167 (94 = single syllabic "ne"; split CLOSED), R19-192 (§7 et/veut rule),
and the verb-class grants all adopted as premises. §7 intact (no new
polyvalence declared). Canonical-stream caveat stands (row offsets unvalidated
beyond a5_03).

## Bookkeeping

- Target: `neque-verb-slot-wide`, status queued → verdict at start of run.
- Lock: created 2026-10-09T12:45:53Z, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
