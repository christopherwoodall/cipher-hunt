# Smith constraints memo — joint-inference objective (round 10, smith-liaison)

Lane: zeschau-seebach-1841. Date: 2026-10-07 ~15:45 CDT. Author: smith-liaison (round-10 WO7).
Audience: the Smith (side-homophonic-rebuild2 fleet: Track A register-gap,
Track B neural char-LM, Track C boundary-informed scoring).
Supersedes: `code/crowd9/liaison/smith-constraints.md` (banked round 9, R2 —
fully carried forward; nothing in §1–§4 of the round-9 memo is rescinded).

## 0. Boundary and purpose

This memo is the spec the Smith's joint-inference objective must build against
**once a scorer passes its red-team gate** — it is NOT a solver build and does
not duplicate rebuild2's work (charter: `code/side-homophonic-rebuild2/FLEET-CHARTER.md`).

- **Main-fleet search scope is ZERO until C1 passes on the register-gapped
  family** (F57; N40 boundary — C1 held only in-distribution, never on the
  gapped family). Current: 3/3 FAIL, worst gap −0.28 nats. Nothing in this
  memo waives C1.
- C1 definition (banked): truth total > max of 20 random-key totals on EVERY
  tested fresh instance.
- Round-10 round status: round 9 COMPLETE — independent adjudicator ruled all
  9 packages (`code/crowd9/redteam/RULINGS-ROUND9.md`; 7/7 battery preregs
  timestamp-audited PASS; no coordinator-applied bars). Baselines extended:
  R9BANK 98/98 PASS, ROUND8-LEDGER 79/79 PASS (extend, don't rebuild).

## 1. F33 conditioned-polyvalence rules — unchanged in force, amended per round-9 adjudication

All round-9 memo §1 rules stand. Amendments from round-9 rulings:

### 1a. 84 (R4 — re-scope GRANTED, LEAD) — amended
- 84="en" iff pre∈{82} (GT-anchored core: 0-based 166 → "m'en", n_eff=1)
  ∪ pre∈{66,89}. The pre∈{66,89} extensions are now conditioned on
  **CONFIRMED class readings** (round-9 R8 Ruling 6): 66 = CONFIRMED broad
  class {noun, infinitive, nous/vous-type} (specific value NULL, honestly);
  89 = NOUN-CLASS CONFIRMED. If either class falls, its extension falls.
- **Residual census banked:** n84=25 = 5 en-islet + 2 withdrawn + 1 fenced
  + 8 rescoped-noun + 9 residual. The 9 residuals remain unclassified;
  recurrence without class signature does not extend islets.
- @857's lean change noted: round-8's adverse-lean correctly WITHDRAWN
  (it was conditional on 48="ne", killed F60 — dependency dissolution).
- The 46-pre condition stays FALSIFIED (no revival); "qu'en en" era-0.
- What this forbids: unchanged — merging all 84s into "en"; reviving the
  46-pre condition; treating free 84s as scored readings.

### 1b. 00 (F54 — STRONG LEAD + LEAD conditioned) — amended
- 00="pour" across 52 windows (STRONG LEAD; B1 3.91×, B3 3.19× — promotion
  to provisional not met: needs B1 or B3 ≤2×).
- Round-9 R8 Ruling 2: **the B3 dissolution premise is DEAD** (86 is not
  que-family; the ratemodel's era number was wrong twice over). B3 3.19×
  STANDS as a live leg. 86="que"-family REFUTED (kill-grade, §4).
- 00="le" iff pre=96 (3 windows: 96-00 bigrams 0-based @47/@465/@960) —
  LEAD conditioned; promotion requires ≥2 NEW independent legs (not met).
- What this forbids: unchanged — 96-00 must read "par le", never "par pour".

### 1c. 06 (R7e — LEAD, condition frozen) — corrected
- 06="ent" iff pre=82 (n=4, n_eff=3; 0-based 06-indices [580,738,1184,1355]).
- **Citation correction (round-9 R2):** the GT-anchored core is the T4 5-mer
  windows 94-82-06-06 @578-581 and **@1182-1185** (0-based; the round-8/9
  memo citation "@1183-1186" was a 1-off slip — pairs[1182:1186]=[94,82,6,6]).
- Frozen falsifier stands verbatim: any 82-06 window in a verbal frame
  kills the islet. Round-9 R1: falsifier did not fire on all three prongs
  (FIRE-PART/FIRE-IN/FIRE-OUT); the coincidence probe is between bars
  (p=0.0138 — honest middle; **n_eff=3 fragility is a standing caveat**:
  one window from the fence).
- Frenchman Gate 2: two FENCED n=1 adverses on the 06-islet's by-ear
  readings — @1184 ("ne mentent/entendent est" ungrammatical with
  59="est"-as-word; escape hatches noted — **this adverse is contingent on
  the round-10 59 battery**, §7) and @738 (technical weakest window: no
  94 prefix, stem 18 unidentified). Neither fires the falsifier.
- Round-10 WO6 follow-on: both suc=6 windows are islet windows (post-hoc,
  p=0.0063) — the 94-82-06-06 4-gram frame hypothesis is a round-10 test,
  not a banked rule.
- What this forbids: unchanged — unconditioned 06→ent merger (REFUTED, N19);
  single-stem-for-all-06 (KILLED, N38, 17.1×).

### 1d. 67 (R6/R8 — et/veut fork SUPPORTED, unpromoted) — amended
- 19/38 classified with zero cross-contamination; 19/38 open. Fork stays
  SUPPORTED (round-9 R9 Ruling 6: the WO-7 kill instrument does not fire).
- Et-arm (8) / veut-arm (11) conditions: unchanged from round-9 memo.
- **@1248 NEITHER-fence UPHELD** (era "pour et que"="pour veut que"=0);
  the 62-conditionality is carried forward procedurally (62 on/il blocker
  holds; fence legs don't involve 62).
- **@199 NEITHER-fence CONDITIONAL on 08="l'"** (round-9 R9 Ruling 2) —
  if 08 is revalued, @199 reopens.
- **@630 et-CONDITIONAL** (round-9 R9 Ruling 3): granted under conditions
  C1 (08="l'") AND C2 (67 standalone word); C2 unresolvable — under the
  clitic-"me" competitor @630 is NEITHER. Not a classification.
- **Gate 4 era-bounding (frenchman):** any new 67 arm is constrained to
  **non-finite** ({cela,peu}-class or infinitive; finite-verb arms era-0
  at @1248). The round-10 @1248 ≥2-leg arm must respect this.
- R_veut4 DROPPED (design-time null); 6 open residuals CONFIRMED open
  (@633, @902, @1372, @1450, @1519, @1623).
- What this forbids: merging 67 into et or veut wholesale; letting either
  arm claim @1248; reading a finite verb into 67@1248.

### 1e. Standing F33-family (older, still binding) — unchanged
- 52: "pas" iff pre∈{94,70} else "so"/"se"; 94: "en" iff pre=82/suc=87.
- {93,8}="l'" unconditioned homophones (M_hom LEAD; 93 alone rate-KILLED,
  kill upheld on strict v8 p=0.0003).
- 16="i" unconditioned LEAD; 01="est" CONFIRMED MEDIUM;
  62="on" fenced STRONG LEAD (62="il" DISFAVORED-STRONG; WO3 blocker
  carried forward — C1–C4 banked as tested-NULL, do not re-run as fresh cells).
- Mehemet-Ali LEAD-weak: M3 'he'-cell adverse **STRUCK, scoped** (germanist
  cross-check: German phonetics for this proper name only — the general
  "German-interference premise" is NOT banked; D1 62-tension and D2
  "mêleront" stand).
- Vetoes banked as constraints on future proposals (not kills): germanist
  V1–V5, frenchman V1–V5 (see `code/crowd9/report_inbox/germanist-crosscheck.md`,
  `frenchman-register.md`).

## 2. Anchor set a joint run must hold fixed — unchanged, with one pending conditioning

**7 GT (hard pins, pencil decipherment):** 11=la, 70=pre, 82=m, 34=i, 29=er,
40=e, 46=que.

**5 provisional (fixed as readings, status does not promote by contact):**
87=ce (provisional, best-tested), 64=qui (provisional, F20),
96=par (provisional, F19), 59=est (provisional, R1 upheld —
**see §7 PENDING**), 77="le" (provisional-CONDITIONED).

Standing conventions: anchor-preserving controls on all future drags; never
score manual-tiling bearing counts (T7); inventory restricted to the 24
crib-derived units + the 11,870-word pattern lexicon under red-team R1–R8
(F34/F44) for any gated R5005 run.

## 3. Windows that discriminate a passing vs failing joint inference — round-9 memo's 5 carried forward + 3 new

1. **64-77-84-59 ×2 (0-based 1445, 1801)** — «qui le [verb=84-59]» (REFERRED
   to the round-9 conditioner; R8 Ruling 3 refined the frame). Passing:
   surfaces the **bisyllabic-verb unit** reading of the 84-59 slot under
   §1a conditions; failing: tiles fluent nonsense OR reads a standalone
   "est" after 84 here. **59="est"-as-word is era-absent at @1447/@1803
   («qui le [V] est» 0/4.2M) — adverse datum, fenced n=2 (59="est"
   provisional stands elsewhere).**
2. **64-96-43-87-01 ×2 (0-based [340..342], [1024..1026]; 45-64-96-43-87-01
   @[340,1024])** — F18 reverse joints; formula stays FORMULA-UNCONFIRMED
   (round-9 R8 Ruling 4: classification as 96=verb-stem DENIED per WO-1 bar).
   Passing: 96 reads verb-stem in these frames WITHOUT banking the reading;
   failing: drops it. **Banked datum:** 43="me" suffers a clitic-order
   adverse IN THIS FRAME («qui [V] me» ungrammatical as verb+object; 43="me"
   WEAK stands globally).
3. **«la 67» @1044–1045 (11=la GT)** — 67@1045 pins a 3sg transitive verb,
   kills "et" there. Passing: 67≠et in this window; failing: the
   unconditioned 67→et merger writes "la et". (Unchanged.)
4. **94-82-06-06 @578-581 / @1182-1185** — frozen 06-islet core (positions
   corrected per §1c). Passing: reads 06="ent" here under the frozen
   condition WITHOUT generalizing "ent" to other 06 windows; failing:
   verbal-frame 82-06 reads, or ent-generalization. (Unchanged save citation.)
5. **@1248 [16,00,67,46,26]** — NEITHER-class fenced window (fence UPHELD
   round 9). Passing: keeps 67 NEITHER here; failing: an unconditioned merger
   forces et or veut into "…pour 67 que". **Gate-4 amendment:** any third arm
   must be non-finite — a failing run also tiles a finite verb into 67@1248.
6. **NEW — @199 [60,8,67,76,87]:** NEITHER-class fenced CONDITIONAL on
   08="l'". Passing: keeps 67 NEITHER here while 08="l'" holds; failing:
   forces et/veut, or — if 08 is revalued — keeps the fence anyway. The
   window's status is explicitly downstream of 08's lead.
7. **NEW — @1351–1356 (FENCED-PENDING, round-10 resolution):** under triple
   fenced pressure (hunter H1c, H1d, frenchman Gate 6 triple collision);
   era favors the 06-islet parse ("ne ment pas") over the gouvernement parse.
   **Fence, don't revisit:** 62="on" is STRONG LEAD, 37="le" MEDIUM,
   64="qui" provisional — revisiting banked neighbors on n=1 tensions is
   disproportionate (round-9 R6). The round-10 resolver1351 adjudication will
   decide which reading owns @1351–1356 (06-islet parse vs gouv parse vs
   77="le"). Until it lands: the Smith must not claim ANY of the three
   readings at this window and must not let a joint optimum tile a reading
   that contradicts the eventual ruling — the liaison relays it (§7).
8. **NEW — qui-96-43 frame / 59-conditioned windows (PENDING, §7):** see §7.

Watch-adverse (must-not regress): 46-84 at 0-based 309–311 / 472–474 must NOT
read "en" (24="en" holds STRONG; "qu'en en" era-absent); 82-84 @166 must read
"en" (GT-anchored islet core). The @857 residual lean change is banked as
dependency-dissolution, not evidence.

## 4. What a joint run must NOT break — round-9 memo's list carried forward + round-9 kills added

Killed mergers and closed claims — no re-litigation, no revival under new
names (all carried from round 9 unless noted NEW):
- 48="ne" KILLED (F60); 48="ne"-allophone {94,48} REFUTED. **NEW — H_verb
  for 48 KILLED (round-9 R4, K2 fired per pre-registered terms): 48 is
  UNIDENTIFIED; no verb reading promotes.** The round-10 48 syllable-cell
  battery is the live question (§7). The F60 guard is ARMED: ne-allophony
  re-litigation gets an interim kill. (Round-9 datum correction banked:
  48 has 29 distinct successors/38 on the repaired parse, not 19 —
  strengthens the syllable-cell alternative.)
- 93="l'" alone rate-KILLED (upheld on strict v8, p=0.0003). Only M_hom {93,8}.
- 24="est" REFUTED (N10); H5 "J'ai l'honneur de" REFUTED (N11).
- 06="ent" general REFUTED (N19); single-stem-for-all-06 KILLED (N38, 17.1×).
- The 46-part of 84's "en" condition FALSIFIED — no revival.
- **NEW — 86="que"-family REFUTED (round-9 R8 Ruling 1, kill-grade
  hypothesis-kill):** L5 elision kill (86→consonant-initial ×7/32:
  «qu'pre/qu'pas/qu'plus» impossible) and L6 77-86×5 era-kill
  (P("que"|"le")≈0.00007). The B3 dissolution premise died with it; B3
  3.19× STANDS. 86's specific value is NULL.
- Crib writes mute -e (40="e" GT): any phonetic model that needs mute-e
  unwritten is KILLED (N17).
- Retired criteria (not deferred, not re-usable as bars): WO-6 second-window
  (n_eff=2).
- **78 fork UNRESOLVED:** H3a banked as a WEAK leg for fork-tine (c)
  (er|ne 10.4×, p=3.2e-11, gouvernement-family excluded — weak by
  construction: language stat ≠ encipherer cut). The Smith must not
  pre-merge 78 into any single reading (78="er" vs {ver,er} fork tines are
  live).
- Instruments VOID or uncalibrated: contact phases are NOT word-position
  classes (N15); F11 cycle direction is labeling-relative; factor-2 rate band
  UNCALIBRATED; 'er'-rate ranking checks uncalibrated.
- Refuge concretizations DEAD (schema survives only as LOGICALLY-OPEN-NO-EVIDENCE).
- Prohibitions (standing): NO R5005 contact; no sealed-key reads; no scoring
  manual-tiling bearing counts (T7); no post-hoc partitions; n≥3 kill rule
  stays; no coordinator-applied bars — red team adjudicates every status change.
- Harness rules from the scorer-liaison memo: the banked prototype imports the
  Smith's RepairedModel — do NOT "fix" the failing import by re-pointing at
  the round-6 objective; adoption bar PRIMARY ≥ 0.20 on `score_fresh.py`;
  scope stays ZERO until C1.

## 5. Rebuild2 status (2026-10-07 15:45 CDT) — for the Smith

- **No results yet on any track.** No `results/` dirs exist as of this memo;
  the newest files in the fleet are Track B's PREREG (20:25 UTC) and the
  red-team RULINGS.md (19:30 UTC). All tracks are executing per their
  pre-registered order of operations under sign-off — nothing stalled,
  nothing killed.
- **Track A (register gap): GO** (R4). Instrument complete
  (`build_ref.py`, `rescore_reg.py`, `lm_ref_diplo/lm.json` sha256
  `5018f44c…`; 20-gram Les-Mis scan reproduces 0/119,485). Next step: run
  the step-3 sanity + diagnostic rescore → `track-a/results/rescore.json`
  (the track-A register-gap diagnostic). Non-blocking hardening:
  `rescore_reg.py` must hard-exit on sanity mismatch (currently prints
  "MISMATCH -- STOP" but continues).
- **Track B (neural char-LM): GO** (R5). 295-line PREREG signed off; 189-form
  adapted-salad pool verified EXACTLY with independent code; numpy LSTM
  (torch absent — honest). Next step: execute the 9-step order; training
  wall-time (<2h CPU) is the milestone. No training output yet.
  (Cross-track constraint R5b stands: Track B must exclude
  guizot-memoires-t5-t6.txt word offsets [100000,104000) and
  [200000,204000) — Track-A-reserved truth slices — pre-tokenization, logged
  in manifest.json; overlap > 0 ⇒ run VOID.)
- **Track C (boundary-informed scoring): GO** (R3). `decodes.json` +
  `word_stats.json` verified byte-exact (N=486,789 / C=1,717,960 /
  V=10,666 / ρ=0.28335293); 184101 slice pre-registered (pairs 0–299, 62
  groups / 55 non-pinned). Next step: run the §4 15-gram Les-Mis hygiene
  gate, then write + run `score_boundaries.py` (the track-C boundary pilot).
  Non-blocking: PREREG.md:83 typo (C=1,717,930 → 1,717,960);
  length-effect interpretation caveat — report W_uni/W_len/W_bnd breakdown
  with the margin.
- **Red-team rulings on their side:** COMPLETE — `side-homophonic-rebuild2/redteam/RULINGS.md`
  (0 KILL / 4 UPHELD / 6 CONCERN / 3 GO). No new red-team findings since.
- The Smith's tracks do not currently plant 59=est, 48, or @1351-dependent
  readings in any PREREG (verified by grep) — §7 hazards are prospective
  (the future joint scorer), not a current control corruption.

## 6. What the Smith needs from the main fleet

- **Nothing urgent.** No request is blocking any track.
- Offer, standing: if the register-matched corpora prove thin (Track A: 215k
  words size-matched diplomatic; Track B: 14-file manifest), the main fleet
  holds era/register-matched text (side-period corpus: Nesselrode v8 —
  banked as the future rate-bar corpus, Metternich, Talleyrand, RdDM 1841,
  Tocqueville) and can supply more 1830s–40s diplomatic French on request.
- Round-9 corpus bookkeeping now banked: RdDM-293× independently recounted
  at 293 and its UNVERIFIED flag LIFTED; fait 4.6× soft edge symmetric
  (rate-bar corpus discipline).

## 7. Round-10 live questions — the Smith's future scorer must respect whatever the round decides

Round-10 executors are scaffolded (`code/crowd10/`; STATE.md work orders);
no executor results have landed as of this memo. These are the questions in
flight, and the constraints each will produce once the red team adjudicates:

- **@1351 resolution (WO1, `resolver1351/`):** triple fenced pressure
  (H1c, H1d, frenchman Gate 6). Which reading owns @1351–1356 — the
  06-islet parse ("ne ment pas") vs the gouvernement parse vs 77="le"
  (provisional-conditioned)? The winner's conditions join this memo's §1
  as banked rules; the liaison relays the ruling. The Smith must not
  pre-claim the window (§3.7).
- **59 conditioned-polyvalence battery (WO2, `conditioner59/`):**
  59="est"-word dead at @1447/@1803 (fenced n=2); the -este verb ID and the
  word-"est" vs verb-final-syllable battery are the live work. **This is the
  cross-fleet hazard of the round:** the provisional anchor 59=est may be
  conditioned by the round-10 ruling, and Frenchman Gate 2's @1184 fenced
  adverse ("ne mentent/entendent est" ungrammatical) is contingent on it.
  Until the ruling lands: 59=est provisional everywhere EXCEPT @1447/@1803,
  where the scorer must NOT read a standalone "est". The liaison will relay
  the conditioned rule once adjudicated; any joint run pre-dating it must be
  re-baselined after.
- **48 syllable-cell battery (WO3, `syllabicist48/`):** 48 is UNIDENTIFIED;
  H_verb killed; 48="ne" killed. The battery tests syllable-cell hypotheses.
  The Smith must not assign 48 ANY reading (no "ne", no verb, no allophone)
  until the red team rules; if the battery banks a value, it joins §2 as a
  new fixed reading — the liaison relays it.
- **@1248 ≥2-leg arm (WO4, `arm1248/`):** any new 67 arm must be non-finite
  per Gate 4 (§1d). If banked with ≥2 legs, it amends §1d with its
  pre-registered conditions.
- **67's 6 open-residuals (WO5, `finisher67/`):** @633/@902/@1372/@1450/
  @1519/@1623 stay open; arms need their own ≥2-leg bars. If banked, they
  amend §1d.
- **06 islet registry refinement (WO6, `watch06/`):** tests the 94-82-06-06
  4-gram frame hypothesis (post-hoc p=0.0063 — a test, not a rule). If the
  frame is banked, it amends §1c.

## Pointers

- Round-9 adjudication (authoritative for §§1/3/4 deltas):
  `code/crowd9/redteam/RULINGS-ROUND9.md`
- Round-8 adjudication (authoritative for the carried-forward base):
  `code/crowd8/adjudicator/RULINGS-FINAL.md`
- Round-8 preregs (bars behind §1): `code/crowd8/redteam/PREREG-ROUND8.md`
- Round-9 preregs: `code/crowd9/redteam/PREREG-ROUND9.md`
- Scorer-liaison predecessor memo (+ T7 standing rule):
  `code/crowd8/scorerliaison/SCORER-CONSTRAINTS.md`
- Rebuild-1 closing verification:
  `code/side-homophonic-rebuild/verifier/CLOSING-VERIFICATION.md`
- Rebuild-2 charter + red-team rulings:
  `code/side-homophonic-rebuild2/FLEET-CHARTER.md`,
  `code/side-homophonic-rebuild2/redteam/RULINGS.md`
