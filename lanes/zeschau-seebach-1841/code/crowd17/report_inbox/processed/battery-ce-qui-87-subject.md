# Battery report: ce-qui-87-subject

**Target:** `ce-qui-87-subject` (priority 3)
**Verdict:** NULL (fence executed)
**Date:** 2026-10-09
**Parent:** battery-87-left-attach-census (null, 2026-10-09)

## Bar (verbatim, pre-registered)

> Bar: all five windows license "ce" as qui-subject with zero new assumptions, or fence.

Restated as numbered clauses before testing:

- **C1 (license):** each of the five "87 64" windows licenses 87=ce as the head
  of a qui-relative clause (64=qui as subject), using standing values only.
- **C2 (zero new assumptions):** no ungranted value and no new frame is used
  in any window's parse. Provisional standing values (59=est, 77=le) may be used
  but are flagged.
- **C3 (fence):** if C1 or C2 fails at any window, the claim is fenced (null),
  not killed — unless a window forces the claim false, which is kill grade.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005 never
touched. Scanned the full stream for the adjacency "87 64": exactly 5 hits,
at 0-based offsets 148, 180, 1767, 1775, 1800. Graded each window with ±8
context for (a) left closure before 87, (b) a licensed relative-clause
predicate after 64=qui (a verb-class or banked verb under standing values).

Standing values used: 87=ce, 64=qui, 96=par, 46=que, 47=ce, 79=tout,
84=on, 29=er, 94=ne, 24=finite/modal verb class (R17-009), 59=est*
(provisional), 77=le* (provisional), 37/32/42 predicative frames (value open,
A1), 78 nominal class (R18). 23, 26, 66 have no standing value.

Lock: no fresh lock existed for this target. Lockfile created at start,
deleted at end.

## Window-level evidence

**W1 @148 (a1_04):** `... 67 64 77 84 29 | 87 64 | 96 47 46 66 ...`
Left: `77=le*, 84=on, 29=er` — an "on …er" infinitive closes cleanly before 87.
Right: 64 is followed by `96=par` (granted preposition), then `47=ce 46=que`.
"qui par ce que" has no licensed predicate: qui needs a finite verb next,
and "par" is not one. The frame is not licensed here. It is not forced false
(87=ce and 64=qui stand) — it is simply unlicensed.
**Result: does NOT license.**

**W2 @180 (a1_05):** `... 69 14 24 | 87 64 | 23 37 06 00 ...`
Left: `24` (verb class) closes before 87 — clean.
Right: 64 is followed by `23` (no standing value), then `37` (predicative
frame, value open). "qui 23 37" would need 23 to be a copula/verb — that is a
new assumption. The frame is not licensed here.
**Result: does NOT license.**

**W3 @1767 (a8_08):** `... 84 09 24 | 87 64 | 26 37 78 62 ...`
Left: `24` (verb class) closes before 87 — clean.
Right: 64 is followed by `26` (no standing value), then `37` predicative and
`78` nominal class. "qui 26 37 78" would need 26 as a verb — a new assumption.
The frame is not licensed here.
**Result: does NOT license.**

**W4 @1775 (a8_09):** `... 62 94 24 | 87 64 | 59 19 48 74 65 ...`
Left: `94=ne, 24` (verb class) — the left clause closes before 87, clean.
Right: 64 is followed by `59=est*` (provisional standing verb). "ce qui est …"
is a fully licensed relative-subject frame under standing values: 87=ce head,
64=qui subject, 59=est predicate. Provisional value used, flagged per C2.
**Result: LICENSES.**

**W5 @1800 (a8_10):** `... 94 59 37 91 79 | 87 64 | 77 84 59 35 ...`
Left: `79=tout` (granted) — "tout ce qui" opens cleanly.
Right: 64 is followed by `77=le* 84=on 59=est*` — "qui le on est" is not a
licensed predicate. 77 is provisional "le", not a verb. The frame is not
licensed here.
**Result: does NOT license.**

## Per-clause result

- **C1 FAIL:** 1 of 5 windows licenses the frame (@1775). Four windows do not
  (@148, @180, @1767, @1800). The bar is conjunctive — it needs all five.
- **C2 HOLD (as constraint):** zero new assumptions were used; the four
  non-licensing windows are exactly the ones where a new assumption (a copula
  at 23/26, an elided verb at @148, a verb at 77) would be required.
- **C3 FIRES:** no window forces the claim false — no banked value contradicts
  87=ce or 64=qui, and the unlicensed windows need assumptions, not
  contradictions. So the claim is fenced (null), not killed.

The "87 64" adjacency is real and stable (5 hits, byte-exact), but only one
window (@1775, "ce qui est") licenses the relative-subject frame at battery
grade. The other four need ungranted assumptions to complete the clause.

No standing/red-team verdict contradicted or downgraded; §7 intact.
Canonical-stream caveat stands (68/70 row offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `qui-predicate-87-census` (P3) — census the immediate follower of 64 in all
   five windows against banked verb classes (24 class, 59=est*, predicative
   frames 37/32/42); bar: two or more windows license a qui-predicate with
   zero new assumptions, or fence @1775 as the sole licensor.
2. `ce-qui-148-par-rival` (P3) — @148 "ce qui par ce que": test whether
   96=par after qui kills the relative reading there or licenses an
   elliptical-agent reading; bar: kill-or-license at battery grade, or fence.
3. `ce-qui-left-closure` (P3) — test left-closure uniformity before 87 across
   the five windows (24-verb x3, 29-er infinitive, 79-tout); bar: all five
   lefts close with zero new assumptions, or fence the outlier windows.
