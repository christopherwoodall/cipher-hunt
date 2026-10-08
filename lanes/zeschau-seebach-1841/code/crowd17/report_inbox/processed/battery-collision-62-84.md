# Battery report: collision-62-84 (62/84 "on" collision)

Worker: 4d9b44cc-4525-4147-9bbb-2488ac07964f. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005 never touched.

## Bar (verbatim, pre-registered)

"resolve iff exactly one of {62,84} holds 'on' unconditioned, with the loser's
frames re-read cleanly"

Numbered clauses:

1. Exactly one of {62,84} holds 'on' unconditioned.
2. The loser's frames re-read cleanly.

## Method

Re-derived every count below from the repaired stream with a fresh parse
(no prior counts trusted). Checked: 62 successor census (n=35), 84 successor
census (n=25), crossover matrix 62->{59,94} x 84->{59,94}, elision-context
predecessor inventory for 62 vs 84, all nine 62->94 windows under the 'il'
rival, all four 84->59 windows under 'on', the 21->62 x5 adverse windows,
62->48 x6, '20 62 94' x3, and '62 n'est 39' @762.

## Window-level evidence (@-offsets, repaired stream)

62->94 x9 (re-derived): @100, @508, @761, @840, @1329, @1362, @1686, @1704,
@1772. 84->59 x4 (re-derived): @1189, @1290, @1447, @1803.
Crossover: 62->59 x0, 84->94 x0. Zero crossover confirmed.

84='on' legs (re-derived, not re-litigated): 77->84 x7 (@145, @259, @1057,
@1446, @1484, @1763, @1802) = 'l'on' x7; 46->84 x2 = 'qu'on' x2 (46='que'
banked). Elision-context predecessors: 84 has 9 (77x7 + 46x2); 62 has 1
(77x1 @508). 62 never follows 46='que' (0/35) — 'qu'on'/'qu'il' x0.

62->94 windows under 'il ne' (94='ne' promoted):
- @100 (a1_02): "08 21 62 94 93 59 45" = "[08] [21] il ne [93] est [45]".
  Indirect frame (same F7 window as verb-93 evidence). Parses no worse than
  'on'. Clean.
- @761 (a5_03): "20 62 94 59 39" = "[20] il n'est [39]". 'ne' elides before
  59='est' (provisional). Clean. (@760 '20 62 94' frame; @762 '62 n'est 39'
  nest-subject window — same reading.)
- @840 (a5_06): "20 62 94 26 12" = "[20] il ne [26] n…" Clean.
- @1329 (a7_04): "06 62 94 70 52" = "[06] il ne pre[70]…" Clean.
- @1362 (a7_06): "92 62 94 79 14" = "[92] il ne tout[79]…" Clean.
- @1686 (a8_05): "93 62 94 79 14" = "[93] il ne tout[79]…" Clean.
- @1704 (a8_06): "20 62 94 88 26" = "[20] il ne [88]…" Clean.
- @1772 (a8_09): "78 62 94 24 87" = "[78] il ne [24] ce[87]…" Clean.
- @508 (a3_00): "67 77 62 94 64 98" — RESIDUAL (see fencing). Left edge:
  "le il ne" is ungrammatical under provisional 77='le' ("l'on ne" would be
  clean). Right edge: "94 64" = "ne qui" is ungrammatical under BOTH 'il'
  and 'on' (64='qui' granted). The window is anomalous regardless of the
  rival; single window of 35. Fenced with stated cause, not ignored.

84->59 windows under 'on est': @1189 "84 59 46" ('on est que' — 46='que'
banked); @1290, @1447, @1803 all 'on est [X]' with clean predicative tails.
All four clean.

## Adverses (answered, never ignored)

A1. "21-62 x5 wrinkle" — ANSWERED by re-parse. All five re-derived on the
repaired stream: @99, @359, @1064, @1463, @1538. @99 = @100 window above
('il ne' indirect frame, clean). @359 "11 21 62 48" ('la [21] il e…'),
@1064 "96 21 62 18" ('par [21] il [18]'), @1463 "01 21 62 48" — each parses
under 'il' exactly as well as under 'on' (21's value is open in both;
symmetric strain, non-discriminating). @1538 "62 06 21 62 93" doubles the
pronoun under BOTH readings (odd under 'il' and under 'on' alike).
Verdict on A1: the wrinkle does not discriminate; fenced with stated cause.

A2. "A15 battery never mentioned the 62 lead (scope gap)" — ANSWERED by
fencing with stated cause. The A15 red-team adjudication scoped to 84's
legs only; this battery is the chartered C2 gap-fill. 84's legs were
re-derived independently above (77-84 x7, 84->59 x4); no contradiction with
A15 was found. The gap is now filled.

## Consistency with queued targets (per brief)

- 62 top predecessor of 48 x6: re-derived @360, @425, @1315, @1349, @1464,
  @1569. Under 62='il' + 48='e' (letter, promoted): "il e…" — mixed
  word/letter sequences are attested in the lane (70-12-94 = "pre"+"n"+
  "ne"). No forced contradiction. Consistent.
- frame-20-62-94 ('20 62 94' x3 @760/@839/@1703): "[20] il ne" leaves 20's
  value untouched; nothing forced that breaks the queued frame. Consistent.
- nest-subject-86-62-42 ('62 n'est 39' @762): "il n'est [39]" is
  subject-shaped. Consistent.
- Concurrent finder beat "84-adjudication inputs" (still queued) expects
  exactly these inputs: 62 profile under the 'il' rival vs 84
  elision-discriminated. This report's censuses and @-offsets are directly
  usable by it. Not waited for, per brief.

## Per-clause pass/fail

1. Exactly one of {62,84} holds 'on' unconditioned — PASS. 84='on' holds
   (A15 grant, legs re-derived). 62='on' unconditioned is eliminated: the
   lane's sole-polyvalence rule (§7: 67 et/veut is the sole true
   polyvalence) forbids a second unconditioned 'on', and the A15 grant
   cannot be overturned at battery level. Exactly one = 84.
2. The loser's frames re-read cleanly — PASS. 62's nine '62 94' frames
   re-read as 'il ne': 8 clean, 1 (@508) fenced as residual with stated
   cause (anomalous under both rivals; single window of 35).

## Verdict

KILL — kill-grade resolution of the collision. The 62='on' side is
eliminated: 62='on' unconditioned is killed by the §7 polyvalence rule
against the standing A15 grant, and the cleaner rival 62='il' is
demonstrated on the same nine frames (8 clean + 1 fenced residual).
84='on' holds 'on' unconditioned. A15-C2 is resolved.

Note: 62='il' is DEMONSTRATED as the rival here, not promoted — an 'il'
promotion needs its own battery with its own bars. Note for the red team:
@508 ("77 62 94") is the one window where a conditioned 62='on'
(elision-context only) would read cleanly; declaring that would be a
second polyvalence, which is a red-team act, not a battery act.

## Standing-constraint check

- 84="on" is an A15 grant with conditions C1-C3: this battery resolves C2.
  C1 (77='le' provisional) and C3 (R1/R2 fenced residuals) are untouched.
- 62='on' was a standing STRONG LEAD, never a grant: killing it does not
  contradict any red-team verdict. No escalation required.
- No R5005 contact, no sealed gates, no red-team queue writes.
