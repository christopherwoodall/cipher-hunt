# Battery report: reseg-86-problem-windows

- Target id: `reseg-86-problem-windows`
- Claim: "86 is word-internal (a syllable of a longer word with its neighbors) rather than a standalone token" at the four problem windows #0 @175 ('ce 86 21'), #6 @671 ('la 86 24'), #8 @728 ('pour 86 48'), #7 @716 ('66 86 01')
- Date: 2026-10-09
- Worker: battery worker (subagent db8c1ac6-af29-499e-b063-3e9e6570cf75)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
  n=1847 asserted, 96 groups asserted). `canonical.py` never used.
  R5005, sealed gates, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/reseg-86-problem-windows.lock (created at
  start, deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"for each window (#0 @175 'ce 86 21', #6 @671 'la 86 24', #8 @728 'pour 86 48',
#7 @716), test whether 86 is word-internal (a syllable of a longer word with
its neighbors) rather than a standalone token."

Numbered pass/fail clauses (from the queue follow-up spec, fixed before
testing, not modified after):

1. C1 (@175): 86 is word-internal iff a cleaner multi-group word parse of
   `87 86 21` is demonstrated on bytes using only standing (banked/granted/
   promoted) values; else the standalone assumption stands.
2. C2 (@671): same for `11 86 24`.
3. C3 (@728): same for `00 86 48`.
4. C4 (@716): same for `66 86 01`.
5. The standalone-word assumption is killed per window IFF the cleaner
   multi-group word parse is demonstrated. Adverses answered, not ignored:
   (a) #7's 66-gate question is owned by orphan86-716 (verdict KILL,
   2026-10-08) — adopted as premise, not re-litigated; (b) @552->@553 and
   @888->@889 are confirmed-standalone "pour 86" controls (adopted).

## Method

1. Re-derived the repaired 1,847-pair / 96-type stream in-session; never used
   canonical.py.
2. Read the standing context: stem-86 (verdict null) adjudicated 86 as 4 stem /
   23 whole / 4 orphans / 1 fenced over n=32, and explicitly deferred these four
   windows to this target. 86 = INF class in the banked registry. Letter-level
   hypotheses for 86 in the lane record: 86='t' killed ("pour 86" x12 fails it;
   ver78-296-97gate), 86='s'/'use'/'ux' killed, 86="voi" lead only in
   verb-adjacent contexts (unratified, word-level not syllabic).
3. For each window, attempted to construct a multi-group French word with 86
   word-internal using ONLY byte-grounded neighbor values. Grant constraints
   applied: a word-internal reading that fuses a banked-GT or granted
   standalone word (11='la' pencil GT; 87='ce' granted; 00='pour' granted)
   contradicts standing values and is rejected.
4. Ran the rival-offset phase check on all four rows (see caveat below).

## Window-level evidence (0-based @, re-derived byte-exact)

- #0 @175 (row a1_05): `60 09 87 86 21 69 14` = "...[09] ce(87) [86] [21-noun]
  [69] [14]...". 87='ce' granted standalone; 21 = NOUN class (battery-promote).
- #6 @671 (row a5_00): `20 67 11 86 24 80 03` = "...[67] la(11) [86] [24] [80]
  [03]...". 11='la' banked pencil GT; 24 = finite-modal promoted
  (ne-24-profile) / 'en' red-team conflict.
- #8 @728 (row a5_02): `64 11 00 86 48 88 11` = "...qui(64) la(11) pour(00)
  [86] [48] [88] la(11)...". 00='pour' granted (A9); 48 = inflectional/
  feminine -e (battery promote, function tier).
- #7 @716 (row a5_01): `63 00 66 86 01 02 21` = "...[63] pour(00) [66] [86]
  [01] [02] [21]...". 66 open; 01 general values ('ci'/'faisant') kill-grade
  dead (ci-01-value); bound '-ci' licensed only in ce-contexts (none here).

### Per-window tests

- **#0 @175 — no demonstration possible.** A multi-group word needs 87 ('ce')
  or 21 (noun-class) to be sub-lexical; both contradict standing values
  (87 granted standalone, 21 promoted noun class). No named French word of the
  form ce+[86]+[21] is stateable with byte-grounded values. C1 FAIL.
- **#6 @671 — no demonstration possible.** Needs 11 ('la', banked pencil GT)
  or 24 (promoted finite-modal verb) sub-lexical; both contradict banked GT /
  promoted class. Letter-value routes dead in the lane record (86='t'/'s'
  killed; no candidate yields a French "la"+X word here). C2 FAIL.
- **#8 @728 — no demonstration possible.** Needs 'pour' (granted standalone)
  fused; contradicts the A9 grant. The only sub-lexical-capable neighbor is
  48 (-e): with the standing 86="voi" lead, "pour voie/voire" is
  ungrammatical after "pour"; 86-as-stem + 48-ending is the standing
  "stem-life" of 86 (a standalone word), not a syllable of a longer word.
  C3 FAIL.
- **#7 @716 — no demonstration possible.** 66 open, 01 dead-general/bound-only-
  in-ce-contexts; no named French word spanning 66-86-01 is stateable without
  invented values. The 66-gate route is independently dead (orphan86-716 KILL,
  adopted per adverse). The window stays an orphan under stem-86's
  adjudication. C4 FAIL.

### Phase caveat (stated, not hidden)

All four windows are canonical-offset objects: each dissolves under its row's
rival offset (a1_05: "87 86 21" -> "00 98 78"; a5_00: "11 86 24" -> "06 71 18";
a5_02: "00 86 48" -> "10 08 64"; a5_01: "66 86 01" -> "30 06 68"). The verdict
holds on the canonical stream per protocol; offset adoption is a red-team act.

## Per-clause pass/fail

1. C1 (@175): FAIL — no cleaner multi-group word parse demonstrable; the
   would-be parse contradicts 87's grant / 21's class promote.
2. C2 (@671): FAIL — contradicts banked 11='la' GT / 24's promoted class.
3. C3 (@728): FAIL — contradicts 00='pour' A9 grant; 48-route yields
   ungrammatical French or the standing stem-life.
4. C4 (@716): FAIL — no byte-grounded word nameable; 66-route already killed
   (orphan86-716, adopted).
5. Kill disjunct: NOT FIRED at any window — the standalone-word assumption
   stands at all four. Adverses: (a) ANSWERED — orphan86-716's KILL is the
   premise; the word-internal test is independent and also fails; (b)
   ANSWERED — the @552/@888 "pour 86" controls are consistent with the
   surviving standalone reading.

## Verdict: KILL

The word-internal rival for 86 is dead at all four problem windows: at #0/#6/#8
any word-internal parse contradicts banked ground truth or granted standalone
values (kill grade); at #7 no French word is nameable without invented values.
The standalone assumption survives. #7 remains a residual orphan under
stem-86's adjudication. No polyvalence declared; §7 intact. No standing or
red-team verdict contradicted or downgraded. No follow-ups proposed (kill,
not null).
