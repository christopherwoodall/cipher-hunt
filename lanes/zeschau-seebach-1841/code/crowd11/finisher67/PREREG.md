# PRE-REGISTRATION — 67-RESIDUAL FINISHER round 11 (work order 4)
**Executor:** 67 RESIDUAL FINISHER
**Timestamp: 2026-10-07 (written before any round-11 computation; only standing/recorded numbers consulted)**

**Task:** STATE.md round-11 WO-4 — attack the 6 open-residual 67 windows
(@633, @902, @1372, @1450, @1519, @1623) with the explicit missing legs named
in round 10 (F74). For each: supply the leg, or record a clean null naming
what would have supplied it.

**Standing record (not re-derived):**
- Repaired 1,847-pair parse (`code/crowd4/repaired_parse.py::load_pairs_repaired`).
- Era: Nesselrode v8, lane tokenizer verbatim (vendored round-9/10 copy; NW=92,123).
  Rate bars use Nesselrode v8 only.
- Board: GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
  provisional 87=ce, 64=qui, 96=par, 59=est (ISLET 10 conditioned),
  77="le" (conditioned); leads {93,8}="l'", 06="ent"-iff-82, 00="pour" (strong),
  16="i", 47="ce", 78="er"-fork.
- 67 fork: SUPPORTED, amended scope (fenced n=2: @1248 NEITHER, @199
  NEITHER-conditional-on-08). 29/38 classified (et 18 / veut 11),
  @630 et-CONDITIONAL(C1∧C2), 6 open-residual (F74, adjudicator GRANT).
- Round-10 bars E3/E4/E7 and all their numbers (results_r10.json) stand as
  the baseline; this round only ADDS the missing legs, never re-runs a
  passed/failed bar to move its number.
- **33's class (WO-3, parallel): OUTCOME AVAILABLE** —
  `code/crowd11/census33/census33_results.json`, verdict **"C1-infinitive"**
  (I1=8 "pour"+33, p≈0; I4=5 33+"er", p=0.0002; nominal kinds ~null).
  NOT yet red-team adjudicated (docket open) — used as decider input with
  that caveat marked. NOT re-censused here (no duplication); two headline
  counts spot-verified only (V-33x below).
- @1248: WO-5's work; not touched (no re-litigation of F73).
- No re-litigation of settled kills (STATE.md WO8 / red-team docket list).
- No manual-tiling bearing counts (F59 ban). All counts are programmatic
  bigram/census counts on the repaired parse, same instruments as round 10.

## Classification bar (inherited, unchanged)

et-CONDITIONAL iff F0 (byte-verify) + L1 (era conditioned frame:
E_et ≥ 20 AND E_veut ≤ 3 AND (E_veut == 0 OR E_et/E_veut ≥ 10)) +
L2 (n(11→W) ≥ 2, W = frame's unknown content word, 11="la" pencil GT).
C1 (lead-condition) / C2 (67 standalone, no clitic interference) marked
explicitly. A conditional is NOT a classification. Red team adjudicates
every status change — this package is a recommendation.

**Board-grade** (for 52/63/92/16 readings): era-attested in Nesselrode v8
AND grammatically coherent in the window. Class-level readings count if
both conditions are met with ≥2 independent legs; value-level readings
need the same. Frenchman register check applied to every French claim
(diplomatic register: formal administrative; post-1835 orthography;
"ne" never dropped; no slang/« ça »).

---

## R-1519 — 31's second leg
Window (F0-verified round 10): 1517:11, 1518:91, 1519:67, 1520:08, 1521:31.
Frame "X l' 31" (C1: 08="l'" lead). E3-L1 PASSED (63:1). Missing: L2.

- **V-1519a (recount L2):** n(11→31) on the repaired parse.
  Leg supplied iff ≥ 2. (Round-10: 1.)
- **V-1519b (31's class — resolves the verbal-vs-nominal contradiction):**
  full contact census of every 31 position (predecessors + successors).
  Nominal-licensor set: pre ∈ {11 (GT), 08 ("l'"-lead), 77 ("le"-prov-cond, C1),
  96 ("par"-prov, C1)}. Verb-licensor set: pre ∈ {64 ("qui"-prov, C1),
  00 ("pour"-strong-lead, infinitive governor → verbal), 46 ("que"-GT,
  verb-frame only)}. 31=NOMINAL-CLASS iff ≥2 distinct nominal-licensor
  contacts; 31=VERBAL-CLASS iff ≥2 distinct verb-licensor contacts.
  A NOMINAL verdict with ≥2 legs supplies the missing leg (independent
  second leg for 31's nominal class). A VERBAL verdict records the adverse
  (contests the et-lean; favors "veut l'[31]" — lean only, no veut-bar
  exists). Mixed/single → clean null, contradiction unresolved.
- Record as context (not legs): n(64→31) [round-10 adverse: 2], n(08→31).

## R-1372 — denser era frame
Window: 1370:16, 1371:91, 1372:67, 1373:98, 1374:00. Frame "X 98 pour"
(C1': 00="pour" strong lead). E4-L1 FAILED (11 < 20; veut 0). Missing:
a denser era frame (E_et ≥ 20, E_veut ≤ 3, ratio ≥ 10 or veut=0).

- **V-1372a (recount):** verify E_et("et * pour")=11, E_veut("veut * pour")=0,
  n(11→98)=0. (Verification only.)
- **V-1372b (denser frame, bare bigram):** L1' = n("et pour") vs
  n("veut pour") in Nesselrode v8 (same tokenizer). Pass iff E_et ≥ 20,
  E_veut ≤ 3, (E_veut == 0 OR E_et/E_veut ≥ 10).
  FENCED-CONDITIONAL by construction: the window is 67-98-00, so the bare
  frame applies only if 98 does not intervene as a separate word (98
  merges with 67/00 or is non-lexical — 98's class unknown). A pass is a
  fenced-conditional datum, NOT a classification. Frenchman check:
  "et pour [NP]" is the common diplomatic construction ("et pour la…");
  "veut pour" needs era-zero/near-zero.
- **V-1372c (98's contact census):** all 98 positions (pre/suc). Any
  GT-anchored nominal contact recorded. Leg supplied iff n(11→98) ≥ 2
  (the standing L2). Else record counts; clean null on L2.
- No other unfenced frame is designable (91 unknown; 16="i"-unit is not a
  word — no left conditioning; right side fixed by C1'). If V-1372b fails
  or stays fenced and V-1372c is null → clean null: the missing leg remains
  an unfenced denser era frame for "X 98 pour".

## R-633 — board-grade 52/63 + era frame
Window: 631:08, 632:52, 633:67, 634:63, 635:74.

- **V-633a (era frame, left-conditioned on 08="l'" lead):**
  L1 = n(["l", *, "et"]) vs n(["l", *, "veut"]) in Nesselrode v8
  (tokenizer maps "l'" → "l"; * = any single middle word).
  Pass iff E_et ≥ 20, E_veut ≤ 3, (E_veut == 0 OR E_et/E_veut ≥ 10).
  L2 = n(11→52) ≥ 2 (standing: 3 ✓ — not re-derived, cited).
  C1: 08="l'" lead. C2: 67 standalone (pre=52 does not merge).
  Verdict if L1 passes: et-CONDITIONAL(C1∧C2).
  Frenchman check (pre-registered): "l' X et" — article+noun ("l'homme et…")
  or pronoun+verb ("je l'appelle et…"), both diplomatic-register clean.
  "l' X veut" — article+noun+veut ("l'enfant veut") clean; *"je l' X veut"
  ungrammatical (object pronoun cannot be split from its verb) so the
  veut-arm counts article-frames only — the rate comparison is still the
  honest test (both arms grammatical, density decides).
- **V-633b (52's second nominal leg):** n(08→52) ≥ 2 → independent second
  leg for 52's nominal class (article contact "l' 52", independent of
  11→52 ×3). Board-grade for 52's CLASS: era "l' [noun]" frame + grammatical
  "l' 52" in-window. (Value-level 52 reading not attempted — class is the
  named missing leg.)
- **V-633c (52="pas" grammatical check AT @633, window-scoped):**
  "l' pas et/veut" — "pas" precedes the verb slot; French negation wraps
  the finite verb ("ne l' [V] pas") or precedes infinitives ("ne pas [inf]").
  67 is et/veut (not an infinitive slot for "ne pas"). Check @625–631 for
  94="ne" (negation frame). If no "ne" licenses a pre-verbal "pas", then
  52≠"pas" AT @633 (window-scoped coherence datum; NOT a global kill —
  F33's conditioned polyvalence stands). Frenchman check: diplomatic
  register never drops "ne" (standing).
- **V-633d (63's class):** full contact census of every 63 position.
  Nominal iff ≥2 distinct nominal-licensor contacts (same sets as V-1519b);
  verbal iff ≥2 distinct verb-licensor contacts. Board-grade iff the class
  is era-attested AND grammatically coherent in "67 63 74"
  (under 67="et" conditional on V-633a: "et 63 74"; else assessed under
  both arms). Value-level reading attempted only if class resolves with
  ≥2 legs AND a specific era value fits the contacts.

## R-902 — board-grade 92/16
Window: 900:16, 901:92, 902:67, 903:16, 904:88.

- **V-902a (92's class):** full contact census of every 92 position.
  92=NOMINAL iff ≥2 distinct nominal-licensor contacts
  ({11 GT, 08 "l'"-lead, 77 "le"-prov-cond C1, 96 "par"-prov C1});
  92=VERBAL iff ≥2 distinct verb-licensor contacts
  ({64 "qui"-prov C1, 46 "que"-GT verb-frame, 00 "pour"-strong-lead}).
  Board-grade iff era-attested in Nesselrode v8 AND grammatically coherent
  in "16 92 67 16 88".
- **V-902b (16's word-status):** 16="i" is a standing lead (single-letter
  unit). The named missing leg was "establishment of 16 as the word 'i'".
  Frenchman pre-check: French has no lexical word "i" (it is a letter
  name; diplomatic register has no "i"-word). A NEITHER-bar via
  n("et i")=n("veut i")=0 is therefore unmeetable by linguistic fact.
  Verdict rule: clean null with reason UNLESS the census finds 16 in a
  word-position signature (≥2 word-frame contacts, e.g. 46→16 "que"-clause
  or 11→16 article — either would force re-examination of the lead, which
  is then referred, not asserted here).
- **V-902c (era frame):** no board WORD is adjacent to 67 (92 unknown;
  16="i"-unit is not a word; pre2=16, suc2=88 unknown) → no conditionable
  frame. Design null confirmed by construction; recorded, not computed.

## R-1450 / R-1623 — 33's class decider (WO-3 outcome used)
Windows: @1450: 59-36-67-33-46; @1623: 78-66-67-33-46. Frame "X 33 que"
(46=que GT). E7-L1 FAILED (16 < 20; veut 2; ratio 8 < 10); L2 FAILED (0).

- **V-33a (decider application):** WO-3 verdict = C1-infinitive (red-team
  pending — caveat marked). F74 decider: infinitive → veut lives.
  Spot-verify two headline counts only: n(00→33) [=I1] and n(33→29) [=I4]
  on the repaired parse (verification, not a re-census).
- **V-33b (recount E7):** verify L1 (16:2) and L2 (0) — verification only.
- Decider consequence (pre-registered): 33=infinitive ⇒ the veut-arm is
  alive at @1450/@1623 ("veut [inf] que" grammatical; era "veut prouver
  que" attested per census33; in-cipher parallel "veut 33-er" @1423–1425
  with 67=veut-classified). The et-arm is NOT established (E7-L1 fails).
  NO veut-classification bar exists (none pre-registered in any round;
  designing one now would fit known data) ⇒ windows stay open-residual
  with the decider applied. What would classify: a pre-registered,
  red-team-approved veut-arm bar (era "veut [inf] que" frame + cipher leg),
  or 33's class adjudicated otherwise.
- 36 (@1450) and 66 (@1623) alternative routes: examined only for bar
  viability (bounded); 66-class is CONFIRMED broad (noun/infinitive/
  nous-vos) — narrowing it to nous/vous for an agreement kill is a new
  battery, out of scope for this finisher; recorded as not-attempted with
  the missing leg named.

## Fork status
Re-verify tally from battery67_final.json + round-9/10 overlays:
29 classified (et 18 / veut 11), @630 et-CONDITIONAL, 6 open-residual,
2 fenced (@1248, @199). Expected: unchanged → fork stays SUPPORTED with
amended scope (fenced n=2); @1248 = scope amendment (F73).

## What counts
- Leg supplied: pre-registered bar passes on repaired parse + Nesselrode v8.
- Window classified: full ≥2-leg bar passes (et-CONDITIONAL only; no
  veut-bar exists).
- Else: clean null with the exact missing leg named.
- Single-leg leans stay unscored. All status changes are recommendations
  for red-team adjudication.
