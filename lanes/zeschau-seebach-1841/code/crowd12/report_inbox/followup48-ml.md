## followup48: 48 follow-ups — ML-1, ML-2, @863 (round-12, STATE.md WO5.5)

- Context: F83 fenced all three 48 paths with explicit missing legs:
  ML-1 (@1078 infinitive-ID), ML-2 (pre=12 licensor-ID), and the @863
  "de ce que" follow-up pointer. This executor ran all three as pre-registered
  batteries (PREREG.md written before any fresh era count) on Nesselrode v8
  strict (92,594 tokens), repaired 1,847-pair parse, by-ear syllabifier v1.2
  verbatim. Code + JSON: `code/crowd12/followup48/`
  (followup48.py, followup48_results.json).
- **Prose-label correction (byte-exact):** F83/D4 prose says "ML-1: @1077
  infinitive-ID" / "@1077 (grp 78 here)". Byte-verified stream: @1075=12,
  @1076=48, @1077=77, @1078=78, @1079=64, @1080=6. The infinitive-slot cell
  (78) is at @1078, not @1077. This package works byte-exact and flags the
  off-by-one; downstream notes citing "@1077 (grp 78)" should read @1078.

- Decision ML-1 (@1078 infinitive-ID): **OPEN, both sub-readings ADVERSE under
  banked 64="qui".** Frame: 48="de", 77="le"-pron → @1078 must be an
  infinitive: (a) monosyllabic (78 = whole inf, @1079=64 starts next word)
  or (b) inf-initial cell (@1079=64 = inf-2nd cell).
  - ML-1a (era "de [article] [INF]" rates): "de le"+INF 29×, "de la"+INF 35×,
    "de l'"+INF 54×, "de les"+INF 12× v8. Monosyllabic share (by-ear 1 cell):
    "de le" 4/29 = 0.1379, and the ONLY monosyllabic X is "voir" ("faire" and
    "croire" syllabify to 2 cells by-ear: fai|re, croi|re). "de le voir" = 4×.
  - ML-1b (era, reading (b)): v8 infinitives with by-ear 2nd syllable "qui":
    **0**. Levant sensitivity: 0. ⇒ ADVERSE-for-(b) under 64="qui".
  - ML-1c (era, reading (a)): "de le [mono-inf] qui" = **0** v8, 0 levant. ⇒
    ADVERSE-for-(a) under 64="qui". ML-1c' (token after "de le voir"):
    {partir, et, ce, attacher} ×1 each — "de le voir ce qui" exists (1×:
    "trouver l'occasion de le voir ce qui") but needs TWO cells (ce, qui);
    the cipher has one (64).
  - ML-1d (cipher): 78→29 ("er" GT) = 0/31 — datum only (by-ear inf-2nd cells
    are rarely bare "er"; expected-weak either way, not scored). Positive
    surface datum: all five non-R-c 77→78 windows (@8,@214,@648,@1181,@1543)
    are surface-compatible with 78="voir"-syllable ("le voir"+X); @1352 is
    R-c-owned (78=R-c-nominal, N51 settled) and excluded.
  - Net: the infinitive SLOT is era-fine ("de le voir" 4× licenses 78 as a
    "voir"-cell), but the successor cell @1079=64 blocks both sub-readings
    under its banked value. **New explicit missing leg ML-1': identify
    @1079=64's value in this window** — tension for 64="qui" (single window,
    not a kill), or era "de le voir qui" beyond v8+levant (0 in both).
    Cipher 64→6 = 2/47 (one is this window): "qui [verb-stem]" grammatical
    but thin.

- Decision ML-2 (pre=12 licensor class): **verb-only framing REFUTED as a
  necessity; 12's class stays OPEN (adj/noun/participle/verb all compatible).**
  - ML-2a (era): L1 of v8 "de le"+INF (29 tokens, 24 distinct, hand-classified
    [FR-JUDGMENT], full list in JSON): adjective 5 (facile×2, chargé×2, +1),
    noun 9 (courage×2, plaisir×2, occasion, moyen, étonnement, habitude, lieu,
    personne), participle 2 (regretté, donnée; forcé→participle), verb 3
    (plaira, empêche, prier), other/hand 10 (et×2, est, était, que, venez,
    loin, + OCR junk tion/luil). **Adjective+noun+participle = 16/29 (55%) —
    the majority. D2b's "pre=12 must be verb/verb-final" was too narrow:**
    recorded as a prereg-scope correction, not a kill (D2b's fence stands;
    its premise set widens).
  - ML-2b (era L2 for adj/noun/part L1s): le×5, l'×2, a×2, était×2 — articles
    dominate, consistent with noun-L1 ("le plaisir de le voir", "l'occasion
    de le voir") and adjective-L1 ("il est facile de le voir", est×1 present).
    Constraint for 98: cipher @1073–1074 = 98,98 — doubled cell; if 98 were
    article-like, "98 98 12" is a mild tension (doubled article unattested);
    98 unidentified, not scored here.
  - ML-2c (cipher): n12=23. pre=70 ("pré-" prefix GT) ×3 (@348,@1119,@1548) ⇒
    12 is word-initial stem cell — compatible with all four classes. 12→48 ×5
    (@169,@709,@809,@1075,@1736). 12→33 @1642 (33=infinitive-class, F79):
    era bare (adj|noun|part, INF) bigrams = 5 tokens v8 — weak support for a
    non-verb 12 taking a bare infinitive; verb reading ("veut faire"-class)
    remains the natural fit there. pre=11 (la) = 0/23 — mild tension for a
    noun-12, softened by @241's "11-26-12" (article two cells left).
  - Net: 12 is class-compatible with adjective, noun, participle, AND verb —
    no cipher datum discriminates. **Missing leg ML-2' (positive class
    battery):** test 12 against the specific era L1 words (facile/plaisir/
    moyen/chargé-cell?) via anchor-adjacent windows — none currently touch 12.

- Decision @863 (48-47-46 "de ce que", 10× v8): **POINTER-ONLY for re-opening
  uniform 48="de"; BANK-AS-LEAD for a conditioned 48="de"-cell in 48→47 frames.**
  - 863-a (era): "de ce que" re-derived = **10/10**, KWIC hand-checked: all 10
    genuine "de ce que"+clause (e.g. "piqué de ce que tu ne lui aies pas",
    "satisfait à paris de ce que l'empereur a dit"). L1s: piqué, heureux,
    courant, quart, contente, compte, contraire, opposé, fâchés, paris —
    adjectives/participles/nouns, the SAME class set as ML-2a (cross-leg
    coherence). "de ce"+noun (non-que) = 29× v8 — the @1658 frame class
    (48-47-98) is licensed as "de ce"+noun provided 98 is nominal.
  - 863-b (cipher): @862=74, n74=34; @861=74 too (doubled cell: 74-74-48-47-46).
    74 unidentified; no banked anchor touches the frame. Reported only.
  - 863-c (48-window accounting, F83 fences reused not re-scored): 38 windows —
    23 neutral, 5 on48 (Path A fenced), 3 m48 (Path B fenced), 2 "48 pas"
    (conditioning escape), 2 de-ce frames (@863,@1658 — same construction,
    one type ×2 tokens), 1 narrow-path-pending (@1076), 1 OUT each (@126, @1350).
  - Per prereg rule, RE-OPEN of uniform 48="de" needed ≥2 INDEPENDENT licensed
    de-frames beyond the narrow path AND no anti-frame under banked premises.
    Fails on both: @863+@1658 are one construction type, and @126 is a banked-
    premise anti-frame ("m de la" 0 era under GT 82=m/11=la). ⇒ POINTER-ONLY.
  - But the conditioned lead passes its own bar (n=10 ≥ 2 genuine): recommend
    **BANK-AS-LEAD: 48 = "de"-cell in 48→47 ("de ce") frames** — a conditioned
    polyvalence reading in the F33 sense, for a future battery. It does not
    promote 48="de" and does not touch the fences.

- Recommendations for the red team:
  1. Accept the @1077→@1078 prose correction (byte-exact positions stand).
  2. ML-1: keep OPEN; register new missing leg ML-1' (@1079=64 value under
     "de le voir ___" — tension for 64="qui", single-window).
  3. ML-2: accept the scope correction (verb-only framing too narrow; era
     majority is adj/noun/participle 16/29); 12 stays unidentified; register
     ML-2' (positive class battery vs specific era L1 words).
  4. @863: POINTER-ONLY on uniform 48="de"; BANK-AS-LEAD the conditioned
     48="de"-cell-in-48→47-frames lead (F33-style) for a future battery.
  5. No status changes to 48 (stays UNIDENTIFIED), no fence lifted, no kill —
     this package is legs and recommendations only.

- Evidence: `code/crowd12/followup48/PREREG.md`,
  [followup48.py](sandbox://workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd12/followup48/followup48.py),
  [followup48_results.json](sandbox://workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd12/followup48/followup48_results.json).
  Corpus: Nesselrode v8 strict via `code/crowd9/frenchman/corpus9.py`
  (elision-split tokenizer); by-ear v1.2 verbatim in-script. No manual-tiling
  bearing counts (T7); no re-litigation of settled kills.
