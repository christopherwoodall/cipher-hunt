## bigram_closer: 77="le" exploitation (round 6)
- Context: F37 promoted 77="le" (the lane's first promotion in five rounds) with
  two fenced dependencies — the "le me"×7 dissolution (conditional on
  78="me"-syllable-LEAD) and "ce le"×2 (fenced on 87=ce). My work order:
  (a) identify 84 in the «ce qui [verbe] 84» slot, (b) stress-test the ×7
  dissolution on the repaired parse, (c) drag 78-windows testing 45="me".
  All numbers re-derived on the repaired 1,847-pair stream; baseline still
  31/31 PASS and my extension agrees with it exactly.
- Decision: (a) 84 = masculine NOUN (que-clause subject) at LEAD-grade —
  identity NULL; (b) the ×7 DISSOLVES per-instance, both fences explicit, no
  holdouts; (c) 45="me"-word DISFAVORED-strong, 78-45="même" LEAD. No promotion
  recommended.
- Why:
  - (a) Four independent cipher-side frames put 84 as a noun: «le 84» ×7,
    «la 84» ×1, «que 84 24» ×2, «que le 84 24» ×1. But the systematic era
    inversions find NOTHING: article-frame inversion (Tocqueville) gives only
    «plus» 1.93× (band-edge, grammatically impossible as a subject), «même»
    3.56×, «faire»/«fait» 7.48×/6.75×; que-subject inversion's in-band hits
    («dans», «des», «se») all fail the article frames; Les Mis agrees (NULL
    robust across registers). 84="fait" re-killed 6.75×; 84="gouvernement"
    killed 6.12×. The slot itself re-parses: 84→59 is ×4 not ×2 (F42
    undercounted), and 59→46 ×2 / 59→37 ×6 make 59="verb" a LEAD — so
    64-77-84-59 ×2 = «qui le [NOUN] [VERB]»: the verb slot is 59, not 84.
  - (b) All 7 positions re-derived (@7/213/647/1077/1180/1351/1542): 2/7 are
    the «ver»-islet inside the ×2 «gouvernement» 5-mer (dissolution fenced on
    the unconfirmed host); 5/7 are me-syllable frames (dissolution fenced on
    the 78-syllable LEAD). The independent check: P(78|77)=0.159 vs
    P(78|47)=0.179 and P(78|37)=0.143 — 77 is unremarkable, no special «le me»
    construction needed. Era («le»,«me»)=0/4570 re-derived.
  - (c) 45="me"-word dies three ways: unigram 9.14× out (generous morpheme
    count), «par me» ×2 era-0, «me qui» ×3 era-0 (kill-rule-shaped but fenced
    on 64="qui" — hence disfavored-strong, not refuted). The replacement:
    78-45="même" at 0.57× in-band with era locks («le même» 87×, «même qui»
    11×) and @313 = «le même qui» — a grammatical lock under 37="le".
- Enlightenment: the «ce qui [verbe] 84» slot was mislabeled — the verb was
  never 84. Once 59=verb is spotted (59→46 «que», 59→37 «le»), the trigram
  reads «qui le [noun] [verb]» and the @1178–1184 stretch becomes
  «[verb] le [gouvernement]», cohering three separate leads (59, 37, 5-mer)
  in one window. Also caught and fixed my own Counter-iteration bug (iterating
  a Counter yields each key once — every "top-N" list was singletons) before
  it contaminated the JSON; the filed numbers are post-fix.
- For the report: three one-liners — (a) 84: noun-class LEAD, identity NULL,
  verb slot re-assigned to 59; (b) "le me"×7 dissolved conditionally, both
  fences mapped per-instance, zero holdouts; (c) 45="me"-word disfavored-strong,
  78-45="même" LEAD (0.57×, «le même qui» lock @313). Numbers that matter:
  84→59 ×4 (F42 correction), P(78|47)=0.179 ≥ P(78|77)=0.159, 9.14× / 0.57×.
- Caveats: 59="verb" is a 2-leg LEAD needing its own battery (not promoted);
  the «que 84 24» frames pressure the 24="en" lead (flagged, not a kill);
  @144 «qui le 84 er» unclassified (single instance); the «même»=me|me
  reading implies 45/78 homophony for one syllable (F35-consistent, untested
  beyond the bigram); WO2 coordination — the 96 verb battery should use 59,
  not 84/96, as the verb in the @1800 window (noted, not duplicated).
