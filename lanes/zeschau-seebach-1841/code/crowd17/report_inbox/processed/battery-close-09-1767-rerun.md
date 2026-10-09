# Battery report: close-09-1767-rerun

**Target:** `close-09-1767-rerun` (priority 3)
**Verdict:** NULL (bar untestable as written — claim precondition unmet)
**Date:** 2026-10-09
**Parent:** `battery-ce-qui-left-closure.md` (null, 2026-10-09) — follow-up from the W3 fence; queued by next-token-supervisor follow-up audit at 2026-10-09T12:15Z

## Bar (verbatim, pre-registered)

> 'on [09] [24]' closes with zero new assumptions iff 09's granted role composes (adverb / object pronoun); else fence W3 permanently.

Restated as numbered clauses before testing:

- **C1:** 09's class is granted (the claim's own precondition: "Re-test ... once 09's class is granted").
- **C2:** The granted role composes in the "on [09] [24]" window (@1765-1767 1-based, row a8_08) as adverb or object pronoun with zero new assumptions → W3 closes.
- **C3:** If a granted role exists and does not compose, fence W3 permanently (the bar's else-arm).

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed exactly like `code/side-keyhunt/repair_parse.py`
(asserts held: 1,847 pairs, 96 types). `canonical.py` never used.
R5005 never touched.

No fresh lock existed (verified before creation). Lockfile
`locks/close-09-1767-rerun.lock` created 2026-10-09T20:23Z with worker agent
id `9942d7bb-16dc-4c92-a222-d004565d6a2d`, deleted on completion.

Adopted premises (standing only): banked GT (11=la, 70=pre, 82=m, 34=i,
29=er, 40=e, 46=que); granted 84=on (A15), 64=qui, 87=ce, 96=par, 79=tout
(A5), 00=pour (A9), 47=ce (A4); kills hold on 09/92 "-ère" value; 09~92 split
holds (A6). 09 has no standing value or class.

## Window-level evidence

**The @1765-1767 window (a8_08), byte-exact from the repaired stream:**
1b@1765 = 84, 1b@1766 = 09, 1b@1767 = 24, 1b@1768 = 87 —
the parent report's W3 triple ("84 09 24", left of "87 64" at @1768),
row a8_08, unchanged from the fence.

**"84 on" windows in the whole stream (84 immediately before 09):**
@1060 and @1766 — the known 'l'on __ V' doublet (matches lon-09-verb's
claim territory, ~2-offset convention difference). All 12 09 windows:
[1, 174, 290, 519, 592, 681, 916, 1060, 1224, 1263, 1766, 1821] (1-based).

**09's class status (queue audit, 2026-10-09T20:23Z):**
Every 09-class target has verdict `null` — hold-09-92, lon-09-verb,
noun-09-916, rel-09-290, lon-09-reseg, doublet-589-09-role
("pin 09's class from its 12 windows"), noun-09-915-value. The only
09-related `promote` is split-09-redteam-input, which packages split
evidence (confirms 09~92, grants no class). Two 09-class landings remain
`queued`: adv-09-1059-1766-value and nom09-open-windows. No red-team
ratification grants 09 any class.

## Per-clause result

- **C1 FAIL (precondition):** 09's class is NOT granted. The claim's own
  trigger — "once 09's class is granted" — has not fired.
- **C2 UNTESTABLE:** "09's granted role composes" cannot be evaluated when
  no granted role exists. Per §2 of the protocol, a bar that is genuinely
  untestable as written is recorded as a finding (counts as null) — the bar
  is not silently rewritten.
- **C3 does NOT fire:** the else-arm ("else fence W3 permanently")
  presupposes a granted role that fails to compose. Absence of a grant is
  not failure-to-compose. Fencing W3 "permanently" now would foreclose the
  two queued 09-class landings (adv-09-1059-1766-value, nom09-open-windows)
  that exist precisely to unblock this re-test — the pipeline's own
  structure contradicts a permanent fence at this point.

**Verdict: NULL.** The W3 fence from battery-ce-qui-left-closure stands;
this rerun is premature, not resolved. W3 remains fenced-with-cause
(09's role open), re-open gated on 09's class.

## Follow-ups proposed (1–3, per §4; all verified absent from the queue)

1. **gate-09-class-w3-rerun** (priority 3): re-dispatch this exact rerun
   once a 09-class verdict lands from adv-09-1059-1766-value or
   nom09-open-windows (priority 2 if one of them promotes, priority 4 if
   they exhaust with null). Claim: "Re-arm close-09-1767-rerun: 09's class
   has now been granted; run the composition test on '84 09 24' @1765-1767."
2. **val-09-w3-compose** (priority 3): conditional composition battery —
   if 09's granted class is adverbial or object-pronominal, test that
   "'on [09] [24-fin]' closes with zero new assumptions" holds at BOTH
   @1766 and @1060 (the 'l'on __ V' doublet, discriminator against the
   lon-09-verb windows); if the granted class is nominal, kill W3's left
   outright (a noun cannot slot between subject "on" and a finite 24).
3. **fence-w3-terminal** (priority 4): fence W3 permanently ONLY if all
   09-class targets (adv-09-1059-1766-value, nom09-open-windows, plus any
   follow-ups they spawn) return null with no class grant — this is the
   bar's else-arm executed in the correct order, after the grant question
   is exhausted rather than before it is asked.

## Notes / anomalies

- The claim's @1764-1766 vs this report's @1765-1767: convention difference
  only (the parent counted the 0-based adjacency "87 64" @1767; the
  repaired stream's 1-based triple is @1765-1767, row a8_08). Same window.
- Lock lifecycle clean: no stale lock, created at start, deleted at end.
  Queue entry touched only for this target, via the target-id-unique tmp
  name per protocol §5.
