# Battery report — gate-satisfiability-16-85 (are the infinitive gates satisfiable at all)

Worker: battery-worker-gate-satisfiability-16-85. Date: 2026-10-08.
Lock: `code/crowd17/next-token/locks/gate-satisfiability-16-85.lock` created
2026-10-08T15:41:48Z; no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
(replicated in-worker, not `canonical.py`). R5005 not touched. Every count
below re-derived from the stream in this run. No observed values redacted.

Scope: gate-satisfiability audit ONLY. No value is named for 16 or 85 anywhere
in this report (classes only, as the bar requires). frame-82-16 and stem-85
own value-naming; their bars are not duplicated — tensions and residuals are
routed to them, not decided here.

## Bar (pre-registered verbatim, from battery-queue.json)

`(a) every window of 16 (28) and 85 (15) assigned noun / finite-verb / infinitive under the §7 sole-polyvalence law; (b) banked-value frames listed separately from lead-grade frames; (c) binary verdict: gates satisfiable (laisser-gate-16/-85 proceed) or unsatisfiable — if a banked-value frame forces a non-infinitive class, the laisser lead is KILLED cleanly and X must be re-profiled`

Adverses (queue): `duplicates neither frame-82-16 nor stem-85 (those name values; this tests gate satisfiability)`. Task-brief constraint honored: this tests gate
satisfiability only — 16's and 85's values are not named.

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. (a) Every one of the 28 windows of 16 and 15 windows of 85 is assigned a
   class (noun / finite-verb / infinitive) under the §7 sole-polyvalence law
   (67 et/veut is the sole true polyvalence — one class per value, no
   positional second polyvalence declared at battery level).
2. (b) Banked-value frames are listed separately from lead-grade frames.
3. (c) Binary verdict: gates SATISFIABLE (laisser-gate-16/-85 proceed) or
   UNSATISFIABLE. The laisser lead is KILLED cleanly iff a BANKED-value frame
   forces a non-infinitive class for 16 or 85; otherwise X is not re-profiled.

Tier definitions used (per §7):
- BANKED (pencil ground truth): 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que.
- PROMOTED/GRANTED: 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5), 00=pour (A9),
  84=on (A15), 47=ce (A4 allophone tier), 94=ne, 12=n + 48=e (letters),
  30=pas, 39=a/à, 06=ent.
- PROVISIONAL: 59=est, 77=le.
- LEAD-GRADE: 62 = subject pronoun, lead-grade only. UPDATE incorporated:
  collision-62-84 (verdict 2026-10-08) KILLED 62="on" unconditioned; 62="il"
  demonstrated as rival, NOT promoted. Either way 62 is a subject pronoun, so
  the 62-16 finite-verb SHAPE signal stands at lead grade.

## Method

Re-parsed the repaired stream (assert 1,847 pairs; assert 96 distinct groups).
Extracted all windows with target at center: 16 → n=28, 85 → n=15 (counts
confirm the queue's "28"/"15"). For each window listed the adjacent
(±1) banked/promoted/lead neighbors, then tested the single-class hypothesis
16=infinitive / 85=infinitive against the banked frames: a banked frame
kills the gate only if it FORCES a non-infinitive class (ambiguity and
fenceable residuals do not force). Lead-grade and promoted-tier tensions are
tiered and routed to the chartered gate follow-ups (laisser-gate-16 bar (b),
laisser-gate-85 bar (b)), not decided here.

Grammatical premises relied on (French, verifiable): "m'" + infinitive is
grammatical under a governing verb ("laissez-moi rire", "il peut me
comprendre", "l'envie de me revoir"); "n'" + infinitive is grammatical in the
ne...pas discontinuous frame ("je regrette de n'avoir pas su", "n'être pas"
literary); "se laisser" + bare infinitive is grammatical ("se laisser aller").
12="n" carries the promoted analytic/syllabic duality (n-e-12-48 battery), so
"12-16" also admits the word-internal spelling reading.

## Window-level evidence (@-offsets are repaired-stream pair indices)

### 16 (n=28) — banked frames vs lead/promoted frames

BANKED frames (tier: pencil ground truth):
- `82-16` x11 (@382, @434, @537, @1195, @1198, @1370, @1387, @1437, @1480,
  @1652, @1832): 82="m" banked → "m'[16]". "m'" + noun is ungrammatical;
  "m'" + verb (finite OR infinitive) is fine. Four windows are INF-clean:
  @434 ("77-86-29-82-[16]": 86 INF-class granted (A9) → "le pouvoir me
  [inf]", grammatical); @1370 ("60-03-30-82-[16]": 30="pas" promoted →
  "ne...pas me [inf]" frame, grammatical); @1480 (stem frame
  "67-33-29-82-[16]" = "veut [X]er m'[16]" → under X=laisser, "veut laisser
  me [inf]", the causative flagship); @1832 ("38-83-24-82-[16]": 83=de-lead
  → "de me [inf]"-pattern, grammatical). The other seven are INF-admissible
  with value-level government (@537, @1195, @1387, @1437, @1652) or fenced
  residuals (@1198, see below). NONE forces finite-verb.
- `12-16` x3 (@242, @844, @1431): 12="n" banked. The negation parse
  "n'[16]" does NOT force a finite verb: (i) "n'" + infinitive is
  grammatical ("n'avoir pas", "n'être pas"); (ii) 12 carries the promoted
  syllabic duality, so "12-16" admits the word-internal "n[16]" spelling
  reading. @844 ("62-94-26-12-[16]": 94="ne" promoted) shows double "ne"
  ("ne ... n'"), which disfavors the negation parse there entirely. None of
  the three forces a non-infinitive class; adjudication routed to
  frame-82-16.
- `16-29` x1 (@1142: "00-98-78-62-[16]-29-42-98-98"): 29="er" banked.
  FENCED RESIDUAL with stated cause: "62-[16]-29" is ungrammatical under
  every class assignment with banked 29="er" (subject + bare infinitive if
  16 is stem; "er" ungrammatical as a separate word if 16 is finite or
  whole-infinitive). A window ungrammatical under all assignments forces
  nothing; routed to frame-82-16 for value-level re-parse.

LEAD-GRADE frames (not kill-grade per bar (c)):
- `62-16` x4 (@83, @659, @1142, @1298): 62 = lead-grade subject pronoun
  ("on" killed unconditioned per collision-62-84; "il" rival demonstrated,
  unpromoted) → finite-verb SHAPE signal. Real tension; chartered to
  laisser-gate-16 bar (b).

PROMOTED-tier frames (not kill-grade per bar (c)):
- `16-00` x4 (@187, @659, @844, @1246): 00="pour" promoted (A9) →
  "[16] pour [inf]" noun-shaped (cf. noun-81 "le [81] pour [INF]" frame).
  Real tension; chartered to laisser-gate-16 bar (b). ("16-59" @1832 is
  provisional-tier: 59="est" provisional; needs a boundary parse, fenced.)

Other 16 windows (neutral or supportive under INF, no banked/lead/promoted
class signal): @220 (42-[16]-24), @294 (65-[16]-01), @533 (32-[16]-08),
@876 (49-[16]-77, 77 provisional), @900 (86-[16]-92, 86 INF-class),
@1394 (89-[16]-76, 89 verb-frame A8), @1411 (42-[16]-97),
@903 (67-[16]-88: 67="veut" reading → "veut [inf]" INF-shaped, supportive).

16 tally: all 11 banked "m'" frames INF-admissible (4 INF-clean); all 3
banked "n'" frames INF-compatible, none forced finite; 1 banked residual
(@1142) fenced; lead-tier tension 62-16 x4 and promoted-tier tension
16-00 x4 routed to laisser-gate-16; 1 non-banked residual (@1198
"m'[16] par m'[16]", ungrammatical under every class) fenced.

### 85 (n=15) — banked frames vs lead/promoted frames

BANKED frames (tier: pencil ground truth):
- `29-85` x3 (@97, @375, @1234): 29="er" banked → "[X]er [85]".
  @1234 (stem frame "29-47-33-29-[85]" = "er ce/se [X]er [85]") is the
  INF flagship: under X=laisser, "se laisser [85=inf]" is grammatical bare
  ("se laisser aller"). @97 ("81-97-46-29-[85]": 46="que" banked → "que
  [X]er [85]") is INF-admissible with value-level government (fenced
  detail: the "que"-governing verb is open). @375 fenced residual (below).
  NONE forces a non-infinitive class.
- `85-82` x1 (@375: "21-65-63-29-[85]-82-48-00-11" = "[X]er [85] m'e pour
  la", 82="m"/48="e" banked letters → "me"): FENCED RESIDUAL with stated
  cause: "[X]er [85] me pour la" is ungrammatical under every class
  assignment for 85 (noun: "me" after noun broken; finite: no subject;
  infinitive: "me" after non-imperative infinitive broken). Forces
  nothing; routed to stem-85 for value-level re-parse.

PROMOTED-tier frames (not kill-grade per bar (c)):
- `79-85` x2 (@54, @595): 79="tout" promoted (A5) → "tout [85]" noun-shaped
  under the determiner reading. The pronoun reading ("tout" = object
  pronoun + infinitive, "tout comprendre"-shaped) is live but needs a
  clause-boundary parse, so the noun-shape is NOT forced. Real tension;
  chartered to laisser-gate-85 bar (b).

Other 85 windows (no banked class signal; class open, routed to stem-85 /
laisser-gate-85): @733 (24-[85]-93), @746 (81-[85]-28), @956
("96-87-46-24-[85]", 24's class value-level), @1047 (76-[85]-41),
@1173 (21-[85]-36), @1278 (56-[85]-48, 48="e" promoted letter),
@1439/@1694/@1755 (24-[85] x3 of the 24-85 x5 set), @1699
("91-[85]-33-94-30", 94="ne"/30="pas" promoted).

85 tally: all banked frames INF-compatible (@1234 INF-clean flagship);
1 banked residual (@375) fenced; promoted-tier tension 79-85 x2 routed to
laisser-gate-85; no banked frame forces a non-infinitive class.

## Per-clause pass/fail

1. Clause (a) — every window assigned under §7 sole-polyvalence: PASS with
   stated fencings. Single-class assignments 16=infinitive and
   85=infinitive are exhibited under which EVERY banked frame parses; the
   43 assigned windows carry explicit tier/status marks above; 3 windows
   fenced as residuals with stated cause (@1142, @1198, @375 — each
   ungrammatical under every class assignment, hence forcing nothing).
   No second polyvalence declared or needed.
2. Clause (b) — banked vs lead-grade frames listed separately: PASS. Banked:
   82-16 x11, 12-16 x3, 16-29 x1, 29-85 x3, 85-82 x1. Lead-grade: 62-16 x4
   (finite-verb shape; 62 lead-grade subject pronoun). Promoted-tier:
   16-00 x4 (noun shape; 00="pour" A9), 79-85 x2 (noun shape under
   determiner reading; 79="tout" A5). Provisional-tier: 16-59 @1832.
3. Clause (c) — binary verdict: PASS → gates SATISFIABLE. No banked-value
   frame forces a non-infinitive class for 16 or for 85. The laisser lead
   is NOT killed; X is not re-profiled. laisser-gate-16 and laisser-gate-85
   PROCEED to adjudicate the lead-grade (62-16 x4) and promoted-tier
   (16-00 x4, 79-85 x2) tensions per their chartered bars.

## Adverses disposition

- "duplicates neither frame-82-16 nor stem-85": ANSWERED — neither
  value-naming bar was run; all value-level tensions and the three
  residuals are explicitly routed to the gate owners, not decided here.
- "this tests gate satisfiability only — do not name 16's or 85's values":
  ANSWERED — no value named for 16 or 85 anywhere in this report; only
  the class (infinitive) required by the bar itself is assigned.

## Standing-verdict check

No contradiction with any standing verdict. x-33-laisser-test (null,
2026-10-08) recorded the gates "open AND contradicted" and chartered
exactly these follow-ups; this battery refines its contradictions to
lead/promoted-tier (not banked-tier), consistent with laisser-gate-16
bar (b) and laisser-gate-85 bar (b), which explicitly own those tensions.
collision-62-84's kill of 62="on" is incorporated (62 cited at lead
grade). No red-team verdict on gate satisfiability exists. Nothing to
escalate; no second polyvalence declared.

## Verdict: promote

Claim "the infinitive gates are satisfiable at all" holds at battery
grade: the infinitive readings of 16 and 85 survive every banked-value
frame, the three residuals are fenced with cause, and the remaining
tensions are tiered to the already-queued gate follow-ups. The laisser
lead ('laisser' at LEAD strength, x-33-laisser-test) is NOT killed —
laisser-gate-16 and laisser-gate-85 proceed.

No follow-ups proposed (verdict is promote, not null). The queued
laisser-gate-16 / laisser-gate-85 targets are the chartered next step.
