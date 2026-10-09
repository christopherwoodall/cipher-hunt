# Battery report: qui-02-609-parse

- Target id: `qui-02-609-parse`
- Claim: "Deep parse of the first qui-window ('64 39 64 02 58 47', 0b@607-613, row a4_00) dissolves its verb requirement, dropping 02's qui-legs to one from the other side."
- Date: 2026-10-09
- Worker: battery worker (subagent f23ebf1b-4f20-4d27-b56b-512cdcf1197a)
- Stream: repaired 1,847-pair / 96-type parse, re-derived in-session from
  `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
  (parsed per `code/side-keyhunt/repair_parse.py`; asserts held).
  `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, pre-registered)

"deep parse the first qui-window ('64 39 64 02 58 47', 0b@607-613, row a4_00);
if its verb requirement dissolves there, qui-legs drop to one from the other side."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (deep parse executed):** every live dissolve route for the verb
   requirement on 02 at the @609 window is tested against the repaired
   stream and standing values (Routes A–G below).
2. **C2 (conditional):** IF a route dissolves the verb requirement on 02 at
   battery grade (FORCED, not merely compatible — stem-03-value precedent,
   same standard the sibling `qui-02-750-parse` applied), THEN 02's
   qui-legs drop to two→one (only @750's leg stands).

Verdict rule: **promote** iff C2 fires (dissolve forced); **kill** iff a
window forces the claim false at kill grade; **null** otherwise, with 1–3
follow-ups per §4.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/qui-02-609-parse.lock` on start (agent id
   + 2026-10-09T10:22:32Z); deleted on completion.
2. Re-derived the repaired stream byte-exact (1,847 pairs / 96 types).
3. Adopted, not re-litigated: 64="qui" banked GT; 47="ce" (A4 allophone
   tier); 77="le" provisional; ant-58-ending's KILL of 58="ant"
   (present-participle ending); 58-complement-1695's PROMOTE (58 in
   gerund-complement nominal position @1695 — pro-nominal datum);
   cede-614-subject's NULL (58's class open at battery grade; verb-ending
   killed, free-verb readings ungrammatical at @1202);
   battery-02-class-609's NULL (02's class an established §7 split
   candidate: verb-selecting "qui [02]" ×2 vs verb-excluding @305/@858);
   qui-02-750-parse's NULL (@750's leg stands, phase-solid on gloss-anchored
   row a5_03).
4. Indexing note: the 6-group sequence "64 39 64 02 58 47" is byte-confirmed
   at **0b@606–611** (queue label "0b@607-613" is off by one; the bytes are
   unambiguous). 02 at 0b@609, 58 at 0b@610, row a4_00 mid-row.

## Window-level evidence (all byte-verified)

Locus, 0b@602–614, row a4_00:

    96 45 93 54 | 64 39 64 02 58 47 | 77 87 83
    par ce [93] [54] | qui [39] qui [02] [58] ce | le ce [83]

- 64="qui" banked GT (both); 96="par" granted; 45="ce" (A11 HOLD);
  47="ce" (A4); 77="le" provisional.
- "64 02" occurs exactly 2× stream-wide (0b@608, 0b@749) — the two
  qui-windows; no other "qui [02]" contact exists.
- 58: n=7 — [55, 122, 157, 610, 1202, 1695, 1756]; predecessors
  {85:3, 19:1, 35:1, 02:1, 45:1}; successors {35:2, 47:2, 66:1, 15:1, 17:1}.
  "02 58" is a stream hapax (only @609–610).
- 02: n=17 — [128, 305, 410, 459, 495, 609, 695, 718, 750, 858, 887, 916,
  1084, 1152, 1299, 1467, 1819]. Zero verb-frame contacts in the successor
  set (02-class-609 census, re-confirmed).
- 39: n=13; class open (antec-08-91-39 NULL found nothing nameable).

## Dissolve routes tested

**Route A — 58 as the finite verb, 02 as nominal subject:**
"qui [02-S] [58-V] ce[=cela]" — object-relative ("l'homme qui Marie
voit"-shaped), grammatical French. The only route with real licensing.
- 58-verb: NOT forced. 58's class is open (cede-614-subject NULL); the
  bound verbal ending is kill-grade dead (ant-58-ending); the only
  class-level promote on 58 is pro-NOMINAL (58-complement-1695 @1695);
  @1695/@1756 ("24-85-58") are uninterpretable pending adjudication of
  the 24="en" (A3 GT) vs 24=finite-verb standings conflict.
- 02-nominal-subject: NOT forced. 02's nominal legs (@128 "la [02] [26]",
  @1467 "21 [02]") are compatible, not forced; 02 is a §7 split candidate.
- **Route verdict: COMPATIBLE, not FORCED.** Per the stem-03-value
  precedent (cited in qui-02-750-parse), compatible-not-forced does not
  dissolve the leg at battery grade. Route does not fire.

**Route B — word/clause boundary between the second 64 and 02**
("qui [39] | qui [02]..."). Mid-row a4_00, same row both sides, no
punctuation, no formula marker, no gloss marker, no crib at the contact.
**FENCED with stated cause** (same finding as qui-02-750-parse Route B).

**Route C — sub-lexical "02 58" as one word.** "02 58" is a hapax; 02 has
no established letter-tier neighbors; no composition evidence at battery
grade. `sub02-wordinternal` is already queued as the venue for this
avenue — not duplicated here. **FENCED** (no battery-grade premise).

**Route D — interrogative "qui".** "Qui [02] [58] ce?" — interrogative
"qui" still requires a finite verb in its clause; the verb requirement on
{02, 58} does not dissolve. **No dissolve.**

**Route E — 39 as the finite verb closing the first relative**
("[54] qui [39-V]"). 39's class is open (no forced verb reading in its 13
windows); even if 39 were the verb, the second clause "qui [02] [58] ce"
still requires a finite verb. **No dissolve.**

**Route F — double-qui as one construction.** French has no double-qui
single construction ("qui [39] qui [02]" cannot fuse). **No dissolve.**

**Route G — 02 as object of 39** ("qui [39-V] qui [02-obj]..."). Requires
39-verb (unforced, see Route E) AND still needs a verb in the second
qui-clause. **No dissolve.**

## Per-clause pass/fail

- **C1: PASS** — all seven routes tested against the repaired stream with
  stated byte evidence; no route ignored.
- **C2: antecedent NOT met** — no route dissolves the verb requirement on
  02 at battery grade. Route A is the live compatible alternative but is
  not forced; Routes B/C fenced with stated cause; Routes D–G do not
  dissolve on their own terms.

## Adverse answered

"strengthened anchoring only applies to @750 (a5_03 gloss-anchored);
@609's window lacks that phase-solidity — it is the weaker leg."
Acknowledged and converted into follow-up 3: because @609 lacks the
gloss-anchored phase-solidity that protected @750 from the offset-1
resegmentation rescues, a rival row-phase re-test of a4_00 is the honest
remaining dissolve avenue at this window (not executed here — no rival
offsets are validated at battery grade).

## Verdict: NULL

The bar's conditional does not fire: the verb requirement on 02 at @609
survives every dissolve route at battery grade. 02's qui-legs stand at two
(@609, @750) — consistent with (not contradicting) qui-02-750-parse's NULL
and 02-class-609's NULL. No standing or red-team verdict contradicted or
downgraded; §7 intact (no polyvalence declared); canonical-stream caveat
stands (row a4_00 offset unvalidated). Not kill grade: no window forces
the deep-parse claim false — Route A remains a live compatible
alternative pending 58's classification.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `routeA-609-58verb` (P3) — test 58 as the finite verb at @610
   specifically ("qui [02-S] [58-V] ce[=cela]"): the @1202 block
   ('ce [58-verb] ce', ant-58-ending) does not apply to the
   post-nominal-verb order here. Coordinate with `58-noun-adjudicate`
   and the 24-conflict adjudication (`24-en-verb-conflict`, queued).
   Bar: promote the Route-A parse iff 58-verb is forced at @610 with
   02 nominal; else fence Route A at kill grade.
2. `val-39-class-census` (P3) — name 39's class from its 13 windows; a
   forced verb-39 re-opens Route E at @609 (first relative closed by
   "qui [39-V]", changing the second qui's attachment). Bar: promote
   verb-39 iff ≥2 independent verb-frame legs; else fence.
3. `a400-phase-rival-609` (P4) — re-test the @609 window under rival a4_00
   row-phases once any rival offset is validated; a rival phase that
   dissolves the "qui [02]" contact drops the leg. Gated on validated
   rival offsets; fence as phase-solid until then.
