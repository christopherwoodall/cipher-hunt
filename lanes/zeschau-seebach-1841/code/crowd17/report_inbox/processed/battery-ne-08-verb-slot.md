# Battery report: ne-08-verb-slot

- Target id: `ne-08-verb-slot`
- Claim: "converse template: 08's successor census vs 94's verb-slot successors (65 is the sole intersection: 08-65 x2, 94-65 x1)"
- Date: 2026-10-09
- Worker: battery worker (subagent 92078e2a-ab27-48d3-94c8-c6a49d5d6cd8)
- Stream: repaired 1,847-pair parse, re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`; asserts 1,847 pairs / 96 types held. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "successor" = the group immediately right of a window. "Verb-slot successors" = followers of 94 in windows where 94 is the verbal negator 'ne'. "Profile" = the multiset of successors with counts.

## Bar (verbatim, pre-registered before testing)

"resolve iff 08's successor profile matches 94's verb-slot successors with byte evidence; fence with stated cause if not"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 08's successor profile enumerated byte-exact (n=18).
2. **C2:** 94's verb-slot successor set enumerated from the standing PROMOTE `ne-94-right-context` (7 clean verbal-negator windows), adopted as premise, not re-litigated.
3. **C3 (resolve):** 08's profile matches 94's verb-slot successors — i.e. 08's followers concentrate on the same verb-shaped set that defines 94's negator frame, with byte evidence.
4. **C4 (fence):** else-arm — fence the 08/94 distributional comparison with stated cause.

Adverses: none listed.

## Method

1. Read BATTERY-PROTOCOL.md first. Lock `code/crowd17/next-token/locks/ne-08-verb-slot.lock` created on start, deleted on completion.
2. Re-derived the stream per `repair_parse.py` tokenization.
3. Full census of 08 (n=18) successors; full census of 94 (n=37) successors for cross-check.
4. 94's verb-slot set taken from `code/crowd17/report_inbox/processed/battery-ne-94-right-context.md` (PROMOTE, 2026-10-09): 7 clean verbal-negator windows:
   - @65 (a1_01): `40 94 92 69` — ne + verb-class 92
   - @161 (a1_05): `52 94 24 87` — ne + 24-fin/modal
   - @699 (a5_01): `28 94 60 12` — ne + 60-verb-class
   - @1549 (a8_00): `12 94 92 45` — ne + 92-verb
   - @1701 (a8_06): `33 94 30 20` — "ne pas", verbal-slot forcing
   - @1705 (a8_06): `62 94 88 26` — "il ne [88-V]"
   - @1773 (a8_09): `62 94 24 87` — "il ne [24]"
   → verb-slot successors: **{92×2, 24×2, 60×1, 30×1, 88×1}**.

## Window-level evidence (all byte-exact)

### 08's successor profile (n=18)

| @ | row | context (−2..+1) | successor |
|---|-----|------|---|
| 35 | a1_01 | 01 08 91 | 91 |
| 60 | a1_01 | 41 08 34 | 34 |
| 98 | a1_02 | 85 08 21 | 21 |
| 198 | a2_00 | 60 08 67 | 67 |
| 534 | a3_01 | 16 08 24 | 24 |
| 631 | a4_01 | 67 08 52 | 52 |
| 779 | a5_04 | 37 08 29 | 29 |
| 881 | a5_08 | 17 08 31 | 31 |
| 922 | a5_09 | 40 08 65 | 65 |
| 944 | a5_10 | 40 08 62 | 62 |
| 975 | a6_01 | 45 08 01 | 01 |
| 1302 | a7_03 | 37 08 43 | 43 |
| 1323 | a7_04 | 80 08 62 | 62 |
| 1339 | a7_05 | 60 08 65 | 65 |
| 1488 | a7_10 | 87 08 31 | 31 |
| 1520 | a7_11 | 67 08 31 | 31 |
| 1592 | a8_02 | 47 08 81 | 81 |
| 1610 | a8_03 | 23 08 55 | 55 |

Successor multiset: **{31:3, 62:2, 65:2, 01:1, 21:1, 24:1, 29:1, 34:1, 43:1, 52:1, 55:1, 67:1, 81:1, 91:1}** — 14 distinct followers over 18 windows.

### Comparison with 94's verb-slot successors

- 94 verb-slot (clean): {92×2, 24×2, 60×1, 30×1, 88×1}
- Intersection with 08's profile: **{24} only** — 08-24 ×1 (@534) vs 94-24 ×2 (@161, @1773).
- The claim's stated premise ("65 is the sole intersection") is wrong under the clean verb-slot reading: 65's only 94-window is @250 (`44 94 65 63` = "44 ne [65-noun]"), which `ne-94-right-context` explicitly classified as **non-negator** ("ne [noun]" ungrammatical as negator). The 94-65 window is not a verb-slot window at all.
- Under 94's full successor profile the 08/94 intersection is {24, 29, 52, 60, 65} — five singletons, no concentration.
- 94's conditional verb-slot windows (8: successors {59×2, 82×3, 02×1, 70×1}) add zero further overlap with 08's profile.

## Per-clause pass/fail

1. **C1: PASS** — 08's successor profile enumerated, n=18, byte-exact above.
2. **C2: PASS** — verb-slot set adopted from the standing PROMOTE (7 clean windows, successors {92×2, 24×2, 60×1, 30×1, 88×1}); not re-litigated per §5.
3. **C3 (resolve): DOES NOT FIRE — no match, at kill-adjacent strength:**
   - None of 94's four characteristic verb followers ({92, 88, 60, 30}) ever follows 08. The negator frame "ne [verb]" is 94's majority function; 08 reproduces none of its characteristic followers.
   - 08's three modal followers are hostile to a negator reading: 65 ×2 is noun-class (R18) — "ne [noun]" is ungrammatical (the same ungrammaticality that fences 94's own @250); 62 ×2 is the 'il'-shaped subject pronoun (cf. "62=il" at @1705) — "ne il" is ungrammatical in any period; 31 ×3 (n(31)=8, predecessors {08:3, 64:2, 11:1, 61:1, 48:1}) has no verb-frame contact in 08's windows.
   - 08's profile is 14 distinct followers over 18 windows (heterogeneous); 94's verb-slot profile is 5 verb-shaped followers over 7 windows (concentrated). No concentration, no shape match, no class match.
   - The sole shared singleton (24) also follows 12='n' (promoted) and is the stream's general finite/modal verb — it does not discriminate.
4. **C4 (fence): EXECUTED.** Stated cause: the distributional comparison was built on a misdescribed premise (94-65 is a non-negator window), and the actual byte evidence shows anti-correlated profiles — 08's followers are noun/pronoun-heavy and heterogeneous where 94's verb-slot followers are uniformly verb-shaped. This is consistent with (and hardens) the NULL of `ne-08-frames` (zero 'ne' legs via the pas-slot audit): the converse direction now also returns negative, at stronger evidence weight.

## Verdict: NULL (fence executed)

Per the bar's designed else-arm. Not kill-grade against 08 itself: 08's class remains open (stem-08-letter-probe PROMOTEd 08 word-internal at its three letter contacts — a word-internal 08 would also produce a heterogeneous successor profile, which is a live rival explanation and is not adjudicated here). No standing/red-team verdict contradicted or downgraded; §7 intact (no polyvalence declared); `ne-94-right-context`'s PROMOTE adopted as premise, untouched; canonical-stream caveat stands (rows a1_01/a7_10/a7_11 offsets unvalidated).

## Follow-ups proposed (nulls regenerate work)

1. `homophone-08-12-n` (P3) — compare 08's successor profile against 12='n' (promoted, n(12)=23, successors {48:5, 94:3, 16:3, 06:2, 41:2, 44:2, 33:1, 34:1, 61:1, 63:1, 66:1, 98:1}); if 08 matches 12's "n" profile better than 94's "ne" profile, the "n"-sibling hypothesis survives this battery's kill. Bar: resolve iff 08's profile matches 12's with byte evidence; fence otherwise.
2. `val-08-successor-class` (P3) — name the classes of 08's top followers {31, 62, 65, 21, 43}; tests whether 08 licenses a coherent frame class (word-internal vs particle) from the right.
3. `frame-08-65-noun` (P4) — test the "08 [65-noun]" ×2 windows (@922, @1339): if 08 is adjectival/adverbial before a noun, that fences the negator hypothesis independently at those windows.

## Bookkeeping

- Report: this file (`code/crowd17/report_inbox/battery-ne-08-verb-slot.md`).
- Queue: `ne-08-verb-slot` queued → `verdict`/`null`, 2026-10-09 (temp-file + rename; pre-write assert confirmed no prior verdict; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/ne-08-verb-slot.lock` created on start, deleted on completion.
- Follow-up ids `homophone-08-12-n`, `val-08-successor-class`, `frame-08-65-noun` all verified absent from `battery-queue.json` before writing this report.
