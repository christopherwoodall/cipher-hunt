# Battery report: standalone-08-wordrole

- Target id: `standalone-08-wordrole`
- Claim: "census the 15 non-31 08-windows for a consistent standalone word role (word-initial attestations @630/@975/@534 vs letter-role @60/@944)"
- Date: 2026-10-09
- Worker: battery worker (subagent a1db36c8-b37e-4d7e-8260-e2e4aa0cad9b)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived and asserted in-session). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched. Lock `code/crowd17/next-token/locks/standalone-08-wordrole.lock` created on start (no stale lock), deleted on completion.
- Parent: `battery-frame-parallel-08-31.md` (NULL, 2026-10-09) — follow-up 1. Note: the claim's "@630" is the parent's 1-based/off-by-one label for the 0-based @631 window (`67 08 52`); all offsets below are 0-based.

Terms (ASD-STE100): "standalone word" = 08 aligns with a word boundary on both sides (a lexical item of its own). "prefixal" = 08 attaches to the following group as word-initial letter t-. "sub-lexical" = 08 is a letter inside or at the edge of a word (medial -t-, final -t).

## Bar (verbatim, pre-registered before testing)

"land the separate-word reading iff a consistent role emerges; kill it iff 08 is only ever prefixal/sub-lexical outside 08-31"

Numbered pass/fail clauses (restated before testing, not modified after):

- **K1 (land clause):** a consistent standalone word role for 08 emerges across the 15 non-31 windows — i.e. the windows share a distributional signature (constrained predecessor/successor classes) and at least one window forces, or positively supports, the word parse.
- **K2 (kill clause):** 08 is only ever prefixal/sub-lexical outside 08-31 — i.e. every one of the 15 non-31 windows parses as the letter t (prefixal t-, medial -t-, or final -t) under standing values, and no window licenses a standalone word.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/standalone-08-wordrole.lock` on start; deleted on completion.
2. Re-derived the repaired stream byte-exact per `repair_parse.py` (1,847 pairs / 96 types asserted in-session).
3. Enumerated every 08 window: 18 total — 3 followed by 31 (@881, @1488, @1520), 15 non-31. Census table saved to `code/crowd17/next-token/standalone-08-wordrole_census.json`.
4. Classified each non-31 window under standing §7 values (pencil banked: 40=e, 34=i, 29=er; holds: 45="ce" A11, 47="ce" A4; frames: 85 verb-stem A3, 80 verb-frame A8, 37/32/42 predicative A1; battery: 08=t x3, 01="en", 52 split-shaped with sub-lexical tier, 67="et" positional rule, 24 finite-verb class R17-009).

## Window-level evidence (all byte-exact, 0-based @)

| @ | row | context (pred 08 succ) | letter parse of 08 | anchor |
|---|---|---|---|---|
| 35 | a1_01 | 01 [08] 91 | 01-08 = "en"+t = "ent" letter string; 08 medial | 01="en" battery; 08=t x3 battery |
| 60 | a1_01 | 41 [08] 34 29 | 08-34-29 = t-i-er = "-tier", word-medial | 34=i, 29=er PENCIL (§7) |
| 98 | a1_02 | 85 [08] 21 | 85-08 = verb-stem + -t (3sg -t ending) | 85 verb-stem A3 (§7) |
| 198 | a2_00 | 60 [08] 67 | "60t" word-final t + 67="et" | 67 et/veut positional rule (§7) |
| 534 | a3_01 | 16 [08] 24 | "16t"+verb(24) or "16"+"t24"; 08 a letter either way | 24 finite-verb class R17-009 |
| 631 | a4_01 | 67 [08] 52 | "et"+"t52"+"et"; 08 word-initial LETTER, not word | 67="et" positional; 52 sub-lexical tier (val-52-630-frame) |
| 779 | a5_04 | 37 [08] 29 | 37-08-29 = "37ter", word-final -ter | 29=er PENCIL (§7) |
| 922 | a5_09 | 40 [08] 65 | 40-08 = "et", word-final t | 40=e PENCIL (§7) |
| 944 | a5_10 | 40 [08] 62 | 40-08 = "et", word-final t | 40=e PENCIL (§7) |
| 975 | a6_01 | 45 [08] 01 | 45-08 = "cet", word-final t ("cet 01 pour") | 45="ce" HOLD A11 (§7); 00="pour" A9 |
| 1302 | a7_03 | 37 [08] 43 | "37t43" letter string | 37 predicative A1 (§7) |
| 1323 | a7_04 | 80 [08] 62 | 80-08 = verb-frame + t | 80 verb-frame A8 (§7) |
| 1339 | a7_05 | 60 [08] 65 | "60t65" letter string | — (letter parse licensed by 08=t) |
| 1592 | a8_02 | 47 [08] 81 | 47-08 = "cet", word-final t | 47="ce" A4 (§7) |
| 1610 | a8_03 | 23 [08] 55 | "23t55" letter string | 23~26 split hold (§7) |

The three 08-31 windows (@881 "fois t31 tout", @1488 "24 ce t31", @1520 "et t31 24") are excluded from the bar by its own terms; all three are consistent with t-initial strings and were not re-tested.

Distributional signature of the 15: 13 distinct successors {01,21,24,29,34,43,52,55,62,65,67,81,91} and 12 distinct predecessors {01,16,23,37,40,41,45,47,60,67,80,85} — letter-grade productivity, no selectional signature of any word class.

## Per-clause pass/fail

- **K1 (land): FAIL.** No consistent standalone word role emerges.
  - The three "word-initial" candidates sit in three unrelated frames — @534 pre-verbal ("16 _ 24"), @631 post-"et" ("et _ 52"), @975 post-"cet" ("cet _ 01") — and each resolves as a letter: @975 is positively the final t of "cet" (45="ce" hold), @631 is a t-initial letter string (52 has a battery-verified sub-lexical tier), @534 is "16t"+verb or "16"+"t24".
  - 6 windows are positively anchored as letter-t by pencil/standing values with zero word-parse alternative: @60 ("-tier": 34=i, 29=er), @922/@944 ("et": 40=e), @975/@1592 ("cet": 45/47="ce"), @779 ("-ter": 29=er), @98 (verb-stem 85 + -t, A3).
  - The word parse in every window requires a French word "t". No such word exists; the elided-pronoun "t'" (= "te") reading is the already-killed 08-particle hypothesis (val-08-successor-class).
  - Zero windows force or positively support the standalone-word reading.
- **K2 (kill): PASS.** 08 is only ever prefixal/sub-lexical outside 08-31.
  - All 15 windows parse as the letter t: word-final -t (@922, @944 "et"; @975, @1592 "cet"; @98 verb+-t; @198 "60t"; @534 "16t"), word-medial -t- (@60 "-tier"; @779 "-ter"; @35 "ent"), word-initial t- (@631 "t52"; @1302 "t43"; @1323 "t62"; @1339 "t65"; @1610 "t55").
  - The distributional signature (13 distinct successors / 15 windows, 12 distinct predecessors) matches a letter's free combination, not a word's constrained distribution — and it is the LETTER role that is consistent across all 15 windows, which is exactly what the kill branch describes.

## Verdict: KILL

The separate-word reading of 08 is killed at battery grade: outside the three 08-31 windows, 08 is only ever the prefixal/sub-lexical letter t. This corroborates and extends the battery 08=t verdicts (val-08-successor-class, syllable-08-letter-value) to a window-complete census; it names no value, changes no registry entry, and contradicts no standing or red-team verdict (§7 intact; 67="et" readings follow the positional rule).

## Scope

- Tested: all 18 08-windows on the repaired 1,847-pair stream; the 15 non-31 windows individually.
- Not tested (out of scope): the value of 31 or of any neighbor group; the 08-31 composition question (parent's venue); any red-team docket item.
- Canonical-stream caveat stands (68 of 70 upstream row offsets unvalidated); pencil gloss rows a5_03/a8_05 validated per repair_parse.py asserts.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-standalone-08-wordrole.md` (this file).
- Census data: `code/crowd17/next-token/standalone-08-wordrole_census.json`.
- Queue: `standalone-08-wordrole` queued → verdict/kill via temp-file + rename, own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated post-write.
- Lock `code/crowd17/next-token/locks/standalone-08-wordrole.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
