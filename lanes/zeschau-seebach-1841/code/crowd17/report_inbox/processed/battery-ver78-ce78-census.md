# Battery report: ver78-ce78-census

Date: 2026-10-09. Worker: efc23e9a-2738-40fc-8931-aeeb23cabecd (battery worker).
Stream: repaired 1,847-pair parse only (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
Verified in-session: 1,847 pairs, 96 distinct groups, 78 n=31.
`canonical.py` never used. R5005 untouched. Sealed gates / red-team adjudication
queue untouched. Lock `locks/ver78-ce78-census.lock` created 2026-10-09T03:51:25Z
(no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"all 7 'ce [78]' windows re-read under standing values with @364/@1397 recorded
as killed completions and @629 recorded as 'ce ver'+67; the successor-completion
formulation retires iff no window shows a completing successor under its
standing values"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. All 7 'ce [78]' windows are re-read under standing values (independent
   re-derivation, not trust of the predecessor report).
2. @364/@1397 are recorded as killed completions (re-derived, not assumed).
3. @629 is recorded as 'ce ver'+67 (re-derived).
4. The successor-completion formulation retires iff no window shows a completing
   successor under its standing values.

@-offsets below are 0-based pair indices of 78 itself (matching the predecessor
report's convention: 0-based @364 = 1-based position 365).

## Standing values used

Banked GT (pencil): 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que.
Promoted/granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5), 00=pour (A9),
84=on (A15), 47="ce" (A4, allophone tier).
Red-team R17: 12="n" (letter), 48="e" (letter), 30="pas", 06="ent".
Red-team R18: 65=noun class, 92=verb class (subset-scoped), 36=NOUN class.
Provisional: 59=est, 77="le".
Premise (not settled): 78="ver" is a LEAD (R16-005, graded LEAD-not-settled;
untouched by this battery). 45="ce" is HOLD (A11); 45="dict" is a lead
(dict-45-host-inventory battery-promoted 2026-10-09, narrow; verdict45-value
queued separately — coordinated, not duplicated). 67=et/veut is the sole true
polyvalence; positional rule stands. No new value was derived for any cell.

## Census

'ce [78]' defined as: 78 with predecessor in {87, 47, 45} (the 'ce'-valued
groups: 87 promoted, 47 granted A4, 45 hold A11). Re-derived full-stream census:
exactly 7 windows.

## Window-level evidence (standing values only)

### @364 (a2_06): `21 62 48 76 47 78 48 49 61 70 17`
47="ce" (granted), 78="ver" (lead), 48='e' (R17-promoted), 70='pre' (GT),
17='fois' (granted). Reads "... ce ver e [49] [61] pre fois". "vere" is not a
French word (1841 or any period); no French word begins "veres"/"verez"/"veret"
for any 49 reading. KILLED completion (re-derived; agrees with
battery-ver78-ce78-open-succ). The "ce" itself is determiner-shaped.

### @573 (a3_02): `76 45 94 52 87 78 45 13 55 61 94`
87="ce" (promoted), 78="ver" (lead), successor 45. Under standing values
(45="ce", HOLD A11): "ce ver ce" — 45 contributes the word "ce", not a
completing letter. NO completing successor under standing values.
Under the 45="dict" lead: "ce verdict" — word-internal 78+45 composition
("verdict"), determiner "ce" + noun. That reading is determiner-profile, NOT
successor-completion of a ver-word ("ce ver[s/t/e]"). Coordinated with
dict-45-host-inventory (promote, 2026-10-09) and verdict45-value (queued); not
duplicated here. Retirement is robust under either 45 reading.

### @629 (a4_01): `59 37 33 29 87 78 67 08 52 67 63`
87="ce" (promoted), 78="ver" (lead), 67=et/veut (sole polyvalence). Reads
"ce ver" + 67 = 'ce ver'+67 as required. 67 is a following token, not a
completion (positional rule stands; 08's value is open so 67 stays fenced).
Cleanest determiner-profile window: "ce ver" = "this worm", determiner + noun.

### @819 (a5_05): `29 49 74 74 47 78 40 95 13 24 87`
47="ce" (granted), 78="ver" (lead), 40='e' (GT). Reads "ce ver e" = "vere[95]".
"vere" is not a French word; the immediate successor 40='e' is fixed standing
GT and yields no ver-word ("verbe"/"verre"/"verge"/"verve" all need a
consonant 40='e' does not supply). KILLED completion (new finding; same shape
as @364/@1397 with 40 instead of 48). The "ce" is determiner-shaped.

### @982 (a6_01): `00 92 07 76 47 78 45 01 24 89 48`
47="ce" (granted), 78="ver" (lead), successor 45. Identical analysis to @573:
under standing 45="ce" (HOLD), "ce ver ce" — NO completing successor; under the
dict lead, "ce verdict" — word-internal, determiner-profile. Not duplicated
from verdict45-value.

### @1105 (a6_06): `52 82 94 74 47 78 65 63 00 66 73`
47="ce" (granted), 78="ver" (lead), successor 65: VALUE OPEN (65=noun class per
R18/prof-65; no value named). Cannot be evaluated here — awaits 65
(ver78-65-completion queued; its gate is 65's value, not this battery's work).
NOT a shown completing successor.

### @1397 (a7_07): `29 89 16 76 47 78 48 40 67 77 81`
47="ce" (granted), 78="ver" (lead), 48='e' (R17), 40='e' (GT). Reads
"ce veree". "veree" is not a French word ("verre" = v-e-r-r-e needs a second
r that 48='e' does not supply; "verte" = v-e-r-t-e needs 't' in the 48 slot).
KILLED completion (re-derived; agrees with battery-ver78-ce78-open-succ).

## Per-clause pass/fail

1. **PASS.** All 7 'ce [78]' windows re-derived and re-read under standing values
   (@364, @573, @629, @819, @982, @1105, @1397), with wider ±5 context.
2. **PASS.** @364 ("ce vere") and @1397 ("ce veree") recorded as killed
   completions, re-derived byte-by-byte (47="ce" granted, 48='e' R17, 40='e' GT).
   @819 ("ce vere") is an additional killed completion of the same shape.
3. **PASS.** @629 recorded as 'ce ver'+67 (87="ce" promoted; 67=et/veut fenced
   by the standing positional rule).
4. **PASS — formulation retires.** Successor standing values across the 7
   windows: 48='e' (@364 → "vere"), 45="ce" hold (@573/@982 → no completion;
   the dict lead reads "verdict" word-internal, determiner-profile),
   67=et/veut (@629 → not a completion), 40='e' (@819 → "vere"), 65 open
   (@1105 → not shown), 48='e' (@1397 → "veree"). NO window shows a completing
   successor under its standing values. The successor-completion formulation
   ("ce ver[successor]" completing French ver-words) RETIRES.

## Adverses answered

- "@1105 awaits 65": recorded as open, not duplicated. 65's value is open
  (noun class only); ver78-65-completion is the queued venue.
- "78='ver' remains LEAD": untouched. This battery uses the lead as its
  premise and does not re-grade it (R16-005 stands; adj-78-fence fenced the
  adjective rival without touching the lead). No standing verdict contradicted
  or downgraded.

## Surviving content (the claim's positive half)

Every window is consistent with the determiner-profile: "ce" as determiner +
(ver | verdict | ver[65-open]):
@629 "ce ver" clean; @573/@982 "ce verdict" under the dict lead;
@364/@819/@1397 "ce"+"ver" with dead completions (the determiner reading of
"ce" is undisturbed by the completion kills); @1105 "ce ver[65]" awaiting 65.
The 'ce 78' frame's surviving content is the determiner-profile.

## Verdict: PROMOTE

All four bar clauses pass and both listed adverses are answered. This promotes
the census finding (determiner-profile is the frame's surviving content; the
successor-completion formulation retires). It promotes NO value and re-grades
NO lead: 78="ver" stays LEAD, 45="dict" stays lead, 65's value stays open.
Red team has final authority.

## Reproducibility

All offsets and windows re-derived in-session from the repaired 1,847-pair
parse via short inline scripts (parse per repair_parse.py); no script files
written, no writes outside this report, the queue update, and the lockfile.
