# Round-16 battery: formula-tails

Finder report: `code/crowd16/report_inbox/next-token-findings-formula-tails.md` (ingested 2026-10-07).
Tails = 3 groups after the formula closes. Stream: repaired 1,847-pair parse.

---

## PRE-REGISTRATION (locked before formal tests)

**Scope notes (overtaken claims):** (i) T1's "00='pour' promotion track" is
already-banked ground (A9) — the "cela pour" ×3 can only STRENGTHEN, not
promote. (ii) T2's "84 noun vs verb-stem fork — test both, do not merge" is
overtaken by the round-15 A15 grant (84="on", F53 noun-arm KILLED) — this
battery does not re-litigate the fork; it checks whether T2's windows add
legs or residuals to the GRANTED value.

**Bar F1 (T1 "cela pour" ×3):** CONFIRM-as-strengthening iff 87-11-00
re-derives ×3 exact. Cannot promote (already banked).

**Bar F2 (T2 84 hub):** the "le 84" frame legs are checked against the
GRANTED 84="on". A window that does not parse under "on" is a FENCED
residual (R3…), not a fork re-opening — the fork is settled kill-grade
(F53 noun-arm superseded).

**Bar F3 (T3 "entrepre[12]"):** LEAD-grade iff (i) the @340 tail re-derives
exact [6,70,12]; (ii) 70="pre" is banked (pencil GT — yes); (iii) the reading
is explicitly CONDITIONED on the 06="ent" LEAD (not a banked value). A lead
names 12's paradigm ("entrepre-" continuation), not 12's value.

**Bar F4 (T4 20):** single-leg feed to the 20-paradox battery, not a
resolution (finder's own "half" grading stands).

**Bar F5 (T5 63):** n=1 → NULL as a value claim; recorded as a 63
constraint.

**Bar F6 (nulls):** the finder's "no cluster" nulls (par-ce-que ×4 distinct
tails, toutefois ×2 distinct) are verified as stated — nulls are results.

---

## TESTS

`t = code/crowd16/next-token/test_formulatails.py`.

| # | assertion | got |
|---|-----------|-----|
| 1 | F-qui-par tails: @340 → [6,70,12]; @1024 → [3,29,80] | |
| 2 | 87-11 starts = [74,163,201,461,830,1242,1403]; 87-11-00 = [74,1242,1403] | |
| 3 | 06-70 ×1 @346 | |
| 4 | @146 window P[144:151] = [64,77,84,29,87,64,96]; 84→29 = [146] | |
| 5 | @1290 window P[1288:1295] = [11,17,84,59,35,94,52] | |
| 6 | @1799 window P[1799:1806] = [79,87,64,77,84,59,35] | |
| 7 | @754 window P[754:762] = [11,70,82,34,29,40,20,62] | |
| 8 | @1041 window P[1039:1046] = [40,17,77,82,63,11,67]; 82-63 = [1042] | |
| 9 | toutefois tails: @451 → [77,60,65]; @1460 → [1,21,62] (distinct) | |
| 10 | par-ce-que tails: @224 → [98,83,82]; @952 → [24,85,4]; @1526 → [21,65,63] (all distinct) | |

---

## VERDICT

**F1 "cela pour" ×3 — CONFIRM as strengthening (not promotion).**
87-11-00 re-derived ×3 @74/@1242/@1403 (bigram starts; 00-cells @76/@1246/@1407).
"cela pour [33/11]…" ×3 are new compositional legs for the already-banked
00="pour" — they strengthen the A9 grant's "pour que"-independent profile
(the grant rested on "pour que" legs + preposition profile; "cela pour" adds
a determiner-phrase frame). No double-promotion.

**F2 84 hub — legs check against the GRANTED value; one new residual.**
The "le 84" ×7 / "le 84 est" ×3 frames are the A15 grant's own legs — no new
information. **@146 is a NEW fenced residual (R3) for 84="on":** P[144:151] =
[64,77,84,29,87,64,96] = "qui l'on er[29]…" — ungrammatical under 84="on"
(and the F53 noun-arm that could have read it is kill-grade dead). The
finder's "test both, do not merge" is overtaken: the fork was settled by A15
(noun-arm KILLED, "on" GRANTED with conditions). @146 joins R1 (@1619 "la
on") and R2 (@1664 "ne on") as fenced 1-window residuals — 3/25, still
fence-grade, not kill-grade. Note: @145 is itself one of the 7 "l'on" legs,
so this residual sits ON a grant leg's successor — the "l'on" bigram stands,
its "er" continuation is what's fenced.

**F3 "entrepre[12]" — LEAD (conditioned).** Tail @340 re-derived exact
[6,70,12]; 06-70 singleton @346; 70="pre" banked (pencil GT). The reading
"entrepre-[12]" ("entreprendre/entrepris"-shaped) is CONDITIONED on the
06="ent" LEAD — lead-grade, correctly short of a value claim. **12's battery:
verbal continuation of "entrepre-"** ({-ndre, -is, -enait…} paradigm —
predict from the 1841 corpus, then check 12's contact profile). The @1024
tail [3,29,80] ("[03]er", verb-stem frame) is a separate 03-battery target.

**F4 20 — single-leg feed, not a resolution.** @754 = [11,70,82,34,29,40,20,
62,94] verified: "la première [20]" (20@760) puts 20 in a feminine-noun
slot — one leg for the feminine-noun side of 20's paradox (with the pour
beat's @667 "pour [20]" leg). The determiner/adjective side (@308 "[20]
fois que") stays open. Fed to the 20-paradox battery as stated.

**F5 63 — NULL as a value claim.** 82-63 singleton @1042 ("le m[63]" after
"la première fois"). Recorded as a 63 constraint (m-initial masculine noun
completion), nothing more.

**F6 nulls — verified as stated.** toutefois tails [77,60,65] vs [1,21,62]:
distinct, no cluster. par-ce-que tails [98,83,82]/[24,85,4]/[21,65,63]: four
windows, four distinct tails — "parce que [clause]" too open to cluster.
The finder's nulls are honest results, kept.

Finder convention note: "@340 …01-06-70-12" cites the formula start; the
tail itself starts @346. All resolve to identical physical cells.

**Queued:** 12-paradigm battery ("entrepre-" continuation); 03 verb-stem
battery ("[03]er"); 20-paradox battery (now 2 feminine-noun legs: @667,
@760); 63 constraint file.
