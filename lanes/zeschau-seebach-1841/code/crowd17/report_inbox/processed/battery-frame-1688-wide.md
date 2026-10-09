# Battery report: frame-1688-wide

- Target id: `frame-1688-wide`
- Claim: full parse of "62 94 79 14 60 27 46 24 85" (@1687-1695); the "ne ... que" bracket empty verb slot is the window other residual
- Date: 2026-10-09
- Worker: battery worker (subagent bcef6aeb-8572-4a24-b48b-a4f804739d75)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session).
  `canonical.py` never used. R5005, sealed gate instances, red-team
  adjudication queue untouched.

Terms (ASD-STE100): "bracket" = the span between "ne" and "que" that must hold
the clause's finite verb. "New assumption" = a value or role that no standing
battery or red-team verdict licenses. "Fence" = a residual that no battery
route can close with standing values. "Hapax" = a group that occurs exactly
once in the stream.

## Index note (byte-exact)

The window's actual stream position is **@1686-1694**, not @1687-1695 as the
queue entry states. The queue claim's group sequence is exact; only its
start/end offsets are off by one. This report uses the stream's real offsets.
@-offsets are 0-based pair indices of the **window's first group** (frame
convention: the window starts at its 62).

## Bar (verbatim, pre-registered before testing)

"resolve iff one grammatical parse covers the full 9-group window with <=1 new
assumption; else fence as genuine residual"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (resolve arm):** one grammatical parse covers all 9 groups
   (@1686-1694) with at most 1 new assumption.
2. **C2 (fence arm):** else, fence the window as genuine residual with stated
   cause.

Adverses: none listed. No adverse answers required.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/frame-1688-wide.lock` on start (agent id +
   2026-10-09T11:16:14Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session; located the window.
3. Tested full-window parses against standing values only; counted the new
   assumptions the best parse needs.

## Window census (byte-exact)

`62 94 79 14 60 27 46 24 85` occurs exactly **1x stream-wide**: @1686-1694,
rows a8_05 (ends @1692) + a8_06 (starts @1693). Gloss (ii) holds: 46="que" at
@1692 is the last pair of row a8_05.

- @1686: 62, @1687: 94, @1688: 79, @1689: 14, @1690: 60, @1691: 27,
  @1692: 46, @1693: 24, @1694: 85.
- n(27) = 1: the lone @1691. 27 is a stream hapax; every bigram touching it
  is a hapax.
- n(62) = 35, n(60) = 18.

## Standing record adopted (not re-litigated)

- **62 = "il"** (subject pronoun) — battery PROMOTE (battery-il-62,
  2026-10-08). Adopted as the window's subject. §7 not contradicted.
- **94 = "ne"** — battery-promoted, pending red-team ratification. Adopted.
- **79 = "tout"** — granted (A5). Adopted.
- **14 = "en"** — battery PROMOTE, pending red-team ratification
  (battery-en14-value-tighten, 2026-10-09). Adopted.
- **46 = "que"** — pencil ground truth. Adopted.
- **60 — value open.** bare-60 verb vs ent-60 verb split (class, no value);
  gerund route open but unlicensed (gerund-60-1688 already QUEUED).
- **27 — class open, hapax.** No licensed role (class-27-independent already
  QUEUED).
- **24 — contested.** ne-24-profile promoted 24 = finite modal verb;
  en85-gerund-reaudit promoted 24 = 'en'; the conflict was NULL'd to the red
  team (24-en-verb-conflict, 2026-10-09; 24-redteam-adjudication already
  QUEUED). Not used as either value in this report.
- **85 — verb-stem granted (A3), value open.**
- 67 sole polyvalence (§7) untouched; no polyvalence invoked.

## Parse test

Best full-window reading under standing values:

> il(62) ne(94) tout(79) en(14) [60] [27] que(46) [24] [85]
> = "il ne tout en [60] [27] que [24] [85]"

"ne ... que" = "only". The restrictive bracket needs a finite verb inside the
ne-que span (@1687-1692). Its occupants: tout (quantifier), en (preposition),
60 (no value; gerund-slot of "tout en"), 27 (hapax, open class). None holds a
licensed finite-verb value:

- 60 as finite verb: unlicensed. 60 sits in the "tout en [60]" gerund slot; the
  bare-60 verb arm names no value and the @1690 window did not cohere in
  battery-verb-60. Making 60 both the gerund of "tout en" and the bracket's
  finite verb needs two contradictory roles.
- 27 as verb: zero licensed role (hapax, class open).
- tout or en as verb: unlicensed.

So the "ne ... que" bracket has an **empty verb slot** — the claim's window
other residual, confirmed at the window's own level.

## New-assumption count (best parse)

- A1: 60's form (gerund vs finite). Unlicensed either way; one role
  contradicts the other.
- A2: 27's dependent role in "en [60] [27]". No standing value supplies a
  licensed slot.
- A3: the bracket's finite verb. Nothing in the ne-que span can fill it; a
  fill would need A1 or A2 to succeed first.

That is **3 new assumptions** on the best parse — above the bar's ceiling of 1.
Even if the tail "que [24] [85]" were fully licensed (queued
neque-tail-24-85-clause tests that half), the main clause's verb slot stays
empty. Granting 62="il" does not close the gap: a subject without a verb is
still no parse.

Kill check: the window does not force the claim false at kill grade. Nothing
in the window rules out a future assembly (named 60 value + gerund license +
27 class could still fill the slot). No cleaner rival value is demonstrated
on these frames. Not a kill.

## Per-clause pass/fail

1. **C1: FAIL** — no grammatical parse covers all 9 groups with <=1 new
   assumption. The best parse needs 3 (60's form, 27's role, the empty verb
   slot).
2. **C2: FIRES (executed)** — the window is fenced as genuine residual. Stated
   cause: the ne...que bracket's verb slot is empty at the window level; 60
   cannot be both gerund and finite verb; 27's hapax status gives it no
   licensed dependent slot; 24's value is red-team-contested and 85's value
   is open. No standing/red-team verdict contradicted or downgraded; §7
   intact. Canonical-stream caveat stands (row a8_05/a8_06 offsets
   unvalidated).

## Verdict: NULL (fence executed)

The bar's else-arm fired as designed: the empty verb slot is the finding, not
a lack of effort. The residual re-opens when any of these land: a 60 gerund
license (queued: gerund-60-1688), 27's class (queued: class-27-independent),
or the 24 conflict's red-team ruling (queued: 24-redteam-adjudication).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `verb-slot-62-1686-neque` (P3) — with 62="il" adopted, census "62 94 ...
   46" windows stream-wide: is any finite verb licensed in the ne-que span
   anywhere, or is the empty verb slot geometry-wide? Discriminates
   window-local residual vs geometry-wide block.
2. `que46-1692-relative-role` (P4) — test pencil 46="que" at @1692 as relative
   pronoun ("that") introducing "[24] [85]". Complements queued
   neque-tail-24-85-clause; licenses the tail so the main-clause verb gap is
   isolated.
3. `dep27-1691-role-narrow` (P4) — test 27 at @1691 in an adjunct/adverbial
   role under neighbors only ("tout en [60] [27]"): does any standing-value
   parse give 27 a licensed dependent slot at this exact window? Narrower
   than queued class-27-independent; directly unblocks the complement route's
   27 fence.

Related already-queued work (not re-proposed): gerund-60-1688,
class-27-independent, neque-tail-24-85-clause, frame-62-94-79-reparse,
val-27-1691-np, 24-redteam-adjudication.

## Bookkeeping

- Report: this file.
- Queue: `frame-1688-wide` queued -> `verdict`/`null`, 2026-10-09 (pre-write
  assert passed — was queued/verdictless; temp-file + rename; JSON
  re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
