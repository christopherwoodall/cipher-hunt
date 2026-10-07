# Formula Hunter — results (2026-10-07)

Executor: formula-hunter (crowd lane). Scope: repeated group sequences as probable set phrases in R5005.

## Method
- Pair-aligned group stream via `code/crib_attack.py::load_pairs` (1,846 pairs, 96 groups; counts re-verified against `data/attempt1_results.json`: distinct=96, `77 78 94 82 06`=2×, `06 77 78 18 71 10 01`=0× ✓).
- Exhaustive n-gram census, lengths 14→2, occurrences counted with overlap. **Never** digit-substring counts.
- Caution: naive maximal-match "extension" double-counts the seed position (off-by-one). One claimed extension (9-mer → 10-mer via 46=que) was **refuted** on re-check; all extensions below were re-verified with direct occurrence scans.

## Verdict
**Scatter, not salutation/valediction.** Repeats are discourse-level set phrases, not letter-opening/closing formulas. 13 of 16 long repeats (L≥5) are body/body; the rest are body/CLOSE pairs; **no repeat is exclusive to the opening or closing 100 groups**, and opening repeats are all L≤4 and shared with body. The valediction phrase occurs once (single letter) → unrecoverable by repetition, as expected.

**Hard win:** `11 70 82 34 29 40` @1033–1038 reads **"la première"** — six consecutive groups, every one a ground-truth pencil-crib anchor (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e), spelling a correct French word. First multi-group word read in the lane from cribs alone. Single occurrence; feed it as 6 locked groups into the next drag run.

## Repeat inventory (top 30 by length×frequency; subsumed shorter forms noted)

| # | Sequence | L | n | L×n | Positions | Zones | Note |
|---|----------|---|---|-----|-----------|-------|------|
| 1 | 56 69 26 00 33 21 64 37 01 | 9 | 2 | 18 | 931, 1625 | body, body | longest repeat; unread — top crib-drag target |
| 2 | 40 67 77 81 87 11 00 | 7 | 2 | 14 | 1237, 1398 | body, body | ends "cela 00" (87=ce, 11=la) |
| 3 | 84 59 35 94 52 80 04 | 7 | 2 | 14 | 1289, 1802 | body, CLOSE | — |
| 4 | 45 64 96 43 87 01 | 6 | 2 | 12 | 340, 1023 | body, body | contains 87=ce |
| 5 | 78 45 13 55 61 94 | 6 | 2 | 12 | 573, 1163 | body, body | — |
| 6 | 76 49 24 26 30 03 | 6 | 2 | 12 | 652, 988 | body, body | — |
| 7 | 65 63 00 66 73 41 | 6 | 2 | 12 | 1105, 1529 | body, body | — |
| 8 | 98 83 82 96 21 | 5 | 3 | 15 | 227, 1059, 1782 | body, body, CLOSE | contains 82=m; que-adjacent once; "pre" follows 2/3 |
| 9 | 46 84 24 37 78 | 5 | 2 | 10 | 309, 472 | body, body | starts 46=que |
| 10 | 00 33 79 80 06 | 5 | 2 | 10 | 466, 1086 | body, body | — |
| 11 | 02 24 49 74 74 | 5 | 2 | 10 | 857, 915 | body, body | — |
| 12 | 06 77 76 01 98 | 5 | 2 | 10 | 889, 966 | body, body | — |
| 13 | 06 11 52 37 43 | 5 | 2 | 10 | 1121, 1719 | body, body | contains 11=la |
| 14 | 44 83 21 67 78 | 5 | 2 | 10 | 1159, 1838 | body, CLOSE | letter-final head (1838–1842; letter ends 1845) |
| 15 | 77 78 94 82 06 | 5 | 2 | 10 | 1179, 1350 | body, body | contains 82=m; "-ment" family candidate |
| 16 | 62 94 79 14 60 | 5 | 2 | 10 | 1361, 1685 | body, body | — |
| 17 | 65 63 00 66 | 4 | 3 | 12 | 251, 1105, 1529 | body ×3 | subsumed in #7 at 2/3; extra @251 |
| 18 | 69 26 00 33 | 4 | 3 | 12 | 405, 932, 1626 | body ×3 | subsumed in #1 at 2/3; extra @405 |
| 19 | 92 69 13 24 | 4 | 2 | 8 | 66, 1378 | OPEN, body | — |
| 20 | 87 11 00 11 | 4 | 2 | 8 | 74, 1402 | OPEN, body | "cela 00 la" |
| 21 | 64 77 84 59 | 4 | 2 | 8 | 1444, 1800 | body, CLOSE | near-miss twin @1444 diverges at 5th group (…59 36… vs …59 35…) |
| 22 | 63 00 66 | 3 | 4 | 12 | 252, 713, 1106, 1530 | body ×4 | — |
| 23 | 49 74 74 | 3 | 4 | 12 | 416, 814, 859, 917 | body ×4 | — |
| 24 | 67 77 81 | 3 | 4 | 12 | 743, 1238, 1399, 1596 | body ×4 | 2 subsumed in #2 |
| 25 | 00 86 56 | 3 | 4 | 12 | 960, 1000, 1504, 1790 | body ×3, CLOSE | — |
| 26 | 24 87 11 | 3 | 3 | 9 | 73, 162, 828 | OPEN, body, body | "24 cela" |
| 27 | 87 11 00 | 3 | 3 | 9 | 74, 1241, 1402 | OPEN, body, body | "cela 00" |
| 28 | 64 77 84 | 3 | 3 | 9 | 144, 1444, 1800 | body, body, CLOSE | — |
| 29 | 24 87 64 | 3 | 3 | 9 | 179, 1765, 1773 | body, CLOSE, CLOSE | "24 ce 64" — hinges on 64="qui" |
| 30 | 96 87 46 | 3 | 3 | 9 | 224, 951, 1525 | body ×3 | "96 ce que"; @224 heads repeat #8 |

Top bigrams (all scatter, none zone-exclusive): `00 86` ×12, `82 16` ×11 (m+16), `24 87` ×10 (24+ce), `29 40` ×9 (er+e), `62 94`/`21 67`/`00 33` ×8, `77 78`/`87 11`/`77 84`/`00 66` ×7.

## Positional clustering
- **OPEN (0–99):** only short repeats (L≤4), every one also occurring in body. No salutation-length formula.
- **CLOSE (1746–1845):** repeats present but **none CLOSE-exclusive** — each also occurs in body (`84 59 35 94 52 80 04`, `98 83 82 96 21`, `44 83 21 67 78`, `24 87 64` ×2, `77 84 59`, `64 77 84 59`, `77 84 09`, `24 82 16`, `00 86 56`, `86 29 82`, `00 86 29`, `78 49 74`, `94 24 87`, `24 85 58`). The letter's final 8 groups are `44 83 21 67 78 49 74 93`; only the 5-group head repeats (body @1159).
- **Conclusion:** the repeated material is mid-discourse formula (subordinate clauses, transitions), not framing formulas.

## Anchor cross-checks
- **87=ce:** appears in `24 87 11` ×3, `87 11 00` ×3, `87 11 00 11` ×2, `24 87 64` ×3, `96 87 46` ×3, `45 64 96 43 87 01` ×2, `40 67 77 81 87 11 00` ×2 — the "cela"/"ce que"/"ce qui" frames are all repeat-supported.
- **82=m:** in `98 83 82 96 21` ×3, `77 78 94 82 06` ×2, `82 16` ×11, and the "première" read.
- **46=que:** heads `46 84 24 37 78` ×2 and (via `96 87 46`) the #8 repeat @224.
- **11=la, 29=er, 34=i, 40=e:** in the "première"/"-ière" items and `29 40` ×9.

## Candidate readings (hypotheses unless marked)

- **R1 — `24 87 11` ×3 = "[de|pour] cela".** Implied: 24 = rank-2 function word (52×, rank 2/96), 87=ce, 11=la. Check PASSED (rank consistency; identical left context ×3). Register caveat stands (NOTES F6/F8: "cela" rare in formal prose) but 87=ce is lane-accepted.
- **R2 — `24 87 64` ×3 = "[pour|en] ce qui".** Depends on attempt-3's 64="qui". If confirmed, 24 ∈ {pour ("pour ce qui est/concerne"), en ("en ce qui concerne"), de ("de ce qui suit", marginal)} — all prime diplomatic frames. UNCHECKED (dependency).
- **R3 — `96 87 46` ×3 = "parce que" | "de ce que" | "à ce que".** Implied: 96 = par|de|à. UNCHECKED. Proposed check: crib-drag 96 in this frame.
- **R4 — `77 78 94 82 06` ×2 = "-ment/-nement" word** ("gouvernement", "département", "en ce moment"). Implied: 06="ent" (?). Check WEAK: `82 06` only 4× (low for "-ment"); 3rd `94 82 06` @578 is followed by 06 again. Letter-level rival "terme/forme/larme" conflicts with 40=e unless homophones. UNCHECKED.
- **R5 — `11 70 82 34 29 40` @1033 = "la première". CONFIRMED at byte level** (pairs[1033:1039] = 11,70,82,34,29,40; all six are ground-truth anchors). Single occurrence. Companion: `34 29 40` ×2 = "-ière"; @61 reads "41 08"+"ière" → propose 41="der", 08="ni" ("dernière") as follow-up test.
- **R6 — `40 67 77 81 87 11 00` ×2 = "e ? ? ? cela ?".** "cela 00" ×3 sub-frame; 00 = "est"|"et" candidates. UNCHECKED. Note: before_00 has 11=la ×4 ("la est" ungrammatical → counts against 00="est").
- **R7 — `98 83 82 96 21` ×3: unresolved.** Structural facts: headed by "96 ce que" once (@224); followed by 70=pre within ≤4 groups 2/3 (baseline P≈0.032, n=3, suggestive). "que je [ne] m…" family noted; 83="ne" testable via 83/21 co-occurrence. UNCHECKED.

## Null results (first-class)
- N1: No CLOSE-exclusive repeat — valediction unrecoverable by repetition (single letter, as expected).
- N2: No salutation-length repeat in opening ("Monsieur le Baron", "J'ai l'honneur" unfound).
- N3: `06 77 78 18 71 10 01` = 0× at pair alignment (upstream ×3 was misalignment artefact) — re-verified.
- N4: `24 87 46` ("24-ce-que" frame) = 0× — the "est-ce que" trigram still does not fire.
- N5: No repeat evidence for Dresde / Saint-Pétersbourg / janvier / dix-huit / Majesté / Excellence / Altesse.
- N6: The 9-mer does not extend backward (corrected off-by-one); maximal match is exactly 9 groups.

## What I'd try next
1. Crib-drag the 9-mer `56 69 26 00 33 21 64 37 01` against the era-matched syllable corpus (attempt-3) — highest-value unknown.
2. Resolve group 24 via `24 87 64` once 64="qui" is ruled in/out.
3. Test 96="par"/"de" in the "96 ce que" frame; test 41="der"/08="ni" ("dernière" @59–63).
4. Probe 00 via "cela 00" ×3 ("est" vs "et" via bigram grammar).
5. Sweep letter-final `44 83 21 67 78 49 74 93` against standard valedictions once more anchors land.
6. Lock `11 70 82 34 29 40` ("la première" @1033) as 6 fixed groups in the next drag run.
