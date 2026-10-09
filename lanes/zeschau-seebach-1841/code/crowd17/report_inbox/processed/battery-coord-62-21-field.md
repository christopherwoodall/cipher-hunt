# Battery verdict: coord-62-21-field

**Verdict: NULL** — the claim's precondition is not met. `val-62-ne-noun`
returned NULL on 2026-10-09: domaine is dead at C1 but "règne" vs "trône"
is a genuine tie, so 62's value did NOT land. Under the surviving tied set
{règne, trône}, the "[21] et le [62]" frame at @505–508 cannot discriminate
at battery grade: French "et" coordination imposes no gender or
semantic-field agreement, both survivors are masculine nouns sitting after
provisional "le", and 21's own value is still open, so no incompatible pair
can be constructed. The claim's "may select" clause is answered in the
negative at battery grade.

## Bar (verbatim, pre-registered)

> Do not duplicate val-62-ne-noun's own bars.

Restated as numbered clauses (before testing):

- **C1**: This report's tests do not duplicate val-62-ne-noun's bars: the
  62-06 parse test ("règnent"/"trônent" vs *"domaient") and the six 62-48
  windows. This battery uses only the @505–508 coordination frame, the
  "21 67" follower census, and the "77 62" census. No 62-06 or 62-48 window
  is touched.

Claim (from queue): Once val-62-ne-noun lands 62's value, test
"[21] et le [62]" semantic-field compatibility at @505 — the coordination
becomes a discriminator for 21's value (and a falsifier for incompatible
pairs).

Adverses (from queue): 62's value open (val-62-ne-noun queued at
registration time; now returned NULL — value still open); the claim's "may
select" clause is answered in the negative at battery grade.

## Method

Read BATTERY-PROTOCOL.md first. Created
`code/crowd17/next-token/locks/coord-62-21-field.lock` on start (agent id +
UTC timestamp). No stale lock was present. Re-derived the repaired stream
in-session from `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt` (parsed per `repair_parse.py`): 1,847 pairs /
96 types verified. `canonical.py` never touched. R5005, sealed gates, and
the red-team adjudication queue untouched.

All @-offsets below are 0-based pair indices (queue convention).

Standing values used as premises (never re-litigated): 64=qui (banked);
67="et" via the sole-true-polyvalence positional rule (67="veut" iff
follower infinitive-shaped; 67="et" otherwise); 77="le" (provisional,
masculine singular); 94="ne" letter-tier (R17-003); syll-94-508-verify
PROMOTE (conditional): at @508, "62 94" composes leftward as "[62]ne",
word-final "ne" syllable — conditional on provisional 77="le".

62's prior state adopted without re-litigation: 62="il" kill-grade dead
globally; sel-62-48-94 KILL; val-62-ne-noun NULL (domaine eliminated at C1,
surviving set {règne, trône}). 21's prior state: suite killed
(suite-21-qui-que KILL, val-21-reopen KILL); de-frame-21-class PROMOTE named
only the class; 21's value is open.

Offset note: the ten-pair window '56 39 68 21 67 77 62 94 64 98' (row
a3_00) begins at @502 in the repaired parse, not @505. The "[21] et le
[62]" sub-frame is @505–508 exactly as stated: 21@505, 67@506, 77@507,
62@508, 94@509, 64@510.

## Window-level evidence

**E1 — the @505–508 frame (row a3_00):**

    @502 '56'  @503 '39'  @504 '68'  [ @505 '21'  @506 '67'  @507 '77'
      @508 '62' ]  @509 '94'  @510 '64'  @511 '98'  @512 '65'

  Under standing values: "[39] [68] [21-noun] et(67) le(77) [62]ne(62+94)
  qui(64) [98]...". Follower of 67 is 77, not infinitive-shaped, so 67="et"
  by the positional rule. The frame parses cleanly.

**E2 — "77 62" census, stream-wide:** exactly 1 occurrence, at @507. The
only "le [62]" window in the stream.

**E3 — "21 67" census, stream-wide:** exactly 8 windows, followers in
window order: @109→93 (a1_03), @115→14 (a1_03), @505→77 (a3_00),
@850→91 (a5_07), @1162→78 (a6_09), @1422→33 (a7_08), @1456→86 (a7_09),
@1841→78 (a8_11). "21 67 77" occurs once (@505).

**E4 — compatibility under the tied set:** 62's live values are {règne,
trône}, both masculine nouns. Both sit grammatically after masculine "le"
(E2's unique window) and both coordinate via "et" with any noun in the
@505 slot regardless of that noun's gender or field: French coordination
imposes no gender/field agreement. Domaine is already dead at C1, so it
does not enter this test. Result: no battery-grade discrimination between
the two survivors.

**E5 — 21's value is open:** with no named 21 value, no incompatible
(21, 62) pair can be constructed, so the falsifier arm of the claim has
nothing to act on.

**E6 — standing fence (not a discrimination):** 77="le" is masculine
(provisional), and @507 is the stream's only "77 62" window. This fences
out any future feminine candidate for 62 at battery grade — the frame is a
guard, not a selector.

## Per-clause pass/fail

- **C1 (do not duplicate val-62-ne-noun's bars): PASS.** No 62-06 window
  and no 62-48 window was tested. All evidence is from the @505–508
  coordination frame and the "21 67"/"77 62" censuses, which are disjoint
  from val-62-ne-noun's bars.

Claim-level assessment:

- **Precondition check: FAIL — claim not testable as designed.**
  val-62-ne-noun returned NULL (2026-10-09); 62's value did not land.
  Per §2, this is recorded as a finding and counts as a null.
- **"may select" clause: answered in the negative at battery grade.**
  Under {règne, trône}, E4 shows the coordination is field-free and both
  survivors behave identically; E5 shows 21's open value leaves no pair to
  falsify.

No contradiction with any standing red-team verdict: this null agrees with
the queue's registered adverse.

## Verdict: NULL

The coordination frame works as a grammatical parse but cannot do the
discriminating work the claim asks of it until both values are landed.

## Follow-up targets (null regeneration)

1. **coord-62-21-field-retest** (priority 3): re-run this target once 62's
   value is actually landed (the règne/trône tie broken) AND 21's value is
   ratified. Bar: "Pre-register the landed values; test '[21] et le [62]'
   at @505–508; every incompatibility must force a parse contradiction,
   not a stylistic judgment."
2. **62-regne-trone-final** (priority 2): break the règne/trône tie with a
   narrower bar outside the consumed 62-06/62-48 sets (candidate: semantic
   fit at the @508 head under "et le [62]ne qui [98]..." with 94="ne"
   letter-tier, or fresh frames from the 35-window census).
3. **21-67-follower-compat** (priority 3): once 21's value is named,
   battery-test "[21] et <follower>" compatibility across the eight
   "21 67" windows (followers 93/14/77/91/78/33/86/78) as a value-level
   falsifier for 21.

---
Date: 2026-10-09. Agent: b851c736. Lock: fresh, deleted on completion.
Pre-registration: bar copied verbatim and restated as C1 before any
stream read. Stream: 1,847 repaired pairs; every number above traces to it.
