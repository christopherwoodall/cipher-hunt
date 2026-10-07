# PRE-REGISTER — 48="ne"-allophone dedicated battery (round-8 WO1, homophonist)

Written 2026-10-07 BEFORE any stream access by this executor. All numbers
below are derived fresh afterward against the repaired 1,847-pair parse.

## Claim under test
48 is a "ne"-allophone: homophone set {94,48}="ne", where 94="ne" is
provisional-strong (era syllable rate 1.025×; 94-82-06 trigram frame).
Referral (frenchman U4, round 7, UNADJUDICATED — F58): 48 (n=38), flat
followers (19 distinct/38, syllable-like), predecessor cosine 0.735 vs 94
(shared 62/12/82 predecessors; noise floor 0.475). Tension: 48→47 ×2
("ne ce" ungrammatical if 47="ce" LEAD holds there). The "LEAD" label must
NOT enter the lane status line until this battery rules.

## Frame
F33 conditioned-polyvalence rules B1–B5 (battery frame per F47's 00="pour"
battery: B1 unigram rate · B2 governor-frame counts/rates · B3 bigram-context
rate · B4 rival grammatical kills (era-0 bigrams) · B5 precedent counts) +
the F56 interchangeability kill template (M1: P(64|87)=5/32 vs P(64|47)=0/28,
Fisher p=0.0086 — same-phase aliases must share every contact cell) +
M1–M9 battery design E1–E7 (phase separation · coherence · disjointness ·
merged-vs-single era fit · phase-explained split · merged unigram · raw tops).

"Allophone" here = 1 sound → 2 groups (homophony), the reverse direction of
F33's 1 group → N sounds. F35 structural priors expect sparse homophones on
frequent syllables ("ne" qualifies). Free (unconditioned) homophony must
survive the F56 template; phase-separated pairs run the E5/M2 frame instead.

## Instruments (continuity, not result-sharing)
- Stream: `aliasing.load_stream()` — repaired 1,847-pair parse
  (`code/side-keyhunt/repaired_offsets.json`), same loader as the M1–M9 battery.
- Phases: `aliasing.phase_labels` / shared `phase_cache.json` (noisy per N43 —
  never sole basis; H1's phase branch is one leg among six).
- Era: `code/crowd7/closer/diplomatic_rates.json` PRIMARY (diplomatic register
  for a diplomatic cipher), `code/crowd7/keystruct/era_rates.json` secondary.

## Predecessor-cosine datum
The referral's predecessor cosine 0.735 (floor 0.475) is the REFERRAL'S datum.
This battery RE-DERIVES it (must reproduce ≥0.70 vs a recomputed floor ≤0.50
or flag instrument drift) but does NOT score it as an independent leg.
The follower-side cosine (never computed by the Frenchman) IS scored (H4).

## Checks (all re-derived)

- **P0 instrument check.** n48, n94, phase(94), phase(48), full contact
  profiles from the repaired stream. Referral says n48=38; mismatch → flag
  parse drift, do not proceed silently.

- **H1 interchangeability (F56 template; scored).**
  Read phase(94), phase(48) from the shared phase instrument.
  (a) SAME phase (both non-R): take 94's top follower cell and top
  predecessor cell (by count — a rule, not a value). For each, Fisher exact
  2×2 [[94→cell, 94→¬cell],[48→cell, 48→¬cell]]. KILL bar: p<0.01 AND anchor
  count ≥4 AND other =0 in either cell → unconditioned merger REFUTED
  (exact F56 analog). No multiple-testing correction: 2 pre-registered cells
  only; further cells reported exploratory.
  (b) PHASE-SEPARATED (non-R, different): the straight F56 template does NOT
  apply (M2 precedent: {77,00}="le" survived E1/T2). Run E5 phase-explained
  split: Fisher on the phase×alias contact table + falsifier rate.
  SUPPORT bar: fals_rate <0.25 and phase-table Fisher p<0.05. Adverse bar:
  fals_rate ≥0.40.
  (c) Either phase R: H1 NULL (instrument cannot place them).

- **H2 B1 merged unigram (scored).** ratio = ((n94+n48)/N)/era_P("ne").
  Era P("ne"): diplomatic syllable rate if present, else Tocqueville 0.01902
  (94="ne" was banked at 1.025× on 0.01950 vs 0.01902).
  Bars: 0.5–2.0 → PASS leg (F20 band). 2–3 → weak-adverse (fence, not scored).
  >3 → KILL leg (rate-incoherent; precedent: 00="pour" B1 6.22× = blocker).
  Report singles too: if n94/N alone ≥2× era, the set is overstuffed → adverse.

- **H3 "ne"-frame B2/B4 (scored).** Era lock: "ne" pairs with "pas" (52="pas"
  is a lane value). Compute 94→52, 48→52, and 48's contacts against era "ne"'s
  top-5 followers (diplomatic; Tocqueville backup).
  (i) If E[48→52] under 94's observed P(52|94) is <1.5 → the pas-cell check
  is NULL (underpowered — "ne" without "pas" is grammatical: ne explétif,
  "ne…que/jamais", so a zero here alone never kills).
  (ii) B4 rival-kill shape: adverse iff 48 takes NONE of era "ne"'s top-5
  followers while 94 takes ≥3 of them. PASS iff 48 shares ≥1 of 94's observed
  "ne"-licensed follower cells (52 or any top-5 era follower) at a rate within
  0.25–4× of 94's rate there.
  (iii) B4 era-0 scan: any 48 contact cell (follower or predecessor) with
  cipher count ≥2 and era count 0 for "ne" on BOTH diplomatic and Tocqueville
  → adverse leg (ungrammatical contact). The known candidate 48→47 ×2
  ("ne ce") is evaluated under H5, not double-counted here.

- **H4 follower-profile cosine (scored; NEW vs the referral).**
  cosine(follower-profile(48), follower-profile(94)); floor = median of
  cosine(follower-profile(48), follower-profile(g)) over all g with n≥20.
  Bars: ≥0.60 → PASS leg. ≤ floor → adverse. Between → null.

- **H5 48→47 ×2 tension (fence-or-adverse; scored once).** List both windows
  (repaired positions). Apply 47's conditioned "ce" rule (LEAD): if the rule
  permits non-"ce" at both windows → tension FENCED (neutral, recorded).
  If 47 is forced "ce" at either window → 1 adverse leg ("ne ce"
  ungrammatical). Both forced → still 1 adverse (single phenomenon, no
  double-count).

- **H6 E4 merged-vs-single era fit (scored iff instrument exists).**
  If `era_rates.json` carries "ne" follower/predecessor contact models:
  xent(merged 94+48 follower dist) vs xent(94-alone) against era "ne".
  Bars: merged better by >0.3 nats → PASS leg; merged worse by >0.3 nats →
  adverse; else null. If "ne" has no contact model → H6 NULL (recorded, not
  a fail).

## Verdict rules
- **CONFIRM** (48="ne"-allophone → LEAD, never higher — single round, n=38,
  red team adjudicates): ≥2 scored legs PASS, zero kills, H1 not firing its
  kill, H5 fenced-or-neutral.
- **KILL**: H1 kill fires, OR H2 >3×, OR ≥2 independent adverse legs.
- **HONEST NULL**: everything else (underpowered, mixed, or fenced tensions).

## Guards
- No double-counting: predecessor cosine = referral verification only; H5's
  "ne ce" not counted in H3(iii); the two H1 cells only.
- The 48="ne" STANDALONE reading (48 as its own value, not 94's alias) is not
  tested: under F33 it would be free polyvalence of 94's sound, which the
  homophone-set frame subsumes. If {94,48} dies but 48-alone fits "ne"
  perfectly, record as residual, not a promotion.
- Independent of all other round-8 executors. Report note to
  `code/crowd8/report_inbox/homophonist-48-ne.md` per REPORTING.md.

## What would change the verdict
- CONFIRM→provisional: a second independent round (different instrument,
  e.g. grammatical-frame battery on 48's verb governors) + red-team ruling.
- KILL→reopen: a verified conditioning rule (phase/lexical, F33-grade) that
  explains the killing cell, or demonstration that the killing cell is a
  parse artifact (bedrock re-audit).
- NULL→ruled: n48 growth is impossible (closed corpus) — only sharper era
  instruments (diplomatic "ne" contact model) or 94's own promotion/demotion
  (94="ne" is provisional-strong; its fall takes 48 with it).
