# Battery report: ver-78-rebar — claim 78="ver" promotes under a lane-legal bar

Date: 2026-10-08. Worker: 6c3441fc-0c35-4a37-b110-e4ee88f1eb84.
Stream: repaired 1,847-pair parse only (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`).
`canonical.py` never used. R5005 untouched (read-only parse; no writes).
Lock `locks/ver-78-rebar.lock` created 2026-10-08T06:37:06Z (no lock present);
deleted on completion.

## Bar (verbatim, pre-registered)

"(a) 'ce [78]' x7 re-derived on the repaired stream, per-window 'er'-exclusion
stated; (b) distributional kill of 'er' re-derived with the corrected
attribution (29: 2/45 det-pred, 5/45 pred-33 vs 78: 16/31, 0/31; OR=22.93); (c)
@296 recorded as red-team-fenced 1-window residual (R16-005) — no allophone
reconciliation attempted"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. (a) 'ce [78]' x7 re-derived on the repaired stream, per-window 'er'-exclusion
   stated.
2. (b) Distributional kill of 'er' re-derived with the corrected attribution
   (29: 2/45 det-pred, 5/45 pred-33; 78: 16/31 det-pred, 0/31 pred-33;
   OR=22.93).
3. (c) @296 recorded as red-team-fenced 1-window residual (R16-005); no
   allophone reconciliation attempted.

## Method

Re-ran the prior battery's analysis (`code/crowd17/next-token/ver78_battery.py`)
against the repaired 1,847-pair stream; asserted 1,847 pairs / 96 groups first.
Determiner set for the predecessor test: {11=la, 77="le" (provisional),
87=ce, 47="ce" (allophone)} — same set as the prior report. Computed both
Fisher two-sided p-values independently (hypergeometric tail; code in the
report file metadata, re-derived, not copied). Every @-offset below is a
pair index in the 1,847-pair stream.

## Window-level evidence

### Clause (a): 'ce [78]' x7 (78 offsets; 'ce' = 87/47 at -1)

Ce-offsets match R16-005's [363,572,628,818,981,1104,1396] exactly.

- 78@364 (ce@363=47, row a2_06): `48 76 [47] 78 48 49 61` -> "ce 78 48".
  Successor 48 value open. 'er' excluded: "ce"+"er" has no elision save, and
  word-internal "cer-" would re-litigate the granted 47/87 word values
  (R16-005). 'ver' admitted ("ce ver-…").
- 78@573 (ce@572=87, row a3_02): `94 52 [87] 78 45 13 55 61` -> "ce verdict
  [13-55-61]" under 45="dict"-allophone (R16-004 lead). Positive 'ver' read,
  conditional on the lead.
- 78@629 (ce@628=87, row a4_01): `33 29 [87] 78 67 08 52` -> "ce 78
  et/veut" (67 = sole polyvalence, positional resolution rule stands).
  'er' excluded; 'ver' admitted. Successor 67 open.
- 78@819 (ce@818=47, row a5_05): `74 74 [47] 78 40 95 13` -> "ce ver+e",
  'verre/verte'-shaped. Positive-leaning 'ver' (word identity open).
- 78@982 (ce@981=47, row a6_01): `07 76 [47] 78 45 01 24` -> "ce verdict
  [01]". Positive 'ver' read, conditional on the 45="dict" lead (R16-004).
- 78@1105 (ce@1104=47, row a6_06): `94 74 [47] 78 65 63 00` -> "ce 78 65".
  Successor 65 value open. 'er' excluded; 'ver' admitted.
- 78@1397 (ce@1396=47, row a7_07): `16 76 [47] 78 48 40` -> "ce 78 48 40".
  Successor 48 value open. 'er' excluded; 'ver' admitted.

Successor census after 'ce 78': 48 x2, 45 x2, 67 x1, 40 x1, 65 x1. 'verdict'
(78->45) x4 total at 78@313 (pred 37), 78@573 (ce), 78@982 (ce), 78@1164
(pred 67); 'ce verdict' x2 = @573, @982. All confirmed on the repaired stream.

### Clause (b): distributional kill of 'er' (corrected attribution)

- n(29)=45, n(78)=31 (re-derived).
- Determiner predecessors {11,77,87,47}: 29 = 2/45 (29@78 pred 11, 29@500
  pred 11); 78 = 16/31 (78@8,214,648,1078,1181,1352,1543 pred 77; 78@297,1670
  pred 11; 78@364,819,982,1105,1397 pred 47; 78@573,629 pred 87).
- Predecessor == 33: 29 = 5/45 (29@274,627,1233,1425,1478); 78 = 0/31
  (zero).
- Odds ratio (16/15)/(2/43) = 22.93. Fisher two-sided: det-predecessor table
  p = 2.47e-06 (rejects at lane standard); after-33 table p = 0.075.
- Corrected linguistic story (unchanged from prior report): 29='er' is mostly
  word-internal ('premiere' in the crib) or an infinitive ending after 33
  (A10 hold 33+29); 78 takes determiners 16/31 ('ce/le/la ver…', noun-shaped)
  and never follows 33. 78 is distributionally unlike 'er'. Kill stands.

### Clause (c): @296 (red-team-fenced 1-window residual)

`16 01 [11]@296 78@297 40@298 97 86` (rows a2_03/a2_04) -> "la 78 e",
'l'ere'-shaped. Votes 'er'. Per the re-bar, this window is RECORDED as the
red-team-fenced 1-window residual per R16-005 — no positional-allophone
reconciliation attempted (the lane-illegal clause that killed the prior bar).
'le/la 78' x9 confirmed at 78 @ [8, 214, 297, 648, 1078, 1181, 1352, 1543,
1670] (matches R16-005); @297 is the fenced residual.

## Per-clause pass/fail

1. **PASS:** 7/7 'ce [78]' windows re-derived on the repaired stream with
   per-window 'er'-exclusion stated above. Force is exclusionary in 4/7
   (@364, @629, @1105, @1397 — open successors 48/65/67); 3/7 give positive
   ver-word reads (@573, @982 'verdict'; @819 'verre/verte'-shaped), of which
   the two 'verdict' reads are conditional on the R16-004 lead.
2. **PASS:** distributional kill re-derived with the corrected attribution
   (29: 2/45 det-pred, 5/45 pred-33; 78: 16/31, 0/31; OR=22.93; Fisher
   p≈2.5e-06).
3. **PASS:** @296 recorded as red-team-fenced 1-window residual (R16-005);
   no allophone reconciliation attempted, per the re-bar.

## Adverses (fenced, not ignored)

- **R16-005 LEAD-not-settled grading stands until red-team ratification.**
  FENCED with stated cause: the red team graded this exact bundle LEAD, not
  settled. A battery-level promote would contradict that standing grading.
  Per protocol §5, escalated below — a promote here is a red-team act, not a
  battery act.
- **'verdict' x4 conditional on the 45='dict' lead (R16-004).** FENCED: the
  two positive 'verdict' legs (@573, @982; also @313, @1164 non-ce) all depend
  on 45='dict', which is a lead, not a grant. Bar clause (a) requires only
  'er'-exclusion, so it passes — but the positives carry no promote force.
  Re-rating is gated on fork-78-45-adjudication / dict-45 resolving the
  78->45 x4 contact (follow-up 2).
- **4/7 ce-78 continuations (48, 67, 65) open.** FENCED to queued
  ver78-ce78-open-succ — not duplicated here. The 67-adjacent window (@629)
  reads "ce ver et/veut" under the standing positional rule; no second
  polyvalence declared.

## Verdict: NULL

**Headline (escalation to the red team):** all three bar clauses pass on the
repaired stream — the re-bar is lane-legal and fully satisfied — but the
listed adverses are not answered at battery grade: promoting 78="ver" here
would contradict standing red-team verdict R16-005, which graded this exact
bundle LEAD, not settled. Per protocol §5 the battery records NULL rather
than overwrite a red-team grading. The two positive 'verdict' legs are
additionally conditional on the un-granted 45='dict' lead (R16-004).

No window forces 78="ver" false at kill grade; no cleaner rival value was
demonstrated on these frames. Not kill.

**Red-team question:** does the fenced-residual status of @296 (clause 3 of
the re-bar) satisfy the settle condition for 78="ver", given clauses 1-2
re-derived clean — i.e. can the battery NULL be ratified to promote, or does
ratification require the R16-004 45='dict' dependency to resolve first?

## Follow-up targets (required for null; coordinate, do not duplicate)

1. **ver78-la78-census** (priority 2). Claim: the 9 'le/la 78' windows
   (@8, @214, @297, @648, @1078, @1181, @1352, @1543, @1670) head noun phrases
   under 78='ver'. Bars: (a) >=7/9 windows parse with 78 as a noun head
   ('la verte'-shaped); (b) @297 explicitly fenced, not reconciled; (c) 77-78
   windows handled under the '77 78'='lever' rival (lever-77-78) — parse or
   fence the overlap, do not re-litigate it. Evidence: this report's
   det-predecessor census (16/31 noun-shaped). Adverses: 'lever'/'elever'
   composition rival (lever-77-78); @297 fenced.
2. **ver78-45-dependency-gate** (priority 3, gated). Claim: once
   fork-78-45-adjudication or dict-45 resolves the 78->45 x4 contact
   (@313, @573, @982, @1164), the two positive 'verdict' legs (@573, @982)
   re-rate from conditional to leg-grade or are dropped. Bars: re-parse all
   four windows under the resolved 45 value and state the rating. Evidence:
   this report. Adverses: 45='ce' HOLD (A11) is the rival value at those
   windows.

## Reproducibility

Re-derivation: `code/crowd17/next-token/ver78_battery.py` (reads the repaired
stream only; run again by this worker 2026-10-08 — outputs matched the prior
report's offsets and counts exactly). Fisher p-values recomputed independently
this run (det-predecessor 2.47e-06; after-33 0.075). No writes outside this
report and the lockfile.
