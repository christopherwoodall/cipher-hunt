# Smith constraints — Round-14 DELTA memo (2026-10-07 ~18:33 CDT / 23:33Z)

Liaison (smith_liaison), round-14 work order. Read-only liaison; no
solver runs launched, no key searches, nothing on the solver side
changed by this memo. Main-fleet search scope stays ZERO until C1
passes.

**Carry-forward:** `code/crowd10/liaison/smith-constraints.md` (full
spec, STANDS) + `code/crowd11/smith_liaison/smith-constraints-round11.md`
(DELTA, STANDS) + `code/crowd12/smithliaison/smith-constraints-round12.md`
(DELTA, STANDS) + `code/crowd13/liaison/smith-constraints.md` (DELTA,
STANDS). This memo is a DELTA over the round-13 memo:
(1) rebuild-side execution state at 23:33Z — Experiment 0 DONE,
substrate-(a) acceptance attempt run and FAILED, Track B mid-training;
(2) the round-14 restructured registry relayed as solver constraints;
(3) unblock plan for the judge instrument (#1 blocker, still active).

Everything banked before stands unless a red-team ruling says otherwise.
Round-13 rulings R12/R12a–g carry forward (full text:
`code/side-homophonic-rebuild2/redteam/RULINGS.md`, R12 verdict
23:24Z).

---

## 1. Rebuild-side execution state — per item (verified from disk 2026-10-07 ~23:33Z)

### 1a. Experiment 0: DONE — 6/6 SLIDE, Branch-B endorsed

`track-d/experiment0.json` (sha256
`67d8d14245a76eeeceaf0737f53b4b8148ed4a46d11e59ca795d7e9fbc0c33a1`,
written 22:58Z) + `track-d/experiment0.log` (EXIT=0). All six original
instances 184101–184106: final J −2,357 to −2,671 vs J(truth) −4,926 to
−5,294 (ΔJ 2,375–2,722), Hamming 86–89/89 groups, primary recovery
0.000–0.034 → SLIDE by the pre-registered rule on 6/6 (STAY/DRIFT
unused). Red-team R12(a) UPHELD the Branch-B call as data-driven
(judge-guided ILS primary; Stage-2-as-designed dead; triage-over-J-climb
endpoints dead, triage-as-mechanism survives inside Branch-B).
Caveat R12c (recorded, non-blocking): probe used the OLD move set; the
"no restart-based method under J" inference generalizes via the
~2.6k-nat J-margin argument, not a probe of the fork moves.

INDEPENDENT CHECK (liaison): recomputed per-line verdicts from
`experiment0.json` values against the PREREG §1 rule
(STAY: hamming ≤ 5; SLIDE: final_J > J_truth+500 AND rec < 0.10) —
6/6 SLIDE confirmed; log line
`184101: J_truth=-4953.3 final_J=-2514.0 dJ=+2439.3 hamming=86(86np)
rec=0.034 -> SLIDE` matches the JSON's (−4953.26, −2513.99, 2439.26,
86, 0.0337) to rounding. J(truth) 184101 reproduces the verifier
reference −4,953.3 to 0.1 nats.

### 1b. Judge instrument: BUILT, substrate-(a) acceptance attempt FAILED — #1 BLOCKER STILL ACTIVE

The instrument EXISTS: `track-d/instrument/` (README, `judge_runner.py`,
`aggregate.py`, `worker_brief_template.md`, `prompt_registry.json`
pinning frozen sha256 `390a1ec0…c08e21d`, triple-checkpoint integrity
contract). At ~23:26Z it ran the binding 54-call acceptance test on the
18 frozen pilot candidates (3 agents × 6 candidates × 3 passes;
logs in `track-d/instrument-acceptance/judge-log-agent{1,2,3}.jsonl`;
sha256: agent1 `0a55f909…11afa0100`, agent2 `405688dd…dcc7efbe`,
agent3 `93a80970…56db8126bef`).

NO solver-side verdict report has been written on the attempt, and
redteam/RULINGS.md has NO ruling on it (R12 predates the run, 23:24Z).

INDEPENDENT CHECK (liaison, text-matched every acceptance candidate
against `track-d/candidates.json` — no unblinding needed; texts are
plaintext in `judge-pkg-{1,2,3}.json`): composition is correct —
6 truth + 6 salad + 6 paraphrase (the six degraded synthetic-truth
decodes look garbled but match the pilot truth labels 1386766b,
c0733a7d, fe847630, 2a87b7a9, b1eee668, 99a93f79; the six fluent texts
match the six frozen Les Mis paraphrases from `freeze_paraphrases.py`).
Prompt sha in every log row = `390a1ec0bf1a…` = frozen. All 54 calls
returned valid integer scores (no extraction failures).

RESULT vs the pre-registered acceptance criterion (branchB §6(1):
medians within ±3 pts of pilot medians; mT−mS ≥ 30 on all six):

| seed | acc truth | acc salad | acc paraphrase | pilot T/S/P | mT−mS (acc) | verdict |
|---|---|---|---|---|---|---|
| 184101 | 30 | 25 | 100 | 64/21/90 | 5 | FAIL |
| 184102 | 25 | 20 | 100 | 61/20/90 | 5 | FAIL |
| 184103 | 30 | 25 | 100 | 61/22/91 | 5 | FAIL |
| 184104 | 25 | 25 | 100 | 63/20/91 | 0 | FAIL |
| 184105 | 25 | 20 | 100 | 62/21/92 | 5 | FAIL |
| 184106 | 25 | 25 | 100 | 62/20/92 | 0 | FAIL |

- Truth: 25–30 vs pilot 61–64 → deviation −31 to −39 (tolerance ±3).
- Paraphrase: 100 vs pilot 90–93 → deviation +7 to +10.
- Salad: 20–25 vs 19–22 → 3/6 within ±3, 3/6 off by +3–+5.
- mT−mS: 0–5 vs required ≥ 30 → fails on all six.

Substance: the subagent-judge substrate does NOT transfer the
operator's judgment. The operator separated degraded truth from salad
by ~40 pts; the workers score degraded truth 25–30 (salad range) and
ceiling-hit clean fluent French at 100 (operator: 90–93). This is the
"judge doesn't transfer from pilot to gate" failure the architect plan
§7(2) named.

Additional observations (not verdicts): cross-pass range >3 on 6/18
candidates (all range exactly 5: f92201e1, a99fda69, 5ddb9969, aef82f28,
425fbb4d, 66f125bc) — R12d's "≤ ~3" bound also unmet; agent2's log has
all 18 rows sharing one coarse timestamp (`2026-10-07T23:26:27+0000`,
1-second granularity) vs agent1 batching by pass and agent3 one
row/sec — sloppy provenance, batch-effect risk.

STATUS: substrate (a) (subagent-judges) is EXHAUSTED — the run is
documented with its 54-call acceptance numbers here. Substrate (b)
(local/API LM endpoint) remains per prereg §7(2). The gate still does
not run without an automated judge instrument (hard precondition,
unchanged). Unblock plan in §4.

### 1c. Track B (neural char LM): EXECUTING — mid-training, NOT finished

`python3 train_lm.py` RUNNING (pid 2401, relaunched 22:35Z after
`rm -f ckpt.npz ckpt.json`). At last check: upd=3050, wall≈3191s
(~53 min elapsed), train_ema=2.1826, held=2.1808, lr=2e-03.
Budget: 3 epochs max (`train_lm.py:388,427`), PREREG ≈2h total → ~35%
of budget consumed, ~65–70 min remaining. Curve monotone-decreasing
(2.4957 @upd=300 → 2.1834 @upd=3000 train NLL; held-out 2.4646 →
2.1808). No scored comparison has run — the 9-step order (finite-diff
gradient check → instrument gate → sanity gates → margins) is still
ahead. Binding constraint R5b (guizot exclusion windows) stands;
non-blocking R5a provenance gap stands.

### 1d. Memorization re-probe on gate truths: NOT RUN — pre-registered, Stage-2-gated

§6(1) of PREREG-D-v2-branchB.md pins it: 36 calls (12×3 = 36; the
"6 candidates × …" parenthetical is garbled prose — R12g), run before
unsealing, with the R12e containment mechanism now specified (§5(1):
the key-holding Runner/coordinator constructs and freezes the
paraphrases; the track pipeline sees only paraphrase strings).
NOT executed — it runs after the judge instrument passes acceptance
and Stage-2 entry criteria (i)–(iii) hold.

### 1e. §6 R5005 criteria: PRE-REGISTERED (banked) — containing document NOT yet red-team-cleared

All five criteria are pre-registered in PREREG-D-v2-branchB.md §8 with
"ALL FIVE; nothing less ships" (R12(f) reviewed): board ≥11/12 with
all 10 islet-registry rules satisfied (incl. one-provisional red-team
carve-out); judge ≥ gate-mean−2σ AND ≥ 55; topic check ≥ 3 cited
period facts; independent byte-exact reproduction; perturbation ≥ 4/5
topic-survival. Substitution fallback pre-registered (R8b carried).
BUT: PREREG-D-v2-branchB.md was written 23:28Z, AFTER the R12 ruling
(23:24Z) — Stage-2 entry criterion (ii) (red-team clearance of this
re-registration) is NOT yet met. Stage-2 entry remains blocked on:
(i) passing instrument, (ii) red-team clearance of branchB file,
(iii) logged pre-run r5005-grep self-check. A gate PASS still would
NOT authorize R5005 — parent's call; Step 5 remains FORBIDDEN.

---

## 2. Round-14 registry restructure → solver-side constraints

Source: `code/crowd14/registry/REGISTRY.md` (full rewrite per red-team
R-IA1–R-IA7; supersedes `code/crowd9/conditioner/islet_registry.md`).
F-numbering jumped to F100+ (round-13 merge; N60/F100–F112). The
paradigm result: the "conditioned-polyvalence" tier was modeling WORDS
while believing it modeled CELLS. Solver-side consequences are
BINDING — the cell model in `track-d/solver-cell/solver.py` must be
re-pinned to this structure before any funnel work (see §2.5).

### 2.1 TIER 1 — word rules (dissolved islets; compositional, NOT cells)

These are frozen WORD/FRAME structures. The solver must treat them as
pre-anchored lexical units, NOT as cells the move set can split/merge:

- W-est1 — 93-59 = «l'est»; W-est2 — 94-59 = «n'est»;
  F-qui-est — 64-59 = «qui est»; W-este2 — [stem]-59 = -este verb unit
  (stems fenced tier 15: 84/06/61/44/86); 59 monovalent «est» syllable
  (SUPPORTED; unconditioned 59="est" REFUTED kill-grade — 8 adverses);
- F-qui-le — 64-77 = «qui le» frame + W-este1 — 84-59 = «[X]este» word;
- W-m'en — 82-84 = «m'en»; F-en — 84="en" in «[noun] en [V]» frame
  arms (66 / 89);
- W-par-le — 96-00 = «par le»; W-ment — 82-06 = «ment» word-final
  syllable unit.

Constraint: alias-split/merge moves must NEVER split a word-rule
cluster (e.g. 93-59, 96-00, 82-84). The old "conditioned-polyvalence"
cells 06/52/94/78 are NOT polyvalent cells — see §2.5.

### 2.2 TIER 2 — the SOLE true polyvalence: 67 et/veut fork (SUPPORTED)

The registry's ONLY genuine frame-conditioned polyvalence (R-IA6).
Conditioning rules: F33-grade R_et4/5/6 (morphologist round 7/8).
n=38; 29/38 classified (et=18, veut=11, open=9), ZERO BOTH-conflicts,
0/38 inside confirmed words (compositional dissolution fails). Open
list: [199, 630, 633, 902, 1248, 1372, 1450, 1519, 1623].
- @1248 NEITHER-fence STANDS (bound on the fork; needs a new arm or
  fork re-scope with its own ≥2-leg bar).
- Double-pour stack [1244:1255] PERMANENT FENCE, both arms
  (frame-unattested, not ungrammaticality evidence).

Constraint: 67 is the only cell the solver may model as
conditioned-polyvalent. Any other cell modeled with forked readings
must be re-justified from scratch.

### 2.3 TIER 3 — class constraints (out of polyvalence; values NULL)

- ISLET 6 — 66 word-class (F-en frame dependency); ISLET 7 — 89
  noun-class (F-en frame dependency). Constraint: 66/89 carry class
  constraints only; do not assign specific values in the solver
  inventory.

### 2.4 Homophone SPLITS (do-not-tie, solver-binding)

- {52,59} SPLIT — do NOT tie 52↔59 as homophones. 59's est-arm windows
  still read «qui est»/«n'est»/«l'est»; -este exclusivity is about
  W-este2 verb-words. 52 UNIDENTIFIED, WEAK est-arm lead (pre∈{64,94,93}
  only, never the este-arm). (R-CD1; ISLET-10 dissolution does NOT
  void the split.)
- {48,94} SPLIT (R-AB2) — do NOT tie 48↔94. 48 UNIDENTIFIED,
  ne-class pre-verbal ≠"ne" (48="ne" killed kill-grade); 48's own
  "de ce que" islet (@863) survives. H_stem leg (leg only, NOT a
  value): 48 = vowel-initial verb-stem syllable cell.
- {76,78} SPLIT (R-CD2) — do NOT tie 76↔78. 78 fork unresolved;
  re-open only if 78="ver" resolves.
- 31=VERBAL (finite) provisional-conditioned CONFIRMED (R-CC31);
  33 NULL constrained; 92 NULL constrained; 79="tout" @1799 clean;
  74-class OPEN (74 unlikely-a-verb is adverse-grade, not kill-grade).

GT anchors carried: 82="m"; 46="que"; 11="la"; 34="i"; 70="pre";
29="er"; 40="e". Provisional anchors: 96="par" (F19), 64="qui"
(F20), 77="le" (prov-conditioned), 59="est" (prov), 87="ce" (prov),
24="en" STRONG (F31), 94="ne" (prov-strong).

### 2.5 Cell-model re-pinning REQUIRED (solver-side action before funnel)

R12(b) verified the fork's cell moves against the OLD registry: the
alias-split/merge machinery was built for the four "conditioned
polyvalence" groups (06/52/94/78). Under the restructured registry:

1. Only 67 is a genuine forked cell — cell moves that create/merge
   polyvalent structure must be re-scoped to 67 (and any genuinely
   unresolved forked cell, with its own battery).
2. Word-rule clusters (§2.1) must be PINNED as units in the move set
   (excluded from alias-split, alias-reassign, cell-swap) — currently
   the fork excludes only pins (`_cell_groups` iterates nonpin).
3. The 4 homophone sets SPLIT per N60 (compositional audit) — the
   split pairs above must never be re-merged by cell-merge.
4. This is a re-registration item: the Branch-B pipeline pinning
   (R12a checklist in branchB §9) carries these cell definitions; the
   red-team clearance of PREREG-D-v2-branchB.md (Stage-2 entry
   criterion ii) must adjudicate the cell-model changes. Do NOT run
   the funnel on the old cell definitions.

### 2.6 Track C handoff — 32 word-boundary segments (F107)

32 word-boundary segments, all board-anchored, coverage 72/1847=3.90%
(anchor constraints, NOT a tiling). Rules: veto-split-inside on A+/A
interiors; NO penalty for cuts in the uncovered 96.1%. Consistency
kills banked: "en cela" supersedes "en ce" at 3/10 windows; "ment"
word-edge soft at @579/@1183 (secure @1354/@737); drag "tout ce qui"
dead at 3 windows (24="en"); "le prince"×2 vs "cela"×2 unresolvable
ambiguity flagged. Memo to Smith written (Track C handoff).
Evidence: `code/crowd13/segmenter/`.

### 2.7 Drag infrastructure (F108) — reusable, null-calibrated

`code/council/drag/`: systematic drag BUILT/RUN/NULLED in ~95s.
Positive control PASS ("par ce que" @224/@952/@1526 reproduced).
Pre-registered bar NOT met: 9 real hits vs 20-shuffle null 13.1±5.2
(FDR≈1.4; real 0.8σ BELOW null mean); decoy null 0/122 (bar tight).
6 new hits = LEAD-grade docket, not discoveries ("le prince"×2
@1240/@1401 — 81="prin" candidate; "tout ce qui"×4 @1799 via 79
clean, ×3 via 24 DEAD if 24="en" holds). Honest read: remaining
plaintext avoids top-500 formulaic phrases — a register/topic
constraint. Solver constraint: the drag is the sanctioned phrase-
hunting instrument; ad-hoc phrase drags must clear the same
null-calibrated bar or report as uncalibrated.

---

## 3. Banked cross-cutting constraints (unchanged, restated for round 14)

- Main-fleet search scope ZERO until C1 passes (F113 carry; reiterated
  in branchB §10 Outcome map — Stage-2 runs the 6 FRESH instances
  only; R5005 untouched; Step 5 FORBIDDEN).
- Track D §5 probe containment: key-holder constructs/freezes
  paraphrases; track sees only strings (R12e, pinned branchB §5(1),
  §8(6)).
- Prompt frozen: sha256 `390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d`;
  any change = re-registration + new pilot (branchB §8(3)).
- Missing-mass priors (R-MM1/R-MM2): PRIORS ONLY — no prior serves as
  a promotion leg without a fresh pre-registered battery and a new
  ruling.
- Missing mass is in uncovered syllables (~17–20 cells among the 84
  unidentified groups), not second cells for la/que/ce; identified
  cells run 2.9× hot. Digit hunt NEGATIVE → RETIRED.
- SPS stays UNBUILT while Track D's funnel is alive (R12 verdict;
  §7 trigger respected); Branch B gets exactly one full-budget gate
  run (496/instance; 2,976 gate; 36 probe; 3,012 program total).

---

## 4. UNBLOCK PLAN — judge instrument (#1 blocker)

### Status
Built (`track-d/instrument/`), acceptance attempted on substrate (a)
(subagent-judges) ~23:26Z; FAILED all 6 instances per the binding
criterion (truth 25–30 vs pilot 61–64; paraphrase 100 vs 90–93;
mT−mS 0–5 vs ≥30). No solver-side verdict report yet; no red-team
ruling yet. The gate does not run without an automated judge
instrument (hard precondition, unchanged).

### What's needed
1. Solver side publishes the acceptance verdict report on the 23:26Z
   run (mechanical numbers above — the liaison has supplied them;
   the solver side confirms and banks, or red team rules the attempt).
2. Stand up substrate (b): a local/API LM endpoint as judge worker,
   reusing `track-d/instrument/` (prompt registry, triple-checkpoint
   integrity contract, aggregation pipeline unchanged — only the
   worker substrate changes).
3. Re-run the binding 54-call acceptance test on substrate (b) on the
   same 18 frozen pilot candidates (truth ~62 / salad ~20 / paraphrase
   ~91 expected; ±3-pt median reproduction; mT−mS ≥ 30 all six;
   per-candidate cross-pass range ≤ ~3, R12d).
4. Address the transfer lesson for (b): substrate (a) collapsed the
   operator's truth−salad margin (40 pts → 0–5) by scoring degraded
   truth like salad and ceiling-hitting clean French at 100. The (b)
   prompt calibration must reproduce the OPERATOR's ordering on the
   degraded stimuli specifically — clean-fluent fluency alone is not
   the signal. Consider piloting (b) on 2–3 candidates before the
   full 54-call run (dry-run flag exists in `judge_runner.py`).
5. If (b) also fails acceptance: §7(2) SPS trigger fires ONCE — Track
   D's Branch-B funnel is declared FAILED, SPS construction begins
   (and re-registers as an instrument before touching any gate
   instance). Branch B gets no second full-budget attempt.

### Who owns it
The solver side (Smith) owns build + acceptance runs; Stage-1
clearance (R12) already authorizes instrument build and acceptance
attempts — no new clearance needed for substrate (b) (it is the
prereg §7(2)-ordered next attempt). The parent orchestrator's action:
relay this memo's §1b numbers to the solver side and ask for (1) the
verdict report, (2) a substrate-(b) proposal. Red-team rules the
acceptance outcome; Stage-2 entry still needs the separate clearance
((i) passing instrument, (ii) branchB re-registration clearance,
(iii) logged grep self-check).

### What it costs
- Substrate (b): ~54 API judge calls for acceptance + 2,976 gate +
  36 probe = ~3,066 calls per full attempt. No infrastructure the lane
  doesn't already have: `track-d/instrument/` is substrate-agnostic;
  only a worker brief for an LM endpoint is new. Time: acceptance
  re-run ≈ minutes at API latency (substrate (a) ran 54 calls in
  ~35s of wall). The expensive part is (4) — prompt calibration, not
  calls.
- Human/operator cost: zero additional operator judging is required
  by the plan (the pilot's 18 frozen medians ARE the target; the
  operator does not re-judge). If substrate (b) needs calibration
  data beyond the frozen 18, that needs re-registration — do not
  improvise operator judging.
- Risk cost if (b) fails: Track D Branch-B is over; the lane falls
  back to SPS (§7 of the architect plan) — the one place where new
  instrument construction is pre-authorized.

### What the liaison will NOT do
No solver runs, no instrument runs, no key searches from the main
fleet. The liaison keeps reading logs and banking constraints.
Main-fleet search scope ZERO until C1 passes — reiterated to the
parent for the round-14 coordinator.

---

## Verification index (round 14)

| claim | file | independent check |
|---|---|---|
| Exp.0 6/6 SLIDE | `track-d/experiment0.json` (`67d8d142…9fbc0c33a1`), `experiment0.log` EXIT=0 | recomputed verdicts from JSON values vs PREREG §1 rule → 6/6 SLIDE; log line 184101 matches JSON to rounding |
| acceptance composition 6/6/6 | `instrument-acceptance/judge-pkg-{1,2,3}.json` vs `track-d/candidates.json` | exact text match → truth 6, salad 6, paraphrase 6 (no unblinding; texts are plaintext) |
| acceptance prompt frozen | `instrument-acceptance/judge-log-agent*.jsonl` (sha256s above) | all 54 rows `prompt_sha256` prefix `390a1ec0bf1a` = registry pin |
| acceptance FAILED 6/6 | same logs | per-instance medians vs PILOT-REPORT table → truth −31..−39 pts, paraphrase +7..+10, mT−mS 0–5 |
| Track B mid-training | `track-b/train.log`, `train_lm.py:427` (3 epochs) | upd=3050, wall≈3191s, train_ema 2.1826; monotone curve 3000-upd checkpoint |
| §6 pre-registered | `track-d/PREREG-D-v2-branchB.md` §8 (23:28Z) | all five criteria present verbatim; file timestamp AFTER R12 (23:24Z) → clearance pending |
| registry restructure | `code/crowd14/registry/REGISTRY.md` | TIER1/TIER2/TIER3/4 homophone splits read from the file; supersedes crowd9 registry |
| 32 segments | NOTES.md F107 | 72/1847=3.90%, veto-split-inside rule, `code/crowd13/segmenter/` |
| drag | NOTES.md F108, `code/council/drag/` | 9 real vs 13.1±5.2 null, FDR≈1.4, decoy 0/122 |

Open questions for the parent: (a) relay §1b acceptance numbers to
the solver side for the verdict report — who writes it (solver side
or solver-side red team)? (b) substrate-(b) proposal approval;
(c) branchB re-registration red-team clearance scheduling (Stage-2
entry criterion ii). Nothing above requires main-fleet action —
search scope ZERO stands.
