# Smith constraints — Round-11 DELTA memo (2026-10-07)

Liaison (smith_liaison), round-11 work order 7. Read-mostly liaison; no
Smith work duplicated, nothing on the Smith's side changed.

**Carry-forward:** `code/crowd10/liaison/smith-constraints.md` (314 lines)
is the full spec and STANDS — all round-9 F33 conditioned-polyvalence rules
(§1a–1e), the anchor set, the must-NOT-break list, scope-zero/C1 gate. This
memo is a DELTA over it: round-10 adjudication outcomes (which post-date the
round-10 memo) + new scorer-relevant constraints.

## 1. Track statuses (from `code/side-homophonic-rebuild2/redteam/RULINGS.md`)

- **Track A (register-gap diagnostic): GO (R4, 2026-10-07).** Cleared to
  execute step 3 (sanity + diagnostic rescore → `track-a/results/rescore.json`).
  Red team independently verified: 9 corpus-file sha256 match disk; 0 shared
  word-20-grams vs `data/gutenberg-17489-miserables1.txt` (119,485 Les-Mis
  20-grams tested); all files pre-1862; `lm_ref_diplo/lm.json` sha256
  `5018f44c…` matches PREREG. Perplexity caveat recorded-and-accepted
  (13.64 vs 6.42 held-out — bias toward INCONCLUSIVE, conservative for H0;
  larger lexicon 4,776 vs 3,546 is salad-favoring, also conservative).
  **Not yet run** — no `results/` dir; no file newer than RULINGS.md on
  any track. Non-blocking concern R4a: `rescore_reg.py` prints
  "MISMATCH -- STOP" on sanity fail but CONTINUES — hard-exit (`sys.exit(1)`)
  required before any diagnostic verdict prints (unaddressed as of this memo).
- **Track B (neural char LM): GO (R5, 2026-10-07).** Cleared to execute its
  9-step order. At PREREG submission `track-b/` held PREREG.md only —
  no training, no code, nothing built. Red-team verified: 14 manifest files
  exist + sha256 match; torch absent (numpy LSTM is the honest architecture);
  independent 8-gram scan reproduces the substance (13 hits, all generic
  pre-1862 idioms, 0 truth-slice overlap); adapted-salad pool premise exact
  (296 inventory items, 3,546-word lexicon, 189 distinct non-lexicon forms);
  strawman kill-switch J_current(adapted) < −2,552.3 meets the ~200-nat rule.
  Non-blocking concern R5a: 8-gram hit table internally inconsistent
  ("13 hits" text vs table summing 14; metternich-v6 4 vs 5) — reconcile
  when the scan script lands (provenance gap: original scan script not on disk).
  **Binding cross-track constraint R5b:** Track B must exclude
  guizot-memoires-t5-t6.txt word offsets [100000,104000) and [200000,204000)
  per Track-A tokenization (`build_ref.py` WORD_RE on lowercased
  marker-stripped body), applied pre-tokenization, logged in `manifest.json`;
  overlap > 0 ⇒ run VOID.
- **Track C (word-boundary inference): GO (R3, 2026-10-07).** Cleared to
  run the §4 hygiene gate then write + run `score_boundaries.py`.
  Decode plumbing done (`decodes.json` sha256 byte-exact vs PREREG).
  5 corpus-file sha256 match; independent recompute N=486,789 / C=1,717,960 /
  V=10,666 / ρ=0.28335293 exact. Hygiene gate (§4 15-gram Les-Mis scan, KILL
  at >5) not yet run; scorer not yet written. Concerns: R3a (PREREG:83 C
  typo 1,717,930 → 1,717,960; `word_stats.json` is machine authority — fix),
  R3b (B(D) is a raw total, not length-normalized; report the
  W_uni/W_len/W_bnd breakdown; the §6 300-cell pilot is the behavioral
  arbiter, not the static margin).
- **Tally: 0 KILL / 0 DEMOTE; 3 GO; nothing blocked.** Pilot gates hold:
  Track A's step-4 anneal requires a positive H0 diagnostic (re-register if
  in-band); Track C's 300-cell pilot requires PROMISING (M ≥ +800).

## 2. Round-10 adjudication deltas (RULINGS-ROUND10.md, R1–R8; post-date the round-10 memo)

All are R5005-main-fleet rulings the future joint scorer must respect.
Baseline: 132/132 R10BANK + 89/89 ROUND10-LEDGER PASS.

- **R7 — ISLET 10 registered as LEAD.** est-arm: 59=word-«est» iff
  pre∈{64,94,93}, n=6 (@103, @316, @1210, @1777, @559, @763; 7-mers all
  distinct); este-arm: narrowed to pre=84 — @1190 firm («[06-84-59] que»),
  @1448/@1804 firm («qui le [84-59]» ISLET-8 frames), @1291 FENCED
  (verb vs «la [17-84] est» ambiguous). F33 narrowing: pre=06/61/44/86
  EXCLUDED from the rule (post-hoc condition expansions — fenced LEAD
  sub-tiers: @216/@1186 = LEAD, @448/@1715 = LEAD-fenced, @554 = lean).
  **Unconditioned 59="est" REFUTED, kill-grade (8 adverses)** — the F52
  provisional is REFINED into the islet, not killed. Registry now 10 islets.
  Dependencies: 64="qui" prov, 94="ne" prov-strong, {93,8}="l'" LEAD,
  06 verb-stem-class (F21 prov), 86 verb-stem-class (F40 working),
  62="on" fenced STRONG LEAD, 46="que" GT, 11="la" GT, 77="le" prov-cond.
  Registry coordination: ISLET 8's "UNBANKED — needs 59 conditioned
  polyvalence" follow-up is now BANKED by ISLET 10; ISLET 3's
  "gouvernement frame" gloss for @1351 is stale (drop it; n_eff=3 stands).
- **R5 — @1351–1356 resolved:** R-c («le [78] ne ment pas») owns the window;
  R-b ("gouvernement") ruled OUT at @1351 (window-level, not a status kill).
  Consequences: 77="gouv" → @1180-only (stays LEAD); 77="le" GAINS @1351
  (the F37-fenced "gou" exception shrinks to @1180); 52="pas" STRONG needs
  the negation frame only R-a/R-c supply.
- **R2 — H4g (06-4-gram) REFUTED** per its own pre-registered bar (knife-edge;
  closing H4g — re-open only on new independent evidence).
- **R6 — 48 stays UNIDENTIFIED** (S-word kills banked; frenchman EV1–EV9 are
  word-frame vetoes that do NOT touch the syllable shortlist; 48="de"
  CONDITIONAL via 77="le"-pronoun ∧ 78=infinitive-initial is the only live
  word-path — test it or fence it).
- **R4 — @1248 NEITHER-fence STANDS; Gate-4 REVISED:** cela-class leg VOID
  (bare «pour cela que»=0 constituents) → era bound is now {peu}-class +
  infinitive only (finite-verb veto era-0 all corpora). 62-WO3 refuted for
  @1248 only. C2/C3 LICENSED-thin.
- **R5/R8 — 67 fork SUPPORTED** (0/6 residuals classified); -este verb ID
  UNATTRACTABLE (set-valued {manifeste, atteste, proteste, conteste, déteste};
  frenchman F-B: specific -este values era-NEUTRAL in «qui le [V]», 0/4.2M all).
- **Tension banked:** 00="pour" STRONG LEAD vs 00="le" LEAD-islet (pre=96, n=3).
  Diplomatic-corpus does NOT repair 00 (F53/F54: despatches-primary r1=9.14× —
  banked as era constraint EV10–EV13).
- **Veto ledger EV1–EV14 (R8): all banked as era constraints.** Notably:
  EV10 (59="est"-word @1447/@1803 era-absent 0/4,218,106 — VETO-grade,
  convergent with the unconditioned-59 kill); EV14 («X pas»-bare era-0 ∀X,
  with three escape hatches: 52-polyvalence, ne-account, fragment).

## 3. Constraints the scorer needs (banked from main-fleet findings)

- **Register-gap evidence.** F10 (attempt-3): n("cela")/n("ce") disagrees
  6.7× (0.041 era Tocqueville vs 0.278 Les Mis) — the register gap is real
  and measured. Track A's diagnostic is testing whether the gap is the
  blocker (H0: truth ≥+500 under the diplomatic reference while salad wins
  under Tocqueville). The diplomatic-corpus reference is validated by the
  red team (see §1); it is the register-matched reference of record.
- **Morpheme-salad diagnostics.** Salad beats truth by 2,601 nats
  (verifier-corrected, `side-homophonic-rebuild/verifier/CLOSING-VERIFICATION.md`):
  Tocqueville char-5-gram +1,540 nats to salad over register-gapped,
  ear-noised Les-Mis truth; lexicon rewards morpheme tiling +1,370;
  primary recovery 1/89 = chance. F57's C1 gate: on the mandated
  register-gapped family the rebuilt objective scores truth BELOW random
  keys 3/3 (worst gap −0.28 nats); LAM_POLY=0.05 the decisive anti-truth
  term; letter term register-saturated (+0.09 nats/letter over noise);
  word bonus register-blind. "Better search" is scoped to zero until C1 —
  the failure is in the likelihood, not the weights (scorer reweighting
  within the 5-gram+lexicon family is EXHAUSTED).
- **Noisy-detector flag (N43, crowd6/contactor).** Two findings the scorer
  must respect: (a) the unsupervised χ² contact instrument is NOISY —
  in-band 0/6 on synthetics; exact χ² magnitudes (181.3, 366.3) are NOT to
  be leaned on; rhythm EXISTENCE is confirmed by label-free lag-3 (z≈+5.6),
  not by the instrument; per-group phase arguments are flagged unless
  independently supported (~0.5 phase purity). (b) CONTACT-COHERENT
  ALIASING — uniform-random homophone aliasing fragments contact profiles
  (χ²=3.9), rotation survives only phase-coherent dealing ⇒ the real
  key-maker's aliasing is contact-coherent (positive key-structure clue,
  consistent with F33). Round-7 follow-up: invert aliasing via
  phase-conditioned contact profiles.
- **Crib constraint (methodology rule):** crib writes mute final -e (40="e"
  in "première"=pre|m|i|er|e) — kills phonetic models that need mute-e
  unwritten (R26 case law; see N17 kill of 06=/mɑ̃/).
- **The scorer's repair target list (per F57 + round-11 work orders):**
  letter-term backoff/interpolation, register-robust training, LAM_POLY
  rescale on the gapped family; then the 6-instance gate
  (`code/side-homophonic/control/CONTROL-DESIGN.md`) must pass before ANY
  R5005 run. Main-fleet search scope stays ZERO until C1 passes.

## 4. Live round-11 questions the scorer must track (hazards)

STATE.md round-11 work orders (executors running): -este verb ID (unique ID
unattainable — report what breaks the tie); 48 successor-word anchoring
(48="de"-conditional narrow path is the only live word-reading); 33's class
(@1450/@1623 decider: infinitive→veut vs nominal→et); 67 residuals
(31's second leg @1519, @1372 era frame, 52/63 @633 and 92/16 @902
board-grade readings); @1248 weak arms (peu/infinitive fenced); 06
falsifier watch (n_eff=3, H4g dead). Any of these can revalue or condition
the provisional anchor set — relay their red-team rulings when they land.

## 5. Channel health

The one-way disk channel is intact: tracks place `PREREG.md` in their
track dirs; the red team reviews from disk (no `subagent.send` tool at this
depth — the parent forwards follow-ups). All three tracks' PREREGs
acknowledge the standing hard constraints (track-a §6 explicit). The fleet
has not cited the liaison memos or the lane's islet registry in its PREREGs
— consistent with the charter's diagnostic scope (current cleared steps
touch no R5005-derived values; the hazards are prospective for the future
joint scorer). Round-10 memo is banked at
`code/crowd10/liaison/smith-constraints.md` and stands unrepealed.
