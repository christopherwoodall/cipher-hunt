# Battery verdict: subj-88-730

- Target: `subj-88-730` (battery-queue.json, priority 3, status queued)
- Claim: "census all 23 88-windows for overt subjects licensing finite-88"
- Evidence: fin-88-730-rerun NULL 2026-10-09 follow-up #3
- Date: 2026-10-09
- Worker: subagent session 102a5dfb (parent: next-token battery dispatch)
- Note: a previous worker died mid-run (daemon restart); no report or queue changes existed — this is a clean re-dispatch, not a duplicate.
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched. All @-offsets are 0-based pair indices.

## Bar (verbatim, from battery-queue.json)

"name >=1 window with a battery-grade overt subject, else fence the finite-88 arm stream-wide (supplies C2's missing subject)"

Numbered pass/fail clauses (pre-registered before testing, not modified after):

1. **C1 (name arm):** ≥1 window has a battery-grade overt subject licensing finite-88 (subject cell valued at standing, in canonical preverbal subject position relative to verb-class 88, zero new assumptions) → promote.
2. **C2 (fence arm):** no such window exists → fence the finite-88 arm stream-wide.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/subj-88-730.lock` on start (2026-10-09T16:49:30Z); deleted on completion.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py`. n(88)=23 confirmed.
3. Adopted, never re-litigated (protocol §7): pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout A5, 00=pour A9, 84=on A15, 47=ce A4); provisional (59=est, 77=le); frames (A1, A8, A3, A12, A7-L2); 88=verb-class (governor-88-value PROMOTE); 45=ce (A11 hold); 69 noun-class (R19-109 red-team grant); 65 noun-class (R20-047); 06=ent (battery-promoted); R24 (24=en iff follower=85, else finite/modal verb class); kills (62='il' killed at kill grade per R19-106/R20-125; 84='fait' superseded); 67 et/veut sole polyvalence.
4. Graded each 88-window: a window licenses finite-88 only if an overt subject cell with a standing value sits in a licensed subject position and no kill-grade contradiction forces 88 non-finite. Windows kill-grading finite-88 (adjacent finite verbs, bound-syllable hosts, word-internal 88) are recorded as non-licensing, not as arm kills.

## Window-level evidence (all 23, ±4 context)

| @ | row | pre-4..-1 | post 1..4 | subject test |
|---|---|---|---|---|
| 42 | a1_01 | 64 41 01 24 | 43 81 30 62 | 24 finite/modal (follower 43≠85) is the qui-clause verb; 88 after a finite verb → finite-88 ungrammatical. No. |
| 86 | a1_02 | 62 16 14 06 | 77 66 98 19 | Left 06='ent' syllable; 62's cell killed, 16/14 open. No standing subject. No. |
| 210 | a2_00 | 06 77 44 50 | 19 74 77 78 | Left 50 open. No. |
| 304 | a2_04 | 86 91 18 89 | 02 88 20 17 | Left 89 (verb-frame A8), not a subject. No. |
| 306 | a2_04 | 18 89 88 02 | 20 17 46 84 | Left 02 open. No. |
| 334 | a2_05 | 92 50 45 54 | 40 03 64 31 | 45='ce' at −2; 'ce [54] [88]' needs 54's value (open). No. |
| **402** | a2_08 | 48 06 11 45 | 53 34 69 26 | **45='ce' (A11) directly preverbal to 88 — 'ce [88]' = 'c'est'-shaped. Battery-grade overt subject.** |
| 497 | a2_11 | 42 94 02 79 | 47 11 29 40 | 'tout [88]' — tout-88-frame battery: '*tout veut' ungrammatical; finite-88 killed at this window. No. |
| 513 | a3_00 | 94 64 98 65 | 56 87 77 80 | 'qui vient [65-N]': 65 is the postposed subject of vient (98 lead); cannot double as 88's subject without a new clause-boundary assumption. No. |
| 616 | a4_00 | 77 87 83 70 | 10 29 88 37 | Left 70='pre' bound GT syllable ('pre[88]' word-internal shape). No subject. No. |
| 619 | a4_01 | 70 88 10 29 | 37 76 82 14 | Left 29='er' GT letter. No. |
| 646 | a4_02 | 20 24 87 61 | 77 78 52 82 | Left 61 open; 'ce [61] [88]' needs 61's class (fin88-646-rerun NULL adopted). No. |
| 730 | a5_02 | 11 00 86 48 | 11 24 85 93 | fin-88-730-rerun NULL adopted: no licensed subject (65 can't reach, qui fails on clitic placement, pro-drop unlicensed). No. |
| 765 | a5_09 | 62 94 59 39 | 66 98 80 10 | 'ne est [39] [88]': 39 class-open; no overt subject for 88. No. |
| 904 | a5_09 | 16 92 67 16 | 18 55 83 54 | Left 16 open. No. |
| 1049 | a6_04 | 67 76 85 41 | 29 40 29 74 | seg-88er-1049 PROMOTE: '[88]ere' one word — 88 is word-internal (finite present-tense shape), not a standalone finite cell. Out of scope for cell-level subject. No. |
| 1117 | a6_07 | 38 30 69 11 | 70 12 06 14 | Left 11='la' GT: 'la [88]' can't be subject-verb ('la' article needs a noun; object pronoun needs preverbal host). No. |
| **1260** | a7_02 | 61 31 29 69 | 01 09 11 50 | **69 noun-class (R19-109 grant) directly preverbal to 88 — '[69-N] [88-fin]'. Zero new assumptions.** |
| 1267 | a7_02 | 11 50 46 69 | 24 30 20 64 | '[88] [24-fin]' (24 follower 30≠85 → finite/modal): adjacent finite verbs → finite-88 kill-grade excluded. No. |
| 1514 | a7_11 | 61 59 39 81 | 11 31 11 91 | Left 81 open. No. |
| 1541 | a8_00 | 06 21 62 93 | 77 78 43 00 | Left 93 verb-class: adjacent verbs ungrammatical for finite-88. No. |
| 1706 | a8_06 | 30 20 62 94 | 26 12 06 29 | 'ne [88]' — subject would precede 'ne'; 62's cell killed (R20-125), 20 cell-less, 30 conditional. No standing subject. No. |
| 1727 | a8_07 | 37 43 98 39 | 24 30 15 01 | '[88] [24-fin]' adjacent → finite-88 kill-grade excluded. No. |

## The two legs

**Leg 1 — @402 (row a2_08):** `[401]45 [402]88` = 'ce [88]'. 45='ce' is A11 (hold, standing). 'Ce' is the subject pronoun; directly preverbal to verb-class 88 gives the canonical 'c'est' construction. Zero new assumptions for the subject itself. Noted strain: the upstream contact '11 45' ('la ce') is ungrammatical under all standing readings — recorded as a fenced residual at the left contact; it does not touch the 'ce [88]' subject-verb pair (a clause may open at 45). No kill-grade contradiction forces 88 non-finite at this window.

**Leg 2 — @1260 (row a7_02):** `[1259]69 [1260]88` = '[69-N] [88]'. 69 is noun-class by red-team GRANT (R19-109). A nominal directly preverbal to a verb-class cell is canonical subject position. Followers 01/09/11/50 present no kill-grade contradiction. Zero new assumptions.

Both legs are independent (different rows, different subject cells, different values).

## Per-clause pass/fail

- **C1 PASS:** two windows (@402, @1260) carry battery-grade overt subjects licensing finite-88. The bar's ≥1 threshold is met twice over.
- **C2 does not fire.**

## Verdict: PROMOTE

The finite-88 arm is NOT fenced stream-wide: finite-88 is licensed at @402 ('ce [88]') and @1260 ('[69-N] [88]') with battery-grade overt subjects.

## Scope

- Names overt subjects for finite-88 at @402 and @1260 only. Does NOT name 88's value, does NOT decide 88's finiteness at @730 (fin-88-730-rerun's C2 stays moot — the subject found here is not at @730), and does NOT claim a uniform finite-88 (windows @497, @1049, @1117, @1267, @1541, @1727, @42 kill-grade or structurally exclude finite-88; 88's non-uniformity per tout-88-frame is untouched).
- This is the subject the parent's C2 was missing — supplied at battery grade, at other windows.

## Adverses

None listed. No standing/red-team verdict contradicted or downgraded (R19-109, R20-047, A11, R24, governor-88-value, tout-88-frame, seg-88er-1049, fin-88-730-rerun all adopted as premises). §7 intact — no polyvalence declared, no value named. Canonical-stream caveat stands (rows a2_08/a7_02 offsets unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-subj-88-730.md` (this file).
- Queue: `subj-88-730` queued → verdict/promote, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- Lock `locks/subj-88-730.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
