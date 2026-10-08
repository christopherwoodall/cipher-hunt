# Round-16 battery: er (29) — frames, "se"-allophone lead, discrepancy kill

Finder report: `code/crowd16/report_inbox/next-token-findings-er.md` (ingested 2026-10-07).
Status entering: 29="er" BANKED (pencil GT). 47="ce" GRANTED (allophone
tier). 67 fork = sole true polyvalence (settled). 77="le" provisional.

---

## PRE-REGISTRATION (locked before formal tests)

**Bar E1 (P1 47="se" after infinitives):** LEAD-grade iff 29 is a top
predecessor of 47 AND 29-47-33 re-derives ×2 with the "se"+infinitive
reading available. Taxonomy: "se"-after-infinitives vs "ce"-after-par are
COMPLEMENTARY distributions (disjoint contexts) — allophony species, same
as the 47/87 split — NOT polyvalence; the 67-sole-polyvalence law is not
violated (refines the ce47 battery's escalation clause, which said
"second polyvalence" — corrected here). Goes to the 47 battery as a
competing frame; not a verdict.

**Bar E9 (finder discrepancy):** the que/ce finder's "46-85-29 @95"
deliberative-infinitive claim is KILLED iff 46-85-29 = 0 globally and the
actual @95 is 46-29-85.

**Bars E2–E8/E10/E11:** counts re-derived; leads queued; @1031 fenced as
77-adverse.

---

## TESTS

`t = code/crowd16/next-token/test_er.py`.

| # | assertion | got |
|---|-----------|-----|
| 1 | n29 = 45; 29 top-pre of 47: pre_c(47) top = {29:4, 76:4} | |
| 2 | 29-47 = [22,422,1230,1590]; windows | |
| 3 | 29-47-33 = [22,1230] | |
| 4 | 29-40-65 = [291,685,1710] | |
| 5 | 86-29 = [431,1375,1391,1825] (finder cited 86-cells +1) | |
| 6 | 29-89-84 = [274,1376] | |
| 7 | 29-87 = [147,627,1425] | |
| 8 | 29-82-16 = [432,1478] | |
| 9 | 46-85-29 = 0; @95: P[93:99] | |
| 10 | 46-29 = [95,217]; 11-29 = [77,499] | |
| 11 | @1031: P[1029:1036] = [1,3,29,80,77,11,70] | |
| 12 | @1155: P[1153:1160] = [0,92,29,80,17,77,82] | |
| 13 | @274: P[272:279]; @1389: P[1387:1394] (67 fork both ways) | |

---

## VERDICT

**E1 47="se" after infinitives — LEAD (competing frame for the 47 battery).**
29 is joint-top predecessor of 47 (4/28, tied with 76) — re-derived;
29-47 ×4 [22,422,1230,1590] and 29-47-33 ×2 [22,1230] re-derived exact.
@22 = [82,43,29,47,33,55,81] ("[43][inf] se [inf]"), @1230 =
[82,48,29,47,33,29,85] ("[48][inf] se [inf]er"). The "se"+infinitive reading
("faire se + inf" / pronominal infinitive) beats "ce"+"[inf]" (marginal)
head-to-head — but both are strained, so this is a LEAD, not a value claim.
Taxonomy (refines ce47's escalation clause): "se"-after-infinitives vs
"ce"-after-par are COMPLEMENTARY (disjoint contexts) — allophony species,
like the 47/87 split — NOT polyvalence. The 67-sole-polyvalence law is not
violated. The 47 battery gets a genuine two-frame competition: "ce" (par-
frames, @548 conditioned) vs "se" (infinitive frames). Queued: 47-predecessor
distribution test (is 29/33/86 over-represented vs chance?) + 47-33 bigram
battery.

**E9 discrepancy — KILLED.** 46-85-29 = 0 globally (re-derived); the actual
@95 is [81,97,46,29,85,8,21] = 46-29-85 ("que-er-85", null-stem anomaly —
see below). The que/ce finder's "46-85-29 deliberative infinitive @95" claim
is VOID — do not test, do not cite.

**E2 29-40-65 ×3 — LEAD (finite-verb frames).** Re-derived [291,685,1710];
twice after 64="qui" ("qui [V]ère [65]" — "considère/préfère"-shaped finite
3sg, not infinitive). Consequence stands: 29's followers split infinitive
vs finite — the stem battery must not assume every 29 is an infinitive
ending. 65 = direct-object slot — queued.

**E3 29-80 — fork CONFIRMED, battery queued.** @1155 = [0,92,29,80,17,77,82]
("[inf] [80] fois" — determiner/quantifier, clean) vs @1031 =
[1,3,29,80,77,11,70] ("[inf] [80] le la" — broken). 80-distribution battery
queued (before 17 / before 77 / elsewhere). **@1031 is a fenced adverse for
77="le"** (P11): "[verb]-le la" ungrammatical unless enclitic+break —
77's promotion battery must resolve it.

**E4 67 fork — corroborated both directions.** @274 = [67,33,29,89,84,91,37]
("veut [33-29]" — "veut demander", veut-reading) and @1389 =
[16,6,29,67,86,29,89] ("[inf] et [86]-er" — parallel infinitives,
et-reading). The settled "sole true polyvalence" holds at byte level; the
fork resolves per-window.

**E5 86-29 ×4 — LEAD (86 infinitive-stem).** Re-derived [431,1375,1391,1825]
(finder cited 86-cells +1). 86 takes "er" like 33 — feeds the 86 battery
(and the stem-finder: name the 86-verb).

**E6/E7/E8 — queued/constraining.** 29-89-84 ×2 [274,1376] (89-84 bigram
battery). 29-87 ×3 [147,627,1425] ("[inf] ce", never "ce que" — constrains
87's post-infinitive frames; "ce+ noun"/"ce qui" readings). 29-82-16 ×2
[432,1478] ("[inf] m' [16]" — 16 vowel-initial profile queued).

**E9b null-stem anomaly — queued.** 46-29 ×2 [95,217] ("que-er": @95 =
46-29-85; @217 = ?), 11-29 ×2 [77,499] ("la-er": @499 = 47-11-29 — the
cela-flagback window; @77 = ?). "er" with no stem — word-initial "er-"
after elided determiner ("l'er[reur]") is the lead hypothesis for 11-29;
46-29 stays anomalous.

**E10 no masculine "premier" — CONFIRM** (consistent with i-beat: 0× without
40).

**Queued:** 47-predecessor distribution + 47-33 bigram (the "se" frame);
65 direct-object profile; 80-distribution battery; 89-84 bigram; 16
vowel-initial profile; 29-after-determiner distribution (46-29/11-29).
