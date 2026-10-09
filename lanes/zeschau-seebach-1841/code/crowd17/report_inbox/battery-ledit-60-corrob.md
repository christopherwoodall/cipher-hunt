# Battery report: ledit-60-corrob (re-run)

Worker: battery subagent (session afcddac0-6b41-48e1-ab18-0f4ee36d7993).
Date: 2026-10-09.
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`), parsed per
`code/side-keyhunt/repair_parse.py` (re-implemented inline; n=1847 asserted,
96 groups asserted). `canonical.py` never used. R5005, sealed gate instances,
and the red-team adjudication queue untouched. @i = 0-based pair index.
Lock: `code/crowd17/next-token/locks/ledit-60-corrob.lock` created at start
with agent id + UTC timestamp, deleted on completion.
No standing verdict overwritten or downgraded (see the headline finding).

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"if none found, @454 participial parse stands as a singleton leg (weakens,
does not kill)"

Numbered clauses (fixed before data examination):

1. (C1) Re-derive the full 60 census on the repaired stream; confirm 18
   occurrences.
2. (C2) Verify @454 is the only "77 60 [noun]" window (left neighbor 77,
   right neighbor noun-class).
3. (C3) Scan the other 17 windows for a second participial-shaped frame —
   a [determiner] 60 [noun] shape admitting a past-participle reading under
   standing values (banked determiners 11=la, 87=ce, 47=ce; provisional
   77="le"; A11 hold 45="ce"; noun-class 65).
4. (C4) Fallback: if none found, the @454 participial parse stands as a
   singleton leg (weakens, does not kill).

## Headline finding (material, pre-scan)

The target was written when the @454 participial parse ("le dit [65]",
past participle of dire used adjectivally) was a live leg. It is no longer
live: `dit-60-syncretic` returned a **kill verdict** (2026-10-09,
`code/crowd17/report_inbox/processed/battery-dit-60-syncretic.md`, recorded
in battery-queue.json): W2 @690 "65 94 29 60 03" = "[65-noun] ne er dit
[03]" admits no grammatical parse under standing values, robust to every
94 re-segmentation because banked pencil GT 29="er" directly abuts 60.
The kill is global — 60 != "dit" — unless the red team grants a §7
positional split (only 67 et/veut holds one). The bar's C4 fallback clause
("the @454 participial parse stands as a singleton leg") is therefore
obsolete as written: a parse whose only licensed value is kill-grade dead
cannot stand as any kind of leg. Per protocol §5.2 spirit, this verdict is
**null**, with the contradiction as the headline, escalated to the red team
(poly-60-redteam docket, which already owns 60's polyvalence question).

This re-run independently re-derived every number and reproduces the prior
2026-10-09 null verdict (no downgrade; same grade, fresh bytes).

## Method

Fresh parse of the repaired stream; all 18 windows re-derived. Each of the
17 non-454 windows inspected for (a) a determiner immediately left of 60
and (b) any frame admitting a past-participle reading under standing
values, given that no battery-available participial value for 60 survives
(60="dit" killed; present-participle killed at @1338 by participle-60 V1;
finite -dre stem killed at @700 by participle-60 V2).

## Window-level evidence (re-derived on the repaired stream)

@454 [a2_10]: `79 17 77 60 65 13 66` — "77 60 65" = "le[77] [60]
[65-noun]". THE flagship window. Its participial parse ("le dit [65]")
dies with 60="dit" (kill, above).

Independent counts: "77 60" bigram occurs exactly once in the 1,847-pair
stream (@454); "77 60 65" trigram exactly once; 65 is the right neighbor
of 60 exactly once (@454); the determiner set {11,77,87,47,45,79} appears
immediately left of 60 exactly once stream-wide (@454). No window among
the other 17 has both a determiner-left and a noun-class-right of 60.

The other 17 (9-gram contexts, inspected for a second participial-shaped frame):

| @ | row | 9-gram context | participial-frame check |
|---|-----|----------------|------------------------|
| 119 | a1_03 | 21 67 14 21 60 90 19 58 66 | left 21 unresolved, right 90 unresolved; no determiner, no noun-class. NO |
| 172 | a1_05 | 53 12 48 21 60 09 87 86 21 | same. NO |
| 197 | a2_00 | 56 47 01 21 60 08 67 76 87 | same. NO |
| 232 | a2_01 | 83 82 96 21 60 71 51 70 98 | same. NO |
| 322 | a2_04 | 94 06 11 92 60 15 63 71 10 | 11 two back (not adjacent); 92's class open; right 15 unresolved. NO |
| 637 | a4_01 | 67 63 74 46 60 67 77 89 48 | "que[46] [60] [67]" — no NP frame. NO |
| 690 | a5_00 | 40 65 94 29 60 03 39 74 46 | the dit-killer ("ne er dit [03]" ungrammatical at kill grade). NO |
| 700 | a5_01 | 50 45 28 94 60 12 98 20 12 | participle-60 V2 died here (finite -dre impossibility). NO |
| 995 | a6_01 | 24 26 30 03 60 67 11 96 82 | "er[03] [60]" — no. NO |
| 1338 | a7_05 | 83 86 71 64 60 08 65 64 52 | "qui[64] [60] [08]" — finite verb forced by "qui"; not a participle frame. NO |
| 1366 | a7_06 | 62 94 79 14 60 03 30 82 16 | "tout[79] le[14] [60] [03]" — determiner-left, but 03 is verb-stem (stem-03 battery-PROMOTED), so no "ledit"-shaped frame possible here. NO |
| 1474 | a7_10 | 26 12 41 53 60 06 67 33 29 | right 06=ent; 06's left-attachment rule needs a verb stem left of 06 — 60's class open; no participle reading. NO |
| 1563 | a8_01 | 11 26 30 06 60 71 50 29 24 | 06 left-attaches to 30; no determiner frame at 60. NO |
| 1644 | a8_04 | 56 12 33 98 60 03 64 31 10 | hostile to dit (98="vient" battery-level wants an infinitive). NO |
| 1674 | a8_05 | 78 55 81 92 60 03 39 74 77 | 92's class open; neutral, no determiner-left NP frame. NO |
| 1690 | a8_05 | 62 94 79 14 60 27 46 24 85 | "79 14 60 27" — determiner-left like @1366, but right 27 unresolved; even a noun-27 cannot host a parse while 60="dit" stands kill-grade dead. NO |
| 1735 | a8_07 | 01 56 30 06 60 12 48 52 86 | 06 left-attaches to 30; no frame. NO |

## Per-clause pass/fail

- C1: PASS. 60 census = 18, offsets
  [119, 172, 197, 232, 322, 454, 637, 690, 700, 995, 1338, 1366, 1474, 1563,
  1644, 1674, 1690, 1735] — matches the queue's "18 occurrences".
- C2: PASS. @454 is the only "77 60 [noun]" window (only left-77 stream-wide;
  only right-65).
- C3: PASS (negative result). No second participial-shaped frame exists
  among the other 17 windows — and no battery-available participial value
  for 60 survives to fill one.
- C4: CANNOT FIRE AS WRITTEN. The fallback presupposes a live @454
  participial leg. Its only licensed value (60="dit") was kill-grade killed
  by dit-60-syncretic after this target was written. A killed parse cannot
  "stand as a singleton leg". This is not the weakening the bar describes —
  the leg is dead, not weakened. Per protocol §5.2: null, contradiction as
  headline, escalate.

## Verdict: NULL

The scan completed on bytes: C1–C3 verified, no second participial frame
exists. But the target's point — corroborate or singleton-ize the @454
participial leg — is moot: the leg itself died with 60="dit"
(dit-60-syncretic, kill, 2026-10-09). Escalate to the red team
(poly-60-redteam): the NP-frame question for 60 now needs a new
participial value hypothesis or a formal retirement of the @454 frame.
No standing verdict was overwritten or downgraded (the dit kill stands
unmodified; this report only records its consequence for the bar).

## Follow-ups proposed (for supervisor queuing)

1. `participle-60-newvalue` (P3): with 60="dit" kill-grade dead, the only
   NP frame that ever licensed a participial 60 ("77 60 65" = "le [P]
   [65-noun]" @454) is value-less. Bar: propose ONE new past-participle
   value for 60 that parses @454 with ≤1 unstated assumption; promote iff
   it also survives the other 17 windows (adverses: @690 "ne er __ [03]"
   hostile, @1338 "qui __" forces finite); kill iff no candidate parses.
   Coordinates with (does not duplicate) poly-60-redteam and
   npframe-60-690 (verdict null, 2026-10-09).
2. `npframe-60-detleft-closeout` (P3, narrower): the only windows with a
   determiner-shape left of 60 besides @454 are @1366/@1690 ("79 14 60").
   @1366 is already closed (03=verb-stem promoted, cannot follow a
   "ledit"-style participle); fence @1690 by testing 27's class once —
   if 27 is non-nominal, every det-left 60 window is fenced and the NP
   question for 60 retires at battery level pending the red-team docket.
3. `framecensus-60-redteam-pack` (P3): build the structured 18-window frame
   census for 60 (left-neighbor class × right-neighbor class, per-window
   frame shapes, the verified table above plus 40/92-boundary and 06
   left-attachment checks) as a battery evidence package for the
   poly-60-redteam docket. No value claim; barred by completeness and
   byte-traceability of the 18 windows.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/ledit-60-corrob.lock` created on start
  (agent id + UTC), deleted on completion.
- Queue update: temp-file + rename on `battery-queue.json`, own entry only;
  pre-write assert confirmed the existing entry's verdict (null, 2026-10-09)
  is not downgraded; JSON re-validated after write.
- No standing verdict contradicted or downgraded. dit-60-syncretic's kill
  is cited, not re-run; npframe-60-454 (null) and npframe-60-690 (null)
  cited, not re-run.
- R5005, sealed gate instances, and the red-team adjudication queue untouched.
