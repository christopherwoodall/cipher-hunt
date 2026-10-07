# PRE-REGISTRATION — 67-FINISHER (round 9, 2026-10-07)

Task (STATE.md WO4): classify the 9 open 67 windows; rule on @1248
("pour 67 que", NEITHER et nor veut); coordinate with the 62-resolver
without duplicating its work.

Standing: `code/crowd7/morphologist/battery67_final.json` — rules R_et1..6,
R_veut1..3, plus the R_et5 fence (does not fire when pre in {21,11}).
Era: Nesselrode v8, lane tokenizer verbatim (lowercase, elision-split,
`[a-zà-ÿ]+`; corpus = 97 dateline-split docs, NW=92,123 — same split as
`code/crowd8/ratemodel/ratemodel.py::split_nesselrode`). Fork re-scope needs
its own ≥2-leg bar (not attempted). PACKAGE only — red team adjudicates.

## Bar N1 — NEITHER-class fence (genuine fork exception)

- F1: window byte-verified in the repaired 1,847-pair parse
  (`code/side-keyhunt/repaired_offsets.json` via `load_pairs_repaired`).
- F2 (era, v8): BOTH fork arms score exactly 0 in the conditioned frame:
  - @1248, frame "pour 67 que" (cond: 00="pour" STRONG LEAD F54, 46="que" GT):
    n("pour et que")==0 AND n("pour veut que")==0.
  - @199, frame "l' 67" (cond: 08="l'" LEAD F61; tokenizer splits elisions so
    "l'"→"l"): n("l et")==0 AND n("l veut")==0.
- F3: no new-arm bar fires at the window this round. New-arm census for @1248
  (pre-registered): era "pour * que" trigram middles; attempt new arm (a)
  only if some single-syllable X has n≥2 (threshold fixed now).
- Pass = F1∧F2∧F3 → recommend NEITHER fence. @1248 unconditional;
  @199 conditional on 08="l'" holding.
- 62-conditionality (pre-registered): @1248's fence is additionally recorded
  CONDITIONAL pending the round-9 62-resolver N35 battery (RULINGS-FINAL
  WO-3). The fence legs do not involve 62; no on/il tests are run here
  (no duplication of the resolver's work).

## Bar E2 — @630 conditional-et (new rule candidate)

Conditions: (C1) 08="l'" (LEAD F61) holds at @631; (C2) 67 is a standalone
word at @630 — i.e. 78 is NOT the clitic "me" attaching forward (under the
clitic-"me" reading n("ce me et")=n("ce me veut")=0, so @630 would be
NEITHER instead; pre-registered as the competing conditional).
- L1 (era v8, frame "67 l' X"): n("et l")==E_et, n("veut l")==E_veut.
  Pass iff E_et ≥ 20 AND E_veut ≤ 3 AND E_et/E_veut ≥ 10
  (order-of-magnitude asymmetry, same leg-kind as the battery's
  196:0 / 185:2 / 38:1; article-vs-pronominal "l'" conflation disclosed).
- L2 (cipher contact, GT-anchored): n(11→52) ≥ 2 — 11="la" GT, so 52 is
  nominal, favoring the article-parse "et l'[52-noun]" over the
  pronominal+infinitive parse "veut l'[52]".
- Pass = L1∧L2 → recommend et-CONDITIONAL on (C1∧C2). C2 is not resolvable
  from current evidence → the recommendation carries the explicit condition;
  red team rules whether it stands or @630 stays open-residual.

## Open-residual default

Any window firing no standing rule and no pre-registered bar above →
open-residual, with reason and any single-leg lean recorded UNSCORED
(a lean is not a classification).

Pre-registered expectations (design, not results): @633, @902, @1372, @1450,
@1623, @1519 expected open-residual — no ≥2-leg bar could be designed.
Recorded leans (unscored): @1519 L1-only 63:1 et-lean (31's class
contradictory: "la 31" 1× vs "qui 31" 2×); @1450/@1623 suc==33 contact
3/3 et on classifieds (@272/@1148/@1476) but all three fired R_et1
independently — confounded, not a bar; @1372 shares the "16 91 67" frame
with @1519 — observation only; @902 n("et i")=n("veut i")=0 but "i"-as-word
unestablished — no fence.

## Design-time null (not attempted)

R_veut4 (pre==78 → veut via clitic-"me" grammatical kill) DROPPED at design:
v8 n("me et")=0 AND n("me veut")=0 — both arms dead under the clitic
reading, so no kill leg exists. The suc-side 67→78=veut ×4 (R_veut2,
"veut me"-frames) does not transfer across direction: suc-side "me" is the
object of a following infinitive ("veut me [V]"), pre-side "me" would be a
forward-attaching clitic — different syntax. Recorded as a null, per the
lane's nulls-are-results convention.
