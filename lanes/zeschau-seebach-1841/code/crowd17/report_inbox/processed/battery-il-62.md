# Battery report: il-62 (62='il', subject pronoun)

Worker: subagent-d14e9ecf-5e0e-47ff-82b4-ea9168f8556b. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt). canonical.py never used. R5005 never touched.

Indexing: @i = 0-based index into the pair list. pairs[i] = (group, row id).
Cited as @i plus row id (example: @100 a1_02).

## Bar (verbatim, pre-registered)

"promote 62='il' iff every 62 window parses under 'il' with zero hard contradictions and all listed adverses are answered (re-parsed cleanly, fenced with stated cause, or shown misread); kill iff any window forces 'il' false or a cleaner rival value is demonstrated on the same frames; else null with 1-3 follow-up targets. Do not re-litigate 62='on' (killed, collision-62-84)."

Numbered clauses:

1. Every one of the 35 windows with 62 parses under 'il'.
2. Zero hard contradictions (no window forces 'il' false).
3. All four listed adverses are answered.
4. No cleaner rival value is demonstrated on the same frames.
5. 62='on' is not re-litigated.

## Method

Fresh parse per the protocol. No prior counts trusted. Re-derived: n=35;
full successor census; full predecessor census; 62->94 x9; 62->59 x0;
62->48 x6; 21->62 x5; predecessor 46='que' x0; elision-context predecessors
(77 or 46 directly before 62) x1 (@508). Each window was read under 62='il'
with the standing values.

Standing values used. Banked: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que. Granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on,
47=ce. Provisional: 59=est, 77=le. Promoted: 94=ne, 48='e' (letter).

"Parses" means: a grammatical French reading exists that is consistent
with all standing values and 62 spelling "il". A hard contradiction means:
no such reading exists and the failure is specific to 62='il'.

## Window-level evidence (@-offsets, repaired stream)

Successor census (n=35): 94 x9, 48 x6, 98 x5, 16 x4, 06 x2, 61 x2,
18 x1, 21 x1, 38 x1, 46 x1, 91 x1, 93 x1, 96 x1. 62->59 x0.
Predecessor census: 21 x5, 20 x4, 74 x3, 03 x2, 08 x2, 78 x2, 92 x2,
93 x2, and one each of 02, 04, 06, 10, 14, 30, 34, 36, 40, 41, 51, 77, 98.
Predecessor 46 x0. Contrast 84 (n=25): 84->59 x4, 84->94 x0.

Group A — 62->94 = 'il ne' x9 (94='ne' promoted):
- @100 a1_02: "21 62 94 93 59" = "[21] il ne [93] est". Clean.
- @761 a5_03: "20 62 94 59 39" = "[20] il n'est [39]" (ne elides before
  59='est'). Clean.
- @840 a5_06: "20 62 94 26 12" = "[20] il ne [26]…". Clean.
- @1329 a7_04: "06 62 94 70 52" = "[06] il ne pre[70]…". Clean.
- @1362 a7_06: "92 62 94 79 14" = "[92] il ne tout[79]…". Clean.
- @1686 a8_05: "93 62 94 79 14" = "[93] il ne tout[79]…". Clean.
- @1704 a8_06: "20 62 94 88 26" = "[20] il ne [88]…". Clean.
- @1772 a8_08: "78 62 94 24 87" = "[78] il ne [24] ce[87]…". Clean.
- @508 a3_00: fenced (see adverse A1).

Group B — 62->48 = 'il e' x6 (48='e' letter, promoted; mixed word/letter
strings are attested in the lane as 70-12-94 = "pre"+"n"+"ne"):
- @360 a2_06, @425 a2_08, @1315 a7_04, @1349 a7_05, @1464 a7_09,
  @1569 a8_01. Each reads "[left] il e [right]" with open neighbors.
  No contradiction.

Group C — 21->62 x5 (21's value is open):
- @100 (group A), @360 (group B), @1464 (group B): covered above.
- @1065 a6_04: "21 62 18 70" = "[21] il [18] pre[70]…" (18 open). Parses.
- @1539 a8_00: "62 06 21 62 93" — doubled pronoun. Reads as a sentence
  boundary: "…il [06 21]. Il [93]…". Odd under both rivals;
  non-discriminating.

Group D — remaining subject readings (neighbors open, no forced break):
- @11 a1_00: "[93] il [98]". @82 a1_02: "[51] il [16]".
- @389 a2_07: "[36] il [91]" then clause boundary before 84='on'
  ("…il [91]. On [73]…").
- @446 a2_09: "[10] il [61] est[59]" (61 open).
- @658 a4_02: "[03] il [16] pour[00]" ("il [verb] pour…" is clean shape).
- @665 a4_02: "[03] il [06] pour[00]".
- @802 a5_04: "[74] il [98]".
- @849 a5_06: "e[40] il [21] [67] [91]" ("il [verb] veut [inf]" possible;
  67 is the polyvalence).
- @945 a5_10: "[08] il [98] par[96]" ("il [verb] par…" is clean shape).
- @1136 a6_08: "[20] il [98] pour[00]".
- @1141 a6_08: "[78] il [16] er[29]" (29='er' banked; 16 open).
- @1297 a7_03: "[04] il [16] [02] pre[70]".
- @1324 a7_04: "[08] il [98]".
- @1454 a7_09: "[92] il [61] [21]" (46='que' stands two back; vowel-initial
  fit, no clash).
- @1468 a7_09: "[02] il [38]".
- @1536 a8_00: "[41] il [06] [21]" then boundary to the second 62 @1539.

Group E — 62 word-internal x2 (multi-pair words are attested: 70-12,
37-01 unit; French words ending in "il" are common):
- @46 a1_01: "30 62 96 00". Standalone "il par pour" is ungrammatical
  (96='par', 00='pour' granted). Reads cleanly as "[30-il] par pour [92]"
  with 62 word-final (30 open). No standing value is broken.
- @1482 a7_10: "98 62 46 77 84". Standalone "il que" is ungrammatical.
  Reads as "[98-il] que l'on…" with 77='le' eliding before 84='on' —
  the same elision as 77-84 x7 'l'on'. The 'que l'on' parse corroborates
  the lane's elision machinery.

Group F — fenced x1: @508 (adverse A1).

Count check: 9 + 6 + 2 (new in C) + 15 + 2 + 1 = 35. All windows covered.

## Adverses (answered, never ignored)

A1. @508 residual ("67 77 62 94 64 98") — FENCED with stated cause.
Re-verified from the fresh parse. No grammatical reading exists under any
value: "le il" is broken (77='le' provisional), "ne qui" is broken
(94='ne' promoted, 64='qui' granted), and no word-merge rescues exist
("leil", "ilne", "nequi" are not French words). Anomalous under 'il' and
under 'on' alike. 1 window of 35. This adopts standing R17-022, which
fences @508 as a 1-window residual and its 'ne qui' right edge as an
independent fenced anomaly.

A2. 21->62 x5 — ANSWERED by re-parse. All five parse under 'il' (group C
above). 21's value is open under both readings; the strain is symmetric
and non-discriminating. @1539's doubled pronoun resolves as a sentence
boundary.

A3. 62->48 x6 — ANSWERED by re-parse. 'il e' with 48='e' as letter;
mixed word/letter strings are attested (70-12-94). Six clean windows.

A4. lon-62-on-conditioned rival (conditioned 'on' in elision context only)
— ANSWERED, shown not cleaner. Elision-context predecessors of 62
(77 or 46 directly before) occur in exactly 1 of 35 windows (@508).
Conditioned 'on' there reads "l'on ne qui" — the right edge "ne qui"
stays broken, so it is not cleaner than 'il'. The red team already
rejected it (R17-022: a second polyvalence under §7). 62='on'
unconditioned is not re-litigated (killed, R17-017).

## Per-clause pass/fail

1. Every 62 window parses under 'il' — PASS. 32 as subject pronoun
   (8 'il ne' clean + 24 weak-but-grammatical), 2 word-internal with
   open neighbors (@46, @1482), 1 fenced per standing R17-022 (@508).
2. Zero hard contradictions — PASS. No window forces 'il' false. @46 and
   @1482 reconcile through attested multi-pair words; @1482's rescue
   yields 'que l'on', which corroborates the lane's elision machinery.
3. All four adverses answered — PASS (A1 fenced, A2/A3 re-parsed,
   A4 shown not cleaner and already red-team-rejected).
4. No cleaner rival demonstrated — PASS. The only rival on the table is
   'on' (killed) and its conditioned variant (rejected, not cleaner).
5. 62='on' not re-litigated — PASS.

## Verdict

PROMOTE 62='il' (subject pronoun). Split: 32/35 windows subject function,
2/35 word-internal (@46, @1482), 1/35 fenced residual (@508, per R17-022).

Supporting distributional legs, re-derived fresh: 62->94 x9 vs 62->59 x0;
84->59 x4 vs 84->94 x0 ('il' takes 'ne', 'on' takes 'est', zero
crossover); 62 never follows 46='que' (0/35) while 84 follows it x2
('qu'on'); elision-context predecessor of 62 x1 (@508).

## Standing-constraint check

- R17-017 (62='on' unconditioned KILL; 62='il' "demonstrated-not-promoted"):
  this battery is the chartered promotion test. Promoting now advances
  the recorded state; it does not contradict the verdict. No escalation.
- R17-022 (@508 fenced; conditioned 62='on' rejected): adopted, not
  overturned.
- R17-012 (nest-subject frame reads 62 as "il n'est a…"): consistent.
- Kills hold (62='on', 84='fait'). 67 remains the sole polyvalence.
- No R5005 contact. No red-team queue writes.
