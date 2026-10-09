# Battery report: det-87-78-frame

**Target:** `det-87-78-frame` (priority 3)
**Verdict:** PROMOTE
**Date:** 2026-10-09
**Lock:** created `locks/det-87-78-frame.lock` at start; no competing fresh lock found; deleted on completion.

## Bar (verbatim, pre-registered)

> Bar: determiner parses at both under standing values, or fence.

Restated as numbered clauses before testing:

- **C1 (parse @572):** the determiner reading "ce [78]" parses at @572 under standing values only (zero new assumptions), or the claim fences.
- **C2 (parse @628):** the determiner reading "ce [78]" parses at @628 under standing values only (zero new assumptions), or the claim fences.
- **C3 (fence):** if either window cannot parse under standing values, the claim is fenced (null), not killed.

Adverse named in the work order: **"87=object" rival** — 87 is the object pronoun of the left verb, and 78 heads a fresh clause, at one or both windows.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(asserts held: 1,847 pairs, 96 types). `canonical.py` never used.
R5005 itself never touched. Offsets are 0-based pair positions.

Standing values used (granted only): 87=ce, 47=ce (A4 allophone tier),
45=ce (A11 hold), 11=la, 94=ne (free word, promoted), 96=par,
37/32/42 predicative frames (A1), 33+29 infinitive-shaped (A10),
78 nominal-class (R18), 67 positional et/veut rule, 24 verb class (R17-009).
Battery-promoted reading x-33-37-licensing (2026-10-09): @628 =
"laisser ce [78]!" with 87 as determiner.

Censuses in-session: n(78)=31; predecessors of 78 include 47 x5, 77 x7,
11 x2, 37 x4, 87 x2; followers of 78 include 45 x4; "87 78" bigrams
occur exactly twice in the stream (@572/@628); "47 78" bigrams occur 5x;
"45 78" bigrams occur 0x.

## Window-level evidence

### @572 (a3_02): `45 94 52 87 78 45 13`

Determiner parse: `87 78` = "ce [78]" — NP-internal demonstrative +
78-nominal head. Licensed under standing values: 87=ce granted;
78 nominal-class granted (R18); the "ce [78]" frame has direct
precedent — 47="ce" (granted, A4) precedes 78 in 5 other windows, and
11="la" (granted) precedes 78 twice. Zero new assumptions.

Object rival: needs 52 to be a verb taking "ce" as object
("ne [52] ce"). 52's class is unsettled: the banked verb class is 24
(R17-009); 52 follows 94='ne' three times (suggestive, not banked) and
precedes 87 exactly once. The rival adds one ungranted assumption and,
even if granted, leaves 78 heading a clause with no licensed verb
nearby. At battery grade the rival is unlicensed: fenced, with stated
cause.

Follower check: 78 is followed by 45="ce" (A11). The same follower
appears in 4 of the other 29 78-windows — a normal continuation, not an
obstacle.

### @628 (a4_01): `37 33 29 87 78 67 08`

Determiner parse: 37-A1 + 33+29-A10 = predicative frame + infinitive
("laisser"), 87="ce" determiner, 78-nominal head: "laisser ce [78]!".
This is already the battery-promoted x-33-37-licensing reading
(2026-10-09), licensed under standing values only.

Object rival: the promoted reading already rules. Under the rival,
"laisser ce" (object) plus a new clause headed by 78 — but the
demonstrative-nominal frame is the granted parse, and the rival
explains nothing the promoted reading does not.

Follower 67: 67=et unless follower is infinitive-shaped (positional
rule); 08's class is open. Either value leaves the determiner parse
untouched.

## Per-clause result

- **C1 PASS:** determiner parses at @572 under standing values; it is the
  only parse needing zero new assumptions. The object rival needs
  ungranted 52=verb — fenced with stated cause.
- **C2 PASS:** determiner parses at @628 under standing values; matches
  the battery-promoted reading.
- **C3 does not fire:** no failure to parse.

## Verdict: PROMOTE

All bar clauses pass. The "87=object" adverse is answered: fenced at
@572 (ungranted 52=verb assumption, stated cause) and superseded at
@628 by the battery-promoted x-33-37-licensing reading. Both 78-windows
license "ce [78]" as a determiner NP with 87 NP-internal, consistent
with the five "47=ce [78]" precedent windows and the two "11=la [78]"
precedent windows.

Standing/red-team verdicts untouched; §7 constraints intact. The 52
class (verb or not) stays open and is fenced here, not resolved.
