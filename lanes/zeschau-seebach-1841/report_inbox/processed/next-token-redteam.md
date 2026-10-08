# Round-16 red-team adjudication: next-token battery verdicts

Adjudicator: red team, kill authority. Date: 2026-10-07.
Scope: all 16 round-16 batteries (`code/crowd16/report_inbox/next-token-*.md`,
each with PRE-REGISTRATION + TESTS + VERDICT) and their 16 finder reports.
Stream: repaired 1,847-pair parse. All cipher-side numbers below re-derived
by the red team independently (`code/crowd16/next-token/streamkit.py`).

Method: (1) pre-registration integrity checked; (2) key numbers re-derived;
(3) the 77="le" promotion attacked through the runner's two self-critique
gaps first; (4) demotion evidence verified, not just original promotions;
(5) the 78 kill attacked via the positional-allophone escape hatch.

## Pre-registration integrity — INTACT (R16-032)

16/16 batteries state bars before data. No post-hoc bars found. The two
within-round revisions (45 PROMOTE->HOLD; tout B4 adverse correction) are
transparently recorded in both affected reports. The forks K3 bar openly
adjudicates a within-round conflict — that is transparency, not cheating.

## Rulings

### The promotion

**R16-001: 77="le" provisional→promoted — DEMOTE (promotion not granted).**
77 stays PROVISIONAL. The "le la" adverse is DISSOLVED (three windows
re-derive with natural parses: @832 cela-boundary, @1034 clause-boundary,
@1042 article+pronoun — byte windows verified exact), so the
"provisional-conditioned" qualifier drops. But bar L1(b) required "≥2
INDEPENDENT 'le' legs on banked values" with conditional legs explicitly
excluded — and all three legs are conditional:
- @832 "En cela, le [76]": anchor 87-11="cela" banked, but needs 76=noun
  (unbanked; gender-tensioned by "la [76]" @1046, R16-029) and 24="en"
  (lead). 59@834 is LEFTOVER, so the leg is "le [76]", not "le [76] est".
- @516 "ce le [80]": anchor 87="ce" banked, but needs 80=verb. 80 has a
  CLEAN determiner leg (@1155 "[inf] [80] fois") against the verb reading;
  the verb reading is the weaker hypothesis.
- @870 "ce le [89]": anchor 87="ce" banked, but needs 89=verb. 29-89 ×5
  (89 after infinitives) tensions the verb reading, conditional on 93/86
  stem-hood (untested prediction).
Worse: the round-15 ledger banked 80/89 verb-frames as CONDITIONAL ON
77="le" (LEDGER15: '80'/'89' verb-frame PROMOTED conditional on 77="le").
The battery used those frames as independent legs for 77="le". That is
circular: A→B→A. The runner's self-critique flagged the gaps but promoted
anyway; the pre-registered bar binds. Bar L1(c) is also soft: @1031's
enclitic+break fence needs 80=verb (same circularity).
Promotion docket (to earn "promoted"): 76-noun battery + 80/89-verb
battery must resolve in favor; then any two of @832/@516/@870/@1042
upgrade to clean legs.

### Demotions and weakenings

**R16-002: 84="on" WEAKENED — GRANT.** The "84→59 ×4 (on est)" legs are
VOID: class(59@1190)=ESTE, @1291=FENCED, @1448=ESTE, @1804=ESTE, re-derived
from `code/crowd10/conditioner59/classification.json` (kill-grade ISLET-10;
the round-15 battery never checked — genuine scope gap). 13
59-independent legs stand intact: "l'on" ×7 [145,259,1057,1446,1484,1763,
1802], "qu'on en" ×2 @309/@472, "mon" @166 (82-84), 84→24 ×3. The grant
survives on its discriminating core, minus the whole "on est" family.

**R16-003: 37/42 predicative frames → HOLD — GRANT (both).** Enforces A1's
own bar (clause (a): ≥2 conditioned "est X" legs) against kill-grade
ISLET-10. 59→37 ×6: all LEFTOVER. 59→42 ×2: LEFTOVER + ESTE. Zero valid
legs → the grants fail their own clause (a) → HOLD (unanchored, not
killed). 32's frame STANDS at 2 EST legs (@316/@1210; @448 ESTE correctly
excluded). 19 HOLD confirmed at 1 genuine EST leg (@1777). Ranking: 32 >
19 > 30 (ne-lead) > 39/45 (1 leg each) > 42 > 37. Note the runner's honest
flag: 32 stands on exactly 2 legs, both leaning on provisional 94/48.

**R16-004: 45="ce" PROMOTE→HOLD (within-round revision) — GRANT.** "ce
verdict" ×2 (@573: 87="ce" banked + 78-45; @982: 47="ce" granted + 78-45)
forces 45="dict" (syllable) — "ce [78] ce" is ungrammatical. "par ce" ×2
(@602/@1213: 96="par" promoted) forces 45="ce" — "par dict" is
ungrammatical. Two values in complementary distribution ("dict" only
after 78, ×4; "ce" elsewhere) → positional allophony, lane-precedented
(47/87). The par-rest promotion was granted without weighing the forks
finder's "verdict" ×4 — correctly revised. **45 "ce/dict" LEAD**,
conditional on 78="ver" (R16-005).

### Kills and declines

**R16-005: 78 "er" KILLED distributionally — GRANT.** Determiner
predecessors: 78 16/31 vs 29="er" 2/45 (OR=22.93, re-derived). After
33=INF: 78 0 vs 29 5. The positional-allophone escape (78="er" as 29's
allophone, cf. 47/87) fails on grammaticality, not distribution: "ce 78"
×7 [363,572,628,818,981,1104,1396] is ungrammatical under "er" ("ce"+"er"
has no elision save; word-internal "cer-" would re-litigate the granted
47/87 word values). "le/la 78" ×9 are elision-compatible and do not
discriminate. **78="ver" LEAD** (surviving arm; "verdict" ×4 word-level
support) — correctly graded LEAD, not settled. CORRECTION TO THE
VERDICT: @296 [16,1,11,78,40,97,86] ("l'ère"-shaped) votes "er" and was
not fenced — it is now a FENCED RESIDUAL adverse for 78="ver" (1
window). The la-battery's "positional allophony (er before 40-type)"
escape is REJECTED under lane law (67 sole polyvalence).

**R16-006: 94="ne" PROMOTE declined → STRONG LEAD — GRANT.** "n'est" ×3
@558/@762/@1795 (conditional on 59="est" provisional), "ne me/m'" ×4
@578/@1182/@1353/@1742 (82="m" banked but continuations strained:
@578/@1182 → doubled 06; @1742 → verbless "ne me que"), 62-94 ×9
(conditional on 62="on" lead), 70-12-94 ×2 "prenne" (conditional on
12="n"). Three conditional legs converging + one independent-strained
leg = STRONG LEAD, not promotion. The decline matches the standard
applied to 77 (R16-001): conditional convergence is lead-grade.

**R16-007: 48="e"-letter DECLINED — GRANT.** No independent legs; the
whole case re-reads A7's 4 granted "me [48]" windows and parses worse
(1/4 possible, 3/4 broken vs the granted frame's 4/4 verb-slot
recurrence). Re-litigation without new evidence — declined. 48's value
stays open.

**R16-008: 84="fait" REJECTED — GRANT.** Re-litigates the A15 grant with
no new evidence. Flagships do not parse: @1189 is 06-84 (no 77, so no
"le fait"); @1447/@1803 "qui le fait est [36/35]" ungrammatical (finder
admits null); "fait est" fails on 59=ESTE (R16-002).

### New leads

**R16-009: 30="pas" — GRANT (LEAD).** Two canonical ne-frame legs:
@559 EST "n'est 30" + @1715 ESTE "ne [44-59] [30]". The 19-window census
("26-30" ×4, "24-30" ×3) is queued, correctly not run here.

**R16-010: 12="n" — GRANT (LEAD).** "prenne/prennent" compositional
(@1547 beautiful: 00/46 banked) + "ni" @1740 (34="i" GT) + 12-48 dual
spelling. Count corrected: 12-48 ×5 [169,709,809,1075,1736], not ×7 —
the correction is material and verified.

**R16-011: 39="a/à" — DEMOTE (LEAD → HYPOTHESIS).** The "qui a" singleton
@606 is actually "qui [39] qui" [64,39,64] — no clean "qui a" frame. The
two 70-39-11 legs are word-internal "pré-a-la" syllables from one word
("préalable"), not independent word-level legs. Fails the pre-registered
"≥2 independent legs" LEAD bar. The "n'est [39]" @763 EST leg supports a
predicative (adjective/noun) reading, not "a/à".

**R16-012: 06="ent/ment" — GRANT (LEAD).** Three "[X]-06 la [NOUN]"
windows (@320/@1123/@1721 re-derived exact); 06→77 ×6, 06→11 ×4
(ending-compatible). Verb-vs-adverb fork stays open — LEAD, not
promotion.

**R16-013: 29-47 "se"-allophone — GRANT (LEAD).** 29 is joint-top
predecessor of 47 (4/28, tied 76); 29-47-33 ×2 "[inf] se [inf]" beats
"ce"+infinitive head-to-head. Complementary to "ce"-after-par →
allophony species (cf. 47/87), NOT polyvalence. Refines (corrects) the
ce47 battery's "second polyvalence" escalation clause. Competing frame
for the 47 battery, not a verdict.

**R16-014: 73="lu" — GRANT (LEAD).** 73-34 ×2 @392/@1347, both
"lui"-shaped before verb-ish groups. Two independent windows — meets
the lead bar.

**R16-015: 33="dire" — GRANT (LEAD).** "67 33 46" ×2 @1450/@1623
idiomatic under BOTH 67 forks ("et dire que" / "veut dire que"); "47 33"
×2 "ce [inf]"; "33 21 64 37" ×2. Promotion correctly BLOCKED by "33 29"
×5 (29-89-84 / 29-82-16 word-shapes puzzle all five candidates).
Candidate scoring (vouloir killed, penser weak) is French judgment on
verified frames — recorded as such.

**R16-016: 86-29 substantivized infinitive — GRANT (LEAD).** "veut le
[86]-er" (@430) is ungrammatical as verb → 86-29 nominal ("le
devoir/pouvoir"-shaped). Converges with 86's INF-class + "par le [86]".

**R16-017: 43 feminine noun — GRANT (LEAD).** "la 43" @562, "par 43" ×2
@342/@1026, "43 pour que" @1544, "43 le" ×2, "37-43" ×3. Value unnamed —
correct.

**R16-018: 65 priority-1 battery target — GRANT (queued).** "e 65 94" ×2
@686/@1711 byte-identical and exclusive (65-94 nowhere else); "65 qui"
×3; top "-ère" follower (3/9). Highest-value unknown — no value named.

**R16-019: 20 feminine noun — GRANT (LEAD).** "la première 20" @760
(feminine-noun slot; 20="fois" killed, 20~17 split) + "pour [20]" @667.
Two legs. The "[20] fois" @309 side stays open (re-examination, not
"fois fois").

### Confirmations

**R16-020: 79="tout" compositional — GRANT (banked stands).** Four legs
re-derived: "toutefois" ×2 @451/@1460 (17 banked), "tout cela" @460
(87/11 banked; 59-leg conditional on 59 provisional — flagged), "tout ce
qui" @1799 (87/64 banked; 77 provisional-conditioned — flagged). The
m-battery's M5 adjudication is ACCEPTED: @396/@1227 are 2 FENCED
strained residuals (qui+tout double-subject; A7 boundary parse strained
by verbless qui-clause), correcting the tout battery's original
"narrow/reducible" weighing. "tous"-range leg lead-grade (conditioned
on 06="ent" lead); 5-gram order corrected to 00-33-79-80-06.

**R16-021: 00="pour" — GRANT (banked stands).** Follower census exact
(86×12, 33×8, 66×7, 92×6, 97×4, 11×4, 46×4, 36×3; singletons incl. the
finder-missed 67). @107 addressed as fork-conditional (votes 67="et"
given 00="pour"; handed to forks battery; direction of conditional on
record). Adverses fenced: @1247 (strongest, 1-window residual), @864
(cheapest decisive test, conditional on 48), @291/@685 (2 new,
"pour"+subjunctive). Rate adverse weighed honestly: 00 = 2.978% of
pairs vs ~0.592% "pour"-syllables in Nesselrode v8 (~5×) — moderate
adverse, joins @1247 in the split battery's docket. Does not kill.

**R16-022: 31=VERBAL class — GRANT (confirmed).** 8 followers, 8/8
distinct {10,11,14,24,29,76,79,92} — class-tier signature (a single word
would show formulaic repeats, cf. 33's doubled 5-grams). Person
undetermined (honest null held).

**R16-023: 67-33 ×6 (was round-11's ×1) — GRANT correction.**
[272,1148,1423,1450,1476,1623]; splits 3/2/1 ("67 33 29" ×3, "67 33 46"
×2, "67 33 66" ×1). Byte-verified.

**R16-024: 26-30 ×4 (was ×3) — GRANT correction.** [655,992,1250,1560];
the 12~30 same-slot pair is 8 windows (26-12 ×4 + 26-30 ×4), not 7.

**R16-025: E1/E2/E3 — GRANT.** 65-94 exclusive collocation ×2
("…ère 65 94…", nowhere else); "20 62 94" ×3 @760/@839/@1703 (20-62 ×4);
"67 77 81" ×4 fork-conditional ("et le [noun]" in-frame; not a global
fork resolution).

**R16-026: F1/F2 absolute construction — GRANT.** "17 11 26" ×2
@238/@1558 + "17 77 82" ×2 @1040/@1157 (77-82 frozen, both post-17).
"le même [44/63]" hypothesis correctly NOT assumed (see R16-030).

**R16-027: 46-85-29 = 0 (finder discrepancy killed) — GRANT.** The
que/ce finder's "46-85-29 deliberative infinitive @95" is VOID; @95 is
46-29-85. Do not cite.

### Escalated items (ruled where evidence permits)

**R16-028: @369 "pre fois" 70-polyvalence — (b) REJECTED; anomaly stays
fenced.** [61,70,17,6,21,65,63]; 70-17 sole in 70's distribution.
70="pre" is Tier-0 pencil GT and 67 is the sole true polyvalence —
70-polyvalence is lane-law-forbidden without kill-grade evidence, which
one window does not supply. Options (a) idiom/boundary and (c)
misassignment stay open; the "49 61" frame-search battery is the next
step.

**R16-029: 76 gender tension — NO RULING (insufficient evidence).**
"le [76]" ×3 (@832/@891/@968) vs "la [76]" @1046, where @1046 also
admits "la"+verb (76 verbal). Stays queued for the dedicated 76
battery. NOTE: this conditionality is load-bearing for 77's promotion
docket (R16-001).

**R16-030: "le même [44/63]" 82-polyvalence — "même" REJECTED.** 82="m"
is Tier-0 crib proof; a second value violates the 67-sole-polyvalence
law. "le m[44/63]" stays unresolved (boundary / "M." / other readings
open) pending the 44~63 same-class battery. The fois battery was right
not to assume it.

**R16-031: 84 -este-verb vs "on" tension — REAL, UNRESOLVED; fenced, not
ruled.** Kill-grade ESTE classification puts 84 inside 3-syllable -este
verbs at 4 windows ([06-84-59] @1189; [84-59] @1447/@1803; fenced
@1291) — a verbal-syllable use conflicting with pronominal "on". This
does not kill 84="on" (13 59-independent legs stand, R16-002), and
84-polyvalence is NOT granted (lane law). The 4 windows are FENCED as
84-residuals (84's value there not established as "on"). Resolution
belongs to the 62/84 collision battery, which inherits this tension.

## What the runner got wrong

1. **Promoted 77="le" on a failed bar (R16-001).** The pre-registered
   L1(b) excludes conditional legs; all three legs are conditional, and
   two lean on 80/89 verb-frames that the round-15 ledger itself marks
   conditional on 77="le" (circularity). The self-critique named the
   gaps but the verdict promoted anyway.
2. **Missed the 29-89 ×5 / 29-80 ×4 counter-evidence (R16-001).** 89
   after infinitives ×5 tensions 89=verb (conditional on untested
   93/86 stem-hood); 80 has a CLEAN determiner leg (@1155) against its
   verb reading. The "ce le [80/89]" legs need the weaker reading in
   both cases.
3. **Forks K2 left @296 unfenced and the polyvalence escape unrejected
   (R16-005).** "l'ère" is a genuine "er"-voting window; it is now a
   fenced residual, and the "er/ver positional allophony" escape is
   rejected under lane law.
4. **Overgraded 39="a/à" to LEAD (R16-011).** Fails the ≥2-independent-
   legs bar; the "qui a" singleton does not parse cleanly.
5. Cosmetic: finder bigram-vs-cell index wobbles (ce47, classes, m,
   tout reports) — all resolve to identical physical cells; no verdict
   impact. The tout battery's original B4 weighing was already
   corrected within-round by M5.

## Baseline extension totals

- `code/crowd7/redteam/verify_f26_17.py`: **357/357 PASS** (305 prior +
  52 new R16BANK cipher-side checks, all re-derived by the red team).
- `code/crowd7/redteam/verify_round7.py`: **196/196 PASS** (181 prior +
  15 new ROUND16-LEDGER status/drift checks).
- 16/16 round-16 battery test scripts pass (unchanged).

## Scoreboard delta (round 16)

Promotions: **0** (sole claimed promotion demoted). Demotions: 77
promotion→provisional; 37/42 frames→HOLD; 45→HOLD; 39 LEAD→hypothesis.
Kills: 78 "er"; 84="fait" (rejected); 46-85-29 finder claim. Confirmed:
79, 00, 31-class, E1/E2/E3, F1/F2, 84 weakened-not-demoted. New leads:
30, 12, 06, 29-47 "se", 73, 33, 86-29, 43, 65 (queued), 20, 45
"ce/dict" (conditional). Escalations held: 76, 84/-este/ tension.
