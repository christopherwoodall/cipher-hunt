# Battery report: ver78-ce78-open-succ

Date: 2026-10-08. Worker: next-token-supervisor-run/1762522078 (session cd7ba857).
Stream: repaired 1,847-pair parse only (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
Verified: 1,847 pairs, 96 distinct groups. `canonical.py` never used. R5005
untouched (read-only parse; no writes). Sealed gates / red-team adjudication
queue untouched. Lock `locks/ver78-ce78-open-succ.lock` created
2026-10-08T14:08:45Z (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"name 48's and 65's values/frames (coordinate with their batteries; do not
duplicate) and show 'ce ver[48/65]' reading as a ver-word in >=3 of the 4 open
windows (@364, @629, @1105, @1397), or record kill-grade incompatibility"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. 48's value/frame is named from its batteries (no duplication of their work).
2. 65's value/frame is named from its batteries (no duplication of their work).
3. "ce ver[48/65]" reads as a French ver-word in >=3 of the 4 open windows
   (@364, @629, @1105, @1397).
4. (Alternative disjunct) Kill-grade incompatibility is recorded: a window
   forces the claim false under standing values with no lane-legal re-parse.

## Method

Parsed the repaired stream per repair_parse.py. @-offsets are pair indices of
78 itself; ce = 87/47 at -1. All values below are standing only: banked
(11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que), granted (87=ce, 47="ce" A4,
64=qui, 96=par, 17=fois, 79=tout A5, 00=pour A9, 84=on A15), red-team-promoted
R17 (12="n", 48="e", 30="pas", 06="ent"), provisional (59=est, 77="le").
78="ver" is a LEAD (R16-005, graded LEAD-not-settled; ver-78-rebar null
2026-10-08) — the claim's premise, not a settled value. 67=et/veut is the sole
true polyvalence (positional rule stands). No new value was derived for any
cell in this battery.

## Coordination (bars 1-2; no duplication)

- **48:** value = **"e" (letter), red-team promoted** (R17, next-token-redteam-r17.md:
  "Newly promoted: 12="n" (letter), 48="e" (letter), 30="pas" ..."). The A7-L2
  verb-stem frame is narrowed to its two exclusive legs @1229/@1589
  (battery-stem48-exclusive-legs, 2026-10-08); the 48='e' vs stem tension is
  escalated to the red team and NOT re-litigated here. At the four target
  windows the stem48 38-window sweep found no stem parse (@365 "78-48-49"
  letter-e-weak; @1398 "78-48-40" doubtful, no stem parse). Operative reading
  at all four windows: 48='e'.
- **65:** value **open** — prof-65 still queued (priority 3) in
  battery-queue.json; nothing is duplicated from it. Recorded frame evidence
  (queue): noun-leaning — '65 qui' x3 (re-derived on the repaired stream: 65's
  top successor is 64='qui', 3/25), '29-40-65' x3 "[X]ere [65]" direct-object
  slot, '21 65' x4, dominates '-ere' followers. No value is named here.

## Window-level evidence (standing values only)

### @364 (a2_06): `62 48 76 [47=ce]@363 78@364 48@365 49 61 70=pre`
`... ce ver e [49] ...` = **"ce vere[49]"**. "vere" is not a French word; no
French word begins "veres"/"verez"/"veret". 47="ce" is granted (A4),
48='e' is red-team-promoted, 78="ver" is the claim's own premise. No
lane-legal re-segmentation yields a ver-word: "ce"+"ver"+"e" cannot fuse to a
word, and 48='e' cannot start the next word ("e"+"[49]" is not word-shaped at
this frame; 49's value is open and no open value turns "vere[49]" into a word).
The window forces the claim false.

### @629 (a4_01): `37 33 29 [87=ce]@628 78@629 67@630 08 52 67`
`... ce ver et/veut [08] ...` = **"ce ver" + 67**. "ver" (le ver, ce ver =
"this worm") reads cleanly as a French ver-word; 67 is the sole polyvalence
and is a *following token*, not a completion (et = "and", or veut iff 08 is
infinitive-shaped — 08's value is open, so 67 stays fenced per the standing
positional rule). This window reads cleanly at the word level but does not
show a successor *completing* a ver-word — the successor here is 67, outside
the bar's [48/65] notation. Counted as a clean "ce 78"-as-ver-word read, not
as a successor-completion.

### @1105 (a6_06): `82 94 74 [47=ce]@1104 78@1105 65@1106 63 00=pour`
`... ce ver[65] [63] pour ...`. 65's value is open (prof-65 pending), so no
reading can be shown without duplicating that battery's work. Candidate
completions under the "ver"-premise: 65='s' -> "ce vers", 65='t' -> "ce vert";
65='e' -> "ce vere" (not a word). Unresolvable here.

### @1397 (a7_07): `89 16 76 [47=ce]@1396 78@1397 48@1398 40=e@1399 67 77`
`... ce ver e e et/veut ...` = **"ce veree"**. "veree" is not a French word;
no French word begins "veree". 47="ce" granted, 48='e' promoted, 40='e'
banked. The tempting "verre/verte" shapes do not parse: "verre" = v-e-r-r-e
needs a second r that 48='e' does not supply; "verte" = v-e-r-t-e needs the
't' in the 48 slot. The window forces the claim false.

## Adverses answered

- "48/65 values open": **half-stale, answered.** 48's value is NOT open —
  48="e" (letter) is red-team-promoted (R17); the open part is the A7-L2 stem
  frame's narrowed scope (@1229/@1589), which admits no parse at these
  windows. 65's value IS open — prof-65 queued, cited not duplicated.
- "67 is the sole polyvalence": **fenced.** At @629, 67=et/veut is the next
  token after the complete ver-word "ce ver"; the positional rule stands and
  08's shape (which would resolve it) belongs to 08's battery, not this one.

## Per-clause pass/fail

1. **PASS.** 48's value/frame named from its batteries: 48="e" (letter,
   R17-promoted); A7-L2 stem frame narrowed to @1229/@1589, no parse at these
   windows. No work duplicated.
2. **NOT SATISFIABLE HERE.** 65's value is open; prof-65 (priority 3) is still
   queued. Frame named from recorded evidence (noun-leaning: '65 qui' x3
   re-derived, '[X]ere [65]' object slot). No value named, per the
   no-duplication rule.
3. **FAIL at kill grade.** Best achievable: @629 clean word-level read,
   @1105 open (awaits 65), @364 and @1397 force the claim false. 1 + 1 open
   + 2 forced-false does not reach >=3, and the two failures are not
   salvable: under standing values (47="ce" granted, 48='e' promoted, 40='e'
   banked) "ce vere" and "ce veree" are not French words and admit no
   lane-legal re-parse. The only escapes — revising a granted/promoted/banked
   value, or dropping the 78="ver" premise (which voids the claim) — are
   outside this battery's scope.
4. **RECORDED.** Kill-grade incompatibility: @364 and @1397 force the claim
   "the open successors after 'ce 78' complete French ver-words" false under
   standing values.

## Verdict: KILL

The claim is falsified at kill grade by @364 ("ce vere[49]") and @1397
("ce veree"): under standing values neither successor completes a French
ver-word, with no lane-legal alternative. The >=3-of-4 bar is unreachable
(1 clean word-level read @629, 1 open @1105, 2 forced-false).

**Scope of the kill (fenced):** this kills the successor-completion claim only.
It does NOT touch 78="ver" as a LEAD — the 'ce verdict' x2 positives (@573,
@982, conditional on the R16-004 45-lead) and the distributional kill of
78='er' (OR=22.93, Fisher p~2.5e-06) stand untouched. It contradicts no
standing red-team verdict: R16-005 graded 78="ver" LEAD-not-settled (this
battery does not re-grade it), and R17's 48="e" promotion is used, not
downgraded.

## Follow-up targets (narrowed; the residue is real)

1. **ver78-65-completion** (priority 2). Claim: @1105's "ce ver[65]" completes
   a French ver-word once 65 is named. Bars: (a) 65's value taken from
   prof-65's verdict, not re-derived; (b) "ce ver[65]" reads as a French
   ver-word ("ce vers"/"ce vert"/other) under that value — or @1105 is fenced
   as non-completing. Evidence: this report. Adverses: 65 open until prof-65
   lands; 63's value open.
2. **ver78-ce78-census** (priority 3). Claim: the 'ce 78' frame's surviving
   content is the determiner-profile, not successor completion. Bars: all 7
   'ce [78]' windows re-read under standing values with @364/@1397 recorded
   as killed completions and @629 recorded as "ce ver"+67; the
   successor-completion formulation retires iff no window shows a completing
   successor under its standing values. Evidence: this report +
   battery-ver-78.md. Adverses: @1105 awaits 65; 78="ver" remains LEAD.
3. **verdict45-value** (priority 3). Claim: the surviving positive leg for
   78="ver" is 'ce verdict' x2 (@573, @982). Bars: (a) 45's value/frame from
   the R16-004 lead (coordinate, do not duplicate); (b) "ce verdict" reads as
   the French word "verdict" at both windows under standing values — or the
   leg is fenced. Evidence: battery-ver-78.md ('verdict' x4 census).
   Adverses: 45="dict" is a lead, not settled.

## Reproducibility

All offsets re-derived in-session from the repaired 1,847-pair parse via
short inline scripts (parse per repair_parse.py); no script files written, no
writes outside this report, the queue update, and the lockfile.
