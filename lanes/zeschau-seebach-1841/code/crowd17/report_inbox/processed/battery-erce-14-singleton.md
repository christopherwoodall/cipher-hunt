# Battery report: erce-14-singleton

- Target: `erce-14-singleton`
- Verdict: **NULL** (dependency fence executed — the bar's conditional trigger is unmet; no content decided)
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse from `code/side-keyhunt/repaired_offsets.json`
  + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
  (asserts held: 1847 pairs, 96 types). `canonical.py` never used.
- French frame: 1841 diplomatic French.

## Bar (verbatim)

"test '29 47 14' @423 once 14's value resolves - boundary ('er | ce [14]') vs internal ('[49][36]erce')"

## Bar restated as numbered clauses

- (C1) 14's value has resolved (a named value usable as a licensed premise for the test).
- (C2) If C1 fires, the '29 47 14' window at @423 is tested: boundary ('er | ce [14]')
  versus word-internal ('[49][36]erce').

The bar is conditional by construction: the test only runs once C1 fires. Per the task,
the dependency is evaluated in the bar and the test is fenced if unmet.

## Method

1. Re-derived the repaired stream in-session; verified the locus bytes and the
   '29 47' cluster census.
2. Checked 14's value-resolution status: `code/table-grid/table-registry.json`,
   battery verdicts in `battery-queue.json`, and the R20 red-team report.
3. Evaluated C1 before running any window test.

## Findings — C1 fails: the dependency is unmet

- The registry holds 50/96 cells; **there is no '14' cell at all**. 14's class and
  value are unregistered.
- 14='en' exists only as **battery-grade** evidence: `en14-value-tighten`
  (PROMOTE) states verbatim "(battery grade; red-team ratification of 14=`en`
  still pending)", and `core-14-622-bank` (PROMOTE) banks a locus-level 'en'
  frame only. R20 references 14='en' as "battery promote" (R20 report lines
  ~524, ~868–874), never as a ratified value.
- A battery promote is not a resolved value for this bar: the red team has not
  ratified 14's value, and the target's own adverses record "14's value is open"
  as the reason Frames B/C are untestable at battery grade
  (battery-frame-29-47). Adopted, not re-litigated.
- **C1 FAILS.** The conditional does not fire; the boundary-vs-internal test at
  @423 cannot run under a resolved value. The test is fenced (evidentiary,
  re-openable once 14's value resolves). C2 is moot — the condition never fired.

## Byte verification (window-level, repaired stream, 1-based @ matching claim)

- '29 47' occurs exactly 4× stream-wide: 1-based @23, @423, @1231, @1591
  (0-based @22, @422, @1230, @1590) — matches the claim.
- @423 locus (0-based @422): '46 49 36 | 29 47 14 | 62 48 76 42' — matches the
  claim's '@423 window' context byte-exact.
- 47's followers at the cluster: 33 ×2 (@23, @1231), 14 ×1 (@423), 08 ×1 (@1591)
  — matches the claim.
- With 29='er' (pencil GT) and 47='ce' (A4, granted), the window is the
  singleton '29 47 14' trigram (1× stream-wide).

## Adverses answered

- "14's value is open, so Frames B/C are untestable at battery grade" —
  confirmed still open at resolution grade; fence stands.
- "the boundary reading is already killed at the systematic Frame A
  ('29 47 33' x2) by standing kills ce-inf-1841 and the @23 fence, so the
  internal reading is favored there" — adopted as standing context; nothing
  about the @423 window is decided by this report.
- No standing or red-team verdict contradicted, downgraded, or re-litigated.
  §7 intact. Canonical-stream caveat stands.

## Verdict

**NULL** — the bar's conditional trigger (C1: 14's value resolved) is unmet, so
the boundary-vs-internal test does not fire. Nothing about the @423 window is
decided; the fence is on the test's admissibility, re-openable on resolution.

## Follow-ups (both verified ABSENT from battery-queue.json)

1. `erce-14-rearm` (P4, gated on red-team ratification of 14's value) — re-run
   the '29 47 14' @423 boundary-vs-internal test once 14's value is registered;
   bars: boundary ('er | ce [14]') vs internal ('[49][36]erce') decided at
   battery grade under the registered value.
2. `erce-14-423-conditional` (P4) — test the same window under the provisional
   14='en' battery-grade premise only (conditional logic, disclosed as
   provisional); fence if any step demands a resolved value.

## Scope

Dependency fence only. Untouched: 14's value question, en14-value-tighten /
core-14-622-bank promotes, the '29 47 33' frame verdicts, §7, red-team docket.
R5005, sealed gates, red-team adjudication queue untouched.

## Bookkeeping

- Lock: `code/crowd17/next-token/locks/erce-14-singleton.lock` created on start
  (agent 293d4363-3b33-4809-811c-2a01a6e665a7, 2026-10-09T21:04:11Z; no stale lock),
  deleted on completion (verified gone).
- Queue: `erce-14-singleton` → `status: verdict`, `result: null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; target-id-unique temp
  `battery-queue.json.erce-14-singleton.tmp` + atomic rename, no leftover;
  disk re-validated; own entry only; no downgrade).
