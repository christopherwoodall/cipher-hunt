# Round-16 battery: classes (31/33) — record correction, "dire" lead

Finder report: `code/crowd16/report_inbox/next-token-findings-classes.md` (ingested 2026-10-07).
Status entering: 31=VERBAL (class), 33=INF (class), 86 INF-class (frame).
33="dire" was a leading partial (round-15 A10, unpromoted).

---

## PRE-REGISTRATION (locked before formal tests)

**Bar C0 (record correction):** CONFIRM iff 67-33 re-derives ×6 (round-11's
"×1" void).

**Bar C1 (33="dire" LEAD):** LEAD-grade iff "67 33 46" ×2 re-derives with
the dual-fork idiomaticity available AND "47 33" ×2 re-derives. The
candidate scoring (vouloir killed, penser weak) is recorded as the finder's
French judgment on frames, not as battery-derived — the battery verifies
frames, not idiomaticity. Promotion BLOCKED by P2 (stated by the finder;
confirmed here).

**Bar C5 (31=VERBAL class):** CONFIRM iff 31's 8 followers are 8/8 distinct
(class-tier signature, not a value).

---

## TESTS

`t = code/crowd16/next-token/test_classes.py`.

| # | assertion | got |
|---|-----------|-----|
| 1 | n31 = 8; n33 = 25 | |
| 2 | 67-33 = 6 [272,1148,1423,1450,1476,1623] (correction) | |
| 3 | 33-29 = [273,626,1232,1424,1477] (×5) | |
| 4 | 00-33 = [185,407,466,845,935,1087,1244,1629] (×8) | |
| 5 | 64-33 = [] ("qui 33" 0×) | |
| 6 | 67-33-46 = [1450,1623] (×2) | |
| 7 | 47-33 = [23,1231] (×2) | |
| 8 | 33-21 = [936,1421,1630]; 33-21-64-37 = [936,1630] | |
| 9 | 31 followers 8/8 distinct: {10,11,14,24,29,76,79,92} | |
| 10 | 31 lefts: {8:3, 64:2, 11:1, 48:1, 61:1} | |
| 11 | 31-79 = [882]; 11-31-11 = [1515]; 31-24 = [1521] | |
| 12 | 03-64-31 = [336,1645] (finder cited 31-cells) | |
| 13 | 33-00-86-56 = [1000,1504] (×2) | |

---

## VERDICT

**C0 record correction — CONFIRM.** 67-33 = **6×** [272,1148,1423,1450,
1476,1623], not round-11's "×1". The correction is byte-verified and
propagates: "67 33 29" ×3 [272,1423,1476], "67 33 46" ×2 [1450,1623],
"67 33 66" ×1. Round-11's count is void.

**C1 33="dire" — LEAD (promotion blocked by P2).**
- "67 33 46" ×2 @1450/@1623 re-derived: "et/veut [inf] que" — idiomatic
  under BOTH forks ("et dire que" the idiom; "veut dire que" = "to mean
  that"). No other candidate is idiomatic under either fork. Strongest
  single lead for 33's value.
- "47 33" ×2 @23/@1231 re-derived: "ce [inf]" (preverbal demonstrative +
  infinitive) — consistent with "dire"/"savoir"/"croire".
- "33 21" ×3, "33 21 64 37" ×2: "[inf] [noun] qui [verb]" — "dire [N]
  qui…" natural.
- The finder's candidate scoring (vouloir KILLED: "et vouloir que"✗;
  penser WEAK; croire/savoir survive) is recorded as frame-based French
  judgment — the battery verifies the frames, not the idiomaticity
  rankings.
- **P2 blocks promotion:** "33 29" ×5 (@273/@626/@1232/@1424/@1477,
  29's #1 left context) puzzles all five candidates — the 29-89-84 /
  29-82-16 word-shapes ("erreur"?) must resolve first. 33="dire" stays
  LEAD (leading partial, unpromoted — as in A10).

**C3/C4 — queued.** The doubled 5-grams ("00 33 79 80 06", "00 33 21 64 37",
"00 33 16 00", "33 00 86 56" ×2 @1000/@1504 — segmentation: "[inf]. Pour
86 56…") and the single-vs-set question ("33 21 67 33", "33 42 33" chains)
go to the 33 battery. "67 33" 3/2/1 split confirmed.

**C5 31=VERBAL — class CONFIRMED.** 8 followers, 8/8 distinct
{10,11,14,24,29,76,79,92} — the class-tier signature (a single word would
show formulaic repeats, cf. 33's doubled 5-grams). Lefts: 08×3, 64×2
("qui 31" ×2), 11/48/61. "31 79" @882 = "[verb] tout" — new compositional
support for 79="tout" (6th leg family: "sait tout"/"dit tout"-shaped).
"11 31 11" @1515 / "31 24" @1521: anomalies queued (imperative vs boundary).
Person: UNDETERMINED (honest null held) — attack via "03 qui 31" ×2
(@336/@1645, the only replicated left frame), not followers.

**Queued:** 29-89-84 / 29-82-16 word-shapes (top blocker); 33 idiom battery
(dire ≫ savoir/croire ≫ penser); 33 single-vs-set; 03 profile; "11 31 11"
anomaly; "33 00 86 56" segmentation.
