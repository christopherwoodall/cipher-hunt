# Battery report: prefix-productivity-08

- Target id: `prefix-productivity-08` (priority 3)
- Claim: "test 08-65 x2 as a second prefixed stem (establish 65's verb-shapeness first)"
- Date: 2026-10-09
- Worker: agent a34158b9-6fcf-42f5-9233-61bde7380798
- Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
  Asserts held: 1,847 pairs, 96 types, gloss (i) crib "117082342940" pair-aligned.
  `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Sibling context read first: battery-prefix-08-31 (NULL, 2026-10-09) — the parent;
  this target is its follow-up #1. Also read: battery-prof-65 (PROMOTE, processed),
  next-token-redteam-r20.md (R20-047).

## Bar (verbatim, pre-registered)

"promote iff 08-65 x2 parses as prefixed stems with 65 verb-shaped; kill iff no second stem exists"

## Bar restated as numbered clauses (fixed before testing)

- C1 (promote arm): "08 65" x2 parses as one prefixed-verb word at both windows
  AND 65 is verb-shaped (frame census) — with every adverse answered.
- C2 (kill arm): no second verb-shaped stem exists among 08's successors
  (65 non-verbal, 62 pronominal, singletons non-verbal) → kill.

## Method

Re-derived the repaired stream inline. Censused all 18 windows of 08 and all
25 windows of 65 (predecessors/followers, ±6 context). Adopted the prof-65
class verdict (65 = noun, verb rival killed at kill grade) and checked its
red-team standing (R20-047: GRANT, "65 stays ['noun','cls']"). Tested the two
08-65 windows against the prefix parse and the separate-word parse. Swept 08's
11 singleton successors for any established verb stem.

## Window-level evidence (@-offsets, repaired stream)

n(08) = 18; successors: 31 x3, 65 x2, 62 x2, 91/34/21/67/24/52/29/01/43/81/55 x1.
n(65) = 25; predecessors {21:x4, 40:x3, 91/74/24/08/06:x2, ...};
followers {63:x4, 23:x3, 64:x3, 13:x3, 94:x2, ...}.

The two 08-65 windows:
- @922 [a5_09]: `74 74 40 [08 65] 71 17 61 96 48`
- @1339 [a5_09→a7_05]: `71 64 60 [08 65] 64 52 38 47 86`

65's class (adopted, not re-litigated): battery-prof-65 PROMOTE — 65 = NOUN,
verb rival killed at kill grade on L1 (three "65 qui" windows: @724, @1208,
@1340 — a verb cannot antecede "qui", 64=qui granted). Ratified by the red
team: R20-047 GRANT, registry "65 stays ['noun','cls']"; only gender deferred.

Kill-grade facts against 65's verb-shapeness:
- @1340 is the SAME window as the target's @1339 locus: `08 65 64` = "08 65
  qui". prof-65's L1 cites exactly this window as a qui-relative head. Under
  the prefix parse ("08-65" = prefixed finite verb), "qui" would follow a verb
  with no nominal antecedent — ungrammatical in French at any period. The
  promote arm's own locus window kills the verb reading of 65.
- "qui 65" (64 before 65) x1 @1588 is 65's sole verb-ish leg, against three
  qui-relative-head windows, two "29 40 65" direct-object slots, and two
  post-finite-verb object slots (prof-65 L2–L5). Not verb-shaped at battery
  grade.

Singleton-successor sweep (no second stem anywhere):
- 08→91 @35: 91 is a noun candidate (DET-91 windows) — nominal, not a stem.
- 08→34 @60: 34="i" banked letter — word-internal, not a stem.
- 08→21 @98: 21 unvalued, noun-ish contexts — no verb frame.
- 08→67 @198: 67 = et/veut (sole polyvalence) — a full word, not a stem.
- 08→24 @534: 24 = finite/modal verb CLASS (granted) — a full finite word;
  a prefix composing with an already-finite verb is not a "prefixed stem".
- 08→52 @631, 08→01 @975, 08→81 @1592, 08→55 @1610: unvalued, no verb frames.
- 08→29 @779: 29="er" banked letter — word-internal.
- 08→43 @1302: 43 nominal class (par-[43] windows) — nominal, not a stem.
- 08→62 x2 (@944/@1323): pronoun-shaped (62-94 x9; battery-62-boundary-census
  PROMOTE) — the parent's negative control; a verbal prefix cannot compose
  with a pronoun. Stands.

## Per-clause pass/fail

- C1 (promote arm): FAIL at kill grade. 65 is noun-class by battery PROMOTE
  and red-team GRANT (R20-047); the verb rival is dead at kill grade on three
  independent windows, one of which (@1340) IS the target's own @1339 locus.
  "08-65 = prefixed verb stem" is therefore ungrammatical at the locus itself.
  65 is not verb-shaped; the arm's premise is false.
- C2 (kill arm): FIRES. No second verb-shaped stem exists: 31 x3 remains the
  only verb-shaped successor of 08; 65 x2 is nominal; 62 x2 is pronominal;
  all 11 singletons are letters, full words, nominals, or unvalued cells with
  no verb frames. 08's prefix attachment stays a 31-only singleton stipulation.

## Verdict

**kill** — 65 is noun-class (battery PROMOTE, red-team R20-047 GRANT); the
verb-65 rival is dead at kill grade, including at the @1339 locus window
itself ("08 65 qui"). No second verb-shaped stem exists among 08's successors.
Per §4 (kill), no follow-ups are required. No standing red-team verdict is
contradicted or downgraded; §7 intact (sole-polyvalence rule untouched —
nothing here asserts a value for 08).

## Bookkeeping

- Queue: `prefix-productivity-08` → `status: verdict`, `result: kill`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; own entry only; no downgrade).
- Lock created on start, deleted on completion.
