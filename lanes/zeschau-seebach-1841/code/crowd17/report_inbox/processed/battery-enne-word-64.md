# Battery report: enne-word-64

- id: enne-word-64
- date: 2026-10-08
- worker: 6a8ebb04-730c-41ca-9b7d-62d2112ade9d
- lock: code/crowd17/next-token/locks/enne-word-64.lock created 2026-10-08T06:37:09Z; no prior lock existed (fresh take, not a stale re-dispatch).

## Bar (verbatim, pre-registered before testing)

"(1) the named word spans the 'enne' letters with stated boundaries; (2) 'prenne' @1547-1550 ('70 12 94') is undisturbed; (3) 92's class is consistent across @66 ('ne 92') and @1550 ('prenne 92'); (4) the ne-battery's 'enne'-shaped fence is either cashed to the word or converted to a residual with stated cause — the battery verdict itself is NOT downgraded."

The bar was not modified after seeing data. Clause numbering fixed before testing:

- C1: A French word is named that spans pairs 34-29-40-12-94, with stated start/end boundaries.
- C2: The '70 12 94' = "prenne" reading at the a8_00 window stands unchanged by this battery.
- C3: 92 shows no class conflict between the @66 window ('ne 92') and the @1550 window ('prenne 92').
- C4: The ne-battery's 'enne'-shaped fence is cashed to a named word OR converted to a residual with stated cause; the ne-battery's 94='ne' promote verdict is not downgraded.

## Anchor note (finder anchors vs repaired stream)

The finder report's @-anchors map to the repaired 1,847-pair stream (0-based) as follows: finder's @66 = repaired @66 (92); finder's @1550 = repaired @1550 (92); finder's "@63-66 ('34 29 40 12 94')" = repaired @61-65; finder's "@1547-1550 ('70 12 94')" = repaired @1547-1549. All evidence below uses repaired-stream 0-based offsets.

## Method

Parsed exactly like code/side-keyhunt/repair_parse.py: code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, upstream tokenization [s[i:i+2] for i in range(o, len(s)-1, 2)]. 1,847 pairs, 96 types. Never canonical.py. Never invented data. Every number below traces to this stream.

Tests: (a) full-stream census of the '34 29 40 12 94' frame; (b) full-stream census of '94 92' and '70 12 94' and '12 94'; (c) 92 and 12 contact profiles; (d) French lexicon check of the forced letter string by word-family enumeration. No red-team verdict touches this window (checked); the only prior adjudication is the battery-level ne-94 promote (pending ratification), which this battery does not downgrade.

## Window-level evidence

- W1 @61-65 (row a1_01): '34 29 40 12 94' — the ONLY occurrence stream-wide. Context: @59=41, @60=08, @61=34, @62=29, @63=40, @64=12, @65=94, @66=92, @67=69, @68=13. Under banked GT (34='i', 29='er', 40='e') + 12='n' (letter) + 94='ne' (letters), the five pairs spell "i"+"er"+"e"+"n"+"ne" = "ierenne".
- W2 @1547-1549 (row a8_00): '70 12 94' = "pre"+"n"+"ne" = "prenne". Context: @1545=00, @1546=46 ('que'), @1547=70, @1548=12, @1549=94, @1550=92, @1551=45, @1552=23. Preceded by 46='que' ("que prenne").
- W3 @347-349 (row a2_05): second '70 12 94' ("prenne"). Context: '01 06 70 12 94 74 67'.
- W4 '94 92' is a closed set of exactly 2: @65-66 ('40 12 94 92' = "e n ne 92") and @1549-1550 ('70 12 94 92' = "pre n ne 92"). No other '94 92' in 1,847 pairs.
- W5 92 profile: n=22. Predecessors: 00x6, 11x3, 94x2, 84x2, 40/98/16/83/30/13/46/31/81 x1 each (confirms the finder's predecessor census). Followers: scattered, no dominant follower (2x: 79, 69, 60, 64, 62; 1x: 63, 50, 98, 47, 67, 07, 29, 61, 44, 39, 45, 65). Class open.
- W6 12 profile: n=23. Followers: 48x5, 94x3, 16x3, 41x2, 44x2, 06x2 (confirms finder note N6; the letter reading rests on GT bigrams).
- W7 '12 94' windows: exactly 3 — @64-65 (W1), @348-349 (prenne W3), @1548-1549 (prenne W2). W1 is the only non-"prenne" '12 94'.
- W8 '34 29 40' windows: exactly 3 — @61-63 (W1), @757-759 ('70 82 34 29 40' = "pre m i er e", the "premiere" crib, row a5_03), @1037-1039 (same crib, row a6_03). The "i er e" reading of 34-29-40 is crib-anchored.

## Lexicon check (C1 core)

Forced letter string: "ierenne". Family sweep:

- (a) "-ienne" feminines (parisienne, citoyenne, moyenne, terrienne, quotidienne, méridienne, vénitienne, chrétienne, sibérienne, ibérienne, libérienne, nigérienne, algérienne, cimmérienne, aérienne, martienne, saturnienne, indienne, canadienne, comédienne, tragédienne, persienne, lesbienne, ancienne, chienne; vienne, tienne, sienne, mienne): every one is [consonant]+"ienne". None contains "ier"+"enne".
- (b) "-ière" words (première, dernière, lumière, rivière, manière, bannière, lanière, civière, poussière, chaumière, frontière, sorcière, fermière, bière, pierre, fière, hier): none takes a "-nne" ending.
- (c) "-nne" subjunctives (prenne, apprenne, comprenne, reprenne, surprenne, méprenne, éprenne, déprenne, entreprenne; vienne, tienne, souvienne, obtienne, retienne, maintienne, soutienne, contienne, appartienne, devienne, revienne, convienne, parvienne, intervienne, prévienne, survienne, redevienne): none contains "ier".
- (d) "pérenne"/"perenne": needs "re"+"nne", but 29='er' is banked GT — segmentation breaks (adverse already flagged by the finder).
- (e) "-ièrent" past historics (lièrent, plièrent, crièrent, prièrent, oublièrent, marièrent): end "-ent", never "-enne".

No French word contains the substring "ierenne". The substring itself is the blocker, so no restatement of word boundaries can save the claim: any word covering the five pairs must contain "ierenne".

## Per-clause pass/fail

- C1 — FAIL (kill grade). The window forces the claim false: any French word covering pairs 34-29-40-12-94 must contain "ierenne"; no French word does (family sweep above). The claim "one French word covers @63-66" is false under banked GT (34='i', 29='er', 40='e') + the 12='n' / 94='ne' promotions.
- C2 — PASS. 'prenne' @1547-1549 verified intact ('00 46 70 12 94 92 45', "que prenne"); this battery asserts nothing at that window.
- C3 — PASS (caveated). Both 92 windows are the only two '94 92' bigrams stream-wide: same left neighbor (94), same structural slot after "nne"-final 94. 92's followers differ (@67=69 vs @1551=45) but 92's follower profile is scattered with no dominant follower, giving no class signal either way — no conflict detected. 92's class stays OPEN (see follow-up F2).
- C4 — PASS. Fence converted to a residual with stated cause (below). The ne-battery's 94='ne' promote is NOT downgraded: this kill targets only the one-word composition, decided under 94='ne' as assumed.

## Verdict: KILL

C1 fails at kill grade. The one-word claim is dead. This verdict is conditional on standing values: banked GT 34='i'/29='er'/40='e' plus battery-promoted (pending red-team ratification) 12='n' and 94='ne'. If the red team overturns either promotion, this kill re-opens. No standing red-team verdict is contradicted.

## Residual (C4 conversion)

R-enne-61: the @61-65 'enne'-shaped window ('34 29 40 12 94', row a1_01) becomes a word-level residual. Stated cause: the forced letter string "ierenne" admits no French word (family sweep §Lexicon check); the analytic letter readings of the five pairs still hold individually (34='i', 29='er', 40='e' GT; 12='n', 94='ne' promoted) — only their one-word composition fails. The residual is about word segmentation, not about 94's value: ne-94 and n-e-12-48 are not downgraded.

## Follow-up battery targets for the supervisor (null-style regeneration)

### F1 id "seg-08-ier-61" — priority 2
- claim: "@60-67 re-segments grammatically once 08 resolves: either '08 34 29' = 'hier' (08='h' spelling-letter) + '40 12' = 'en' + '94' = 'ne' (negation, promoted value) + 92, or '08 34 29 40' forms one word ('fière'/'bière'/'pierre'-tail if 08 in {f,b,p}) with '12 94' = 'n'+'ne'."
- bars: "resolve iff ONE segmentation parses @60-67 grammatically with <=1 non-granted value assumption (08's value); else fence the window as multi-residual."
- evidence: "@60-67 '08 34 29 40 12 94 92 69' (a1_01); one-word 'ierenne' KILLED by this battery; 08 open; 94='ne' negation is the promoted value."
- adverses: "'en ne' order obstacle at @64-65 under the 'hier' arm; 08's value unknown — gated on queued stem-08, do not force."

### F2 id "class-92" — priority 2
- claim: "92's class is named from its 22-window profile."
- bars: "name 92's class iff >=3 windows parse under it with zero forced contradiction; result feeds C3-proper and queued prenne-70-12-94's subject search (92 follows @1548)."
- evidence: "92 n=22; predecessors 00x6/11x3/94x2/84x2; followers scattered (max 2x: 79/69/60/64/62); '94 92' x2 closed set (@65-66, @1549-1550)."
- adverses: "follower scatter gives no dominant signal; 92's killed '-ère' value is NOT re-litigated (class claim is distinct)."

### F3 id "enne-family-12-94" — priority 3
- claim: "The '12 94' letter-pairing is word-internal ('nne') at both 'prenne' windows and word-resistant only at @64-65."
- bars: "confirm iff @348-349 and @1548-1549 both parse with 12='n'+94='ne' as letters inside one word AND @64-65 stays the sole word-resistant '12 94' (already shown); else re-open the letter reading."
- evidence: "'12 94' x3: @64-65 (this battery's residual), @348-349 ('70 12 94'), @1548-1549 ('70 12 94'); 12 n=23, followers 48x5/94x3/16x3."
- adverses: "conditional on 12='n' + 94='ne' promotions (pending ratification); a red-team overturn re-opens this battery's kill too."

## Standing constraints observed

Did not touch R5005, sealed gate instances, or the red-team adjudication queue. Nothing promoted by this battery (verdict is kill). No invented numbers: every offset verified on the repaired 1,847-pair stream.
