# TRACK-D PREREG-D-v2-branchB — Branch-B pipeline re-registration (BINDING per R12a)

**Track:** D (LM-judge, solver-rebuild round-2 fleet).
**Date:** 2026-10-07.
**Status:** PRE-REGISTERED (Branch-B fork of PREREG-D-v2). PREREG-D-v2.md is
UNTOUCHED — this file is the mechanical re-specification the red team made
BINDING before Stage-2 clearance (R12a: seed counts, triage placement,
judge-call budget, code-pinned lexicon-start construction). No gate work
runs until this file is red-team-cleared.
**Author:** track-d Branch-B re-registration agent.

## 0. Branch context (why this exists)

Experiment 0 went **6/6 SLIDE** (PREREG-D-v2 §1): initialized AT the truth
key, the frozen annealer abandons it on every instance, landing 2,375–2,722
nats above J(truth) at chance-level primary recovery (0.000–0.034). Truth is
not a local optimum under J on any instance. Consequences, all pre-registered
in v2 and endorsed by R12(a):

- §3 Stage 2 (J-climbs) is **dropped** — J-climb endpoints carry no truth
  signal (rec ≤ 0.034), so triage-over-J-climb-endpoints is dead.
- §3 Stage 4 (judge-guided ILS) is **promoted to the primary loop**,
  seeded from lexicon starts rather than J-climb endpoints.
- The 100/60/40 seed split and the 280/170 judge-call split from Branch A
  do **not** carry over: both were sized around a J-climb stage that no
  longer exists.

## 1. The Branch-B pipeline (complete, mechanical)

INPUT per instance: ct pairs (1,846), crib JSON (7 pins), Tocqueville LM,
the frozen cell-space solver fork (`solver-cell/`, objective J byte-identical
per R12(b)). OUTPUT: one 96-group → cell key. PINS: 7 GT groups fixed forever.
No `SYNTHETIC-key-18420*.json`, `sealed-pclasses.json`, or fresh plaintext
is ever read (pre-run grep self-check, logged; §8).

Notation: `inst_idx` = 0..5 for the 6 fresh gate instances in Runner order.

### STAGE 1 — diverse seeding (judge calls: 0; compute: trivial)

**Seed counts: 120 per instance = 72 lexicon-seeded + 48 crib-extended.**
Pure-random seeds are DROPPED. Justification: Experiment 0 killed every
undirected start (J-climbs dead; a pure-random start is a lexicon start
with the word-bearing structure removed, i.e. strictly less judge signal
per triage call). Every lexicon start carries a random remainder, so
diversity is not lost — the 72/48 split preserves v2's 3:2
lexicon:crib ratio while concentrating the judge budget where the judge
can discriminate. 120 (not 200): each seed now costs judge calls directly
(no cheap J-climb stage to amortize over), so the count is sized to the
triage budget below.

#### 1a. Lexicon-start construction (code-pinned; R12a/R12f)

Resolves arch §3's "crib-inventory drag" prose into an algorithm. All
choices deterministic from the seed; the single RNG stream is
`rng = random.Random(3000 + 100*inst_idx + i)`, `i = 0..71`.

1. `inv` = the frozen fork's `load_inventory('crib', pins, soft={}, lex_wt={})`
   — byte-deterministic given the 7 pins (R12(b) verified the fork).
2. `lx` = `lm_ref/lm.json['lexicon']`: 3,546 `{'w','wt'}` entries, `wt`
   descending (verified on disk).
3. Word pool: `[e['w'] for e in lx if 3 <= len(e['w']) <= 6][:200]` —
   frequency-ranked, deterministic. Band 3–6 chars: inventory cells are
   1–5 chars (115×2-char, 97×3-char on disk), so 3–6-char words tile into
   1–5 cells — long enough to be judge-visible, short enough to tile
   reliably.
4. `tile(w)`: deterministic longest-match left-to-right segmentation of
   `w` over inventory cell strings; cell order = length-desc, then
   lexicographic-asc; returns `None` if any position is un-tileable.
   `tileable = [(w, tile(w)) for w in pool if tile(w) is not None]`
   (pool order = frequency rank).
5. Group frequencies: `gf[g]` = pair-count of group `g` in the 1,846 ct
   pairs; `med` = median of `gf` over non-pin groups.
6. Place up to 12 words (stop early at 12), over 8 windows:
   - Window: draw `s = rng.randrange(0, 1846 - 8)`; take the first `T`
     consecutive pairs of the window once the word (hence `T = len(tiles)`)
     is chosen. **Frequency bias (mechanical):** accept the window iff the
     mean `gf` over its groups ≥ `med`; resample up to 10 draws, else take
     the 10th. This is the pinned meaning of "high-frequency windows."
   - Word choice: `order = rotate(tileable, rng.randrange(len(tileable)))`;
     scan the first 20 entries of `order` for the first placeable word.
   - **Conflict rule (pinned):** for positions `t = 0..T-1` with group `g`
     and tile cell `c`: if `g` is a pin, require `pins[g] == c`, else the
     word is skipped; if `g` already assigned (earlier word or pin),
     require equality, else the word is skipped; same-group positions
     inside one word must map to the same cell (checked incrementally).
     **First assignment wins; a conflicting word is skipped ENTIRELY — no
     partial commit, no overwrite, no re-pick of the window.**
7. Remainder: every unassigned non-pin group gets `rng.choice(inv)`.

A lexicon start is thus: ≤12 real inventory words spelled exactly into
high-frequency ct windows (judge-discriminable anchors), random remainder
(diversity). Expected outcome: ~40–80 of 89 non-pin groups assigned
word-consistently, the rest random.

#### 1b. Crib-extended construction (mechanical)

RNG: `random.Random(5000 + 100*inst_idx + i)`, `i = 0..47`. `inv` and
`assign = dict(pins)` as in §1a.

1. Group adjacency: `adj(g1, g2)` = count of consecutive ct pairs
   `(t, t+1)` with groups `{g1, g2}` in either order.
2. **Cell-bigram table** (built ONCE per track-d run, logged with sha256):
   tile every lexicon word with the §1a `tile()`; count adjacent cell
   pairs; `P(c2|c1) = n(c1→c2)/n(c1)` with floor `1e-6` over `inv`.
   Tocqueville-only, decode-blind, deterministic — no leakage surface.
3. For each pin `(g*, c*)` in sorted-group order: for every non-pin,
   unassigned group `g` with `adj(g, g*) >= 3` (either direction):
   `assign[g] = rng.choices(inv, weights=[P(c|c*) for c in inv], k=1)[0]`.
   **First assignment wins** (a group adjacent to two pins keeps the
   first pin's draw in sorted order); no overwrite.
4. Remainder: `rng.choice(inv)`.

Seed IDs: `bL000..bL071` (lexicon), `bC000..bC047` (crib-extended).
All 120 `assign` dicts + seeds logged before any judge call.

### STAGE 2 — judge triage (RESTRUCTURED; the v2 280-call triage is dead with the J-climbs)

The 280 triage calls from Branch A filtered 200 J-climb endpoints; those
endpoints are gone. Triage now filters the 120 Stage-1 starts:

- **Pass 1:** all 120 seeds × 1 pass (blind 8-hex labels, fresh random
  order) = **120 calls**.
- **Median pass:** top-48 by pass-1 → 2 more passes = **96 calls** →
  per-candidate median-of-3 → **top-8 = PARENTS**.
- **Triage total: 216/instance.**

Net width 48/120 = 40% (Branch A: 40/200 = 20%). The wider relative net
is justified: Stage-1 starts are pre-biased toward judge-discrimination
(§1a/§1b), and the ≤2-pt cross-pass range (R8a-verified, R12d to be
reported by the instrument) means a 48-wide net cannot lose a
truth-adjacent start to noise.

### STAGE 3 — judge-guided ILS (the primary loop)

- **Rounds:** 4. **Parents:** 8. **Neighbors:** 8 per parent per round.
- Neighbor construction (RNG:
  `random.Random(7000 + 10000*inst_idx + 100*r + n)`, `r` = round 0..3,
  `n` = neighbor index 0..63 within the round = 8 parents × 8):
  deep-copy the parent key; draw mutation count `k ∈ {1,2,3}` with
  **P = {0.50, 0.30, 0.20}**; apply `k` sequential mutations, each drawn
  from the frozen fork's proposal distribution —
  **chg1 0.30 / swap 0.10 / poly 0.10 / alias-reassign 0.30 /
  cell-swap 0.10 / alias-split 0.05 / alias-merge 0.05** (R12(b)-verified
  probabilities; pins excluded from every touched set; a no-op draw is
  re-drawn ≤5 times, then that mutation slot is skipped).
- **Neighbor judging:** 4 × 8 × 8 = **256 calls**, 1 pass each, blind,
  fresh random order. No dedup against the pool: fresh candidates each
  round, no history to stabilize (v2 §4 rationale carried over).
- **Parent selection (per round):** pool = previous 8 parents + this
  round's 64 neighbors; candidate score = median of valid passes where
  ≥2 valid (parents carry medians forward), else the single pass;
  parents = argtop8 by (score, J, −candidate-index). Tie-break: higher
  score, then higher J under the rebuilt objective, then lower candidate
  index.
- **Final:** top-12 overall by best available score × 2 more passes =
  **24 calls** → median-of-3; **WINNER = argmax median**; same tie-break.
- **ILS total: 280/instance.**

### STAGE 4 — gate scoring

WINNER's 96-group mapping → Runner scores PRIMARY/SECONDARY per
CONTROL-DESIGN.md §4 against the §7 bars (unchanged — bars do NOT move).

## 2. Judge-call budget (pinned)

| stage | calls/instance |
|---|---|
| S1 seeding | 0 |
| S2 triage pass-1 (120 × 1) | 120 |
| S2 triage medians (48 × 2) | 96 |
| S3 ILS neighbors (4 × 8 × 8 × 1) | 256 |
| S3 final medians (12 × 2) | 24 |
| **per-instance total** | **496** |
| 6-instance gate | 2,976 |
| gate-truth memorization probe (§5) | 36 |
| **program total** | **3,012** |

Vs Branch A's 450/instance (2,700 gate): +46/instance (+10%). The increase
buys what Branch B needs and drops what Experiment 0 killed: the entire
~37-min/instance J-climb compute stage is deleted, and the judge budget is
reinvested in search depth — a 4th ILS round, 8 parents instead of 5, and
256 neighbor evals vs 170 (+51%). Judge calls are the only live search
signal left; the §5 instrument makes them feasible.

Additional authorized runs (outside the 2,976 gate figure, reported
separately): the 2 diplomatic secondary-gate instances (2 × 496 = 992),
the 2× ear-noise ablation instances (2 × 496 = 992, report-only), and the
q_cycle=0 scrubbed set 184213–184218 (6 × 496 = 2,976 if run —
pre-registered check, not moved).

## 3. Variance justification (against the pilot's ≤2-pt cross-pass range)

**1-pass suffices** for (i) triage pass-1 over 120 starts and (ii) ILS
neighbor ranking within a round: cross-pass range ≤ 2 pts (18/18 pilot
candidates, R8a) means single-pass noise cannot move a candidate more
than ~2 points — the 48-wide triage net and the 8-of-72 parent cut both
have far more slack than that, and the round structure (not the median)
is the stated variance control for neighbors.

**Median-of-3 is required** for (i) parent selection across rounds —
parents carry medians forward, so a noisy promotion would compound over
4 rounds — and (ii) the final winner. Every decision that persists beyond
its round, and the final selection, rests on median-of-3; <2 valid
queries → VOID (v2 §4 rule carried over unchanged).

## 4. Judge-call protocol (carries v2 §4 / R7 / R8 verbatim)

Frozen prompt sha256 `390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d`
(DO NOT MODIFY — any prompt change = re-registration + new pilot).
Candidates = raw `join(pcell)` decode strings, unmodified (spaceless,
ear-noise spellings intact). Blind 8-hex labels; label→(instance, stage)
map sealed until logging completes. Mechanical first-line-int extraction;
EXTRACTION-FAILED logged, excluded, never re-queried. Every call logged to
`judge_log.jsonl` (timestamp, label, pass_no, prompt_sha256, raw_response,
extracted_score). Per-candidate score = median of valid queries; <2 valid
→ VOID (reported, not claimed).

## 5. Additive controls (carried over; bars do NOT move)

1. **Memorization probe on GATE truths (non-negotiable, before unsealing):**
   6 fresh paraphrases + 36 judge calls (12 candidates × 3 passes — R12g
   correction applied), blind, median-of-3. Void rule: `mT−mP ≥ 15` on ANY
   instance → gate VOID. **R12e containment (binding):** the key-holding
   Runner/coordinator — NOT the track pipeline — constructs the paraphrases
   from the gate truths and freezes them (sha256 logged) BEFORE any track
   unsealing; the track sees ONLY the paraphrase strings (forensics-class
   carve-out, logged). This resolves the v2 §10(6) tension: the track never
   reads fresh keys, pclasses, or plaintexts.
2. **Diplomatic-plaintext secondary gate:** Track A's 2 register-matched
   instances run the same Branch-B pipeline (496 calls each). The 6 Les-Mis
   instances stay the PRIMARY gate (comparability). Require the primary
   only; *believe* the secondary — pass Les-Mis + fail diplomatic = the
   solver won't transfer to R5005; report both.
3. **Noise-mismatch ablation (report-only):** 2 instances re-generated with
   2× ear-noise knobs; run the Branch-B pipeline; report degradation vs the
   primary gate.
4. **q_cycle=0 rhythm-crutch check:** the existing ablation set
   (184213–184218) stands; any solver that collapses on the scrubbed set is
   leaning on rotation, not French (pre-registered, not moved).
5. **Substitution fallback clause (R8b — registered in advance, not
   improvised):** v2 §6(5) carried over verbatim — instrument-identical
   source only, provenance logged, deviation disclosed to red team BEFORE
   downstream numbers are cited. No re-rolling, no cherry-picking.
6. **Bars frozen:** CONTROL-DESIGN.md §4 bars restated unchanged —
   PRIMARY mean ≥ 0.20 / min ≥ 0.10; SECONDARY mean ≥ 0.30 / min ≥ 0.22.
   PASS = all four; anything else = FAIL: stop, do not touch R5005.

## 6. Stage-2 entry criteria (verbatim)

Stage 2 (funnel/gate execution on the fresh instances) runs ONLY when ALL
THREE hold:

1. the §5 judge instrument has PASSED the binding acceptance test — 54
   calls on the 18 frozen pilot candidates, medians within ±3 pts of the
   pilot medians (truth ~62 / salad ~20 / paraphrase ~91), mT−mS ≥ 30 on
   all six, WITH per-candidate single-pass cross-pass range reported
   (R12d);
2. this re-registration (PREREG-D-v2-branchB.md) is RED-TEAM-CLEARED
   (Stage-2 clearance issued in redteam/RULINGS.md);
3. a logged pre-run grep self-check over `track-d/` for
   `r5005|R5005|ct_R5005` shows zero data hits — any data hit = self-KILL
   of the run (§10(1) of PREREG-D-v2).

## 7. SPS trigger (binding)

**Track D's Branch-B judge-driven funnel is declared FAILED, and escalation
to the Segment-Parse-Score fallback (council arch §7) is REQUIRED, if EITHER
of the following holds:**

**(1) the gate FAILS** — winning keys scored per CONTROL-DESIGN.md §4 miss
any of the §5 bars (PRIMARY mean ≥ 0.20 / min ≥ 0.10; SECONDARY mean ≥ 0.30
/ min ≥ 0.22) — after the judge instrument passed acceptance and the full
Branch-B budget was spent exactly as pre-registered (496 judge calls per
instance; 2,976 for the 6-instance gate; 36-call gate-truth probe). No
additional judge calls, no re-seeding, no extra ILS rounds, no
re-registration of the bars are authorized after a FAIL.

**(2) no viable automated judge instrument exists after two substrate
attempts** — (a) subagent-judges, then (b) a local/API LM endpoint, in that
order — each attempt documented with its 54-call acceptance numbers.

The trigger fires ONCE and is not re-armed for a second Branch-B attempt:
Branch B gets exactly one full-budget gate run. SPS construction begins
only after this trigger fires, and SPS itself re-registers as an instrument
(frozen spec + acceptance test) before touching any gate instance. SPS is
not built speculatively while Track D's funnel is alive. A gate PASS does
NOT authorize R5005 — that authorization is the parent's call; Step 5 (any
R5005 contact) remains FORBIDDEN.

## 8. Hard constraints (all steps, no exceptions)

1. **NO R5005 contact.** The §6(3) grep self-check is logged before the
   instrument acceptance test AND before the gate; any data hit = self-KILL.
2. Control/diagnostic only. Nothing in this track touches real data.
3. The prompt is frozen at sha256 `390a1ec0…c08e21d`. Any change =
   re-registration + new pilot (not the operator's call).
4. Deterministic seeds everywhere except the judge instrument itself
   (controlled per §4). All seeds logged: lexicon `3000+100*inst_idx+i`
   (i=0..71), crib-extended `5000+100*inst_idx+i` (i=0..47), ILS neighbors
   `7000+10000*inst_idx+100*r+n` (r=0..3, n=0..63), judge presentation
   order fresh-random per pass (controlled, logged).
5. No cherry-picking: exactly the pre-registered query counts per candidate
   per stage, medians taken, all raw responses logged, extraction failures
   logged not hidden.
6. Fresh seals (184201–184204, 184206, 184207) are read ONLY as ct pairs +
   crib JSON — NEVER their keys, pclasses, or plaintexts — until Runner
   scoring. R5005 stays sealed and untouched. (§5 probe paraphrases are
   constructed by the key-holder, never the track.)

## 9. R12a pinning checklist (for the red-team review)

- [x] **Seed counts:** 120/instance = 72 lexicon + 48 crib-extended (§1);
  pure-random dropped with justification; 100/60/40 does NOT carry over.
- [x] **Triage placement:** restructured to 120 + 96 = 216 calls (§2 triage
  stage); the Branch-A 280-call triage over J-climb endpoints is dead with
  the endpoints; triage now filters Stage-1 starts → top-48 median-of-3 →
  top-8 parents.
- [x] **Budget:** 496/instance; 2,976 gate; 36 probe; 3,012 program total
  (§2 table); secondary/ablation runs authorized and separately reported.
- [x] **Lexicon-start construction:** fully algorithmic §1a — word pool
  (3–6 chars, freq-ranked, top-200), deterministic longest-match tiling,
  frequency-biased window sampling (mean group freq ≥ instance median,
  10-draw resample), first-assignment-wins conflict rule (pins never
  overwritten, conflicting words skipped whole), ≤12 placements over
  8 windows, random remainder, RNG `3000+100*inst_idx+i`.
- [x] **ILS loop:** 4 rounds × 8 parents × 8 neighbors (§3); mutation-count
  distribution {1:0.50, 2:0.30, 3:0.20}; fork proposal probabilities pinned;
  parent selection argtop8 on (median where ≥2 valid, else single-pass)
  with (score, J, −index) tie-break; final top-12 × 2 passes → median-of-3
  winner.
- [x] **R12e containment:** §5(1) — key-holder constructs/freezes
  paraphrases, track sees only strings.
- [x] **R12d:** instrument acceptance must report per-candidate cross-pass
  range — restated in §6(1).

## 10. Outcome map

- Instrument acceptance PASS + this file red-team-cleared + logged grep
  self-check → run the Branch-B pipeline on the 6 FRESH instances → §5
  scoring.
- Gate PASS → report; R5005 authorization is the parent's call.
- Gate FAIL after the full 496/instance budget → SPS trigger §7(1) fires;
  stop; report per-instance numbers incl. where it failed (coverage? judge
  transfer? ILS stuck?); do not touch R5005.
- No viable instrument after two substrate attempts → SPS trigger §7(2)
  fires.
