# Red Team — crowd round 3b (2026-10-07)

Follow-up review of the three late finishers: **bigram closer** (`bigram_closer_results.{md,json}`,
battery `battery.py`), **frenchman** (`frenchman_results.{md,json}`), **segmenter**
(`segmenter_results.{md,json}`). Read `red_team_results.{md,json}` first; the 13
round-3 verdicts stand except where explicitly revised below.

Recomputation: every cipher count re-derived from `crib_attack.load_pairs()`
(run from `code/`); every era rate re-derived from Tocqueville t1+t2 with the
attempt-3 tokenizer (`code/crowd3/battery.py` `Models`); word-space checks with
`battery.load_words`. Script: `/tmp/rt3b_recompute.py` (ephemeral; key outputs
quoted inline).

## Verdict table

| # | Item | Verdict |
|---|---|---|
| a | 78="me" PROMOTION (bigram closer) | **REJECT** → LEAD. Two load-bearing legs broken: B-78a (the "e"-kill is a syllabifier artifact), B-78b (L2 ratio miscomputed: claimed 1.66×, true 2.26× out of band — wrong marginal). "l'"-kill survives (recomputed 58×). "e" returns as a live rival. |
| b | 77 three-way (closer: "pas" REFUTED, "que" LEAD 3-check, "le" LEAD-weak) | "pas": REFUTED **downgraded → DISFAVORED (strong)** — direction right, grade too high (grammatical leg is provisional-conditioned). "que": closer's LEAD does **not** overturn DISFAVORED (uncalibrated-band legs only; ear contradicts at @790; polyvalence cost stands). "le": LEAD-weak accepted. The battery is a legitimate new instrument, not a void one. |
| c | Calibration exclusion (29/82/34 dropped) | **VALID** (reproduces: 181.5×/61.1×/3.3×). Blast radius: my round-3 "ent\|er strained" leg (verdict 3) **VOID**; the 06="ne" ne+er-initial leg **VOID** (no live claim affected); closer's 94→82 "ne m'" void endorsed. **Extension (red-team): 40="e" CONDITIONAL legs are uncalibrated too** — the era 'e' syllable ≠ the cipher's word-final mute-e 40. |
| d | Frenchman K1–K7 | K1 **accept** (independent corroboration of standing kill). K2 **accept scoped** (conditioned on 87=ce/64=qui). K3 **conditional only** (needs 01="est"). K4 **accept provisional** (3.84× + "ici" ×0). K5 **accept scoped** (forces 52 polyvalence). K6 no action. K7 **reject** (conditioned on unconfirmed 37="le"). |
| d2 | Frenchman ear-confirmations (87=ce, 64=qui, 96=par, 94=ne) | Recorded as **independent corroboration, no status changes**. 64→77×3 reclassified: a 77-problem, not a 64-problem (ear reads "qui [verb]"). Re-promotion of 64 stays **blocked**. 94="en" islets = LEAD-grade conditioned polyvalence. |
| e | Frenchman leads | 24="en" **STRONG LEAD** (sharpest ear-vs-stats tension recorded, see below). 52="pas" **STRONG LEAD bounded** (K5). 62="on" **STRONG LEAD** (strongest of batch; ear + recomputed 62→94 "on ne" ×8 at 1.97× in-band). 37="le" / 01="est" / 56="plus" / 43="me" **MEDIUM**. 17="fois" **WEAK**. No promotions. |
| f | Segmenter PARTIAL | **Method accepted.** The 5/23 provisional-boundary non-confirmation is **not anti-evidence** against 87=ce/96=par (metric muddling + model weakness; cela-internal 7/7 <0.5 mildly favors "cela" one word). 25 drag targets **cleared as LEAD-grade** with scorer-lesson caveats. |
| g | Cipher-model position | **Rigid syllabification is dead as an instrument** (tuner NULL + calibration + inconsistent encipherer cuts). Survives: cipher-side geometry, word-space grammatical kills, ear/formula locks, era unigrams as context. Era-syllable-conditional legs are invalid for morphological fragments. |

---

## (a) 78="me" — promotion REJECTED

**Recomputed from the archived `battery.py` (all reproduce unless noted):**
n(78)=31; L1 0.01679/0.01515=**1.108** ✓ in band. 78→40 ×3 ✓; era
('e','e') bigram n=**0** with eu['e']=5965 ✓. 11→78 ×2 ✓; cipher P=0.0455.
47→78 ×5 ✓; 37→78 ×4 ✓. L2b cipher top3 0.290 / era "me" top3 0.397 = **0.731** ✓.
L3b: era ('la','me') n=**154** ✓ ("la même"/"la mesure" coherent).

**B-78a — the "e"-kill is VOID (syllabifier artifact).** The kill's logic:
78→40 ×3 as "e"+"e" vs era ("e","e")=0. But the era model's bare-'e' syllable
(eu=5965) is a different distributional object than the cipher's 40="e". The
era tokenizer almost never emits a word-final bare 'e' ("rue"→'rue',
"première"→'pre','mie','re'); its 'e' syllables are word-initial fragments
('e','tats' 979×, 'e','tre' 474×). The cipher's 40 is the word-final mute-e
writer (crib "première" = pre|m|i|er|**e**). ("e","e")=0 measures the era
tokenizer's habits, not French grammar. The kill cannot bear weight — same
disease as the 29/82 exclusion (M2), one group further down. **Consequence:
40="e" CONDITIONAL/attestation legs are uncalibrated** (unigram 0.71× stays as
context). "e" returns as a live rival for 78 (L1 1.044 in band).

**B-78b — the L2 leg is miscomputed (wrong marginal).** Closer reported
era P(me|la)=0.0274, ratio 1.66× in band. Recomputed: eb[('la','me')]=154,
eu['la']=7652 → P=**0.0201**, ratio **2.26× — out of band**. 154/5617=0.0274:
the closer divided by eu['me'] (the wrong marginal — that's P(la|me), not
P(me|la)). The headline L2 leg does not reproduce from the archived code
(M6 traceability break, load-bearing).

**Weakened (not broken):** the "même" joint (47→78 ×5 + 37→78 ×4) is
era-coherent (era ('me','me') n=827, P=0.147) but circular as a promotion leg —
47="me"/37="me" are both unconfirmed (47 carries the 802× "par me"
contradiction; 37="me" has an L2 fail). Consistency note, not a leg.

**Survives:** the "l'"-kill — recomputed **stronger** than reported:
11→78 ×2 at 0.0455 vs era P(l|la)=0.0008 → **58×** (closer said 40.4×; the
direction holds, number corrected), and "la l'" is genuinely ungrammatical.
L1 in band; L3a otherwise clean; L3b coherent.

**Net:** 78="me" → **LEAD** (rival "l'" killed grammatically; rival "e"
unkilled; one in-band rate + clean attestation + coherence ≠ promotion).

## (b) The 77 three-way

**Recomputed:** n(77)=44. L1: "pas" **6.69×** ✓ (word-space: 5.21× — survives
the sense-mixing correction); "que" **1.645** ✓; "le" **0.982** ✓.
87=ce→77 ×2 (P=0.0625); 64=qui→77 ×3 (P=0.0652). Follower-cosine(77,46):
**0.198** ✓ reproduces. era ('qui','que')=**0** ✓.

**The closer's L2prov numbers do not reproduce and are not in archived code.**
`battery.py`'s `run_battery` only emits L2 rows for usable GT anchors — the
77 L2prov legs (all provisional-anchored) were hand-computed and pasted into
the JSON. No archived-code path yields the reported ratios under any of the
three era instruments (syllable cross-word / syllable within-word /
word-space). My recompute (cross-word syllable): "ce que" 1.32 (in band),
"ce pas" **57.5**, "ce le" 4.56, "qui pas" **78.5**, "qui le" 4.13. Direction
matches the closer's claims (the kills are, if anything, stronger), but the
legs are **unverifiable as stated** — mark them recomputed, not confirmed.

**77="pas": closer REFUTED → DISFAVORED (strong).** The closer's direction is
correct and my recomputed numbers support it: L1 5.2–6.7× out of band (robust
to syllable/word level), plus a genuinely grammatical leg — 87→77 ×2 adjacent
as "ce pas" is ungrammatical **under 87="ce"**. But REFUTED-grade needs an
unconditional leg; the grammatical leg is provisional-conditioned (87=ce) and
the band is uncalibrated (M3 standing). My N18 (INCONCLUSIVE) is therefore
refined, not overturned: the evidence now leans clearly against "pas".
**This is not a recycled void instrument** — the battery is a new instrument;
its weakness is the uncalibrated band + provisional anchors, not the void
phase mapping.

**77="que": the closer's 3-check LEAD does not overturn DISFAVORED.**
(1) All three checks (L1 1.645, L2b 1.78 ✓ reproduces, "ce que" 1.32
recomputed) are uncalibrated-band legs — none is grammatical or count-zero.
(2) The polyvalence cost stands: GT 46=que exists, cosine(77,46)=0.198 argues
against a shared reading. (3) **The frenchman's ear contradicts**: @790
`77 64 46 07` read as « qui que » + subjunctive ("qui que ce soit") — under
77="que" this is "que qui que", ungrammatical. The ear's own window kills the
reading at its crown example. (4) The L2prov leg is provisional-conditioned.
DISFAVORED stands.

**77="le": LEAD-weak accepted** (1 check; L2prov fails recomputed 4.6×/4.1×).

**New lead-direction (frenchman, ungraded):** his « qui [verbe] » reading of
64→77 ×3 and 77's top predecessors (06 ×6, 67 ×6 — verb stems) suggest 77 may
be verb-adjacent. Noted for round 4; no value proposed.

## (c) Calibration exclusion — VALID, with blast radius and one extension

**Reproduces:** 29=er **181.5×**, 82=m **61.1×**, 34=i **3.3×** over era;
usable anchors 11=la 1.15×, 46=que 1.08×, 40=e 0.71×, 70=pre 1.88× ✓. The
logic is sound: the cipher's morphological syllabification (keeps -er) vs the
era maximal-onset model — confirmed independently by the tuner's 67×
segmentation mismatch. Excluding 29/82/34 from rate/attestation legs is
correct.

**Blast radius — legs this voids:**
1. **My round-3 verdict-3 standing leg is VOID:** "06→29×5 strained as ent|er;
   needs enter-splits at ~2.4× the era enter-word rate." The er-rate comparison
   is uncalibrated — the leg is void. The 06="ent"-general REFUTED still stands
   (frenchman K1 ear kill, independent + the 06 unigram rate leg), but it no
   longer rests on the enter-word argument. Status of the refutation: UPHELD,
   legs reduced.
2. **The 06="ne" kill leg is VOID as era-uncalibrated:** "era ne+er-initial
   0/1793 vs 5/46" (cited as surviving in my §4). The era syllabifier never
   emits bare "er" word-initially, so 0/1793 measures the tokenizer, not
   French. No live claim affected (nobody claims 06="ne"; F21 is verb-stem).
3. **Closer's 94→82 "ne m'" void: endorsed** (already self-voided in
   single_legs — correct call).
4. **Unaffected:** 87="ce" rival battery + inversion (followers are
   la/qui/que — no er/m legs); 94="ne" unigram rate (1.025×); the 64→77×3
   anomaly (word-space P(pas|"qui")=0/2360); the 94-82-06/-rement trigram word
   rates; all cipher-side count legs (67→29=0, V29 membership, 86→29 ×4);
   every frenchman ear reading (no era rates involved).

**Red-team extension:** 40="e" CONDITIONAL legs are uncalibrated too (see
B-78a). The closer stopped the exclusion at 34; the 'e'-fragment evidence
forces it one step further for conditional/attestation use. 40's unigram
(0.71×) stays as context.

## (d) Frenchman K1–K7

- **K1 (06="ent" general): ACCEPT.** Independent ear corroboration of the
  standing kill (N19, upheld): "qui ent" / "ne ent la" ungrammatical (@1078,
  @1665, @318, @578, @758 — windows verified in the pair stream). Two
  instruments, same verdict. Bonus: @1181 shows the polyvalence naked
  (trigram-internal 06 vs following verb-stem 06) — supports restricted-"ent"
  PLAUSIBLE.
- **K2 (24="de" inside « en ce qui »): ACCEPT, scoped.** "de ce qui" is
  ungrammatical (@179, @1765 verified: `14 24 87 64 23` / `09 24 87 64 26`).
  Conditioned on provisional 87=ce/64=qui — the kill lives and dies with them.
  Does not touch 24="de" elsewhere (24 stays INCONCLUSIVE globally).
- **K3 (43="mi"/"parmi" in the ×2 formula): CONDITIONAL ONLY.** The kill
  assumes 87+01="c'est", i.e. 01="est" — itself an unconfirmed MEDIUM lead.
  Cannot enter the kill ledger until 01="est" confirms. Recorded as
  conditional; the formula stays "…par 43 c'est" with 43 open.
- **K4 (01="ci"): ACCEPT, provisional grade.** Recomputed: cipher P(01)=
  1.571% vs era syll P("ci")=0.409% → **3.84×** over (band-uncalibrated, noted);
  34→01 ("ici") ×0 ✓; the @295 leg ("16 est la" needs "est") is circular with
  the 01="est" lead and doesn't count independently. "ci" killed at
  provisional strength.
- **K5 (52="pas" as single reading): ACCEPT, scoped.** @160 verified:
  `…93 52 94 24 87 11…` — as "…93 pas ne…" ungrammatical; "per|so|nne" the
  coherent parse. Conditioned on provisional 94="ne". **This forces 52
  polyvalent** — bounds the frenchman's own STRONG "pas" lead (negation frames
  + word-internal values coexist).
- **K6 (own « ce n'est pas cela »): no action.** Self-kill recorded; honesty
  noted (missing-"est" catch is the right instinct).
- **K7 (56="plus" as single reading): REJECT as a kill.** Rests on @795
  "qui 56 37 44" = "qui a le 44", which assumes 37="le" (unconfirmed MEDIUM)
  with 44 unidentified — provisional-on-unconfirmed. Recorded as live tension:
  56 polyvalent ("plus" + "a"-class?) or the @795 parse is wrong.

**Ear-confirmations (87=ce, 64=qui, 96=par, 94=ne): independent corroboration,
no status changes** — the frenchman explicitly defers authority, and I hold
it. Notes: (i) the « parce que » ×3 / « ce qui » ×5 / « cela » ×7 /
« on ne prend pas » locks are compositional (grammatical, not rate-based) —
the strongest positive evidence these provisionals have; (ii) **64→77×3
reclassified**: the ear reads "qui [verb]" (verb unidentified), which
dissolves the round-3 anomaly's pressure on 64="qui" *under 77≠"pas"* — it
becomes a 77-problem. **64 re-promotion stays BLOCKED**: its check (b) still
conditions on a provisional, and an ear reading is not a second statistical
check. (iii) 94="en" islets @1168 ("en ce") / @1575 ("m'en") — windows
verified; LEAD-grade conditioned polyvalence, consistent with the
morphologist's "m'en" anomaly; @1741 still unreadable under both readings
(1/36, noted not fatal). (iv) Genuine conflict adjudicated: none — no
ear-verdict contradicts a statistical ruling at gradeable strength. The
@790 window contradicts the *closer's* 77="que" lead (see §b), not a ruling.

## (e) Frenchman leads — graded, collisions noted

- **24="en": STRONG LEAD.** Formula-locked: « en ce qui » ×2 (@179/@1765),
  « en plus » @73, « en cela » @73, « qu'en 85 » @952; rank 2 (2.82%) fits
  "en". **Collision — the sharpest ear-vs-stats tension of the round:**
  24→87 ×10 (P=0.192) vs era P(ce|en)≈0.006–0.007 → **26–31×** over (recomputed
  both instruments; the closer's 15.9× is hand-computed/unverifiable). Under
  87="ce", "en"+"ce" at 0.192 needs the despatch register to use "en ce/cela"
  far beyond Tocqueville essays — the frenchman's genre argument (« en cela »
  as reporter's anaphora) is the live defense, but it is unmeasured.
  Resolution path: formula-aware check on a diplomatic corpus, or decompose
  the 10 instances (3/10 are « en ce qui » frames). The failed L2prov does
  **not** kill the lead — it is unverifiable as stated and formula-blind.
- **52="pas": STRONG LEAD, bounded by K5.** « on ne prend pas » @1331
  (window verified: `56 30 06 62 94 70 52…`) and « ne pas [inf] » ×2
  byte-identical (@1293/@1806) are locks. K5 proves 52 does other duty
  ("per|so|nne") → polyvalent by necessity. **Collision:** closer's 52="se"
  LEAD (L1 1.191 + qui→52 r=1.32, provisional-flavored) stays live as the
  rival; both can hold under polyvalence.
- **62="on": STRONG LEAD — strongest of the batch.** Ear lock « on ne prend
  pas »; « on ne [verbe] » ×5+; "pers|on|ne" @508 (window verified:
  `77 62 94`) gives 62 word-internal "on" too. Statistical leg (recomputed,
  verifiable): 62→94 ×8 as "on ne": cipher 0.2353 vs era P(ne|on)=0.1194 →
  **1.97×** in band (word-space: 1.96× ✓). Note the closer's 62→94 ×8
  "te"-kill is exactly this leg wearing a rival's clothes. L1 4.27× over era
  is consistent with polyvalence (pronoun + word-internal "on"), not a kill.
  One more independent check → promotion candidate.
- **37="le": MEDIUM.** « le gouvernement » @1178 (window verified:
  `59 37 77 78 94 82 06`), « qui le [verbe] » ×3. Tension: @529/@1356/@1443
  "37 qui" reads "ce/celui qui", not "le". Rival: closer's 37="me" LEAD-weak
  (L1 perfect 1.001, L2 37→11 r=5.5 out).
- **01="est": MEDIUM.** @295 "16 est la 78" (window verified:
  `65 16 01 11 78`); « c'est »=87+01 in the ×2 formula. Underwrites
  K3-conditional and K4's third leg — if 01="est" confirms, K3 enters the
  ledger.
- **56="plus": MEDIUM, tension open.** « en plus » @73 vs K7-rejected
  @795 "qui a le 44". Polyvalence or misparse — ear can't distinguish from
  encipherer allophony (his own caveat, accepted).
- **43="me": MEDIUM, scoped outside the formula.** @43/@439 windows;
  K3 bounds it out of the ×2 formula only.
- **17="fois": WEAK.** Single window @1033 « la première 17 » (verified:
  `…11 70 82 34 29 40 17`). Awaiting a second instance.
- No promotions from ear alone (standing rule).

## (f) Segmenter — PARTIAL upheld, anti-evidence question adjudicated

**Method accepted.** GT checkpoint "la"+"première" @1033: 3/3 boundaries
≥0.5 out-of-sample (0.727/0.937/0.608), 3/4 internals <0.5 — the model found
the split unprompted. MAP lengths sane (958 words, mean 1.93 vs era 1.75,
χ²=121.8 vs 1446.2 prior-only). EM decontamination honest; ANCHOR variants
correctly flagged circular. The rotation-break signal is real (B→B never
within-word; EM π_C=0.578 highest, matching 29=er word-final-ish, untold).

**The 5/23 provisional-boundary non-confirmation is NOT anti-evidence against
87=ce/96=par.** Decomposition (from `segmenter_results.json` STRUCT_all):
cela spans contribute 4/14, parce-que 1/9, GT 3/3 = 8/26. Three reasons it
doesn't move status: (1) the metric muddles — cela-*internal* (87|11) scores
<0.5 in **7/7** (mean ~0.40), which is the model *correctly* not splitting
"cela"; counting internals as boundary misses misreads the instrument.
(2) The true boundary parce|que (87|46) scores 0.395/0.48/0.346 — the
rotation-break signal is simply weak there, while the ear's grammatical locks
("parce que" ×3 byte-identical) are stronger evidence than this uncalibrated
boundary instrument. (3) The frenchman's inconsistent-segmentation
enlightenment *predicts* this: a boundary model assuming consistent word
structure underperforms on inconsistently-cut text; the GT span passes
because it's cleanly cut. Verdict: model weakness + metric muddling, not a
read indictment. 87=ce/96=par statuses unchanged. (Side: cela-internal <0.5
mildly favors "cela" one word — weak supporting, not a promotion leg.)

**25 drag targets: CLEARED as LEAD-grade round-4 crib-drag targets.**
Caveats (scorer lesson, BROKEN-ON-CONTROL upheld): any drag built on them
needs its own pre-registered control; targets overlapping provisional-read
groups inherit provisional uncertainty; this is not a decode map. Targets of
interest: @507-509 [77 62 94], @1703-1705 [62 94 88] ("on ne"-adjacent under
leads), @81-83 [51 62 16], @1110-1112 [41 65 38].

## (g) Lane position: what the three newcomers jointly mean for the cipher model

**Rigid syllabification is dead as an instrument.** Three independent kills:
(1) tuner NULL (phase≠position) stands — the segmenter honored it and still
got signal from rotation-break alone, which is the best possible obituary;
(2) calibration: the era maximal-onset syllabifier ≠ the encipherer's
segmentation (29/82/34 excluded; 40-conditionals excluded per B-78a);
(3) the frenchman's enlightenment: the encipherer **spells by ear and cuts
inconsistently** — « prend »→« pre », « personne » as « per|so|nne » AND
« pers|on|ne » (two spellings of one word in one cipher), « erre »→« er|e »,
« première »→« pre|m|i|er|e » down to single letters. A fixed segmentation —
era's or any other — cannot be the comparison instrument against a cutter
this loose. This also explains the tuner's LOO failure and F22: rigid
syllable-position statistics patent on inconsistent segmentation.

**What survives:**
1. **Cipher-side distributional geometry** — follower/predecessor counts and
   count-zeros (67→29=0, 06→29 ×5, V29 as a *structural* class with M8's
   contamination warning attached). These never needed the era.
2. **Word-space grammatical kills** — "ce pas", "la l'", "de ce qui":
   constructions, not rates. Syllable-space attestation is void for fragments.
3. **Ear/formula locks** — « parce que » ×3, « ce qui » ×5, « on ne prend
   pas »: the frenchman is right that the ear is the *better* instrument here,
   precisely because it tolerates inconsistent segmentation.
4. **Era unigram rates as context only** — band uncalibrated (M3 standing).
5. **The morphological-syllabary hypothesis as the recovery target** — tuner
   step 2 (read `data/upstream-syll*.py`): the cipher's "syllables" are
   morphological/phonetic fragments. Until the syllabary is recovered, no
   era-conditional leg on a fragment group is valid.

**Explicit rule for round 4+:** no era-syllable-conditional rate or
attestation leg on any group whose hypothesized value is a morphological
fragment (29, 82, 34 excluded; 40-conditionals excluded; all single-letter
fragments suspect). Era word-space legs survive. New fragment hypotheses must
be tested against the recovered syllabary, not Tocqueville's.

---

## Updated round-3 ledger (3 + 3b combined)

**KILLS (hard):** 06=/mɑ̃/ "demand-/command-" CONFIRMED — ground-truth
contradiction (crib writes mute -e as 40).
**KILLS (provisional):** 01="ci" (3b, K4: 3.84× + "ici" ×0).
**KILLS (scoped):** 24="de" inside « en ce qui » (3b, K2; conditioned on
87=ce/64=qui); 52="pas" as *single* reading (3b, K5; conditioned on 94=ne;
forces 52 polyvalence).
**KILLS (conditional — not in ledger until condition met):** 43="parmi" in the
×2 formula (needs 01="est").
**KILL CLAIMS REJECTED:** 56="plus" single-reading (K7; provisional-on-
unconfirmed).
**DEMOTIONS:** 87="ce" CONFIRMED→PROVISIONAL (strengthened); 94="ne"
CONFIRMED→PROVISIONAL (strong); 06 verb-stem class CONFIRMED→PROVISIONAL;
06 polyvalent CONFIRMED→PLAUSIBLE; 67="veut"-class CONFIRMED→PROVISIONAL
("veut" PLAUSIBLE); 77="pas" CONFIRMED→INCONCLUSIVE→**DISFAVORED (strong)**
(3b revision); tension "DISSOLVED"→OPEN.
**REFUTED→DISFAVORED (stands):** 77="que"; 06="ent" general REFUTED (upheld,
legs reduced per §c).
**VOIDED LEGS/INSTRUMENTS:** phase→position (tuner); 06 "ent|er strained"
2.4× leg (3b, er-rate uncalibrated); 06="ne" ne+er-initial leg (3b, no live
claim affected); closer 94→82 "ne m'" (self-voided, endorsed); closer 78="e"
L3a kill (3b, B-78a syllabifier artifact); closer 78="me" L2 leg (3b, B-78b
wrong marginal); closer 77 L2prov legs as stated (3b, hand-computed,
unverifiable — recomputed stronger but provisional-conditioned); closer 94
"ne se" 5/36 pooling (3b — mixes « ne pas » ×2 with word-internal 52; the
94→59 ×2 "ne se" r=1.48 piece survives).
**PROMOTIONS:** none. 78="me" promotion REJECTED → LEAD. 62="on" STRONG LEAD
(promotion candidate, one independent check short).
**UPHELD:** -ment family PLAUSIBLE; scorer BROKEN-ON-CONTROL; tuner NULL;
segmenter PARTIAL (method validated; 25 targets cleared as LEAD-grade).

## Best next step

1. **Repair the battery and re-run 77/78 cleanly** — fix the B-78b marginal
   bug, compute L2prov in archived code (word-space for function-word
   bigrams), re-grade. The 77/78 verdicts currently rest on hand-computed
   legs.
2. **62="on" is one independent check from promotion** (ear lock + 62→94
   "on ne" ×8 at 1.97× recomputed). A distributional or positional third leg
   promotes it — the lane's first promotion since the demotions.
3. **Resolve 47** — the frenchman's biggest neighborhood jar (« …ce qui par
   47 que… » @148–150); the 47="me" 802× contradiction vs the "même" joint
   can't both stand.
4. **Read `data/upstream-syll*.py`** (tuner step 2) — recover the encipherer's
   syllabary; rebuild fragment comparison on it per §g.
5. **Round-4 drag on the 25 segmenter targets with a pre-registered control**
   (scorer lesson) — targets inherit provisional uncertainty where they touch
   provisional reads.

## Caveats (not verified)

- Elision handling still uncalibrated (round-2 standing).
- Injectivity questioned, not replaced — polyvalence is now the working
  assumption for 06, 52, 56, 62 (ear-observed), with 47/37/78 "me" as the
  statistical polyvalence candidate.
- Era corpus remains Tocqueville essays, not despatches; the frenchman's
  genre-reclassification of the cela gap is plausible but unmeasured.
- The closer's Les-Mis leg figures remain the closer's (audited round 3).
- 94="re" ("-rement") rival still red-team-constructed, not worker-tested.
- `/tmp/rt3b_recompute.py` is ephemeral; the numbers above reproduce from
  `code/crib_attack.py` + `code/crowd3/battery.py` as documented.
- No GitHub push (per WO). No crack claim.
