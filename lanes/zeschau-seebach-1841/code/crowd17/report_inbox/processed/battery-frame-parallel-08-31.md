# Battery report: frame-parallel-08-31

- Target id: `frame-parallel-08-31`
- Claim: "sharpen the '24 ce <X>' / '<X> 24' frame census into a discriminating test"
- Date: 2026-10-09
- Worker: battery worker (subagent 7e2e3ca7-c0da-476a-a459-bd355705036f)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived and asserted in-session). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched. Lock `code/crowd17/next-token/locks/frame-parallel-08-31.lock` created on start (no stale lock), deleted on completion.
- Parent: `battery-prefix-08-31.md` (NULL, 2026-10-09) — "24 ce [08-31]" patterns with "24 ce est" (@823); "et [08-31] 24" patterns with "est 24" (@1496) — real frame parallels but not discriminating.

Terms (ASD-STE100): "composition" = 08 and 31 form one word ("08-31", a prefixed verb). "adjacency" = 08 and 31 are two separate words side by side ("08 | 31").

## Bar (verbatim, pre-registered before testing)

"resolve iff the frame census discriminates composition from adjacency with stated cause"

Numbered pass/fail clauses (restated before testing, not modified after):

- **C1:** the "24 ce <X>" and "<X> 24" frame censuses are complete and byte-exact on the repaired stream.
- **C2:** the census discriminates composition from adjacency with stated cause — i.e. [08-31] patterns with finite verbs across ≥3 independent frame families AND the separate-word reading's required 08-word has zero frame parallels.
- **C3:** resolve iff C2 passes; else record the parsimony argument as insufficient at battery grade (the bar's else-branch).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/frame-parallel-08-31.lock` on start; deleted on completion.
2. Re-derived the repaired stream byte-exact per `repair_parse.py` (1,847 pairs / 96 types asserted).
3. Census A: every "24 87 <X>" trigram (24-87 bigram, n=10). Census B: every "<X> 24" predecessor of 24 (n=57). Census C: followers of 67 (n=38) and of 17="fois" (n=15) for the third frame family. Census D: every "67 08", "08 24", "08 31", "24 87 08" window to test the separate-word 08-word's frame parallels.
4. Standing values held fixed per §7. Note on 24: 24="faire" was REJECTED at R18-008 (demoted to conditional lead); R17-009 stands (24 = finite verb, modal-shaped, class-level). The parallels below use 24's class, not a value.

## Window-level evidence (all byte-exact, 0-based @)

### Census A — "24 ce <X>" (n=10)

| @ | X | X+1 | gloss |
|---|---|-----|-------|
| 73 | 11 | 00 | 24 ce la pour |
| 162 | 11 | 24 | 24 ce la 24 |
| 179 | 64 | 23 | 24 ce qui [23] |
| 190 | 98 | 56 | 24 ce [98] [56] |
| 643 | 61 | 88 | 24 ce [61] [88] |
| 823 | 59 | 38 | 24 ce est [38] |
| 829 | 11 | 77 | 24 ce la le |
| 1486 | 08 | 31 | 24 ce 08 31 [92] |
| 1766 | 64 | 26 | 24 ce qui [26] |
| 1774 | 64 | 59 | 24 ce qui est |

Follower set X = {11 x3, 64 x3, 98 x1, 61 x1, 59 x1, 08 x1} — matches the parent's set exactly. The slot after "24 ce" holds exactly **one group** in all 10 windows. 59="est" (provisional finite verb) occupies the slot at @823.

### Census B — "<X> 24" predecessors (n=57)

Full distribution: 11 x4, 01 x3, 13 x3, 84 x3, 46 x3, 14 x2, 94 x2, 16 x2, 49 x2, 86 x2, 02 x2, 88 x2, and 22 singletons (34, 66, 08, 43, 20, 69, 24, 48, 19, 03, 89, 07, 61, 15, 39, 59, 31, 29, 98, 26, 09, 83).

Relevant windows:
- @1497 (a7_11): `66 15 59 24 89` = "15 est(prov) 24 89" — single finite verb 59 directly before 24.
- @1522 (a7_11): `67 08 31 24 11` = "et [08-31] 24 11" (composition) or "et 08 | 31 24 11" (adjacency).
- @534 (a3_01): `26 32 16 08 24 82` — standalone 08 directly before 24 (08's successor is 24, not 31).

### Census C — third frame family

- "67 _" followers (n=38): 33 x6, 77 x6, 78 x4, 11 x4, 86 x3, 64 x2, 76 x2, 46 x2, **08 x2**, 93/14/63/91/16/96/98 x1. @1519 (a7_11): `31 11 91 67 08 31` = "et 08 31". @630 (a4_01): `29 87 78 67 08 52 67 63` = "et 08 52" — 08 NOT followed by 31. 67="et" at @630 (follower 08 is not infinitive-shaped, so the §7 positional rule gives "et", not "veut").
- "17 _" followers (n=15): 77 x3, 11 x2, 64/46/06/86/98/08/61/84/01/78 x1. @880 (a5_08): `86 78 17 08 31 79` = "fois 08 31 tout". "17 08" occurs only here (always +31).

### Census D — the separate-word 08-word's parallels

- "08 31": exactly 3x stream-wide (@881, @1488, @1520).
- "24 87 08": exactly 1x (@1486), always followed by 31.
- "67 08": 2x — @1519 (followed by 31, the locus) and **@630 ("67 08 52", 08 standalone)**.
- "08 24": 1x — **@534 ("08 24", 08 standalone before verb-class 24)**.

## Per-clause pass/fail

- **C1: PASS.** All four censuses complete and byte-exact; the parent's X set reproduced exactly.
- **C2: FAIL — the conjunction is not met.**
  - Pro-composition leg (stated): the "24 ce" slot is single-group in 9/10 windows; composition keeps it single-word in 10/10 ("24 ce [08-31]"), while adjacency forces a two-word slot ("24 ce 08 | 31") unattested anywhere else in the family. [08-31] also patterns with finite "est" in two families: "24 ce _" (@1486 vs @823 "24 ce est") and "_ 24" (@1522 vs @1497 "15 est 24").
  - Conjunction-breaker (stated): the bar requires the separate-word reading's 08-word to have **zero** frame parallels. It has two: **@630 "et 08 52"** (standalone 08 in the "et _" frame, not composing with 31) and **@534 "08 24"** (standalone 08 in pre-verbal position before verb-class 24). Caveat on @630: if "08 52" composed, @630 would instead attest 08-prefix productivity (follow-up 1's venue) — either way it breaks the "08 composes only with 31" exclusivity the bar's (b)-condition needs.
  - Net: the discrimination is parsimony-grade (composition is the tidier parse), not battery-grade. The separate-word reading's 08-word is independently attested in verb-adjacent frames.
- **C3: does not fire → verdict NULL.** Per the bar's else-branch, the parsimony argument is recorded as **insufficient at battery grade**.

## Verdict: NULL

No standing or red-team verdict contradicted or downgraded; §7 intact (no polyvalence declared; 67="et" at @630/@1519 follows the positional rule). Canonical-stream caveat stands (rows a7_10/a7_11 offsets unvalidated).

## Follow-ups proposed (nulls regenerate work; all verified absent from battery-queue.json)

1. `standalone-08-wordrole` (P3) — census the 15 non-31 08-windows for a consistent standalone word role for 08 (word-initial attestations @630/@975/@534 vs letter-role @60/@944); lands the separate-word reading's 08-word iff a consistent role emerges, kills it iff 08 is only ever prefixal or sub-lexical outside 08-31.
2. `slot24ce-geometry` (P4) — test the "24 ce" single-slot geometry across the full 10-window family: does any window besides @1486 put two words in the post-"24 ce" slot under standing values? Strengthens the composition leg iff the slot is strictly single-word; dissolves it iff a two-word slot is licensed elsewhere.
3. `val-52-630-frame` (P3) — name 52's class at @630 ("et 08 52"); a verb-shaped 52 gives the standalone 08 a verb-adjacent word frame ("et 08 [52-V]"), directly testing the separate-word reading's 08-word; a non-verbal 52 re-opens 08-52 composition (prefix-productivity venue).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-frame-parallel-08-31.md` (this file).
- Queue: `frame-parallel-08-31` queued → verdict/null via temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated post-write.
- Lock `frame-parallel-08-31.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
