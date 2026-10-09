# Battery report: reseg-13-armB

Target: `reseg-13-armB`. Claim: "the same leftward nominal-closing 13
re-segments all 7 arm-B windows (@139/@456/@481/@567/@575/@1166/@1360)".
Date: 2026-10-09. Worker: subagent (battery worker).
Lock `locks/reseg-13-armB.lock` created 2026-10-09T15:30:00Z (no
pre-existing lock for this id); deleted on completion.

Offset convention: @n = 0-based pair index in the repaired 1,847-pair
stream.

## Bar (verbatim, pre-registered)

"(a) state the nominal closed leftward per window with standing values
— hard cases '00=pour [13] 52' (@481) and '45=ce [13] 55' (@575/@1166);
(b) any window forcing a word-level 13 kills the uniform-suffix account."

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. For each of the 7 arm-B windows, the nominal that 13 closes
   leftward is stated using standing values only (protocol §7 +
   registry; battery leads marked as leads, class-open cells marked,
   nothing invented). The two named hard cases must be resolved, not
   skipped.
2. Falsifier: if ANY window forces a word-level 13 (no standing-value
   parse admits 13 as sub-lexical), the uniform-suffix account is
   killed.

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired 1,847-pair
stream independently from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py` (asserted 1,847 pairs / 96 types
before testing). n(13)=12, loci byte-exact:
@68/@139/@456/@481/@567/@575/@822/@1166/@1360/@1381/@1554/@1684 —
5 arm-A + 7 arm-B, matching R20-106's partition. `canonical.py`
never used. R5005, sealed gates, red-team queue untouched. Every
number traces to the stream.

Standing values used (§7 + registry): GT letters 11=la, 82=m, 34=i,
29=er, 40=e, 46=que; 00="pour" (A9, registry ["pour","prom"]);
45="ce" (hold A11, registry ["ce/dict","lead"]); registry classes
65=["noun","cls"], 35=["noun","cls"], 76=["noun","prom"],
24/92/93=["verb","cls"]. Class-open: 52, 55, 66, 97 (INF/NOM-tied),
99, 95. 13's gloss open (sub-lexical, per R19-170).

## Window-level evidence (all 7, re-derived)

Legend: `[X]-13` = proposed leftward nominal-closing.

### @139 (a1_04) — STRONG
`... 65 [13] 66 14 ...` (full: @134:21 @135:65 @136:23 @137:91 @138:65
@139:13 @140:66 @141:14 @142:74 @143:67 @144:64)
- Left: 65=["noun","cls"] (registry). 13 closes "[65]-13" leftward.
- Follower 66 class-open; irrelevant to the leftward bar.
- Nominal stated with a registry-known noun. STRONG.

### @456 (a2_10) — STRONG
`79 17 77 60 65 [13] 66 14 02 79 87` (@451–@461)
- Left: 65=["noun","cls"]. 13 closes "[65]-13" leftward. Same
  "65 13 66 14" frame as @139 (byte-exact 4-gram "65 13 66 14" x2
  stream-wide — the only repeat of any "X 13 Y Z" frame).
- STRONG. (Left context 79=tout, 17=fois, 77=le provisional noted;
  not needed for the bar.)

### @481 (a2_11) — HARD FAIL (named hard case)
`78 74 45 93 00 [13] 52 30 01 19 64` (@476–@486)
- Left: 00=["pour","prom"] (A9). A nominal-closing suffix cannot
  attach to the preposition "pour" — no nominal ends at @480 under
  standing values. The wider left context (45="ce" @478, 93=verb
  class @479) forms no nominal phrase terminating at 00.
- Stress test — nominal "pour" ("peser le pour et le contre"):
  rejected. No determiner precedes 00 (@479=93 verb class), no
  standing license puts nominal "pour" here, and it would need 13's
  gloss invented on top. Two inventions; bar demands standing values.
- No nominal statable. The leftward-suffix parse is excluded at
  @481. (Remaining live options: rightward "pour [13-52]" with
  class-open 52, or word-level 13 — neither forced; see clause 2.)

### @567 (a3_02) — CONDITIONAL ADMIT
`11 43 24 80 97 [13] 76 45 94 52 87` (@562–@572)
- Left: 97, registry-ABSENT, INF/NOM-tied (class open). IFF 97 is
  nominal, 13 closes "[97]-13" leftward; follower 76=["noun","prom"].
- Same admissibility standard as arm-A's 69/95/99 legs
  ("compatible-not-proven"): no standing value forces 97
  non-nominal. CONDITIONAL on the tie resolving nominal. If 97
  resolves infinitive-shaped, this window joins the hard fails.

### @575 (a3_02) — HARD FAIL (named hard case)
`94 52 87 78 45 [13] 55 61 94 82 06` (@570–@580)
- Left: 45=["ce/dict","lead"] (hold A11), DIRECTLY adjacent to 13.
  A nominal suffix cannot attach to the determiner "ce". Unlike
  arm-A @1554 ("45=ce 23 [99]-13", where 13 attached to 99 with 45
  as the NP's determiner), there is no X between 45 and 13 here —
  13 would have to suffix onto "ce" itself, which French does not
  license and the lane's own arm-A precedent does not do.
- No nominal statable. Excluded. (Live options: rightward
  "ce [13-55]" with class-open 55, or word-level 13; neither
  forced — see clause 2.)

### @1166 (a6_09) — HARD FAIL (named hard case)
`83 21 67 78 45 [13] 55 61 94 87 83` (@1161–@1171)
- Left: 45=["ce/dict","lead"], directly adjacent to 13 — byte-same
  "45 13 55" trigram as @575 (the only two "45 13 55" in the
  stream). Same exclusion: no nominal statable; 13 cannot suffix
  onto "ce".
- Excluded. (Live options as @575.)

### @1360 (a7_06) — STRONG
`06 52 37 64 35 [13] 92 62 94 79 14` (@1355–@1365)
- Left: 35=["noun","cls"] (registry). 13 closes "[35]-13"
  leftward. (Left context 37 predicative frame (A1) + 64=qui GT:
  "est [37-pred] qui [35]-13" — grammatical shape, not asserted as
  the parse.)
- STRONG. (Right successor 92=["verb","cls"] noted; the right leg
  is outside this bar. Observation: R20-106's "seven arm-B windows
  carry non-verb successors" does not count 92 as verb-class here —
  flagged for the red team, not litigated; immaterial to the bar.)

## Per-clause pass/fail

1. **FAIL AT KILL GRADE.** Bar (a) requires the nominal stated per
   window. Three of seven windows admit no leftward-nominal-closing
   parse under standing values:
   - @481: left neighbor is the preposition "pour" (00, A9) —
     a nominal suffix has no host.
   - @575, @1166: left neighbor is the determiner "ce" (45, A11),
     directly adjacent — a nominal suffix has no host, and the
     arm-A precedent (@1554) attached 13 to the following noun,
     not to 45.
   The universal claim ("re-segments ALL 7") is thereby forced
   false: standing values positively exclude the required
   segmentation at three windows. This is not inconclusive — it is
   a demonstrated falsification. 3 strong (@139/@456/@1360),
   1 conditional (@567), 3 hard fails.
2. **NOT TRIGGERED (by its letter).** No window forces a
   word-level 13 specifically: at @481/@575/@1166 the live
   alternatives are rightward attachment ("pour [13-52]",
   "ce [13-55]" — 52/55 class-open, admissible, unproven) versus
   word-level 13, and nothing in standing values selects between
   them. The kill arrives via clause 1, not clause 2.

## Adverses answered

- **66/52/92 class-open: ANSWERED.** The bar is leftward; the
  followers' classes are immaterial. The kill rests on the LEFT
  neighbors (00, 45), whose values are standing (A9, A11), not on
  any open class.
- **13's gloss still open: ANSWERED (acknowledged).** This battery
  tests segmentation uniformity only, exactly as arm-A did. The
  suffix's value remains sub-lexical and unnamed; the kill does not
  depend on it.

## Scope

Kills ONLY the uniformity claim — "the SAME leftward
nominal-closing 13 re-segments ALL 7 arm-B windows". Untouched:
(a) the three strong windows (@139/@456/@1360) and the conditional
(@567) still individually admit 13-as-leftward-suffix — a narrowed
4-window suffix battery remains viable; (b) arm-A's R19-170/R20-106
grant (conditional segmentation at @68/@822/@1381/@1554/@1684) is
not contradicted — this report concerns arm-B uniformity only;
(c) no value named, no class changed, no registry delta. No
standing/red-team verdict contradicted or downgraded; §7 intact.

## Verdict: KILL

The uniform-suffix account is falsified at kill grade. Bar (a)
fails at three of seven windows: @481 ("pour [13] 52") and
@575/@1166 ("ce [13] 55" x2) admit no leftward-nominal-closing
parse under standing values — the immediate left neighbor is the
preposition "pour" (A9) or the determiner "ce" (A11), neither of
which can host a nominal suffix. The claim's universal quantifier
is forced false. 13 may still be a leftward suffix at
@139/@456/@1360 (registry-known noun predecessors) and
conditionally at @567 (iff 97 is nominal), but it is NOT uniform
across arm-B.

## Recommendations for the supervisor (not queued by this worker)

1. **reseg-13-rightward** (P3): test rightward attachment at the
   three killed windows — "pour [13-52]" (@481), "ce [13-55]"
   (@575/@1166) — with 52/55 class-open; bar: name the host word
   or fence the rightward arm.
2. **suffix-13-narrow** (P4): re-test the 13-suffix segmentation on
   the four admitting windows (@139/@456/@567/@1360) toward naming
   13's sub-lexical value; bar: value named with byte evidence or
   fence.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-reseg-13-armB.md`
- Queue: `reseg-13-armB` → `status: verdict`, `result: kill`,
  2026-10-09 (pre-write assert passed — was queued/verdictless;
  temp-file + rename; disk re-read confirms verdict/kill; own
  entry only; no downgrade)
- Lock created on start, deleted on completion. R5005, sealed
  gates, red-team adjudication queue untouched.
