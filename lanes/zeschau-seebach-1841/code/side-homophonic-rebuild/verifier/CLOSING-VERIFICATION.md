# CLOSING VERIFICATION — Seebach rebuild pilot FAIL (2026-10-07)

Independent verifier. Method: read-only rescoring with my own code
(`verifier/rescore.py`, written from the REBUILD.md §1 spec — NOT from
`diag_rescore.py`), my own E-step/CharLM/phonetics/phase reimplementations,
cross-checked against the library on 3,845 strings (lexicon + inventory +
truth/pilot values; zero mismatches). No solver runs, no Smith code changes,
no R5005 contact. Sealed 184101 truth opened for post-diagnostic forensics
only.

## 1. Pilot artifacts preserved

- `pilot/rebuild-pilot-final/result.json` — sha256
  `d4e2dd6f728e3b9a56ea62b8269f13a54039c597ca5f17c122dc511ab7f1b70b`
  (identical to `/tmp` source at copy time)
- `pilot/timing/result.json` — sha256
  `a16fea5f86843a2fe16be482fab103b41ec420e86065a5f7c9b35e0ef9f560c5`
- Both `/tmp` sources existed and were copied before any rescoring.

## 2. Morpheme-salad finding: CONFIRMED (stronger than reported)

My rescore of the pilot winner (restart 199939, npoly=0) under the final
objective:

| key | S_char | S_cov | S_single | S_word | S_potts | S_conc | n_poly | total |
|---|---|---|---|---|---|---|---|---|
| planted truth | −4,865.2 | 211.4 | 0.0 | +211.4 | 0.580 | 0.0 | 6 | **−4,953.3** |
| pilot salad | −3,325.7 | 1,581.3 | 559.4 | +1,021.9 | 1.521 | 10.0 | 0 | **−2,352.3** |

Every part matches the Smith's table to ≤0.1 nats (S_char, S_cov, S_single,
S_potts, S_conc, n_poly all exact). **Margin: salad beats truth by 2,601
nats** — slightly LARGER than the Smith's quoted 2,577. Reason: the Smith
quoted the annealer's pre-refine incremental best (−2,376.3); the recorded
assignment is the post-refine state, whose parts sum to −2,352.3 (refine:
+24 nats). The FAIL is, if anything, understated.

- (b) Primary recovery: **1/89 = 0.0112 — CONFIRMED** (chance level).
- (c) Morpheme composition: **CONFIRMED byte-exact** — 37 distinct raw
  values: tre×8, elle×7, ter×7, pre×7, me×6, gouverne×6, par×6, les×5,
  pro×4, ment×4, des×3, de×3, … (projected: tre×8, pre×8, ele×7, ter×7,
  mA×6, me×6, guverne×6, par×6, de×6, le×6, …).
- All four restarts beat truth (−2,352 / −2,441 / −3,046 / −2,680 vs
  −4,953). Non-winning restarts show ±hundreds-of-nats noise vs their
  recorded `best` — expected: their JSON `w2` is rounded to 4dp and
  E-step choices flip on rounding. The winner (npoly=0) has no such
  ambiguity.

## 3. R2 discrepancy: direction CONFIRMED, attribution CORRECTED

- **Shipped config (word_minlen=6) flips the diagnostic optimum:
  CONFIRMED.** My rescore: truth −4,953.3 vs frozen degenerate −6,507.8,
  margin **+1,554.5 nats** (Smith §6: +1,555). The degenerate's parts also
  reproduce exactly (S_char −2,809.7, S_word −469.8, 60 secondaries,
  conc −230).
- **"Reproduces exactly with word_minlen=0": REFUTED as literally stated.**
  On the shipped code, `word_minlen=0` gives degenerate **−1,128.6** vs
  truth **−4,460.7** — NOT R2's −4,585.6/−7,215.7. R2's exact numbers
  additionally require the **pre-§4 raw (un-normalized) S_char**. My
  reconstruction of the pre-gate code state {raw S_char + gate-off S_word +
  λ_poly=50}: degenerate raw S_char −6,251.1 (R2: −6,245.9, 0.08% off),
  truth raw S_char −7,752.0 (R2: −7,592.9, 2% off); gate-off S_word
  degenerate +4,909.3 (R2: +4,888.5), truth +703.9 (R2: +676.6). Residuals
  are R2's own-implementation deltas (their AC-equivalent scorer and E-step
  loop; their `/tmp/rt_*.py` scripts are gone with `/tmp`, so this can't be
  closed further — but the structural attribution is unambiguous).
- **R2's KILL verdict itself stands**: with the gate off the degenerate
  still beats truth (my run: by 3,332 nats). The Smith's §7 sentence should
  read "reproduce with the pre-gate code (gate off AND raw S_char)", not
  "with word_minlen=0" alone.

## 4. Goodhart assessment: narrow claim REFUTED, conclusion UPHELD

Margin decomposition (truth − salad = −2,601 nats):
S_char −1,539.5 · S_word −810.5 · S_potts −0.9 · poly −300 · conc +50.

- **The Smith's static claim is too strong.** A grid search over
  reweightings J = a·S_char + b·S_cov − c·S_single + S_potts − d·n_poly −
  e·S_conc(cap) finds **854/1152 points flip the pilot with truth still
  beating the frozen degenerate** — e.g. (a=b=c=1, d=50, e=20, cap=2):
  M1=+809, truth −5,953 vs degen −12,498; or (a=1,b=1,c=2,d=50,e=20,cap=2):
  M1=+1,368. So "no reweighting of the current terms could cover ~2,600
  nats without killing truth" is **false as stated** — many cover it
  statically.
- **But the conclusion ("needs a new French model") survives**, because
  the pilot criterion is about the annealer's *argmax*, not one static
  matchup. Every static flip taxes *incidental* features of this salad
  (lexicon-word values → S_single; repetition → S_conc), while the core
  misalignment — **S_char(salad) > S_char(truth) by 1,540 nats and
  S_cov(salad) > S_cov(truth) by 1,370 nats — is a property of the
  LM/lexicon no reweighting removes**. Against an *adapted* salad
  (non-lexicon morphemes, all-distinct values, n_poly=0 — all achievable
  from the 296-item inventory), truth's margin is
  M = −1539a − 1370b − 6d − e·S_conc_truth ≤ 0,
  with equality only at a=b=d=e=0 — at which point the objective contains
  no French-likeness signal at all and truth still isn't the argmax
  (96 distinct non-lexicon values score ≈0 + potts > truth's ≤0). There is
  **no weighting in the current term family under which truth is the
  robust argmax**. Note n_poly structurally favors salad (truth pays 300
  for 6 genuine secondaries; any salad pays 0).
- **Quota-overlap claim: CONFIRMED in substance, minor numeric
  correction.** Projected-value max quotas: truth = 6, 8, 7, 7, 11, 9
  across seeds 184101–184106 (Smith: "6–10"; 184105 measures 11);
  salad = 8 (184101), 7–8 on other restarts (Smith: "8–9"). The
  distributions overlap heavily — concentration cannot separate the
  truth-class from the salad-class, exactly the Smith's point.

## Verdict

1. Pilot artifacts preserved? **YES** — both `/tmp` result.json files
   copied to `pilot/` with sha256 recorded.
2. Morpheme-salad independently confirmed? **YES** — all parts to ≤0.1
   nats, recovery 0.0112, composition byte-exact; margin is 2,601 nats
   (not 2,577 — the Smith quoted the pre-refine best).
3. R2 discrepancy resolved? **PARTIALLY** — shipped config flips the
   optimum (+1,554.5, confirmed); R2's KILL direction confirmed; but the
   "reproduces exactly with word_minlen=0" attribution is incomplete —
   R2's numbers need the pre-§4 raw S_char as well.
4. Goodhart assessment upheld or refuted? **BOTH, at different levels** —
   the narrow "no reweighting can cover 2,600 nats" is refuted (854/1152
   static flips, e.g. λ_conc=20/cap=2); the conclusion "needs a new French
   model" is upheld (no weighting makes truth the robust argmax against an
   adapted salad; proof sketch in §4 above).

**Recommendation: concur with the Smith — DO NOT run the fresh batch on
this objective.** The failure is in the likelihood, not the weights.

## Files

- `verifier/rescore.py` — independent rescorer (own CharLM/E-step/
  phonetics/phase implementations; 3,845-string cross-check vs library)
- `verifier/verify.py` — driver for findings 2–3
- `verifier/sweep.py` — Goodhart reweighting grid search
- `verifier/parts.json` — measured score parts (truth/salad/degen)
- `pilot/rebuild-pilot-final/result.json`, `pilot/timing/result.json` —
  preserved artifacts

## Caveats

- Sealed truth keys for 184101–184106 were opened for forensics only
  (quota distributions); no solver was run on any seed.
- Non-winning restart totals carry w2-rounding noise (4dp in JSON flips
  E-step choices); the winner (npoly=0) is exact.
- R2's `/tmp/rt_*.py` scripts are unrecoverable (`/tmp` ephemeral), so the
  5–159 nat residuals against R2's own implementation are attributed, not
  closed.
