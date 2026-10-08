# Smith constraints — Round-13 DELTA memo (2026-10-07 ~23:30 CDT)

Liaison (smith_liaison), council round-13 work order 8. Read-only liaison;
no Smith work duplicated, nothing on the Smith's side changed, no solver
runs launched, no key searches. Main-fleet search scope stays ZERO.

**Carry-forward:** `code/crowd10/liaison/smith-constraints.md` (full spec,
STANDS) + `code/crowd11/smith_liaison/smith-constraints-round11.md` (DELTA,
STANDS) + `code/crowd12/smithliaison/smith-constraints-round12.md` (DELTA,
STANDS). This memo is a DELTA over the round-12 memo: (1) rebuild-side
execution state — Track A has its first RESULT, Track C v3 has a static
verdict, Track D's Experiment 0 is mid-flight, Track B is training,
(2) council architect-plan relay items not yet absorbed by the solver
side, (3) the banked main-fleet constraint set in round-13 state.
Supersedes nothing; everything banked before stands unless a red-team
ruling below says otherwise.

---

## 1. Rebuild-side execution state — per track (verified from disk 2026-10-07 ~23:20 CDT)

### 1a. Track A (register-gap diagnostic): RESULT LANDED — H1 SUPPORTED, H0 FAILED

`track-a/results/rescore.json` exists (written 2026-10-07 21:57; the
R4a hardening was applied before the run — `rescore_reg.py:119` now
`sys.exit(1)` on sanity mismatch).

- Sanity reproduced EXACTLY: salad−truth under Tocqueville =
  −2352.26 − (−4953.26) = **+2,601.0 nats** (≤1 nat vs the verifier's
  +2,601.0). Instrument healthy.
- Diagnostic: M_d = total_salad − total_truth under the register-matched
  (diplomatic) reference = −2350.08 − (−4550.77) = **+2,200.68 nats
  ≥ +500** → **H1 supported** per the pre-registered decision rule:
  **the 5-gram+lexicon family is the blocker, not the register gap.**
  The register-matched reference shrinks the salad margin by only
  ~400 nats of 2,601 — the rest is the LM family itself.
- Charter consequence: the step-4 pilot anneal was cleared ONLY on a
  diagnostic-positive H0 (margin ≥+500 for truth under the
  register-matched reference). H0 failed → **no step-4 anneal on Track A
  without re-registration.** Track A's 2 diplomatic-plaintext instances
  for the §3 secondary gate (§5.2 of the architect plan) are NOT built.
- **Scorer consequence (banked): the register gap is real (F10: cela/ce
  6.7×) but it is NOT the cause of the salad-beats-truth failure.**
  Register-matched training is a minor term, not a rescue. The council
  architect's core claim (§1.2: "rerank-only cannot beat the generator's
  bias") is corroborated: the failure is structural — the likelihood
  itself rewards the salad, at any register tested.

### 1b. Track B (neural char LM): EXECUTING — training in progress

- `python3 train_lm.py` RUNNING since 2026-10-07 22:35 CDT (~45 min in
  at last check; upd=1950, wall=1642s, train_ema=2.2718,
  held_ema=2.2655, lr=2e-03; `train.log` logging heartbeats).
  Relaunched fresh after a `rm -f ckpt.npz ckpt.json` (23:04 wrapper
  timestamp shows the relaunch). No scored comparison has run — the
  9-step order (finite-difference gradient check → instrument gate →
  sanity gates → margins) is still ahead.
- Binding cross-track constraint R5b stands: exclude
  guizot-memoires-t5-t6.txt word offsets [100000,104000) and
  [200000,204000) per Track-A tokenization, pre-tokenization, logged in
  manifest.json; overlap > 0 ⇒ run VOID.
- Unaddressed non-blocking: R5a (8-gram hit-table "13 hits" text vs
  table summing 14; metternich-v6 4 vs 5) — reconcile when the training
  lands; provenance gap (original scan script not on disk) stands.

### 1c. Track C (boundary-informed scoring): v3 STATIC RUN → NULL-v3 (third honest null)

`track-c/boundary_scores_v3.json` exists (R9 cleared the static run only;
no `RESULTS-C-v3.md` written yet; **red team has not reviewed the v3
static result** — RULINGS.md has no v3-results ruling):

- M = +2,683.86 ≥ +800 → gate (a) PASS.
- Validity precondition carried from v2 (mean len 2.44 ∈ [1.765,7.059];
  in-vocab fraction 0.997 ≥ 0.50) → gate (b) PASS.
- Per-char gate (c) **FAILED**: B_v3(truth)/|truth| = −6.7407 nats/char
  vs B_v3(salad)/|salad| = −4.6687 nats/char. Salad still scores better
  per unit of content under the word-bigram repair.
- Pre-registered verdict: (a)∧¬(c) → **NULL-v3**. The §6 300-cell joint
  pilot does NOT get clearance; a diagnosis report of the failing
  term/gate with numbers is the registered next step.
- Substance (banked): the word-bigram term helps (+834 nats W_bi
  truth-favoring; pair counts nearly equal 1,296 vs 1,259) but the
  margin stays length-driven — the salad's tiles are *adversarially
  French word-forms*, and no unigram-or-bigram boundary term can see
  adversarial placement of real words. This is the same lesion as v1/v2:
  the boundary signal lives in word ORDER beyond bigram rate, which is
  exactly what the SPS fallback (§7 of the architect plan) makes
  structural.

### 1d. Track D (LM-judge): pilot PASSED, Experiment 0 MID-FLIGHT, gate anneal cleared-but-not-run

- Pilot 6/6 PASSED 6/6 (margins 43,41,39,43,41,42; probe clean;
  red-team R8 verified byte-exact; R8a seed-column correction required
  on the report table, non-blocking). **Step-4 clearance GRANTED (R8) —
  but NOT executed: no `track-d/gate_runs/` on disk.** The fresh sealed
  instances (184201–184204, 184206, 184207) remain untouched.
- **Experiment 0 is RUNNING** (`python3 experiment_0.py` since 22:58 CDT;
  1 of 6 instances logged, ~168.8s/run): 
...[truncated 12758 chars]
---

## 2. Council architect-plan relay — what the solver side has NOT yet absorbed

The architect's plan (`code/council/solver-architecture.md`, 2026-10-07)
is the pipeline design once a track passes its gate. Relay status:

1. **Experiment 0 (§2) — IN FLIGHT.** Flagged to the solver side as the
   highest-information 9-minute experiment; gates the funnel
   architecture. Running now under PREREG-D-v2 §1 (6 original instances,
   old solver, single-group moves). Branch rule registered: ≥4/6 STAY →
   funnel as designed; ≥3/6 SLIDE/DRIFT → §3 Stage 2 dropped, judge-guided
   Stage-4 ILS becomes the primary loop, SPS fallback flagged. First
   datum (184101: SLIDE) favors Branch B.
2. **Cell-space move set (§4) — IMPLEMENTED, pending functional re-check.**
   The ~40-line spec is in `track-d/solver-cell/solver.py`
   (alias-reassign 0.30 / cell-swap 0.10 / alias-split-merge 0.10 /
   chg1+swap+poly retained for fine-tuning; `block` dropped). The
   architect's step-3 "re-run one control instance to confirm the
   annealer still functions" has NOT been reported — the solver side
   should report one control-instance smoke run before funnel work.
3. **Control changes (§5) — mostly NOT built:**
   - (1) Memorization probe RE-RUN on the 6 fresh gate truths (36 judge
     calls) before unsealing — NOT done; non-negotiable before the gate
     (the pilot's probe covered old slices).
   - (2) Two diplomatic-plaintext instances as a SECONDARY gate (Track A's
     register-matched instances) — NOT built; Track A's pilot anneal was
     never cleared (H1 won) and needs re-registration.
   - (3) Noise-mismatch ablation (2× ear noise, report-only) — NOT built.
     The Frenchman's H-split finding (real encipherer over-splits beyond
     the generator's knobs) makes this the R5005-robustness predictor.
   - (4) q_cycle=0 ablation set (184213–184218) — KEPT, pre-registered,
     stands as the rhythm-crutch check. No change needed.
   - (5) No "strong pass" tier added to the control — the §6 R5005
     criteria handle "solved vs signal". Stands.
4. **§6 R5005 success criteria — relayed for red-team PRE-REGISTRATION.**
   The five criteria (board consistency ≥11/12 with all 10 islet rules at
   registered windows; judge bar ≥ mean-gate-median−2σ and ≥55; topic check
   ≥3 independently verifiable period facts; independent reproduction of
   the decode from the key alone; perturbation stability ≥4/5) must be
   registered BEFORE any R5005 run. The solver-side red team has NOT
   recorded them in `redteam/RULINGS.md` — flagging this as an open
   pre-registration item.
5. **§8 Monday-morning priorities — status relay:**
   (1) Experiment 0: RUNNING. (2) Automated judge instrument: NOT stood
   up — #1 infrastructure prerequisite. (3) Cell-space moves: implemented,
   smoke re-run pending. (4) §3 funnel on the 6 fresh instances (the
   gate): blocked on the judge instrument. (5) In parallel: Track A
   diplomatic instances (secondary gate) + red-team pre-registers the §6
   criteria — neither started. (6) If the gate passes: R5005 run under §6
   — N/A, far downstream.

## 3. Banked main-fleet constraints — round-13 state (what the future scorer must respect)

**3a. The 12 board values (7 GT hard pins + 5 provisionals).**
- 7 GT (hard pins, pencil decipherment — unchanged through round 12):
  **11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que.**
- 5 provisional (fixed as readings; status does not promote by contact):
  **87=ce** (provisional, best-tested); **64=qui** (provisional, F20);
  **96=par** (provisional, F19); **59=est** (provisional — HOLDS per
  round-12 R11; ISLET 10 is its conditioned form, §3b); **77="le"**
  (provisional-CONDITIONED — GAINS @1351 per round-10 R5; the F37-fenced
  "gou" exception shrinks to @1180-only).
- Demotions standing: **77="gouv" DEMOTED→disfavored** (round-12 R9,
  "gouvernement" thread DEAD at all 7 windows); 59="est"-as-word is
  era-absent at @1447/@1803 (EV10 veto) — the provisional stands
  everywhere else.
- **REGISTRY UNDER AUDIT:** the round-13 islet auditor
  (`code/crowd13/islet-audit/`) has produced NOTHING yet — it may
  DISSOLVE some of the 10 islets into word rules or widen/narrow arms.
  The 10-islet registry below is binding UNTIL a red-team ruling changes
  it; the scorer side should treat islet conditions as provisional
  pending the audit, but must NOT relax them on its own.

**3b. The restructured registry (round-14 rewrite, red-team R-IA1–R-IA7
GRANTED 2026-10-07 — supersedes the 10-islet list below; binding as
amended).** Full text: `code/crowd14/registry/REGISTRY.md`. Tiers:
- WORD rules (compositional): W-est1 (93-59=«l'est») / W-est2
  (94-59=«n'est») / W-este2 ([stem]-59, stems 84/06/61/44/86, fenced
  tier 15) / F-qui-est (64-59=«qui est») + 59 monovalent «est» syllable;
  F-qui-le (64-77=«qui le») + W-este1 (84-59=«[X]este», dependency
  BANKED-AS-WORD); W-m'en (82-84); F-en («[noun] en [V]», depends on
  66/89 class tier); W-par-le (96-00 ×3 @47/@465/@960); W-ment (82-06,
  n=4/n_eff=3). 59's old conditioned F1–F4 falsifiers superseded by word
  rules (content preserved).
- SOLE true polyvalence: 67 et/veut fork SUPPORTED (29/38 clean:
  et=18, veut=11, open=9; era legs 99:1/115:1/273:1; @1248
  NEITHER-fence stands as bound; PC-1 peu leg 5/9; DP-1 permanent fence).
- CLASS tier (specific values NULL): 66 (noun/infinitive/nous-vous-class,
  19/19); 89 (noun-class, 14/14; 52-89 ×2 fenced tension).
- SINGLETON: ISLET 5 → INCONCLUSIVE (64-96-47 @150, LEAD holds; no
  promotion case without v8).
- KILL: ISLET 9 — 86=que-family REFUTED kill-grade (retired); F40
  verb-stem-class hypothesis stands, value NULL.
- Solver constraints: do NOT merge 33+86 / 48+94 / 76+78 / 52+59
  (SPLIT ×4). 52 UNIDENTIFIED (WEAK est-arm lead, pre∈{64,94,93});
  48 UNIDENTIFIED (ne-class pre-verbal ≠"ne"); 76 ver-lead weak-local;
  74-class OPEN.
Original 10-islet list as written round 13 (kept as record; superseded
where dissolved):
1. **ISLET 1** — 00="pour" across 52 windows (STRONG LEAD; B1 3.91×,
   B3 3.19× — promotion to provisional not met: needs B1 or B3 ≤2×);
   00="le" iff pre=96 (3 windows @47/@465/@960 — LEAD conditioned;
   96-00 must read "par le", never "par pour"). "par le"×3 corroborates
   (not strengthens) the islet; "par ce que"×3 is corroboration-grade
   (named GT-anchored formula, NOT a new promotion leg).
2. **ISLET 3** — 06="ent" iff pre=82 (LEAD conditioned, n=4/n_eff=3;
   0-based 06-indices [580,738,1184,1355]; T4 5-mer cores
   94-82-06-06 @578-581 / @1182-1185 — citation corrected round 10).
   Corroborated round-12 R9 (no upgrade). New lead from R9: 06-«ne»-
   allophone (live, not a rule). Unconditioned 06→ent merger REFUTED
   (N19); single-stem-for-all-06 KILLED (N38, 17.1×).
3. **ISLET 8** — 84="en" iff pre∈{82} (GT-anchored core @166 "m'en")
   ∪ pre∈{66,89} conditioned on CONFIRMED class readings (66 = broad
   class {noun, infinitive, nous/vous-type}; 89 = NOUN-CLASS CONFIRMED).
   The 46-pre condition stays FALSIFIED (no revival). Round-12 R6:
   -este verb stays set-valued {manifeste, atteste, proteste, conteste,
   déteste} across @1448/@1804 vs @1190 → 84 is polyvalent across these
   windows OR @1190's verb ≠ @1448/@1804's — the scorer must score
   84="este"-verb set-valued, never a single ID.
4. **ISLET 10** — 59=word-«est» iff pre∈{64,94,93} (est-arm, 6/6
   windows clean @103/@316/@1210/@1777/@559/@763); 59=verb-final
   «-este» iff pre=84 (@1190/@1448/@1804 firm; @1291 FENCED). HOLDS
   with NO widening (round-12 R11); F1-WATCH armed with exact trigger;
   @825 candidate-grade; S5 adverses banked (1 full, 1 corrected at
   reduced weight — "n'est le" 8/10 are the «si ce n'est le» idiom, 2
   genuine counterexamples). Unconditioned 59="est" REFUTED kill-grade
   (8 adverses).
5–10. **The older six** (carried from the round-9/10 base, unchanged):
   67 et/veut fork SUPPORTED (29 classified + 2 conditional + 5 open +
   2 fenced = 38; @633 et-CONDITIONAL(C1∧C2); @1248 NEITHER-fence stands
   + peu leg STRENGTHENED 5/9 + double-pour stack ERA-VETO — any decode
   emitting «pour 33 16 pour 67 que» is dead on arrival); 52="pas" iff
   pre∈{94,70} else "so"/"se"; 94="en" iff pre=82/suc=87;
   {93,8}="l'" unconditioned homophones (93 alone rate-KILLED);
   16="i" unconditioned LEAD; 01="est" CONFIRMED MEDIUM.

**3c. The 5 discriminating windows (round-10 §3 carried forward, round-12
amended).** A joint run passes only if it reads these correctly:
1. **64-77-84-59 ×2 (@1445, @1801)** — «qui le [verb=84-59]» bisyllabic-
   verb unit (F-qui-le frame + W-este1/W-este2). Failing reads tile
   fluent nonsense OR a standalone "est" here (era-absent).
2. **64-96-43-87-01 ×2 (@[340..342], @[1024..1026])** — F18 reverse
   joints; formula UNCONFIRMED (96=verb-stem classification DENIED per
   WO-1 bar; Fork-S cost against 96="par" recorded as conditional
   tension, not a re-read of F19). Passing: 96 reads verb-stem WITHOUT
   banking; 43="me" suffers a clitic-order adverse IN THIS FRAME.
3. **«la 67» @1044–1045 (11=la GT)** — 67@1045 = 3sg transitive verb;
   kills "et" there. Failing: unconditioned 67→et merger writes "la et".
4. **94-82-06-06 @578-581 / @1182-1185** — frozen W-ment core. Passing:
   06="ent" under the frozen condition WITHOUT generalization; failing:
   verbal-frame 82-06 reads or ent-generalization.
5. **@1248 [16,00,67,46,26] (frame @1244–1254)** — NEITHER-class fenced
   window, fence UPHELD round 12. Passing: keeps 67 NEITHER here; peu leg
   STRENGTHENED 5/9 (any third arm must be non-finite per Gate 4);
   double-pour stack era-VETO. Failing: forces et/veut, or tiles a
   finite verb, or emits the double-pour stack.
- Resolved/fenced watch (NOT discriminating, do not revisit):
  **@1351–1356 RESOLVED** (round-10 R5: the 06-islet parse «le [78] ne
  ment pas» owns the window; gouvernement ruled OUT at @1351
  window-level); @647 OPAQUE; "la première fois" @1034 GRANTED LEAD
  (round-12 R10; 20="fois" homophone battery warranted for round 13).
- Watch-adverse (must-not regress): 46-84 @309-311 / @472-474 must NOT
  read "en" (24="en" STRONG; "qu'en en" era-absent); 82-84 @166 must read
  "en" (GT-anchored core); 96→11 = 0 (R12); head/tail nulls recorded.

**3d. Must-NOT-break list (round-10 §4 + round-11/12 kills — no
re-litigation, no revival under new names).**
- Killed mergers and closed claims: 48="ne" (F60); {94,48} ne-allophone
  REFUTED; H_verb for 48 KILLED (round-9 R4 — 48 stays UNIDENTIFIED;
  unconditioned 48="de" KILLED kill-grade, 10 clean windows, round-12
  R13; conditioned "de ce que" islet stays LEAD — R4×R13 convergence is
  one leg, strict no-double-count); 93="l'" alone rate-KILLED; 24="est"
  REFUTED (N10); H5 REFUTED (N11); 06="ent" general REFUTED (N19);
  single-stem-for-all-06 KILLED (N38); 46-part of 84's "en" condition
  FALSIFIED (no revival); 86="que"-family REFUTED kill-grade (L5/L6);
  unconditioned 84s KILLED; three mergers KILLED (F56 {77,00}="le"
  among them); "cela" re-litigation CLOSED; médiatrice-class CLOSED;
  é-initial-noun theory RETIRED permanently (dead twice over);
  "gouvernement"/"gouvernent" KILLED at all 7 77-78 windows (R9);
  92 H-pre REFUTED / H-presuc FENCED (R3); "qu'en en" era-absent.
- Instruments VOID or uncalibrated: contact phases are NOT word-position
  classes (N15); F11 cycle direction labeling-relative; factor-2 rate
  band UNCALIBRATED; 'er'-rate ranking checks uncalibrated; V29
  contaminated; phase instrument VOID (F26); Nesselrode v8 token-level
  zeros are VOID as French (OCR word-splits — F77: rate bars on the clean
  3.96M diplomatic corpus; any phrase-zero claim on a v8-inclusive
  corpus must be re-verified v8-excluded before it banks).
- Prohibitions (standing): NO R5005 contact (red-team greps every track's
  code); no sealed-key reads beyond the 6 forensics-opened originals;
  no scoring manual-tiling bearing counts (N30/N32); no post-hoc
  partitions; n≥3 kill rule; no coordinator-applied bars — red team
  adjudicates every status change; strict no-double-count (one
  observation = one leg).
- Harness rules: the banked prototype imports the Smith's RepairedModel —
  do NOT "fix" the failing import by re-pointing at the round-6
  objective; adoption bar PRIMARY ≥ 0.20 on `score_fresh.py`; scope stays
  ZERO until C1 (F57: the failure is in the likelihood, not the weights —
  scorer reweighting within the 5-gram+lexicon family is EXHAUSTED).

---

## 4. Word-segmenter handoff — PENDING

`code/crowd13/segmenter/memo-to-smith.md` has NOT landed (the
`segmenter/` dir does not exist). Noted as pending; the relay goes out
when the memo lands. Nothing in §§1–3 depends on it.

## 5. Search-scope status: ZERO, maintained and re-confirmed

- No joint search was run; none is scoped. Track A's step-4 anneal was
  never cleared (H1). Track C's pilot was never cleared (NULL-v3). Track
  D's step-4 gate anneal is cleared (R8) but NOT executed. Track B is
  mid-training. C1 has not run, let alone passed.
- **Main-fleet search scope stays ZERO until C1 passes on the
  register-gapped family. No R5005 runs. Ever. Until the gate passes.**

## 6. Channel health

One-way disk channel intact: tracks place `PREREG.md` in their track
dirs; red teams review from disk (no `subagent.send` at this depth —
parent forwards follow-ups). All tracks' PREREGs acknowledge the
standing hard constraints. The fleet's PREREGs do not cite the liaison
memos — consistent with the diagnostic charter (cleared steps touch no
R5005-derived values; the §3 constraints are prospective for the future
joint scorer). Round-13 batteries running but unadjudicated: homophone-cd
WO2 (`PREREG.md` landed 23:04; `homophone_cd.py` + `homophone_cd_results.json`
executed — results NOT yet ruled, not constraints); islet audit (empty —
pending); @998 conditioner WO (pending); 20="fois" battery (pending);
"mêleront" rival battery (pending).

## Pointers

- Architect plan: `code/council/solver-architecture.md`
- Track-D v2 revision: `code/side-homophonic-rebuild2/track-d/PREREG-D-v2.md`
- Track-D pilot: `code/side-homophonic-rebuild2/track-d/PILOT-REPORT.md`
- Experiment 0 (running): `code/side-homophonic-rebuild2/track-d/experiment_0.py`,
  `experiment0.log`
- Cell-space solver fork: `code/side-homophonic-rebuild2/track-d/solver-cell/solver.py`
- Track A result: `code/side-homophonic-rebuild2/track-a/results/rescore.json`
- Track C v3 static: `code/side-homophonic-rebuild2/track-c/boundary_scores_v3.json`
- Solver-side red team: `code/side-homophonic-rebuild2/redteam/RULINGS.md`
- Round-12 adjudication: `code/crowd12/redteam/RULINGS-ROUND12.md`
- Full constraint base: `code/crowd10/liaison/smith-constraints.md`;
  deltas: `code/crowd11/smith_liaison/smith-constraints-round11.md`,
  `code/crowd12/smithliaison/smith-constraints-round12.md`
