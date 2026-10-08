# Battery report: adj-60 (60 = masculine adjective)

Worker: 987f7f45-470d-4914-b8b6-1785246233a2. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py.
canonical.py never used. R5005 never touched. @i = 0-based pair index.
No red-team verdict on 60 exists (checked
code/crowd15/report_inbox/next-token-redteam.md) — no contradiction, no
escalation of a standing verdict.
No prior lock on adj-60 (no stale lock to note).

## Bar (verbatim, pre-registered before testing)

"promote iff 'le [60-adj] [65-N]' @454 plus >=2 of the @690/@1644/@1674 '[60] [03-N]' frames cohere with 65 and 03 nominal (both independently supported: '65 qui' x3 @724/@1208/@1340; 'le [03]' @722, 'ce [03]' @1014/@1790 via 47='ce') and zero contradictions"

Numbered clauses (fixed before data examination):

1. (C1) 'le [60-adj] [65-N]' @454 parses with 60 as masculine adjective
   and 65 nominal, using only independently-supported anchors.
2. (C2) At least 2 of the 3 '60 03' windows (@690, @1644, @1674) parse as
   '[60-adj] [03-N]' with 60 adjectival and 03 nominal, using only
   independently-supported anchors.
3. (C3) 65 and 03 are nominal on independent evidence: '65 qui' x3
   (@724/@1208/@1340); 'le [03]' @722; 'ce [03]' x2 (@1014/@1790).
4. (C4) Zero contradictions across all 18 windows of 60, and the listed
   adverses answered: @1338 ('qui 60 08') and @700 ('ne 60 12') re-parse
   under the adjective claim, or are fenced with stated cause.

## Method

Fresh parse per protocol. No prior counts trusted (all numbers below are
re-derived). 60 n = 18 on the repaired stream (@119, 172, 197, 232, 322,
454, 637, 690, 700, 995, 1338, 1366, 1474, 1563, 1644, 1674, 1690, 1735).
Standing values used: 64='qui' (red-team granted), 47='ce' (A4 granted),
77='le' (provisional), 59='est' (provisional), 94='ne' (battery-promoted),
12='n' (letter, battery-promoted), 06='ent' (battery-promoted), 67
positional rule (67='veut' iff follower infinitive-shaped).

## Window-level evidence

W1 — 'le [60-adj] [65-N]' @454 (row a2_10):
@448 59 @449 32 @450 48 @451 79 @452 17 @453 77 @454 60 @455 65 @456 13
Reads: "...est[59] [32] e[48] tout[79] fois[17] le[77] [60] [65] [13]..."
Under 60 = masculine adjective: "le [adj] [65-N]" parses cleanly with
77='le' (provisional) as the only assumption. '77-60' x1 and '60-65' x1
on the stream — this frame is unique. 65 nominal is independently
supported (see anchors). PASS.

W2 — '60 03' @690 (row a5_00):
@686 40 @687 65 @688 94 @689 29 @690 60 @691 03 @692 39 @693 74 @694 46
Reads: "...e[40] [65] ne[94] er[29] [60] [03] a[39] [74] que[46]..."
Local frame: "[60] [03] a [74] que". Under 60=adjective + 03=noun:
"[adj] [03-N] a [74] que" parses cleanly. 03 nominal independently
supported (see anchors). PASS.

W3 — '60 03' @1644 (row a8_04):
@1641 12 @1642 33 @1643 98 @1644 60 @1645 03 @1646 64 @1647 31 @1648 10
Reads: "...n'[12] [33-inf] [98] [60] [03] qui[64] [31]..."
Local frame: "[60] [03] qui [31-V]". Under 60=adjective + 03=noun:
"[adj] [03-N] qui [V]" parses cleanly. PASS.

W4 — '60 03' @1674 (row a8_05):
@1671 55 @1672 81 @1673 92 @1674 60 @1675 03 @1676 39 @1677 74 @1678 77
Reads: "...[92] [60] [03] a[39] [74] le[77] [44]..."
Local frame: "[60] [03] a [74] le". Same as W2: clean under
60=adjective + 03=noun. PASS.

Anchors (re-derived, independent of the bar frames):
- '65 qui' x3: @724 (row a5_02), @1208 (row a7_00), @1340 (row a7_05).
  64='qui' is red-team granted; a relative 'qui' needs a nominal
  antecedent, so 65 is noun-shaped. (The bar's noun-60 evidence gloss
  also cites '29-40-65' x3 direct-object slot; not re-needed here.)
- 'le [03]' @722 (row a5_02): '21 80 77 03 91 65' — "le [03-N]" with
  77='le' provisional.
- 'ce [03]' @1014 (row a6_02): '78 47 03 24 41' — "ce [03-N]" with
  47='ce' granted (A4).
- 'ce [03]' @1790 (row a8_09): '68 47 03 00 86' — same.
- '87 03' occurs x0 (attribution check: the 47='ce' attribution is
  correct). '03-64' x4 on the stream — relative 'qui' after 03,
  consistent with 03 nominal.

K1 — kill window @1338 (row a7_05):
@1335 86 @1336 71 @1337 64 @1338 60 @1339 08 @1340 65 @1341 64 @1342 52
Reads: "...[86-inf] [71] qui[64] [60] [08] [65] qui[64] [52]..."
64='qui' is red-team granted. A subject relative 'qui' must be followed
by a finite verb (or verb+clitic complex). 60 as masculine adjective
cannot sit in the verb slot: "qui [adj] [08]" is ungrammatical. 08's
candidates ({ne, se, on, spelling-letter}; stem-08 still queued) hold
no finite verb, and even a verbal 08 would leave "qui [adj] [verb]"
ungrammatical. The only grammatical parse forces 60 verbal:
"qui [V-60] [08] [65] qui [V]". The sole rescue is adjective/verb
polyvalence, which per §7 is a red-team declaration (67 et/veut is the
sole true polyvalence) — not available at battery level. KILL-GRADE.

K2 — kill window @700 (row a5_01):
@697 45 @698 28 @699 94 @700 60 @701 12 @702 98 @703 20
Reads: "...[28] ne[94] [60] n[12] [98]..."
'ne' must be followed by a verb. Under 60=adjective, "ne [60-adj] n"
is ungrammatical; 60 is forced verbal. Premises: 94='ne'
(battery-promoted) and 12='n' (letter, battery-promoted) — flagged as
battery-level, but K1 alone suffices. KILL-GRADE (independent of K1).

Other 60 windows scanned for class evidence (fenced, not duplicated):
- @119/@172/@197 '21 60' + @232 '21 60' (vient-parvenir formula third):
  21 open; @232's thirds question is owned by queued
  frame-vient-parvenir — fenced, not a contradiction on its own.
  @197 '21 60 08 67' is adjective-unfriendly (08 open) but not
  derivable as a contradiction; fenced.
- @322 '92 60 15': 92 and 15 open — fenced.
- @637 '46 60 67': "que [60] et[67] le[77] [89]...". 67's follower
  @639=77='le' is not infinitive-shaped, so 67='et' by the positional
  rule. Strained under both rival readings; 89 open — fenced.
- @995 '03 60 67': "[03] [60] et[67] la[11] [96]...". 67's follower
  @997=11='la' is not infinitive-shaped, so 67='et'. Under 60=adj:
  "[03-N] [60-adj] et la ..." — postnominal adjective, the normal
  French position. SUPPORTS the adjective arm (outside the bar's four
  frames; see follow-up 2).
- @1366 '14 60 03' / @1690 '14 60 27': 14's value owned by queued
  tout-14-rerun / the 62-94-79 frame family — not touched.
- @1474 '53 60 06': 53 open; 06='ent' ending gives a verbal stem reading
  ("[53] [60-stem]ent") while 06='en' keeps an adjective+preposition
  reading. Ambiguous; owned by queued verb-60 — fenced.
- @1563 '06 60 71' / @1735 '06 60 12': 06 en/ent — owned by queued
  verb-60 — fenced, not duplicated.

## Per-clause pass/fail

- C1: PASS. @454 "le [60-adj] [65-N]" parses with one provisional
  assumption (77='le'); 65 nominal is independently supported.
- C2: PASS, 3/3. @690, @1644, @1674 all parse as '[60-adj] [03-N]'
  with 03 nominal independently supported.
- C3: PASS. '65 qui' x3 re-derived at the cited offsets; 'le [03]'
  @722; 'ce [03]' @1014/@1790 via granted 47='ce'; '87 03' x0.
- C4: FAIL AT KILL GRADE. @1338 'qui 60 08' (64='qui' granted) and
  @700 'ne 60 12' both force 60 into a verb-only slot, which the
  single-value adjective claim cannot occupy. Per §7 the only rescue
  is a second polyvalence, which this battery may not declare.

## Verdict

**kill** — 60's masculine-adjective value, as a single-value claim, is
killed. The four bar frames cohere under the adjective reading (C1–C3
pass; the adjective arm is confirmed as the cleaner rival to the
killed noun claim on those frames), but two independent windows force
60 verbal (C4 fails at kill grade: @1338 with red-team-granted
64='qui', @700 with battery-promoted 94='ne').

Note for the red team (not an escalation of a standing verdict — none
exists on 60): the NP-frame adjective evidence (W1–W4, plus the
@995 postnominal-adjective support) versus the verbal windows
(@1338/@700, and verb-60's six windows, already queued) is a live
adjective-vs-verb second-polyvalence question. Per §7 only the red
team can declare it. Coordinate with verb-60 (queued, verbal arm):
this battery did not duplicate its six-window verbal bar.

## Follow-ups (work regenerates)

1. **poly-60-redteam** (priority 1): red-team adjudication packet —
   60 adjective (NP frames @454/@690/@1644/@1674, all clean, anchors
   independently supported; @995 postnominal support) vs 60 verb
   (@1338 kill-grade under granted 64='qui'; @700; verb-60's six
   windows). Bar: "resolve iff red team declares 60 polyvalent
   (adjective/verb) with a positional rule, or assigns one class with
   all 18 windows parsing." Adverses: only the red team may declare
   per §7 (67 sole true polyvalence); battery gathers evidence only.
   Evidence: this report + queued verb-60.
2. **adj-frames-995-637** (priority 2): harden the adjective arm —
   @995 '03 60 et' (postnominal-adjective frame) and @637 'que 60 et'
   (coordination frame). Bar: "promote-frame iff both parse as
   postnominal/coordinated adjective with 03 nominal (independently
   supported) + zero contradictions." Adverses: load-bearing on the 67
   positional rule (67='et' via non-infinitive followers 77/11);
   does not duplicate the four bar frames. Evidence: @995 support in
   this report. Priority: feeds poly-60-redteam.
3. **participle-60** (priority 2): single-class rescue test — does one
   VERBAL value for 60 (e.g. present participle / verb stem) parse the
   four NP frames (@454/@690/@1644/@1674) AND the verb slots
   (@1338/@700)? If yes, no polyvalence is needed. Bar: "resolve iff
   one stated verbal value parses all six windows with <=1 unstated
   assumption; else confirm the polyvalence question." Adverses:
   coordinate with verb-60 (do not duplicate its six-window bar);
   '21 60' x4 formula thirds question is fenced to frame-vient-parvenir.
   Evidence: K1/K2 vs W1–W4 tension in this report.
