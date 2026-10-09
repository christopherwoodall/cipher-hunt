# Battery report: split-03-redteam-feed

- Target id: `split-03-redteam-feed`
- Claim: "package the uniform-verb-03 fence (12 kill-grade windows documented in battery-val-03-value-census) as red-team input for the deferred 03/71 section-7 split docket"
- Adverses: "red-team venue: batteries do not decide splits (R20 deferred 03/71)"
- Date: 2026-10-09
- Worker: battery worker (subagent 0ed4303b-4ad9-49c9-845f-e31374a1fb30)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

Terms (ASD-STE100): "uniform-verb-03" = the claim that one verb-stem value for 03 parses all 20 03-windows. "Fence" = the claim is dead at battery grade with stated kill-grade causes. "Split" = conditioned split under §7: different classes in different licensed positional frames. "Polyvalence" = true homophony (§7: 67 et/veut is the sole standing instance). "Deferred" = the red team has not adjudicated the item.

## Bar (verbatim, pre-registered before testing)

"evidence package for red-team adjudication; gather-only, no battery decision"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** the package delivers the uniform-verb-03 fence (all 12 kill-grade windows, with @-offsets and byte-exact contexts) → PASS on delivery.
2. **C2:** the package includes the standing red-team base (R19-178 conditioned grant, R19-180 split package, R20 deferral) so the red team adjudicates against the full record → PASS on delivery.
3. **C3:** the package makes no battery-level decision on the §7 split → PASS (nothing declared, per the adverse).

## Method

1. Read BATTERY-PROTOCOL.md in full before touching anything. Created `code/crowd17/next-token/locks/split-03-redteam-feed.lock` on start (agent id + 2026-10-09T19:00:00Z; no prior/stale lock); deleted on completion.
2. Re-derived the repaired stream in-session; byte-confirmed n(03)=20 and all 12 kill-grade windows of `battery-val-03-value-census` byte-exact (§3 below).
3. Read the standing record: R19-178, R19-179, R19-180, R19-186 (next-token-redteam-r19.md), R20 deferral table (next-token-redteam-r20.md), and the post-R19 battery outcomes `val-03-value-census` (NULL), `val-03-noun` (NULL), `seg-77-03-722` (NULL), `val-03-letter-probe` (KILL). No data re-tested; all evidence adopted at face value from the red-team record and verdict reports, re-anchored to the stream.
4. 1841 diplomatic French throughout.

## Findings — ruling-ready package

### P1. Standing red-team base (adopted, not re-litigated)

- **R19-178 (GRANT-WITH-CORRECTIONS):** stem-03 promoted as verb-stem **conditioned to the "03 29" frame ×3** (@1030/@1320/@1594 0-based). F1 @1321 passes on R17-009's finite/modal class; F2 @1031 STRUCK (exclamatory-infinitive skeleton corpus-fenced, 0 genuine in 27.66M chars); F3 @1595 passes, conditional on nounfamily C2 + §7 uniformity. Registry: ADD ["03","verb-stem","cls"] — conditioned scope only.
- **R19-179 (GRANT, window-local):** "03 29" = stem+ending forced given 03 word-shaped (nounfamily C2) + §7.
- **R19-180 (GRANT, finding grade: split evidence package):** 12/12 03-windows noun-compatible, 7 forced-nominal; **split packaged, NO polyvalence declared** (correct §7 posture). Registry: none. R20 frame: "03 conditioned split vs second polyvalence (§7)."
- **R19-186 (GRANT, finding grade: §7 split candidate):** 71 split-candidate; no split declared.
- **R20 (deferral table):** "03 and 71 §7 splits | DEFER — no docket item owned them; R19-178 (stem-03) and R19-186 (71 split-candidate) stand on their own dockets."
- **R19-142 / R20-038:** the @1028–1031 window ("Ceci, [03]er!" reading) stays **FENCED** — do not ratify for banked use.

### P2. The uniform-verb-03 fence (battery-val-03-value-census, NULL 2026-10-09)

n(03)=20; tally **12 kill-grade, 5 fenced, 3 "03 29" legs**. Re-verified byte-exact in-session on the repaired stream (all 12 windows matched the report's ±4 contexts to the pair). A bare (uninflected) verb stem is ungrammatical in French; a stem needs inflection or a licensing frame.

Kill-grade windows (0-based @-offsets, byte-exact contexts re-verified):

| # | @ | context (±4) | kill cause (standing values only) |
|---|---|---|---|
| 1 | 31 | 00 34 24 30 **03** 64 32 01 08 | bare 03 before granted "qui" (64); bare stem cannot head a relative |
| 2 | 336 | 45 54 88 40 **03** 64 31 14 45 | "e [03] qui" — bare stem between "e" (40 GT) and "qui" |
| 3 | 657 | 49 24 26 30 **03** 62 16 00 86 | "pas [03]" — "ne…pas" governs an infinitive word, not a bare stem |
| 4 | 664 | 00 86 50 80 **03** 62 06 00 20 | bare 03 adjacent to verb-frame 80 (A8); two verb elements, no license |
| 5 | 674 | 11 86 24 80 **03** 64 37 77 45 | bare 03 between verb-frame 80 and "qui" |
| 6 | 722 | 02 21 80 77 **03** 91 65 64 11 | determiner "le" (77 provisional) + bare 03 |
| 7 | 994 | 49 24 26 30 **03** 60 67 11 96 | "pas [03]" — same as @657 |
| 8 | 1014 | 79 80 78 47 **03** 24 41 15 66 | "ce [03]" — determiner (47 granted A4) + bare stem |
| 9 | 1367 | 94 79 14 60 **03** 30 82 16 91 | W6 "ne…pas" frame; finite-03 REJECTED at R20 (ne-W6-pas-verb) |
| 10 | 1645 | 12 33 98 60 **03** 64 31 10 03 | bare 03 + "qui" |
| 11 | 1649 | **03** 64 31 10 03 38 82 16 01 | bare 03 + "qui" (second 03 at @1653 also bare) |
| 12 | 1790 | 96 21 68 47 **03** 00 86 56 42 | "ce [03] pour" — determiner (47) + bare stem |

Cause grouping: bare-03 before "qui" ×5 (@31/@336/@674/@1645/@1649); "pas [03]" ×2 (@657/@994); determiner + bare 03 ×3 (@722/@1014/@1790); adjacent to verb-frame 80 ×1 (@664); W6 rejected-finite ×1 (@1367).

The 3 "03 29" legs: @1030 FENCED at red-team level (R19-142/R20-038, cannot supply a banked leg); @1320 and @1594 are genuine infinitive legs (R19-178 F1/F3) but accept any -er stem identically — no value nameable (§3 forbids invention).

**Scope of the fence:** it kills only the GLOBAL/UNIFORM claim. It is fully consistent with R19-178's conditioned scope (verb-stem within "03 29" ×3) and with R19-180's nominal arms elsewhere. No value is named for 03 at battery or red-team level.

### P3. Post-R19 battery outcomes on the nominal arm (adopted)

- **val-03-noun (NULL, 2026-10-09):** the candidate inventory is empty; failure is epistemic, not substantive. The six nominal windows remain noun-compatible; R19-180 stands; the split stays red-team venue.
- **seg-77-03-722 (NULL, 2026-10-09):** consistent with the @722 kill row.
- **val-03-letter-probe (KILL):** letter value for 03 killed — removes the letter tier from the split inventory.
- No battery result after val-03-value-census contradicts the fence (queue entries checked 2026-10-09: all verdicts in `battery-queue.json` reconciled).

### P4. The adjudication question for the deferred docket

The R19-180/R20 frame is **"03 conditioned split vs second polyvalence (§7)."** The battery record now supplies both sides at battery grade:
- FOR conditioned split: R19-178's conditioned verb-stem grant ("03 29" ×3) + the uniform fence above (uniformity dead at 12/20 windows) + R19-180's 7 forced-nominal windows.
- AGAINST polyvalence: 67 et/veut is the sole standing true polyvalence; no polyvalence declared for 03 (R19-180 honored §7).
- The 71 arm (R19-186 split-candidate) is on its own docket; this package makes no 71 claim.

No battery decision is made here. The venue for the declaration is the red team's 03/71 §7 split docket (deferred at R20).

## Scope (stated, not hidden)

- Gather-only: the package adds no bankable content beyond what R19-178/R19-180, R20, and the battery record already hold. §7 intact.
- The 12-window re-verification used the repaired 1,847-pair/96-type stream (re-derived in-session; asserts held; `canonical.py` never used). Canonical-stream caveat stands (68/70 upstream row offsets unvalidated).
- No standing or red-team verdict contradicted, downgraded, or re-litigated. The adverse is honored: no split declared.
- Per the gather-only precedent (R19-182 GRANT of fem32e-1211-redteam-input as "ruling-ready package"; battery-redteam-tonic-fence-input NULL gather-only), no new follow-up targets are proposed: the package is complete and all further battery work on the 03 split question is blocked on the red-team docket.

## Per-clause pass/fail

- C1: PASS — 12 kill-grade windows delivered with byte-exact contexts, re-verified in-session.
- C2: PASS — standing red-team base (R19-178/R19-180/R19-186/R20 deferral, R19-142 fence) included in full.
- C3: PASS — no battery-level split decision; adverse honored.

## Verdict: NULL (gather-only package delivered)

The evidence package for red-team adjudication of the deferred 03/71 §7 split docket is complete and ruling-ready. No battery decision is made. No registry change requested. Further battery work on the 03 split question is blocked until the red team adjudicates the deferred docket.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-split-03-redteam-feed.md` (this file).
- Queue: `split-03-redteam-feed` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade; no existing verdict overwritten).
- Lock `code/crowd17/next-token/locks/split-03-redteam-feed.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched. No standing/red-team verdict contradicted; §7 intact.
