## finisher67: round-9 67 classification + @1248 ruling

- Context: STATE.md WO4 — classify the 9 open 67 windows (round-8
  morphologist left 29/38 classified), rule on @1248 ("pour 67 que",
  NEITHER et nor veut), coordinate with the 62-resolver without duplicating
  its work. Worked in `code/crowd9/finisher67/` (`prereg.md`,
  `score67_r9.py`, `results_r9.json`). Era: Nesselrode v8, lane tokenizer
  verbatim (97 dateline docs, NW=92,123). Standing battery
  (`battery67_final.json` R_et1..6, R_veut1..3, R_et5 fence) re-checked
  mechanically: none of the 9 fires any standing rule.
- Decision (PACKAGE — red team adjudicates everything):
  - @1248 → NEITHER-fence UPHELD (option (c)). Bar N1 passed F1∧F2∧F3:
    parse-verified; n("pour et que")=0 ∧ n("pour veut que")=0 on v8;
    new-arm census null — "pour * que" middles are {cela:3, empêcher:1},
    n("pour ce que")=0, no single-syllable X with era support, so new-arm
    option (a) declined with evidence, re-scope (b) not attempted.
    Ruling recorded CONDITIONAL pending the 62 N35 battery per
    RULINGS-FINAL WO-3 (procedural; the fence legs do not involve 62).
  - @199 → NEITHER-fence, CONDITIONAL on 08="l'" (LEAD, F61). Bar N1 passed:
    parse-verified; n("l et")=0 ∧ n("l veut")=0 on v8 ("60 l' 67 76":
    neither fork arm can follow the elided article). Second fenced
    NEITHER-class window under the F63 mechanism.
  - @630 → et-CONDITIONAL (new rule candidate, Bar E2, 2 legs):
    L1 n("et l'")=63 vs n("veut l'")=1 (frame "67 l' 52", cond. 08="l'");
    L2 n(11→52)=3 (11="la" GT → 52 nominal → article-parse "et l'[52-noun]"
    beats pronominal+infinitive "veut l'[52]"). Conditions: (C1) 08="l'",
    (C2) 67 is a standalone word at @630 — under the competing clitic-"me"
    reading n("ce me et")=n("ce me veut")=0, i.e. NEITHER instead. C2 is
    unresolvable on current evidence; the condition is explicit.
  - @633, @902, @1372, @1450, @1519, @1623 → open-residual (no standing
    rule, no pre-registered bar fires; not forced).
  - Design-time null (recorded, not attempted): R_veut4 (pre==78 → veut via
    clitic-"me" kill) DROPPED — v8 n("me et")=0 AND n("me veut")=0 voids the
    legs; suc-side 67→78=veut ×4 (R_veut2) does not transfer across
    direction (object-of-infinitive vs forward clitic — different syntax).
- Why: the fork's legs are word-space era asymmetries on anchored frames;
  the only frames among the 9 with ≥2 pre-registerable legs were the two
  "l'"-adjacency windows (@199 pre-side, @630 suc-side) and the already-fenced
  @1248. Everything else had at most one leg (recorded unscored as leans) or
  none. Forcing classifications on single legs would violate the ≥2-leg bar
  rule, so 6 windows stay honestly open.
- Enlightenment: the exploratory counts killed my own best idea first —
  I designed R_veut4 (pre==78 → veut) expecting "me veut" to carry it, and
  v8 returned n("me veut")=0, n("veut me")=0: the "veut me"-syllable frames
  have zero word-space support on Nesselrode v8 (R_veut2 itself is standing
  and not re-litigated — but nothing new can be built on that direction).
  The "l'" frame then flipped sign on me twice: pre-side "l' 67" kills both
  arms (@199 NEITHER), suc-side "67 l'" favors et 63:1 (@630/@1519) because
  era "et l'" is 60+/63 article+noun while the single "veut l'" is
  pronominal+infinitive — and 52's "la 52" ×3 (GT-anchored) picks the
  nominal parse. Conditioning discipline is the whole game here: every
  positive result carries an explicit, falsifiable condition.
- For the report: 67-fork section. Numbers that matter: 29/38 classified
  (standing, unchanged); +1 conditional-et (@630); 2 NEITHER fenced
  (@1248 upheld, @199 new conditional); 6 open-residual. Fork stays
  SUPPORTED with amended scope (fenced n=2). Era legs all on Nesselrode v8:
  "pour et que"/"pour veut que"=0/0; "l et"/"l veut"=0/0; "et l'"/"veut l'"=
  63/1; "ce me et"/"ce me veut"=0/0; "pour * que" middles cela:3,
  empêcher:1. Artifacts: `code/crowd9/finisher67/{prereg.md,
  score67_r9.py,results_r9.json}`.
- Caveats: (1) @199's fence and @630's et both condition on 08="l'"
  (LEAD, not provisional) — if 08 is revalued, both reopen. (2) @630's C2
  (67 standalone word) is unresolvable; the clitic-"me" competitor gives
  NEITHER, so the et recommendation is genuinely conditional, not a
  classification. (3) E2/L1 conflates article-"l'" with pronominal-"l'"
  (disclosed in prereg). (4) Unscored leans are not classifications:
  @1519 et-lean (L1-only; 31's class contradictory: "la 31" 1× vs "qui 31"
  2×); @1450/@1623 et-lean (suc==33 3/3 et on classifieds, all R_et1-
  confounded); @1372 shares "16 91 67" with @1519 (observation only).
  (5) 62-coordination: resolver62 round-9 returned HOLD (no bar met;
  62="on" stays fenced STRONG LEAD, 62="il" DISFAVORED-STRONG; "@1248 still
  needs its own ≥2-leg arm — the WO3 blocker is carried forward, not
  resolved"). No substantive interaction found between 62's value and the
  @1248 fence legs; no on/il tests run here (no duplication).

## For the red team to rule on

1. Bar N1/@199: does the conditional NEITHER fence stand (on 08="l'"), or
   does @199 stay open-residual?
2. Bar E2/@630: does conditional-et stand with C1∧C2 explicit, or does the
   unresolvable C2 send @630 back to open-residual? Rule on the L1
   article/pronominal conflation.
3. @1248: uphold the fence with the 62-conditionality carried forward
   (resolver62 HOLD — blocker not lifted, no status change).
4. Confirm the 6 open-residuals and the amended fork scope (SUPPORTED,
   fenced n=2: @1248 + @199-conditional).
5. Confirm design-time null R_veut4 stays dropped.
