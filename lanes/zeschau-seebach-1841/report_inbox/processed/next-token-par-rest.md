# Round-16 battery: par-rest (96) — 45="ce" promotion adjudicated

Finder report: `code/crowd16/report_inbox/next-token-findings-par-rest.md` (ingested 2026-10-07).
Status entering: 96="par" PROMOTED. 45="ce" HOLD (round-15 A11, red-team
confirmed: "~1.5 mirrored frame-types, bar needs ≥2"). 7 solved windows
excluded before clustering (verified: 96-00 ×3, 96-87-46 ×3, 96-47-46 ×1).

---

## PRE-REGISTRATION (locked before formal tests)

**Bar R1 (45="ce" PROMOTE):** A11's bar needs ≥2 mirrored frame-types; it
had ~1.5. PROMOTE iff the par-rest finder supplies ≥0.5 NEW full frame-types
of clean "ce" frames, with zero contradictions. Legs examined: @314 "ce qui
est 32", "par 45" ×2, @437 "ce que" (frame-label CHECKED — "ce que"+noun is
strained, discounted if so). Taxonomy (third allophone vs homophone) is
QUEUED, not ruled — the value promotes; the distribution model follows.

**Bars R2–R7:** counts re-derived; formulas confirmed; anomalies fenced;
no new values named.

---

## TESTS

`t = code/crowd16/next-token/test_parrest.py`.

| # | assertion | got |
|---|-----------|-----|
| 1 | n96 = 21; n45 = 22 | |
| 2 | solved excluded: 96-00 [47,465,960]; 96-87-46 [224,952,1526]; 96-47-46 [150] | |
| 3 | @314: P[310:320] = [84,24,37,78,45,64,59,32,94,6] | |
| 4 | 45-64 = [314,340,1024] | |
| 5 | 96-45 = [602,1213]; @602 P[600:607]; @1213 P[1211:1218] | |
| 6 | @437: P[435:442] = [78,63,45,46,43,98,80]; 45-46 = [437] | |
| 7 | 96-43-87-01 = [342,1026] | |
| 8 | 11-43 = [562]; 43-00 = [244,1126,1544]; @1544 P[1542:1549] | |
| 9 | 83-82 = [228,1061,1784] (only ×3); 98-83 = [227,897,930,1060,1783] | |
| 10 | @109: P[107:114] = [46,11,21,67,93,29,89] | |
| 11 | 96-86 = [947]; @947 P[945:953] | |
| 12 | 82-16-96 = [1194]; @1196 P[1194:1202] | |
| 13 | 96-48 = [927]; @927 P[925:933] | |

---

## VERDICT

**R1 45="ce" — PROMOTE → REVISED TO HOLD (forks battery, this round).**
A11 held for "~1.5 mirrored frame-types (bar needs ≥2)". The par-rest
finder supplied "par ce" ×2 as the second type → PROMOTED. **The forks
battery then forced a revision:** "ce verdict" ×2 (@573/@982, 87/47="ce"
banked + 78-45) makes "ce [78] ce" ungrammatical → 45="dict" (in
"verdict") at those windows; @314 ("verdict qui est 32" vs "[78] ce qui
est 32") is contested. 45 has two values in complementary distribution
("dict" only after 78; "ce" elsewhere) — positional allophony,
lane-precedented (47/87).
- **45="ce" DEMOTED from PROMOTE to HOLD** (this round's promotion
  revised; the @314 flagship leg is contested and the value is bipartite).
- **45 "ce/dict positional allophones" LEAD** (conditional on 78="ver").
- Standing "ce" legs (78-independent): "par 45" ×2 (@602/@1213), "45-64"
  ×2 (@340/@1024 formula heads), 0/22-vs-10/32 complementarity, zero
  contradictions. The value isn't wrong; it's incomplete.

**R2 formula — CONFIRM, null on reading (honest).** 98-83-82-96-21
byte-identical ×3 (@227/@1060/@1783 — the m-beat's P1, corroborated);
83-82 occurs ONLY in these 3 windows; 98-83 ×5. French not visible — the
finder's formula-grade null is kept. 21 = feminine noun ("la 21 et" @108
verified) — 21 battery queued.

**R3 43 feminine noun — LEAD.** "la 43" @562, "par 43" ×2 (96-43 in
F-qui-par), "43 pour que" @1544, "43 le" ×2, "37-43" ×3 — all re-derived.
43 = feminine noun of means/purpose (suite/condition/manière/mesure
candidates, "pour que"-frame discriminates). LEAD (value not named).

**R4 96-86 anomaly — fenced.** @947 = [62,98,96,86,1,77,86,96] = "par 86 01
le 86" — "par"+bare infinitive ungrammatical. FENCED as a 96-frame anomaly;
the 86=infinitive class (12× "pour 86" bedrock) is PROTECTED, not weakened.

**R5 doubled 82-16 frame — red-team anomaly.** @1196 = [82,16,96,82,16,64,…]
= "82-16 par 82-16 qui" — the doubling doesn't parse ("mais par mais qui").
Flagged as a standalone anomaly (possible boundary misread). Not forced.

**R6 96-48 — fenced.** @927 = [17,61,96,48,82,98,83,56] = "par 48 m 98".
If 48="ne", "par ne" ungrammatical — value or frame is off here. Fenced;
48's value stays open.

**R7 singletons — leads.** "par e-62" @847 (folded into e-beat E7); "par 09"
@914 (09 pronoun/determiner candidate, "09 qui" frame); "par 56" @131 ("56
ce" ×4 lead frame).

**Queued:** 45/87/47 contact-similarity (taxonomy); 65 profile; 21 battery;
43 feminine-noun battery; 83 via "98-83"; 09 "qui" frame; 56 "ce" frame.
