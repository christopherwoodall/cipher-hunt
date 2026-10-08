# Finder report — beat parvenir-thirds (wave 2)

Beat: parvenir-thirds — "'vient de me parvenir' thirds (60/62/68) homophone-set test + 83='de' cross-check."
Date: 2026-10-08. Stream: repaired 1,847-pair parse (repaired_offsets.json + data/upstream-ct_R5005.txt, parsed like repair_parse.py). R5005 untouched (read-only). No sealed gates, no adjudication queue touched.

## Headline findings

1. **The 3-cell homophone set is dead distributionally.** Successor-distribution permutation test on {60, 62, 68}: p < 0.0001 (B=20,000). The rejection is driven by 62: 62->94 x9 (26% of 62's tokens) vs 60->94 x0, 68->94 x0; 60->03 x4 vs 62->03 x0, 68->03 x0. This is consistent with (not a re-litigation of) the collision-62-84 kill: 62='il' is demonstrated on the nine 62-94 windows, and §7 allows 67 as the sole true polyvalence, so 62 cannot share a syllable value with 60/68.
2. **The {60, 68} pair is inconclusive, not excluded.** Pairwise successor p=0.0540, predecessor p=0.0560 (formula-bound tokens excluded). Not distinguishable at the {33,86} standard, but 68 n=7 free is thin and the p-values sit at the margin. This is the surviving homophone hypothesis: a 2-cell set, 62 split off.
3. **83='de' has two clean cross-checks and three adverses.** Clean: 83-86 x2 (@898, @1334) = "de [86-INF]" under the A9 INF-class grant. Adverses: "ce de" x2 (@614, @1171) and "qui de est" @911 — all ungrammatical under unconditioned 83='de'. The @614/@1171 pair admits a "cède"-verb rival reading (87-83 = "cède"), which fences the adverse without killing the lead.
4. **New replicated frame: "44-83-21-67-78" x2** (@1160, @1839, byte-identical 5-gram). Reads "[44-noun] de [21] [67] [78]" — the strongest independent 'de' context outside the formula, and it drags 21/67/78 into one testable frame.
5. **98 is not "vient"-shaped.** Doubled 98-98 x3 (@1073, @1145, @1660) resists any finite-verb reading; 98-82 x3 and 98-80 x3 have no clean "vient" parse. The formula's French head (98) stays unconfirmed — the standing adverse stands.

## Census tables (@-offsets, repaired stream)

### Formula windows (byte-identical 98-83-82-96-21-[third], x3)

| @ | third | follower | row |
|---|---|---|---|
| 227 | 60 | 71 | a2_01 |
| 1060 | 62 | 18 | a6_04 |
| 1783 | 68 | 47 | a8_09 |

96-21 occurs nowhere else globally (x3, all formula-bound) — confirmed. 98-83 occurs x5: @227, @897, @930, @1060, @1783 (matches le83-window's gloss).

### Thirds: 60 (n=18), 62 (n=35), 68 (n=8)

Formula-bound: 1 token each (@232, @1065, @1788). Free: 60 x17, 62 x34, 68 x7 (de-duplicated per §7).

Successor profile (top):
- 60 -> 03 x4 (@690, @1366, @1644, @1674), 08 x2, 71 x2, 67 x2, 12 x2; 94 x0
- 62 -> 94 x9 (@100, @508, @761, @840, @1329, @1362, @1686, @1704, @1772), 48 x6, 98 x5, 16 x4; 03 x0
- 68 -> 21 x2 (@114, @504, both "68-21-67"), 37/00/52/59/06/47 x1; 94 x0, 03 x0

Predecessor profile (top): 60 <- 21 x4, 92 x2, 14 x2, 06 x2; 62 <- 21 x5, 20 x4, 74 x3; 68 <- all x1 (89, 39, 79, 55, 65, 52, 47, 21).

### 21 (n=30) — the thirds' shared predecessor

Followers: 67 x8 (@109, @115, @505, @850, @1162, @1422, @1456, @1841), 62 x5, 60 x4, 65 x4, 64 x2. **21's top follower is 67, not the thirds.** 21-60: @118, @171, @196 free + @231 formula. 21-62: @99, @359, @1463, @1538 free + @1064 formula. 21-68: ONLY @1788 formula-bound (n=1 globally) — 68's contact with 21 is 100% formula-bound.
Predecessors: 96 x3 (all formula), 33 x3, 83 x3, 11 x2, 68 x2.

### 98 (n=40) — the formula head

Followers: 83 x5, 82 x3 (@19, @124, @894), 80 x3, 98 x3 (doubled @1073, @1145, @1660), 00 x3, 56 x2, 20 x2.
Predecessors: 62 x5 (@11, @82, @802, @945, @1141), 42 x3, 66 x3, 98 x3.
Doubled-98 windows: @1073 "11 44 74 42 98 98 12 48 77 78" (note 12-48 = "ne" letters, 77-78 = "lever" per queued lever-77-78); @1145 "62 16 29 42 98 98 86 67 33 66"; @1660 "11 24 48 47 98 98 80 22 94 84". No finite-verb reading survives the doublings.

### 83 (n=15) — full census ±3

| @ | window | 83-follower | note |
|---|---|---|---|
| 228 | 87 46 98 83 82 96 21 | 82 | formula |
| 614 | 47 77 87 83 70 88 10 | 70 | "ce de pre" adverse / "cède" rival |
| 898 | 82 14 98 83 86 16 92 | 86 | "98 de [86-INF]" cross-check |
| 907 | 88 18 55 83 54 49 64 | 54 | open |
| 911 | 54 49 64 83 59 37 96 | 59 | "qui de est" adverse |
| 931 | 48 82 98 83 56 69 26 | 56 | 98-83, non-formula follower |
| 1061 | 84 09 98 83 82 96 21 | 82 | formula |
| 1161 | 77 82 44 83 21 67 78 | 21 | "44 de 21" (pairs with @1840) |
| 1171 | 61 94 87 83 21 85 36 | 21 | "ne ce de [21]" adverse / "ne cède" rival |
| 1217 | 45 36 77 83 92 61 24 | 92 | owned by queued le83-window |
| 1334 | 70 52 39 83 86 71 64 | 86 | "[a] de [86-INF]" cross-check (left context caveat) |
| 1612 | 23 08 55 83 71 48 31 | 71 | open |
| 1784 | 65 23 98 83 82 96 21 | 82 | formula |
| 1829 | 29 82 38 83 24 82 16 | 24 | "[38] de en[24]" plausible (24='en' conditional) |
| 1840 | 22 42 44 83 21 67 78 | 21 | "44 de 21" (pairs with @1161) |

Follower summary: 82 x3 (all formula), 21 x3, 86 x2, 70/54/59/56/24/92/71 x1.

## Permutation test (homophone-set profile, {33,86} precedent standard)

Method: total-variation distance summed over cell pairs on the successor (resp. predecessor) distributions; labels permuted B=20,000 preserving cell counts; p = (ge+1)/(B+1). Reported both with and without the 3 formula-bound tokens (de-duplicated per §7; the de-duplicated figure is authoritative).

| cells | side | excl formula | n | stat | p |
|---|---|---|---|---|---|
| 60, 62, 68 | successor | no | 18/35/8 | 2.8032 | <0.0001 |
| 60, 62, 68 | successor | yes | 17/34/7 | 2.7941 | <0.0001 |
| 60, 62 | successor | yes | 17/34 | 0.9412 | <0.0001 |
| 62, 68 | successor | yes | 34/7 | 0.9118 | 0.0021 |
| **60, 68** | successor | yes | 17/7 | 0.9412 | **0.0540** |
| 60, 62, 68 | predecessor | no | 18/35/8 | 2.3802 | 0.1371 |
| 60, 62, 68 | predecessor | yes | 17/34/7 | 2.6471 | 0.0113 |
| **60, 68** | predecessor | yes | 17/7 | 1.0000 | **0.0560** |

Precedent yardstick (from queue): 09/92 HOLD — successor p=0.256; 23~26 SPLIT — successor p=0.0029.
Reading: the 3-way claim is rejected at kill grade on successors. Every pair involving 62 is rejected. 60 vs 68 is not rejected on either side, but p≈0.055 on n=7 is a thin null, not a positive homophony demonstration (uniformity is necessary but insufficient per lane law; counts 17:7 are skewed).

## 83='de' cross-checks (2 clean, per beat brief)

- **@898** "82 14 98 83 86 16 92": "98 83 86" = "[98] de [86-INF]". 86 is A9 INF-class granted. "de" + infinitive is the canonical frame. 98's value open (not assumed).
- **@1334** "70 52 39 83 86 71 64": "39 83 86" = "[a] de [86-INF]" (39=/a/ promoted). Left-context caveat: "70 52" ("pre [52]") unparsed; the 'de'+INF core is clean.
- Supporting pair: **@1161/@1839** "44-83-21-67-78" x2 byte-identical: "[44] de [21] [67] [78]". 44 is noun-shaped (queued noun-44); "noun de X" is natural. Both windows share the full 5-gram, so this is one frame-type, two instances.

Adverses (kill-grade for *unconditioned* 83='de' if unfenced):
- **@911** "54 49 64 83 59 37 96": "qui de est[59]" — ungrammatical. Fences: 59='est' is provisional (not 'est' here), or a clause boundary between 83 and 59.
- **@614** "47 77 87 83 70 88 10" and **@1171** "61 94 87 83 21 85 36": "ce de" x2 — ungrammatical. Rival fence: 87-83 = "cède/cédé" verb ("ne cède [21]" at @1171 parses under 94='ne' promoted; @614 "ce cède pre[70]" needs the 70-frame).

## Ranked frames (confidence x testability)

- **F1 "44-83-21-67-78" x2** (@1160/@1839): replicated 5-gram, 'de'-frame, tests 83/44/21/67/78 jointly. Highest testability.
- **F2 formula x3** (@227/@1060/@1783): the thirds locus; followers 71/18/47 all clause-level, consistent with "venir"-tails.
- **F3 "83-86" x2** (@898/@1334): cleanest 'de' cross-checks (86 INF-class granted).
- **F4 "87-83" x2** (@614/@1171): 'ce de' adverses / "cède" rival — decides whether the 'de' lead needs conditioning.
- **F5 "64-83-59"** (@911): 'qui de est' — the sharpest single adverse on 83='de'.
- **F6 "98-98" x3** (@1073/@1145/@1660): anti-verb evidence; fences the formula head.
- **F7 "21-67" x8**: 21's dominant frame; subsumes "68-21-67" x2 and the F1 tail. 21's class lives here, not in the thirds.
- **F8 "60-03" x4** (@690/@1366/@1644/@1674): 60's sharpest sub-pattern; "03" is verb-stem (queued stem-03) — if 60 ends a word, 03 starts the next.

French predictions (1840s diplomatic register): the formula reads "…de me parvenir" with 96="par" granted and 82="me" banked; 21+third = "venir" forces the thirds to be one syllable ("nir"-shaped) — the distributional test says 62 is not that syllable. "ne cède" (literary ne-alone) is the live rival at @1171. "de"+infinitive at F3 is the canonical 'de' frame.

## Ranked battery targets for the supervisor (5)

### T1. de-frame-44-83-21 — priority 2
- **id:** de-frame-44-83-21
- **claim:** "'44-83-21-67-78' x2 (@1160, @1839) reads '[44] de [21] [67] [78]' under 83='de'."
- **bars:** (a) both windows parse with 44 noun-shaped and 83='de'; (b) 21-67-78 resolves with stated values (67's positional rule, 78's 'ver'-lead or stated alternative); (c) zero contradiction across both windows.
- **evidence:** byte-identical 5-gram, two instances, two rows (a6_09, a8_11); "noun de X" is natural French; independent of the formula (not formula-bound).
- **adverses:** 44's value open — coordinate with queued noun-44 (do not duplicate); 21's class open; 67 is the sole polyvalence (positional rule required); the shared 83='de' lead carries the @911/@614/@1171 adverses (fenced at T2/T4, not re-litigated here).

### T2. fence-911-de — priority 2
- **id:** fence-911-de
- **claim:** "@911 '64-83-59' fences with stated cause under the 83='de' lead, or unconditioned 83='de' is killed."
- **bars:** resolve iff ONE grammatical parse covers "64-83-59" (@911, "54 49 64 83 59 37 96") with <=1 non-granted assumption; else record kill-grade failure of unconditioned 83='de' and escalate (do not kill at battery level — the lead is shared with le83-window).
- **evidence:** "qui de est" is ungrammatical under 64='qui' granted + 59='est' provisional + 83='de'.
- **adverses:** 59='est' is provisional (cheapest fence: 59 not 'est' here); a clause boundary between 83 and 59 is the alternative fence.

### T3. thirds-60-68-pair — priority 2
- **id:** thirds-60-68-pair
- **claim:** "60~68 form a 2-cell homophone set; 62 is excluded (not a homophone of either)."
- **bars:** (a) re-derive the {60,68} permutation test on the repaired stream (formula-bound tokens excluded) and meet the {33,86} indistinguishability standard on successors AND predecessors; (b) the two formula slots @227/@1783 parse as 'venir'-tails; (c) 62's exclusion cites the collision-62-84 kill and the 62->94 x9 vs 60->94 x0 / 68->94 x0 asymmetry — no re-litigation of 62's value.
- **evidence:** finder numbers: successor p=0.0540, predecessor p=0.0560 (n=17/7, B=20,000); 62->94 x9 (@100/@508/@761/@840/@1329/@1362/@1686/@1704/@1772) vs zero 94-followers for 60/68; 60->03 x4 vs 62->03 x0, 68->03 x0.
- **adverses:** 68 n=7 is thin; p≈0.055 is marginal, not a positive demonstration; 60-03 x4 vs 68-03 x0 not tested for significance; uniformity 17:7 is skewed (necessary-but-insufficient per lane law).

### T4. frame-87-83-cede — priority 3
- **id:** frame-87-83-cede
- **claim:** "'87-83' x2 (@614, @1171) reads 'cède/cédé' (verb), fencing the 'ce de' adverse against 83='de'."
- **bars:** (a) both windows parse with 87-83 as a 'céder'-shaped verb (@1171: "94 87 83 21" = "ne cède [21]" under 94='ne' promoted); (b) @614's left context "47 77" and "70 88" tail parsed or fenced with cause; (c) the consequence for the 83='de' lead stated (fenced adverse, not a kill).
- **evidence:** "ce de" x2 is ungrammatical under 83='de'; the verb rival explains both windows with one assumption.
- **adverses:** 83='de' lead (this fences rather than kills it); 70's frame at @614 unparsed; "céder" takes "à", not a bare complement — 21's class must allow it.

### T5. prof-98 — priority 3
- **id:** prof-98
- **claim:** "98's class is decided by its follower census (verb-frame test of the formula head)."
- **bars:** (a) 98-83 x5 parsed under one class for 98 (the x3 formula + @897/@930); (b) 98-98 x3 (@1073/@1145/@1660) fenced as formula or parsed — finite-verb readings must survive the doublings or be withdrawn; (c) 98-82 x3 (@19/@124/@894) and 98-80 x3 parsed under the same class.
- **evidence:** n=40 census; followers 83 x5 / 82 x3 / 80 x3 / 98 x3 / 00 x3; predecessors 62 x5 / 42 x3 / 66 x3 / 98 x3.
- **adverses:** French of 98 unconfirmed (standing adverse — this target exists to test it); doubled 98 resists finite-verb; 62->98 x5 entangles the collision cell.

## Nulls and non-findings (results, not gaps)

- 3-way thirds homophony: rejected, p<0.0001 (successors). The queued frame-vient-parvenir bar "thirds profile as homophone set" fails at 3-way; T3 is the 2-cell fallback.
- 60 vs 68: null (p=0.054/0.056, thin n). Not evidence for homophony — absence of rejection only.
- 21-68 exists solely in the formula slot (n=1 globally). Any claim about 68's non-formula behavior is unsupported.
- 96-21 x3 confirmed formula-bound; 98-83 x5 confirmed (not x4). Both match existing queue glosses — no new claim.
- 83's follower census is mixed: "de"-compatible (86 x2 INF, 24 x1, 21 x3) vs hostile ("ce de" x2, "qui de est" x1). Unconditioned 83='de' is null-to-negative pending T2/T4 fencing.
- No second "44-83-21"-shaped frame beyond the x2 pair; no "21-[third]" frame outside the formula except 21-60 x3 / 21-62 x4 free (formula-adjacent, not formula-bound).
- 98's "vient" reading: negative signal (doublings). 98 stays class-open.

## Coverage map (queued targets NOT duplicated)

- **frame-vient-parvenir** (queued): owns the thirds permutation test + 83='de' cross-checks. This report FEEDS it (numbers, windows, cross-checks above). T3 narrows the claim to the 60/68 pair — a distinct claim, not a duplicate.
- **le83-window** (queued): owns @1216 ('36 77 83') + 98-83 x5. Untouched. T2 (@911) and T4 (@614/@1171) use different windows — complementary, fenced as such.
- **lon-ne-77-62-94** (queued): @507 frame untouched. Noted in passing: @508's window "21 67 77 62 94 64 98" places 98 right after the frame — context only, no claim.
- **noun-44** (queued): owns 44's class. T1 coordinates (does not name 44's value).
- **collision-62-84** (verdict: kill): 62='on' killed, 62='il' demonstrated. Cited for 62's exclusion (T3c); nothing re-litigated.
- **ver-78 / lever-77-78 / ne-le-1075** (queued): 78's value cited as open in T1b; @1073's "98 98 12 48 77 78" noted as cross-evidence, not claimed.
- **stem-03** (queued): 60-03 x4 (F8) noted as its input; not claimed here.
- **frame-62-94-79, slot-split-62-84, 06-forces-84** (queued): 62's pre-'ne' slot behavior cited only.

## Method note

Clustered by follower pattern first (thirds successor census), then predecessor; permutation test vs the {33,86} precedent standard (09/92 p=0.256 hold / 23~26 p=0.0029 split yardsticks); French predicted from 1840s diplomatic register ("vient de me parvenir", literary "ne cède", "de"+infinitive); formula windows de-duplicated before counting productive frames; settled kills never re-litigated. All @-offsets are repaired-stream indices.
