# Battery report — seg-528294-word

- Target: `seg-528294-word` (priority 3)
- Claim: test "52 82 94" as word-internal composition ("[52]mne...")
- Worker: 41fb5259-6226-439b-8ba4-afb0d66e1017
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`). `canonical.py` not used. R5005 not touched.
- Lock: `code/crowd17/next-token/locks/seg-528294-word.lock` created 2026-10-09T09:45:55Z. No stale lock pre-existed.
- Parent: battery-frame-76-94-trigram (NULL, 2026-10-09).

## Bar (verbatim, frozen before testing)

> promote-word-unit iff a French "mne"-medial word is enumerated that fits 52's other windows with <=1 new assumption; kill the word-unit iff no such word fits

Numbered pass/fail clauses:

1. (C1) A French word containing the consecutive letter trigram "mne" is enumerated such that segment 52 maps to the letter immediately preceding "mne" (word = "[52]mne...").
2. (C2) The enumerated word fits 52's other windows (all 24 non-trigram windows) with at most 1 new assumption beyond standing banked/promoted/provisional values.
3. (C3) Kill grade: no such word fits — i.e., every candidate is forced false by a window under standing values, or a cleaner rival value is demonstrated on the same frames.

Adverses (from queue): (A1) word-internal composition vs non-negator 94 is a polyvalence question = red-team venue; parent fence does not adjudicate 94 at these windows. (A2) 52's class/value open.

## Method

1. Verified the trigram "52 82 94" in the repaired stream: byte-identical at pair-indices @649 (row a4_02), @1100 (row a6_06), @1574 (row a8_01). Note: the target evidence cites @651/@1102/@1576 — a consistent +2 shift; the trigram and rows check out, so this is an indexing discrepancy in the evidence, not a data problem.
2. Enumerated French words containing consecutive "mne" from lexicon knowledge (frozen before window testing):
   - Word-initial "[52]mne...": "amnestie" (period spelling variant of "amnistie", current in 1841), "amnestier" (verb). X = "a".
   - Word-medial "...X+mne...": "automne" (X="o", onset "aut"), "hymne" (X="y", onset "h"), "damner"/"condamner"/"redamner" (X="a", onsets "d"/"cond"/"red"), "indemne" (X="e", onset "ind").
   - Excluded: "amnésie/amnésique" (m-n-é, not m-n-e), "amène/emmène/ramène" (m-è-n-e), "calomnie/insomnie/somnambule/somnifère/gymnase/amnistie" (m-n-i or m-n-a), "emmener/promener/aménager" (no "mn").
3. Applied the ≤1-new-assumption budget: all word-medial candidates require the three trigram windows' distinct left neighbors (78 @649, 86 @1100, 28 @1574) to each encode the word onset ("aut"/"h"/"d"/"cond"/"ind") — 3+ new assumptions, over budget, none granted. Only the word-initial candidate "amnestie"/"amnestier" (X="a") needs zero left-context assumptions (word boundary before 52) and exactly 1 new assumption total: 52="a".
4. Tested 52="a" against all 24 other 52-windows using standing values only (banked: 82=m, 34=i, 46=que, 11=la, 70=pre; promoted: 87=ce, 64=qui, 84=on, 47=ce; provisional: 77=le, 59=est; holds: 45=ce, frames 37/32 predicative, 80/89 verb-frames, 85 verb-stem; 94="ne" strong lead used only outside the fenced trigram windows).

## Window-level evidence (@-offsets, pair index / row / context)

52 occurs 27x. Non-trigram windows with standing-value reads under 52="a":

- @160 a1_04 | 35 93 [52] 94 24 — "93 à ne 24": "à ne pas"-type construction ("à ne 24"). PASS.
- @264 a2_02 | 45 93 [52] 33 42 — 45=ce: "ce 93 a 33"; no forced reading, no contradiction. PASS (neutral).
- @284 a2_03 | 42 48 [52] 89 28 — no standing neighbors. PASS (neutral).
- @383 a2_07 | 82 16 [52] 38 37 — 82=m; no forced reading. PASS (neutral).
- @482 a2_11 | 00 13 [52] 30 01 — 00=pour: "pour 13 a 30" ("pour <n.> a <v.>") plausible. PASS.
- @571 a3_02 | 45 94 [52] 87 78 — 45=ce, 94=ne, 87=ce: "ce ne a ce 78" reads as "ce n'a ce"+78, i.e. "ce n'a cessé"-shaped. PASS (supportive).
- @632 a4_01 | 67 08 [52] 67 63 — 67 polyvalent; no forced reading. PASS (neutral).
- @1007 a6_02 | 91 11 [52] 35 18 — 11=la: "91 la a 35" ("la a..." / "l'a..."). PASS.
- @1081 a6_05 | 64 06 [52] 89 24 — 64=qui: "qui 06 a 89". PASS (neutral).
- @1124 a6_07 | 06 11 [52] 37 43 — 11=la, 37=predicative frame: "06 la a 37". PASS.
- @1129 a6_07 | 00 86 [52] 37 86 — 00=pour, 37=pred frame. PASS (neutral).
- @1294 a7_03 | 35 94 [52] 80 04 — 94=ne, 80=verb-frame: "35 n'a 80" ("n'a"+verb frame). PASS (supportive).
- @1308 a7_04 | 77 74 [52] 30 92 — 77=le (prov): "le 74 a 30" ("le <n.> a <v.>"). PASS.
- @1332 a7_05 | 94 70 [52] 39 83 — 94=ne, 70=pre: "ne pre"+"a" = "ne préa..." ("préalable"/"préavis"/"préambule"). PASS (strongly supportive).
- @1342 a7_05 | 65 64 [52] 38 47 — 64=qui, 47=ce: "qui a 38 ce" ("qui a <v.> ce"). PASS (supportive).
- @1356 a7_05 | 82 06 [52] 37 64 — 82=m, 37=pred frame, 64=qui: "m 06 a 37 qui" ("a 37" = "a été"-shaped). PASS.
- @1385 a7_06 | 65 68 [52] 82 16 — 82=m: "68 a"+"m" = "68 am 16" ("am..." onset: ami/amour/amener). PASS (supportive).
- @1409 a7_07 | 95 46 [52] 42 16 — 46=que: "que a 42" ("que a <v.>"). PASS.
- @1416 a7_08 | 74 34 [52] 32 84 — 34=i, 32=pred frame, 84=on: "74 ia 32 on" ("ia" internal as in "diable"/"piano"/"fiacre"). PASS (neutral).
- @1435 a7_08 | 49 64 [52] 82 16 — 64=qui, 82=m: "qui am 16" ("am..." onset). PASS (supportive).
- @1441 a7_08 | 85 01 [52] 68 59 — 85=verb-stem, 59=est (prov). PASS (neutral).
- @1722 a8_07 | 06 11 [52] 37 43 — same shape as @1124: "06 la a 37". PASS.
- @1738 a8_07 | 12 48 [52] 86 12 — no standing neighbors. PASS (neutral).
- @1807 a8_10 | 35 94 [52] 80 04 — same shape as @1294: "35 n'a 80". PASS (supportive).

Trigram windows (word-unit): @649 a4_02 "77 78 [52] 82 94" = "... a"+"m"+"ne" = "amne..." ("amnestie"/"amnestier"); @1100 a6_06 "67 86 [52] 82 94"; @1574 a8_01 "32 28 [52] 82 94". All three byte-identical.

Distributional: 52 occurs 27x, in the same band as other short segments (47=ce 28x, 59=est 27x, 45=ce 22x, 40=e 21x, 82=m 39x) — consistent with a single-letter segment; no frequency rejection.

Rival check: no cleaner rival demonstrated on these frames. X="o"/"y"/"e" medial candidates all exceed the assumption budget (see Method §3).

## Per-clause verdicts

- C1: PASS — "amnestie" (period spelling of "amnistie", attested 1841) / "amnestier" enumerated; "[52]mne..." = "a"+"m"+"ne".
- C2: PASS — 52="a" is the single new assumption; all 24 other windows fit under standing values (zero forced contradictions; positive fits at @1332 "préa...", @1342 "qui a", @1385/@1435 "am", @1294/@1807 "n'a"+verb-frame, @571 "ce n'a ce...").
- C3: not triggered — a fitting word exists; kill grade not met.

## Adverses

- A1 (94 polyvalence at these windows): FENCED with stated cause — per §7 and the task brief, whether 94 is the negator "ne" or the letters "ne" inside "amnestie" at @649/@1100/@1574 is red-team venue. This report does not adjudicate it; the word-unit result is conditional on the red team's 94 ruling. Fencing = answered per §4.
- A2 (52's class/value open): ANSWERED — 52="a", single-letter class, frequency-consistent (27x).

## Verdict: PROMOTE (word-unit only)

The word-unit "52 82 94" = "a"+"m"+"ne" ("amnestie"/"amnestier") passes every bar clause with exactly 1 new assumption (52="a"). Promotion is scoped: it ratifies the word-unit composition only. The 94-status question at these windows is fenced for the red team; if the red team rules 94 a negator here, this promotion is conditional on re-read (escalation noted, not an overwrite — no standing red-team verdict is contradicted).

Null follow-ups: none required (verdict is promote, not null).
