## smith-liaison: round-11 rebuild2 track health + constraints delta

- Context: round-11 liaison work order (WO7). Checked the rebuild2 fleet
  (`code/side-homophonic-rebuild2/`): read all three track PREREGs, the
  red-team RULINGS.md, and verified on disk that no scored comparison has
  run since the GOs. Banked main-fleet constraints the scorer needs —
  register-gap evidence, morpheme-salad diagnostics, the diplomatic corpus
  as the register-matched reference, the N43 noisy-detector flag, the
  contact-coherent-aliasing clue, and the R5b Guizot cross-track exclusion.
- Decision: (1) banked the round-11 DELTA memo at
  `code/crowd11/smith_liaison/smith-constraints-round11.md` (10.5 KB) — it
  carries forward `code/crowd10/liaison/smith-constraints.md` as the standing
  spec and adds the round-10 adjudication deltas (which post-date that memo)
  plus the new scorer constraints; (2) banked nothing else — main-fleet
  search scope stays ZERO until C1 passes on the gapped family, and all
  three tracks are within charter scope, so there was nothing to flag to
  the red team.
- Why: the lane rule for liaison is constraints-only until C1 (STATE.md,
  WO7). The three tracks are executing diagnostic work that needs no new
  main-fleet input; the round-10 adjudications (ISLET 10, H4g kill, @1351
  resolution) landed after the round-10 memo, so they're the deltas that
  matter. Everything else is carry-forward.
- Enlightenment: the cross-track exclusion (Guizot spans [100000,104000) /
  [200000,204000) reserved for Track A's instances, binding on Track B's
  manifest) is the only live main-fleet-adjacent constraint that touches a
  currently-cleared track step — and the red team already bound it (R5b).
  The one surprise on the fence: Track A's PREREG never hard-exits on
  sanity failure (R4a, unaddressed) — a broken instrument could emit a
  citable H0/H1 line; the red team flagged it but made it non-blocking.
- For the report: belongs in the rebuild2/liaison section. The 3 numbers
  that matter: 3 GO / 0 KILL / 0 scored comparisons run (no results dirs
  on any track; no file newer than redteam/RULINGS.md); 10 islets in the
  registry (ISLET 10 registered LEAD — est-arm pre∈{64,94,93} n=6,
  este-arm pre=84; unconditioned 59="est" REFUTED kill-grade); 132/132
  R10BANK + 89/89 ROUND10-LEDGER PASS.
- Caveats: the liaison channel is one-way (disk + parent-forwarded
  follow-ups — no `subagent.send` at this depth), and no rebuild2 track
  has cited the liaison memos or the islet registry on disk. That's
  consistent with the charter's diagnostic scope (current cleared steps
  touch no R5005-derived values), but there is no on-disk acknowledgment
  that the fleet knows the islet registry exists — the hazards remain
  prospective for the future joint scorer. No R5005 runs, no scorer runs
  executed by this liaison.
