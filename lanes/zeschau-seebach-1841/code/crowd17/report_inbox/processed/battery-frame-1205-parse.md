# Battery report: frame-1205-parse

Target: `frame-1205-parse`. Claim: the third window (@1205) parses standalone.
Date: 2026-10-09. Worker: frame-1205-parse battery worker.
Lock `locks/frame-1205-parse.lock` created 2026-10-09T06:16:31Z (no fresh lock for
this id; none pre-existing); deleted on completion.

Parent null: `name-13-55-61` (2026-10-08, processed). This battery tests only the
narrowed standalone-parse bar below; it does not re-litigate the parent's naming
null.

## Bar (verbatim, pre-registered)

"(a) state 43/21/65 contact profiles on the repaired stream; (b) parse '29 45 58
ce(47) 43 55 61 21 65' (@1199-1209, 0-based) with word boundaries stated under
granted values only (47='ce'); (c) fence the 29/45/58 left context with stated
cause."

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. The 43/21/65 contact profiles are stated on the repaired stream. [state]
2. The 9-pair sequence parses with word boundaries stated under granted values
   only (47="ce" the named grant). [parse]
3. The 29/45/58 left context is fenced with stated cause. [fence]

Offset convention: @n below = 0-based pair index in the repaired 1,847-pair
stream. Offset correction: the bar's "@1199-1209" is an 11-index range; the
stated 9-pair sequence "29 45 58 47 43 55 61 21 65" is exactly @1200-1208
0-based, flanked by @1199=64 and @1209=64. The third 55-61 bigram is @1205-1206.
No re-parse needed; the shift is +1 at the left edge.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
(stride-2 pairing per row offset). Asserted 1,847 pairs / 96 types before
testing. `canonical.py` never used. R5005 untouched (read-only parse). No sealed
gates, no red-team contact. Every number below was re-derived in-session; no
number is carried over from the parent report.

Granted values used (protocol §7 only): banked 11=la, 70=pre, 82=m, 34=i,
29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour,
84=on, 47=ce (allophone tier). Nothing else is leaned on for clause (b):
45="ce" is A11 HOLD (not granted), 94="ne"/30="pas"/59="est"/77="le" are
battery-provisional or provisional — excluded per the bar.

## Window-level evidence (re-derived)

The window, @1200-1208 (row a7_00):

```
@1199:64  |  @1200:29  @1201:45  @1202:58  @1203:47  @1204:43  @1205:55  @1206:61
@1207:21  @1208:65  |  @1209:64  @1210:59  @1211:32  @1212:48
```

With granted values: `qui | er [45] [58] ce [43] [55] [61] [21] [65] | qui ...`.
Inside the 9-pair sequence exactly two tokens carry granted values: 29="er"
(banked) and 47="ce" (allophone tier). 45, 58, 43, 55, 61, 21, 65 are all open.

Contact profiles (re-derived, full):

- 43, n=16: pre {37x3, 96x2, 82x1, 88x1, 56x1, 32x1, 46x1, 11x1, 06x1, 47x1,
  08x1, 21x1, 78x1}; suc {00x3, 77x2, 87x2, 98x2, 29x1, 81x1, 91x1, 24x1, 07x1,
  55x1, 21x1}. Positions: [21, 43, 244, 258, 343, 386, 439, 563, 1027, 1092,
  1126, 1204, 1303, 1305, 1544, 1724].
- 21, n=30: pre {96x3, 33x3, 83x3, 11x2, 68x2, 48x2, 01x2, 06x2, 61x2, 08x1,
  14x1, 64x1, 86x1, 66x1, 02x1, 62x1, 43x1, 46x1}; suc {67x8, 62x5, 60x4, 65x4,
  64x2, 69x1, 35x1, 80x1, 85x1, 43x1, 02x1, 68x1}. Positions: [99, 109, 115,
  118, 134, 171, 176, 196, 231, 359, 371, 505, 706, 719, 850, 937, 1064, 1162,
  1172, 1207, 1304, 1422, 1456, 1463, 1466, 1529, 1538, 1631, 1787, 1841].
- 65, n=25: pre {21x4, 40x3, 91x2, 74x2, 24x2, 08x2, 06x2, 94x1, 60x1, 98x1,
  78x1, 41x1, 64x1, 92x1, 79x1}; suc {63x4, 23x3, 13x3, 64x3, 94x2, 16x1, 88x1,
  84x1, 14x1, 71x1, 38x1, 46x1, 68x1, 48x1, 34x1}. Positions: [135, 138, 251,
  293, 372, 455, 512, 687, 724, 787, 812, 923, 1106, 1112, 1208, 1253, 1340,
  1383, 1530, 1588, 1608, 1683, 1712, 1748, 1781].

Interior bigram census of the window (re-derived, full stream):

| junction | count | windows |
|---|---|---|
| 29->45 | 1 | @1200 only |
| 45->58 | 1 | @1201 only |
| 58->47 | 2 | @610, @1202 |
| 47->43 | 1 | @1203 only |
| 43->55 | 1 | @1204 only |
| 55->61 | 3 | @576, @1167, @1205 |
| 61->21 | 2 | @1206, @1455 |
| 21->65 | 4 | @134, @371, @1207, @1529 |
| 65->64 | 3 | @724, @1208, @1340 |

Left block: 29 n=45, pre {33x5, 86x4, 06x4, 34x3, 64x3, 03x3, 11x2, 46x2, ...},
suc {40x9, 89x5, 47x4, 80x4, 42x3, 85x3, 87x3, 82x3, ...} (suffix-profiled:
29->40="e" x9). 64->29 x3 (@290, @684, @1199). 58 n=7, pre {85x3, 19x1, 35x1,
02x1, 45x1}, suc {35x2, 47x2, 66x1, 15x1, 17x1}; no value arm anywhere. 45 n=22,
pre {78x4, 74x3, 76x2, 50x2, 96x2, ...}, suc {93x3, 64x3, 23x3, 28x2, 13x2,
...}; value is A11 HOLD only, ungranted.

## Per-clause pass/fail

1. **PASS.** 43/21/65 profiles stated above, fully re-derived (43 n=16, 21
   n=30, 65 n=25, with every predecessor/successor count and positions).
2. **FAIL (null grade).** Under granted values only, the sequence contains two
   valued tokens (29="er", 47="ce") and seven open ones. No interior word
   boundary can be stated: 29->45, 45->58, 47->43, 43->55 are stream-unique
   adjacencies between unvalued neighbors (uniqueness is boundary-neutral here;
   it supports no direction), 58->47 x2 has an unvalued left edge, 55->61 x3
   and 61->21 x2 and 21->65 x4 are distributional leads with no value anchor.
   The single statable boundary is at the sequence's RIGHT EDGE: @1208|@1209
   ("65|qui") via 65->64 x3 with granted 64="qui" (the @1209-1211 "qui 59 32"
   right context is outside the bar). One edge boundary does not parse a
   9-pair interior. Not kill-grade: no granted contradiction forces the claim
   false; the interior is conditional on open values (21, 43, 65, 45, 55, 61,
   58) — per the fork-78-45-rerun precedent an unfired conditional is null,
   not kill. No cleaner rival parse was demonstrated.
3. **PASS (fence with stated cause).** The 29/45/58 block cannot parse under
   granted values, and the cause is stated: (i) 29->45 and 45->58 are
   stream-unique adjacencies with no frame support; (ii) 29's left neighbor is
   @1199=64="qui" (granted) — "qui er…" with 29 suffix-profiled (29->40="e" x9,
   modal predecessors 33/86/06/34) gives no word-initial or qui-prefixed
   reading with support; (iii) 58 has no value arm anywhere (n=7, 5 distinct
   predecessors); (iv) 45's value is A11 HOLD only, and A11 explicitly forbids
   the mirror bar from importing 87's individual legs. The block is fenced as
   unparseable-standalone under granted values; resolving it requires naming
   45/58, which the bar forbids.

## Adverses answered

- "21, 43, 65 values open": answered — all three remain open throughout; the
  null rests on exactly this openness. 65 carries a promoted full profile
  (prof-65, 2026-10-08) but no named value; 21 is open; 43's noun candidates
  (noun-43 null, 2026-10-09: {suite, condition, maniere, mesure}) are unchosen
  here.
- "coordinate with queued w1-573-subject, do not duplicate": answered —
  `w1-573-subject` already returned verdict (null, 2026-10-09) per the queue;
  this battery makes no "ne mentent" subject claim and overlaps it nowhere.
  Nothing duplicated.

No standing red-team verdict is contradicted (A11 HOLD scoping, §7
banked/granted/killed values all respected; no value claimed) — no escalation.

## Verdict: null

Headline: clause 1 passes (profiles verified), clause 3 passes (fence with
stated cause), but clause 2 is unsatisfiable — the third window does not parse
standalone under granted values only. Two valued tokens (29="er", 47="ce") in
nine; the single statable boundary ("65|qui") sits at the right edge, not in
the interior. The failure is conditional on open values, so this is null
grade, not kill: the claim is underdetermined, not falsified.

## Follow-up targets (null regenerates work; all ids verified absent from the queue 2026-10-09)

1. **bound-65-64-qui** (priority 2). Claim: the @1208|@1209 "65|qui" boundary
   is a real word/clause boundary under granted 64="qui". Bars: (a) state the
   right contexts of all three 65->64 windows (@724, @1208, @1340); (b) the
   "21 65" predecessor gate: 21->65 x4 (@134, @371, @1207, @1529) parsed or
   fenced with cause; (c) fence any window whose right edge fails the
   "nominal + qui" shape. Evidence: this report. Adverses: 65/21 values open;
   61->21 x2 (@1206, @1455) may show the left edge instead.
2. **noun-43-1205-window** (priority 3). Claim: @1200-1208 reads "er [45] [58]
   ce [43-noun] [55] [61] [21] [65]" with 43 drawn from noun-43's candidate
   set {suite, condition, maniere, mesure}. Bars: (a) run noun-43's
   "pour que"-frame discriminator to select the candidate; (b) "ce [43]" fits
   with granted 47="ce"; (c) the 55-61 bigram window parses under the chosen
   noun. Coordinate with noun-43 (verdict null recorded); do not re-litigate
   it. Evidence: this report. Adverses: 45="ce" HOLD, 58/55/61/21/65 open;
   47->43 x1 stream-unique.
3. **left-64-29-boundary** (priority 3). Claim: the @1199|@1200 "qui|er"
   junction decides 29's word-initial status. Bars: (a) state all three
   64->29 windows (@290, @684, @1199) with left context stated; (b) resolve iff
   all three show 29 word-initial or all three show 29 as suffix; (c) fence
   the residual with stated cause. Evidence: this report (64="qui" granted,
   29="er" banked, 29->40 x9 suffix profile). Adverses: 29's modal
   predecessors (33x5, 86x4, 06x4) differ from "qui".

## Reproducibility

All counts re-derived in-session from the repaired stream (1,847 pairs /
96 types asserted before testing). Analysis scripts were session-local
(/tmp/f1205*.py, not retained); the profiles, bigram censuses, and window
dumps above are the record. No writes outside this report, the queue edit,
and the lockfile (deleted).
