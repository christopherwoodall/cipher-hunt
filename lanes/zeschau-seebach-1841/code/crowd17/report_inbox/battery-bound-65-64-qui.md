# Battery report: bound-65-64-qui

- Target id: `bound-65-64-qui`
- Claim: right-edge '65|qui' boundary test across all three 65->64 windows (@724, @1208, @1340)
- Date: 2026-10-09
- Worker: battery worker (subagent 274ff898-1753-4582-85aa-a683f42fcbe1)
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`).
  All @-offsets are 0-based repaired-stream indices. n(65->64) = 3, verified by
  byte-exact census (@724, @1208, @1340). `canonical.py` never used.
  R5005, sealed gate instances, and the red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/bound-65-64-qui.lock` (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"resolve iff the '65|qui' boundary is confirmed or rejected at all three
windows with the '21 65' predecessor gate stated"

Numbered pass/fail clauses (restated before testing, not modified after):

1. C1: the '65|qui' boundary is CONFIRMED or REJECTED at @724, with the
   '21 65' predecessor gate stated.
2. C2: the '65|qui' boundary is CONFIRMED or REJECTED at @1208, with the
   '21 65' predecessor gate stated.
3. C3: the '65|qui' boundary is CONFIRMED or REJECTED at @1340, with the
   '21 65' predecessor gate stated.

Boundary test standard (stated before testing): a clause boundary at 65|64 is
CONFIRMED iff (a) the left span licenses 65 as clause-final — i.e. a complete
clause whose finite verb is granted, ratified, or byte-evidenced at battery
grade — AND (b) 64's qui-clause parses as an independent clause with a
licensed finite verb. It is REJECTED iff the left fails (a) — battery-grade
finite-verb inventory only: granted values, R18 ratifications, and promoted
battery findings are NOT licensees until the red team ratifies them. A qui-clause
with no licensed finite verb is a residual, not a boundary rescue.

## Method

1. Re-derived the repaired parse in-session (1,847 pairs, 96 groups). Never
   used canonical.py. R5005 not touched.
2. Ran a byte-exact census of 65->64 bigrams: exactly 3 windows
   (@724, @1208, @1340). Counts match the brief.
3. For each window, pulled +/-12 context and ran a finite-verb inventory
   against the lane's standing register (granted / R18-ratified only;
   battery-promoted but unratified items flagged as unlicensed).
4. Ran a 65-predecessor census for the gate: predecessors = 21 x4, 40 x3,
   91 x2, 74 x2, 24 x2, 08 x2, 06 x2, 94/60/98/78/41/64/92/79 x1 each.
   '21 65' bigram census: exactly 4 stream-wide (@134, @371, @1207, @1529) —
   the @1207 bigram is the predecessor of the @1208 window.

## Window-level evidence

### W1 @724 (row a5_02): `... 77 03 91 [65] [64] 11 00 86 48 88 11 24 85 ...`

**Predecessor gate:** 65's predecessor is 91 (not 21). '21 65' gate not
applicable; @724 is not one of the four '21 65' bigrams.

**Left span** (@712-723): `12 63 00 66 86 01 02 21 80 77 03 91` —
finite-verb inventory: 63 (verb-class, battery-PROMOTE, UNRATIFIED —
not a licensee), 86 (INF class, registry — cannot be finite),
80 (A8 verb-frame, value open — cannot license finiteness).
No granted/ratified finite verb anywhere on the left. Even granting
63 (battery-grade only), the span 63->65 runs 12 tokens
(`63 pour [66] 86 01 02 21 80 le 03 91 65`) with no licensed second
finite verb and no licensed way to fence the interior — the clause
cannot close at 65. (a) FAILS.

**Right span** (qui @725): `qui 11 00 86 48 88 11 24 85 93` —
finite-verb candidates: 88 (verb-class, battery-PROMOTE, unratified),
24 (finite-modal, battery-PROMOTE, unratified). Even granting them,
both fail on the bytes: 88 needs "qui la pour [86]e [88]" (ungrammatical
insertion between object and verb); 24 needs
"qui la pour [86]e 88 la [24] [85]" (two unlicensed insertions).
(b) FAILS.

**Verdict for C1: REJECTED.** 65 is not clause-final at @724; no clause
boundary at 65|64. The locus is a residual (both sides unlicensed), not
a boundary.

### W2 @1208 (row a7_00): `... 55 61 21 [65] [64] 59 32 48 96 45 36 77 ...`

**Predecessor gate:** 65's predecessor is 21 — one of the four '21 65'
bigrams (@1207). "21 65" is a noun-noun juxtaposition: 21 is
battery-promoted NOUN (pending ratification), 65 is ratified noun
class (R18-001). The gate does not block either reading on its own:
a "21 65" NP (possibly appositive) can end a clause or sit mid-clause.
The gate therefore defers to the finite-verb test.

**Left span** (@1196-1207): `96 82 16 64 29 45 58 47 43 55 61 21` —
finite-verb inventory: EMPTY. 16 is value-open (infinitive/a crisis,
unresolved). No granted or ratified finite verb anywhere on the left;
65 cannot be licensed as clause-final. (a) FAILS.

**Right span** (qui @1209): `qui 59 32 48 96 45 36 77 83 92` —
with provisional 59='est': "qui est [32] [48]" = "qui est [32]-e",
a predicative frame on 32 (A1 granted predicative frames: 37/32/42).
"65, qui est [32]-e" = "65, who is [32]" — a clean relative clause
anchored on 65, needing nothing beyond provisional 'est'. This is the
single cleanest window of the three: qui attaches directly to 65,
which is the opposite of a boundary.

**Verdict for C2: REJECTED.** No clause boundary at 65|64; qui attaches
as a relative clause on 65 (conditional on provisional 59='est').

### W3 @1340 (row a7_05): `... 60 08 [65] [64] 52 38 47 86 66 73 34 ...`

**Predecessor gate:** 65's predecessor is 08 (not 21). '21 65' gate not
applicable.

**Left span** (@1328-1339): `06 62 94 70 52 39 83 86 71 64 60 08` —
finite-verb inventory: only 86 (INF class, registry — cannot be finite).
62's 'on' value is unconditioned-ELIMINATED (seg-81-30-boundary);
62 nominal values (regne/trone) are not finite. 94 is particle/syllabic,
never finite. 65 cannot be licensed as clause-final. (a) FAILS.

**Right span** (qui @1341): `qui 52 38 47 86 66 73 34 62 48 77 78 94` —
finite-verb inventory within 14 tokens: only 86 (INF). 38's determiner
arm is kill-grade dead (adj-37-385-gate); 52/38/47/62/73/78 are all
non-finite under standing values. qui's clause is verbless within the
window — a residual, not a new clause. (b) FAILS.

**Verdict for C3: REJECTED.** 65 is not clause-final at @1340; no clause
boundary at 65|64. qui's clause is an unlicensed residual, which does
not rescue a boundary.

## Per-clause pass/fail

1. C1 (@724): PASS — boundary REJECTED (left: no licensed finite verb;
   right: qui-clause unlicensable even granting unratified promotes;
   predecessor 91, gate n/a).
2. C2 (@1208): PASS — boundary REJECTED (left: zero finite-verb inventory;
   "qui est [32]-e" parses cleanly as a relative on 65 under provisional
   59='est'; predecessor 21 — the '21 65' gate stated, noun-noun
   juxtaposition, defers to the finite-verb test).
3. C3 (@1340): PASS — boundary REJECTED (left: only INF 86; right: qui-clause
   verbless within 14 tokens; predecessor 08, gate n/a).

## Adverse answered

- "65's value open": answered — the test used only 65's ratified noun
  CLASS (R18-001), never its value. No value hypothesis was assumed,
  tested, or promoted anywhere in this verdict.

## Verdict: PROMOTE

The right-edge '65|qui' boundary is uniformly REJECTED at all three
windows. Findings for the lane record (battery grade, needs red-team
ratification):

- qui attaches as a relative clause on 65 (cleanest at @1208:
  "65, qui est [32]-e" under provisional 59='est').
- @724 and @1340 are residuals: neither side licenses a complete clause
  at the junction — no boundary, but also no clean qui-clause.
- The '21 65' predecessor gate (@1207): noun-noun juxtaposition; does
  not itself license or block clause-finality — the finite-verb test
  governs.

## Caveats

- Canonicality caveat stands (protocol §7): rows a5_02, a7_00, a7_05 are
  offset-0 rows and their upstream offsets are unvalidated. This verdict
  lives on the canonical stream; a rival offset for any of these rows
  re-opens the window.
- @1208's clean relative parse is conditional on provisional 59='est'.
  If 'est' falls, the qui-clause at @1208 degrades to residual grade.
- No standing red-team verdict contradicted or downgraded. §7 intact.
- This verdict names no value and no class; it records a structural
  resolution only. No follow-ups required (promote, not null).
