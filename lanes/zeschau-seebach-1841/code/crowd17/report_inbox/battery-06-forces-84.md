# Battery report: 06-forces-84

- Target id: `06-forces-84`
- Claim: "@1188 '06-84-59' gates unconditioned 84='on' on 06's class"
- Date: 2026-10-09
- Worker: battery worker (subagent 6b90e92d-b600-4591-8f18-8c2ebe8fb3d7)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
  n=1847 asserted, 96 groups asserted). `canonical.py` never used. R5005,
  sealed gates, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/06-forces-84.lock (created at start,
  deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"resolve iff: if the 06 battery promotes 06='en', record NULL with the 'en on
est' contradiction as headline and escalate to red team (killing unconditioned
84='on' would contradict the A15 grant — a red-team act); else state 06's
class with @1188 parsing. Control @1289 must read clean as clause boundary
either way"

## Numbered pass/fail clauses (restated before testing, not modified after)

1. (C1) Gate check: did any battery promote 06='en'? If yes → verdict NULL,
   headline the 'en on est' contradiction, escalate to red team. If no →
   the escalation branch is closed.
2. (C2) State 06's class (from the standing 06 battery) with @1188 parsing
   under it: 06-84 must admit a parse in which the feared 'en on est'
   clitic-order contradiction does not arise.
3. (C3) Control @1289 ('00-11-17-84-59-35-94') reads clean as a clause
   boundary — i.e. 84='on' clause-initial after a complete constituent —
   under either 59 value.
4. (C4) Adverses answered: (a) 06's class gate (was "open, gated on queued
   ent-06"); (b) the A15 grant of 84='on' is not killed unconditioned at
   battery level.

## Method

1. Read BATTERY-PROTOCOL.md first; created the lock on start.
2. Read the target's queue entry; copied the bar verbatim above.
3. Checked the 06 battery's standing: `ent-06` → status `verdict`, result
   `promote`, date 2026-10-08 (report:
   code/crowd17/report_inbox/processed/battery-ent-06.md). Swept the whole
   queue for any other 06='en' promotion.
4. Re-derived the repaired stream in-session (1,847 pairs / 96 types
   asserted); located the 06-84 bigram byte-exact (exactly 1x stream-wide)
   and the control 7-gram byte-exact.
5. Parsed both windows under standing values only (banked GT; granted
   84='on' A15, 46='que', 64='qui', 96='par', 17='fois', 79='tout',
   00='pour', 87='ce', 47='ce'; promoted 94='ne', 06='ent'; provisional
   59='est', 77='le'). 1841 diplomatic French only.

## Standing values used (premises, not re-litigated)

- ent-06 PROMOTE (2026-10-08): **06="ent"** — verb-ending syllable/letters
  ("-ent", 3pl; "mentent" = 82+06+06 compositional; single value, no
  polyvalence — §7 67-rule untouched).
- A15: 84="on" (grant stands; REPORT.md wave notes it is weakened — the
  "on est" 59-family legs are VOID because 59@1190/@1448/@1804 are ESTE —
  but the grant itself was not killed).
- 59='est' remains protocol-provisional; crowd10 conditioner59 classes
  @1186 and @1190 as ESTE (cited as the live tension, not adjudicated
  here).

## Window-level evidence

### Witness @1188 (row a6_10; 06-84 bigram = stream hapax)

0-based @1180–1196 re-derived byte-exact:

```
@1180  77   (le~)      a6_10
@1181  78              a6_10
@1182  94   ne         a6_10
@1183  82   m          a6_10
@1184  06   ent        a6_10
@1185  06   ent        a6_10
@1186  59   (est~/ESTE) a6_10
@1187  42              a6_10
@1188  06   ent        a6_10
@1189  84   on         a6_10
@1190  59   (est~/ESTE) a6_10
@1191  46   que        a7_00
@1192  07              a7_00
@1193  24              a7_00
```

The finder-anchored 7-gram '59-42-06-84-59-46-07' = @1186–1192 ✓.
The 06-84 bigram occurs exactly 1x stream-wide (@1188–1189) ✓.

Parse under the promoted 06='ent':

- @1182–1185 "94-82-06-06" = **"ne mentent"** — clean, adopted from
  ent-06 F2 (94='ne' promoted, 82='m' GT, 06-06 = "ent"+"ent").
- @1187–1188 "42-06" = **"[42]ent"** — verb stem + 3pl ending, conditional
  on 42 being a verb stem (42's class open; A1 predicative-frame tension
  noted; stated assumption per the 06-attachment rule's left-neighbor
  condition). This is the same 42-06 contact ent-06 flagged for its own
  battery; not re-litigated here.
- @1188–1189 "06-84" = **"ent" + "on" with a word boundary**:
  "[42]ent | on …". Because 06='ent' is word-final here, 84='on' opens a
  new word — there is no clitic stack. The feared **'en on est'**
  contradiction requires 06='en' ("[42]en on est" — clitic "en" before
  subject pronoun "on" violates French clitic order; "on en est" is the
  grammatical order). That contradiction is **void at battery grade**
  because 06='en' never promoted (see C1).
- @1189–1191 "84-59-46": under the A15 grant, 84='on'. 59@1190 is
  ESTE-class per crowd10 conditioner59 and the REPORT.md A15 correction
  (the "on est" family is VOID there) — so "on est" does NOT parse at
  @1189–1190 under 'est'. The live lane reading is the 3-syllable -este
  verb unit "06-84-59" ({manifeste, atteste, proteste, conteste, déteste},
  set-valued) + "que" (46) + clause: "…[42]ent. [este-verb] que [07]
  [24]…" — fully grammatical. Under that rival reading 84 is the verb's
  middle syllable, not 'on' — but este-verb-id (WO1) pre-registered this
  as **not a kill; polyvalence live**, i.e. red-team venue. It is fenced
  here, not adjudicated, and it does not constitute a battery-grade kill
  of the A15 grant.

Result: under the promoted 06 class, @1188 parses with **no battery-grade
threat to unconditioned 84='on'**. The gate the claim worried about (06's
class deciding 84's fate via 'en on est') resolves cleanly: 06='ent' was
promoted, 06='en' is dead, the clitic-order contradiction never fires.

### Control @1289 (row a7_03; '00-11-17-84-59-35-94' @1287–1293)

0-based @1281–1295 re-derived byte-exact:

```
@1287  00   pour       a7_03
@1288  11   la         a7_03
@1289  17   fois       a7_03
@1290  84   on         a7_03
@1291  59   (est~/FENCED) a7_03
@1292  35              a7_03
@1293  94   ne         a7_03
@1294  52              a7_03
@1295  80              a7_03
```

The 7-gram '00-11-17-84-59-35-94' = @1287–1293 ✓ (claim labels it @1289,
the 'fois' position).

Clause-boundary reading: **"…pour la fois | on …"** — "pour la fois" is a
complete adverbial constituent; 17='fois' is banked; "fois on" cannot
compose into a word (the "foison" rival — "pour la foison" — is fenced as
strained: "foison" is archaic as a noun and "pour la foison" is an
unattested preposition frame in 1841 French, versus the live "à foison").
84='on', a subject pronoun, therefore opens a new clause. The boundary
itself is byte-evidenced and **holds under either 59 value** ('est'
provisional → "…on est [35]…"; ESTE/fenced → "…on [este-verb] [35]…"):
the boundary sits between @1289 and @1290, upstream of the 59 question.
The mechanism the control establishes — 84='on' clause-initial after a
complete constituent — is exactly the shape @1188–1189 takes under
06='ent' ("[42]ent | on …").

## Per-clause pass/fail

1. **C1 — PASS (escalation branch closed).** No battery promoted 06='en':
   ent-06 promoted 06="ent/ment" (verdict `promote`, 2026-10-08); a
   whole-queue sweep finds 06='en' mentioned only in this target's own
   entry. The 'en on est' contradiction therefore has no live premise at
   battery grade — there is nothing to escalate.
2. **C2 — PASS.** 06's class stated: **"ent"** — verb-ending
   syllable/letters, single value, no polyvalence (ent-06 PROMOTE).
   @1188 parses under it: 42-06 = "[42]ent" (42-as-verb-stem conditional,
   stated); 06-84 = "ent"+"on" word boundary — the 'en on est'
   clitic-order contradiction requires the dead 06='en' and does not
   arise. Unconditioned 84='on' at @1189 survives the 06-class gate at
   battery grade. (The -este verb-unit rival for 06-84-59, with 84 as
   middle syllable, is fenced to the red-team venue per este-verb-id's
   pre-registered not-a-kill; it is not a battery-grade kill of the A15
   grant.)
3. **C3 — PASS.** Control @1289 reads clean as a clause boundary:
   "…pour la fois | on …" — boundary byte-evidenced (17='fois' banked;
   "foison" rival fenced as strained); holds under either 59 value.
4. **C4 — PASS.** Adverse (a): 06's class is no longer open at battery
   grade — the ent-06 gate resolved to 06='ent' (verdict/promote).
   Adverse (b): the A15 grant is not killed, unconditioned or otherwise,
   at battery level — the only battery-grade threat (06='en') is dead;
   the este-unit rival is red-team venue.

## Verdict: PROMOTE

The gate resolves cleanly at battery grade: **06 = "ent"** (promoted,
single value); under it @1188's "06-84" parses as "ent"+"on" with a word
boundary, so the feared 'en on est' contradiction never fires and
**unconditioned 84='on' at @1189 survives the 06-class gate**. The
NULL/escalation branch (06='en') is closed — no red-team escalation from
this target. The -este verb-unit rival (84 as middle syllable of
06-84-59) remains live at the red-team venue per este-verb-id's
pre-registered not-a-kill; it is fenced here, not adjudicated. Control
@1289 confirms the clause-initial-'on' mechanism.

No standing or red-team verdict contradicted or downgraded; §7 intact
(67 et/veut remains the sole true polyvalence). No follow-ups required
(promote, not null); the este-unit question is already red-team-owned.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/06-forces-84.lock` created on start,
  deleted on completion.
- Queue update: temp-file + rename on `battery-queue.json`, own entry
  only; pre-write assert confirmed no prior verdict; JSON re-validated
  after write.
- R5005, sealed gates, red-team adjudication queue untouched.
