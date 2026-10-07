## red-team: rulings on the side-homophonic control + solver

- Context: red-team pass (kill authority) over the synthetic control
  (`code/side-homophonic/control/`) and the joint-inference solver
  (`code/side-homophonic/solver/`), executed while the control batch was in
  flight (launched 15:20:29Z; no recovery claimed yet) and while the Smith
  was still editing the solver (solver.py/METHOD.md/config.json changed
  15:22–15:29Z mid-review). Full numbered rulings with file+line citations:
  `code/side-homophonic/redteam/REDTEAM-RULINGS.md` (2 KILL / 4 DEMOTE /
  8 CONCERN / 11 UPHELD). Sealed keys were read only for verification
  (ceiling, rank-baseline, purity, determinism); nothing fed back to the
  solver.

- Decision: **2 KILLs.** (K1) `solver/control_harness.py:49-56` gates on the
  Smith's superseded 0.50-proposal bars, not the Designer's registered §4
  bars (mean ≥0.20/min ≥0.10 primary; mean ≥0.30/min ≥0.22 secondary) —
  wrong in both directions (false negatives below 0.50; false positives via
  no secondary check, no 6-instance aggregation). The running batch's
  CONTROL-PASS/BROKEN labels will be wrong. (K2) The registered SECONDARY
  (decode accuracy) **cannot be computed**: `control/generator.py::
  write_instance` drops per-position `'planted'` (kept in memory at :483,
  used for the chance baseline at :587, never written), so the harness
  scores a proxy that is a deterministic reweight of PRIMARY with zero
  independent information. No PASS verdict is registrable until `'planted'`
  is persisted (deterministic rebuild verified bit-identical on 184101, so
  the fix is mechanical).

- Why: every structural claim was attacked with the Designer's own
  ammunition and measured against the sealed keys. Phase calibration: the
  occurrence-χ² band [181,320] is real but generator-internal — the
  solver's own instrument (verbatim `reference_chi2`) reads 0.4–787,
  in-band 0/6, gate ≤0.026 on 4/6 (DEMOTE-1); independently verified
  planted-phase purity is 0.62–0.66 on all six, so the coin-flip is a
  clustering artifact and the contact-coherence axis the proposals use IS
  certified (UPHELD-11). The 6-instance luck math holds (~28σ on the mean
  bar; UPHELD-1). The rank-match shortcut is dead under the register gap
  (Tocqueville ranks: 0.000–0.034 ≤ chance; UPHELD-2) but alive behind it
  (oracle ranks: up to 0.191 ≈ the bar — CONCERN-5). The primary metric's
  true ceiling is ~0.53–0.60 under perfect phonetics (projection collisions
  + 3–7 groups/instance with planted cells missing from inventory), so the
  0.20 bar is ~36% of achievable — stiffer than advertised, still valid
  (DEMOTE-2). The solver's SA choice genuinely addresses the diagnosed
  failure (round-1's z=+17.7 confident-wrong ⇒ objective, not sampler;
  UPHELD-3); the patchwork (spanning-only, S_conc) is reactive pilot-tuning
  with pilot recovery 0/89→2/89 ≈ chance and unverified pilot/control
  disjointness (CONCERN-2); the running batch tests pre-S_conc code
  (CONCERN-3).

- Enlightenment: the two fiercest-looking attacks both collapsed into
  corroboration. The frequency-rank shortcut I expected to threaten the bar
  scores *below* chance with the solver's actual reference — the register
  gap the Designer insisted on is doing real work. And the Designer's
  "noisy detector" confession verified even stronger than claimed (purity
  0.62–0.66, not ~0.5) — which is exactly what demotes the gate while
  upholding the contact axis. The real kills were procedural, not
  mathematical: the wrong gate function and the uncomputable secondary.

- For the report: belongs in the side-homophonic solver section as the
  red-team gate. Numbers that matter: 2 KILL / 4 DEMOTE / 8 CONCERN /
  11 UPHELD; phonetic ceiling E[primary] ≈ 0.53–0.60 vs bar 0.20; gate ≤0.026
  on 4/6 instances; secondary-min P≈1e-3 on 184101 (softest bar);
  anchor coverage 14.7% on 184101 (+32% vs real); batch launched 15:20:29Z
  tests superseded code (S_conc wired 15:29:49Z). No recovery claimed yet —
  when the batch lands, re-derive against §4 (never the harness gate),
  and no PASS is registrable until KILL-2 is fixed.

- Caveats: rulings cite solver.py md5 `37fcdd0e…` (15:29:49Z) and METHOD.md
  md5 `2de6557c…` (15:22:55Z); if the Smith edits again, CONCERN-3
  re-applies. I could not verify pilot/control disjointness or
  hyperparameter provenance from lane files (CONCERN-2/7 — needs Smith
  attestation). The 1/K collider expectation in the ceiling is an upper
  estimate (Potts string-equality may bias toward common spellings).
  Les Mis-vs-diplomatic register direction is unmeasured (CONCERN-8).

## Supplement — cross-fleet memos (folded ~10:45 CDT)

- Context: overwatch audit handed two new surfaces with a precondition
  standard — a fix that doesn't fully close the surface must be named.
  Memos: `code/crossfleet/memo-crib-inventory-to-homophonic.md`,
  `code/crossfleet/memo-parse-repair-to-homophonic.md`. New rulings:
  KILL-3, CONCERN-9/10/11, UPHELD-12 (full text in REDTEAM-RULINGS.md
  supplement). Tally now 3 KILL / 4 DEMOTE / 11 CONCERN / 12 UPHELD.

- Decision: **KILL-3 (scoped) — inventory circularity.** The solver's
  inventory and the control's planted units derive from the same rule
  syllabifier, so the control assumes the inventory family it would need to
  test; F34/N32 (word-pattern fleet: the "première" m|i|er|e tail returns
  zero candidates in a standard-French syllabified lexicon) and N29
  (upstream-syll.py is not the encipherer's table) independently doubt the
  family for R5005. A control PASS is therefore not registrable as
  R5005-readiness on the inventory axis. The Smith's fixes do NOT close
  this — stated explicitly: METHOD.md §6 and the `--inventory-mode units`
  ablation vary inventory *within* the standard-French family and cannot
  detect family-level inadequacy. Precondition for registrable PASS: the
  memo's crib-derived inventory core + re-run, or minimum an explicit scope
  limitation on the verdict. **UPHELD-12 — parse repair.** The memo's gap is
  closed: `solver/ct_loader.py` repointed at `repaired_offsets.json`, and I
  executed the byte-level verification the memo demanded — 1847 pairs, 96
  groups, `11-70-82-34-29-40` @754 and @1034 VERIFIED (md5 matches the
  protocol pin). The Smith's fix fully closes the functional precondition;
  residue is doc hygiene (CONCERN-9: RUN-PROTOCOL.md + runner-results.md
  still declare the adapter STALE and forbid running it — now false and
  blocking; CONCERN-10: `code/crib_attack.py` still feeds old-parse labels
  to the control generator — label sets identical, so no live corruption,
  but a rebuild landmine).

- Why: audit of the generator (memo Action 1) found the circularity is
  narrower than the memo's strongest reading — the control DOES plant
  letter-tier by-ear-style chunks (9–11 distinct standalone single letters
  per instance via encipher_split) and the solver's inventory covers them;
  what it cannot plant is the real encipherer's *systematic* by-ear
  chunking, because its "by-ear" is parametric noise on rule-syllabified
  units. The tolerance machinery is thus validated only against the
  generator's noise guess. On the parse: label sets old-vs-new are
  identical (31 groups shift ±1–2 in frequency; +1 pair), so the control's
  old-parse labels are fine and the 1846 synthetics stay self-consistent.
  But the repaired parse moved the contactor's unsupervised χ² 181.3 →
  **366.3** (measured with the verbatim instrument) — CONCERN-11: the
  control's [181,320] band was justified as "[real, 1.8× real]" and no
  longer contains the measurement; given the instrument is a coin flip, the
  answer is to disclaim the unsupervised anchor, not recalibrate to 366
  (cross-fleet: crowd must re-run the contactor on the repaired parse).

- Enlightenment: the two memos pulled in opposite directions — the
  inventory memo's attack *narrowed* under measurement (letter-tier by-ear
  is covered; the hole is systematic chunking habits), while the parse
  memo's "already fixed" surface *widened* it (the repair moved the χ²
  anchor the whole phase calibration rests on). Byte-level execution beats
  memo text: the adapter verification took 0.4s and closed the question
  the memo left open.

- For the report: KILL-3 belongs next to the other kills as a scoping
  precondition on any PASS ("validates inference conditional on inventory
  adequacy"). UPHELD-12 + the verification line close the parse-repair
  thread; CONCERN-9 is the immediate unblock (update the two stale docs);
  CONCERN-11 goes to the crowd fleet as a re-measurement request.

- Caveats: the crib-derived inventory prescription (memo Action 2) is
  underspecified — 7 cribs yield ~20 attested chunks, far short of the
  ~300 the solver needs; the extension method is the hard part and is not
  designed yet. The 366.3 re-measurement used my `/tmp/r5005.pairs.json`
  (repaired parse via the verified adapter); it is the contactor method
  verbatim, but the crowd fleet owns the canonical re-run.
