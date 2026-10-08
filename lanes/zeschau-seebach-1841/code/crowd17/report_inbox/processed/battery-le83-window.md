# Battery report: le83-window — 83 takes a value making @1216 '36 77 83' parse

- Target: le83-window (priority 2)
- Date: 2026-10-08
- Worker: ba37e9b3-5cd3-4c46-b2a2-603ff53cb10c
- Verdict: **null** (bar's own fence path: 83 fenced as the blocker at the @1216 window, not 77)

## Bar (verbatim, pre-registered)

"resolve iff ONE 83 value parses both 'le [83]' (@1216) and 98-83 x5 ('vient de'); else fence 83 as the blocker, not 77"

## Bar restated as numbered pass/fail clauses

1. (C1) ONE 83 value parses '36 77 83' (@1215/1216/1217, row a7_00) as grammatical 'le [83]'.
2. (C2) The SAME value parses all five 98-83 windows as 'vient de [X]'.

## Offset correction (repaired stream)

The queue evidence anchors the window at @1216. On the repaired stream
(1,847 pairs, repair_parse.py), the window is @1215/1216/1217 = '36 77 83':
36@1215, 77@1216, 83@1217, row a7_00. Same physical window; 83 is at @1217.
The 77-83 bigram is unique stream-wide.

## Method

Parsed the repaired stream per code/side-keyhunt/repair_parse.py
(code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt).
83 census re-derived: n=15 at @228(a2_01), @614(a4_00), @898(a5_08),
@907(a5_09), @911(a5_09), @931(a5_10), @1061(a6_04), @1161(a6_09),
@1171(a6_09), @1217(a7_00), @1334(a7_05), @1612(a8_03), @1784(a8_09),
@1829(a8_11), @1840(a8_11). Never used canonical.py. Never touched R5005.

## Window-level evidence

### C2: 98-83 x5 — all five parse as 'vient de [X]' under 83='de'

- @227/@228 (a2_01): '87 46 98 83 82 96 21 60' = 'ce que [98] de [82] [96] [21] [60]'.
- @897/@898 (a5_08): '98 82 14 98 83 86 16' = '[98] [82] [14] [98] de [86-INF] [16]' — 86 is INF-class (A9); 'vient de [infinitive]' is grammatical.
- @930/@931 (a5_10): '98 83 56 69' = '[98] de [56] [69]'.
- @1060/@1061 (a6_04): '98 83 82 96 21 62' — formula window.
- @1783/@1784 (a8_09): '98 83 82 96 21 68' — formula window.

5/5 windows grammatical as 'vient de X'. **C2 PASSES** under 83='de'.
Caveat: load-bearing on the unconfirmed 98='vient' reading
(frame-vient-parvenir adverse: "French of 98 unconfirmed").

### C1: '36 77 83' @1215-1217 — 'le de' is ungrammatical

Window (a7_00): '...1213:96 1214:45 1215:36 1216:77 1217:83 1218:92 1219:61...'
= '... par ce [36] le de [92] ...' (96='par', 45='ce' HOLD, 77='le' provisional,
83='de' under test). 'le de' is ungrammatical in every clause position: article
+ preposition has no grammatical reading, and no clause boundary between the
adjacent 77-83 pair rescues it. No elision applies ('de' is consonant-initial;
77-83 cannot form an l'- elision). **C1 FAILS** under 83='de'.

No other single value satisfies both clauses either: the only value class that
parses 'le [83]' AND 'vient [83]' simultaneously would be an infinitive
('le dire'-shaped / 'vient dire'-shaped), but the three formula windows are
98-83-82 ('[vient] [INF] m...'), which breaks a bare-infinitive fork unless 98
is re-read — that is a bigger claim than this bar tests, recorded below as a
finding and follow-up.

### 'cède'-verb rival check (task instruction)

The 'cède' rival is window-inapplicable at @1216: it needs the 87-83 bigram
('cède' = 87+83 composition), which occurs at @613 and @1170, not here.
The rival's standing: fenced at queued frame-87-83-cede (owns @614/@1171);
cited as decided-direction evidence, not re-litigated.

### Contact profile (supporting, 83='de' compatibility elsewhere)

- Predecessors: 98 x5, 87 x2 ('ce de' — fenced adverse, frame-87-83-cede owns),
  55 x2, 44 x2 (de-frame-44-83-21 owns), 64 x1 (@911 'qui de est' — fence-911-de owns),
  77 x1 (this window), 39 x1, 38 x1.
- Followers: 82 x3 ('de m(e)...'), 21 x3 ('de [21]'), 86 x2 ('de [86-INF]' —
  86 INF-class granted, A9), 70/54/59/56/92/71/24 x1.
- 12-13 of 15 windows are de-compatible; the 'de' lead survives everywhere
  except the three fenced cells (@613/@1170 'ce de', @911 'qui de est',
  @1217 'le de'). None of these is a battery-level kill: kill-grade on
  unconditioned 83='de' is owned by fence-911-de per the brief.

## Per-clause verdict

- C1: FAIL ('le de' ungrammatical at @1215-1217; no alternative parse).
- C2: PASS (5/5 'vient de X' windows grammatical under 83='de').

Per the bar's own resolution path: no ONE 83 value parses both clauses, so
**83 is fenced as the blocker at the @1216 window, not 77**. This is a null
(the value question stays open; the residual is localized to 83 at this
window). Not a kill: the bar's failure mode is the fence, and kill-grade on
the unconditioned 'de' lead belongs to fence-911-de.

## Adverses answered

- "'de' lead vs article frame pull opposite ways": answered — the pull
  resolves as a localized 83-blocker fence at this one window; the article
  frame (77='le' provisional) is not downgraded, per the bar.
- "83 value is open": stays open; fence recorded, not a value claim.
- Shared-lead interactions cited without re-litigation: @911 'qui de est'
  (fence-911-de owns), @613/@1170 '87 83' 'ce de' (frame-87-83-cede owns the
  'cède' fence), @1160/@1839 '44-83-21' (de-frame-44-83-21 owns).

## Follow-up targets (null regenerates work)

1. **fence-83-1217** — formalize the fence: re-parse '36 77 83' @1215-1217
   (a7_00) with 83 as the designated blocker. Bar: ONE grammatical parse of
   the window with 83 unfixed (name 36 or place a clause boundary), or confirm
   the localized residual with stated cause.
2. **de-83-sweep** — full 15-window promotion battery for 83='de', gated on
   fence-911-de, frame-87-83-cede, and fence-83-1217. Bar: promote 83='de' iff
   all fenced adverses stay fenced with cause AND zero new contradictions
   across the 15 windows.
3. **inf-83-fork** — test 83 as an infinitive value ('le dire'-shaped at
   @1216 vs 'vient dire'-shaped at the five 98-83 windows). Bar: resolve iff
   the three formula windows (98-83-82-96-21-[60/62/68]) parse with a re-read
   98 or the fork dies at those windows; coordinate with frame-vient-parvenir.

## Lock note

locks/le83-window.lock created 2026-10-08T09:35:34Z, deleted on completion.
No stale lock encountered.
