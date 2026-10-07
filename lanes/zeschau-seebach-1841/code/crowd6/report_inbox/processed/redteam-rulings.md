## Red Team: round-6 armed baseline + adjudication framework

- Context: Red team for Seebach round 6, holding kill authority over all
  seven executors' promotion claims (Frenchman, Morphologist, Bigram Closer,
  Scorer Smith, Segmenter, Closer, Inventorist). No claim packages have
  landed yet in `code/crowd6/` — this note arms the adjudication instrument
  BEFORE the claims arrive, so rulings are mechanical and traceable.
- Decision: (1) Extended the round-5 verification instrument
  (`code/crowd5/redteam/verify_baseline.py`, 30/30 PASS — left untouched, not
  rebuilt) into `code/crowd6/redteam/verify_baseline.py`: 30 inherited checks
  + 19 round-6 additions = **49/49 PASS** against the canonical repaired
  1,847-pair stream. (2) Banked standing kill conditions per docket in
  `code/crowd6/redteam/rulings.md`, keyed to the round-6 work orders.
- Why: Every round-5 audit lesson is now checkable by machine before a single
  claim lands. The 19 additions arm exactly the numbers the work orders
  hinge on: the 62 follower/predecessor profiles (complete, both sum to 35 =
  n62) for the on-vs-il fence; 59→46 ×2 @[216, 1190] (follow-59 lead);
  46→62=0 (the double-duty datum, N35); 64-77-84 trigram ×3 @[144, 1445,
  1801] with n_eff=1 recorded (N27 — no triple-counting the byte-identical
  phrase); the 64-77-84-59 quad ×2 refinement (F42); 87→01 ×2 @[344, 1028] +
  47→01 @[194] ("c'est" legs, F42 A1); 78→45 ×4 (45="me" drag targets, WO3);
  00→46 ×4 (F40 "pour que"); 67→11 ×4 / 11→67 @1044 (F42 chiasmus, WO7);
  96→43 ×2 («par 43» ×2 vs era "par me"=0 — F42 pressure on 43="me").
- Enlightenment: writing the chiasmus into the baseline exposed a precision
  gap in the banked prose (F26-14): the F42 chiasmus holds on the adjacent
  instances (67→11 @753 before the @754 crib; 11→67 @1044 after the @1034
  crib) but the full 67→11 distribution @[561, 669, 753, 996] includes @996
  — post-@754, pre-@1034. The armed baseline records the full distribution,
  so any executor leg must scope its instances.
- For the report: Red-team / methodology section. The 1-3 numbers: 49/49
  baseline PASS; 0/7 dockets adjudicated (no claims landed); 2 new
  methodology flags (F26-14 chiasmus scoping, F26-15 62-profile accounting).
- Caveats: No claim packages have landed in `code/crowd6/` as of 2026-10-07
  11:50 CDT — the ledger is empty and every ruling below is prospective.
  The baseline inherits round 5's stream invariants; if the canonical parse
  moves, all 49 checks must re-fire. Rulings will be appended to
  `code/crowd6/redteam/rulings.md` as packages land, with per-claim audits
  next to them.
