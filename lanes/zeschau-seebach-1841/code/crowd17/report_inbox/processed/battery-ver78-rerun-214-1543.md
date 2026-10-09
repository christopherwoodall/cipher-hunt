# Battery report: ver78-rerun-214-1543

- Target id: `ver78-rerun-214-1543`
- Claim: re-test soft-fail windows @214 and @1543 as noun-head 'le ver' frames, or fence.
- Date: 2026-10-09
- Worker: battery worker (subagent e31628b9-4e0e-49fc-8511-14e8e6718854)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; asserted in-session: 1,847 pairs, 96
  types). `canonical.py` never used. R5005, sealed gates, red-team queue
  untouched.
- Lock: `code/crowd17/next-token/locks/ver78-rerun-214-1543.lock` created
  2026-10-09T12:01:37Z (no prior lock); deleted on completion.

Terms (ASD-STE100): "noun head" = the noun of a noun phrase (the word that
heads it). "Fence" = set the question aside with a stated reason, not kill
it. "Standing values" = the lane's banked and promoted values (§7).
"Host" = the word that an ending or particle attaches to.

## Bar (verbatim from battery-queue.json, pre-registered)

"resolve iff both windows parse as noun-head 'le ver' frames under the
resolved neighbor values, or are fenced with stated cause."

(The dispatch brief's shorter bar — "resolve iff both windows parse as
noun-head 'le ver' frames; else fence" — is the same bar. No rewrite.)

Numbered clauses (frozen before testing):

1. **C1:** @214 parses as a noun-head 'le ver' frame under the resolved
   neighbor values (06='ent', ent-06 PROMOTE).
2. **C2:** @1543 parses as a noun-head 'le ver' frame under the resolved
   neighbor values (43's status per noun-43).
3. **Verdict rule:** promote iff C1 and C2 both pass; else NULL, with each
   window fenced with stated cause per the bar's else-arm.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock on start; deleted on
   completion.
2. Re-derived the repaired stream byte-exact. All @-offsets below are 0-based
   repaired-stream pair indices. Windows confirmed byte-exact against the
   parent report's loci.
3. Adopted, never re-litigated: ent-06 PROMOTE (06="ent/ment", 2026-10-09);
   noun-43 NULL (2026-10-09, §4 below); lever-213-complement KILL
   (2026-10-08, §@214); fin-88-1541-parallel KILL ("Il [93-fin] [88-inf] le
   [78]", @1539–1544, adopted as the standing parse of the @1543 window);
   §7 banked/promoted/provisional/killed/split/held values; 67 sole
   polyvalence.

## Window-level evidence

### @214 (row a2_00), 0-based @210–219

`88 @210 | 19 @211 | 74 @212 | 77 @213 | 78 @214 | 06 @215 | 59 @216 |
46 @217 | 29 @218`

Span: "…[19] [74] le(77) ver(78) ent(06) [59] que(46) er(29)…"

Standing: 77='le' (provisional), 78='ver' (claim under test), 06='ent'
(promoted), 46='que' (banked), 29='er' (banked), 59='est' (provisional, and
its est-arm at pre=06 is excluded by the granted conditioner59 rule —
lever-213-complement §standing citations). 74's class is open (n=34;
successors {74x6, 45, 46, 62, 67, 77} — no finite-74 established; no
word-internal 74 license asserted).

Integration test of 06='ent' at @215. 'ent' is a bound verb ending
(ent-06; 06 never word-initial stream-wide, 29 predecessor types). It needs
a verbal host:
- Left host 78 ('ver', the noun head under test): "verent" is not a French
  word. No license.
- Right host 59: "entest" is not a French word. No license.
- Freestanding 'ent': not a French word. No license.
- The [06-59] ISLET-10 V-este verb-unit is the lever-premise-side
  integration (GRANTED-lead); lever-213-complement's kill exhausts the
  lever-premise slots, and the ent-06 promote (post-dating that kill)
  puts the 'ent' axis at battery level — the deadlock it creates here is
  composition-independent, as that battery's L3 records for the F2 twin.
- "…[74] le ver ent [59] que…" — 'ent' stranded between the NP and "que".
  No licensed parse with <=1 open assumption.

The parent adverse pre-stated this outcome: "if 06 resolves 'ent', @214
may stay failed (record, don't force)".

**C1 FAIL — fence.** Stated cause: promoted 06='ent' (bound verb ending,
never word-initial) has no licensed verbal host in the window; both
neighbor compositions ("verent", "entest") are non-French; freestanding
'ent' is not a French word. The 'le ver' NP segment is clean; the failure
is the 'ent' continuation, not 78.

### @1543 (row a8_00), 0-based @1539–1548

`62 @1539 | 93 @1540 | 88 @1541 | 77 @1542 | 78 @1543 | 43 @1544 |
00 @1545 | 46 @1546 | 70 @1547`

Span: "[62] [93] [88] le(77) ver(78) [43] pour(00) que(46) pre(70)…"

Standing: the adopted fin-88-1541-parallel KILL gives the window's parse:
"Il [93-fin] [88-inf] le [78]" — "le ver" is a clean NP, object of the
infinitive 88. 43's value status (noun-43 NULL, 2026-10-09): feminine-noun
class; all four named candidates — suite, manière, condition, mesure —
killed at battery grade; full-distribution survivor set EMPTY; the noun-43
line is closed at battery level pending red-team act.

Integration test of 43 at @1544 with 43's value open:
- Epithet: no surviving candidate is epithet-shaped; none parses
  ("le ver condition" ungrammatical).
- Elided 'de': unlicensed (no standing license for 'de'-elision at 43).
- Apposition ("le ver, [43], pour que…"): unestablished for two bare nouns;
  no standing apposition frame covers it.
- The "pour que prenne 92" purpose clause: its subject is unresolvable
  (the prenne battery's own flag at @1548) — the parent adverse records
  this as the prenne battery's flag, not this target's to fix.
- The lever rival's clean parse at this window ("[88] lever [43] pour
  que…") stays fenced to lever-77-78, not re-litigated; it is NULL, not
  demonstrated.

**C2 FAIL — fence.** Stated cause: 43's value remains open — the queue's
"do not run before 43's value resolves" gate only partially fired, and
noun-43's survivor set is empty at battery level, so no new integration
exists; none of the four exhausted candidates parses as post-nominal
attachment; 'de'-elision unlicensed; apposition unestablished; the purpose
clause's subject gap is the prenne battery's flag. The "le ver" NP itself
is intact under the standing parse; the failure is 43's non-integration.

## Per-clause pass/fail

1. **C1 — FAIL.** No grammatical parse of @214 under promoted 06='ent';
   'ent' stranded. Fenced with stated cause (§@214).
2. **C2 — FAIL.** No grammatical parse of @1543 under noun-43's open value;
   43 unintegrated. Fenced with stated cause (§@1543).

Neither window forces the claim false — 'ver' as noun head is never
contradicted (the "le ver" NP is the clean left segment at @214 and 88's
licensed infinitive object at @1543). Not kill grade. Per the bar's
else-arm: **fence both**.

## Adverses answered

- **06's class resolved (ent-06 promote): ADOPTED.** It is the mechanism of
  the @214 fence — the promote's own scope (verb endings on "ne ment(ent)"
  frames) supplies no host for a stranded 'ent' after a noun.
- **43's value open (noun-43 null): ADOPTED.** The gate's second trigger
  did not fire; noun-43's survivor set is empty at battery level. The
  bar's fence else-arm is exercised rather than forcing a value.
- **Parent adverse on @214 (stays failed if 06='ent'): CONFIRMED.** The
  predicted outcome materialized; recorded, not forced.
- **Parent adverse on @1543 (prenne subject gap): HONORED.** The purpose
  clause's unresolvable subject is recorded as the prenne battery's flag;
  this target does not attempt to fix it.

## Verdict: NULL

No red-team contradiction: ent-06's promote is adopted (not re-litigated or
downgraded); noun-43's null is adopted; lever-213-complement's kill is
convergent (the composition-independent deadlock it records for the F2
twin now has the ent-06 promote in place, unchanged in outcome);
fin-88-1541-parallel's kill is adopted as the standing parse of @1543;
ISLET-10 is not re-litigated. No existing verdict downgraded. §7 intact
(67 sole polyvalence). Canonical-stream caveat stands (rows a2_00/a8_00
unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `ver78-1543-rerun-gated` (P4) — re-run @1543 once 43's value is named;
   bar: resolve iff "le ver [43-value]" parses as a noun-head frame with
   <=1 ungranted assumption; else fence. The remaining gate for this
   target's C2.
2. `ent-06-host-214` (P3) — name 06's host classes across all 44 06-windows;
   bar: 'ent' binds only to licensed verbal / 94-82 frames; if no host
   class covers "[noun] ent [est] que", fence the span as residual.
   Resolves whether @214's 'ent' strand is a standing residual.
3. `val-74-212` (P3) — name 74's class at @212; bar: verb-shaped 74
   licenses "[74-fin] le ver…" as a subject-NP left clause, else fence
   the left edge; revives @214's NP-integration arm independent of the
   'ent' continuation.

## Bookkeeping

- Queue: `ver78-rerun-214-1543` → status `verdict`, result `null`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/ver78-rerun-214-1543.lock`: created on start, deleted on
  completion (verified gone).
