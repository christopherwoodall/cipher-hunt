# Round-16 battery: tout (79) — compositional verification + adverse weighing

Finder report: `code/crowd16/report_inbox/next-token-findings-tout.md` (ingested 2026-10-07).
Stream: repaired 1,847-pair parse, start-index convention.
Status entering: 79="tout" is BANKED (round-15 A5, red-team GRANT). This battery
VERIFIES compositionally; it does not re-promote.

---

## PRE-REGISTRATION (locked before formal tests; bars precede numbers)

**Scope note:** the finder's "4 solid legs" rest on windows already verified in
round 15 (@451, @1460, @460, @1799). This battery's job: (a) re-derive them
independently; (b) test the NEW claims (@496 weak leg, "tous"-shaped 5-grams,
null windows as constraints); (c) weigh the 79-82-48 adverse EXPLICITLY —
it is the battery's load-bearing requirement, not an appendix.

**Bar B1 — compositional CONFIRM (strengthens banked value):**
≥2 INDEPENDENT compositional windows that parse cleanly on BANKED values only
(87=ce, 17=fois, 11=la, 59=est provisional, 64=qui, 82=m), with ZERO new hard
contradictions across the full 18-window census.
Kills: ≥1 window where every neighbor is banked and no grammatical parse
exists under "tout"/"tous".

**Bar B2 — "tous" inflectional-range leg (conditioned):**
CONFIRM-conditioned iff: (i) 33-00-79-80-06 is byte-identical ×2 (@468/@1089);
(ii) 80 is verb-locked (banked A8: post-"er"×4, pre=29×4 — banked, not
re-litigated); (iii) the plural-agreement reading ("tous [80]ent") rests on
the 06="ent" LEAD, not a banked value — so this leg is LEAD-GRADE, cannot
stand alone as promotion-grade evidence. Inflection ≠ polyvalence (tout/tous
= one lemma); the 67-fork "sole polyvalence" claim is untouched.

**Bar B3 — weak leg @496 (79→88-47-11):**
HOLD unless 88's class is independently constrained. "tout [88]" needs 88
nominal/adjectival; 88 unresolved → cannot confirm, cannot kill.

**Bar B4 — adverse 79-82-48 ×2 (@396/@1227):**
KILLS the tout story iff a window's core fails grammatical French under BOTH
"tout" and "tous" (core = "tout/tous m'"+verb — 48 verb-stem-shaped is
banked-adjacent: "m'[48]"×4, 48→29×2). Otherwise the adverse is WEIGHED:
real but narrow iff the residual is reducible to 67/57/48 resolution.

**Bar B5 — nulls:**
Recorded as constraints, not forced. Null is a result.

---

## TESTS

`t = code/crowd16/next-token/test_tout.py` — every count below is asserted
there; failures abort the battery.

| # | assertion | got |
|---|-----------|-----|
| 1 | n79 = 18 | |
| 2 | 79→17 starts = [451, 1460] | |
| 3 | 79→87→11 start = [460] | |
| 4 | 79→87→64 start = [1799] | |
| 5 | 79→80 starts = [468, 1010, 1089] | |
| 6 | 33-00-79-80-06 ×2 byte-identical @468/@1089 | |
| 7 | 79-82-48 starts = [396, 1227]; @396 full 6-mer = [67,64,79,82,48,6]; @1227 = [57,64,79,82,48,29] | |
| 8 | @496 = [94,2,79,88,47,11] (79→88-47-11) | |
| 9 | all 18 window starts = [50,53,396,451,460,468,496,594,883,1010,1089,1227,1364,1419,1460,1682,1688,1799] | |
| 10 | @1010 tail 79-80-78: full = [35,18,79,80,78,47] | |
| 11 | 79→14 ×2 = [1364, 1688] (identical bigram claim) | |
| 12 | "tout en"/"tout à coup" proxies: 79→24 count and 79→92... | |

---

## VERDICT

**B1 compositional CONFIRM — GRANTED.** All four windows re-derived exact and
parse on banked values only: @451/@1460 "toutefois" (17=fois banked),
@460 "tout cela est" (87=ce, 11=la banked; 59=est provisional — the 59 leg is
conditional on 59's provisional status), @1799 "tout ce qui [le…]" (87/64
banked, 77="le" provisional-conditioned). Zero hard contradictions across the
full 18-window census. This STRENGTHENS the banked 79="tout" — it does not
re-promote it (already banked; no double-promotion).

**B2 "tous" inflectional-range leg — CONFIRM-CONDITIONED (lead-grade).**
The 5-gram is byte-identical ×2 @466/@1087 — but the TRUE ORDER is
**00-33-79-80-06**, not the finder's "33-00-79-80-06" (finder transcription
error, corrected and asserted). "pour [33-INF] … tous [80]ent": 80 is
verb-locked (banked A8), and the plural-agreement reading rests on the
06="ent" LEAD (not a banked value) — so the leg is lead-grade, correctly
stated by the finder as "testable either way." Inflection ≠ polyvalence:
the 67-fork "sole polyvalence" claim is undisturbed.

**B3 weak leg @496 — HOLD.** 79→88-47-11 re-derived exact ([94,2,79,88,47,11]
@494); "tout [88]" needs 88 nominal/adjectival — 88 unresolved. Cannot
confirm, cannot kill. The finder's honest grading stands.

**B4 adverse 79-82-48 — CORRECTED (m-beat adjudication, see next-token-m.md
M5): 2 FENCED RESIDUALS, not "narrow/reducible".** Re-derived exact:
@396 = [67,64,79,82,48,6], @1227 = [57,64,79,82,48,29]. The m-finder's
double-subject objection is valid for the single-clause parse ("qui
tout/tous m'[verb]" ungrammatical; corpus: zero "qui tout/tous m'" in
Nesselrode v8 + Guizot t1–t3), and A7's boundary parse ("…qui [X]. Tout me
[48-verb]…") is strained at both windows (the qui-clause is verbless:
@396 "…[73][34][67] qui |", @1227 "…[9][20][57] qui |" — no verb before the
boundary). The "tous m'entourent" grammatical core cited in the first
weighing does not survive the preceding "qui". **@396/@1227 are fenced as
strained residuals for 79="tout" (2/18).** The banked value stands on its 4
compositional legs (none has the "qui"+"tout" problem); A7's L2 frame
(48=verb-stem) is untouched. 79→24 = 0, 79→46 = 0 (no "tout en"/"tout que"
census hits — consistent with a determiner/adverb profile).

**B5 nulls — recorded as constraints.** @50 (79→37: "tout [37]" adjective-slot
datapoint for the 37 verb/adj fight — handoff to the est battery), @53/@594
(79→85 ×2: if 79=tout, 85 must be nominal/adjectival — constraint banked for
the 85 battery), @1364/@1688 (79→14 ×2 identical bigram: "tout [14]" nominal
constraint), @1419 (79→15), @1682 ("que pour tout [65]" weak), @883. @1010
(79-80-78-47: "tous [80]-" tail unresolved — recorded null, not forced).

**Finder corrections (2, both cosmetic to verdicts):**
1. 5-gram order is 00-33-79-80-06, not 33-00-79-80-06.
2. @396 order is 67-64-79, not 64-67-79 (affects the parse header, not the
   grammatical verdict).

No new contradictions. 79="tout" banked status CONFIRMED; "tous"-range added
as a conditioned lead-grade leg; adverse fenced to 67/57/48 resolution.
Weakest leg for self-critique: @460's "tout cela est" inherits 59=est
provisional — if 59 falls, that leg degrades (the other three legs are
59-independent).
