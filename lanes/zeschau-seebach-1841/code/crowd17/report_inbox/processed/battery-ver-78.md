# Battery report: ver-78 — claim 78="ver"

Date: 2026-10-08. Worker: cdab139b-5be1-446b-a307-2c6444b4a1f1.
Stream: repaired 1,847-pair parse only. `canonical.py` never used. R5005 untouched
(read-only parse; no writes). Lock `locks/ver-78.lock` created 2026-10-08T05:51:50Z
(no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"promote iff 'ce [78]' x7 all parse as 'ver'-words + distributional kill of 'er' holds + @296 reconciled"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. All 7 'ce [78]' windows parse as 'ver'-words.
2. The distributional kill of 78='er' holds against the 29='er' control.
3. @296 ('la 78-40', 'l'ere'-shaped) is reconciled.

## Method

Parsed `data/upstream-ct_R5005.txt` with `code/side-keyhunt/repaired_offsets.json`
exactly like `repair_parse.py` (stride-2 pairing per row offset). Verified:
1,847 pairs, 96 distinct groups. Determiner set for the predecessor test:
{11=la, 77="le" (provisional), 87=ce, 47="ce" (allophone)} — this set reproduces
the red team's re-derived counts exactly (see correction below). All counts below
are pair-index offsets (@n = index of the named group in the 1,847-pair stream).

## Correction to the queue's evidence gloss (verified against bytes)

The queue's `evidence` field transposes the 29/78 attributions. Re-derived:

- n(29)=45, n(78)=31.
- Determiner predecessors: 29='er' **2/45**; 78 **16/31**.
  (Queue gloss assigns 16/31 to the control — backwards. R16-005 has it right.)
- Predecessor == 33: 29='er' **5/45**; 78 **0/31**.
  (Queue gloss assigns 0/31 to the control — backwards, and it would contradict
  the A10 "33+29" hold. R16-005 has it right.)
- Odds ratio = (16/15)/(2/43) = **22.93** (symmetric; the kill conclusion is
  unaffected by the transposition).
- Fisher two-sided: det-predecessor table p ≈ 2.5e-06 (rejects at lane standard);
  after-33 table p ≈ 0.075.

Corrected linguistic story: 29='er' is mostly word-internal ('premiere' in the
crib) or an infinitive ending after 33 (A10 hold 33+29); 78 takes determiners
16/31 ('ce/le/la ver…', noun-shaped) and never follows 33. 78 is
distributionally unlike 'er' — the kill stands, with the direction corrected.

## Window-level evidence

### 'ce [78]' x7 (78 offsets; 'ce' = 87/47 at -1; ce-offsets match R16-005's
[363,572,628,818,981,1104,1396] exactly)

- 78@364 (ce@363=47, a2_06): `62 48 76 [47] 78 48 49 61 70` → "ce 78 48".
  48 value open. 'er' excluded (no elision save for "ce"+"er"); 'ver' admitted.
- 78@573 (ce@572=87, a3_02): `45 94 52 [87] 78 45 13 55 61` → "ce verdict
  [13-55-61]" under 45="dict"-allophone (R16-004 lead). Positive 'ver'.
- 78@629 (ce@628=87, a4_01): `37 33 29 [87] 78 67 08 52 67` → "ce 78 et/veut"
  (67 = sole polyvalence). 'er' excluded; 'ver' admitted.
- 78@819 (ce@818=47, a5_05): `49 74 74 [47] 78 40 95 13 24` → "ce ver+e",
  'verre/verte'-shaped. Positive-leaning 'ver' (word identity open).
- 78@982 (ce@981=47, a6_01): `92 07 76 [47] 78 45 01 24 89` → "ce verdict [01]".
  Positive 'ver'.
- 78@1105 (ce@1104=47, a6_06): `82 94 74 [47] 78 65 63 00 66` → "ce 78 65".
  65 value open. 'er' excluded; 'ver' admitted.
- 78@1397 (ce@1396=47, a7_07): `89 16 76 [47] 78 48 40 67 77` → "ce 78 48 40".
  48 value open. 'er' excluded; 'ver' admitted.

Successor census after 'ce 78': 48 x2, 45 x2, 67 x1, 40 x1, 65 x1.

'verdict' x4 (78→45): 78@313 (pred 37), 78@573 (ce), 78@982 (ce), 78@1164
(pred 67). 'ce verdict' x2 = @573, @982. Evidence claim confirmed.

### @296

`29 40 65 16 01 [11]@296 78@297 40@298 97 86 91` (rows a2_03..a2_04) →
"la 78 e" = 'l'ere'-shaped. Votes 'er'. 'le/la 78' x9 confirmed at 78 @
[8, 214, 297, 648, 1078, 1181, 1352, 1543, 1670] (matches R16-005).

## Per-clause results

1. **PASS (caveat):** 7/7 exclude 'er' via the granted grammaticality argument
   ("ce"+"er" has no elision save; word-internal "cer-" would re-litigate the
   granted 47/87 word values — R16-005). 3/7 give positive ver-word reads
   (@573, @982 'verdict'; @819 'verre/verte'-shaped). 4/7 are ver-compatible
   with open continuations (48, 67, 65) — the force there is exclusionary.
2. **PASS:** the distributional kill of 78='er' re-derives on the repaired
   stream (corrected attribution above; OR=22.93, Fisher p≈2.5e-06).
3. **NOT SATISFIED AS WRITTEN:** the bar's adverse proposes the
   positional-allophone reconciliation (78='er' after 'la', 'ver' after 'ce').
   Standing red-team verdict R16-005 **rejected** that escape under lane law
   (67 et/veut is the sole true polyvalence — protocol §7, not negotiable).
   @296 stands as a red-team-fenced 1-window residual: fenced, not reconciled.

No window forces 78="ver" false at kill grade; no cleaner rival value was
demonstrated on these frames. Not kill.

## Verdict: NULL

**Headline (escalation to the red team):** the bar is unsatisfiable as written —
its clause 3 requires the positional-allophone reconciliation of @296, which
R16-005 rejected under lane law. All other clauses re-derived and confirmed on
the repaired stream, and the queue's evidence gloss needs the attribution
correction recorded above (29: 2/45 det-pred, 5/45 pred-33; 78: 16/31, 0/31).

This battery adds no new discriminating evidence beyond re-derivation:
R16-005 already adjudicated this exact bundle as **78="ver" LEAD, correctly
graded LEAD not settled**. A promote verdict here would contradict that
standing grading. The red team should decide whether the fenced-residual status
of @296 satisfies a re-barred clause 3, or re-bar ver-78 without the
allophone route (follow-up 1 below).

## Follow-up targets (required for null)

1. **ver-78-rebar** (priority 1). Claim: 78="ver" promotes under a lane-legal
   bar. Bars: (a) 'ce [78]' x7 re-derived on the repaired stream, per-window
   'er'-exclusion stated; (b) distributional kill of 'er' re-derived with the
   corrected attribution (29: 2/45 det-pred, 5/45 pred-33 vs 78: 16/31, 0/31;
   OR=22.93); (c) @296 recorded as red-team-fenced 1-window residual (R16-005)
   — no allophone reconciliation attempted. Evidence: this report.
   Adverses: R16-005 LEAD-not-settled grading stands until red-team
   ratification; 'verdict' x4 conditional on the 45="dict" lead (R16-004);
   4/7 ce-78 continuations (48, 67, 65) open.
2. **ver78-ce78-open-succ** (priority 2). Claim: the open successors after
   'ce 78' complete French ver-words. Bars: name 48's and 65's values/frames
   (coordinate with their batteries; do not duplicate) and show "ce ver[48/
   65]" reading as a ver-word in ≥3 of the 4 open windows (@364, @629,
   @1105, @1397), or record kill-grade incompatibility. Evidence: successor
   census above. Adverses: 48/65 values open; 67 is the sole polyvalence.
3. **ver78-296-reparse** (priority 2). Claim: @296 "11 78 40 97 86" re-parses
   cleanly under 78="ver". Bars: (a) 97 and 86 given values/frames from their
   own batteries; (b) "la ver-e-[97]-[86]" reads as one French word under
   78="ver" — or the residual stays fenced with the failure stated.
   Evidence: @296 window above. Adverses: 'l'ere' rival read stands;
   11=la banked.

## Reproducibility

Analysis script: `code/crowd17/next-token/ver78_battery.py` (reads the repaired
stream only; no writes outside this report and the lockfile).
