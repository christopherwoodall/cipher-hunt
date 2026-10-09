# Battery report: 87-left-attach-census

**Target:** `87-left-attach-census` (priority 3)
**Verdict:** NULL (fence executed)
**Date:** 2026-10-09

## Bar (verbatim, pre-registered)

> systematic left-closing pattern with byte evidence at battery grade; fence if no pattern

Restated as numbered clauses before testing:

- **C1 (pattern):** "X 87" shows a systematic left-closing pattern — 87='ce' is clause-final (the left clause ends at 87) at battery grade with byte evidence.
- **C2 (fence):** if no systematic pattern exists, the claim is fenced (null), not killed — 87's roles are described, not denied.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(asserts held: 1,847 pairs, 96 types). `canonical.py` never used.
Censused all 32 87-windows (0-based offsets) with ±3 context, then graded
each window as LEFT-CLOSING (87 clause-final, "V ce" / "par X ce" object),
NON-CLOSING (87 opens a clause or is NP-internal), FENCED, or INDETERMINATE
using standing values only.

Standing values used: 87=ce, 64=qui, 46=que, 96=par, 82=m, 29=er, 79=tout,
59=est*, 77=le*, 84=on* (granted); 94='ne' (battery-promoted free word);
24 = finite/modal-shaped verb class (R17-009); 78 nominal-class, 81 noun,
65 noun (R18); 67 positional et/veut rule; A10 "33 29"; x-33-37-licensing
PROMOTE (2026-10-09): @628 = "laisser ce [78]!" with 87 as determiner.

n(87) = 32. Predecessors: 24 x10, 29 x3, 96 x3, 43/56/76/79/81 x2, 09/52/70/74/77/94 x1.
Followers: 11 x7, 64 x5, 46 x3, 01/77/78/83 x2, 08/14/59/61/63/74/76/86/98 x1.

## Window-level evidence

**LEFT-CLOSING (6):** 87 = clause-final object pronoun.
- @163 (a1_05): `52 94 24 87 11` — "ne [24] ce, la...": 94='ne', 24 verb-class;
  ce = direct object; 11=la opens a new clause.
- @344 (a2_05) / @1028 (a6_03): `64 96 43 87 01` — "qui par [43] ce":
  96=par; ce = object of the par-phrase, phrase-final.
- @824 (a5_05): `24 87 59 38` — "[24] ce, est [38]": ce object; 59=est*
  starts a new clause.
- @830 (a5_06): `82 01 24 87 11` — "m' [24] ce la": 82='m' proclitic;
  ce = object.
- @1426 (a7_08): `67 33 29 87 63` — "veut [33]er ce": 67='veut'
  (33+29 infinitive-shaped positional rule); ce = object of the infinitive.

**NON-CLOSING, clean (7):**
- "ce qui" x5 — 87 heads the relative clause as subject; the left clause
  closes *before* 87, not at it: @148 (a1_04) `[29]er ce qui`, @180 (a1_05)
  `[24] ce qui`, @1767 (a8_08) / @1775 (a8_09) `[24] ce qui`,
  @1800 (a8_10) `tout ce qui` (79=tout granted).
- Determiner "ce [78-N]" x2 — 87 is NP-internal, not clause-final:
  @572 (a3_02) `52 87 78`, @628 (a4_01) `[33]er ce [78]` ("laisser ce [78]!",
  battery-promoted reading; 78 nominal-class granted).
- Secondary non-closing: "ce que" x3 (@225 a2_01, @953 a6_00, @1527 a8_00)
  — 87 is the antecedent *inside* the subordinate clause (clause-initial
  there); the left phrase ends before 87.

**FENCED (7):** @71 (56 verb-family class unsettled), @191 (66 class open),
@515 (56/88 interaction), @225/@953/@1527 (ce-que rival parse: if "ce" is
taken as object of the left par-phrase the window is arguably closing —
two parses, no battery-grade choice), @644 (pending `det-87-644-function`).

**INDETERMINATE (12):** @74, @174, @201, @461, @613, @869, @1170
(ne-ce-1169 fence venue), @1242/@1403, @1274, @1487, @1636 — open-class
neighbors both sides; no licensed parse either way at battery grade.

## Per-clause result

- **C1 FAIL:** 6/32 windows clearly close the left clause; 7/32 clearly do
  not (5 ce-qui + 2 ce-det); 3 more are secondarily non-closing. No
  systematic left-closing pattern exists — 87 is polyfunctional: object
  pronoun (clause-final), determiner ("ce [78]", NP-internal), and
  relative-clause head ("ce qui", clause-opening).
- **C2 FIRES:** claim fenced, not killed. The six closure windows are real
  battery-grade instances (e.g. @163 "ne [24] ce", @344/@1028 "par [43] ce",
  @1426 "veut [33]er ce"); the claim's error is the *systematic* scope,
  which the seven clean counter-instances falsify.

No standing/red-team verdict contradicted or downgraded; §7 intact.
Canonical-stream caveat stands (68/70 row offsets unvalidated; the two
byte-identical "64 96 43 87 01" windows @344/@1028 give this locus
repetition leverage independent of offsets).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `ce-qui-87-subject` (P3) — census "87 64" x5 as a relative-subject frame;
   bar: all five windows license "ce" as qui-subject with zero new
   assumptions, or fence.
2. `det-87-78-frame` (P3) — test the "ce [78]" determiner reading at both
   78-windows (@572/@628) against the "87=object" rival; bar: determiner
   parses at both under standing values, or fence.
3. `obj-87-closure` (P3) — test the six "V/par ce" closure windows as a
   uniform object-closure frame once 24's class is banked; bar: uniform parse
   with <=1 ungranted assumption, or fence @824/@830 as 24-load-bearing.
