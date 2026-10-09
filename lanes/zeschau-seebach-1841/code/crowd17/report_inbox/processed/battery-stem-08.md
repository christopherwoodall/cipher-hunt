# Battery report: stem-08 — "08 disambiguation"

Worker: battery-worker-stem-08 (f954611b-afdc-4649-98e8-de3347592429), 2026-10-09.
Lock: created fresh (no stale lock present). Stream: repaired 1,847-pair parse
(code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per
code/side-keyhunt/repair_parse.py). canonical.py never touched. R5005, sealed
gate instances, and the red-team adjudication queue never touched. All numbers
trace to the stream.

## Bar (verbatim, pre-registered)

"resolve iff contact profile decides; do not force"

## Bar restated as numbered clauses (fixed before testing)

- C1 (resolve): the contact profile of 08 decides — exactly one of the
  candidates {ne, se, on, spelling-letter} is consistent with all 18 of 08's
  windows AND cleanly separable from granted 84="on" (A15) and promoted 94="ne".
- C2 (do not force): if C1 cannot be met — the windows cannot cleanly separate
  08 from the granted/promoted values, or no candidate covers all windows —
  the verdict is null. Never a forced promote or kill.

## Method

Enumerated all 18 windows of 08 on the repaired stream with ±5 context.
Censused predecessor/successor distributions for 08 vs 84 ("on", granted A15),
94 ("ne", battery-promoted), 48/12 (promoted letter band), 31, 40, 67.
Tested each candidate against every window; applied the §7 sole-polyvalence
rule (67 et/veut) where 67 contacts 08.

## Window-level evidence (@-offsets, repaired stream)

n(08) = 18. Predecessor top: 60 x2, 67 x2, 37 x2, 40 x2. Successor top:
31 x3, 65 x2, 62 x2.

- @35 (a1_01): 32 01 [08] 91 39
- @60 (a1_01): 12 41 [08] 34 29 40 — 08 directly precedes 34-29-40 = "i"+"er"+"e"
  ("-iere"); sits inside a letter run (12="n" letter promoted, 34="i" banked,
  29="er" banked, 40="e" banked). Strongest spelling leg.
- @98 (a1_02): 29 85 [08] 21 62 94 93 59 — cf. verb-93's F7 gloss "'on ne [93] est'".
- @198 (a2_00): 21 60 [08] 67 76
- @534 (a3_01): 32 16 [08] 24 82
- @631 (a4_01): 78 67 [08] 52 67 — "et/veut 08"; 08 word-initial after a word.
- @779 (a5_04): 73 37 [08] 29 89
- @881 (a5_08): 78 17 [08] 31 79 — "fois 08 [31-finite]".
- @922 (a5_09): 74 40 [08] 65 71 — "e(40) 08"; 40-08 x2 (see @944).
- @944 (a5_10): 50 40 [08] 62 98 — "e(40) 08".
- @975 (a6_01): 51 45 [08] 01 00 — "ce(45) 08"; word-initial after "ce".
- @1302 (a7_03): 70 37 [08] 43 21
- @1323 (a7_04): 29 80 [08] 62 98
- @1339 (a7_05): 64 60 [08] 65 64
- @1488 (a7_10): 24 87 [08] 31 92 — "ce(87, promoted) 08 [31-finite]".
- @1520 (a7_11): 91 67 [08] 31 24 — "et/veut 08 [31-finite]".
- @1592 (a8_02): 29 47 [08] 81 03
- @1610 (a8_03): 65 23 [08] 55 83

31's profile (n=8): predecessors 08 x3, 64 x2, 61 x1, 11 x1, 48 x1.
"qui 31" x2 (@337, @1646; 64="qui" promoted) → 31 is finite-verb-shaped.
The queue's "(before finite verbs)" gloss for "08 31" x3 is confirmed.

Anchor-frame separation counts (repaired stream):
- 62-08: 0 (vs 62-94: 9, the "il ne" near-fixed pair)
- 77-08: 0 (vs 77-84: 7, "l'on"); 46-08: 0 (vs 46-84: 2, "qu'on")
- 08-59: 0 (vs 84-59: 4 "on est"; vs 94-59: 3 "n'est")
- 12-08: 0 (vs 12-94: 3, "n'" elision); 82-08: 0 (vs 82-94: 3, "m'" elision)
- 08-82: 0 (vs 94-82: 4); 08-94: 0; 40-48: 0 (vs 40-08: 2; 40-12: 1, the
  promoted "en"=40-12 composition)

## Per-candidate results

**"se" — KILLED (kill grade).** 08-31 x3 with 31 finite-verb-shaped. Reflexive
"se" + finite verb requires a subject; all three windows are subjectless even
under clause-boundary fencing: @1520 "et se [31]" (67="veut" would need 31
infinitive — contradicted by "qui 31" x2; 67="et" leaves "et se [finite]"
broken), @881 "fois se [31]", @1488 "ce se [31]". 3/3 windows ungrammatical.
No rescue available.

**"on" — WEAKENED, fenced; not promotable, not cleanly killable.** Positive:
@1520 "et on [31]" parses cleanly; @881 "fois, on [31]" parses with a clause
boundary; @98 "…on [21] | il ne [93] est…" fenceable with a boundary at 21-62.
Negative: ZERO of A15's anchor frames (77-08 x0, 46-08 x0, 08-59 x0) and zero
elision contact (12-08 x0, 82-08 x0) — a vowel-initial "on" should attract
"l'/qu'" frames the way 84 does. @1488 "ce on" adjacency is ungrammatical as
written; fenceable only as "que l'on [24-modal] ce | on [31]…" (load-bearing on
24's promoted modal-verb class and "ce" as its object — strained, recorded as
fenced with cause, not clean). Homophony with granted 84 would require the full
{33,86}-precedent homophony bar (uniformity + permutation test); not attempted
here — asserting it would be forcing.

**"ne" — ZERO positive legs; inseparable without forcing.** Complete anchor
separation from promoted 94 on every frame (62-08 x0, 12-08 x0, 82-08 x0,
08-59 x0, 08-82 x0). No "ne"-frame parses without ungranted assumptions
("et ne [31]" needs 24="pas" at @1520; literary "ne"-alone cannot be ruled out,
so not kill-grade). Promoting 08="ne" would assert homophony with 94 — forcing.

**"spelling-letter" — real legs, but killed as a pure word-internal reading.**
Legs: @60 "08-iere" (08 before 34-29-40 inside a letter run); 40-08 x2
("e"+08, cf. promoted "en"=40-12); 08-34 x1. Killed as word-internal: 08 is
word-initial after full words at @631/@1520 (67="et/veut"), @1488 (87="ce"),
@881 (17="fois"), @975 (45="ce") — a letter cannot sit word-internally after a
word boundary. The surviving variant (word-initial syllable/prefix composing
with 31: "08-31" x3 as prefix+verb, 31 standing bare at "qui 31" x2) is outside
the stated candidate set and untested.

## Adverse (answered, not ignored)

"spelling vs clitic readings pull opposite ways" — CONFIRMED real and
decisive. @60 + 40-08 x2 pull spelling; 67-08 x2 + 87-08 + 17-08 + 45-08 pull
clitic (word-initial position). Neither reading covers all 18 windows. This
tension is exactly why C1 fails; it is the finding, not a loose end.

## Per-clause pass/fail

- C1 (resolve): FAIL. "se" killed at kill grade; "on" weakened/fenced with zero
  A15 anchors; "ne" zero legs; spelling-letter contradicted at word-initial
  windows. The contact profile does not decide — no candidate is consistent
  across all 18 windows and cleanly separable from 84/94.
- C2 (do not force): HOLDS → verdict follows C2.

## Verdict

**null** — the contact profile does not decide 08's value. "se" is eliminated
at kill grade (recorded above for downstream use); "on"/"ne" cannot be
separated from granted 84="on" / promoted 94="ne" without forcing; the
spelling reading survives only in a word-initial syllable/prefix form outside
the tested candidate set. No standing red-team verdict is contradicted, so no
escalation; per §5 no overwrite of anything.

## Follow-ups (nulls regenerate work)

1. **prefix-08-31** — test 08 as a word-initial verbal prefix/syllable:
   "08-31" x3 (@881/@1488/@1520) as prefix+finite-verb vs bare "qui 31" x2
   (@337/@1646); compositional check modeled on promoted 82-48="me".
   Bar: resolve iff 08+31 parses as one prefixed verb at all 3 windows with
   31's bare-verb frames intact; kill iff any window needs 08 as a separate word.
2. **on-08-homophony** — full homophony battery 08~84 per the {33,86} precedent
   (1690 uniformity + permutation test on predecessor/successor classes),
   with @1488's "ce | on" clause-boundary adjudicated (load-bearing: 24's
   modal-verb class, "ce" as object). Bar: merge iff distributions
   indistinguishable AND the boundary parse holds; else "on" stays fenced.
3. **ne-08-frames** — sweep 08's 18 windows for "ne"-frames with a "pas"-slot
   audit (any "pas" candidate after 08+verb?); joint with 24's promoted
   modal-verb class at @1488/@1520. Bar: promote-08="ne"-frame iff >=2 clean
   "ne…(pas)" frames parse; else record the zero-leg sweep as the kill-grade
   baseline for any future "ne" claim on 08.
