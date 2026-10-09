# Battery w5-enter-junction — verdict: PROMOTE

Target: `w5-enter-junction` (P3). Date: 2026-10-09.

## Bar (verbatim from battery-queue.json)

"one parse with stated subject or boundary; else fence 42-06-29 as word-internal"

Numbered clauses (locked before testing):

1. C1 — produce one parse of the @1815 junction with a stated subject or a
   stated boundary.
2. C2 — else (no such parse): fence "42 06 29" as word-internal.

Adverse (from queue): "42-06-29 span fenced as word-internal dissolves the
stem window."

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/w5-enter-junction.lock` on
start. Re-derived the repaired stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed per `repair_parse.py`): 1,847 pairs, 96 types, byte-identical.
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
All @-offsets below are 0-based (queue convention).

## Window

Target junction: 0-based @1814–1816 = `42 06 29`, mid-row a8_10
(row spans @1796–1821; no row edge, no gloss, no formula marker at contact).

Wider context @1810–1821:

```
1810 61      1811 15      1812 93      1813 50
1814 42      1815 06      1816 29
1817 37      1818 01      1819 02      1820 09      1821 19
```

Standing values at contact: 93 = verb class (battery), 06 = "ent"
(letters-tier, battery-promoted pending ratification), 29 = "er" (pencil GT),
37 = predicative frame (A1, class open), 00 = "pour" (A9, class-level).
42: class open (predicative A1 frame), value open. 50/15/61: open.

## C1 — PASS (boundary arm)

The junction parses as ONE word: `[42]enter` — an infinitive in the French
-enter family (inventer, présenter, représenter, tenter, contenter).
06 + 29 compose as letters "ent" + "er"; 42 supplies the stem/letter-cluster
(open groups composing as letters with letter-tier neighbours is lane-standard,
cf. the "53 12 [41]" letter slot in donn-41-44).

Stated boundaries: word boundary after 50 (@1813) and before 37 (@1817).
No clause boundary falls between 06 and 29. The subject/governor of the
infinitive is NOT named (50/15/61 open) — the bar permits subject OR boundary,
and the boundary is stated.

## Rival B killed (clause boundary before 29, 29 word-initial)

1. 29 word-initial is kill-grade dead under standing battery doctrine:
   battery-elision82-48-x1 holds that "an infinitive ending cannot start a
   French word" — no 'er'-initial word is statable under standing values.
   The only lane-known 'er'-initial rescue ("erce" via 47 = 'ce') needs
   47 as 29's successor; here 29's successor is 37. Rescue unavailable.
2. The finite-verb variant of B ("[42]ent." as a complete 3pl clause) needs
   42 = verb stem. That fork is already fenced: ent-06-host-census fenced this
   exact 06 window with cause "42's class open", and the standing 06 decision
   rule makes 06 a finite "-ent" ending IFF its left neighbour is a verb stem.
   42 is not an established verb stem. Fork stays fenced; not re-litigated.

## Distributional support

- 29's stream profile is word-internal: predecessors 33 x5 (A10 "33+29" hold),
  34 x3 ("ier", cf. "première" = 70-82-34-29-40), 03 x3 ("[03]er" infinitive
  frames), 48 x2, 06 x4; successor 40 x9 (analytic "-ere"). n(29) = 45.
- "06 29" occurs 4x stream-wide (@1096, @1388, @1709, @1815); "42 06" 5x.
  The bigram is a normal word-internal letter sequence, not an anomaly.

## Adverse answered

The adverse warns that fencing "42-06-29" as word-internal "dissolves the
stem window". No live stem window is dissolved: the finite-06 reading at this
locus was ALREADY fenced by ent-06-host-census (cause: 42's class open).
The word-internal reading AGREES with the standing 06 decision rule
(finite "-ent" iff left neighbour is a verb stem — 42 is not one), so the
syllabic-06 function holds here with no §7 cost (value "ent" stays single;
only function varies, as the rule already grants).

## Fenced residuals (not verdict-blockers)

- 42's letter-cluster value is unnamed (42 class/value open).
- The infinitive's governor/subject is unnamed (50/15/61 open).
- The other three "06 29" windows (@1096/@1388/@1709) are not adjudicated here.

## Verdict: PROMOTE

C1 passes via the boundary arm; the rival boundary-before-29 parse is dead
at kill grade under standing doctrine; the adverse is answered with no live
window dissolved. No standing verdict contradicted or downgraded; §7 intact.
No follow-ups required (promote, not null).
