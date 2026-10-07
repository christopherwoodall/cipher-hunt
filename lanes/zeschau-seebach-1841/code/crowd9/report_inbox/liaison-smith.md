# Report note — smith-liaison (round-9 WO5), 2026-10-07 15:19 CDT

Executor: smith-liaison subagent. Scope: scoping only — no solver experiments,
no duplication of rebuild2's work.

## Delivered

**Constraints memo for the Smith** at
`code/crowd9/liaison/smith-constraints.md`:

1. **F33 conditioned-polyvalence rules** a joint objective must respect
   (conditioned islets, never unconditioned mergers):
   - 84: "en" iff pre∈{82} (GT-anchored @166→167 "m'en", n_eff=1) ∪ pre∈{66,89}
     (conditional on 66/89 noun-class readings); noun identity-NULL iff
     pre∈{77,11}; the 46-part of the condition FALSIFIED (46-84 never "en");
     9 windows residual.
   - 00: "pour" elsewhere (52 windows, STRONG LEAD); 00="le" iff pre=96
     (3 windows, LEAD conditioned).
   - 06: "ent" iff pre=82 (frozen; n=4, n_eff=3; core 94-82-06-06 @578-581,
     @1183-1186); falsifier: any 82-06 window in a verbal frame kills it;
     all other 06 windows not "ent" (verb-stem class provisional).
   - 67: et/veut fork SUPPORTED as conditioned polyvalence (19/38 classified,
     zero cross-contamination); et-arm and veut-arm conditions itemized;
     @1248 [16,00,67,46,26] = NEITHER-class, fenced.
2. **Anchor set held fixed:** 7 GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
   46=que) + 5 provisional (87=ce, 64=qui, 96=par, 59=est, 77="le" conditioned).
3. **5 discriminating windows** nominated (64-77-84-59 ×2; 64-96-43-87-01 ×2;
   «la 67» @1044–1045; 94-82-06-06 @578-581/@1183-1186; @1248 NEITHER-class),
   with stated pass/fail behaviors.
4. **Must-NOT-break list:** 48="ne" kill, 93-alone rate-kill, 24="est"/H5
   refutations, 06-ent-general refutation, single-stem-for-all-06 kill,
   46-part of 84's condition falsified, mute-e crib constraint, WO-6
   second-window criterion retired, phase/refuge voids, T7/C1/no-R5005
   standing prohibitions, prototype-import and PRIMARY ≥ 0.20 adoption rules.

## Rebuild2 status — HEADLINE: not stalled

All three tracks signed off GO by the red team on 2026-10-07
(`side-homophonic-rebuild2/redteam/RULINGS.md`, 19:30; tally 0 KILL /
4 UPHELD / 6 CONCERN / 3 GO):

- **Track A (register-gap diagnostic):** instrument complete
  (`build_ref.py`, `rescore_reg.py`, `lm_ref_diplo/lm.json` sha256
  `5018f44c…`; Les-Mis 20-gram scan reproduces 0). Cleared to run step-3
  sanity + diagnostic rescore → `track-a/results/rescore.json`.
- **Track B (neural char-LM):** PREREG signed off (189-form adapted-salad pool
  verified EXACTLY with independent code; torch absent → honest numpy LSTM).
  Cleared to execute the 9-step training order. No training output yet —
  training wall-time (<2h CPU) is the next milestone.
- **Track C (boundary-informed scoring):** `decodes.json` + `word_stats.json`
  verified byte-exact; 184101 slice pre-registered (pairs 0–299). Cleared to
  run the §4 15-gram Les-Mis hygiene gate, then write + run
  `score_boundaries.py`.
- No `results/` dirs exist as of 15:19 CDT — no scored comparison has run;
  every track is executing per its PREREG order of operations under sign-off.

## Needs from the main fleet

None urgent. Three non-blocking CONCERNs are track-local (R3a PREREG C typo
1,717,930→1,717,960; R4a `rescore_reg.py` should hard-exit on sanity
mismatch; R5a Track B 8-gram table reconcile + scan-script provenance gap).
Standing offer: main fleet holds era/register-matched text (side-period
corpus; Nesselrode v8 banked as the future rate-bar corpus) and can supply
more 1830s–40s diplomatic French if the Smith's corpora prove thin.
Cross-track exclusion (Track B vs Track A's reserved Guizot word offsets)
is binding and recorded (R5b); no main-fleet action unless the Smith reuses
the trained model.

## Files

- `code/crowd9/liaison/smith-constraints.md` (this WO's deliverable)
- `code/crowd9/report_inbox/liaison-smith.md` (this note)
