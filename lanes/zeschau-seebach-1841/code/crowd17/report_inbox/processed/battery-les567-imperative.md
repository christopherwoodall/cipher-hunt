# Battery report: les567-imperative

Target: `les567-imperative`. Claim: @567 re-segments as "[97-imperative] les!"
+ new clause "[76] ce...", reviving a local pronoun parse.
Date: 2026-10-09. Worker: 73cae17c-278b-4e59-86ba-0dfb76415b10 (battery worker).
Lock `locks/les567-imperative.lock` created 2026-10-09T09:05:36Z (no pre-existing
lock for this id); deleted on completion.

Offset convention: @n = 1-based pair index in the repaired 1,847-pair stream
(prior battery pronoun-13-les used 0-based; its "@567" = 13's window = @568 here;
97 sits immediately left at @567 here, row a3_02 in both conventions).

## Bar (verbatim, pre-registered)

"name 97's class independently (>=3 windows, zero contradictions); imperative
iff 97 is verb-shaped - kill iff 97 is nominal/infinitive ('pour [97]' x4 is
the standing counter-evidence)"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. 97's class is named independently from >=3 windows with zero contradictions
   under standing values.
2. The imperative reading is licensed iff C1 names a verb-shaped class for 97;
   the claim is KILLED iff 97 is nominal or infinitive-only.

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired 1,847-pair / 96-type
stream in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py` (asserted 1,847 pairs / 96 types before
testing). `canonical.py` never used. R5005, sealed gates, red-team queue
untouched. Every number traces to the stream. Standing values per protocol
§7 (pencil GT, granted, provisional) plus adopted battery premises noted
where used (not re-litigated).

97, n=10, 1-based windows: @3, @95, @289, @300, @526, @567, @589, @752,
@1413, @1824.

## Window-level evidence (independent class census of 97)

- @3 (a1_00): `09 00 97 51 47 41` = "[09] pour(00) [97] [51] ce(47) [41]".
  pour-slot: noun or infinitive. Unforced.
- @95 (a1_02): `98 81 97 46 29 85` = "[98] [81] [97] que(46) er(29) [85]".
  Two readings: "[81] [97-noun] que [verb]" (relative, needs 81 determiner-ish)
  vs "[81-subj] [97-verb] que [verb]" (complement, needs 81 subject). 81's
  class is open, so the window is unforced; nominal-consistent.
- @289 (a2_03): `00 97 09 64 29 40 65` = "pour(00) [97] [09] qui(64)
  [29][40][65]". Adopted premise (rel-09-290, verdict on queue): clean
  relative clause "pour [97] [09] qui [verb]". If 97 were the infinitive,
  "pour [inf] [09] qui [verb]" strands 09 and leaves "qui" antecedentless:
  ungrammatical at kill grade. The noun arm parses clean. **Forces 97
  NOMINAL** (antecedent-NP zone) under standing values (64=qui granted,
  00=pour A9, 65=noun-class R18).
- @300 (a2_04): `78 40 97 86 91 18` = "[78] e(40) [97] [86] [91] [18]".
  If 86 is V-life (86 split fenced, V arm live), "[97] [86-verb]" needs a
  subject: nominal-consistent. No verb-forcing frame. Nominal-consistent.
- @526 (a3_00): `81 97 47 44 59 37` = "[81] [97] ce(47) [44] est(59) [37]".
  "ce [44] est [37]" is a clean A1 copula clause. The verb reading of 97
  ("[81-subj] [97-verb]") leaves "ce [44] est" as a second clause with no
  conjunction: unmotivated. The noun reading ("[81] [97-noun]" dislocated/
  appositive NP + copula clause) is natural. Nominal-consistent.
- @567 (a3_02): `80 97 13 76 45 94` = "[80] [97] [13] [76-noun] ce(45)
  ne(94)". Test locus; class assessed from the other nine windows.
- @589 (a3_02): `00 97 41 41 09` = "pour(00) [97] [41] [41] [09]".
  pour-slot: noun or infinitive. Unforced; §7 extends the @289 nominal.
- @752 (a5_03): `02 97 40 67 11` = "[02] [97] e(40) [67] la(11)". The only
  verb-shaped leg anywhere: "fait [97-inf]" causative, but conditional on
  02='fait', which is a fenced NULL (adv-02-858: 'fait' packaged as
  conditioned candidate, 3 hard contradictions elsewhere), not a standing
  value. Unforced under standing values; recorded, not usable.
- @1413 (a7_07): `16 97 69 74 34` = "[16] [97] ce(69) [74] i(34)". 16 and 74
  class-open. Unforced; nominal-consistent.
- @1824 (a8_11): `00 97 00 86 29` = "pour(00) [97] pour(00) [86] er(29)".
  pour-slot: noun or infinitive. Unforced; §7 extends the @289 nominal.

Follower census of 97: {51, 46, 09, 86, 47, 13, 41, 40, 69, 00} — zero
verb-forcing governors. Predecessors: 00 x4, 81 x2, 40, 80, 02, 16 — zero
verb-forcing frames under standing values.

## Per-clause results

- **C1: PASS.** 97 = NOMINAL, named independently: forced at @289
  (kill-grade relative-antecedent evidence), consistent at @95/@300/@526/
  @589/@1413/@1824, zero contradictions under standing values. The sole
  verb leg (@752) is conditional on the fenced 02='fait' and cannot stand
  as independent class evidence.
- **C2: KILL fires.** 97 is nominal, not verb-shaped. The imperative
  "[97-imperative] les!" is unlicensed at kill grade.

## Adverses answered

- ADV1 ("00->97 x4"): answered, not ignored. "pour [97]" x4 is
  noun/infinitive-ambiguous; @289's "pour [97] [09] qui [verb]" frame
  selects the noun arm at kill grade (the infinitive arm is ungrammatical
  there), and §7's one-value rule extends nominal to the other three.
  The x4 is consistent with the kill, not counter-evidence against it.
- ADV2 ("§7 one-value rule bars a local imperative exception"): answered.
  §7 applies on top of the class finding: 97 is nominal at @289 at kill
  grade, so a verb-shaped imperative at @567 would be a second value for
  the cell — barred. This converges with (does not duplicate)
  pronoun-13-les's original rejection of attempt (i).

## Further note (not a finding)

The re-segmentation fails twice over: 97 is nominal (this battery), and
13='les' object pronoun was already killed at kill grade (pronoun-13-les),
so the "les!" half is independently dead. @567's parse remains: 76 is a
promoted noun that cannot host a preverbal clitic.

## Verdict: KILL

Headline: the "[97-imperative] les!" re-segmentation at @567 is dead at
kill grade. 97 is nominal (forced at @289, zero contradictions across all
10 windows); the imperative requires a verb-shaped 97 that does not exist.
Per the bar's kill clause, the claim is killed. No standing or red-team
verdict contradicted; §7 intact; no downgrade. Kill verdicts do not
regenerate follow-ups per protocol §4; 97's nominal value remains unnamed
(an observation for the supervisor, not a mandated target).

## Bookkeeping

- Queue: `les567-imperative` → status `verdict`, result `kill`, date
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; JSON re-validated; own entry only; 931+ targets intact).
- Lock created on start, deleted on completion (verified gone).
- `canonical.py` never used; R5005, sealed gates, red-team adjudication
  queue untouched.
