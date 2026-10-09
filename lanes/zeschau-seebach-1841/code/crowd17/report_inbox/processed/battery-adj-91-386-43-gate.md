# Battery report: adj-91-386-43-gate

- Target id: `adj-91-386-43-gate`
- Claim: "re-test '43 91 36' @386-387 once noun-43 names 43"
- Date: 2026-10-09
- Worker: battery worker (subagent 216b0b6d-588c-4776-a5da-830b50eb1b40)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "postnominal adjective" = an adjective that comes after its noun ("un homme sage"). "attributive frame" = noun plus adjective together as one noun phrase. "determiner" = a word like "la", "ce", "tout" that marks the noun phrase. "fence" = the reading is blocked at battery grade but not killed — a red-team ruling could re-open it.

## Bar (verbatim, pre-registered before testing)

"91=postnominal adjective iff a determiner-supported attributive parse of '43 91 36' stands under the named 43; else the window stays fenced"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 43 has a battery-grade named value, AND a determiner-supported attributive parse of "43 91 36" stands under that named value.
2. **C2:** iff C1 passes, 91 = postnominal adjective at @386-387.
3. **C3:** else (C1 fails), the window stays fenced — fence executed with stated cause.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/adj-91-386-43-gate.lock` on start (agent id + UTC timestamp 2026-10-09T12:01:40Z); deleted on completion.
2. Re-derived the repaired stream in-session (asserts held). All @-offsets below are 0-based.
3. Standing premises used, not re-litigated: banked/promoted values per §7; 36 = noun class (registry `cls`); 37's value is S5-owned — the adverse bars re-litigating it; noun-43's line is not duplicated — only its standing verdicts are used as premises.

## Window-level evidence

- **Locus byte-confirmed:** 0-based @382–392, row a2_07: `16 52 | 38 37 | 43 91 36 | 62 91 84 73`. The focal trigram "43 91 36" is @386–388.
- **Census (byte-exact, re-derived):** "43 91" x1 stream-wide; "91 36" x1 stream-wide — the locus is the only window for both bigrams. "37 43" x3; "38 37" x1.
- **No determiner at the locus:** no standing determiner (11, 47, 87, 79) is adjacent to 43 at @386. Predecessor chain is "38 37" — 37 sits directly before 43, and 37's frame is predicative territory (adverse: do not re-litigate 37's value). Successor chain is "91 36" with 36 noun-class.
- **n(43) = 16**, re-derived. Only 4 of 16 windows have a determiner adjacent to 43: @343 ("96 43 87"), @563 ("11 43 24"), @1027 ("96 43 87"), @1204 ("47 43 55"). The @386 window is not one of them.

## Per-clause pass/fail

- **C1 — FAIL, on two independent grounds.**
  - *(a) No named 43 exists.* The gate condition ("once noun-43 names 43") never fired: `noun-43` verdict NULL (2026-10-09) — candidate set exhausted, @21 kills monovalent nouns at kill grade; `noun-43-discriminator` verdict KILL (43="suite" rejected); `frame-43-pour-que-1544` verdict NULL; registry has no entry for 43; `prof-43-rerun-polyvalence` is queued on a red-team ruling. Nothing at battery grade names 43.
  - *(b) No determiner-supported attributive parse at this window — value-independent.* Even under a hypothetical named 43, the geometry "38 37 | [43] [91] [36]" is "N [91] N" with no determiner and a predicative-37 left edge. A postnominal adjective needs DET + noun + adjective; this window supplies none of the frame. This leg does not depend on 43's value.
- **C2 — does not fire.** Moot; C1 fails.
- **C3 — FIRES.** The window stays fenced: 91 is not adjective-shaped at @386-387, for two stated causes above.

## Scope and caveat

The fence's second leg (C1b) is value-independent. It means the gate's trigger as written ("once noun-43 names 43") is **insufficient**: naming 43 alone cannot license "91=postnominal adjective" here, because the window lacks a determiner-supported attributive frame regardless of 43's value. Any future re-arm needs new frame evidence at this window (a licensed determiner before 43 or a licensed re-segmentation of the 37-edge), not only a named 43. The @386 window is the sole host of both bigrams, so the adjective arm for 91 via "43 91 36" is doubly fenced — on the missing value and on the missing frame.

## Adverses (answered, none ignored)

- "predicative-37 territory (37's value S5-owned -- do not decide)": honored. 37's value was never tested, litigated, or decided; it was used only as the standing frame leg the parent battery recorded.
- "do not duplicate noun-43": honored. noun-43's bar was not re-run; only its verdict (NULL) and the discriminator's verdict (KILL) are cited as premises.

## Verdict: NULL (fence executed)

The window stays fenced. No standing or red-team verdict is contradicted or downgraded (all 43-naming verdicts stand; §7 intact — no polyvalence declared). Canonical-stream caveat stands (row a2_07 offset unvalidated).

## Follow-ups proposed (null regeneration; all verified ABSENT from battery-queue.json)

1. `detframe-43-hunt` (P3) — census all 16 43-windows for a determiner-supported attributive geometry that could host postnominal-91 once 43 is named; the search space is the four det-adjacent windows (@343/@563/@1027/@1204). Bar: land a "DET 43" frame that licenses postnominal-adjective 91, or fence the attributive-91 arm across the full 43 population.
2. `frame-37-43-1204` (P3) — test the det-adjacent @1204 window ("47 43 55", ce[43]...): if "ce [43]" parses as a licensed NP under standing values, it is the only surviving host candidate for an attributive-91 parse; else fence it there too.
3. `gated-rerun-386-2trigger` (P4) — re-test "43 91 36" @386-387 iff BOTH (a) 43 gets a battery-grade named value AND (b) a determiner-supported attributive frame is landed at this window (see scope caveat). Gated, not dispatchable now.

----
Lock: `locks/adj-91-386-43-gate.lock` created 2026-10-09T12:01:40Z, deleted on completion of this report.
