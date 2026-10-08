# Red-team adjudication — next-token battery round (crowd15, round 15)

Date: 2026-10-07. Adjudicator: red team (kill authority).
Scope: all 16 battery reports in `code/crowd15/report_inbox/next-token-*.md`
(A1–A16) + the P1 "cela" confirmation battery. Finder reports
(`next-token-findings-*.md`) are inputs, not verdicts.

Method: (1) bar-before-data structure checked per report and every verdict
tested against its own bar; (2) all key cipher-side numbers re-derived
independently from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` via the lane's own
`code/crowd6/redteam/verify_baseline.load_stream` (1,847 pairs); the runner's
counts are reproduced byte-exact unless noted; (3) corpus legs spot-checked
against `code/side-period/corpus/` (era/register: Nesselrode v8 covers the
full 1841 run — the corpus slice is genuinely 1840s diplomatic; the
era/register failure mode does NOT fire on any corpus leg); (4) the runner's
named weakest legs attacked first.

Headline: the runner's numbers are clean — every material count re-derived
exact. The adjudication is therefore about bars, scope, and collisions, not
arithmetic. One real collision found (84="on" vs the standing 62="on" lead);
four minor runner slips (none verdict-flipping).

---

## Rulings

### VALUE PROMOTIONS

**A15 — 84="on": GRANT-WITH-CONDITIONS** (biggest claim; attacked hardest)
- Bar check: bar was written for "84=clitic (frame)"; verdict upgrades to the
  "on" value. Allowed: the "on"-specific legs ("qu'on en"×2, "mon"@166) pin
  the value, not just clitic-hood. All three bar clauses met.
- Re-derived: 77-84 ×7 @145/259/1057/1446/1484/1763/1802 ✓;
  46-84-24-37-78 byte-identical @309/@472 ✓; 46-77-84-24-87 @1483 (84@1485) ✓;
  82-84 @166 ✓; 84→59 ×4, 84→24 ×3 ✓; R1 11-84 @1619 ✓; R2 94-84 @1664 ✓.
- Discriminating (non-ear) legs, 77-independent: "qu'on en"×2 kills the
  "en" rival ("qu'en en" = 0 in ~27MB of period corpus, ungrammatical) and
  the noun rival ("que [N] en" strained); "mon"@166 ("en mon [53]" ✓ vs
  "en m'en" ✗ — 82="m" is crib-established); cross-arm successor overlap
  (24 and 59 taken in both the 77-arm and the en-arm) supports ONE value,
  unifying F53's split arms.
- On-vs-il (the N35/N39 gap): "l'on"×7 discriminates non-aurally — "l'il"
  is impossible; "l'en" is 8× rarer in the corpus (2246 vs 288) AND dead at
  the "qu'on en" windows. This closes the non-ear gap for 84 specifically.
- **Conditions:** (C1) the 7 "l'on" legs inherit 77="le" provisional — if 77
  falls, they fall (the 77-independent legs carry the value regardless);
  (C2) **the standing 62="on" STRONG LEAD collides** — 62→94 ×9 ("on ne")
  vs 84→59 ×4 ("on est") put two "on" cells in overlapping syntactic slots
  with zero crossover. Both cannot be unconditioned "on". A 62/84 collision
  battery is REQUIRED (leading resolution: 84="on" discriminated by elision;
  62 re-examined, "il" the live rival — "il ne"×9 is clean French). The A15
  battery never mentions the 62 lead: scope gap, recorded.
  (C3) R1 (@1619 "la on") and R2 (@1664 "ne on") stay fenced — genuine
  1/25 residuals; the "non"=94+84 rescue is FORBIDDEN by the registry
  (67 fork = sole polyvalence; 94 cannot be letter-"n").
- Runner's weakest leg ("l'on" frequency over-fit) is real but contained:
  the promotion does not depend on frequency magnitude.

**A4 — 47="ce" (allophone tier): GRANT**
- Re-derived: 87←24 10/32 vs 47←24 1/28 (@548); Fisher p=0.0069 EXACT ✓;
  47→46 ×3 @151/@548/@864 ✓; 87→46 ×3 @225/@953/@1527 ✓;
  47→11 ×3 @269/@357/@498 ✓; 47→77 @611 ✓; tail parity 3/3 vs 1/3 ✓.
- Bar met on its ≤1-shift clause: the single @548 exception parses as
  "en ce que" ("insofar as") — a bonus mirror frame, not a contradiction.
- 28-window contradiction scan: zero hard contradictions (47→33 ×2 is
  "ce"+"[inf]", grammatical; @611 strained, correctly held conditional).
- Notes: the finder's "0×" is corrected to 1× (done by the battery);
  the conditioning rule still needs specification — "par ce que" uses 87
  after 96="par" (3×, banked C1), which the simple "47=ce-after-non-en"
  story does not explain (frozen-formula wrinkle, not a kill).
  Allophone tier only — 47 does not inherit 87's individual legs.

**A5 — 79="tout": GRANT**
- Re-derived: 79-17 ×2 @451/@1460 ✓; 79-87-11 @460 ✓; 79-87-64 @1799 ✓;
  79-80 ×3 @468/@1010/@1089 ✓; full 18-window scan, zero hard
  contradictions, 2 fenced with stated cause ✓.
- Correction to the battery's framing (not its verdict): the "toutefois"
  leg is better read as syllable-inventory ("tout" cell + "fois" cell)
  than as a clerk mute-e elision habit — the lane documents final mute-e
  WRITTEN as its own cell (40="e" in the "première" crib) and has no
  precedent for internal-e drop. The leg survives the re-framing;
  "toutefois" is lexicalized /tut.fwa/.
- A8's "tout 80" pronoun+verb re-read is CONFIRMED (see A8) — 79="tout"
  never needed the noun reading.

**A9 — 00="pour": GRANT (with leg-(1) downgrade)**
- Re-derived: 00→86 ×12, 00→33 ×8 (20/55) ✓; 00-46 @106/@545/@1545/@1680 ✓;
  86: pre=00 ×12, suc=29 ×4 ✓; 33: pre=00 ×8, suc=29 ×5 ✓;
  predecessor spread preposition-like, zero determiner/finite-verb slots ✓.
- Bar (a) met via @1545 ("pour que pre[12]", GT "pre") and @1680
  ("pour que tout [65]"); @106's 67-tension correctly fenced as
  fork-conditional; @545 correctly fenced unparsed.
- **Downgrade:** leg (1) ("dominant pour+infinitive signature") is
  CLASS-level only. The A10-HOLD stem/whole tension means the "pour"+bare
  form of those 20 windows is provisional — if 33/86 are stems,
  "pour"+stem would be ungrammatical. The promotion stands on the
  "pour que" legs + profile, which are independent of the INF morphology.
  The 96-00="par le" islet (F54) is undisturbed (conditioned value).

### FRAME PROMOTIONS (value open)

**A1 — 37/32/42 predicative frames: GRANT (42 weakest, named); 19: HOLD**
- Re-derived: 59→37 @528/624/912/1178/1443/1796 (6) ✓; 59→32
  @316/448/1210 (3) ✓; 59→42 @463/1186 (2) ✓; 59→19 @1777 (1) ✓.
  The finder's "19 ×2" is confirmed as ONE physical window — correction ✓.
- 37: 6 independent legs, successors verb/infinitive/que-class ✓.
  32: 3 legs, 48/94 post-predicate slot shared with 19 at class level ✓.
  42: bar met EXACTLY (2 legs); (b) holds on the global reading
  (94×3, 48×1, 33×1 successors) — @463's "est [42] par" is
  participle-compatible, @1186's 06 feeds the "certain" composition lead.
  No contradictions in any est-window. No merges (the {33,86} standard
  correctly not met for any pair).
- Corpus census figures (vrai 49 etc.) do NOT reproduce exactly on the
  corpus dir (independent count: 37/20/19/14/16/10/6/3) — same order,
  same conclusion (register-typical slot), exact numbers unverified.
  Not verdict-critical.

**A8 — 80/89 verb-frames: GRANT (conditional); DISTINCT: GRANT**
- Re-derived: 87-77-80 @515 ✓; 87-77-89 @869 ✓; 80: pre 29×4/98×3/79×3,
  post-"er" ×4, "tout [80]" ×3 ✓; 89: pre 29×5, suc 48×3/84×2 ✓;
  shared successor classes: ZERO ✓.
- **Conditional on 77="le" provisional** (both C3 windows need it; battery
  states this). Note: A15's "l'on" re-read indirectly SUPPORTS 77="le".
- 80-vs-89 DISTINCT granted (zero shared frames/suc-classes; the
  p=0.0021 successor-distribution gap is driven by real zero-overlap).
- "tout 80"×3 → pronoun+verb re-read CONFIRMED: 80's profile is
  verb-locked (post-"er" ×4, "ce le [80]"), the noun reading has no legs
  left. Correction to A5 recorded.
- Slip (no verdict impact): the printed 89-successor list omits 89→41 ×1
  (counts still sum to n89=14).

**A7 — trigram: L1 (48="est") KILLED; L2 ("tout me [48-verb]") GRANTED
  (frame); L3 EXCLUDED**
- Re-derived: 79-82-48 @396/@1227 (trigram starts; n_eff=1, battery says
  so) ✓; 82-48 ×4 @125/@376/@397/@1228 ✓;
  48→{37,32,35} = 0/38 vs 59→{37,32,35} = 12/27 ✓.
- The kill is clean and distributional: an "est"-homophone would show 59's
  predicative concentration; 48 shows zero of it at n=38. Scope: kills the
  unconditioned "est"-homophone hypothesis; a conditioned "est"-islet for
  48 would need its own legs (none exist).
- L2 granted as FRAME (48 = verb-stem candidate): corpus "tout me/m'+verb"
  is register-real (the finder's "poor French" adverse note is refuted),
  "me [48]" ×4 independent of the trigram, verb-compatible profile,
  "[48]er ce" ×2 (@1229/@1589 ✓). Value NOT promoted. R1/R2 stay open.

**A3 — "parce qu'en" @952: CONFIRM (frame); 85 verb-stem candidate: GRANT**
- Re-derived: 96-87-46 @224/@952/@1526 ✓; tail @952→24 ✓ (@224→98,
  @1526→21); 85: pre=24 ×5 (@733/@956/@1439/@1694/@1755), pre=29 ×3 ✓;
  second "que en 85" @1692 (85@1694) ✓.
- Bar met 3/3; corpus "parce qu'en" ×1 reproduced EXACTLY in Guizot t2
  (the elision family exists in-register; exact family counts differ by
  normalization — not verdict-critical). The ×1 attestation is the bar
  minimum, met honestly.
- 85 = verb-stem candidate with 7 frame-legs ("en [85]"×5 + "que [85]er"×2);
  value NOT promoted. Queued for the verb battery, correctly.

**A9 (86 INF-class): GRANT** — pre=00 ×12, suc=29 ×4, 33-parallel solid.
(Subject to the same stem/whole caveat as 33 — class-level claim only.)

**A12 — 37-01 unit: GRANT (unit, not value)** — 3× @939/@1633/@1817 ✓,
  twice in the byte-identical "21-64-37-01" 4-gram ✓. The "certain"
  (cer-tain) link is compatible, not proof — correctly not promoted.

**A10 — 33 que-valency: CONFIRM; 33+29 composition: HOLD**
- Re-derived: 33-46 @1451/@1624 (46@1452/@1625) ✓, identical "67-33-46"
  trigram ×2, different tails ✓; 33→46 exactly 2/25 ✓; 33-29 ×5
  @273/@626/@1232/@1424/@1477 ✓; pre=00 ×8/25 ✓.
- Valency CONFIRM narrows 33 to que-taking infinitives; value NOT named
  ("dire" recorded as leading partial, unpromoted — correct).
- Stem-vs-whole HOLD is the honest verdict: 8 windows need whole
  ("pour 33"), 5 need stem ("[33]er"); forcing either orphans 20–32%.
  Correctly refused to force; "[33]er ce" ×2 queued, not re-litigated.

**A14 — "par le"+substantivized infinitive: GRANT (set-level)**
- Re-derived: 96-00-92 @47 ✓; 96-00-33 @465 ✓; 96-00-86 @960 ✓;
  92: pre=00 ×6, →29 ×1/22 ✓.
- Bar met: 33 and 86 show strong INF-signal (≥2 of 3), all three windows
  parse under (a). No split: 92 does not discriminate toward (b) — its
  "la [92]"×3 is genuinely ambiguous (article+noun vs object-pronoun+verb)
  and its →29 ×1 is thin-INF, not nominal. 92 rides on the set; correctly
  named weakest. Values NOT named.

**A13 — "qui 77-84" frame: GRANT as re-valued ("qui l'on est [X]")**
- The frame is real (3× pre=77 trigram, "77-84-59" ×2 sub-frame,
  distributionally anchored by 84→59 ×4). A13 correctly did NOT promote
  84's value. A15 substitutes the value: "qui le [84-noun]" →
  "qui l'on …", "le [N] est [X]" → "l'on est [X]" ("one is [X]" — cleaner,
  no noun needed). Frame promotion STANDS; F53's masc-noun VALUE arm for
  84 is KILLED (superseded).

### KILLS / SPLITS / HOLDS

**A2 — 23~26 homophony: SPLIT GRANTED**
- Re-derived: n23=8, n26=17 ✓; shared suc-types outside anchor: 0
  (37 shared only inside the anchor windows) ✓; shared pre-types: {64}
  ("qui", weak) ✓; successor-class {12,30,00}: 23→0/8 vs 26→11/17,
  Fisher p=0.0029 EXACT ✓.
- Exceeds the {33,86}-precedent split standard. Near-synonymy correctly
  not rescued at the homophone bar. The "en ce qui [verb]" formula
  survives (corpus "concerne"×6/"touche"×2 reproduced EXACTLY); the
  "concerne/regarde" value stays open but unattached.

**A6 — 09~92: HOLD CONFIRMED (not split, not merged); "-ère" value KILLED**
- Re-derived: anchors [09/92]-64-29-40-65 @289/@683 ✓ — the finder's
  "qui [09/92] er e" direction is CONFIRMED WRONG; frame is
  [09/92]-qui-er-e-65; the "-ière/-ère noun" prediction is directionally
  void → value KILLED ✓.
- Relation: 5-group identical anchor + shared pre {30,84} + shared suc
  {7,64,98} + successor distributions indistinguishable (p=0.256) vs
  predecessor asymmetry p=0.0455, single-class-driven (92←00 ×6 vs 09←00
  0×) at 09's n=12. HOLD is the bar-honest verdict — the p=0.0455 is
  suggestive, not a clean split. Re-test at 09 n≥20.

**A11 — 45="ce": HOLD CONFIRMED** — 0/22 vs 10/32 complementarity ✓,
  "45-64" ×3 mirror ✓, zero contradictions ✓, but only ~1.5 mirrored
  frame-types (bar needs ≥2). Formula French NULL ✓, 96 verb-stem NULL ✓.
  Correctly unpromoted.

**A16 — Q5/Q6/§7: HOLDs CONFIRMED** — Q5 0/2 clean "c'est que" windows;
  Q6 single speculative window (already fenced in A9); §7 "fois le m" ×2
  unit solid, 63/44 continuations at n=1 each indistinguishable.
  No-battery ingestion items closed per finder instructions.

**P1 — "cela"=87+11: PROMOTE CONFIRMED (compositional)** — 7×
  @74/163/201/461/830/1242/1403 ✓; mutual top-attraction verified
  (87→11 = 87's #1 suc 7/32; 87 = 11's #1 pre 7/45) ✓; 4 clean windows +
  F107's "en cela" 3/10 confirmed and extended. Strengthens 87="ce"/11="la";
  @460 cross-confirms 79="tout" (two predictions interlocking).

### Corrections to prior lane findings — all VERIFIED
- **F71 est-arm = 7, not 6** ✓ (64-59×3 @315/1209/1776 + 94-59×3
  @558/762/1795 + 93-59×1 @102; all three 94-59 windows "n'est [30/39/37]"-
  compatible). Correction GRANTED.
- **19's "est ×2" → 1 physical window** ✓ (59→19 = [1777] only).
- **A5→A8 "tout 80" re-read** ✓ (pronoun+verb; noun leg retired).
- **A6 direction correction** ✓ ([09/92]-qui-er-e-65).
- **F53 84-arm supersession** ✓ (masc-noun → "l'on"; en-arm "en" killed by
  "qu'on en"; conditioned on C1–C3 above).

---

## What the runner got wrong (minor; none verdict-flipping)

1. **A8 transcription slip:** printed 89-successor list omits 89→41 ×1
   (counts still sum to n89=14). Cosmetic.
2. **Corpus magnitude figures unverified as exact:** "l'on" ×1852 /
   "qu'on en" ×21 (A15), the A1 adjective census, and A3's elision-family
   counts do not reproduce exactly on any natural slice of
   `code/side-period/corpus/` (independent counts: "l'on" ~2246–2289,
   "qu'on en" 18, "parce qu'en" ×1 exact in Guizot t2). Orders of magnitude
   confirm; the exact numbers imply a different normalization or file
   subset than stated. Not verdict-critical — but corpus legs should cite
   the exact file set going forward.
3. **Mixed position-citation convention:** some reports cite bigram/trigram
   starts (A7 @396), others the key cell (A5 @1364 for the same region;
   A9 @107 vs stream @106). All resolve to identical physical cells —
   substance unaffected — but the lane should fix one convention
   (`code/crowd4/REINDEX.md` says starts).
4. **A9 leg (1) overstated:** "dominant pour+infinitive signature" is
   class-level until the A10 stem/whole HOLD resolves (downgraded above;
   promotion intact via "pour que" legs).
5. **A5 "toutefois" framing:** syllable-inventory, not clerk elision habit
   (no lane precedent for internal-e drop; crib shows final mute-e written).
6. **A15 scope gap:** no mention of the standing 62="on" STRONG LEAD —
   conditioned above (C2). The 62/84 collision battery is now the
   highest-priority follow-up: it also bears on the N35 on-vs-il gap.

## Baseline extension

`code/crowd7/redteam/verify_f26_17.py`: **259/259 → 305/305 PASS**
(R15BANK: 46 cipher-side checks). `code/crowd7/redteam/verify_round7.py`:
**174/174 → 181/181 PASS** (ROUND15-LEDGER: 7 checks). Earlier
BANK/LEDGER blocks untouched; both scripts exit 0.
Note: the "237/237 + 160/160" figures in STATE.md are stale — the R14BANK
(12) + R14BANK-close (10) and LEDGER14C (14) blocks landed after that
figure was recorded (true pre-extension: 259/259 + 174/174).

## Priority follow-ups queued by this adjudication

1. **62/84 "on" collision battery** (conditions C2 on the 84="on" grant;
   bears on N35). Test: 62="il" rival ("il ne"×9 vs the 21-62×5 wrinkle),
   positional/homophone ruling, or 62's "on" legs re-examined.
2. **77="le" provisional** — now load-bearing for A8 (both C3 frames),
   A13/A15 ("l'on"), A5's @830 leg. Promote-or-kill battery.
3. **33/86 stem-vs-whole** (A10 HOLD) — bears on A9 leg (1) and A14's 92.
4. **09 n-growth re-test** (A6 HOLD; re-test homophony at n≥20).
5. **45="ce" second mirror** (A11 HOLD).
