# Battery report: det-91-11-frame (NULL — fence executed)

**Target:** `det-91-11-frame` (priority 3). Worker session 78cdab46-f1f1-4e1c-a8c6-6ddcf64cceee (supervisor-dispatched).
**Date:** 2026-10-09. **Verdict: NULL** (fence executed; not kill grade).
**Parent:** battery-antec-08-91-39 (NULL, 2026-10-09).

## Bar (verbatim from battery-queue.json — pre-registered BEFORE testing)

"promote 91 nominal iff 'la' licenses a following-NP frame with stated byte cause at both windows; else fence with stated cause"

## Bar as numbered pass/fail clauses (frozen before testing; not modified after seeing data)

1. **C1 (promote arm, W1):** at the 1b @1006 window, 'la' (11=banked GT) licenses a following-NP frame with stated byte cause → counts toward promoting 91 nominal.
2. **C2 (promote arm, W2):** at the 1b @1669 window, 'la' licenses a following-NP frame with stated byte cause → counts toward promoting 91 nominal.
3. **Else-arm:** if either clause fails, fence the '91 11' nominal route with stated cause (fence, not kill — no window forces 91 nominal false).

## Method

1. Read `BATTERY-PROTOCOL.md` in full. Created `code/crowd17/next-token/locks/det-91-11-frame.lock` on start (no stale lock; deleted on completion).
2. Re-derived the repaired 1,847-pair stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py` (1,847 pairs, 96 types asserted). `canonical.py` never used. R5005, sealed gate instances, red-team queue untouched. Offsets: "0b" = 0-indexed pair stream; "1b @N" = 0b @N−1 (lane convention).
3. Confirmed "91 11" is exactly x2 stream-wide (0b @1005–1006, 0b @1668–1669; 91 n=21, 11's only 91-predecessors) — the two windows named in the claim are exhaustive; no third "91 11" window exists to rescue the bar.
4. Tested "la [X]" NP licensing on STANDING values only (protocol §7 banked/promoted/granted). Did not re-run the queued la-1006-52-frame adjective-arm control; did not re-litigate 78='ver' (R16-005 LEAD-not-settled respected) or adj-91-nulls' adjective fence (different bar, no duplication).
5. Canonicality caveat stands: rows a6_02 and a8_05 are among the 68 unvalidated upstream row offsets.

## Window-level evidence (@-offsets, repaired stream)

**W1 — 1b @1006 (0b @1005–1006), row a6_02:** `33 00 86 56 47 91 11 52 35 18 79 80 78 47`
→ "…ce[47,granted] [91] la[11,banked] [52] [35] [18] tout[79,granted] [80,A8-verb]…"

- The 'la'-licensed NP candidate is "la [52]". 52's class is unsettled on standing values: adj-52-37-value NULL (même/seule/dite tie), unit-52-37-name NULL, la-frame-52-37-43-noun NULL, la-1006-52-frame queued (control not yet run).
- The only standing NP evidence touching "la 52" is the byte-identical "la 52-37 43" tail pair (1b @1124/@1722) — itself NULL, and **not transferable**: this window has "la 52 35", not "la 52-37". "la 52" x3 stream-wide; this instance is the tail-less one.
- No banked/promoted/granted nominal head follows 'la' at this window. Stated byte cause for a licensed NP: **absent**.

**W2 — 1b @1669 (0b @1668–1669), row a8_05:** `22 94 84 64 06 91 11 78 55 81 92 60 03 39`
→ "…ne[94,promoted] on[84,A15] qui[64,granted] [ent-06,promoted] [91] la[11,banked] [78] [55] [81]…"

- The 'la'-licensed NP candidates are "la [78]" or the extended "la [78] [55] [81]".
- "la [78]": 78's value is open — ver-78 NULL, ver-78-rebar NULL; 'ver' is a red-team R16-005 LEAD, correctly not settled. No battery-grade nominal cause.
- "la … [81]": 81 is **promoted masculine abstract noun** (noun-81, 2026-10-09). "la" is feminine. A single NP "la [78] [55] [81(masc)]" fails French agreement at the byte level — this is not merely missing evidence, it is an agreement clash against a promoted verdict.
- "la 78" x2 stream-wide; the other instance (1b @297: "11 78 40 97") → "la [78] [e-40]…" — likewise no battery-grade nominal cause.
- Stated byte cause for a licensed NP: **absent**; the extended candidate is agreement-killed.

**Left-frame note (context, not counted toward the bar):** W1's left contact is "47 91" = "ce[47,granted] [91]" — 91 in demonstrative-head position (the adj-91 battery's marginal candidate 3, rejected as an adjective leg but noted as nominal-positioned). The bar asked for the 'la'-following frame only; the "ce 91" frame is named as follow-up nom-91-ce-head, not decided here.

## Per-clause pass/fail

- **C1 (W1 @1006): FAIL.** "la 52 35" — 52 unsettled; the la-52-37-43 tail NP does not transfer (missing "37 43" bytes here); no standing nominal follows 'la'.
- **C2 (W2 @1669): FAIL.** "la 78 55 81" — 78 open; the only battery-grade nominal in reach (81) is promoted masculine, clashing with feminine "la".
- **Else-arm: FIRES.** The '91 11' nominal route is **fenced**: at neither of the two exhaustive "91 11" windows does 'la' license a following-NP frame with stated byte cause.

## Adverses (answered, none ignored)

- "coordinate with adj-91-nulls — do not duplicate its bars": honored. adj-91-723-second-leg fenced 91's **adjective** reading (@"le 03 91" stands alone). This battery tested the **determiner-licensed NP frame** — a disjoint bar; no re-test of adjective-shaped windows.
- "11='la' banked GT": adopted as given, not re-litigated. (Note: the bar's premise needs 'la'-as-article; the clitic-article decision at these windows is follow-up det-91-la-clitic-test.)

## Standing-state check (no contradiction, no downgrade)

- No red-team verdict on 91 exists; 91's value stays open. The fence constrains the licensing route, it does not kill any 91 value — C3's fence grade is per the bar's own else-arm.
- noun-81's promoted masculine verdict was used as evidence, not re-litigated.
- R16-005 (78='ver' LEAD, correctly not settled) respected: 78 was not settled at battery level.
- §7 intact: 11=la banked GT used as premise; no polyvalence declared; 67 sole-polyvalence untouched.

## Verdict: NULL (fence executed)

Neither "91 11" window gives 'la' a battery-grade following-NP frame: W1 lacks the "37 43" tail bytes that the only live "la 52" NP evidence depends on, and W2's extended candidate crashes on the promoted masculine noun-81 vs feminine "la". Not kill: no window forces 91 non-nominal; the "ce 91" head frame (W1 left context) is a live, separate nominal route.

## Follow-ups proposed (all verified absent from battery-queue.json)

1. **det-91-la-clitic-test** (P3): decide article vs object-clitic for 11 at 1b @1006/@1669. The bar's premise needs 'la'-as-article; if "la" is the clitic at both windows, the det-frame route dies at kill grade and 91 needs a new frame entirely. Bar: decide article vs clitic at both windows once 52's and 78's classes land; coordinate with queued la-1006-52-frame — do not duplicate it.
2. **det-91-81-agree-test** (P3): at W2 (1b @1669), test whether "la [78] [55] [81-masc]" admits ANY grammatical parse under standing values given the la/81 agreement clash. Bar: if no parse survives the clash, harden the W2 fence into a kill of the la-frame route for 91; else record the surviving parse.
3. **nom-91-ce-head** (P4): test 91 as demonstrative-head nominal via the W1 left frame "ce [91]" (1b @1005–1006, 47=ce granted). Bar: name 91 nominal iff a second independent DET+91-head frame stands on the repaired stream; else fence the ce-head route. Adverses: do not duplicate adj-91-723-second-leg's adjective fence (that battery rejected @1004 as an ADJECTIVE leg; the nominal arm was never decided).

## Bookkeeping

- Report: this file (`code/crowd17/report_inbox/battery-det-91-11-frame.md`).
- Lock: `code/crowd17/next-token/locks/det-91-11-frame.lock` created on start, deleted on completion.
- Queue entry `det-91-11-frame` updated via temp-file + rename (pre-write assert: status `queued`, verdict null; post-write JSON re-validated; own entry only).
