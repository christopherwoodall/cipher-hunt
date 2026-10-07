## 67 RESIDUAL FINISHER: round-11 residual verdicts
**Executor:** 67 RESIDUAL FINISHER (WO-4) · **Date:** 2026-10-07
**Package:** `code/crowd11/finisher67/` (PREREG.md written before any round-11
computation; `score67_r11.py`; `results_r11.json`)
**Status:** recommendation only — red team adjudicates every status change.

- **Context:** Round 10 (F74) left 6 open-residual 67 windows, each with an
  explicit missing leg: 31's second leg (@1519), a denser era frame (@1372),
  board-grade 52/63 (@633), board-grade 92/16 (@902), and 33's class as the
  @1450/@1623 decider (WO-3, parallel). I pre-registered a bar per missing
  leg (thresholds inherited from round 10: L1 E_et≥20/E_veut≤3/ratio≥10,
  L2 n(11→W)≥2), then computed. WO-3's outcome was available
  (`code/crowd11/census33/census33_results.json`, verdict C1-infinitive,
  red-team pending) and is used as the decider input — not re-censused.
- **Decision:** 1 of 6 residuals classifies — **@633 → et-CONDITIONAL
  (C1:08="l'", C2)** on a new left-conditioned era frame. The other 5 stay
  open-residual (2 clean nulls, 2 with decider applied, 1 contested-class
  null). Fork stays SUPPORTED with amended scope (fenced n=2).
- **Why:**
  - *@633 (08-52-67-63-74):* new frame "l' * et" vs "l' * veut"
    (conditions on 08="l'" lead, left side): Nesselrode v8 gives **92:2**
    (ratio 46:1; middles noun-dominant: empereur×13, autriche×10,
    angleterre×9 — "l'empereur et l'impératrice"-type diplomatic
    coordination; veut-arm "l'empereur veut…" ×2). L1 passes
    (92≥20, 2≤3, 46≥10); L2 n(11→52)=3≥2 (standing). Sampled era
    instances verify real (not tokenizer artifact). Frenchman: both arms
    grammatical in diplomatic register; the *"je l' X veut"* split-pronoun
    reading is ungrammatical, so the veut-arm counts article-frames only —
    the rate test stays honest. → et-CONDITIONAL(C1∧C2), recommended.
    (52's own second nominal leg fails: n(08→52)=1<2; 63 has no class —
    the window classifies via the frame, the groups stay open.)
  - *@1519 (11-91-67-08-31):* L2 recount n(11→31)=1 <2 — the literal
    missing leg is not supplied. The 31-class battery (V-1519b) is
    **withdrawn as designed**: 08="l'" is article/pronoun-ambiguous, so it
    cannot serve as an unconditional nominal licensor (prereg flaw, caught
    by the frenchman check). Follow-up census: 31 is **contested, leaning
    verbal** — nominal: 11→31 ×1 (GT); verbal: 64→31 ×2 ("qui"+verb,
    prov), 31→29 ×1 (stem+"er" infinitive), 31→11 ×1 (verb+"la" object);
    08→31 ×3 ambiguous (pre-08 ∈ {17,87,67}, no disambiguation). The
    verbal-vs-nominal contradiction is sharpened, not resolved. Clean null.
  - *@1372 (16-91-67-98-00):* clean null. "et * pour"=11<20 (verified);
    the denser bare frame "et pour"=14<20 also fails — **no conditionable
    frame reaches density**, fenced or otherwise. n(11→98)=0; 98's census
    is diffuse (n=40, no nominal contact; weak verb-licensors 64×2/46/00).
  - *@902 (16-92-67-16-88):* clean null. 92's class is **contested**:
    verbal (00→92 ×6 "pour"+inf, 46→92 ×1 = 2 distinct) vs nominal
    (11→92 ×3, GT-anchored) — not board-grade. 16-as-word unmeetable:
    French has no lexical word "i" (frenchman). No conditionable era frame
    (no board word adjacent to 67). New datum banked: 92's
    infinitive/noun contest (00→92 ×6 vs 11→92 ×3) — candidate for a
    conditioned-polyvalence battery, not asserted here.
  - *@1450/@1623 ("X 33 que"):* WO-3 verdict C1-infinitive applied
    (I1 n(00→33)=8 and I4 n(33→29)=5 spot-verified ✓; E7 numbers 16:2/0
    verified ✓). F74 decider: infinitive → **veut-arm lives**
    ("veut [inf] que" grammatical; era "veut prouver que"; in-cipher
    parallel "veut 33-er" @1423–1425 with 67=veut-classified). Et-arm not
    established (E7-L1 16<20 fails). No veut-classification bar exists in
    any round — designing one now would fit known data — so both windows
    stay **open-residual with the decider applied**. The named missing leg
    (33's class) is supplied; what would classify: a pre-registered,
    red-team-approved veut-arm bar.
- **Enlightenment:** the productive move was left-conditioning: round 10
  only tried right-conditioned frames ("et * que", "et * pour"), but @633's
  window has its board anchor (08="l'") on the LEFT — "l' * et" 92:2 was
  sitting in the open. Conversely, the 08="l'" ambiguity bit twice (31 and
  92): a "l' X" contact is not nominal evidence until the article/pronoun
  reading is fixed — GT-anchored "la" (11) remains the only clean nominal
  licensor. Also: 31 and 92 both show noun/verb contests with GT on the
  nominal side and leads on the verbal side — the lane's next conditioned-
  polyvalence candidates.
- **For the report:** 67-fork section. Numbers that matter: @633
  et-CONDITIONAL(C1∧C2) [L1 92:2, L2 n(11→52)=3]; @1519 null
  [n(11→31)=1; 31 contested verbal-lean]; @1372 null ["et pour"=14<20];
  @902 null [92 contested; 16-as-word unmeetable]; @1450/@1623 open,
  decider applied [33=C1-infinitive, veut lives]. Tally if @633 granted:
  29 classified + 2 conditional (@630, @633) + 5 open + 2 fenced = 38.
- **Caveats:** (1) census33 C1-infinitive is a recommendation — red-team
  ruling pending; if it falls, the @1450/@1623 decider re-opens.
  (2) @633's et-CONDITIONAL is conditional on the 08="l'" lead (C1) and
  carries a phonological caveat ("la 52"×3 vs "l' 52" — encipherer elision
  inconsistent per the frenchman enlightenment; does not break the rate
  frame). (3) V-633c: 52≠"pas" AT @633 only (window-scoped; "l' pas
  et/veut" ungrammatical, no 94="ne" in @625–631) — not a global kill;
  F33's conditioned polyvalence for 52 stands. (4) No re-litigation of
  settled kills; no manual tiling; all counts programmatic on the repaired
  1,847-pair parse + Nesselrode v8 (NW=92,123).
