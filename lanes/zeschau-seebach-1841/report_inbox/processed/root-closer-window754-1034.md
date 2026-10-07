## closer: "la premiere" windows @754 vs @1034 (round 5, work order B)
- Context: the @754 occurrence (row a5_03, the manuscript gloss line) was never
  mined — it was off-phase before the F32 parse repair. Comparative mining, +/-15
  pairs, against @1034.
- Decision: the two windows are DIFFERENT grammatical contexts, not a formulaic
  repetition. Five banked leads; F12's "back-reference" reframed as discourse
  function (no cipher-level antecedent exists).
- Why: @754 reads "...qui [02-97-e] veut la PREMIERE [20], on ne [59]..." —
  relative clause + negation matrix, with "on ne" @761-762 (the 9th of 9 on the
  repaired parse, P(94|62)=0.257 vs era 0.120). @1034 reads "...c'est [03]er
  [80]le, la PREMIERE [17], le m[63]... la veut" — contains "c'est" @1028-1029
  (feeds leg A1), the formula 64-96-43-87-01 x2, and a unique "la veut" @1044-1045
  (object pronoun + verb, supports 67="veut"). Byte-level: not identical;
  type-Jaccard 0.171 (excl. crib); phase-match 14/31. Chiasmus: 67->11 ("veut
  la") BEFORE the crib @754 vs 11->67 ("la veut") AFTER it @1034.
  "premier"/"premi-"/"pre-" occur nowhere else ([754,1034] only), so F12's
  back-reference has no cipher antecedent — both are discourse-anaphoric "the
  first [one]".
- Enlightenment: the never-mined window paid off immediately — a fresh "on ne"
  instance and the "veut la premiere" + "la veut" chiasmus. Also: the @1034
  window breaks 43="me" — 96->43 x2 both sit inside 64-96-43-87-01 and "par me"
  is era-dead (n=0); cleanest repair is conditioned polyvalence (43="me" iff
  pre!=96) or 43!="me".
- For the report: windows section — the two skeletons, the chiasmus, F12 reframe;
  leads list: (1) "on ne" @761 -> follow 59 for the 62="on" battery (round-5
  WO1); (2) "la veut" @1044-1045 -> pin 67="veut"; (3) "par 43" x2 -> adjudicate
  43 (fence pre=96); (4) "c'est" @1028 -> leg A1; (5) 17="fois" @1040 stays WEAK
  (era P(fois|premiere)=0.114 favors, but 40->17 x2 in different contexts and
  unigram 13.3x over era).
- Caveats: annotations mix GT/provisional/lead (marked per-cell in the table);
  the @1034 pre-frame segmentation ("c'est ?er ?le") unresolved; 67->11 x4 vs era
  P(la|veut)=0 attributed to corpus sparsity (n=86), not a kill. Evidence:
  code/crowd5/window754_1034.{py,md,json} (31-pair tables + deep analysis).
