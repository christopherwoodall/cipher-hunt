## frenchman: 62="on" unblockers + gouv/er independent support (round-7 work order 9)

- Context: era/register specialist. Corpi: Tocqueville T1+T2 (221,059 tok,
  elision-split) AND diplomatic primaries Guizot t5–t6 + Nesselrode v8
  (391,442 tok, `code/side-period/corpus/`, closer's tokenization) — diplomatic
  numbers used for all rate-sensitive claims. Cipher: repaired 1,847-pair
  parse; positions per `verify_f26_17.py` (61/61). H-split respected throughout:
  no premise requiring merger of /k/+V or /s/+V; N28/N35 stays void.
  Code: `code/crowd7/frenchman/` (`u1_quon.py`, `u2_lcell.py`,
  `u3_impersonal.py`, + inline U4/U5 derivations); results JSON:
  `code/crowd7/frenchman/frenchman_round7_results.json`.

- **Verdicts up front: U1 NULL. U2 NULL. U3 NULL. U4: 48 LEAD "ne"-allophone
  → referred to WO6 (not promoted here); 98 WEAK "re"-syllable, weakened;
  16="i" LEAD-entailed (F48), WO4's battery. U5: no independent support for
  77="gouv"/78="er" outside T4 — islets stay LEAD (conditioned, n_eff=1).
  62="on": NO STATUS CHANGE (stays fenced STRONG LEAD, ear legs 1&3 only).
  Joint on/il stays tied (Δ=+0.27); unigram "il" +9.4 nats — no new
  discriminating cell, so no update.**

- U1 — "qu'on" whole-word cell: NULL. Three screens, zero survivors.
  (a) Rare (2≤n≤8) + complementizer-predecessor similarity to 46=que [GT] +
  verb-follower fraction: top cos_pre 0.175–0.207 (68, 38, 23) — diffuse,
  none verb-shaped. (b) ne/verb-follower + complementizer-pre: only 35, 36 —
  35 killed (syllable chains 35-58-35, followers 53/56/94/58, no verbs),
  36 killed (36→62 ×1: "qu'on on"/"qu'il il" ungrammatical under both).
  (c) n≤15 + X→62=0 + complementizer-pre: 32/35/44/68/83 — 44 killed
  (n=15, 4.5× over era E≈2.63 diplomatic, pre-profile not complementizer);
  68 killed (→21="me" LEAD ×2, "qu'on me" impossible); 83 killed
  (→21 ×3, →82=m ×3). The Leg-1(c) rescue (dedicated "qu'on" cell) stays
  unfalsified-but-unevidenced. Note: diplomatic P(qu'|on)=0.3088 (vs
  Tocqueville 0.2475) — Leg-1(c) adverse strengthens to E=8.96, p=2.2e-5,
  still single-datum with the same 4 caveats (h-aspiré, register,
  inconsistency, whole-word rescue).

- U2 — the l'-cell: NULL. Full screen of all 21 of 62's predecessors:
  l'-shape = vowel-GT followers {34,40,29} with zero consonant-GT followers
  {11,70,82,46} (elision obligatory). 17 killed: 74/30/51/36/77/6/2/98 on
  cons-GT followers ("l'que"/"l'la" impossible); 3 on →64="qui" ×4; 92 on
  →64 ×2; 21 on →67 ×8 ("l'veut" impossible); 20 on →67 ×3; 78 on
  "ce l'"/"le l'" predecessors; 34/40 excluded (GT letters).
  Survivors: 93 (n=14, →62 ×2), 8 (n=18, →62 ×2), 14 (n=15, →62 ×1) — all
  weak. **93="l'" is shape-STRONG but rate-KILLED**: "ne l'est" trigram @102
  (94→93→59, grammatical), "l'on" ×2 (@10/@1685), "l'er…" (→29), pre 94
  ("ne l'") — but n=14 vs diplomatic E≈32.0, P(n≤14)=2.9e-4 kill-grade
  (Tocqueville E≈44.6 gave 8.7e-8). No second l'-shaped cell exists to
  rescue it via allophony (next-best 8/14 are weak, n=18/15). Banked as
  shape-lead/rate-killed, NOT promoted. The missing l' is unexplained —
  NOT un-elided "le on" (37→62=0, 77→62=1). Discrimination math (diplomatic):
  P(pre=l'|on)=0.0365 → E[X→62]=1.28; P(pre=l'|il)=0.00043 (≈0, the 2 hits
  are punctuation artifacts — "l'il" is grammatically impossible). A future
  identified l'-cell with X→62≥1 still kills "il"; X→62=0 would be weak
  adverse to "on" (p≈0.28).

- U3 — impersonal-verb cell: NULL. Screen (94→V≥1 ∧ V→62≥1): 74 (94→74 ×3,
  74→62 ×3, 74→46=que ×3 — que-clause signature, era "faut"-adjacent rates)
  KILLED as word-verb by 74→74 ×6 self-doubling ("faut faut"
  ungrammatical; "49 74 74" ×4 — syllable or "non plus. Plus…" boundary
  behavior, not impersonal); 92 killed ("la"+"92" ×3); 93 is the l'-candidate;
  2/6/30 weak or killed (6 precedes 11=la ×4). The 9 "62 94 V" frames
  (V∈{93,64,59,26,70,79×2,88,24}): no V has a que-clause signature except
  59="est" (V→46 ×2) — and "est" is not impersonal-only. Era "faut-il"=4 vs
  "faut-on"=0 confirms the inversion test is sharp, but no "faut"-shaped V
  with V→62 exists. ("semble"/"arrive" are NOT impersonal-only in era:
  P(on|pre)=0.011/0.055 — correctly excluded.)

- U4 — 48/98/16 (62's top followers: 48×6, 98×5, 16×4):
  - 48 (n=38): flat followers (19 distinct/38 — syllable-like) but
    predecessor-cos 0.735 with 94="ne" prov-strong (shared 62/12/82
    predecessors; noise floor 0.475). **LEAD "ne"-allophone candidate —
    REFERRED to WO6's homophone battery** (contact-coherent aliasing is
    WO6's work order; not promoted here). Tension noted: 48→47 ×2
    ("ne ce" ungrammatical if 47="ce" LEAD holds there).
  - 98 (n=40): "98 83 82=m" ×3 collocation (E≈0.007 under independence —
    real structural fact; "re|com|m…" by-ear) but the "re"-syllable reading
    is WEAKENED: 62→98 ×5 vs diplomatic E≈0.52 (9.6× over; Tocqueville
    4.7×), and the downstream 96 after "98 83 82" conflicts with
    "recommander" under 96="par" prov-strong. Kept as open weak lead.
    98→98 ×3 self-loop noted (syllable-like).
  - 16 (n=28): "i" LEAD-entailed via F48 "parmi" @1196–1198 (96=par
    prov-strong + 82=m GT); consistency confirmed (82→16 ×11 "m|i"
    mi-prefix, diverse followers). **WO4 owns the 16="i" battery — no
    duplication here.**
  - Net: NO new mappable+discriminative cell → N39's unbridgeability proof
    for the on/il profile route STANDS (no follower/predecessor cell is
    both identified and discriminating with n≫2).

- U5 — independent support for 77="gouv"/78="er" (T4 @1180/@1351,
  pairs=[77,78,94,82,06]): **NULL — islets stay LEAD (conditioned,
  n_eff=1); do not promote.**
  - 77="gouv" outside T4: the five non-T4 77-78 bigrams (@7/213/647/1077/
    1542) read as "le|me"-shaped (F51's 5/7 dissolution), never "gouv|er".
    @647 ("77 78 52 82 94") is NOT a second "gouvernement" — it reads
    "gouv|er|52|m|ne", no French word fits (would need [77,78,94,82,06]).
    Era "gouv*" E≈6.3 windows vs 2 observed byte-identical — topic-consistent,
    n_eff=1 stands. The 5-mer 77-78-94-82-06 occurs exactly 2× at pair
    alignment (the "×5" digit repeat straddles pair boundaries).
  - 78="er" independent: no clean non-T4 "er" window. 78→40=e ×3 ("er|e"
    feminine) plausible-but-ambiguous; 67→78 ×4 not infinitive-shaped
    (67="veut" is finite); 78→45 ×4 "er|me" ("ferme"/"terme") contradicted
    by "le même qui" @313 (37="le" MEDIUM + 64="qui" prov); 47→78 ×5
    ("ce|er…") unclear; 78→48 ×2 ("er|ne"?) stacks two unproven allophones —
    not claimed. Phase: 78 and 29="er" share label phase C (N43 purity
    caveat — weak instrument; no support for phase-conditioned allophony,
    but homophony without phase-conditioning not excluded).
  - Era morphology CORROBORATES the ruling (not independent of T4, but
    independent of the cipher windows): "*vernement" 554 = ALL
    "gouvernement*" (gouv|erne|ment per F38's own memo), "*verrement" 0,
    "*ernement" 478 — "ver" has no independent morphemic existence; "er"
    wins at T4 by lexicon, as ruled. "ver"-general killed on rate
    (n78=31 vs era "ver"-morpheme E≈2–3) — consistent with the fork's
    existing conditioning.
  - The ruling's "what would change this" items (second non-byte-identical
    "gouvernement" window; independent 78="er"-vs-"ver" evidence) REMAIN OPEN.

- 62="on" status recommendation: **NO CHANGE.** All four ranked unblockers
  returned NULL (U4's 48 is a WO6 referral, not a new mappable cell for the
  profile route). 62="on" stays fenced STRONG LEAD on ear legs 1&3 only;
  N39's honest null UPHELD and extended to diplomatic register. The single
  weak positive (+0.91 nats, Leg 2(b)) and the single caveated adverse
  (Leg-1(c), now p=2.2e-5 diplomatic) remain 1-vs-1 — promotion and demotion
  both correctly withheld. Most promising future direction: 93="l'"
  (shape-strong, rate-killed — reinstatement needs an allophony model or a
  rate explanation); WO6's homophone battery (48 as "ne"-allophone).

- Traceability: `code/crowd7/frenchman/u1_quon.py` (+`u1_quon.json`),
  `u2_lcell.py` (+`u2_lcell.json`), `u3_impersonal.py`
  (+`u3_impersonal.json`), `util.py`,
  `frenchman_round7_results.json`. All cipher counts re-derived on the
  repaired parse in this round's code. No promotions made; nothing merged.
  Red team holds kill authority over any future promotion from these leads.
