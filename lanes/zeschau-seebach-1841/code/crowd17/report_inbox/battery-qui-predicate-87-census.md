# Battery report: qui-predicate-87-census

**Target:** `qui-predicate-87-census` (priority 3)
**Verdict:** NULL (fence executed)
**Date:** 2026-10-09
**Parent:** battery-ce-qui-87-subject (null, 2026-10-09)

## Bar (verbatim, pre-registered)

> Bar: two or more windows license a qui-predicate with zero new assumptions, or fence @1775 as the sole licensor.

Restated as numbered clauses before testing:

- **C1 (two-license):** two or more of the five "87 64" windows license a
  qui-predicate — the immediate follower of 64=qui falls in a banked verb
  class (24 finite/modal class, 59=est* provisional, predicative frames
  37/32/42, or another banked verb class) — using standing values only, zero
  new assumptions.
- **C2 (fence):** if C1 fails, fence @1775 as the sole licensor of the
  qui-predicate frame.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005 never
touched. Scanned the full stream for the adjacency "87 64": exactly 5 hits,
independently re-derived (64 at @149, @181, @1768, @1776, @1801; 87 one pair
earlier — matches the parent's @148/@180/@1767/@1775/@1800 labeling of the
87 position). Censused the immediate follower of 64 in each window against
banked verb classes.

Standing values used: 87=ce (granted), 64=qui (promoted), 96=par (granted
preposition), 59=est* (provisional verb), 77=le* (provisional determiner),
24=finite/modal verb class (R17-009), 37/32/42 predicative frames (A1, value
open). 23 and 26 have no standing value.

Lock: no fresh lock existed for this target. Lockfile created at start,
deleted at end.

## Window-level evidence

| Window (64 @) | Follower | Standing class | Licensed? |
|---|---|---|---|
| @149 (a1_04) `... 87 64 | 96 47 46 ...` | 96 = par | No — preposition, not a verb class |
| @181 (a1_05) `... 87 64 | 23 37 06 ...` | 23 — no standing value | No — copula/verb at 23 is a new assumption |
| @1768 (a8_08) `... 87 64 | 26 37 78 ...` | 26 — no standing value | No — verb at 26 is a new assumption |
| @1776 (a8_09) `... 87 64 | 59 19 48 ...` | 59 = est* provisional verb | **Yes — "ce qui est"** |
| @1801 (a8_10) `... 87 64 | 77 84 59 ...` | 77 = le* provisional determiner | No — "qui le on est" ungrammatical |

Follower inventory: 96, 23, 26, 59, 77 — five distinct followers, zero of
which fall in the 24 finite/modal class or the 37/32/42 predicative frames.
Only the 59 follower is a banked verb. No follower required a banked value
to be contradicted; the four non-licensing windows fail on missing license,
not on forced falsity.

## Per-clause result

- **C1 FAIL:** exactly 1 of 5 windows licenses a qui-predicate (@1776,
  "ce qui est", using provisional-but-standing 59=est). The bar needs two.
- **C2 FIRES:** @1775 (87's offset; 64 at @1776) is fenced as the sole
  licensor of the "ce qui" + predicate frame among the five "87 64"
  windows. The other four windows are fenced, not killed: no standing or
  red-team verdict contradicts 87=ce or 64=qui at those loci.

No standing/red-team verdict contradicted or downgraded; §7 intact.
Canonical-stream caveat stands (68/70 row offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `qui-fol-23-26-value` (P3) — test whether 23 or 26 can carry
   copula/verb value under standing values via their other stream windows;
   a named verb value at either re-opens the @181/@1768 qui-predicate
   windows. Bar: name the value with ≥2 independent legs, or fence the
   followers as non-verbal.
2. `qui-59-1776-scope` (P4) — bound the sole-licensor window: parse the full
   predicate after 59=est* at @1776 (@1777=19 onward) with zero new
   assumptions; fence the clause's right edge if the parse runs out.
