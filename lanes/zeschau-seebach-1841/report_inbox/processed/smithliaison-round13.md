## smithliaison: round-13 constraints memo + rebuild-fleet status

- Context: council round-13 WO8 — bank main-fleet constraints for the
  rebuild fleet (Track A/B/C/D in `code/side-homophonic-rebuild2/`), relay
  unabsorbed items from the council solver-architecture plan, and confirm
  search scope ZERO. Liaison only: no solver runs, no key searches.
- Decision: wrote `code/crowd13/liaison/smith-constraints.md` (round-13
  DELTA over the round-10 full memo + round-11/12 deltas, which all stand).
  Banked: 12 board values (7 GT + 5 provisional, 77="gouv" demoted,
  59 provisional holds, 77="le" conditioned), the 10-islet registry with
  an UNDER-AUDIT flag (round-13 islet-audit/ is empty — auditor may
  dissolve some into word rules), the 5 discriminating windows with
  round-12 amendments (@1351 resolved to the 06-islet parse, @1248
  NEITHER-fence + peu leg 5/9 + double-pour stack ERA-VETO, named
  "par ce que"×3 GT-anchored formula), and the must-NOT-break list
  (incl. unconditioned-48="de" KILLED, gouvernement KILLED at all 7
  windows, v8 phrase-zero VOID rule, strict no-double-count).
- Why: the rebuild fleet finally has EXECUTION STATE to bank. The three
  results that matter: (1) Track A H1 SUPPORTED — M_d=+2,200.68 nats,
  sanity +2,601.0 exact: register-matched training does NOT rescue
  truth; the LM family is the blocker, not the register. (2) Track C v3
  NULL-v3 — per-char gate failed (truth −6.74/char < salad −4.67/char):
  the salad's tiles are adversarially French word-forms; bigram terms
  can't see adversarial placement of real words (third honest null;
  SPS fallback logic corroborated). (3) Track D Experiment 0 running —
  184101 SLIDE (dJ=+2,439.3, rec=0.034): truth is NOT a local optimum
  under J with single-group moves; first datum favors the architect's
  Branch B (drop Stage 2, judge-guided ILS primary). Cell-space moves are
  implemented in `track-d/solver-cell/solver.py` per architect §4.
- Enlightenment: the night converged three independent nulls onto one
  lesion — the objective LIKELIHOOD rewards the salad structurally
  (Track A: not register; Track C: not boundaries; Experiment 0: not
  even a local optimum). F57's "failure is in the likelihood, not the
  weights" is now triply confirmed. The judge is the only instrument
  that discriminates (Track D pilot 6/6, margins 39–43).
- For the report: solver-rebuild status section. Numbers that matter:
  Track A H1 M_d=+2,200.68 (H0 needed truth ≥+500 under diplomatic ref);
  Track C v3 M=+2,683.86 but per-char −6.74 vs −4.67 → NULL-v3;
  Experiment 0 184101 → SLIDE (dJ=+2,439.3 nats, hamming=86, rec=0.034);
  Track B training at upd=1950, held_ema=2.2655 (in progress);
  Track D step-4 GO cleared (R8) but not executed; automated judge
  instrument NOT stood up (2,700-call gate blocked).
- Caveats: Experiment 0 is 1/6 (5 runs pending; branch undecided);
  Track C v3 static result not yet red-team reviewed; R4a/R5a concerns
  resolved (R4a hardened via sys.exit(1)) / pending (R5a); segmenter
  memo (`code/crowd13/segmenter/memo-to-smith.md`) has NOT landed —
  pending; islet registry under round-13 audit (binding until ruled);
  §6 R5005 criteria not yet pre-registered by the solver-side red team;
  §5 control changes (memorization re-probe, 2 diplomatic instances,
  noise ablation) NOT built. Scope stays ZERO until C1 passes on the
  gapped family — no R5005 runs, ever, until the gate passes.
