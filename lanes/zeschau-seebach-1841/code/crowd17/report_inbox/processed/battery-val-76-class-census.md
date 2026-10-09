# Battery verdict: val-76-class-census — PROMOTE (battery-grade confirmation of R19-111)

- Target id: `val-76-class-census`
- Claim: Name 76 class from its 21 windows ("le [76]"x3 / "ce [76]"x2 nominal legs vs "ne [76]"x2 / "qui [76]" verbal legs); a forced nominal-76 re-opens the inversion route at @12, a forced verb-76 closes it.
- Date: 2026-10-09
- Worker: battery worker (subagent fee48b16-a546-474f-98d4-b8e12e95bb49)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived in-work, asserts held). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.

Terms (ASD-STE100): "frame leg" = a window where standing values on 76's
neighbors license 76's class with zero new assumptions. "Battery grade" =
uses only granted/promoted/pencil ground-truth values.

## Bar (verbatim from battery-queue.json, pre-registered)

"class named with >=2 frame-legs at battery grade"

Numbered pass/fail clauses (fixed BEFORE the stream census, not modified after):

- **C1:** >=2 frame-legs license the same class for 76 at battery grade.
- **C2:** No bar clause fails at kill grade (no window forces the named class false).

## Critical context (found during work, not an adverse)

**R19-111 already promoted 76=noun.** `next-token-redteam-r19.md` R19-111:
"noun-76 — GRANT PROMOTE (76=noun, masculine). Registry: UPGRADE 76
['noun','lead']→['noun','prom']; _meta: gender masculine; class legs
conditional on 77='le' provisional."

This battery therefore does NOT name a new class. It independently tests
whether >=2 battery-grade frame-legs confirm the standing promote — and,
critically, whether any legs exist that do NOT depend on provisional
77="le" (R19-111's stated condition). Per protocol §5, a confirming result
is not a contradiction; no escalation is triggered.

R20-116 independently used "le [76]" as a direct object ("[03] [02]
pourvoient le [76]", subject + 3pl finite verb + direct object), a second
red-team presupposition of nominal-76.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/val-76-class-census.lock` on start
   (agent id + 2026-10-09T17:25:00Z); no stale lock present.
2. Re-derived the repaired stream byte-exact per `repair_parse.py`.
3. Full census of all 21 windows of 76 with ±3 context; tabulated
   predecessor/successor distributions.
4. Tested each claimed leg against standing values only.

## Window-level evidence (all byte-verified on the repaired stream)

### Nominal legs

**"ce [76]" x2 — granted-value legs (battery grade, independent of provisional 77):**

- **@1273** (row a7_02): `30 20 64 47 [76] 87 76 48` — "47 76" = "ce [76]".
  47="ce" (A4, allophone tier, standing). Demonstrative determiner "ce"
  requires a nominal complement → 76 nominal. Zero new assumptions.
- **@1275** (row a7_02): `64 47 76 87 [76] 48 56 85` — "87 76" = "ce [76]".
  87="ce" (promoted/granted, standing). Same determiner frame → 76 nominal.
  Zero new assumptions.

On "ce" determiner vs pronoun: pronoun "ce" in 1841 French occurs
exclusively with etre-forms ("c'est", "ce sont", "ce fut"). No evidence
places an etre-form at 76 (59 is the "est" candidate, provisional). The
determiner reading ("ce [N]", core French frame) is the only licensed
parse. Both legs are independent windows (distinct bigrams, distinct "ce"
cells: 47 vs 87).

Caveat recorded: the two legs are 2 groups apart in one clause ("20 64 47
76 87 76 48"); the larger "qui ce [76] ce [76]" clause is odd (the "qui"
left context is unparsed), but the "ce [76]" bigram frame stands on its
own in each window.

**"le [76]" x3 — provisional-value legs (supporting, not battery grade):**

- **@833** (row a5_06): `24 87 11 77 [76] 59 35 56` — "77 76" = "le [76]".
- **@892** (row a5_08): `00 86 06 77 [76] 01 98 82` — "77 76" = "le [76]".
  (R20-116's "pourvoient le [76]" direct-object window.)
- **@969** (row a6_00): `19 24 06 77 [76] 01 98 48` — "77 76" = "le [76]".
  77="le" is provisional (§7), so these three are supporting legs only.

### Verbal legs (counter-evidence assessed)

- **"qui [76]" x1 @487** (row a2_11): `30 01 19 64 [76] 42 41 20`.
  64="qui" (granted). Relative "qui" requires a finite verb → 1 verbal
  leg at battery grade. Does NOT meet the >=2 bar. Recorded as a
  residual; re-explaining it is red-team venue (cf. R19-111's promote,
  which stands).
- **"ne [76]" x2 @652/@1577** (rows a4_02/a8_01): `52 82 94 [76] ...`.
  94="ne" is STRONG LEAD (R17-001), not granted → not battery grade.
  R20 already flagged @651-652 as "ungrammatical under standing values
  (@651=94='ne' + @652=76 promoted noun — 'ne' is strictly preverbal)".
  Known residual, not a refutation.

### Distributional summary (n=21)

Predecessors: 77x3, 67x2, 48x2, 94x2, 16x2, 98x1, 64x1, 13x1, 37x1,
93x1, 07x1, 01x1, 47x1, 87x1, 31x1. Successors: 47x4, 42x3, 49x3, 45x2,
87x2, 01x2, 82x1, 18x1, 59x1, 85x1, 48x1.

No predecessor or successor forces a verbal reading at kill grade. The
nominal frame ("ce"/"le" + [76]) is the only determiner frame present.

## Per-clause results

- **C1: PASS** — 2 nominal frame-legs at battery grade ("ce [76]" @1273
  via granted 47, "ce [76]" @1275 via granted 87), plus 3 supporting
  provisional legs ("le [76]" x3). The granted-value legs are new:
  R19-111's legs were conditional on provisional 77="le"; these are not.
- **C2: PASS** — no window forces nominal-76 false at kill grade. The
  verbal legs ("qui [76]" x1, "ne [76]" x2 on a lead value) are residuals
  that do not meet the bar and do not overturn the standing promote.

## Verdict: PROMOTE

76's nominal class is confirmed at battery grade with >=2 frame-legs
using granted values only. This **confirms and strengthens R19-111**
(76=noun, masculine, promoted): the evidential basis no longer depends
solely on provisional 77="le". No registry change is proposed (76 is
already ["noun","prom"]); no red-team verdict is contradicted or
downgraded; §7 intact.

## Implication for @12 (the claim's stated consequence)

"A forced nominal-76 re-opens the inversion route at @12."

- The parent (`battery-inv-98-76-12`, NULL) fenced 98-76 because the
  inversion parse ("vient [76]" as subject-verb inversion) was
  **triggerless AND class-blocked**.
- This battery removes the **class-block**: 76 is nominal (confirmed),
  so a postposed nominal subject after "vient" is grammatically
  available.
- The **trigger-block remains**: @12 shows no licensed inversion
  trigger (no question morphology, no subordinator "que", no initial
  adverbial in "09 00 97 51 47 41 06 77 78 18 93 62").
- Net: the inversion route is re-opened (class leg now passes), but
  "vient [76]" is still unlicensed (trigger leg still fails). The 98-76
  fence stands, with its stated cause narrowed to trigger-only. Updating
  the fence's cause is red-team venue; the fence itself is not disturbed.

The verb-76 arm is closed: only 1 granted-value verbal leg exists
("qui [76]" @487), below the bar, against 5 nominal legs.

## Follow-ups

None required by §4 (promote). One optional note for the supervisor:
`qui-76-487-residual` (P4) — re-explain "qui [76]" @487 under the
confirmed nominal-76 (e.g. test whether 64="qui" admits a non-relative
reading at this window); red-team venue if it resists.

## Bookkeeping

- Queue: `val-76-class-census` queued → verdict/promote via temp-file +
  rename, own entry only; pre-write assert confirmed no prior verdict;
  JSON re-validated post-write.
- Lock `val-76-class-census.lock`: created on start, deleted on
  completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
