# Battery `neque-tail-24-85-clause` — report

**Verdict: PROMOTE**

## Bar (verbatim, pre-registered from battery-queue.json)

> "promote iff 85 licenses a verb-stem parse with [24] as a licensed dependent under A3 conditions; kill iff the tail forces 85 into a non-verb reading; null iff A3's conditions are untestable on this frame"

Restated as numbered clauses (before testing):
- **C1** — 85 licenses a verb-stem parse with [24] as a licensed dependent under A3 conditions → promote.
- **C2** — the tail forces 85 into a non-verb reading → kill.
- **C3** — A3's conditions are untestable on this frame → null.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(asserts held: 1,847 pairs, 96 types). `canonical.py` never used.
Adopted standing premises: A3 (crowd15 red-team: "85 = verb-stem candidate",
value open); R24 (R19-191: 24='en' iff follower=85, declared on kill-grade
byte evidence); registry cells 46=["que","gt"], 58=["nominal","cls"],
24=["verb","cls"] (R24 recorded in _meta/protocol, cell unchanged).

## Window-level evidence

Locus byte-confirmed (0-based, row-validated):
- @1691=27, @1692=46, @1693=24, @1694=85, @1695=58 — rows a8_05/a8_06.
- Tail shape: "[27] que(46) [24] [85]".
- "24 85" bigram is exactly 5× stream-wide: @732/@955/@1438/@1693/@1754 —
  all five are R24-declared 'en' windows.

Per-clause findings:

**C1 — PASS.** All four elements hold on standing premises:
1. 85 is an A3 verb-stem candidate (standing grant; value open). The A3
   grant's own leg list explicitly names this window: "second 'que en 85'
   @1692 (85@1694)". The tail matches the "en [85]" leg shape exactly.
2. 24 at @1693 is 'en' (pronominal clitic) by red-team law R24 (follower=85;
   @1693 is one of the four verb-kill windows named in R19-191; R19-185's
   24-conditionality is discharged "@1693 → 'en' licensed").
3. Clitic 'en' is a licensed dependent of a verb-stem: "en [verb]" is
   grammatical 1841 French (partitive/ablative clitic + verb).
4. The wider tail continues "@1695=58" (nominal class), giving
   "que en [85-verb] [58-noun]" — verb + nominal object, a licensed verb
   clause shape. 27 (unvalued) needs no value for the bar's parse test.

**C2 — FAIL (does not fire).** Nothing in the tail forces 85 into a
non-verb reading. The "que en [85]" shape is the A3-licensed shape itself;
no rival non-verb reading of 85 is forced at this window.

**C3 — FAIL (does not fire).** A3's conditions are testable here — this
window is one of A3's own named legs. No untestability.

## Adverses answered

- "A3 conditions must be tested, not assumed": tested. The window is an A3
  leg by the grant's own leg list, and the "en [85]" dependent shape matches
  the grant's leg shape byte-exactly.
- "24's class unresolved (24-redteam-adjudication venue...)": superseded by
  R24 (R19-191), a standing red-team declaration. I do not adjudicate 24's
  class; I adopt R24 as a premise. The adverse's premise (unresolved class)
  no longer obtains at this window.

## Verdict rationale

C1 passes on standing premises with zero new assumptions; C2 and C3 do not
fire. The bar's promote condition is met: 85 licenses a verb-stem parse with
[24] as a licensed dependent ('en' clitic) under A3 conditions, and the tail
opens the licensed clause "que en [85] [58]".

No standing/red-team verdict contradicted or downgraded (A3, R24, R19-185,
46="que", 58 nominal class all adopted as premises); §7 intact (no
polyvalence declared — R24's §7 exception is the red team's, adopted, not
re-litigated); no value named for 85 or 27. Canonical-stream caveat stands
(rows a8_05/a8_06 offsets unvalidated). No follow-ups required per §4
(promote).

## Bookkeeping

- Queue: `neque-tail-24-85-clause` → `status: verdict`, `result: promote`,
  2026-10-09 (pre-write assert: was queued/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade).
- Lock `neque-tail-24-85-clause.lock` created on start, deleted on
  completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
