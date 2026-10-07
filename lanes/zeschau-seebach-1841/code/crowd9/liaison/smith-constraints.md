# Smith constraints memo — joint-inference objective (round 9, smith-liaison)

Lane: zeschau-seebach-1841. Date: 2026-10-07. Author: smith-liaison (round-9 WO5).
Audience: the Smith (side-homophonic-rebuild2 fleet: Track A register-gap,
Track B neural char-LM, Track C boundary-informed scoring).

## 0. Boundary and purpose

This memo is the spec the Smith's joint-inference objective must build against
**once a scorer passes its red-team gate** — it is NOT a solver build and does
not duplicate rebuild2's work (charter: `code/side-homophonic-rebuild2/FLEET-CHARTER.md`).

- **Main-fleet search scope is ZERO until C1 passes on the register-gapped
  family** (F57; N40 boundary — C1 held only in-distribution, never on the
  gapped family). Current: 3/3 FAIL, worst gap −0.28 nats (`diagnose.json`,
  `c1x2.json`). Nothing in this memo waives C1.
- C1 definition (banked, `code/crowd7/search/diagnose.py`, `c1x2.py`):
  truth total > max of 20 random-key totals on EVERY tested fresh instance.
- Diagnosed scorer facts the Smith owns (do not re-litigate):
  letter term register-saturated (+0.09 nats/letter above noise);
  word bonus no separation (truth 0.111–0.127 vs random max 0.087–0.123);
  LAM_POLY=0.05 decisive anti-truth (−0.30 for truth's 6 islets vs
  letter+word +0.12 over random) — rescale on the gapped family.
  Transferring cleanly: concentration penalty (truth S_conc=0, max_n_c=3 at
  cap 3) and the 617-cell inventory (D3 missing=0 on 184207).
- Verifier's binding conclusion (round 1): the failure is in the likelihood,
  not the weights. Salad beats truth by **2,601 nats** at chance primary
  recovery (1/89); reweighting within the 5-gram+lexicon family is exhausted.
  `code/side-homophonic-rebuild/verifier/CLOSING-VERIFICATION.md`.

## 1. F33 conditioned-polyvalence rules — any joint objective must implement these

F33 doctrine (banked, `code/crowd5/scorer_identifiability.md` §3; round-7/8
case law): polyvalence is CONDITIONED. A joint objective must model
**conditioned islets** — windows join an islet only under a pre-registered,
GT-anchored, falsifiable condition with zero free cases. It must NEVER merge
a value into one reading across all its windows ("unconditioned mergers" are
the failure mode behind every killed claim below). Concrete rules as of round 8
(adjudicator: `code/crowd8/adjudicator/RULINGS-FINAL.md`):

### 1a. 84 (R4 — re-scope GRANTED, LEAD)
- **84="en" iff pre∈{82}** (GT-anchored core: 0-based 166 → "m'en", n_eff=1)
  **∪ pre∈{66,89}** (conditional extensions: 66-84 ×2 @154/@1151,
  89-84 ×2 @276/@1378, n_eff=4 — CONDITIONAL on the 66/89 noun-class
  readings, which are leads, not provisional; if those fall, the extensions fall).
- The 46-part of the old pre∈{46,94,82} condition is FALSIFIED, not expanded:
  46-84 must never read "en" («qu'en en» = 0/4.2M era; legs @310/@473
  withdrawn; 24="en" holds STRONG locally — the window stays an open residual).
- **84 noun identity-NULL iff pre∈{77,11}** (@1803 withdrawn, @1447 conditional).
- 9 windows remain residual (2 en-lean, 2 adverse-lean, 5 plain): unclassified.
- What this forbids: merging all 84s into "en"; reviving the 46-pre condition;
  treating free 84s as scored readings instead of identity-NULL.

### 1b. 00 (F54 — STRONG LEAD + LEAD conditioned)
- **00="pour"** across 52 windows (STRONG LEAD; B1 3.91×, B3 3.19× after the
  register fix — promotion to provisional not met: needs B1 or B3 ≤2×).
- **00="le" iff pre=96** (3 windows: 96-00 bigrams 0-based @47/@465/@960) —
  LEAD conditioned; promotion to provisional requires ≥2 NEW independent legs
  (not met). Round-9 WO-5 follow-on: 86's identity (86 que-family dissolves B3).
- What this forbids: merging 00→"pour" unconditionally — 96-00 must read
  "par le", never "par pour" (ungrammatical).

### 1c. 06 (R7e — LEAD, condition frozen)
- **06="ent" iff pre=82** (n=4, n_eff=3; 0-based 06-indices [580,738,1184,1355];
  GT-anchored core = the in-prereg T4 5-mer windows 94-82-06-06 @578-581,
  @1183-1186, "ne-ment" frames).
- Falsifier frozen verbatim: **any 82-06 window in a verbal frame kills the
  islet** (06-falsifier-watch, round-9 WO-6).
- All other 06 windows are NOT "ent": 06=verb-stem class provisional (F21
  wins the general reading by worker convergence; F25: neither side holds
  CONFIRMED on 06; restricted-"ent" plausible on the 3 trigrams only).
- Standing F33-grade distributional rule: 06/86 M1 (00→86 ×12 vs 00→06 ×0;
  06 in finite frames →11 ×4, →77 ×6, →00 ×4; 86 never there, 0/14).
- What this forbids: the unconditioned 06→ent merger (REFUTED, N19) and
  single-stem-for-all-06 (KILLED, N38, 17.1× rate).

### 1d. 67 (R6/R8 — et/veut fork SUPPORTED as conditioned polyvalence, unpromoted)
- 19/38 classified, **zero cross-contamination**, 19/38 open — the fork is real
  but half the data hasn't voted.
- **et-arm conditions (8):** 67→64 ×2 ("veut qui" impossible; era et-qui=99
  vs veut-qui=0), 06-29-67 ×2 ("[inf] veut [inf]" impossible), pre∈{06,86} ×4
  (verb-verb adjacency kills "veut").
- **veut-arm conditions (11):** "et me"×4 @351/@491/@1163/@1842, "me et"-frames
  ×6, "la et"×1 @1044 (all et-killed). Caveat: veut-specific identity is thin
  (era n("veut")=52); 67@1045 pins a 3sg transitive VERB, not uniquely "veut".
  The pre=21 strain (@1841 "me veut me" broken under 21="me") tensions 21's
  lead, not 67's.
- **@1248 [16,00,67,46,26] = NEITHER-class, fenced n=1:** neither arm licenses
  the frame (era "pour et que"="pour veut que"=0). A new non-{et,veut} arm or
  a fork re-scope needs its own ≥2-leg bar (WO-7).
- What this forbids: merging 67 into et or veut wholesale; letting either arm
  claim @1248.

### 1e. Standing F33-family (older, still binding)
- 52: "pas" iff pre∈{94,70} else "so"/"se"; 94: "en" iff pre=82/suc=87.
- {93,8}="l'" unconditioned homophones (M_hom LEAD; 93 alone rate-KILLED).
- 16="i" unconditioned LEAD; 01="est" CONFIRMED MEDIUM;
  62="on" fenced STRONG LEAD (62="il" DISFAVORED-STRONG).

## 2. Anchor set a joint run must hold fixed

**7 GT (hard pins, pencil decipherment):** 11=la, 70=pre, 82=m, 34=i, 29=er,
40=e, 46=que.

**5 provisional (fixed as readings, status does not promote by contact):**
87=ce (provisional, best-tested), 64=qui (provisional, F20),
96=par (provisional, F19), 59=est (provisional, R1 upheld),
77="le" (provisional-**CONDITIONED**).

Standing conventions: anchor-preserving controls on all future drags; never
score manual-tiling bearing counts (T7); inventory restricted to the 24
crib-derived units + the 11,870-word pattern lexicon under red-team R1–R8
(F34/F44) for any gated R5005 run.

## 3. Windows that discriminate a passing vs failing joint inference

A joint run on R5005 (or a fresh gated batch) earns attention when it handles
these right; a salad/annealer optimum demonstrably handles them wrong.
(Positions 0-based unless noted; canonical parse =
`code/side-keyhunt/repaired_offsets.json`.)

1. **64-77-84-59 ×2 (0-based starts 1445, 1801)** — «qui le [verb=84-59]» lead
   (REFERRED to round-9 conditioner). Passing: surfaces a verb reading of the
   84-59 slot under the §1a conditions; failing: tiles fluent nonsense.
2. **64-96-43-87-01 ×2 (0-based [341..343], [1025..1027])** — F18 reverse
   joints; tests the 96=verb conditioned reading (only 96 with suc=47 is @150).
   Passing: 96 reads verb-stem in these frames; failing: drops the reading.
3. **«la 67» @1044–1045 (11=la GT)** — 67@1045 pins a 3sg transitive verb,
   kills "et" there. Passing: 67≠et in this window; failing: the
   unconditioned 67→et merger writes "la et".
4. **94-82-06-06 @578-581 / @1183-1186** — frozen 06-islet core. Passing: reads
   06="ent" here under the frozen condition WITHOUT generalizing "ent" to
   other 06 windows (the islet's stated falsifier is the discriminator:
   failing = verbal-frame 82-06 reads, or ent-generalization).
5. **@1248 [16,00,67,46,26]** — NEITHER-class fenced window. Passing: keeps 67
   NEITHER here (era licenses neither fork arm); failing: an unconditioned
   merger forces et or veut into "…pour 67 que".

Watch-adverse (must-not regress): 46-84 at 0-based 309–311 / 472–474 must NOT
read "en" (24="en" holds STRONG; "qu'en en" era-absent); 82-84 @166 must read
"en" (GT-anchored islet core).

## 4. What a joint run must NOT break

Killed mergers and closed claims — no re-litigation, no revival under new
names:
- 48="ne" KILLED (R1 round-8, F60); 48="ne"-allophone {94,48} REFUTED.
  The 48 successor battery runs no allophony presumption.
- 93="l'" alone rate-KILLED (p=4.1e-4 every slice). Only M_hom {93,8}.
- 24="est" REFUTED (N10); H5 "J'ai l'honneur de" REFUTED (N11).
- 06="ent" general REFUTED (N19); single-stem-for-all-06 KILLED (N38, 17.1×).
- The 46-part of 84's "en" condition FALSIFIED — no revival.
- Crib writes mute -e (40="e" GT): any phonetic model that needs mute-e
  unwritten is KILLED (N17 — killed 06=/mɑ̃/ demand-).
- Retired criteria (not deferred, not re-usable as bars): WO-6 second-window
  (n_eff=2) — the stream is fixed and fully censused, the bar is unmeetable.
- Instruments VOID or uncalibrated: contact phases are NOT word-position
  classes (N15); F11 cycle direction is labeling-relative; factor-2 rate band
  UNCALIBRATED; 'er'-rate ranking checks uncalibrated.
- Refuge concretizations DEAD (schema survives only as LOGICALLY-OPEN-NO-EVIDENCE).
- Prohibitions (standing): NO R5005 contact; no sealed-key reads; no scoring
  manual-tiling bearing counts; no post-hoc partitions; n≥3 kill rule stays;
  no coordinator-applied bars — red team adjudicates every status change.
- Harness rules from the scorer-liaison memo (banked,
  `code/crowd8/scorerliaison/SCORER-CONSTRAINTS.md`): the banked prototype
  imports the Smith's RepairedModel — do NOT "fix" the failing import by
  re-pointing at the round-6 objective; adoption bar PRIMARY ≥ 0.20 on
  `score_fresh.py`; scope stays ZERO until C1.

## 5. Rebuild2 status (2026-10-07 15:19 CDT) — for the Smith

- Red-team review COMPLETE: `side-homophonic-rebuild2/redteam/RULINGS.md`
  (19:30). Tally: 0 KILL / 4 UPHELD / 6 CONCERN / 3 GO.
- **Track A (register gap): GO** (R4). Instrument complete
  (`build_ref.py`, `rescore_reg.py`, `lm_ref_diplo/lm.json` sha256
  `5018f44c…`; 20-gram Les-Mis scan reproduces 0/119,485). Cleared to run
  step 3 (sanity + diagnostic rescore → `track-a/results/rescore.json`).
  Non-blocking hardening: `rescore_reg.py` must hard-exit on sanity
  mismatch (currently prints "MISMATCH -- STOP" but continues).
- **Track B (neural char-LM): GO** (R5). 295-line PREREG signed off; 189-form
  adapted-salad pool verified EXACTLY with independent code; numpy LSTM
  (torch absent — honest). Cleared to execute the 9-step order. No training
  output yet — training wall-time (<2h CPU) is the next milestone.
- **Track C (boundary-informed scoring): GO** (R3). `decodes.json` +
  `word_stats.json` verified byte-exact (N=486,789 / C=1,717,960 /
  V=10,666 / ρ=0.28335293); 184101 slice pre-registered (pairs 0–299, 62
  groups / 55 non-pinned). Cleared to run the §4 15-gram Les-Mis hygiene
  gate, then write + run `score_boundaries.py`. Non-blocking: PREREG.md:83
  typo (C=1,717,930 → 1,717,960); length-effect interpretation caveat —
  report W_uni/W_len/W_bnd breakdown with the margin.
- **No scored comparison has run yet** (no `results/` dirs as of 15:19 CDT).
  All tracks are executing per PREREG order of operations under sign-off —
  nothing stalled, nothing killed.

## 6. What the Smith needs from the main fleet

- **Nothing urgent.** No request is blocking any track.
- Offer, standing: if the register-matched corpora prove thin (Track A: 215k
  words size-matched diplomatic; Track B: 14-file manifest), the main fleet
  holds era/register-matched text (side-period corpus: Nesselrode v8 —
  banked as the future rate-bar corpus, Metternich, Talleyrand, RdDM 1841,
  Tocqueville) and can supply more 1830s–40s diplomatic French on request.
- Binding cross-track constraint already recorded (R5b): Track B must exclude
  guizot-memoires-t5-t6.txt word offsets [100000,104000) and [200000,204000)
  (Track-A-reserved truth slices) pre-tokenization, logged in manifest.json;
  overlap > 0 ⇒ run VOID. No main-fleet action unless the Smith reuses the
  trained model.

## Pointers

- Adjudicator rulings (authoritative for §§1–4):
  `code/crowd8/adjudicator/RULINGS-FINAL.md`
- Round-8 preregs (bars that became §1 rules): `code/crowd8/redteam/PREREG-ROUND8.md`
- Scorer-liaison predecessor memo: `code/crowd8/scorerliaison/SCORER-CONSTRAINTS.md`
  (+ `T7-STANDING-RULE.md`)
- Rebuild-1 closing verification: `code/side-homophonic-rebuild/verifier/CLOSING-VERIFICATION.md`
- Rebuild-2 charter + red-team rulings: `code/side-homophonic-rebuild2/FLEET-CHARTER.md`,
  `code/side-homophonic-rebuild2/redteam/RULINGS.md`
