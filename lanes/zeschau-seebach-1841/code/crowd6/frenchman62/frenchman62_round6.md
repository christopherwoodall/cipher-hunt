# 62="on" — non-ear on-vs-il discrimination battery (round 6, frenchman)

Work order: deliver the instrument-independent third leg for 62="on" — on-vs-il
discrimination with ZERO ear content (N35 named the gap: follower/predecessor
profile with n≫2 in independent cells, a word-space grammatical asymmetry, or an
independent "qu'il"-merger calibration from the cipher's own elision/merger
habits). Statistical/structural only. Legs 1&3 (ear) stand and are not repeated.
F42 order "follow 59" executed as Leg 3.

Code: `code/crowd6/frenchman62/battery62.py` (+ `explore.py`, `era_rates.py`,
`qu_rates.py`, `que_contexts.py`, `windows.py`).
Numbers: `code/crowd6/frenchman62/battery62_results.json`.
All cipher-side counts re-derived on the REPAIRED 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json`). All era legs in WORD SPACE only
(F30), Tocqueville T1+T2 (221,027 tokens), audit tokenizer.
Status marks: [GT] = pencil crib, [prov] = provisional, [prov-strong] =
provisional-strong, [LEAD] = lead-grade.

## Verdict (up front)

**NO PROMOTION. 62="on" stays STRONG LEAD (fenced).** The non-ear battery does
not deliver the third leg — it delivers an honest null with teeth:

1. **Leg 1 (the red-team-named calibration) VOIDS both** N28's merger
   corroboration ("qu'on"→1 group) and N35-leg-1's "il"-differential
   (p=0.041 kill) as licensed inferences. Under the cipher's best-calibrated
   elision habit, 46→62=0/29 is **ADVERSE to "on"** (E=7.18, p=2.6e-4,
   single, caveated — not kill-grade) and **INERT re "il"**.
2. **Leg 2 (three-way on/il/qui likelihood): on≈il TIE** (Δ=+0.27 nats for
   "on" on clean disjoint pieces); "qui" weakly disfavored (−6.2 nats).
   The unigram favors "il" (+9.4 nats) but is granularity-hedged (groups≠words).
3. **Leg 3 (59): 59=verb established structurally** (11=la [GT]→59:
   object-pronoun+verb); subject-selection does not discriminate on/il with
   available instruments. NULL on the on-vs-il question.
4. **Unbridgeability proof**: no follower/predecessor cell is BOTH mappable
   AND discriminative with n≫2 — the profile route is structurally
   unachievable with the current value inventory, not a matter of trying
   harder. All three grammatical-asymmetry sub-routes are blocked
   ("l'on" needs the l'-cell; impersonal-"il" needs verb cells; the
   qu'on/qu'il merger asymmetry does not survive cipher-internal calibration).

Net: the fence ("on-vs-il needs a non-ear resolution") is NOT cleared. The
battery's positive contributions: it stops the lane re-trying the void
differential and the unbridgeable profile route; it scores "qui" as a rival
for the first time (weakly disfavored); it banks 59=verb; it names the exact
unblockers (the "qu'on" cell hunt; the l'-cell; verb-cell identification).

## Re-derived baselines (repaired parse)

| quantity | value | status |
|---|---|---|
| n62 | 35/1847 (rank 13/96) | re-derived ✓ (WO: 35) |
| 62→94 | 9/35 = 0.2571 | re-derived ✓ |
| 46→62 | 0/29 | re-derived ✓ |
| n24 / n52 | 52 / 27 | re-derived ✓ |
| n59 / n64 / n87 / n96 / n94 | 27 / 47 / 32 / 21 / 37 | re-derived |
| followers of 62 (13) | 94×9, 48×6, 98×5, 16×4, 61×2, 6×2, 96×1, 91×1, 21×1, 18×1, 38×1, 46×1, 93×1 | re-derived |
| predecessors of 62 (21) | 21×5, 20×4, 74×3, 93/3/8/78/92×2, 13 singles (incl. 77[prov]×1, 40[GT]×1, 34[GT]×1) | re-derived |
| 62→46 / 62→21 / 62→11 | 1 / 1 / 0 | re-derived |
| 87→62 / 96→62 / 24→62 / 00→62 | 0 / 0 / 0 / 0 | re-derived |
| 62→87 / 62→64 / 64→62 / 62→24 | 0 / 0 / 0 / 0 | re-derived |
| 96→64 | 0 | re-derived |
| 62-X-46 trigrams (X≠62) | 0 | re-derived |

Frame conditioning (stated, not smuggled): the rival set {on, il, qui} is
conditioned on legs 1&3 (ear), which establish 62 as subject-capable. "qui"
(relative pronoun) is subject-capable; it was Check A's unexamined survivor
("blocked by 64='qui'" was asserted, never scored). N35's audit never scored
it either (logL ran on-vs-il only).

## Leg 1 — 46→62 elision-habit calibration (cipher-internal, [GT]-anchored)

**Method.** N35's "il"-differential (46→62=0/29, p=0.041 under 62="il") rests on
an unlicensed spelling premise: that "qu'il" would be written 46-62. N28's
corroboration rests on the mirror premise: "qu'on"=/kɔ̃/ merges to one group
(so 46→62=0 is predicted). Both premises are ear-theory. The red team asked
for calibration from the cipher's OWN elision/merger habits. Calibration
sites (no ear, no corpus — pure cipher geometry):

- 46=que [GT] before vowel-initial [GT] groups: 46→34(/i/)=0, 46→40(/e/)=0,
  **46→29(/ɛʁ/)=2** (@95, @217 — "qu'er…" shapes; the natural reading is
  elided "qu'"+vowel, i.e. 46 writes /k/, not only /kə/).
- 94=ne [prov-strong] before vowel-initial [GT]: 94→34=0, 94→40=0, 94→29=1.
- 87=ce [prov]→01 ("c'est", 01="est" MEDIUM lead): /sɛ/ (one spoken syllable)
  → **two groups** ×2 (@344/@1028) — provisional-conditioned, same direction.

**The cipher's demonstrated habit (H-split): /k/+V and /s/+V monosyllables are
SPLIT into two groups** (4 instances: 2 [GT]-anchored + 2 prov-conditioned).
/kɛʁ/ (one spoken syllable) → 46-29 (two groups). The N28 merger premise
("/kɔ̃/ = one spoken syllable → one group") goes AGAINST the demonstrated
direction — the cipher over-splits relative to spoken syllables
("première" 2–3 syllables → 6 groups; "personne" 2 → 3).

**Consequences.**

(a) N35's "il"-kill is VOID: "qu'il"=/kil/ would need a /k/+/i/ split, and
46→34=0 — the cipher never writes 46 before /i/. The spelling premise is
uncalibrated; p=0.041 was a number without a license. The datum is INERT re
"il" (its spelling under 62="il" is unknowable with current instruments).

(b) N28's merger corroboration is VOID as a licensed inference: the
"genuine predicted zero" (F44) assumed H-merge; the cipher's own habit
disfavors H-merge (4 split instances vs 0 merge instances at calibrated
sites).

(c) Under H-split, "qu'on"=/kɔ̃/ → 46-62 (exact analogy to /kɛʁ/→46-29).
Era P(pre="qu"|"on")=0.2475 (400/1616; unelided "que"+"on" is 0/1616 —
*all* of it is elided "qu'"). E[46→62 | 62="on", H-split] = 29×0.2475 = 7.18;
observed 0 → **p=2.6e-4, ADVERSE to "on"** (single datum, caveated — not
kill-grade; a demotion needs ≥2 independent checks).

**Caveats on (c) (all explicit):** (i) 46-29 could be "que"+h-aspiré rather
than "qu'er" (possible, unevidenced — if true, the /k/+V calibration
evaporates and the datum collapses to inert); (ii) era "qu'on" rate vs
despatch register (at ½ rate p=0.024; at ¼ p=0.16 — the datum needs era
within ~3×); (iii) the encipherer's inconsistency dilutes any consistent-habit
expectation unquantifiably (R2); (iv) a dedicated whole-word "qu'on" cell in
the mixed table (F35/F44-R4) would explain 46→62=0 under "on" — unfalsified,
unevidenced, named as the rescue to hunt.

**Leg-1 verdict:** the red-team-named calibration is delivered; it does not
promote "on" — it voids two old legs and surfaces one caveated adverse datum.

## Leg 2 — three-way likelihood (on/il/qui), disjoint clean pieces

**Method.** Score each hypothesis on data NOT used in N35 (46→62 excluded as
recycled). Era word-space, exact binomial log-likelihoods.

**(a) 62→94 = 9/35 vs era P(ne|w)** [cond. 94="ne" prov-strong]:

| w | era P(ne\|w) | logL(9/35) | exact P(X≥9) |
|---|---|---|---|
| on | 0.1584 | −21.07 | 0.091 |
| il | 0.1896 | −20.43 | 0.206 |
| qui | 0.0797 | −24.93 | 0.0013 |

"il" +0.65 nats over "on" (negligible); "on" +3.85 over "qui".

**(b) 62→46 = 1/35 vs era P(que\|w)** [GT 46]. The @1482 window is
`…98 | 62 | 46=que | 77=le…` — "98 62 que", the inversion frame: era "on que"
(8/1616) is *entirely* "dit-on/voit-on/pense-t-on que" inversion; era "il que"
(5/2795) entirely "dit-il que". Both hypotheses explain it via inversion;
"qui que" is 0/2360 in era (concessive "qui que ce soit" exists but unattested
in Tocqueville — weak, not zero).

| w | era P(que\|w) | logL(1/35) |
|---|---|---|
| on | 0.00495 | −5.48 |
| il | 0.00179 | −6.39 |
| qui | 0.00042 (Laplace) | −7.78 |

"on" +0.91 nats over "il" (weak positive-"on", n=1), +2.31 over "qui".
Non-ear corroboration of subject-hood: inversion requires a subject
(conditioned on 46=que [GT]; 98=verb is positional, not ear).

**(d) 96→62 = 0/21 vs era P(w\|"par")** [prov 96]: P("qui"|"par")=0.00290,
P("on"|"par")=P("il"|"par")=0 (grammatical zeros). logL: on=0, il=0,
qui=−0.06. Negligible (I over-hoped on this one; "par qui" is too rare to
bite at n=21). 96→64=0 likewise — "par qui" simply doesn't occur in the
cipher; inert under the qui-allophone model too.

**Joint (a)+(b)+(d):** on=−26.54, il=−26.82, qui=−32.77.
**Δ(on−il)=+0.27 nats — a tie. Δ(on−qui)=+6.2 nats — "qui" weakly
disfavored** (driven by (a) p=0.0013 and (b); the 87→62=0 vs 87→64=5
"ce qui"-slot datum is inert under conditioned allophony — no conditioning
rule identified, Jaccard fol/pre 0.139/0.190 consistent with either
conditioned polyvalence or distinct values).

**(c) Unigram, reported separately (granularity-hedged, NOT in joint):**
35/1847 groups = 1.895% vs era on 0.7311% (2.59×), il 1.2646% (1.50×), qui
1.0677% (1.77×). Binomial logL: on −185.4, il −176.0, qui −178.3 → "il" +9.4
nats. Hedge: cipher groups ≠ words (segmenter: ~958 provisional words →
35/958=3.65%: on 5.00×, il 2.89×, qui 3.42× — "il" still leads); the true
comparator is diplomatic-register "on", which we don't have (F41 unblocker
#3). Already-known adverse direction (N35); not double-counted.

**Leg-2 verdict:** no on-vs-il discrimination on clean pieces (tie);
"qui" newly scored as a rival: weakly disfavored, not killed.

## Leg 3 — the 59 follow (F42 order)

**Method.** Structural profile of 59 (n59=27, re-derived): followers
37×6, 32/35×3, 46×2, 42/30/39/36×2…; predecessors 84×4, 64[prov]×3, 94[prov]×3,
6/61/44×2…; 59→46=2 ("59 que"); 94→59 ×3 with subjects {86, 62, 42}
(@557/@761/@1794); 59→29=0 (no infinitive -er follower); 59→52=0.

**59=verb established structurally:** 11=la [GT]→59 ×1 — determiner/object
pronoun + X forces X verbal ("la"+"59" = object+verb). Consistent: 59→37 ×6
with 37="le" MEDIUM lead ("59 le" = verb+object); 59→46 ×2 ("59 que" =
verb+complement clause); 64[prov]="qui"→59 ×3 ("qui"+verb).

**On/il discrimination: NULL.** 59 takes diverse subjects (11[GT], 87[prov],
64[prov], 84, 6, 61, 44…); "que"-complement verbs (dire/croire/penser/
vouloir/savoir — and impersonal falloir) do not select "on" vs "il" except
the impersonal-only class, which is NOT established for 59 (would need its
own ≥2-check battery; 87→59 ×1 and 64→59 ×3 weakly disfavor "falloir"-class
but both rest on provisional anchors and "sembler"-class survives them).
The 62-94-X frames (9×: 93/64/59/26/70[GT]/79×2/88/24) are verb-shaped under
both hypotheses. The @761 window "62 94 59 46" = "on/il ne [verb] que"
(restrictive) fits both.

**Leg-3 verdict:** NULL on on-vs-il. Byproduct banked: 59=verb (structural,
[GT]-anchored) — feeds WO2's 96 verb battery (cf. bigram-closer's
reassignment of the verb slot to 59).

## Unbridgeability proof (the profile route)

Red team: "follower/predecessor profile with n≫2 in INDEPENDENT cells."
Tabulation of 62's cells (mappable = [GT]/[prov]/[LEAD]-identified):

**Followers** — mappable: 94[prov-strong]×9 (both in band 1.62×/1.36×,
RECYCLED in N35); 96[prov]×1 ("par on/il" both grammatical-0);
21[LEAD]×1 (P(me|on)=0.0050, P(me|il)=0.0097 — both small);
46[GT]×1 (0.0050/0.0018 — weak, n=1). Discriminative-but-unidentified:
impersonal-verb followers (faut / y-a / semble / suffit — *il*-only,
P(faut|on)=0 exactly) have NO identified cell; 48×6, 98×5, 16×4, 61×2, 6×2
unidentified.

**Predecessors** — mappable: 40[GT]×1, 34[GT]×1 (bare letters, unmappable in
word space); 77[prov]×1 ("le on"/"le il" both 0); 78×2 (proclitic; "l'"-word
killed 58× in N20, euphonic "l'" unidentified); 21[LEAD]×5 ("me on"/"me il"
both ~0 — shared puzzle, hypothesis-independent). Discriminative-but-
unidentified: "l'" ("l'on", P=0.0619, *on*-only) — l'-cell unidentified;
"s"/"si" ("s'il" vs "si on", P=0.0369/0.0080) — cells unidentified;
20×4, 74×3, rest unidentified.

**No cell is both mappable and discriminative with n≫2.** The profile route
is structurally unachievable with the current value inventory — not a matter
of effort. The grammatical-asymmetry route is blocked on all three
sub-routes: "l'on" (l'-cell), impersonal-"il" (verb cells), qu'on/qu'il
merger (calibration voids it; §Leg 1).

## Decision-why (first-class)

- **Why no promotion:** the bar is ≥2 independent non-ear checks. Delivered:
  zero. Leg 1 voids rather than builds; Leg 2 ties; Leg 3 is null. The
  single weak positive-"on" datum (Leg 2(b), +0.91 nats, n=1) cannot carry a
  promotion alone, and Leg 1(c) points the other way (p=2.6e-4 adverse,
  caveated).
- **Why no demotion:** the adverse datum is one caveated datum, not ≥2
  independent checks; legs 1&3 (ear) stand unrefuted; the four caveats
  (h-aspiré, register, inconsistency, whole-word rescue) are live.
- **Status:** 62="on" remains STRONG LEAD (fenced). The fence is now
  precisely characterized: unbridgeable with current instruments (§above).
- **What would change the verdict** (ranked): (1) identify the "qu'on" cell —
  a whole-word group with complement-clause distribution rescues "on" from
  Leg 1(c) and would be a positive leg; (2) identify the l'-cell — the "l'on"
  test (P=0.0619 vs 0) is the sharpest grammatical asymmetry available;
  (3) identify any impersonal-verb cell (faut/sembler) — an *il*-only
  follower kills "on" outright; (4) identify 48/98/16 (62's top followers) —
  new mappable cells are the only way to re-open the profile route.

## Byproducts & open threads (not claimed)

- 21→62 ×5 with 21="me" [LEAD]: "me"+"{on,il,qui}" ungrammatical under all
  three → 21 is not the word "me" in these instances (syllabic fragment, cf.
  78="me"-syllable F38) — structural, hypothesis-independent. A 21-polyvalence
  note for the lane, not a leg.
- 77[prov]="le"→62 @508 (`…67 77=le 62 94=ne 64=qui…`): "le"+"{on,il,qui}"
  ungrammatical under all three → shared anomaly; belongs to the 77 file
  (F37's conditioned reading), not the on/il battery.
- 62-94-64 ×1 ("on/il ne qui"): verbless-frame tension under both; noted,
  n=1.
- "qui" as a 62-rival: scored for the first time — weakly disfavored
  (−6.2 nats), not killed; the Check-A "blocked by 64='qui'" now has numbers
  behind it (needs a conditioning rule that doesn't exist).
- Era note: unelided "que"+"on"/"il" is 0/1616 and 0/2795 — *all* pre-"on"/"il"
  "que" is elided "qu'". Any cipher "que"+62/…"il" spelling must go through
  the elision habit, which is what Leg 1 calibrates.

## Traceability

- `battery62.py` — full battery, emits `battery62_results.json` (all counts,
  era rates, log-likelihoods, joint, unbridgeability tables).
- `explore.py`, `era_rates.py`, `qu_rates.py`, `que_contexts.py`, `windows.py`
  — supporting derivations (follower/predecessor inventories, era conditional
  tables, "qu" rates, "on que"/"il que" instance inspection, key windows).
- Every cipher-side number re-derived from the repaired 1,847-pair stream in
  this round's code; no number carried over from .md prose.
