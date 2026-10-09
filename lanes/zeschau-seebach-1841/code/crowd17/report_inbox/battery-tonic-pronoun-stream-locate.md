# battery-tonic-pronoun-stream-locate — report

## Bar (verbatim, pre-registered)

"name at least one tonic-pronoun candidate group with distributional + gloss evidence, or fence the stream as tonicless"

## Numbered clauses

1. **Clause 1 (name arm):** at least one unvalued group named as a personal-tonic-pronoun
   (moi/toi/lui/elle/nous/vous/eux inventory) candidate with distributional evidence
   from the repaired stream AND gloss evidence (standing-value French reading).
2. **Clause 2 (fence arm):** else fence the stream as tonicless at battery grade with
   stated cause (unlocks the personal-tonic family by closing the prerequisite).

## Method

- Venue: the repaired 1,847-pair stream — `code/side-keyhunt/repaired_offsets.json`
  + `data/upstream-ct_R5005.txt`, parsed exactly as `code/side-keyhunt/repair_parse.py`
  (`[s[i:i+2] for i in range(o, len(s)-1, 2)]` per row with the repaired offsets;
  verified 1,847 pairs, 96 distinct groups). `canonical.py` never touched. R5005 read only.
- Decoded only with standing §7 values: banked 11=la, 70=pre, 82=m, 34=i, 29=er,
  40=e, 46=que; promoted 87=ce, 64=qui, 96=par, 17=fois, 79="tout", 00="pour" (A9),
  84="on" (A15), 47="ce" (A4); provisional 59=est, 77="le". No other group read.
- Five tonic-pronoun distributional signatures tested per unvalued group:
  S1 post-prepositional (after 00="pour"/96="par"), S2 pre-"ce" (47/87),
  S3 post-"est" (59), S4 post-"et" (67), S5 post-"que" (46).
- Determiner-exclusion test: a tonic pronoun never follows "la"/"le"/"ce" as
  determiner OR object pronoun — any group with determiner predecessors is
  excluded regardless of the determiner/pronoun ambiguity.
- "pour [tonic] + INF" geometry sweep: all 55 "00" windows checked for
  "00 X [INF]" with INF-shaped Y (97, "03 29", 86/66/33/92-class).

## Window-level evidence (@-offsets, 0-based pair index)

- Signature census (unvalued groups, n>=8, pp>=2 or subj>=2):
  86 (n=32, pp=13, subj=3), 33 (n=25, pp=8), 92 (n=22, pp=6), 66 (n=19, pp=7, subj=1),
  97 (n=10, pp=4), 36 (n=9, pp=3). Full table in method script output.
- Determiner-exclusion (kill-grade, reading-independent):
  - 86: 8 determiner predecessors — 77 ("le") x5, 87 ("ce") x1, 11 ("la") x1,
    47 ("ce") x1. Whether "le"/"la"/"ce" read as determiner or object pronoun,
    a tonic pronoun never follows them. **86 excluded at kill grade.**
  - 92: 3x after 11="la" (ground truth). **Excluded.**
  - 33: 2x after 47="ce" (promoted). **Excluded.**
  - 66: 1x after 77="le" (provisional) at @88 ("77 66 98" = "le [66] vient").
    **Excluded at battery grade** (single hit, provisional determiner — weakest
    exclusion, noted for re-arm).
- Hostile-window exclusions:
  - 66 at @189 (a1_05): "00 66 24" with 24 finite (follower 87=/=85 per R24) =
    "pour [66] [V-fin]" — ungrammatical under 00="pour" (A9) for any nominal or
    pronominal 66. Second hostile window; 66's candidacy needs a re-parse of
    00's class or 24's finiteness (red-team venue).
  - 97: INF/NOM-tied, never pronominal contexts; after-det=0 but class-bound.
  - 56 (n=23): predecessors span 86/98/35/48/46/01/24/96, followers span
    87/47/37/69/41/32/30/64 — 20+ distinct contexts; scattered function-word
    profile, not pronoun-shaped.
  - 36 (n=9): pp=3 but followers (74x2, 62, 29, 20, 77, 67, 70, 69) too diverse;
    below useful distributional threshold.
- "pour [X] [INF]" geometry: **zero** "00 X 97" windows, **zero** "00 X 03" windows
  stream-wide. The only "00 X [INF-shaped]" window is @714 (a5_01):
  "00 66 86" ("71 12 63 00 66 86 01 02") — X=66, already excluded above.
  "00 X 29" windows (@76, @1153, @1374, @1824) all resolve without a tonic:
  @76 = "pour la er[42]" (T3 composition), @1153/@1374/@1824 = "pour [92/86] er"
  with 29 as letter/composition, not infinitive.
- Low-frequency sweep (2<=n<=7, pp>=1, det=0): **zero** groups. No "96 X"
  with unvalued low-frequency X.
- Gloss evidence: the manuscript pencil gloss anchors only "la premiere"
  (a5_03) and "que" (a8_05) — **no pronoun gloss exists**. n(84)=25 confirmed;
  84="on" is the sole granted pronoun and sits outside the sibling tonic
  inventory (moi/toi/lui/elle/nous/vous/eux) per the adverse.

## Per-clause pass/fail

1. **Clause 1 (name arm): FAIL.** No unvalued group survives both the
   determiner-exclusion test and the hostile-window screen with a coherent
   tonic-pronoun distribution. Closest miss is 66 (sole "00 X INF" survivor at
   @714) but it is excluded at battery grade (@88, @189).
2. **Clause 2 (fence arm): FIRES.** The stream is fenced as tonicless at battery
   grade: no personal-tonic-pronoun candidate group is locatable under standing
   values. Scope is explicit — this does NOT claim the French text lacks
   pronouns; it claims no GROUP is locatable, which is exactly the prerequisite
   the parent battery ("until a tonic group is granted, NO stream battery can
   instantiate a tonic-pronoun claim") needed closed.

## Adverse answered

84="on" (25 loci) is granted and adopted as premise, not named as a candidate —
it is outside the sibling tonic inventory per the adverse. Candidate status was
tested only on unvalued groups; none qualified.

## Verdict

**NULL** (fence executed; lane convention: "name X or fence" bars record the
fence as NULL, per reseg-1564-pasent / noun-42-value / formula-49-value).

No standing/red-team verdict contradicted or downgraded; §7 intact;
canonical-stream caveat stands. R5005, sealed gates, red-team adjudication
queue untouched.

## Follow-ups proposed (nulls regenerate work; both verified ABSENT from queue)

1. **tonic-66-rearm** (P4, GATED) — re-test 66 as the sole "00 X INF" survivor
   (@714, "00 66 86") iff 77="le" provisional is killed (removes the @88
   determiner-exclusion) AND 00's "pour" class is re-scoped or 24's finiteness
   at @189 is overturned (removes the hostile window). Do not run before both
   gates clear.
2. **redteam-tonic-fence-input** (P2) — package this fence as red-team input for
   the personal-tonic family's stream-side closure: the 5-signature census, the
   determiner-exclusion table (86/92/33/66), the zero "00 X INF" geometry
   (55 windows swept, 1 candidate @714 hostile), and the gloss gap. Gather
   only; no adjudication.

## Standing items

- No numbers invented: every count traces to the repaired-stream parse above.
- Lock: created on start, deleted on completion (verified 0 matches).
