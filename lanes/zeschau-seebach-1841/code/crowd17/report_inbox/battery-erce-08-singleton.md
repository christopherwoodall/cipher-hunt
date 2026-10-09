# Battery verdict: erce-08-singleton

Target: `erce-08-singleton` (priority 3).
Date: 2026-10-09. Worker: 8191f31c-dfe4-42c5-a329-df9d1feea7a0.

## Bar (verbatim from battery-queue.json)

> test '29 47 08' @1591 once 08's value resolves

Numbered clauses (pre-registered before testing):
1. 08's value resolves at battery grade (precondition for the test).
2. Given a resolved 08, the '29 47 08' window at @1591 tests as word
   boundary versus word-internal under that value.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types
verified). `canonical.py` never touched. R5005, sealed gates, the
red-team adjudication queue untouched. Lockfile
`crowd17/next-token/locks/erce-08-singleton.lock` created with agent id +
UTC timestamp; no prior verdict or fresh lock existed.

Standing values used: 29='er' (pencil GT), 47='ce' (A4 allophone tier with
87), 81 = masculine abstract noun (noun-81 PROMOTE), 48 = 'e' letter tier
(R17-003), 08's value open.

## Window evidence (all byte-traced)

- The '29 47 08' trigram occurs exactly once stream-wide, at 0-based
  indices @1590-1592 (queue convention @1591 = the 47 anchor).
  Full @1586-1596 window, all mid-row a8_02:
  `70 64 65 48 | 29 47 08 | 81 03 29 80`
  (matches the target evidence verbatim: `36 70 64 65 48 | 29 47 08 |
  81 03 29 80`; 36 sits at @1585).
- 47's follower census (n=28): 78 x5, 46 x3, 11 x3, 33 x2, 03 x2, 98 x2,
  then 14 x1, 08 x1, 41/01/44/77/91/43/76/86/68 x1 each. The target
  evidence's cluster claim (33 x2, 14 x1, 08 x1) is confirmed as the
  low-count tail of this distribution.
- '29 47' bigram x4 (29-position, 0-based): @22, @422, @1230, @1590.
  The two 'erce'-shaped windows in the target evidence (@1231/@1591)
  are the 47 positions of @1230 and @1590; both are '48 29 47'.
- 08's contact census (n=18): predecessors 60/67/37/40 x2, 01/41/85/16/
  17/45/80/87/47/23 x1; followers 31 x3, 65 x2, 62 x2, 91/34/21/67/24/
  52/29/01/43/81/55 x1. Heterogeneous both sides; no class.

## Adverse audit

1. "08's value is open (untestable at battery grade)" — CONFIRMED by the
   queue itself: `stem-08` returned null ("08 disambiguation"), and
   `on-08-homophony` killed the only standing 08-value hypothesis
   (08='on'). No promote, kill, or provisional value names 08 anywhere
   in the 1,672-target queue. The adverse is therefore accurate, and it
   is exactly the bar's own precondition.
2. "The '[stem]erce' internal reading survives unrefuted at Frame A though
   no stem value is named at battery grade" — STANDS: `erce-1590` (promote)
   resolved '48 29 47' as a grammatical segmentation ("48-e | 29-er |
   47-ce"), and `erce-stem-fenceA` remains queued to kill or confirm the
   word-internal stem reading. Nothing in this battery contradicts it.

## Per-clause pass/fail

1. 08's value resolves at battery grade — FAIL (precondition unmet;
   08's value is open: stem-08 null, no standing value).
2. Boundary-vs-word-internal test under resolved 08 — UNTESTABLE
   (blocked on clause 1).

Per protocol §2, the bar is genuinely untestable as written and is not
rewritten. This is recorded as a null finding.

## Verdict

**null** — the bar's precondition ("once 08's value resolves") is not
met; 08's value is open at battery grade. Evidence at the window
(@1590-1592) is fully verified byte-trace; no clause could pass or fail.

## Follow-ups (null-regeneration; ids verified absent from battery-queue.json)

1. **`erce-08-rerun-gated`** — gated re-fire of this exact bar once 08's
   value is banked: re-test '29 47 08' @1591 as boundary versus
   word-internal under the landed 08 value. This is the bar's own
   deferred test; it stays live, not dead.
2. **`erce-08-81-adjacency`** — test the '47 08 81' contact at @1591-1593
   using values already standing: 47='ce' (A4), 81 = masculine abstract
   noun (noun-81 PROMOTE). Narrow bar: "produce one grammatical
   segmentation of @1589-1593 ('48 29 47 08 81') honoring the standing
   29/47/81 values; 08 passes as modifier iff the contact parses."
   Needs no 08 value, only a class-typed reading.
3. **`08-31-lettertier-boundarytie`** — 08's strongest successor is 31
   (x3: the only repeat follower). Test whether the 08 at @1591 and a
   second 'ce 08' contact (e.g. @976, target ci-976-08-gate's window)
   share a word-tier position via their successor classes. If the two
   08s show different successor classes, 08 is positional rather than
   value-carried, and the @1591 boundary question reframes.
