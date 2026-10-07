## scorer-smith: identifiability attack (round 5, work order 7)

- Context: The round-4 joint engine was declared "model-correct but search-broken"
  (N30): truth -2.65 beats annealed -3.05, so the failure was diagnosed as an
  identifiability/search problem (flat landscape from the lossy 96-vs-~700 key).
  Work order 7 told me to attack identifiability two ways — (a) better search
  (parallel tempering, smarter proposals, longer runs), (b) shrink the space with
  the F33 conditioned-polyvalence rules — and to read (not duplicate) the
  side-homophonic solver mid-flight for synergy/contradictions.
- Decision: Before running either route, I re-derived N30's headline numbers in
  the current `joint_engine.py` on the sealed round-4 control — and the
  "model-correct" claim does not survive contact with the configured objective.
- Why: Truth key + the model's own E-step decode scores -2.64 ONLY with
  lam_poly=0 (penalty disabled) — that is N30's "-2.65". On the actual search
  objective (lam_poly=10), truth scores -32.64 vs the annealed key's -2.91: the
  truth sits ~30 nats BELOW the "best" nonsense. The polyvalence penalty
  (10 nats/key-level vs a per-letter-normalized letter term) makes v2
  un-addable by construction (needs >~58,000 nats of letter improvement to pay
  for itself); the annealed key ends n_poly=0 and the islet bar (>=2/3) is
  unmeetable. Worse: even with the penalty off, the letter 7-gram alone prefers
  the annealed key (-3.11/letter) over truth (-3.64/letter). The search is
  optimizing correctly — the objective is wrong. This CONFIRMS the
  side-homophonic fleet's independent diagnosis (their pilot: degenerate
  salad -3.89/pair beats truth -4.44/pair on a char 5-gram) and explains why
  their model stack (phonetic projection + spanning word bonus + concentration
  penalty) is the repair ours lacks.
- Enlightenment: The "flat landscape" framing was backwards. It is not that the
  search cannot find truth's basin — there IS no basin: the objective ranks
  truth below fluent nonsense. N30 compared truth-with-penalty-off against
  annealed-with-penalty-on (which paid nothing at n_poly=0): apples to oranges.
  Second surprise: the round-4 control's own metric is partly unidentifiable BY
  CONSTRUCTION — the lossy tail inheritance makes group 41's "true primary"
  'ri' (emitted 1.8% of 274 occurrences; modal emitted 'mi' 2.2%, 160 distinct
  cells) unrecoverable by any likelihood method. Max achievable top-1 on the
  bar is 0.90, and 2/20 bar groups are lottery tickets. The side fleet's
  control (frequency-weighted homophony, well-defined primaries, Les Mis
  register gap) is the better-designed test.
- For the report: belongs in the round-5 scorer-smith section + the
  methodology lessons. The 1-3 numbers: truth -32.64 vs annealed -2.91 on the
  configured objective (N30's -2.65 was penalty-off); letter-term truth -3.64
  vs annealed -3.11 per letter; poly penalty needs >~58k nats to ever pay.
  Import list for the engine: phonetic projection, spanning word bonus,
  concentration penalty ON (LAM_HOM is currently 0.0), homophone-pool/block
  proposals, per-stream chi2-gated phase (no banked map). Fix lam_poly scale
  first — it is a model bug, not a search tuning.
- Caveats: Route (a) better-search (parallel tempering DONE: gbest -2.88,
  top1 0.05 — no better than the best single-chain baseline restart at -2.59;
  smarter proposals + basin test still in flight) and route (b) shrink-space
  (COMPLETE — see below) run in `code/crowd5/scorer_identifiability*.py`,
  results in `scorer_identifiability.json`. The side-homophonic positive
  control's first attempt was SIGTERMed mid-scoring (owner revised the harness
  mid-batch); new runs (`run2`, `frozen-ctl-*`) in flight, no verdict yet.
  I did not touch R5005; the gate holds.

## Route (b) verdict (COMPLETE 2026-10-07 ~16:00Z)

- **b1 (hard-known: 12 pins, 3 islet (v1,v2) fixed, 301-cell inventory):**
  best -33.54..-33.56 vs truth ceiling -33.43 — the search reaches within
  0.13 nats of truth's objective value. top1 0.35-0.40 (4x baseline's
  0.00-0.10), islets 1/3 (vs 0/3). Shrinking the space DOES fix the search
  half of the problem: the basin becomes reachable.
- **b2 (conditioned polyvalence, R4/F33 rules):** 0/15 groups verify a
  pre/suc-group conditioning rule; 0/3 true islets verify — the honest
  expected negative (the control plants UNCONDITIONED islet coins, while F33
  says real polyvalence is conditioned). Documents a control-vs-reality gap:
  the control cannot test conditioned-polyvalence machinery.
- **b3 (small inventory alone, 7 pins):** best -2.67/-2.83, top1 0.05 —
  no better than baseline. Inventory shrink without hard readings is not
  enough.
- Net: space-shrinking gets the search to truth's neighborhood (b1), but
  recovery still stalls at top1 0.35-0.40 < 0.50 bar with decode agreement
  ~0.09 — because the letter model's miscalibration (-3.11 nonsense beats
  -3.64 truth per letter) is independent of search. Fix the objective first;
  then the constraints will carry it over the bar.
