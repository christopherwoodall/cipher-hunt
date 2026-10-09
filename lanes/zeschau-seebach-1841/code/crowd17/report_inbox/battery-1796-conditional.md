# Battery report: 1796-conditional

- Target id: 1796-conditional
- Priority: 2
- Date: 2026-10-09
- Worker: e825f1c4-c31e-4470-93ff-f99aa694549c
- Lock: created 2026-10-09T20:24:58Z, no prior lock or verdict found

## Claim

@1796 is a valid 'n'est [37]' est-arm leg

## Bar (verbatim, from battery-queue.json)

(a) red team lifts S5 (this battery is BLOCKED until D2 is decided - do not run before); (b) successor-91 profile compatible with the predicative class (@316/@1210 successors); (c) no window contradicts

## Bar as numbered pass/fail clauses (pre-registered, unchanged)

1. The red team has lifted S5 on @1796 (gate; the battery must not run before this).
2. The successor-91 profile at @1796 is compatible with the predicative class (compare @316 and @1210 successors).
3. No window contradicts the claim.

## Method

- Read the red-team docket first. The bar's clause 1 is a gate. I checked whether the gate opened before any testing.
- Stream check used ONLY the repaired 1,847-pair stream: `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`. `canonical.py` was not used. R5005 was not touched.
- Red-team sources: `code/crowd10/redteam/RULINGS-ROUND10.md`, `code/crowd11/redteam/RULINGS-ROUND11.md`, `code/crowd12/redteam/RULINGS-ROUND12.md`, `code/crowd14/redteam/RULINGS-ROUND14.md`.

## Window-level evidence (@-offsets, repaired stream)

Window @1794 to @1799 = 42-94-59-37-91-79.

| Offset | Pair | Row |
|---|---|---|
| @1794 | 42 | a8_09 |
| @1795 | 94 | a8_09 |
| @1796 | 59 | a8_10 |
| @1797 | 37 | a8_10 |
| @1798 | 91 | a8_10 |
| @1799 | 79 | a8_10 |

Census of all 59-windows with pre in {64,94,93}: exactly 7.

1. @103 pre=93 suc=45 (row a1_03)
2. @316 pre=64 suc=32 (row a2_04)
3. @559 pre=94 suc=30 (row a3_02)
4. @763 pre=94 suc=39 (row a5_03)
5. @1210 pre=64 suc=32 (row a7_00)
6. @1777 pre=64 suc=19 (row a8_09)
7. @1796 pre=94 suc=37 (row a8_10)

The first six are the granted est-arm members. @1796 is the seventh. This matches the red team's verified datum byte-exactly.

## Red-team record on the gate

- R10: "@1796 (pre=94) correctly excluded as S5-fenced (verified: 7th pre in {64,94,93} window, suc=37)." The banked falsifier F3 reads: "none; @1796 'n'est le' is S5-fenced, fence stands." The S5-fenced set (@528, @624, @912, @1178, @1443, @1796) is "NOT re-litigated."
- R12 (newest ruling touching this, 2026-10-07): ISLET 10 HOLDS. S5 adverse 1 banked in full ("est le qui"=0/3.87M at @528/@1443 — fence-strengthening). S5 adverse 2 banked in CORRECTED form: "n'est le" = 8/10 idiom «si ce n'est le», with two real counterexamples ("tel n'est le cas"; "n'est le fils"), at reduced weight. R12 states it "is still an adverse for the S5 fence (the idiom is the dominant frame and @1796 lacks it)."
- R11 and R14: no mention of @1796 or S5. No later ruling lifts the fence.

## Per-clause pass/fail

1. FAIL — the gate is not open. The red team did not lift S5 on @1796. R10 fenced it (not re-litigated); R12 kept the fence and banked the adverses. The bar's own words say "do not run before." The bar is untestable as written.
2. NOT EVALUATED — clause 1 blocks testing.
3. NOT EVALUATED — clause 1 blocks testing.

## Adverses

- "classification.json 'n'est le era 10/3.96M' rarity note" — ANSWERED: R12 corrected it to 8/10 idiom + 2 counterexamples, banked at reduced weight. Not ignored.
- "round-10 R7(b) exclusion" — ANSWERED: R10 excluded @1796 as S5-fenced; the exclusion stands through R12. Not ignored.

## Verdict

**null** (protocol section 2: bar genuinely untestable as written — gate clause unmet; counts as a null, never a silent rewrite).

This is not a kill. No kill-grade test ran. The fence is the red team's ruling, not this battery's finding. This result does not contradict any red-team verdict; it agrees with it.

## Follow-ups (for the supervisor to queue)

### F1 — s5-adverse2-census (priority 2)

- Claim: "era census of the corrected S5 adverse 2: 'n'est le' = 8/10 idiom, 2 counterexamples — verify the count and frame each counterexample."
- Bars: (a) census «n'est le» tokens in the era corpus with frame classification (idiom «si ce n'est le» vs other); (b) exact frame of each non-idiom instance ("tel n'est le cas"; "n'est le fils" per R12); (c) compare each counterexample frame with @1794–@1799 (42-94-59-37-91-79); report match or no-match per case.
- Evidence: R12 banked adverse 2 in corrected 8/10 form at reduced weight. The idiom is the dominant frame but two counterexamples weaken it. @1796 lacks the idiom frame.
- Adverses: must not re-litigate the S5 fence; census only, descriptive result.

### F2 — 1796-conditional-r2 (priority 3, GATED)

- Claim: "@1796 is a valid 'n'est [37]' est-arm leg" (same claim as this battery).
- Bars: GATED — run ONLY after a red-team round supersedes R10/R12 and re-litigates S5. R10/R12 state "NOT re-litigated." Original bars (a)–(c) apply at dispatch time.
- Evidence: this null report; red-team R10/R12 (S5 fence stands).
- Adverses: same as 1796-conditional.

### F3 — est-arm-successor-census (priority 3)

- Claim: "descriptive census of 59-successors: is @1796's suc=37 anomalous against the predicative-class successor profile (@316/@1210 suc=32)?"
- Bars: (a) successor distribution of the six granted est-arm members vs @1796's suc=37; (b) full 27-window 59-successor census for context; (c) no value judgment on S5 — descriptive only, groundwork for any future re-litigation.
- Evidence: this battery verified 7 pre-in-{64,94,93} windows (@1796 is 7th, suc=37). Original bar (b) asked for successor-profile compatibility with the predicative class.
- Adverses: S5 fence stands — this census must not be read as a fence challenge.

## Anomaly

None. The lock file was absent (no stale lock). The queue entry was "queued" with no verdict. The red-team docket was consistent across R10–R14: the fence stands, not re-litigated. Stream verification matched the red team's verified datum exactly (7th window, suc=37).
