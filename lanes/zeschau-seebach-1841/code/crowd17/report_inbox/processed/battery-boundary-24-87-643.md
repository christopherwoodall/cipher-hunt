# Battery report: boundary-24-87-643

- Target id: `boundary-24-87-643`
- Claim: test for a licensed clause boundary between 24@643 and 87@644
  (subject-position evidence, pause-mark precedent in the lane corpus); a
  licensed boundary dissolves the 24/88 collision at battery grade,
  removing ungranted assumption (2).
- Date: 2026-10-09
- Worker: battery worker (subagent a24512e6-4c28-4bdd-aff2-cb77705b6906)
- Stream: repaired 1,847-pair parse re-derived in-session from
  `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
  (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005,
  sealed gate instances, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/boundary-24-87-643.lock` (created at
  start, no fresh lock existed; deleted on completion).

## Bar (verbatim, from battery-queue.json)

"Bar: test for a licensed clause boundary between 24@643 and 87@644
(subject-position evidence, pause-mark precedent in the lane corpus); a
licensed boundary dissolves the 24/88 collision at battery grade,
removing ungranted assumption (2)."

Numbered pass/fail clauses (pre-registered before testing, not modified
after):

1. **C1 (subject-position evidence):** an 87-initial NP ("ce [61]") has
   standing support as a clause subject — i.e. a licensed reading in
   which @644 opens a new clause with "ce [61]" as subject of finite-88.
2. **C2 (pause-mark precedent):** the lane corpus licenses a zero-marked
   clause boundary at @643|@644 (boundary precedent, not raw French
   grammaticality alone).
3. **Verdict rule:** promote iff C1 and C2 both pass at battery grade;
   kill iff a window forces the claim false; else NULL. Per §5, a
   contradiction with a standing verdict is recorded as NULL with the
   contradiction as headline, escalated to the red team — never
   downgraded at battery level.

Terms (ASD-STE100): "licensed" = allowed by granted values and lane
precedent. "Ungranted assumption (2)" = the clause-boundary resolution of
the 24/88 collision named in the parent null (fin88-646-rerun).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock on start
   (2026-10-09T11:46:55Z); no fresh lock existed (the topup hook had not
   taken it). Deleted on completion.
2. Re-derived the repaired stream byte-exact per
   `code/side-keyhunt/repair_parse.py`. All @-offsets are 0-based pair
   indices.
3. Adopted, never re-litigated: det-87-644-function PROMOTE (87 =
   determiner at @644, window-level, 2026-10-09); seg-ceci-87-61 PROMOTE
   (87+61 = "ceci" at @644, locus-level, 2026-10-09); fin88-646-rerun NULL;
   val-61-646-locus NULL; form-24-643 NULL; clause-boundary-precedent KILL;
   24 = finite/modal-shaped verb class (R17-009, standing); 88 = verb
   class (battery PROMOTE, finiteness open).

## Window-level evidence

### The locus — byte-confirmed

`[641]48 [642]20 [643]24 | [644]87 [645]61 [646]88 [647]77 [648]78`
(row a4_02; @643 is row-initial, the row spans @643–@667).

### HEADLINE: two same-day battery PROMOTEs contradict on @644–645

- **det-87-644-function PROMOTE (2026-10-09):** 87 is a determiner at
  @644; "ce [61]" is an NP; the pronominal-87 route is closed at this
  window. It licenses the 61 adjectival/nominal arm ("ce premier" as
  possible subject of finite-88). The one-word "87 61" rival was fenced
  as an "untestable sub-route, not a function rival".
- **seg-ceci-87-61 PROMOTE (2026-10-09):** 87+61 fuses to one word
  "ceci" (87="ce" + 61="ci"); "ceci" is the direct object of modal-24
  ("faire ceci"), byte-parallel to granted "faire cela" @829-830
  ("...01 24 87 11 77..."). Under this reading there is NO clause
  boundary between 24@643 and 87@644 — "ceci" belongs to clause A.

These are mutually exclusive tokenizations of the same two pairs.
The bar's premise (87@644 as determiner opening a subject NP) is
contradicted at battery grade by the standing ceci PROMOTE.

### C1 test — subject-position evidence

Under the det reading, the subject arm is "ce [61]" = "ce premier" as
subject of finite-88. It needs two unstated premises:

1. 61 = "premier" at @645 — unstated (val-61-646-locus NULL).
2. An 87-initial NP in subject position is precedented — absent.
   Census (this battery): 87 occurs 32x stream-wide; "87 61" is a
   singleton (@644 only). 87's followers: 11 x7 (cela compounds), 64 x5,
   46 x3, 01/77/78/83 x2, 14/86/98/59 x1. No other 87-initial NP stands
   in subject position anywhere in the stream.

And the ceci PROMOTE actively contradicts the arm: "ceci" is an OBJECT
of 24, not a subject. **C1: FAIL/BLOCKED.**

### C2 test — pause-mark precedent

- **clause-boundary-precedent KILL (2026-10-09):** the lane's own
  "clause boundary after an article" mechanism is dead at battery grade
  (exhaustive census, 0/31 demonstrable legs). That kill is a different
  mechanism (after an article, not after a finite verb), so it does not
  touch this bar — but it set the lane's rule: future boundary rescues
  "must bring their own byte evidence." This battery finds none.
- **Row-head enrichment licenses the wrong position.** Row-initial slots
  are mildly enriched for clause-initial groups (46=que, 00=pour per
  edge-1024-clause-boundary). @643 IS row-initial — but that licenses a
  boundary at @642|@643 (row head), not at @643|@644 (the bar's
  position).
- **No pause-mark precedent.** The cipher stream carries no pause-mark
  tokens (every boundary is zero-marked in the token stream). The lane's
  register pause-mark work (disloc pausemark censuses) covers dislocated
  demonstratives in French prose — out of frame for a
  modal+demonstrative-subject join. No zero-pause-juxtaposition
  precedent exists for this shape.
- Under the ceci reading, no boundary is needed or licensed between
  643 and 644 at all ("…[24-modal] ceci [88]…").

**C2: FAIL.**

### Kill check

Does any window force the claim false at battery grade? No. The det-87-644
PROMOTE stands (battery-grade, never downgraded here), and under it a
boundary remains grammatically statable. The ceci PROMOTE contradicts the
boundary, but it is a battery verdict of equal rank — battery grade
cannot adjudicate between two standing PROMOTEs. Killing the claim would
downgrade det-87-644-function; forbidden by §5. **Not kill-grade.**

## Verdict: NULL (contradiction headline, escalate to red team)

Two same-day battery PROMOTEs make mutually exclusive claims about
@644–645: seg-ceci-87-61 ("ceci" = 87+61, object of modal-24, no boundary
between 643 and 644) vs det-87-644-function (87 = determiner, "ce [61]"
NP, subject arm open). The bar's subject-position arm is contradicted by
the ceci PROMOTE; the pause-mark arm has no lane precedent. Battery grade
cannot resolve the conflict. This NULL is recorded with the contradiction
as the headline; the adjudication belongs to the red team.

No standing or red-team verdict contradicted or downgraded. §7 intact.
Canonicality caveat stands (a4_02 row offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `ceci-det-644-adjudicate` (P1, red-team venue) — adjudicate the
   @644–645 contradiction: seg-ceci-87-61 PROMOTE (87+61="ceci",
   61="-ci", direct object of modal-24, no boundary between 643 and 644)
   vs det-87-644-function PROMOTE (87=determiner, 61
   nominal/adjectival, "ce [61]" NP). Battery cannot resolve; the loser
   must be downgraded by the red team. Evidence to weigh: ceci's
   "fois-ci" @926 parallel and "faire cela" @829-830 object-slot
   parallel, plus zero nominal legs in n(61)=18 (ceci E4a; confirmed by
   this battery's census: 18 windows, no determiner-headed nominal
   parallel for 61) vs det's zero-assumption grammatical elimination
   (bare-"ce" pronominal frames dead; 0 instances of finite-verb + bare
   "ce" + clause punctuation in 31.7M chars of 1841 French).
2. `boundary-24-87-643-rerun-gated` (P3, gated on the adjudication) —
   if the red team ratifies determiner-87 at @644 (ceci arm dead),
   re-test this bar with the ceci arm excluded: subject-position
   evidence for "ce [61]" as subject of finite-88 plus pause-mark
   precedent. If the red team ratifies ceci, this bar dies at kill
   grade (no boundary between 643 and 644 under "…[24-modal] ceci
   [88]…").
3. `nominal-61-645-legs` (P4) — census n(61)=18 for any
   nominal/adjectival leg licensing "ce [61]" as an NP head under the
   determiner reading; needed only if the red team ratifies
   determiner-87. Bar: one genuine nominal/adjectival 61 window revives
   the determiner arm; confirmed zero buries it independent of the
   adjudication.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-boundary-24-87-643.md`
  (this file).
- Queue: `boundary-24-87-643` queued → verdict/null, 2026-10-09
  (pre-write assert: was queued/verdictless; temp-file + rename; JSON
  re-validated; own entry only; no downgrade).
- Lock `locks/boundary-24-87-643.lock`: created on start, deleted on
  completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
