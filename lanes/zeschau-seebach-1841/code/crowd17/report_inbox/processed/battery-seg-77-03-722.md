# Battery verdict: seg-77-03-722

- Target: `seg-77-03-722` (battery-queue.json, priority 3, status queued)
- Claim: decide the '77 03' frame at @722 directly: nominal-03 vs nominalized infinitive vs word-boundary rival
- Worker: 5752078a-06d9-48b0-aec9-baf4426f3856. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gates, red-team queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/seg-77-03-722.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"name the frame with standing values and zero new assumptions; else fence all three arms at the locus"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (name arm):** one of the three arms (nominal-03 / nominalized infinitive / word-boundary rival) is forced by standing values with zero new assumptions.
2. **C2 (else arm):** if no arm is forced, all three arms are fenced at the locus.

Standing values used (protocol §7): pencil ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77="le"); frames granted (A1 predicative, A8 verb-frames, A3 85 verb-stem, A12 37-01 unit, A7-L2). R20 deferred the 03/71 §7 split; 03's value and class open.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session (asserts held); byte-confirmed the locus.
3. Tested each arm against standing values only: an arm is "named" only if forced with zero new assumptions; an arm is killed only at kill grade (a window forcing it false).

## Locus (byte-confirmed)

Row boundary sits inside the frame: @720=80 on row a5_01; @721=77, @722=03, @723=91, @724=65, @725=64, @726=11 on row a5_02.

Full window @712–@732:
`12 63 00 66 86 01 02 21 | 80 77 03 91 65 64 11 | 00 86 48 88 11 24 …`
(`@714=00`="pour" A9; `@725=64`="qui" granted; `@726=11`="la" GT; `@724=65` noun-class per R20-047.)

"77 03" is a **stream hapax** (1/1,847). n(77)=44; 77's top followers are 78×7, 84×7, 86×5, 81×4, 76×3 — the follower distribution does not discriminate determiner-77 from clitic-77 at this locus.

## Clause results

- **Arm A — nominal-03 ("le [03-noun]"): NOT FORCED.** Requires 77 as determiner (provisional, compatible) AND 03 nominal at this locus. 03's class is open at battery grade (R20 deferred the 03/71 §7 split; `val-03-noun` and `val-03-value-census` are queued, undecided). Assigning nominal class to 03 here is a new assumption. No standing value forces 03 non-nominal either — the arm is **not kill-grade contradicted**, merely unforced.
- **Arm B — nominalized infinitive ("le [03-inf]"):** NOT FORCED. Requires 03 infinitive-shaped at @722. 03's genuine infinitive legs are the "03 29"=Xer windows (@1030/@1320/@1594); none transfers here (no 29 present; @723=91). Importing the infinitive value to this locus is a new assumption. Not kill-grade contradicted (a nominalized infinitive need not expose an "er" pair in the cipher).
- **Arm C — word-boundary rival: NOT FORCED.** Sub-variants: (C1) 77 = clitic "le" + 03 begins a following word — requires 03's class, a new assumption; (C2) "le[03]" one word with 03 word-internal — requires 03's letter content, a new assumption. Not kill-grade contradicted.
- **C1: FAIL.** **C2: FIRES — all three arms fenced at the locus (@721–@722).**

## Verdict: NULL (fence executed)

No arm is forced by standing values with zero new assumptions; no arm is killed at kill grade. The fence is locus-scoped: it says nothing about 03's class/value elsewhere, about 77's determiner/clitic status stream-wide, or about the queued 03 batteries (`val-03-noun`, `val-03-value-census`). No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Adverses answered: 77="le" provisional is compatible with every arm (determiner for A/B, clitic for C1); 03's openness is the stated reason the bar's name-arm fails, not an ignored gap.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-77-722-det` (P3) — determiner-vs-clitic test for 77 at @721 (follower-class census across n(77)=44): determiner-shaped 77 keeps arms A/B alive and kills C1; clitic-shaped 77 forces C1.
2. `seg-77-03-wordinternal` (P3) — test the "le[03]" one-word arm once 03's letter content is named (consumes `val-03-value-census` / `val-03-noun` outcomes).
3. `frame-722-65-qui` (P4) — parse the right context "[03] [91] [65-N] qui la" (@722–@726) to bound 03's options from the right flank.

## Bookkeeping

- `battery-queue.json`: `seg-77-03-722` queued → verdict/null (temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated from disk; no downgrade).
- Lock `locks/seg-77-03-722.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
