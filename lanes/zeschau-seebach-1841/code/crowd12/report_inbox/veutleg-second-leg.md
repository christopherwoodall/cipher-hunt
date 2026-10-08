## veut-second-leg: pre-side subject bar for lean-veut @1450/@1623
- Context: STATE.md round-12 WO-2. F79's decider made 33 infinitive-class and
  left 67="veut" LEAN at @1450/@1623 (one check; >=2-check rule). This package
  is check 2: the pre-side. Under 67="veut", the adjacent predecessor (36
  @1449 / 66 @1622) MUST be the subject -- nominal and subject-capable. A
  verbal 36/66 would kill the veut-arm at that window. Era license checked on
  Nesselrode v8 (WO-directed), verbatim lane tokenizer. Bar pre-registered at
  `code/crowd12/veutleg/PREREG.md` (2026-10-07 21:24 UTC) BEFORE any
  computation; script `veutleg.py` implements it literally; results in
  `veutleg_results.json`. Byte-exact windows verified: @1450 =
  59-36-67-33-46, @1623 = 78-66-67-33-46 (repaired 1,847-pair parse).
- Decision: **second leg NULL** -- clean null at both windows; lean-veut
  stays LEAN. No status change recommended. 67 stays provisional, fork stays
  SUPPORTED.
- Why: cipher-side classes both UNRESOLVED under the pre-registered bar
  (>=2 distinct licensor legs; decider windows excluded; no recycled cells):
  - 36 (n=8 excl. @1449): ZERO nominal licensors; ONE verbal licensor
    (suc=29 "36-er" @421, E=0.195, p=0.18 chance-consistent). |nom|=0,
    |vrb|=1 -> UNRESOLVED, not VERBAL (bar needs >=2 distinct; the bar is
    the bar, F72 case law). Pre-side otherwise: "pour 36" x3 (@740/@1313/
    @1585; E=0.24, p=1.3e-3) -- ambiguous cell (00 excluded from scoring per
    prereg), banked as datum.
  - 66 (n=18 excl. @1622): ONE weak nominal licensor (pre=77 "le" @88,
    E=0.43, p=0.35 chance-consistent); ZERO verbal. |nom|=1 -> UNRESOLVED.
    Pre-side otherwise: "pour 66" x7 (E=0.54, p=4.95e-07) with ZERO article
    contacts (11/08) in 18 windows -- ambiguous cell, unscored, but an
    extreme excess banked as the lead below.
  - Era E1: n("veut")=59 in v8; subject-pronoun predecessors (il 12, on 10,
    elle 4, qui 4, cela 1) = 31/59 = 0.5254 >= 0.50 bar -> PASS (thin
    margin, honestly noted). Noun subjects also attested (empereur, roi,
    france, prusse, autriche, palmerston, canitz). "ne veut" x11 = negation
    frames, not subjects. So the era DOES license a nominal 36/66
    predecessor -- the license holds; the cipher side simply doesn't supply
    the class.
  - Alternative (b) negative (byte-exact, pre-registered): 33-positions with
    suc==46 are EXACTLY [1451, 1624] -- the decider pair. No other "33 que"
    frame exists in the stream, so (b) has no independent discriminator (the
    "que" is the discriminating element per census33; "veut 33-er" @1424 is
    same-arm consistency, "et 33-er" @273/@1477 shows et+infinitive is fine
    WITHOUT "que"). Reason (a) was pursued, documented.
- Enlightenment: the pre-side didn't discriminate -- it went quiet. Both
  predecessors sit in the ambiguous middle: 36 leans verbal on sub-bar
  evidence ("pour 36" x3 + "36-er" x1, neither reaching the bar), 66 leans
  nominal on sub-bar evidence ("le" 66 x1) while its "pour 66" x7 screams
  for the infinitive member of F65's broad class. The honest read: the data
  refuse to resolve, and a null with named missing legs is the correct
  output. The bar's conservatism (F72: knife-edge bars are still bars) held.
- For the report: round-12 section; belongs under the 67 fork / lean-veut
  tracking. The 3 numbers: CLASS(36)=UNRESOLVED (0 nom / 1 vrb), CLASS(66)=
  UNRESOLVED (1 weak nom / 0 vrb), E1=0.5254 PASS. Joint: NULL.
- Caveats: (1) 36's class rests on n=8 -- low power; a larger sample could
  flip it either way. (2) E1 margin is thin (0.5254 vs 0.50 bar); the
  subject-premise license is real but not overwhelming. (3) F79's decider is
  itself red-team-pending; if 33's class is overturned, this whole leg is
  moot. (4) The person/number agreement question for 66 (F65's nous/vous
  member; F82-noted new battery) was explicitly fenced, not tested -- the
  bar licenses the subject SLOT, not agreement. (5) "pour"-cells are
  ambiguous by pre-registration; the x7/x3 excesses are leads, not legs.
- Banked leads (not scored): L1 -- 66 infinitive-vs-noun narrowing: "pour
  66" x7 at p=4.95e-07 with zero 11/08 article contacts in 18 windows; if 66
  narrows to infinitive, *"66 veut" kills the veut-arm at @1623 (agreement/
  category kill). L2 -- 36 verbal lean: "pour 36" x3 (p=1.3e-3) + "36-er"
  @421; needs a second distinct verbal licensor to become a kill. L3 --
  clean-corpus (3.96M diplomatic) cross-check of E1, available per F77, not
  run (WO directed v8).
- Evidence: `code/crowd12/veutleg/PREREG.md`, `code/crowd12/veutleg/veutleg.py`,
  `code/crowd12/veutleg/veutleg_results.json` (full pre/suc tables, firings,
  binomial nulls, E1 top-25). Red team adjudicates; recommendation only.
