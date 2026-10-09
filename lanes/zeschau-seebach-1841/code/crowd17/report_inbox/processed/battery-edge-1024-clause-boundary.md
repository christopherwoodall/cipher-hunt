# Battery verdict: edge-1024-clause-boundary

- id: `edge-1024-clause-boundary`
- date: 2026-10-08
- worker: subagent-7aae1149
- stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`)

## Bar (verbatim from queue)

"(a) 92's class named (coordinate with class-92); (b) state whether the 6-gram spans a clause boundary — if yes, the claim formulation 'reads ce qui par [43] ce [01]' needs a boundary-aware revision; (c) the '53-on' left edge parsed or fenced"

Numbered clauses:
1. (a) Name 92's class at @1022, coordinating with (not duplicating) class-92.
2. (b) State whether the 6-gram @1024–@1029 (45-64-96-43-87-01) spans a clause boundary; if yes, give the boundary-aware revision of "reads ce qui par [43] ce [01]".
3. (c) Parse or fence the "53-on" left edge (@1020–@1021).

## Claim under test

"A clause boundary falls between @1023 ('qui') and @1024 ('ce') — the 6-gram spans '…on [92] qui [V]. Ce qui par suite, ce [01]…'"

## Method

Dumped @960–@1050 on the repaired stream with banked values applied. Tested the
claimed boundary position and every adjacent alternative boundary position for
grammaticality in 1841 diplomatic French under banked/granted values
(64=qui granted, 45=ce A11 hold, 96=par promoted, 84=on promoted-weakened,
87=ce promoted, 77=le provisional, 43 in {condition, mesure} per the
suite/manière kills). A relative "qui" must be followed by its clause's verb;
a clause cannot end with a verb-less relative pronoun. All four class
assignments for [92] (verb-finite, verb-inf, noun, other) were tried against
each boundary position.

## Window-level evidence

Stream @1020–@1040 (row a6_03 starts at @1020):

```
@1020 53   [53]      <- row-initial
@1021 84   on
@1022 92   [92]
@1023 64   qui
@1024 45   ce        <- claimed boundary is between @1023 and @1024
@1025 64   qui
@1026 96   par
@1027 43   [43]      (condition/mesure survivors; suite/maniere killed)
@1028 87   ce
@1029 01   [01]
@1030 03   [03]
@1031 29   er
@1032 80   [80]
@1033 77   le (provisional)
@1034 11   la
@1035-@1040 pre m i er e fois  ("la premiere fois" island; note "le la" @1033-1034)
```

Left context @1010–@1019: "tout [80] [78] ce [03] [24] [41] [15] [66] [91]".

## Clause (b): the boundary question — FAIL at kill grade

**Claimed boundary (@1023|@1024): ungrammatical.** It forces clause A to end
"…53-on [92] qui" — a relative "qui" with no following verb inside clause A.
Under every class assignment for [92]:

- [92]=VFIN: "on [V] qui." — clause ends with a verb-less relative pronoun.
  Un grammatical.
- [92]=noun: "on [N]" — "on"+noun is ungrammatical before the "qui" question
  even arises.
- [92]=INF or other: "on [92]" ungrammatical.

The window therefore forces the claim false: no clause boundary can fall
between @1023 and @1024.

**No alternative boundary parses either** (each forces an ungrammatical side):

- @1022|@1023: "…on [92]. Qui ce qui par [43]…" — "qui ce qui" ungrammatical.
- @1024|@1025: "…qui ce. Qui par [43]…" — "qui ce" and verb-less "qui"
  both ungrammatical.
- @1025|@1026 or later inside the 6-gram: the 6-gram "ce qui par [43] ce [01]"
  contains no finite verb; "ce qui par [43]" is subject+adjunct with no verb,
  "ce [01]" is an NP fragment. No internal split yields two clauses.

**The 6-gram does not span a clause boundary.** The "boundary-aware revision"
bar (b) asks for is not triggered — there is no boundary to be aware of. The
@1020–@1029 span is ungrammatical as one clause too ("qui ce qui"), which
corroborates class-92's standing fence R-class92-1022 rather than resolving it.

Caveat recorded: 84="on" is promoted-weakened; if 84 were ever re-valued, this
window needs re-analysis. The interrogative-"qui" reading ("…on [92]. Qui?")
has no support (no question context, 1841 diplomatic prose) and does not
rescue the claim's declarative formulation.

## Clause (a): 92's class — coordinated, not named (fence stands)

- class-92 (NULL, 2026-10-08): 92's global class open; @1022 fenced as
  residual R-class92-1022, "anomalous under ALL classes", red-team eyes.
- verb-92-subset (PROMOTE battery-level, 2026-10-08): 92=verb on the
  verbal-governor subset only; fenced residuals @1022/@683 explicitly excluded
  from the promote scope.
- prenne-92-noun (KILL, 2026-10-08): noun value arm killed.

This battery's boundary analysis gives no new class information for @1022's
92: the residual persists under all classes at every boundary position.
Naming a class here would duplicate/contradict the standing red-team fence,
so per protocol §5.2 the class stays UNNAMED at battery level and
R-class92-1022 stands untouched. Coordination complete; nothing re-litigated.

## Clause (c): "53-on" left edge — FENCED

@1020=53 is row-initial (row a6_03 starts here); @1021=84=on. 53 occurs 11x
stream-wide with scattered followers (12 x4, 84 x2, 17/34/69/61/60 once each);
the "53 84" bigram also occurs mid-row at @411 ("01 02 53 84 51"), so it is not
inherently row-initial. Row-initial slot shows mild enrichment for
clause-initial groups (46=que 3/70 vs 29/1847 base; 00=pour 3/70 vs 55/1847;
94 3/70 vs 37/1847) — suggestive of, but not proving, clause starts at row
heads. 53 itself is open (no banked value); "53-on" cannot be parsed with
granted values. Fenced as unparsed left edge; 53 needs its own value battery
before this edge can be decided.

## Per-clause results

- (a) 92's class: COORDINATED — fence R-class92-1022 stands, class unnamed at
  battery level (not a pass, not a kill-grade fail of the claim).
- (b) Boundary: FAIL AT KILL GRADE — claimed boundary ungrammatical; no
  boundary anywhere in @1020–@1029.
- (c) Left edge: FENCED (unparsed, with stated cause).

## Verdict: KILL

The window forces the claim false: a clause boundary between @1023 ('qui')
and @1024 ('ce') strands a verb-less relative "qui" at the end of clause A,
ungrammatical in 1841 French under every class assignment for [92]. No
alternative boundary position in @1020–@1029 parses. The @1022 residual
(R-class92-1022) is corroborated, not resolved — it goes back to the red team
as fenced, not as decided.

No standing red-team verdict touched. R5005, sealed gate instances, and the
red-team adjudication queue untouched. No invented numbers: every offset
verified on the repaired 1,847-pair stream.

## Notes for the red team / pipeline (not verdicts)

- The "le la" bigram at @1033–@1034 (77=le provisional + 11=la ground truth)
  inside the "la premiere fois" island echoes the 37-11 "le la" anomaly the
  la-523743-adjective battery escalated to s5-foundation. 77="le" may need the
  same scrutiny 37 got. Suggested follow-up: "le77-la11-1033" (priority 3).
- 53's value remains the blocker for the @1020 left edge. Suggested
  follow-up: "value-53-distributional" (priority 3): 11 occurrences, followers
  {12 x4, 84 x2, 17/34/69/61/60}, two row-initial.
