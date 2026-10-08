# Battery report: lever-77-78

Target: `lever-77-78`
Claim: "'77 78' reads 'lever' (infinitive; '48 77 78' = 'elever') in all 7 windows, not article 'le' + stem 'ver'"
Date: 2026-10-08
Worker: 9df8d9a4-9a73-423f-a526-39e791ec9470
Lock note: no stale lock existed (locks/ empty at start); created locks/lever-77-78.lock 2026-10-08T14:58:35Z, deleted on completion.

## Bar (verbatim from battery-queue.json)

"(1) all 7 windows parse with 'lever'/'elever' + complement-shaped follower (18, 06, 52, 64, 94, 43); (2) F5's 'lever ne m'' x2 (@1180, @1351) resolves via a stated clause boundary or the conditioned-94 'en' reading; (3) @1077 'ne lever qui' resolves via a stated boundary or 12-48 re-parse; (4) '77 78' adjacency holds 7/7 (control: the bigram never splits)"

## Numbered clauses (fixed before testing)

1. All 7 windows (@7, @213, @647, @1077, @1180, @1351, @1542) parse with
   77-78 = "lever" (or 48-77-78 = "elever") followed by a complement-shaped
   follower (18, 06, 52, 64, 94, 43 respectively).
2. @1180 and @1351 ("lever ne m'" x2) resolve via a stated clause boundary
   or via the conditioned-94 "en" reading (F25: 94="en" iff pre=82 or suc=87).
3. @1077 ("ne lever qui") resolves via a stated clause boundary or via the
   12-48 letter re-parse ("n"+"e").
4. "77 78" adjacency holds at all 7 windows; control: the bigram never splits
   stream-wide.

Scope (per work order): the 77-78 COMPOSITION only. 77="le" stays provisional
per the le-77 NULL; 78="ver" stays open per the ver-78 NULL. The le-77 NULL's
F2 "le [78]" article frame is the standing analytic alternative — tested
against, not re-litigated. Complementary to queued ver-78 and the ne-le-1075
kill (battery-level); coordinated, not duplicated.

## Method

Repaired 1,847-pair stream only: code/side-keyhunt/repaired_offsets.json over
data/upstream-ct_R5005.txt, parsed exactly like
code/side-keyhunt/repair_parse.py (byte-exact
`[s[i:i+2] for i in range(o, len(s)-1, 2)]`). code/side-keyhunt/canonical.py
never used. R5005 untouched. @-offsets are 0-based repaired-stream pair
indices. All 7 "77 78" bigrams re-derived from the stream: exactly 7,
at @7, @213, @647, @1077, @1180, @1351, @1542 (matches the queue evidence).
Standing values used: banked GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que; promoted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on,
47=ce; provisional 59=est, 77=le; battery-promoted pending ratification
94=ne (ne-94), 12=n + 48=e letter (n-e-12-48); granted frames 37/32/42
predicative (value open), 80/89 verb-frames, 85 verb-stem. F25 conditioned
polyvalence (94="en" iff pre=82 or suc=87) cited from
report_inbox/processed/crowd4-morphologist-94-re.md (red-team: 94="en"
co-value DENIED, LEAD-held). F52-L2 (06 verb-stem-class, non-nominal) and the
ISLET-10 "V-este" analysis cited from code/crowd10/conditioner59
(classification.json @216: "cleft 'NP est que' hostile (06 non-nominal)").

## Window-level evidence

### @7 (a1_00): `00 97 51 |47 41 06| [77 78] 18 93 62 98 76 45 91`
Parse: "[06-verb-stem] lever [18]" — finite verb 06 governs infinitive
"lever"; 18 as object. 18 n=7, class fully open (predecessors all x1:
78/91/19/76/88/35; followers all x1) — complement assumed, nothing hostile.
Left tail "00 97 51 47 41 06" fenced to open values (97/51/41). No hard
contradiction. SOFT PASS (fenced: 18-as-complement is assumption-only).

### @213 (a2_00->a2_01): `77 44 50 88 19 |74| [77 78] 06 59 46 29 42 16 24`
Candidate: "[74-verb] lever [06-complement]". PROBLEM: 06 is verb-stem-class,
non-nominal per F52-L2 — the lane classifier marks the "NP est que" cleft
hostile at exactly @216 for this reason, and the ISLET-10 analysis reads
06-59 here as the "V-este" verb unit ("[06-59] que" verb+que-clause). No
clean "lever + complement(06)" parse exists under standing lane law:
06-as-object is hostile (non-nominal); boundary after "lever" leaves "lever"
absolute (ungrammatical); 06-59-as-verb-unit leaves "lever" absolute too.
The strain is SHARED with the F2 rival ("le ver 06" has the identical 06
problem) — it does not discriminate lever-vs-F2 and does not force the
composition false. 59@216: pre=06 not in {64,94,93}, so the ISLET-10 license
does not put 59 in the est-arm here; 59 fenced open. SOFT FAIL of clause 1
at this window (fenced to the open 06 value; queued ent-06 / 06-polyvalence
work owns it).

### @647 (a4_01->a4_02): `48 20 24 87 61 |88| [77 78] 52 82 94 76 49 24 26`
Parse: "[88] lever [52-nominal]" — 88 precedes 77 x3 stream-wide
(@86, @646, @1541: consistent governor contact); 52 nominal via "la 52" x3
(11="la" banked). Local frame parses. Tail "52 82 94 76": with 94="ne"
(promoted) the order reads "[52] m' ne" — the acknowledged "m"+"ne"
inversion strain (adverse, fenced: strain localizes to the 82-94-76 tail,
76 value open / noun-76 battery's claim not re-litigated); with F25 94="en"
(condition SATISFIED here: pre(94@651)=82) the tail reads "[52] m'en [76]"
but "en"+nominal-76 does not integrate — fenced. SOFT PASS (tail fenced).

### @1077 (a6_05): `74 42 98 98 |12 48| [77 78] 64 06 52 89 24 02 55`
12-48 re-parse (clause 3 route): 12="n" + 48="e" as LETTERS (both
battery-promoted pending ratification, n-e-12-48) gives "n'"+"e"+"lever" =
"n'elever" ("not to raise"); 64="qui" (promoted) as object pronoun ("whom"):
"n'elever qui" parses as an infinitive clause. Verified from the stream:
12-48-77 is unique stream-wide (x1 @1075); no 94 within distance 3 of 77 at
this locus (the only stream-wide 94/77 d3 co-occurrences are @507-509,
@1180-1182, @1351-1353) — the "ne" here comes from the 12-48 letter
reading, never from 94, exactly as the ne-le-1075 battery directed. Fences:
bare "ne" (ne-alone-02-74 doctrine, queued not granted); doubled "98 98"
(98 value open); tail boundary after "qui" ("Qui [06-verb] [52]…" new
clause). SOFT PASS.

### @1180 (a6_10): `36 74 32 48 59 |37| [77 78] 94 82 06 06 59 42 06`
Conditioned-94 "en" route: UNAVAILABLE — F25 requires pre=82 or suc=87;
at @1182 pre=78, suc=82. FAILS. (Consistent with the red-team's denial of
the 94="en" co-value.)
Boundary route (stated): "[37-predicative] lever | Ne me [06-verb]…"
= "…[37] lever. Ne me [06] [06] [59] [42] [06]…" — "ne"+"me"(82=m banked)+
verb in correct French order; bare "ne" per 1840s ne-alone licensing.
Fences: 37-as-governor (predicative frame granted, value open;
predicative+infinitive soft); bare-"ne" (doctrine queued); 06@1184-as-verb
(verb-stem class) vs the crowd4 trigram-internal-"ent" conditioning
(06 inside 94-82-06 @1182-1184 — FLAGGED as an open conflict, owned by
queued ent-06 work, not decided here); tail "06 59 42 06" fenced
(59@1186 open per ISLET-10, pre=06; 42 predicative frame granted value
open). No hard contradiction. SOFT PASS via the boundary route.
Note: the same 5-gram 77-78-94-82-06 is the morphologist's "nement"-host
("…levement", e.g. "soulevement") — UNDEMONSTRATED rival (missing
pre-syllable has no value at 59@1178; bare "levement" is not a French
word); recorded, not a kill (see FU3).

### @1351 (a7_05->a7_06): `86 66 73 34 |62| 48 [77 78] 94 82 06 52 37 64 35`
Conditioned-94 "en": UNAVAILABLE (pre=78, suc=82 — same F25 failure).
Boundary route (stated): "[62] elever | Ne me [06-verb] [52]…"
= "…[62] elever. Ne me [06] [52-obj]…" — 48="e" (promoted) + "lever" =
"elever"; "ne me [verb] [object]" correct order; 52 nominal ("la 52" x3).
Fences: 62-as-governor (value open; 62="il" demonstrated-not-promoted
leans hostile — "il elever" — fenced explicitly); bare-"ne"; 06@1355-as-verb
vs trigram-internal-"ent" (flagged, same as @1180); tail "[37] [64=qui]
[35]" fenced (boundary after 52; 35 open). SOFT PASS via boundary.

### @1542 (a8_00): `62 93 |88| [77 78] 43 00 46 70 12 94 92`
Parse: "[88-verb] lever [43-obj] pour que prenne [92]"
= "…lever [43] [00=pour] [46=que] [70=pre][12=n][94=ne]=prenne [92]".
43 nominal: "par 43" x2 (96="par" promoted), "43 pour" x3 (@244, @1126,
@1544). "pour que prenne" is the battery-validated prenne composition
(prenne-70-12-94). Purpose clause after an infinitive+object — fully
grammatical. Strongest window. Fences only: 88-as-governor (88-77 x3
supports contact), 43-as-object (well-evidenced). SOFT PASS (firmest leg).

## Per-clause pass/fail

1. "All 7 windows parse with lever/elever + complement-shaped follower":
   FAIL (soft). 6/7 parse (@7, @647, @1077, @1180, @1351, @1542 — with
   stated fences); @213 does not: follower 06 is verb-stem-class /
   non-nominal per F52-L2, and the lane's conditioner reads 06-59 as the
   "V-este" verb unit, leaving no clean "lever + complement(06)" parse.
   The @213 strain is shared with the F2 rival (does not discriminate;
   fenced to the open 06 value).
2. "@1180/@1351 resolve via boundary or conditioned-94 'en'": PASS (soft).
   The "en" route is unavailable (F25 fails at both: pre=78, suc=82);
   both resolve via the stated clause boundary
   ("[37] lever | Ne me [06]…", "[62] elever | Ne me [06] [52]…"),
   with fences stated above (bare-"ne", 06-as-verb vs trigram-"ent"
   flagged, governors/ tails open).
3. "@1077 resolves via boundary or 12-48 re-parse": PASS (soft) via the
   12-48 re-parse ("n'elever qui"; 12-48-77 unique x1; no 94 within d3 at
   this locus). Bare-"ne" and "98 98" fenced.
4. "Adjacency 7/7; control: bigram never splits": PASS WITH CORRECTION.
   All 7 windows are adjacent 77-78 (7/7 holds; the 7 windows ARE the full
   stream census of the bigram). The control gloss is corrected: one
   non-adjacent 77…78 co-occurrence exists stream-wide — "77 86 78"
   @877-879 (a5_08), i.e. 43/44, not "never". It is not a lever window
   (86 intervenes; 86 value open) and does not contradict the composition;
   fenced.

## Adverses answered

- F2 "le [78]" article frame (le-77 NULL) on the same 7 windows: FENCED
  with stated cause — the analytic (article+stem) and synthetic
  (word "lever") readings are alternatives on the same frames; this
  battery tests the composition against F2 without re-deciding it, per
  scope. 77="le" stays provisional under either reading. The ver-78 NULL
  (78="ver" open) and the queued ver-78 target are coordinated, not
  duplicated (ver-78-rebar lists this composition as its named rival).
- @647 "'lever 52 m' ne'" m'+ne order strain: FENCED — localizes to the
  82-94-76 tail (76 open), not to the 77-78 composition; F25 "en" is
  licensed there (pre=82) but "m'en [76-nominal]" does not integrate.
- @1077 "'ne lever' ungrammatical as words": SHOWN MISREAD — it is not
  "ne lever" as words but the analytic 12-48 letter re-parse "n'elever"
  (blessed by the ne-le-1075 battery).
- 77="le" provisional / composition-only scope: RESPECTED throughout; no
  value promoted or killed by this report.
- Complementarity with ver-78 / ne-le-1075: COORDINATED, not duplicated.

## Correction to a cited note (anomaly, not load-bearing)

The ne-le-1075 battery's worker note ("94 never co-occurs with 77 within
distance 3") is true AT THE @1075 LOCUS but false stream-wide: 94 falls
within d3 of 77 at @507-509, @1180-1182, and @1351-1353 (re-derived from
the repaired stream). The locus conclusion ("the 'ne' at @1075 comes from
12-48, never 94") is unaffected.

## Verdict: NULL

Not promote: clause 1 fails (soft) at @213 — no clean "lever +
complement(06)" parse under standing lane law (F52-L2 06 non-nominal;
ISLET-10 "V-este"). Not kill: no window forces the composition false —
the @213 strain sits in the follower (06), is shared with the F2 rival,
and belongs to queued 06-value work; the "…levement"/nement-host rival at
@1180/@1351 is undemonstrated (no pre-syllable value; bare "levement" not
a French word); no cleaner rival value was demonstrated on these frames.
This null does not contradict any standing red-team verdict (R16-005's
78="ver" LEAD grading untouched; 94="en" denial consistent with the F25
failure found here). No existing verdict downgraded.

## Follow-up targets (null regenerates work)

### FU1 id "lever-213-complement" (priority 2)
- claim: "@213 '74 lever 06' resolves the 06-complement problem"
- bars: "(1) ONE grammatical parse of @213-216 with 77-78='lever' and 06
  complement-shaped, OR confirm the 06-59 'V-este' verb-unit forces a
  clause boundary after 'lever' and state whether absolute 'lever' is
  licensable; (2) cite F52-L2 and ISLET-10, do not re-litigate them;
  (3) test 06='/ɑ̃/'-adverbial and a 06-nominal islet as rival
  integrations."
- evidence: "@213-216 '74 77 78 06 59 46' (a2_00); F52-L2 '06 non-nominal';
  ISLET-10 'V-este' @216 (classification.json); 06 polyvalence /ɑ̃/ vs
  /mɑ̃/ (crowd4); 59 open here per ISLET-10 (pre=06 not in {64,94,93})."
- adverses: "strain shared with F2 ('le ver 06' identical problem) —
  non-discriminating; 59's est-arm status is conditioner59's lane, not
  this battery's."

### FU2 id "lever-88-governor" (priority 2)
- claim: "88 governs the 'lever' infinitive at @647/@1542"
- bars: "(1) 88 shows verb-frame contact at >=2 of the 88-77 windows
  (@86, @646, @1541) independent of the 77-78 composition; (2) @1542
  '88 lever 43 pour que prenne 92' re-parses cleanly with 88 as governor
  and 43 nominal; (3) 88's class consistent across @646/@1541."
- evidence: "88-77 x3 (@86, @646, @1541); '43 pour' x3 (@244, @1126,
  @1544); 'par 43' x2 (96='par' promoted); prenne-70-12-94 composition
  @1547-1550 ('pour que prenne 92')."
- adverses: "88 value fully open; @86 '88 77 [non-78]' needs integration;
  does not decide 77-78 by itself (governor evidence only)."

### FU3 id "lever-lement-rival" (priority 3)
- claim: "the '…levement' rival at @1180/@1351 stays undemonstrated"
- bars: "(1) test whether 59@1178 / 62@1349 can host the missing
  pre-syllable of '…levement' (sou-/en-/re-) under any granted,
  provisional, or battery-promoted value; (2) if no host, record the
  77-78-94-82-06 'nement'-host as a count-level observation (morph94),
  not a parse — it does not kill the lever composition; (3) state which
  06 value (trigram-internal-'ent' vs verb-stem) the clause-2 boundary
  parse requires at 06@1184/@1355."
- evidence: "94-82-06 x3 @578/@1182/@1353; morphologist note
  '77-78-94-82-06 ×2 @1179/@1350' nement-host; crowd4 06
  trigram-internal-'ent' conditioning (06@[580,1183,1354] inside
  94-82-06); 62='il' demonstrated-not-promoted."
- adverses: "bare 'levement' is not standard French; the rival needs the
  unattested pre-syllable; red-team denied 94='en' co-value (LEAD-held)."

## Constraints respected

R5005, sealed gates, and the red-team adjudication queue untouched. §7
banked/promoted/provisional/killed/split/held values respected; 67
et/veut sole polyvalence untouched. No promotion recorded beyond this
battery verdict (null). canonical.py never used.
