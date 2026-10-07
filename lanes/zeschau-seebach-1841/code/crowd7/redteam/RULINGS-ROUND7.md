# Round-7 Red-Team Adjudication — executor status-change recommendations

Red team: round-7 red-team adjudicator · 2026-10-07 · kill authority over round-7 promotions.
Scope: the 8 recommendation packages in `code/crowd7/report_inbox/` (round-7 executors).
Method: independent re-derivation on the repaired 1,847-pair stream
(`code/side-keyhunt/repaired_offsets.json`; positions per
`code/crowd7/redteam/verify_f26_17.py`, 61/61 PASS). Corpus claims re-derived
with an independently written tokenizer (elision-split, per round-5 convention),
not by re-running executor scripts. New extension checks:
`code/crowd7/redteam/verify_round7.py` **45/45 PASS**.
Pre-registered bars enforced; exact tests; N28/N35 case law; F33 conditioning
(zero free cases, falsifiable); no double-counting.

## Ruling 1 — Conditioner (84 + 00 conflicts)

**GRANTED in full.** Every load-bearing number re-derives exactly on the
repaired stream; the diplomatic pipeline reproduces byte-exact under an
independent implementation.

- 84 table: n=25; en-class @[(167,82,53),(310,46,24),(473,46,24),(1665,94,64)]
  (n=4, n_eff=3 — 310/473 byte-identical 46-84-24); noun-class 8 windows
  (n_eff=6 — (77,84,9)×2 and (77,84,59)×2); 13 free windows with exactly the
  reported predecessors {66×2, 89×2, 91, 53×2, 65, 48, 06, 17, 32, 74}
  @[154,276,391,412,788,857,1021,1151,1189,1290,1378,1418,1501]. The 13 are
  honestly unclassified — no post-hoc fitting attempted (F33 honored).
- (a) 84="en" conditioned islet (pre∈{46,94,82}) → **LEAD** (n_eff=3).
  @1665 "n'en qui" is a genuine single adverse (94="ne" prov-strong); n=1,
  not kill-grade under the lane's n≥3 kill rule. Fenced, not hidden.
- (b) 84=masculine-noun islet (pre∈{77,11}) → **LEAD** (n_eff=6).
  Zero adverses; identity NULL (honest). @1620 «la X»+78 is soft tension
  only (78 polyvalent) — correctly not graded as adverse.
- Both unconditioned 84 claims **KILLED** — the side comparison is sound:
  en-only dies on E4 + "la en" @1620 + 13 unexplained windows; noun-only
  dies on the GT-anchored "qu'en"×2 (n_eff=1) and "m'en". E4 dissolves
  correctly: all seven 77→84 windows are noun-class, so the blocker applies
  to zero en-islet occurrences.
- (c) 00="le" conditioned islet (pre=96, @47/465/960, successors 92/33/86)
  → **LEAD** (n_eff=3, non-byte-identical). C2/C3/C4 pass as pre-registered:
  00→86 12→11 excl. pre=96 (the 12th is the @960 le-window itself — honest),
  00→06 0, 06→00 4, 00→46 4, 00→11 4 all survive the drop.
- (d) 00="pour" **stays STRONG LEAD** — C1 FAILS honestly: no diplomatic
  register brings r1 or r3 ≤2× (despatches-primary r1=9.14×/r3=3.27×;
  full r1=5.05×/r3=4.00×; per-file r1 ∈ [4.01,15.36]×; method-parity
  Tocqueville re-derivation reproduces B1=6.22×/B3=3.85× exactly under my
  own tokenizer). Blockers B1/B3 stand; no provisional.
- Bar note: PREREG B2's letter ("≥1 unrepairable break ⇒ side fails") is
  stricter than the verdict (en-islet kept at LEAD with the @1665 adverse);
  the lane's standing n≥3 kill rule resolves the tension, and the note is
  transparent about it. The decision tree didn't explicitly pre-authorize
  banking two islets after both-sides-killed, but both islets were
  pre-registered constructs with passing coherence bars — acceptable.

## Ruling 2 — Closer (59="est" promotion battery)

**GRANTED with modification: 59="est" → provisional.** The 01="est"
MEDIUM→WEAK recommendation is **DENIED** as a battery outcome (see below).

- Blocker (a) S4 resolved per pre-registered L1 (the verdict rule needed
  L1 OR L2; L2 honestly FAILS — S4#1's frame remains structurally
  unexplained, disclosed as caveat 3). Diplomatic P(que|est) re-derived:
  Guizot t5–t6 0.0213 / Nesselrode v8 0.0414 / aggregate 0.0249 — exact.
  Binomial P(X≥2|n=27): 0.112/0.308/0.145, none <0.05 ✓; ratio shrinks
  5.41× → 3.48×/1.79×/2.97× ✓ (register attribution, as L1 required);
  cipher 95% CI [0.009,0.243] contains Guizot's rate ✓.
- Blocker (b): resolved in the **weak sense licensed by the verdict rule's
  own wording** ("01='est' shown to cost 59 nothing"): every one of 59's
  legs (S1/S2/S3, L1/L3/L4/L5) is 01-independent; I3 shows @824
  ([...,24,87,59,38,...]) is hostile-neutral under banked values, so the
  allophony claim there is unsupported either way. I1's >3× bar fires on
  Guizot (4.74×) and aggregate (3.72×) but is borderline on Nesselrode v8
  (2.24×) — the register-best comparator — so it does NOT cleanly reject
  both-hold; I2's own bar (verb-shaped profile: 37→01 ×3, 87→01 ×2,
  47→01 ×1, 01→11/01→77 ×1 each — all re-derived) keeps F33-class
  allophony live. The note's upgrade to "mutual exclusivity (59 wins)" is
  post-hoc conjunction (6/6 split p=0.0140 ✓ arithmetic, shared
  predecessors {15,16,48,76,86,87} ✓, shared followers {19,24} ✓) with no
  pre-registered bar — **not granted**. The 6/6 p=0.014 datum is banked as
  a leg for a future 01 battery; the demotion needs its own pre-registered
  battery. 01="est" stays MEDIUM.
- L3 (S2): 64→59 ×3/47=0.0638 vs 0.026/0.085/0.033 → 2.45×/0.75×/1.92×,
  P(X≥3)=0.12–0.78 n.s. ✓. L4 (S3): 94→59 ×3/37=0.0811 vs
  0.134/0.230/0.192 → 0.35–0.61× ✓. L5: rivals doute/dit/fait/veut/peut at
  40.4×/16.5×/9.1×/50.9×/12.6× from cipher P(59)=0.01462 — kills stand,
  stronger than Tocqueville's 7–45× ✓; "est" unique survivor at 1.10× vs
  Nesselrode v8 (1.83× aggregate) ✓.
- ≥2 independent legs: L1, L3, L4, L5 pass (different cipher cells per the
  pre-registered independence definition) ✓. S5 (59→37 ×6) stays fenced on
  37="le" MEDIUM — disclosed, not re-litigated.
- Traceability nit: PRE-REGISTER.md cites "64→59 ×3 @315/1209/1795" then
  "@[1209]/1776"; actuals are @315/1209/1776. Counts correct.

## Ruling 3 — Morphologist (47="ce" unblock + 67 classification)

**GRANTED.** The WO-10 leg is the round's strongest independent confirmation.

- 47="ce": **BLOCKED → LEAD (strengthened)**. The diplomatic-corpus leg
  reproduces EXACTLY under my independent frame-miner (own code, own file
  subset): "ce qui [gap 1–3] ce que" = 5 frames, every filler verb-led
  ("est et" Guizot t5–t6; "est et attendons" Nesselrode v9; "paraît
  certain" + "renverse tout" RDM 1841-q2; "arriva" RDM 1841-q3), and
  "ce qui par ce que" = 0. Independent three ways (new register-matched
  corpus, new instrument, new direction — constrains the slot's filler
  class, not 47's value). Cipher-side census re-derives: 64-96-47 @149–151
  (the residual), 47→46 @151/548/864 only, 64→47 @1271/1717 ("qui ce").
  Promotion to provisional NOT claimed — correctly scoped.
- 96=verb conditioned reading (pre==64 & suc==47, n_eff=1) → **LEAD**.
  F33-falsifiable; needs a second 64-96-47 window or independent 96-as-verb
  datum before any promotion (same n_eff=1 precedent as the T4 islets).
  Does not disturb 96="par" provisional elsewhere.
- 67 et/veut fork **stays SUPPORTED** — no status change. 29/38 classified
  (et=18, veut=11, open=9; open list [199,630,633,902,1248,1372,1450,1519,
  1623] re-derives from battery67_final.json; **zero BOTH conflicts**).
  Era legs reproduce exactly on Tocqueville (221,059 tok): "et la"=196 vs
  "veut la"=0; "et le"=185 vs "veut le"=2; "et par"=38 vs "veut par"=1;
  "la et"=0 vs "la veut"=1. The @506 collision is adjudicated (veut), not
  absorbed; the fence is placed on the new rule R_et5. R_et6 (n=1 @959)
  honestly flagged thin. Neither "et" nor "veut" promoted — binarity is
  the claim, correctly.

## Ruling 4 — Frenchman (62="on" + gouv/er)

**GRANTED (no change).** All four unblockers honestly NULL; the discriminating
math re-derives exactly.

- 62="on" **stays fenced STRONG LEAD** (ear legs 1&3 only). U1/U2/U3 nulls
  verified: diplomatic P(qu'|on)=0.3088 (mine: 0.30880, n=391,210) vs
  Tocqueville 0.2475 ✓; Leg-1(c) adverse E=8.96, p=2.23e-5 ✓ (single datum,
  same 4 caveats — correctly not kill-grade, not promotion-grade).
  93="l'": n=14 vs E≈32.0, Poisson P(X≤14)=2.94e-4 ✓ — shape-STRONG but
  rate-KILLED, banked as such, NOT promoted ✓ honest.
- 77="gouv"/78="er" islets **stay LEAD (conditioned, n_eff=1)**. U5 null
  verified: the 5-mer 77-78-94-82-06 occurs exactly 2× (@1180/@1351) ✓;
  @647 reads [77,78,52,82,94] — not a second "gouvernement" ✓. The T4
  ruling's open items remain open.
- **FLAG — unadjudicated referral:** frenchman graded 48 as LEAD
  "ne"-allophone but explicitly referred it to WO6 (keystruct), and
  keystruct's battery (M1–M9) contains **no 48 candidate** — 48 appears
  only inside contact lists. The referral is UNTESTED. The "LEAD" label in
  the worker note must NOT enter the lane status line; 48="ne"-allophone
  is an unbanked hypothesis until a homophone battery tests it.

## Ruling 5 — Key-structure (aliasing battery)

**UPHELD.** Load-bearing numbers re-derive; no merger reaches
promotion-grade (B1–B5); the negative results are precise.

- M1 unconditioned {87,47}="ce" merger **REFUTED**: P(64|87)=5/32=0.15625
  re-derived, P(64|47)=0/28 re-derived, interchange kill-shot
  p=(0.84375)^28=**0.00859** ✓ exact. The conditioned "ce" homophone set
  (Q1/Q2) stays LEAD — sharpened, not promotion-grade (Q1 thin; 13/28 of
  47's frames unclassified = F33 free cases; B5 not met — honestly stated).
- M2 {77,00}="le" **REFUTED**: similarity z=−0.56 (null); merged 2.60×
  over era le-syllable (singles 1.16×/1.44× — arithmetic ✓). The 00="le"
  question stays a WO-2 conditioned-polyvalence matter (now banked per
  Ruling 1), not a merger — consistent.
- M8 {43,21}="me" **REFUTED**: merged 3.28× over era me-syllable
  (32.9× over word-"me") ✓; zero shared followers ✓ re-derived.
- M3/M4/M5/M6 **INSUFFICIENT** (one weak leg each or less) — honest;
  M7 CONDITIONAL on WO-4 (16="i" unconfirmed) — correctly held.
  Instrument note: keystruct's era uses P("est")=0.01078 (its own
  215,246-word tokenization) vs F45's 0.01054 — instrument difference,
  verdict-neutral.
- Ranked proposals accepted as stated; **no merger promotion-grade**.

## Ruling 6 — Patternist (16="i" + Mehemet-Ali)

**GRANTED (HOLD/HOLD).** Both holds are honest and conservative.

- 16="i" **stays LEAD**: B1 clean FAIL (permutation p=0.8374/0.9291 —
  contact-coherent-dealing prediction does NOT hold unconditioned;
  correctly redirects to an UNTESTED position-conditioned alternative,
  not promoted on); B2 mechanical pass but thin (informative subset 6
  windows, 'i'-unique at @381/@1831 only, n_eff=2; @1386 exclusion
  discounted as lexicon-coverage artifact — honest); B3 weak
  no-contradiction. Two thin passes ≠ promotion ✓.
- "Mehemet-Ali" @8 **stays LEAD**: M0 null 0.28% ✓; M1 honestly VOIDED
  (bearing-count is a structural constant of anchor placement — the
  worker caught its own design flaw); M2 spelling PASS (both accent
  forms attested; the "293× RdDM" figure flagged UNVERIFIED, not cited
  ✓); M3 weak pass (33 common-word rivals at the same null — possible,
  not preferred); Mohamed cleanly excluded; silent-h adverse discharged
  (t/d indifferent by ear). Dependency recorded: falls with the 78="me"
  islet.

## Ruling 7 — Segmenter (rotation round 7)

**CONFIRMED — no value-reading status change smuggled.** Results files
match the note: flag audit re-derives gate z=5.81 and P2a (r1=0.6327/
r0=0.4856, z=4.77); label-free momentum INCONCLUSIVE (n0=49<50 guard,
pre-registered conservativeness mechanism confirmed empirically — r0=1.00
re-sync artifact); coda-column refuge WEAKENED (Tocqueville lag-3 z=11.9
but flat profile; plaintext momentum z=−64.91, noise-stable sign).
Two package-internal verdict changes are disclosed and are NOT
value-status changes: P2c fixed-column-order FALSIFIED→**INCONCLUSIVE**,
and the columns refuge **WEAKENED**. Coordinator should record these as
rotation-package verdict updates; they touch no cipher-value status.

## Ruling 8 — Search designer (joint-inference search family)

**GRANTED: KILL the search-family bake-off; scope search to zero until the
objective passes C1 on the register-gapped family.** The C1-analog failure
is real and not a harness bug.

- 3/3 fresh instances: truth below random keys — 184207: −3.5269 < −3.2998
  (gap −0.24); 184208: −3.5818 < −3.3044; 184209: −3.5727 < −3.3310
  (worst gap −0.28) ✓ re-derived from diagnose.json/c1x2.json.
- Airtight argmax test: baseline SA on 184207 reaches −3.2898 (above
  truth) while the sealed-key gate scores — re-derived with the scorer's
  own logic against keys the search never reads — PRIMARY 0.0112 (1/89),
  SECONDARY 0.1148, proj_equiv 0.0112, islets 0/6 ✓ exact. The objective's
  optimum is truth-orthogonal; no search can pass the 6-check gate against
  it. The mechanism is identified (letter term register-saturated: truth
  only +0.09 nats/letter over char-shuffled noise; LAM_POLY −0.30 penalty
  on truth's 6 islets vs +0.12 letter+word advantage).
- Methodology-bug reports check out: solver.py:726 `anneal()` calls
  `init_key()` (would wipe a perturbed-truth start — the N40-era basin
  test's bug is real). These don't touch the C1-analog conclusion.
- The recommendation follows: iterate on the objective first (letter-term
  backoff/interpolation, register-robust training, LAM_POLY re-examined
  on the gapped family), THEN run the banked prototype vs baseline at
  equal proposal budget. R5005 untouched ✓.
- Traceability nits: the note cites `runs/baseline/` and
  `runs/baseline_one/` interchangeably (both contain asg-184207.json);
  score_fresh.py asserts all 6 seeds per tag so it can't score a
  single-seed tag as-is (I re-ran its exact logic inline — scores match).

## Bars misapplied (round-7 scope)

1. **Closer I1/I2 → "mutual exclusivity / 01→WEAK"** (see Ruling 2). The
   pre-registered bars support only the weak resolution (01 costs 59
   nothing); the demotion recommendation is post-hoc. DENIED pending a
   dedicated 01 battery.
2. **Conditioner B2 letter vs verdict** — the @1665 adverse vs "≥1
   unrepairable break ⇒ side fails"; resolved by the lane's standing n≥3
   kill rule, transparently. No ruling change.
3. **48="ne"-allophone referral untested** (Ruling 4 FLAG) — a WO6 work
   item that produced no test. Not a bar misapplication, but a gap the
   coordinator must not let become a banked status by drift.
4. **Traceability nits** (no verdict impact): closer PRE-REGISTER position
   typo (@315/1209/1795 vs actual @315/1209/1776); search note's
   runs/baseline vs runs/baseline_one; score_fresh.py's all-seeds assert.

## Final merged status-change list (for the coordinator)

**MERGE (granted):**
- 59="est": STRONG LEAD → **provisional** (L1/L3/L4/L5; (a) resolved,
  (b) resolved-weak; S5 fenced on 37="le" MEDIUM; S4#1 frame unexplained —
  disclosed residuals, provisional is the right grade)
- 47="ce": BLOCKED → **LEAD** (strengthened, +1 diplomatic-corpus era leg)
- 84="en" (unconditioned): LEAD → **KILLED**; replaced by conditioned
  islet 84="en" iff pre∈{46,94,82} at **LEAD** (n_eff=3; @1665 adverse fenced)
- 84=masc-noun (unconditioned): LEAD → **KILLED**; replaced by conditioned
  islet 84=noun iff pre∈{77,11} at **LEAD** (n_eff=6; identity NULL)
- 00="le": re-banked as conditioned islet (iff pre=96) at **LEAD**
  (n_eff=3; provisional-dependent; tension vs F40/F47 stands)
- 96: new conditioned reading 96=verb iff pre==64 & suc==47 at **LEAD**
  (n_eff=1; needs second window for promotion)
- Keystruct: no status changes; unconditioned {87,47}="ce" merger
  **REFUTED** (p=0.00859); {77,00}="le" **REFUTED**; {43,21}="me"
  **REFUTED**; conditioned "ce" set stays LEAD (not promotion-grade)

**NO CHANGE (granted holds):**
- 00="pour" stays STRONG LEAD (B1/B3 block provisional)
- 62="on" stays fenced STRONG LEAD; 77="gouv"/78="er" stay LEAD (n_eff=1)
- 16="i" stays LEAD; "Mehemet-Ali" @8 stays LEAD; 67 fork stays SUPPORTED
- Rotation package: no value-status changes (P2c→INCONCLUSIVE and refuge
  WEAKENED recorded as package-verdict updates)
- Search lane: bake-off KILLED; search scoped to zero until C1 passes on
  the register-gapped family

**DENIED:**
- 01="est" MEDIUM→WEAK — no pre-registered bar; needs its own battery
  (6/6 p=0.014 datum banked toward it)

**FLAGGED (not banked):**
- 48="ne"-allophone: unadjudicated WO6 referral — must not enter the
  status line until tested
