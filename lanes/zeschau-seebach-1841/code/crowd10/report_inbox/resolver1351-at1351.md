## resolver1351: @1351–1356 ownership — verdict: R-c («le [78] ne ment pas»)
- Context: round-10 WO-1. The window @1351–1356 carried three fenced items
  (H1c, H1d, frenchman triple collision, F66): the 06-islet parse «ne ment
  pas» (era-good) vs the gouvernement parse «gouvernement pas» (era-0) vs
  77="le" provisional-conditioned. Pre-registered the bar in
  `code/crowd10/resolver1351/PREREG.md` BEFORE touching data; recommendation
  only — red team adjudicates.
- Decision: **R-c owns @1351–1356** — 77="le" fires; @1353=94 "ne"
  (negation, prov-strong); @1354=82 "m" (GT); @1355=06 "ent" (ISLET 3,
  pre=82 fires); @1356=52 "pas" (STRONG). 78 unidentified. The gouvernement
  reading (R-b) is ruled OUT at @1351; the R-a/R-c difference (77 unresolved
  vs 77="le") resolves to R-c by deduction from standing F37.
- Why:
  - D1 byte-exact re-derivation from the repaired 1,847-pair parse: PASS.
    @1349–1362 = 62 48 **77 78 94 82 06 52** 37 64 35 13 92 62. W06
    re-confirmed: 82→06 at 82-positions [579,737,1183,1354] → 06 at
    [580,738,1184,1355]. (Evidence: `derive1351.py`, `derive1351.json`.)
  - D2 (94's role, decided first — 94 cannot be both negation and syllable):
    two independent pre-registered discriminators BOTH fire against R-b.
    (D2i) Era grammaticality on Nesselrode v8 strict (92,594 tokens,
    elision-split): «gouvernement pas» = 0/40 and ungrammatical (needs an
    intervening verb+ne); «ne ment pas» = grammatically perfect 1841 French
    (exact trigram 0/92k — attestation gap, honestly noted, not kill-grade).
    (D2ii) 52="pas" (STRONG) is F33-conditioned on a negation frame:
    R-a/R-c supply 94="ne"@1353 three cells back; scan of @1340–1370 finds
    NO other 94 at/before @1356 (@1363 is after). R-b strands 52="pas"
    unlicensed and would need an unbanked demotion of 52@1356 to
    "so"/"se"-LEAD. Dependency weight kills R-b.
  - D3 (77's value): F37's fenced "gou" exception at @1351 existed ONLY
    because the 5-mer might be "gouvernement". D2 kills that trigger at
    @1351, so 77@1351 falls back to the standing F37 conditioned default
    (77="le", 3 independent legs) — no banked @1351-specific adverse blocks
    it (F37's fenced "ce le"×2 are @515/@869; F51's "le me"×7 dissolved
    conditionally with @1351's 78 open). The frenchman Gate-5 clitic veto is
    conditional on 48=transitive-verb; 48 is UNIDENTIFIED (F64) — it
    constrains a non-existent conjunction, not 77="le" alone. Banked as a
    future-48 constraint (round-10 WO-2 relevant).
  - D4 dependency audit: R-c rests on GT + prov-strong + STRONG + LEAD +
    standing provisional values; R-b needed an unbanked 52-demotion and ate
    two fenced adverses (H1c, H1d).
- Enlightenment: the "triple" was really a 2×2 — 94's role and 77's value
  are separate binary choices, and R-a/R-c agree on 94/82/06/52. The
  decisive structural fact is not era counts but the **52="pas"
  negation-frame dependency (F33)**: it needs 94="ne" in range, which only
  the islet parse supplies. Also: the 06-islet CANNOT lose @1355 under any
  verdict — ISLET 3 membership is positional (pre=82) and all three readings
  keep 06="ent". The registry needs no edit (conditioner: ISLET 3 stands
  n=4/n_eff=3; only the by-ear gloss at @1355 is now "ne ment pas").
- For the report: verdict section — **R-c owns @1351–1356**
  («le [78] ne ment pas»; 78 open). Costs: (1) gouvernement thread loses
  its @1351 leg → 77="gouv" @1180-only (n=2→1; n_eff was already 1, stays
  LEAD — n≥3 kill bar binds, NO kill recommended); 78="ver" islet keeps
  positional membership (@1352 next=94) but its by-ear "ver" gloss at @1352
  dies (was fenced on the unconfirmed host → by-ear support @1181-only);
  fork 78={ver,er} unresolved. (2) H1c MOOT (target reading dead). (3) H1d
  NARROWS to {37="le" MEDIUM, 64="qui" prov} — the 37-64 "le qui" bigram
  (0/391,210, re-derived) survives this ruling; flagged for the 37/64 lanes,
  NOT adjudicated here. (4) 77="le" GAINS @1351 — fenced "gou" exception
  shrinks to @1180-only (out of scope, untouched). (5) H1e's conditional
  (IF gouvernement@1351) is vacuous — 48 lane unaffected.
- Caveats: D3's R-c step is MEDIUM-HIGH confidence (deductive, resolves a
  fenced exception — red team must rule). The «ne ment pas» exact trigram is
  0/92k v8 (grammatical, unattested). 78@1352 unidentified — if 78 ever
  resolved to the WORD "me" (currently disfavored-strong), «le me ne...»
  would break the frame; noted as future constraint. @1180's fenced state
  explicitly not touched. No re-litigation: F56's killed {77,00}="le"
  merger is the unconditioned claim, distinct from F37's conditioned 77="le"
  used here.
