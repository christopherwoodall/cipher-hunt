# Battery report: seg-86-52-37-86 (NULL — no arm parses the full clause)

**Target:** `seg-86-52-37-86` (P3)
**Date:** 2026-10-09
**Verdict:** NULL (fence — all three word-internal arms blocked at battery grade)

## Bar (verbatim from battery-queue.json)

"adjudicate using 86's resolved value(s) and 86-52 x2 (@1099/@1128); decide iff one segmentation parses the full clause '…43 pour 86 52 37 86 24 77 86…' grammatically"

## Bar restated as numbered clauses

1. Adjudicate using 86's resolved value(s) — 86's value status is stated (resolved or open).
2. Use the "86-52" x2 distributional evidence (@1099, @1128).
3. Decide (adopt one segmentation) IFF one of '86 [52-37] 86' / '[86-52] 37 86' / '86 52 [37-86]' parses the full clause "…43 pour 86 52 37 86 24 77 86…" grammatically.

## Adverses

- "86=INF class granted (A9) with determiner-life — both lives must be honored or fenced." Answered below.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/seg-86-52-37-86.lock` on start (agent id + UTC 2026-10-09T08:03:08Z), deleted on completion. Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. All @-offsets are 0-based on the repaired stream.

Target window (row a6_07), pair index : group:

- @1126: 43 | @1127: 00 (=pour, granted A9) | **@1128: 86 | @1129: 52 | @1130: 37 | @1131: 86** | @1132: 24 | @1133: 77 (=le, provisional) | @1134: 86

The claim's "@1129" is the 52 of the span @1128–1131 = "86 52 37 86" (matches the la-frame battery's "@1129 ('52 37 86')" locus).

Standing values consumed as premises (not re-litigated):
- 86 INF-class (A9, class-level); 86's determiner-life (86='le', subset-scoped, le-86-determiner-subset).
- @1128 = whole-infinitive ("pour [86-INF]"), inherited from stem-33-86's per-window adjudication via orphan86-1131-1147 (not re-litigated).
- @1131 = confirmed orphan, inherited from orphan86-1131-1147 (2026-10-08, KILL): no stated neighbor assumption yields a zero-contradiction whole-parse (infinitive L/R, substantivized-noun subject/complement, stem all failed).
- "52-37" adjective unit {même, seule, dite} (Type-A @1124/@1722; "telle" killed at kill grade, telle-52-37-rival); 52's value otherwise open (leftedge-52-86-1736 NULL).
- 37: 'le' fenced MEDIUM (S5, contradicted, red-team territory); 're' killed uniform (enterre-37re-s5, conditional on 77='le'); value otherwise open (frame-37-reexam, red team).
- 86="voi" (voir stem) fails globally (REPORT.md determiner/adjective block).

## Window-level evidence

**Clause 1 — 86's value status:** OPEN. 86="voi" fails globally; no standing value names 86. 86 is class-stated only (INF-class A9 + subset-scoped determiner-life). Clause 1 recorded as open, not resolved — the bar's "resolved value(s)" antecedent does not hold.

**Clause 2 — "86-52" x2:** confirmed byte-exact. @1099–1100 ("67 86 52 82", row a6_06) and @1128–1129 ("00 86 52 37", row a6_07). Neither locus names a word under standing values (86 open, 52 open). The @1128 locus is additionally constrained: @1128 is adjudicated whole-infinitive, so a "[86-52]" fusion there would contradict a standing battery adjudication (see arm B).

**Clause 3 — the three arms against the full clause:**

- **Arm A ('86 [52-37] 86'):** FAIL. Frame = "…43 pour [86] [52-37] [86] [24] [77] [86]…". The orphan battery already tested this shape at this window: "pour [inf] [52] [37] [inf]" as a double-infinitive frame is ungrammatical French (orphan86-1131-1147, attempt (a)), and @1131 is a confirmed orphan — no whole-parse exists, so it cannot stand as the second 86. Reading "52-37" as the adjective unit {même/seule/dite} does not repair this: the adjective needs a head it does not get, and the double-86 frame stays ungrammatical. No French parse under standing values.
- **Arm B ('[86-52] 37 86'):** BLOCKED at battery grade. "[86-52]" as one word makes @1128 a stem, contradicting the inherited stem-33-86 adjudication (@1128 = whole). A battery worker cannot overturn a standing battery adjudication. Independently, no French word is nameable for "86-52" under standing values (both values open). The "86-52" x2 distributional fact is noted but cannot be converted into a word without inventing values.
- **Arm C ('86 52 [37-86]'):** FAIL. "37-86" is a hapax contact (exactly 1/1,847, @1130–1131). No French word is nameable under standing values: 37='re' is killed uniform (enterre-37re-s5, conditional on provisional 77='le'); 37='le' + 86 is not a French word, and 37-as-determiner is S5/red-team territory; 86's value is open. The hapax has zero distributional support.

**Adverse — both 86 lives:** HONORED at @1128, FENCED at @1131. @1128's INF-life is honored ("pour [86-INF]", inherited whole-adjudication). @1131's INF-life and determiner-life are both fenced with stated cause: the orphan battery exhausted whole-parse attempts (infinitive governed L/R, substantivized noun as subject — fails for want of an article, which 37 cannot supply per S5's fence — noun complement, stem) and confirmed the orphan. Neither life is ignored.

## Per-clause pass/fail

1. 86's value status stated: **RECORDED (open).** No resolved value exists; the bar's "resolved value(s)" antecedent is not met.
2. "86-52" x2 used: **PASS.** Both loci confirmed byte-exact; neither yields a word under standing values.
3. One segmentation parses the full clause grammatically: **FAIL.** Arm A fails (double-86 frame ungrammatical; @1131 confirmed orphan). Arm B is blocked (contradicts @1128-whole). Arm C fails (hapax "37-86", no nameable word). No arm is adoptable.

## Verdict: NULL

The segmentation of @1128–1131 cannot be decided among the three arms at battery grade. All three word-internal arms are blocked with stated causes; the window is fenced as unparsed. No standing or red-team verdict contradicted or downgraded; §7 intact. Canonicality caveat stands (a6_07 offset 0, upstream offsets unvalidated).

## Follow-ups proposed (all verified absent from battery-queue.json)

1. `seg-1128-1131-revisit-37` (P3): re-test arms B and C once red-team frame-37-reexam decides 37's value. A decided 37 value (prefix or otherwise) makes "37-86" and the standalone-37 slot testable.
2. `seg-1128-1131-revisit-86` (P3): re-test all three arms once 86's value is named. Every arm is gated on 86's open value; the "86-52" x2 distributional question likewise needs it.
3. `w1128-1131-nonarm` (P4): test parses outside the three arms (all-standalone "86|52|37|86"; clause boundary after @1130), since all three word-internal arms are blocked at battery grade.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/seg-86-52-37-86.lock` created 2026-10-09T08:03:08Z, deleted on completion.
- `battery-queue.json`: `seg-86-52-37-86` queued → verdict/null (temp-file + rename; pre-write assert confirmed no prior verdict; JSON re-validated; only this entry touched).
- R5005, sealed gates, red-team adjudication queue untouched.
