# Battery report: frame-20-62-94

Worker: 5882f2b3-a91d-4038-ba64-a5e11f0b1084. Date: 2026-10-08.
Target: `frame-20-62-94`. Priority 3.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005 never touched. All counts re-derived below;
no prior counts trusted.

## Claim (verbatim)

"20 62 94" frame; 62 as {48,94}-selector

## Bar (verbatim, pre-registered)

"resolve iff 62's class named + 20's noun-leg frames parse"

Numbered clauses:

1. 62's class is named (a single class, with byte-level evidence, covering
   62's distribution — not just the 62-94 subset).
2. 20's noun-leg frames parse (the three '20 62 94' windows share a
   grammatical parse in which 20 occupies a noun leg).

## Method

Fresh parse of the repaired stream. Census: 62 (n=35), 94 (n=37), 48 (n=38),
20 (n=15). Enumerated every 62 window (35/35), every 20 window (15/15),
follower/predecessor distributions for 62/94/48, and the three trigram
windows at 0-indexed pair offsets @760, @839, @1703 (match the brief's
@760/@839/@1703). Tested candidate classes for 62 (subject pronoun 'il',
verb, 'qu'il'-fused, stem) against ALL 35 windows, not only 62-94 frames.
Checked standing verdicts first: collision-62-84 (processed) KILLED 62='on'
unconditioned and DEMONSTRATED 62='il' on the nine 62-94 frames (not
promoted); lon-62-on-conditioned NULL; lon-94-64-rightedge NULL ('ne qui'
@509-510 genuine residual); 94='ne' is promotion-track, not granted;
20='fois' kill holds (§7).

## Window-level evidence (@-offsets, repaired stream)

Trigram '20 62 94' x3 (re-derived):
- @760 (a5_03): "82 34 29 40 20 62 94 59 39" = "m i er e [20] [62] [94]
  est?[59] [39]" → "la premiere [20] [62] [94] est [39]"
  (82 34 29 40 = "miere"; 70 precedes at @759 = "pre", so "la premiere").
- @839 (a5_06): "35 56 17 98 20 62 94 26 12" = "[35] [56] fois[17]
  vient?[98] [20] [62] [94] [26] n[12]".
- @1703 (a8_06): "85 33 94 30 20 62 94 88 26" = "[85] [33] ne?[94]
  pas[30] [20] [62] [94] [88] [26]".

'20 62' x4 (re-derived): @760, @839, @1135, @1703. @1135 (a6_08):
"86 24 77 86 20 62 98 00 98" = "[86] VERB?[24] le?[77] [86] [20] [62]
vient?[98] pour[00] vient?[98]" — 20-62 selects 98, NOT in {48,94}.

62 follower census (n=35): 94 x9, 48 x6, 98 x5, 16 x4, 06 x2, 61 x2,
96 x1, 91 x1, 21 x1, 18 x1, 38 x1, 46 x1, 93 x1.
62 predecessor census: 21 x5, 20 x4, 74 x3, 93 x2, 03 x2, 08 x2, 78 x2,
92 x2, 30 x1, 51 x1.
62 is top predecessor of 94 (9/37) and of 48 (6/38) — the selector
distribution is confirmed; what it selects FOR is not.

94='ne' particle legs (supporting): 94->59 x3 ("n'est": @760-window,
@100 "21 62 94 93 59", one more); 94->24 x2 (finite verb); 94->82 x4
("ne m" + verb, 82='m' banked).
94='ne' particle counter-legs: 12-94 x3 = word-internal "n"+"ne":
@348 "70 12 94" = "pre"+"n"+"ne" = "prenne" (takes); @64 "34 29 40 12 94"
= "iere"+"nne"; @1548 "46 70 12 94" = "que prenne". 94 is usable as a
syllable, not only as the particle. @508 "62 94 64" = "[62] ne qui[64]"
ungrammatical under 94='ne' (lon-94-64-rightedge NULL stands).
@1362/@1686 "62 94 79" = "[62] ne tout[79]" — "ne" + adverb "tout" with
no verb in frame; ungrammatical as a 'ne'-negation frame.

62='il' rival tested on all 35 windows (collision-62-84 covered only the
nine 62-94 frames). Un-mergeable windows under 62='il':
- @46 (a1_01): "43 81 30 62 96 00 92" = "[43] [81] pas[30] il par[96]
  pour[00] [92]" → "pas il par" ungrammatical.
- @665 (a4_02): "50 80 03 62 06 00 20" = "[03] il ent[06] pour[00] [20]"
  → "il ent pour" ungrammatical.
- @1315 (a7_04): "00 36 74 62 48 98 15" = "pour[00] [36] [74] il e[48]
  vient[98]" → "il e vient" ungrammatical.
- @1349 (a7_05): "66 73 34 62 48 77 78" = "[73] i[34] il e[48] le?[77]"
  → "il e le" ungrammatical.
- @1482 (a7_10): "16 98 62 46 77 84" = "[16] vient[98] il que[46]
  le?[77] on[84]" → "il que le" ungrammatical.
- @1536 (a8_00): "66 73 41 62 06 21 62" = "[41] il ent[06] NOUN?[21]"
  → "il ent [21]" ungrammatical.
- @1569 (a8_01): "29 24 74 62 48 56 32" = "er[29] VERB?[24] [74] il
  e[48] [56]" → "il e [56]" ungrammatical.
Clean under 'il' (subject + verb/particle): @11, @802, @945 ("il vient
par[96]" ✓), @1136 ("[20] il vient pour[00]"), @1324, @1772 ("il ne
VERB?[24] ce[87]" ✓), plus the nine 62-94 frames per collision-62-84
(with @508 fenced). Remainder (16/18/38/61/91/93 followers) unparsed,
not ungrammatical — unknown values, no verdict forced.

20 census (n=15): @280, @307, @490, @642, @668, @703, @741, @760, @839,
@873, @958, @1135, @1224, @1270, @1703. Determiner/adjective leg @307
(a2_04): "89 88 02 88 20 17 46 84 24" = "[89] [88] [02] [88] [20]
fois[17] que[46] on[84] VERB?[24]" → "[20] fois que" — 20 precedes
17='fois' in determiner/adjective slot. Untouched by this battery;
paradox stands (see Adverses).

## Per-clause pass/fail

1. 62's class named — FAIL. The best rival, 62='il' (demonstrated, not
   promoted, by collision-62-84 on the nine 62-94 frames), is
   ungrammatical in at least seven non-94 windows (@46, @665, @1315,
   @1349, @1482, @1536, @1569). No alternative single class covers all
   35 windows at battery grade (verb fails on 94='ne'/48='e' followers;
   'qu'il'-fused fails @839/@1703; stem-with-{48,94}-spellings names no
   stem). The {48,94}-selector distribution is real (94 x9 + 48 x6 =
   43% of 62's followers; 62 top predecessor of both), but a selector
   needs a value to select FOR, and none survives the full census.
   Naming 'il' would also contradict nothing standing (collision
   demonstrated it) but would overclaim: the class is not established
   beyond the 62-94 subset.
2. 20's noun-leg frames parse — FAIL. The three trigram windows share
   no single noun-leg parse:
   - @760 parses as "la premiere [20] il n'est [39]" only with an
     implied clause boundary after 20 ("la première [NOUN]. Il n'est…");
     20's feminine-noun value is unnamed (20='fois' kill holds) and no
     boundary is in evidence.
   - @839 "vient[98] [20] il ne [26]" likewise needs a boundary after
     20; 20 sits post-verbally, not in the "la premiere __" noun slot.
   - @1703 "ne?[94] pas[30] [20] il ne [88]" — "ne pas" selects an
     infinitive, not a noun; the noun leg is actively fought here, and
     20 would need a THIRD leg (infinitive) or a re-parse of 33-94.
   "Parses" at the level of "[20] il ne …" (collision-62-84) leaves 20's
   noun-leg claim exactly where it started.

## Adverses

- "20's determiner/adjective leg (@307) unresolved — paradox stands":
  NOT ANSWERED. This battery did not test @307; the paradox (20 before
  17='fois' at @307 vs 20 after 'la premiere' at @760) is untouched and
  stands as stated.
- collision-62-84 KILL (62='on' unconditioned): honored, not
  re-litigated. Nothing here proposes 'on' for 62.
- lon-94-64-rightedge NULL ('ne qui' residual): honored; the 94='ne'
  promotion-track is not re-litigated, only its load-bearing role in
  the selector claim is noted.
- §7 sole-polyvalence law: honored; no second polyvalence declared or
  implied.

## Verdict

**NULL.** Neither bar clause passes at battery grade: 62's class cannot
be named from the full 35-window census ('il' fails seven non-94
windows; no rival covers all 35), and the three '20 62 94' windows
share no uniform noun-leg parse (@1703's "pas 20" selects infinitive,
not noun; @760/@839 need unestablished clause boundaries). The listed
adverse stands unanswered. No standing verdict is contradicted or
downgraded; no red-team docket item touched.

## Null follow-ups (per §4 — work regenerates, never ends)

1. `class-62-fullcensus` — Name 62's class from the FULL 35-window
   census, not the 62-94 subset. Bar: one class (or red-team-approved
   conditioned split) parsing all 35 windows; the 'il' rival must
   survive @46 ("pas il par"), @1482 ("il que le"), @1315/@1349/@1569
   ("il e …"), @665/@1536 ("il ent …") or fence each with stated cause.
   Priority 2.
2. `noun-20-value` — Name 20's noun-leg value. Bar: a feminine noun
   value for 20 parsing @760 ("la premiere [20] il n'est"), @839
   ("vient [20] il ne"), @1703 ("pas [20] il ne") AND surviving the
   @307 determiner-leg adverse ("88 20 fois que") — or show the paradox
   resolves via conditioned polyvalence (red-team act, not battery).
   Priority 2.
3. `sel-62-48-94` — Test the selector claim directly: is there a 62
   value under which 62-48 and 62-94 are one morpheme with spelling
   variants (48='e' vs 94='ne')? Bar: produce the value and parse three
   62-48 windows (@360, @1349, @1569) plus three 62-94 windows (@100,
   @1329, @1772) under it; kill-grade if the 12-94="prenne"
   word-internal use (@348) forces 94 syllabic and breaks the
   particle-only selector. Priority 3.
