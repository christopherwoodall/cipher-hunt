# Battery report — orphan86-300 (@300's 86 does not resolve via 97's or 78's class)

Worker: ffaad827-25e1-4c4f-b83c-e48eb6949560. Date: 2026-10-08.
Lock: `code/crowd17/next-token/locks/orphan86-300.lock` created 2026-10-08T19:25:11Z (no lock present); deleted on completion.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`.
`canonical.py` not used. R5005 not touched. No invented numbers: every count
below was re-derived from the stream in this run.
Coordination: no overlap with erstem-33-id, fork-78-45-adjudication, or the
86 stem-side (stem-86) targets. The @296 re-parse is separately queued as
`ver78-296-97gate` (gated on frame-97-profile + stem-86 verdicts) — this
battery does not duplicate it.

## Bar (verbatim, from battery-queue.json)

"resolve iff a stated 97-class or 78-value makes '...e [97] [86] [91]...' parse
as whole with zero contradiction; else confirm orphan (test the letters-context
hypothesis: 86-as-letter against the promoted 12/34/40/48 set)"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. A stated 97-class exists and makes the @300 window
   (`78-40-97-86-91-18-89-88-02`, row a2_04) parse as whole with zero
   contradiction → claim resolves.
2. A stated 78-value makes the same window parse as whole with zero
   contradiction → claim resolves.
3. Otherwise: the letters-context hypothesis (86-as-letter) is tested against
   the promoted 12/34/40/48 letter set and rejected on stated distributional
   grounds → orphan confirmed.

## Method

Re-derived 97's and 86's censuses and neighbor distributions on the repaired
stream (asserted 1,847 pairs / 96 groups first). Attempted whole-window parses
under every stated class/value (§7 standing). Tested 86-as-letter by
letter-cell adjacency and by 86's stem behavior. Checked the queue for existing
97/78 targets to avoid duplication.

## Window-level evidence

Target window @300 (row a2_04), all pair indices on the repaired stream:

`@295:01 @296:11 @297:78 @298:40 @299:97 @300:86 @301:91 @302:18 @303:89 @304:88 @305:02`

= "…[01] la [78] e [97] [86] [91] [18] [89] [88] [02]…" (11="la", 40="e" banked).

86 census: n=32 on the repaired stream (offsets [175, 300, 431, 553, 557, 661,
671, 716, 728, 799, 867, 878, 889, 899, 948, 951, 962, 1002, 1099, 1128, 1131,
1134, 1147, 1335, 1345, 1375, 1391, 1458, 1506, 1739, 1792, 1825]); the
corrected census is used throughout, per the task brief.

97 census: n=10 (offsets [2, 94, 288, 299, 525, 566, 588, 751, 1412, 1823]).
pre = 00 x4, 81 x2, 40/80/02/16 x1. The four 00→97 windows on the repaired
stream: @2 `00-97-51` "pour [97] [51]"; @288 `00-97-09-64-29-40` "pour [97]
acquière"-shaped (fenced pour-adverse per crowd16 i-finder — old numbering
@291; @288 here); @588 `00-97-41-41-09-00`; @1823 `09-19-00-97-00-86-29-82`
"pour [97] pour [86]er me" (a stem window of 86, per stem-33-86).

### Clause 1: 97's class

There is NO stated 97-class in the lane. 97's class is the subject of the
still-queued target `frame-97-profile` ("97's class is named from its contact
profile"). The pre=00 x4 pattern SUGGESTS the INF class under A9's 00="pour"
leg-1 class-level grant, but a suggestion is not a stated class, and the
bar demands a stated class. Even as a hypothesis the INF reading fails the
whole-window test: "e [97-inf] [86] [91]" has no INF frame for two consecutive
infinitives (97→86), and 40="e" precedes 97 without any frame. Zero-contradiction
fails. Clause 1 does not resolve.

### Clause 2: 78's value

78's only stated value is LEAD "ver" (red-team R16-005: bundle graded LEAD,
not settled). Attempted parse: "la ver(?) e [97] [86] [91]" — "la 78-40" reads
"la vere"/"la verre"-shaped under 78="ver", but 97/86/91 remain unparsed:
97 has no adjective slot (contradicted by its pre=00 x4 INF distribution),
and no role exists for 86 or 91 in the tail. Zero-contradiction fails. The
@296 re-parse is already gated as queued `ver78-296-97gate` (runs once
frame-97-profile and stem-86 have verdicts) — this battery defers to it.
Clause 2 does not resolve.

### Clause 3: 86-as-letter against the promoted 12/34/40/48 set

Promoted letter tier: 12="n", 48="e" (R17 grants); pencil banked: 34="i",
40="e". Test results:

- (a) 86 takes 29="er" compositionally in 4 stem windows (@431, @1375, @1391,
  @1825 — re-verified against stem-33-86's list). A letter-cell does not host
  the infinitive ending as a verb stem. Behavioral contradiction of
  86-as-letter.
- (b) 86 neighbors a promoted letter-cell in only 2/32 windows (suc=48 @728;
  suc=12 @1739, the ni-frame). Letters cluster with letters; 86 does not
  (30/32 windows, letter-free).
- (c) In the @300 window, 40="e" is separated from 86 by 97, so the letter
  reading would require 97 (and 91) to be letter-tier too — contradicted by
  97's pour-governed distribution (pre=00 x4; suc=00 @1823 "pour [97] pour…",
  which no letter can precede). Granting 97/91 letter status would invent data.
- (d) Frequencies: 86 n=32 (1.73%) vs 12=23, 34=11, 40=21, 48=38 — same band,
  non-discriminating; the behavioral tests (a)–(c) carry the weight.

86-as-letter is rejected. The @300 orphan is CONFIRMED: no infinitive frame,
no nominal slot, suc=91 blocks stem (per stem-33-86's localization), and the
letters-context rescue fails.

## Per-clause pass/fail

1. Stated 97-class whole-parse: FAIL — no stated 97-class exists (naming is
   queued as frame-97-profile); the INF hypothesis fails the whole-window test.
2. Stated 78-value whole-parse: FAIL — 78="ver" is an unsettled LEAD
   (R16-005) and yields no contradiction-free parse of the window.
3. Letters-context rejected, orphan confirmed: PASS — (a) 86-29 stems x4
   contradict letter behavior; (b) letter-adjacency 2/32; (c) 97's
   pour-distribution contradicts letter-tier 97 at @300.

## Adverses disposition

- "97's and 78's classes open": ANSWERED — both remain open. 97's class is
  owned by queued `frame-97-profile`; 78="ver" stands as R16-005 LEAD
  (unsettled); the @296 re-parse is queued as `ver78-296-97gate`. Fenced with
  stated cause, not ignored.
- "86-as-letter would tension A9's INF-class grant (red-team eyes)": FENCED —
  the letters hypothesis was rejected on behavioral/distributional grounds
  before reaching the grant, so the tension is not decided at battery level.
  Flag for red-team eyes: a letter reading of 86 at @300 would require
  letter-tier status for 97 as well, and 97 pre=00 x4 sits in the INF class
  under A9's 00="pour" leg-1 class-level grant. Any revival of 86-as-letter
  must reconcile with A9 first.

## Standing-verdict check

No contradiction found. R16-005 (78="ver" LEAD) untouched — this battery only
tested it, never asserted it. A9's INF-class grant untouched. stem-33-86's
null (orphan list incl. @300) is confirmed, not contradicted. A10, A14,
nest-subject-86-62-42 unaffected. No escalation.

## Verdict: kill

The claim "@300's 86 resolves via 97's or 78's class" is refuted at kill
grade: no stated 97-class exists, the only stated 78-value is an unsettled
LEAD that cannot parse the window, and the bar's fallback letters-context
hypothesis is rejected by 86's stem behavior and letter-adjacency rate. The
@300 orphan stands CONFIRMED (the bar's else branch is satisfied; the
resolution claim is dead).

## Follow-ups

None proposed — kill verdicts do not regenerate work, and the @300 line is
already covered going forward: `frame-97-profile` (queued) will name 97's
class, and `ver78-296-97gate` (queued, gated) will re-parse @296 once
frame-97-profile and stem-86 have verdicts. Proposing new targets here would
duplicate queued work.

## Reproducibility

Census scripts run inline in this session against the repaired stream only
(assert 1,847 pairs / 96 groups before each count). No writes outside this
report, the queue entry, and the lockfile.
