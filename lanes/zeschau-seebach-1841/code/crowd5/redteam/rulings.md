# RED TEAM — Round 5 rulings

Date: 2026-10-07. Kill authority over every promotion.

## Ruling 1 — Frenchman 62="on" leg-3 case: PROMOTION DENIED → FENCED-LEAD

**Ruling: FENCED-LEAD.** 62="on" stays STRONG LEAD. The two delivered legs fail
the instrument-independence bar N28 set (a leg "from an instrument independent
of the ear — statistical/structural only"). Every number in the case file was
re-derived independently (`code/crowd5/redteam/audit_frenchman62.py`); the
cipher-side counts and era marginals reproduce exactly (era tokenizer
byte-identical: 221,027 tokens). The failure is in the independence logic, not
traceability — credit: the case file is fully traceable, the adverse 2.59×
unigram datum disclosed, caveats marked, anchor statuses marked per cell.

### Leg 1 (Check A+E — subject battery + "il"-differential): NOT independent
- Check A's rates and word-space grammatical kills (/ɔ̃/ rivals son/mon/nom/ont)
  are genuine word-space instruments. **But the subject-position premise is
  ear-derived** (legs 1&3's ear readings) and undisclosed as such — the rival
  kills are conditional on an ear premise.
- The unigram battery FAVORS the rival: "il" 1.50×, "qui" 1.77×, "on" 2.59×.
  The case does not win "on" on rates.
- The entire on-vs-il discrimination rests on Check E's "il"-differential:
  46→62=0/29 vs E=3.03 under 62="il", binomial p=0.041. This p-value is
  **assumption-maximal**: it assumes "qu'il" is written 46+62 (no merger) while
  "qu'on" merges to one group. The asymmetry is ASSERTED, not evidenced —
  "qu'il"=/kil/ and "qu'on"=/kɔ̃/ are both single spoken syllables, and the
  very ear model that merges /kɔ̃/ would merge /kil/ too. Under the same ear
  with merger, 46→62=0 is expected under BOTH hypotheses and discriminates
  nothing. An ear-phonetics assertion doing load-bearing work inside a
  "non-ear" leg is instrument contamination.
- "qui" is blocked only by provisional 64="qui" — a provisional-anchor
  dependency, marked but load-bearing.

### Leg 2 (Check C — mappable-cell profile): fails as stated
- Reported χ²=11.24, df=4, p=0.024 — but **3/4 named cells have expected
  counts <5** (me 0.173, la 0.412, que 0.173); the χ² approximation is invalid
  as reported. Exact multinomial (MC 200k): p=0.0450 — survives, barely.
- **Minus the recycled ne cell** (62→94=9 is legs-1&3's "on ne" datum re-entered;
  binomial P(X≥9|p=0.1584)=0.0908 on its own): exact p=**0.0675** — the
  genuinely independent part (me/la/que, n=2 total) is not significant.
- The same profile is also "significant" under era P(·|il) (exact p=0.0386)
  and the log-likelihood FAVORS "il" (delta −0.50). The profile does not
  discriminate "on" from its closest rival.
- me/que cells (n=1 each) lean on 21=[me] LEAD and 94=[ne] provisional-strong
  without F33-style fencing.

### Double-duty audit (the 46→62 null)
46→62=0/29 is used twice: Check B (marked corroboration — honest, one use is
fine) and Check E (load-bearing). **One datum, two uses** — and the
discriminative use is the ear-contingent one. The datum is genuine (the ear
model's novel prediction, quantified: written-era E=2.31, p=0.090), but it
cannot serve as the independent leg.

### The 2.59× unigram overage
Adverse, disclosed. The genre defense (lane-documented 6.7×/11.9× swings) is
plausible but those swings are on specific register features, not a blanket
license; the factor-2 band is uncalibrated (F20) so neither kill nor pass by
band. It stands as a caveat: "on" is not the best unigram fit, and the case's
discrimination rests entirely on the ear-contingent null.

### Methodology flags banked (F26-class)
- **F26-5**: χ² reported with expected <5 in 3/4 named cells, no exact-test
  verification — overstates precision (0.024 claimed vs 0.045 exact).
- **F26-6**: asserted by-ear merger asymmetry inside a "non-ear" leg —
  instrument contamination.
- **F26-7**: undisclosed ear-derived premise (subject position) in Check A's
  rival-kill framing.
- **F26-8**: recycled datum (62→94=9) re-entered in Check C without
  independence accounting; provisional/LEAD-anchor leaning unfenced.
- Auditor's own: my first audit draft had a denominator bug on P(·|que)
  (divided by uni[word] instead of n_que) — caught by the ratio check,
  corrected; claimant's numbers verified exact. Fallibility is symmetric.

### Fence
The open thread is precise: **on-vs-il discrimination is ear-contingent and
needs a non-ear resolution.** Candidates: a follower/predecessor profile with
n≫2 in the independent cells; a word-space grammatical asymmetry between
"on" and "il" contexts (e.g., "on" takes infinitives/subjunctives differently);
or an independent "qu'il"-merger calibration from the cipher's own
elision/merger habits. Until then, 62="on" holds STRONG LEAD on legs 1&3.

### Fence
The open thread is precise: **on-vs-il discrimination is ear-contingent and
needs a non-ear resolution.** Candidates: a follower/predecessor profile with
n≫2 in the independent cells; a word-space grammatical asymmetry between
"on" and "il" contexts (e.g., "on" takes infinitives/subjunctives differently);
or an independent "qu'il"-merger calibration from the cipher's own
elision/merger habits. Until then, 62="on" holds STRONG LEAD on legs 1&3.

## Ruling 2 — Bigram Closer WO1/WO2/WO3: one PROMOTION, two ACCEPTs

Audit: `code/crowd5/redteam/audit_bigram78_77_578.py`. Every cipher-side count
re-derived; all era word-space numbers verify exactly (L1w 22.76×, Leg C
1.152×, vernement 554 / verrement 0, nement 641 / rement 282, "ce me" 1/1134,
"me ne"/"le me"/"ce le" era-0, sixmer ×2 @573/@1164 with 94→87 @1170,
77-diversity 20/22, P(77|64)=0.0638, 67-77-81 ×4, 86→29 @431 confirming the
@430 "le"+stem+"er" frame). Two discrepancies found (below); neither changes
a verdict grade except as noted.

**Position correction (F26-9):** F14's banked 5-mer positions @1179/@1350 are
OLD-parse stale — repaired parse gives **77-78-94-82-06 @1180/@1351**
(recomputed). The worker's "gou" caveat positions (@1180/@1351) are correct;
F14 needs the REINDEX fix. Same staleness class as the n06=46 catch.

### WO1 — 78="me" vs 78="ver": ACCEPT (COEXIST)
- **78="me"-WORD → disfavored-strong: ACCEPT.** L1w 22.76× out of band
  (verified); "la me"×2 era-0 (GT 11=la, n=2 — below the n≥3 kill rule, no
  formal kill); "ce me"×7 era-~0 (era_n=1, not a kill); "me ne"×2 era-0
  (n=2, fenced on 94="ne"-prov). Disfavored-strong is the correct grade —
  the worker does not overclaim a kill.
- **78="me"-SYLLABLE holds LEAD: ACCEPT.** L1s 1.131× verified (recomputed
  with battery4's syllabifier: era "me"-syllable 0.014838). F30 assessment:
  L1s is a *unigram* comparison, not a conditional leg — outside F30's letter
  (which bans era-syllable-*conditionals* on fragments); "me" is not in the
  tuner's flagged er/m/i/e class. Admitted as CONTEXT, not an independent leg.
  The LEAD rests on elimination + the standing "l'"-rival kill (N20 precedent,
  not re-litigated) + the adverse dissolution below.
- **Category-error dissolution of the 77→78×7 "adverse": ACCEPT as
  conditional.** Testing the WORD "me" against a syllable bigram was indeed a
  category error; under the syllable reading the frames are "le"+"me…" (cf.
  "le même"/"le mener"). Conditional on 78="me"-syllable (LEAD, unconfirmed) —
  the worker fences this honestly.
- **78="ver" → LEAD (conditioned islet): ACCEPT, with n_eff=1.** Positional
  rule "78=ver iff next=94": 2/2 @1181/@1352, 0/29 other 78s followed by 94 —
  exceptionless, but both instances sit inside the ×2 5-mer repeat
  (@1180/@1351): **n_eff=1** by the lane's own N27 standard. Lexical leg
  (vernement 554 vs verrement 0, word-space) is real; compositional leg
  ("me ne" era-0 forces non-"me") fenced on 94="ne"-prov. LEAD is the correct
  ceiling — the worker claims no more.
- **COEXIST verdict: ACCEPT.** Neither kills the other. F33's conditioned-
  polyvalence count grows to 4 groups (06/52/94/78). Rival "e" stays live.
- **Traceability note:** Leg A era P(inf|le) — worker claimed 507/4570=0.1109
  (1.024×); recomputed **450/4570=0.0985 (1.154×)** with the worker's own
  is_infinitive recipe. Both in-band (band uncalibrated); the "near-exact
  match" rhetoric does not reproduce — minor flag, does not change the leg
  grade (in-band consistency). The worker's own caveat (one stem vs all
  infinitives = "consistency, not identification") stands and is the right
  frame: Leg A is corroboration-grade.

### WO2 — 77="le": PROMOTE LEAD→provisional (CONDITIONED)
**Ruling: PROMOTE.** The lane's first promotion in five rounds. Independent
legs: (1) the 77→86×5 follower frame — positional, verified @430/798/877/950/
1133, with the @430 77→86→29 "le"+stem+"er" frame confirmed (86→29 @431);
(2) the diversity free-word profile — 20 followers / 22 predecessors,
structural, verified; (3) unigram 1.152× in-band (context, verified). The
bar (≥2 independent checks) is met. Adverses all fenced with explicit
dependencies: "ce le"×2 era-0 @515/@869 (verified; fenced on 87=ce-prov,
genuine tension, n=2 below kill); rate overshoot 4.07× (band uncalibrated,
reported); "le me"×7 dissolution conditional on 78="me"-syllable-LEAD.
- **Leg B grading:** the predecessor grammatical frames ("qui le [84]"×3
  n_eff=1, "veut le [81]"×4, 06→77×6) are real word-space grammar but all
  three lean on provisional anchors (64="qui", 67="veut", 06 verb-stem) —
  fenced-leaning, not an independent leg. The promotion does not rest on it.
- **The "gou" caveat forces the conditioned framing — with the exception
  FENCED, not established.** 77="gou" word-internally @1180/@1351 requires
  the 5-mer host to be "gouvernement", which stacks four unconfirmed readings
  (78="ver" islet n_eff=1 + 94="ne" prov-strong + 82="m" GT + 06="ent"
  restricted-PLAUSIBLE). The contradiction is conditional, not established.
  Promotion is for **77="le" as the conditioned free-word reading
  (F33-style)**; the "gou"×2 exception is FENCED (trigger unconfirmed,
  n_eff=1).
- **Dependencies recorded on the promotion:** (a) the "le me"×7 dissolution
  is conditional on 78="me"-syllable — if that LEAD falls, a kill-grade
  adverse revives; (b) "ce le"×2 tension tests 87=ce as much as 77.

### WO3 — @578 trigram host: ACCEPT (scoped thread-closure)
**Ruling: ACCEPT the @578 revival-thread closure (fence lifts); 94="re" as a
general reading stays DISFAVORED — "BURY" accepted as scoped thread-closure,
not a general kill.**
- Sixmer `78 45 13 55 61 94` ×2 @573/@1164 verified; continuation 94→87 @1170
  verified (F33 "en"-islet applies at @1169). The particle argument is sound
  *conditional* on (94="en"-LEAD + 87=ce-prov + sixmer-identity). The identity
  assumption is reasonable though fenced: byte-identical ×2, and the attested
  by-ear inconsistency was different spellings, not identical sixmers
  re-segmented.
- Lexical legs verified (vernement 554 / verrement 0; host odds 2.27:1). Gap
  noted: at @578 the pre-94 group is **61**, so the "vernement" completion
  needs 61="ver" (untested allophony — worker discloses). The @578-specific
  anti-"re" leg is the sixmer particle argument (fenced), not the lexical one.
- **Montrera datum (cross-fleet memo) weighed explicitly:** sidepath's
  "montrera" as 94="re" support (S=0.917) comes from a **VOIDED pass**
  (174 < 2×208.3 — the loop's own stop rule fired). It is weak corroboration
  at most, general (not @578-specific), and does not dent the sixmer-identity
  argument. It keeps general 94="re" at DISFAVORED rather than dead — which is
  exactly where this ruling leaves it. The burial argument stands regardless
  *at @578*; "re" is not buried generally.
- "re" has no positive support at any trigram (the 1.28× leg VOID per F30,
  N24). The N24 fence (@578 revival thread) is retired by this ruling.

## Docket status: 2 claims adjudicated, 4 pending

## Ruling 3 — Morphologist WO1/WO2/WO3: LEAD strengthened (not promoted), NULL honest, M1 accepted

Audit: `code/crowd5/redteam/audit_morph47_06.py`. Every load-bearing number
re-derived and verified exactly: Q2 partition (6 ce / 9 frag / 0 overlap),
Q1 counts and tests (47→64=0/28, 87→64=5/32, 87→46=3/3 all pre=96; Fisher
one-sided 0.0476; binomials 0.0029/0.0086), C2 frames = Q2 pre==29 frames,
29→87 ×3 @147/@627/@1425, 06→29 ×4 @1096/1388/1709/1815, 86→29 ×4,
rate 45.98/1000w, M1 counts (00→86 ×12 vs 00→06 ×0; 86→11/77/00 = 0/0/0),
Fisher 7.278e-06, binomial 6.292e-11, enrichment 12.59×. The worker's code is
fully traceable. Two prose-vs-JSON discrepancies flagged below; neither
overturns a verdict.

### WO1 — 47="ce": LEAD (strengthened), promotion BLOCKED — AGREE
- **Q2 fragment rule: ACCEPT as F33-form islet rule.** The partition is clean
  (9/9 fragment frames, 0/6 ce-frames and 0/13 others trigger the condition).
  Caveats: (a) "zero cross-contamination" is partly definitional — the
  features (suc∈{46,11}/pre==96 vs suc==78/pre==29) are disjoint by
  construction, so overlap was impossible; the empirical content is the clean
  partition itself; (b) 13/28 frames unclassified — Q2 is a marked-reading
  islet rule (like 94's "en"), not a full partition; (c) the fragment SOUND
  is unidentified ("même"-fragment is a candidate, not established) — F33's
  existing cases all have identified sounds for both readings.
- **Q1 qui/que complementarity: ACCEPT as F33-form, thin.** Stated
  falsifiably with explicit falsifiers (one 47→64; one 87→46 with pre≠96).
  Caveats: 47→relative-que is n=2 (@548/@864); Fisher 0.0476 is one-sided and
  borderline; the rule leans on 87=ce-provisional and 64="qui"-provisional;
  the "fused" carve-out (parce que/cela/c'est) is principled but adds
  complexity. It strengthens the LEAD; it does not promote.
- **C2 dissolution: ACCEPT as legitimate.** The 12.6× rate was F30-void
  (N22-class); the worker self-kills it explicitly, citing the red team's N22
  precedent — exemplary. Cipher-side reclassification (the 4 frames are Q2's
  pre==29 context) verified; cross-allophone 29→87 ×3 shows the phenomenon is
  "ce"-level, not 47-level. This is reclassification with evidence, not
  hand-waving.
- **Unigram: numbers corrected.** The .md's 4.11×/2.79× do NOT reproduce from
  the JSON — verified values are **2.13** (elision-corrected) and **1.446**
  (ce-proper, elision-corrected); trust the JSON (F26-11). The substantive
  point (residual = register + polyvalence; rival ranking unaffected) stands.
- **Rival battery: "ce" unique survivor under the stated kill rule — ACCEPT
  with caveat.** B2=121.5 for "ce" (the cela-register gap, F10/F31) is
  unaddressed in the writeup; the lane's genre position covers it, but the
  worker should have said so (F26-13).
- **Promotion BLOCKED: AGREE (worker's own call, upheld).** The @148–152
  64-slot residual is genuinely unresolved (era attestation zero under all
  readings; three live alternatives). What unblocks, in order: (1) the 96
  conditioned-verb battery in the "ce qui __ ce que" frame (worker's ranked
  #1; the context miner flagged the same window independently); (2) identify
  the Q2 fragment sound; (3) close the unigram residual with a diplomatic
  corpus (Meisel 1826 not in lane).
- **Ruling: 47="ce" stays LEAD (strengthened).** Seven legs, two new F33-form
  conditions, honest blockers. The strengthened LEAD is earned; provisional
  is not.

### WO2 — 06 stem: NULL — ACCEPT as honest
- 06→29 ×4 positions verified; 86→29 ×4 verified; 7 infinitive events (with
  the @1388/@1391 coordination noted and fenced as T2).
- **Single-stem-for-all-06 KILLED on rate: ACCEPT.** 45.98/1000w vs best
  "pri*" 2.685 = 17.1× — kill-grade, verified.
- **"donner" conditional lead: ACCEPT as properly fenced.** The worker marks
  it UNVERIFIED (19× register inflation needed) and does not promote it.
  No over-claiming.
- 67 et/veut fork (114:1 era, cipher-side fork real): accepted as an
  unpromoted lead with 8/38 classified — honest scoping, round-6 work.
- T1/T2/@1709 tensions all fenced, not hidden. **The NULL is honest.**

### WO3 — 06/86 M1: ACCEPT as F33-grade distributional rule
- **M1 the rule: ACCEPT.** 00→86 ×12 vs 00→06 ×0; 06 in finite frames
  (→11 ×4, →77 ×6, →00 ×4), 86 never there (0/14); falsifiers stated and all
  zero (the @889 86→06 is fenced as clause-boundary, and is not one of the
  three falsifiers in any case). Fisher 7.278e-06 and binomial 6.292e-11
  verified. This clears F33's bar: verified positional conditioning,
  falsifiable as stated, significant.
- **M1 the allomorph interpretation: ACCEPT as working hypothesis, not
  established.** The distributional facts are solid; "same stem,
  mood-conditioned" is consistent with M1 + the petit-chiffre prior, but T1
  (79.4/1000w vs ~40 max) and T2 ("donner et donner") challenge one-stem,
  and the →29 slot is shared with conditioning unfenced (worker's honest
  caveat). The interpretation is adopted per memo direction with fenced
  tensions — the right epistemic grade.
- 00="pour" lead noted, out of scope (needs its own battery — not
  adjudicated). No nulls posited (compliant with the standing constraint).

## Docket status: 3 claims adjudicated, 3 pending

No round-5 executor claims have landed. `code/crowd5/` and `report_inbox/`
contain no Frenchman, Morphologist, Bigram Closer, Closer, Segmenter, or
Inventorist outputs as of this review. **Zero rulings issued; zero promotions;
zero kills; net promotion count = 0.**

This file records (a) the armed baseline every future round-5 claim will be
judged against, and (b) the standing kill conditions per expected claim, so
that adjudication, when claims land, is mechanical and traceable.

## Armed baseline (recomputed against the repaired 1,847-pair stream)

`verify_baseline.py` builds the canonical stream from
`code/side-keyhunt/repair_parse.py` + `repaired_offsets.json` and re-derives
every load-bearing number named in the round-5 work orders. **29/29 checks
PASS** (canonical: 1,847 pairs, 96 distinct groups, "la première" @754/@1034).

Corrections the instrument forced on my own expectations (documented, not hidden):
- `47->64` — I had written want=2 from memory; recomputed **0**. The "ce qui"
  route goes via 87, never 47. (Noted as evidence, not as a number I carried.)
- `n06` = **44** on the repaired parse, not 46 — the 46 was the OLD-parse count
  (N28's P(77|06)=6/46). The exact old-parse staleness failure this brief warns
  about, caught live. P(77|06) recomputed 6/44=0.1364.
- `n78` = **31** — I had no banked number; recorded from the stream.
- `94->82` positions = [578, 1182, 1353, 1742] — old-parse [578,1181,1352,1741]
  + REINDEX rule (old n≥773 → n+1), verified byte-level.

N31 spot-check (independent): the round-4 rulings' "values identical for
n≥773" assertion holds — every re-derived count matches its banked value;
only indices shifted, per REINDEX.md. N31 stands.

## Standing kill conditions for the expected round-5 claims

### 1. Frenchman — 62="on" third leg (instrument-independent)
- Current legs: ear lock + 62→94 = 9/35=0.2571 (2.18× era, recomputed — a 9th
  "on ne" @761 from the repaired a5_03 region) + fresh-window subject
  triangulation @845–853 ("…par écrit, on me [dit]…", zero counterexamples in
  26 fresh windows, /ɔ̃/ rivals killed).
- PROMOTION REQUIRES: a leg from an instrument independent of the ear —
  statistical/structural only. Legs 1&3 share the ear instrument (N28); a
  restated ear reading, a bigger fresh-window sample, or any 62-count
  re-derivation does NOT qualify. N22 calibration exclusions enforced (no
  29/82/34 in rate legs); F30 (no era-syllable-conditionals on fragments).
- KILL CONDITION: if the "independent" leg divides by a wrong marginal (the
  N20 B-78b failure mode — verify the denominator), cites 62→94 on the old
  8/34 count, or leans on 87/64/96-provisional anchors without support.
- Status without the leg: STRONG LEAD, unchanged.

### 2. Morphologist — 47="ce" promotion battery
- Current: "ce que" 3/28=0.1071 vs era 0.1076 → 1.00× exact; "par ce" 2.85×;
  47→11 ×3 "cela". Blockers (N29): C2 "..er→ce" 12.6× unexplained, unigram
  2.87×, @148–150 jar bounded (@150–152 "par ce que" ✓), the verbless 64 slot.
- PROMOTION REQUIRES: C2 explained AND the 64-slot residual resolved, or an
  equivalent second independent leg. "Ce que" 1.00× is one leg, not two.
- ECHO WARNING: 87/64/96-provisional are live in every 47 context ("par ce
  que" = 96-47-46). A candidate that "reads" only through provisional anchors
  gets FENCED, not promoted. 47->64=0 (recomputed) — "ce qui" never via 47;
  that's tension for uniform "ce", not a kill, but the battery must address it.
- F33 GUARD: a claim of unconditioned 47=ce∥47=me polyvalence breaks F33 —
  the battery must name the conditioning rule or be denied.

### 3. Morphologist — 06 stem identification
- Current: 06→29 ×4 (repaired; the old 5th was an off-phase artifact), 06→77 ×6,
  06→11 ×4, 06→00 ×4; 00→86 ×12 vs 00→06 ×0 (06/86 complementary distribution);
  n06=44 (repaired). 06="ent" general REFUTED; /mɑ̃/ KILLED (N17); class
  PROVISIONAL; specific stem bounded, NOT identified.
- PROMOTION REQUIRES: ≥2 independent checks on a SPECIFIC stem reading —
  the class already holds provisional. The 66× "demand*" rate gap is the
  baseline any specific-stem claim must clear.
- F30: no era-syllable-conditional legs (06 is a morphological fragment;
  -er-strip legs uncalibrated). F33: 06/86 distribution is complementary
  conditioning — fine as-is; a second free reading without a rule kills F33.

### 4. Bigram Closer — 77="le" / 78="me" vs 78="ver"
- Current: 77→86 ×5 verified @430/798/877/950/1133 ("le"+verb-stem frame);
  77→78 ×7 adverse frames under 78="me" ("pas me" era-0 — kill-grade against
  the frame); 2/7 inside the "gouvernement" trigram → 78="ver" word-internal
  open; 77="pas"/77="que" DISFAVORED.
- PROMOTION (77="le") REQUIRES: the object-pronoun frame + L1 as independent
  legs; the 77→78 ×7 adverse frames must be ADJUDICATED, not waved — either
  killed as frame-adverse (fatal) or absorbed by 78="ver" conditioning (F33).
  If 78="ver" is claimed word-internal, its conditioning rule must be stated.
- 78="me" PROMOTION STAYS DENIED until the 77→78 ×7 frames are resolved
  (N25 — the closer's own finding). "pas me" era-0 is a grammatical kill,
  not a rate anomaly.

### 5. Closer — 87=ce new angles
- Current: provisional-strengthened (F27); cela leg DEAD (N27 — register-matched
  reporter-voice subset fails the pre-stated bar); 87-64-77-84 @1800–1803 =
  «ce qui [verbe] 84» corroboration (not promotion).
- PROMOTION REQUIRES: a non-circular anchor or a non-circular leg.
  The N3 "parce que" frame was admitted CIRCULAR (conditions on 96="par");
  the R1 recycled the dead 24="est" number (VOID). Any claim reusing these
  without disclosure is a traceability violation, not a leg.
- 24-inversion stays empty under era, Les Mis, AND the union model (F27) —
  "24 is not a plain function word" is a legitimate finding, but it is not a
  leg for 87=ce. The F30 instrument restriction still stands.

### 6. Segmenter — rotation claims
- Current: recomputed chi²=366.3 (N30) under repaired phases; cluster
  assignments fragile (61/96 groups change phase); tuner NULL stands
  (phases ≠ word-position classes, N15).
- PROMOTION REQUIRES: a falsifiable positive claim of what the rotation IS,
  not "consistent with X". A rotation-break drag that only reproduces the
  chi² is a re-derivation, not a claim. Any claim using phase→position
  mapping is VOID per N15 (tuner-falsified instrument).
- The 06/86 split and conditioned polyvalence (F33) are the model the rotation
  must coexist with — a claim contradicting F33's falsifiable form
  (1 group → 2 sounds, unconditioned) is itself a claim to adjudicate:
  verify it against the conditioning rules, or kill it with extra care.

### 7. Inventorist — inventory claims
- Current: side-wordpattern fleet adjudicated (redteam/ADJUDICATION.md, F34);
  26 proposals killed; crib-derived inventory is the only legal base for
  fragment hypotheses (F30). The K≥3 synthetic numbers from the tester §6 do
  NOT reproduce — regenerate, never cite.
- Any round-5 inventory claim is judged against R1–R8 (red-team-amended).
  Echo warning: an "inventory" that re-derives the pencil cribs plus the
  provisional anchors is a re-statement, not an instrument.

## Methodology flags carried into round 5

- N22 calibration exclusions enforced in every rate leg (29/82/34 excluded;
  40-conditionals excluded; my own baseline complies).
- F30: rigid syllabification DEAD — no era-syllable-conditional legs on
  morphological fragments; era word-space legs survive.
- Round-3 traceability violation (N20/N26: .md ratios not reproducing from
  archived code) must not recur — every executor number must reproduce from
  shipped code+JSON on the repaired stream; prose ratios are not evidence.
- Instrument independence is audited per claim, not per check count: two checks
  from the same ear/rate are ONE check (the 62="on" legs-1&3 precedent).
- Any number computed on the 1,846-pair parse is VOID unless re-derived
  (REINDEX.md: old n≥773 → n+1). My baseline caught an old-parse count (n06=46)
  in my own first draft — the staleness rule is live.

## Kill ledger — round 5

| Claim | Ruling | Reason |
|---|---|---|
| Frenchman 62="on" leg-3 (A+E battery + Check C profile) | **FENCED-LEAD** (promotion DENIED; stays STRONG LEAD) | Leg 1: subject-battery framing inherits an undisclosed ear premise; unigram rates favor "il" (1.50×) over "on" (2.59×); the "il"-differential (p=0.041) is ear-contingent — the qu'on/qu'il merger asymmetry is asserted, and the same ear merges /kil/ too. Leg 2: χ² p=0.024 invalid (3/4 cells exp<5); exact p=0.045 full but 0.0675 minus the recycled ne datum; profile fits "il" equally (logL favors il). 46→62 null = one datum, two uses; discriminative use is ear-contingent. |
| Bigram Closer WO1 (78="me"/"ver") | **ACCEPT** (COEXIST) | me-WORD→disfavored-strong (L1w 22.76×; no formal kill, correct grade); me-SYLLABLE holds LEAD (L1s 1.131× as context; F30-letter clear); 77→78×7 adverse dissolution accepted as conditional on the syllable LEAD; "ver" islet joins as LEAD with n_eff=1 (both instances in the ×2 5-mer); F33 grows to 4 groups. |
| Bigram Closer WO2 (77="le") | **PROMOTE** LEAD→provisional (CONDITIONED) | Independent legs: 77→86×5 frame (verified) + diversity 20/22 (structural) + unigram 1.152× (context). Leg B provisional-leaning (fenced). Adverses fenced: "ce le"×2 (87=ce-prov), "le me"×7 dissolution conditional on 78="me"-syllable. "gou"@1180/@1351 exception FENCED (trigger unconfirmed, n_eff=1). Leg A 1.02×→recomputed 1.15× (minor traceability flag). Lane's first promotion in five rounds. |
| Bigram Closer WO3 (@578 host) | **ACCEPT** (scoped; fence lifts) | @578 revival thread closed on sixmer-identity argument (fenced but reasonable) + lexical legs. 94="re" general stays DISFAVORED — "BURY" accepted as scoped thread-closure, not a general kill. Montrera (S=0.917, VOIDED pass) weighed: weak, general, does not dent @578; keeps "re" disfavored rather than dead. |
| Morphologist WO1 (47="ce" battery) | **LEAD (strengthened), promotion BLOCKED — AGREE** | Q1 ACCEPT as F33-form (n=2 thin, provisional-leaning, Fisher one-sided 0.0476); Q2 ACCEPT as F33-form islet rule (clean partition; 13/28 unclassified; fragment sound unidentified); C2 dissolution legitimate (F30-void self-kill + cipher-side reclass + cross-allophone); unigram .md numbers corrected to JSON (2.13 / 1.446); rival battery "ce" unique survivor (B2=121.5 cela-tension unaddressed). Blocked on @148–152 (worker's own call, upheld); unblockers: 96 conditioned-verb battery, fragment sound, diplomatic corpus. |
| Morphologist WO2 (06 stem) | **NULL — ACCEPT as honest** | Single-stem-for-all-06 KILLED on rate (17.1×, verified); "donner" conditional properly fenced UNVERIFIED; 67 et/veut fork (114:1) unpromoted lead; all tensions fenced. No over-claiming. |
| Morphologist WO3 (06/86 M1) | **ACCEPT** (F33-grade rule; allomorph = working hypothesis) | M1 distributional rule verified (Fisher 7.3e-06, binomial 6.3e-11, falsifiers all zero); allomorph interpretation consistent but fenced (T1 rate tension, T2 self-coordination, →29 shared unfenced). 00="pour" out of scope. |

- Promotions: **1** · Demotions: **0** · Kills: **0** · Fenced leads: **1** · Nulls: **0**
- Net promotion count: **1** — the bar held four rounds; round 5 promotes 77="le" (conditioned).

## Standing constraints (cross-fleet memo, 2026-10-07)
- **No nulls:** petit-chiffre intel — the French reference table has NO nulls,
  matching the lane's null-digit negative. Any claim positing null groups is
  pre-voided. (No round-5 claim posits nulls.)
- **Published-key channel EXHAUSTED:** key-hunt fleet, 20 queries + 13 source
  checks, clean negative. No round-5/6 effort goes to literature key-hunting.
- **Baseline extension (memo item 1):** sidepath pre-repair recounts re-verified
  on the 1,847-pair stream — n24=52 (unmoved), n52=27 (unmoved), n62=35 (moved
  from 34; N28 already carries 9/35; sidepath skeleton's 34 superseded).
  verify_baseline.py now 31/31 PASS.
- **F26-9:** F14's 5-mer positions @1179/@1350 are old-parse stale; repaired =
  @1180/@1351. Flagged for the F14 correction.
- **F26-10:** WO2 Leg A era P(inf|le) 507/4570 (1.024×) does not reproduce;
  recomputed 450/4570 (1.154×) with the worker's own recipe. Both in-band;
  leg grade unchanged (corroboration).
- **F26-11:** morph47_06.md unigram numbers (4.11× / 2.79×) do not reproduce
  from morph47_06_results.json (verified: 2.13 elision-corrected, 1.446
  ce-proper). Trust the JSON; prose/JSON mismatch class.
- **F26-12:** Q2's "zero cross-contamination" is partly definitional (features
  disjoint by construction); empirical content is the clean partition. 13/28
  frames unclassified; fragment sound unidentified.
- **F26-13:** rival-battery B2=121.5 for "ce" (cela-register, F10/F31)
  unaddressed in the writeup; lane's genre position covers it but unstated.

## For the record

The round-4 ledger stands unmodified: kills 47="me" (uniform word),
94="re"→disfavored, 64="même"→disfavored (bounded), 77="le" LEAD-weak→LEAD
(fenced), 62="on" STRONG LEAD (third leg pending), 94="en" co-value DENIED.
Nothing in the armed baseline moves any of those.
