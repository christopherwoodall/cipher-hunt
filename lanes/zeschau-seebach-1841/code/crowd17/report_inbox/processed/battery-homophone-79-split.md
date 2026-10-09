# Battery verdict: homophone-79-split

**Target:** `homophone-79-split` (priority 2)
**Date:** 2026-10-09
**Worker:** 921fc461-41bb-4093-93d3-d76a895e6a43 (clean re-run; prior worker died
in a runtime restart before producing anything; its lock was cleared)

## Bar (verbatim from battery-queue.json)

> distributional test per the {33,86} precedent; section 7 - needs red-team
> declaration, do not declare at battery level

Numbered clauses:
1. Distributional test per the {33,86} precedent: classify every 79 window as
   W (grammatical as independent word 'tout'), S (requires a word-internal /
   syllabic reading of 79), or O (open — compatible with either); report the
   partition with byte offsets.
2. Section 7 compliance: gather evidence and escalate only. Do NOT declare any
   polyvalence or homophone split at battery level.

Adverses (must be answered, not ignored): section 7 sole-polyvalence
(67 et/veut only); battery gathers evidence, escalates.

## Method

Read BATTERY-PROTOCOL.md first; created
`code/crowd17/next-token/locks/homophone-79-split.lock` on start. All counts
re-derived from the repaired 1,847-pair stream
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py`; verified 1,847 pairs /
96 types; `canonical.py` never touched). R5005, sealed gates, and the
red-team queue untouched. 1841 diplomatic French throughout.

Precedent mirrored: the 86 battery (`processed/battery-split-86-amended-rule.md`)
partitioned all 32 windows into D/V lives with mutual exclusivity and promoted
the RULE (not the split). Here the analog is a W/S partition of 79's 18
windows; the split declaration stays a red-team act.

## Window-level evidence (all 18 windows of 79, 0-based @-offsets)

Context key: GT = ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que); promoted = 87=ce, 64=qui, 96=par, 17=fois, 00=pour, 84=on, 47=ce,
48=e; provisional = 59=est, 77=le.

### W-family: grammatical as independent word 'tout' (9 windows)

- @50 `00 92 [79] 37 11` (a1_01): "pour [92], tout [37] la" — 'tout' as subject
  pronoun ("everything") of 37. Conditional on 37 finite-verb-shaped.
- @396 `67 64 [79] 82 48` (a2_07): "qui tout me [48-verb]" — the granted A7-L2
  frame "tout me [48-verb]".
- @460 `14 02 [79] 87 11` (a2_10): "[02] tout cela" (87=ce, 11=la) — "tout cela"
  ("all that"), clean.
- @468 `00 33 [79] 80 06` (a2_10): "pour [33] tout [80]" — "pour dire tout"
  (verb + object pronoun "everything"). Conditional on 33 verbal.
- @594 `00 92 [79] 85 01` (a4_00): "pour [92] tout [85]" — "pour tout [inf]"
  ("pour tout dire" pattern). Conditional on 85 infinitive-shaped and 92
  left-attaching.
- @1089 `00 33 [79] 80 06` (a6_05): same shape as @468.
- @1227 `57 64 [79] 82 48` (a7_01): "qui tout me [48-verb]" — A7-L2 again.
- @1682 `00 46 [79] 65 13` (a8_05): "pour que tout [65]" (46=que) — 'tout' as
  subject pronoun, "for everything to [verb]". Conditional on 65 verbal.
- @1799 `37 91 [79] 87 64` (a8_10): "[91] tout ce qui" (87=ce, 64=qui) —
  "tout ce qui" ("all that which"), clean.

### S-family: ungrammatical as independent word 'tout' (4 windows)

- @53 `37 11 [79] 85 58` (a1_01): "[37] la tout [85]" — the s5-la-tout-adjudicate
  clash: "la tout" is kill-grade ungrammatical (article la (fem.) + tout
  (masc.); no clitic, ellipsis, or boundary rescue; offset 0 is bedrock
  PROBABLE). Requires a word-internal reading of 79.
- @451 `32 48 [79] 17 77` (a2_10): "[32]e tout fois le" (17=fois) — "tout fois":
  adverb 'tout' + feminine noun needs "toute"; determiner 'tout' + "fois"
  needs "toute"; pronoun 'tout' cannot precede a noun. Unrescuable as a word.
- @1419 `32 84 [79] 15 33` (a7_08): "[32] on tout [15] [33]" (84=on, promoted
  A15) — "on tout [verb]" is not a French constituent (adverb 'tout' never
  modifies a finite verb directly; *"on tout homme" impossible).
- @1460 `86 66 [79] 17 01` (a7_09): "[66] tout fois [01]" — "tout fois", same
  failure as @451. Note @451/@1460 share the "tout fois" shape (2-window
  shape, not a singleton).

### O-family: open, compatible with either (5 windows)

- @496 `94 02 [79] 88 47` (a2_11), @883 `08 31 [79] 68 37` (a5_08),
  @1010 `35 18 [79] 80 78` (a6_02), @1364 `62 94 [79] 14 60` (a7_06),
  @1688 `62 94 [79] 14 60` (a8_05) — unvalued neighbors on both sides in each;
  no grammatical verdict possible yet. (@1364/@1688 share a shape.)

### Distributional signature

- The S-family is 4/18 (22%) — too large for a hapax fence (contrast the lone
  @53 clash, which s5 fenced as a single-window contradiction).
- Follower 17=fois occurs 2/2 in S-windows (@451, @1460), 0/9 in W-windows:
  the "tout fois" shape is the cleanest distributional marker of the S-life.
- Predecessor 11=la occurs 1/1 in S (@53), 0 elsewhere.
- Follower 85 occurs in both lives (@53 S, @594 W) — does not discriminate.
- The W-family's conditionals rest on unvalued neighbors, symmetric with the
  86 precedent's caveat ("V-class label rests on lane-granted values; the
  byte facts stand").

### Observation for the red team (not a finding)

@451/@1460 "tout fois" is one 'e' away from "toutefois" ("however"):
79='toute' + 17='fois' would read cleanly. That is a VALUE variant
('tout'/'toute' allomorphy), not the syllable split tested here; recorded
only because it bears on how the red team names the S-life.

## Per-clause results

**Clause 1 (distributional test): PASS.** All 18 windows classified:
W=9 (@50, @396, @460, @468, @594, @1089, @1227, @1682, @1799),
S=4 (@53, @451, @1419, @1460),
O=5 (@496, @883, @1010, @1364, @1688).
The partition is bimodal: no W-window requires a syllabic reading, no
S-window parses as word-'tout'. Monovalent word-'tout' fails on 4 windows
(22%); the split hypothesis SURVIVES the distributional test. It is not
exceptionless (5 O-windows remain), so no battery-level rule promotion is
warranted — unlike the 86 case (32/32 assigned).

**Clause 2 (Section 7): PASS.** No polyvalence or homophone split is declared.
Evidence gathered; escalation below.

## Adverses

- Section 7 sole-polyvalence (67 et/veut only): honored. No second
  polyvalence declared; the 79 split is a red-team candidacy, presented with
  the partition evidence.
- The standing 79="tout" promotion (A5) is NOT contradicted for the W-family
  (9 windows, incl. 2 clean legs @460/@1799 and the granted A7-L2 frame);
  the S-family is new split-candidacy evidence, escalated per the brief.

## Verdict: NULL

The distributional test is positive (bimodal W/S partition, split hypothesis
survives), but declaring the split is a red-team act per Section 7.
**Headline for the red team:** 79's 18 windows partition 9 / 4 / 5
(word-'tout' / requires-syllabic / open). Four windows (@53 "la tout" clash,
@451/@1460 "tout fois" x2, @1419 "on tout [15]") are ungrammatical under the
banked word-'tout' value. Either 79 needs a declared homophone split
(word-'tout' vs syllable-'tout'), or four independent rescues are owed.

## Follow-ups (null regenerates work)

1. `redteam-79-split-docket` (P1, red-team venue): present the W/S/O partition
   (9/4/5 with @-offsets); ask the red team to declare or reject the 79
   homophone split; include the 'toute'/"toutefois" allomorph observation for
   @451/@1460.
2. `syl79-wordname` (P2): name the multi-group words containing syllabic 79
   at @53 ("la tout[85]"), @451/@1460 ("tout fois"), @1419 ("on tout[15]")
   as neighbor values resolve.
3. `o79-adjudicate` (P3): adjudicate the 5 O-windows (@496, @883, @1010,
   @1364, @1688) as neighbors resolve; S-growth strengthens the split,
   W-growth weakens it.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-homophone-79-split.md` (this file)
- Queue: `battery-queue.json` — target `homophone-79-split` → status
  `verdict`, result `null`, date 2026-10-09 (own entry only, temp-file +
  rename; pre-write assert confirmed no prior verdict, no downgrade)
- Lock `locks/homophone-79-split.lock` created on start with agent id +
  UTC timestamp, deleted on completion.
