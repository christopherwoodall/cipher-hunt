# Round-16 battery: e (40) — collocations, formulas, anomaly

Finder report: `code/crowd16/report_inbox/next-token-findings-e.md` (ingested 2026-10-07).
Status entering: 40="e" BANKED (pencil GT). 96="par" PROMOTED. 67 fork =
sole true polyvalence (settled). 62="on" STRONG lead.

---

## PRE-REGISTRATION (locked before formal tests)

**Scope:** 40="e" is banked; followers are word-boundary onsets (next word's
first syllable). This battery adjudicates collocations and formulas, not
the value.

**Bar E1 (P1 "e 65 94" ×2):** CONFIRM iff byte-identical ×2 AND 65-94
occurs nowhere else (exclusive collocation). 65 queued as battery target.

**Bar E2 (P2 "20 62 94"):** CONFIRM iff ×3 re-derived; "la première 20" ≠
fois recorded; 62's dual {48,94} selection noted for the collision battery.

**Bar E3 (P3 "67 77 81" ×4):** CONFIRM iff ×4 re-derived; the 67="et"
frame-vote recorded as FORK-CONDITIONAL (not a global fork resolution).

**Bar E7 (P7 @848 anomaly):** fenced as mild adverse for 96="par" (or
word-boundary case); not a kill.

---

## TESTS

`t = code/crowd16/next-token/test_e.py`.

| # | assertion | got |
|---|-----------|-----|
| 1 | n40 = 21 | |
| 2 | 40-65-94 = [686,1711]; 65-94 global = [687,1712] (exclusive) | |
| 3 | 20-62 = [760,839,1135,1703]; 20-62-94 = [760,839,1703] | |
| 4 | @760: P[758:766] = [29,40,20,62,94,59,39,88] | |
| 5 | 62-94 = 9; 62-48 = 6 | |
| 6 | 67-77-81 = [743,1239,1400,1597]; @1239/@1400 windows | |
| 7 | 08-31 = [881,1488,1520] | |
| 8 | 65-64 = 3; 21-65 = 4 | |
| 9 | @848: P[844:852] = [16,0,33,96,40,62,21,67]; 96-40 = [847] | |
| 10 | @60: P[58:65] = [12,41,8,34,29,40,12] | |
| 11 | @1557: P[1555:1562] = [93,61,40,17,11,26,30] | |

---

## VERDICT

**E1 "e 65 94" ×2 — CONFIRM (exclusive collocation).** Byte-identical
@686/@1711 ("…ère 65 94…" ×2); 65-94 occurs NOWHERE else ([687,1712] —
both post-40). A fixed collocation after feminine "-ère" nouns. 65 is now
the single highest-value unknown: top "-ère" follower (3/9), "65-94"
exclusive, "65 qui" ×3, "21 65" ×4. Full 65-profile battery QUEUED
(priority 1).

**E2 "20 62 94" — CONFIRM.** ×3 @760/@839/@1703; 20-62 ×4. @760 =
[29,40,20,62,94,59,39,88] = "…ère [20] [62] [94] est [39]…" — "la première
[20-62-94] est…". "la première 20" ≠ fois (20="fois" killed, 20~17 split):
20 needs a feminine singular noun (partie/occasion/année/place/moitié —
census candidates, not verdicts). **62's dual selection:** 62-94 ×9 AND
62-48 ×6 — 62 takes BOTH members of the ne-distributed {48,94} pair as
frames ("on ne" ×9, "on [48]" ×6). This is load-bearing for the 62/84
collision battery: 62's "on"-frames span both cells. Noted, not ruled.

**E3 "67 77 81" ×4 — CONFIRM (fork-conditional).** @743/@1239/@1400/@1597
re-derived; @1239/@1400 share the byte-identical 6-gram 67-77-81-87-11-0
("et/veut le [81] ce la pour"?? — [67,77,81,87,11,0]). In THIS frame 4/4
windows read as "et le [noun]" while "veut le [noun]" ×4 is strained (no
subject). Frame-conditioned evidence for 67="et" — handed to the forks
battery as a fork-conditional datum, not a global resolution. 81's "prin"
reading is dead per the finder (kill record not re-verified in this
battery); 81 returns to NULL/open — 81 noun-profile queued.

**E4 08 — battery queued, no verdict.** 08-31 ×3 @881/@1488/@1520 (08 before
finite verbs); "et/veut 08" ×2; "…e 08" ×2; @60 "[08]ière" (spelling-letter
pull) vs the verbal frames (ne/se/on pull). Genuine fork — needs the full
contact profile. Not forced.

**E5/E6 — queued/recorded.** 65's "-ère" dominance (3/9) folded into the 65
battery. @1557 "61-40 17" singleton hypothesis recorded ("un"+"e" split?
61 as subject before "est" ×2 @447/@1510 noted).

**E7 @848 — fenced mild adverse for 96="par".** [16,0,33,96,40,62,21,67] =
"[33-INF] par e [62][21] et/veut" — 96-40 ×1 globally ("par e" has no clean
reading under 96="par" promoted). Either 96≠"par" here (mild adverse,
fenced) or word-boundary ("…[33] par | e…" — "par" + "e"-initial word).
The finder's red-team flag is kept: "33 96 40" @846 does not recur.

**Queued:** 65 full profile (priority 1); "20 62 94" frame + 20 feminine-
noun filter; 81 noun profile; 08 disambiguation; @848 re-examination with
96's profile.
