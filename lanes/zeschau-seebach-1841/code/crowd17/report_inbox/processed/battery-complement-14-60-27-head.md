# Battery report: complement-14-60-27-head

- Target id: `complement-14-60-27-head`
- Claim: "license a head for the complement 'tout [14] [60] [27]' under standing values"
- Date: 2026-10-09
- Worker: battery worker (subagent a5b513d1-c671-4270-947a-5768bf969475)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "head" = the group whose licensed value makes the complement
a grammatical phrase. "Dependent" = a group that the head licenses in a stated
role. "Fence" = a residual that no battery route can close with standing values.

## Bar (verbatim, pre-registered before testing)

"resolve iff a single licensed head value parses for [14], [60], or [27] with
the other two parsing as its dependents; fence as residual if 27's hapax status
blocks every frame"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (resolve arm):** some licensed head value among {14, 60, 27} parses the
   complement with the other two as its stated dependents under standing values.
2. **C2 (fence arm):** else, fence the complement as residual with stated cause —
   specifically whether 27's hapax status blocks every frame.

Adverses: §7 intact; no standing verdict touched; 79='tout' granted and
94='ne' battery-promoted pending ratification — both used as given.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/complement-14-60-27-head.lock` on start
   (agent id + 2026-10-09T10:38:00Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session; located the complement.
3. Tested three head routes (H-14, H-60, H-27) against standing values only.

## Locus census (byte-exact)

`79 14 60 27` occurs exactly **1x stream-wide**: @1688–1691, row a8_05.
Full window: `62 94 79 14 60 27 46 24 85 58 15 23`
= "…[62] ne(94) tout(79) [14] [60] [27] que(46) [24] [85]…"

- `79 14 60` occurs 2x (@1364, @1688) — only @1688 carries the [27] tail.
- n(27) = 1: the lone @1691. 27 is a stream hapax; every bigram/trigram
  touching it is a hapax.
- Left frame is the frozen "62 94 79" unit (frame-76-94-trigram NULL/fenced:
  frozen formula, not a demonstrable frame); right frame is "…que [24] [85]".

## Standing record adopted (not re-litigated)

- **14="en" — battery PROMOTE** (battery-en14-value-tighten, 2026-10-09:
  "PROMOTE (battery grade; red-team ratification of 14=`en` still pending)").
  The only licensed head value among the three.
- **60 — value open.** battery-verb-60 (NULL: the six windows do not cohere
  under one nameable verbal value); split-60-verbs promotes bare-60 verb
  (V1–V4, -dre family) vs ent-60 verb (V5–V6) as two items sharing syllable 60 —
  no value named either side. Past-participle avenue fully closed
  (participle-60-newvalue KILL, 2026-10-09; "dit" kill-grade dead).
- **27 — class open, hapax.** battery-npframe-60-detleft-closeout (2026-10-09,
  NULL): "27's class is open … 27's class (any future named 60 value re-tests
  the '14 60 27' geometry)".
- 79="tout" granted (A5); 94="ne" battery-promoted pending ratification.

## Head-route tests

### H-14 — head = 14="en" (the licensed value)

Shape: "tout en [60] [27]" — 14 parses as head; 60 and 27 must parse as
dependents.

- "tout en [60]": licensed shape per the en14 census ("tout en [60]" frames
  are positive legs). But "en [60]" as a dependent needs 60 in a
  gérondif/infinitive-compatible form: 60's verbal arm has no gérondif license
  (participle dead; -dre family is finite/verb-stem; ent-60 is verb).
  → 60's dependent role needs ≥1 unstated assumption (form).
- 27 as dependent of the construction: **zero licensed role.** 27 is a hapax
  with an open class; "en [60] [27]" has no licensed dependent slot for a
  classless group under standing values. → second unstated assumption.

**H-14 FAILS:** two unlicensed assumptions; the bar demands the other two
parse as dependents under standing values.

### H-60 — head = 60

60 has **no named value** at battery grade (split-60-verbs: class, no value;
participle dead; no named verb). There is no "licensed head value" to test.
**H-60 FAILS** on the bar's first condition.

### H-27 — head = 27

27 is a hapax with an open class. No licensed value exists; no head test
possible. **H-27 FAILS** on the bar's first condition.

## Per-clause pass/fail

1. **C1: FAIL** — no licensed head value among {14, 60, 27} parses the
   complement with the other two as stated dependents. The sole licensed value
   (14="en") would need 60's form AND 27's role, both unlicensed.
2. **C2: FIRES (executed)** — the complement is fenced as residual. Stated
   cause: 27's hapax status blocks every frame. Every head route terminates at
   27: H-14 needs 27 in a licensed dependent slot that no standing value
   supplies; H-60 and H-27 cannot even start because no licensed head value
   exists. No standing/red-team verdict contradicted or downgraded; §7 intact;
   the en14 promote, the 60 split, and 27's open class are all adopted
   untouched. Canonical-stream caveat stands (row a8_05 offset unvalidated).

## Verdict: NULL (fence executed)

The bar's else-arm fired exactly as designed: the hapax fence is the finding,
not the absence of effort. The residual's next life begins only when one of
the three opens: 27's class, 60's value, or a 60 gérondif license.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `gerund-60-1688` (P3) — test 60 as gérondif at @1689 ("tout en [60]").
   A licensed gérondif-60 re-opens the H-14 route with 27 as sole open.
2. `frame-1688-wide` (P3) — full parse of "62 94 79 14 60 27 46 24 85";
   the "ne … que" bracket's empty verb slot is the window's other residual.
3. `class-27-independent` (P4) — class 27 from its single window's grammar
   alone (nominal / adverbial / adjunct arms armed by neighbors only); the
   only battery-grade way to unblock the hapax fence.

Note: `val-27-1691-np` (P4) is already queued — not re-proposed here.

## Bookkeeping

- Report: this file.
- Queue: `complement-14-60-27-head` queued → `verdict`/`null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
