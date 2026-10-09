# Battery report: disc-01-24-ci-X

- Target id: `disc-01-24-ci-X`
- Claim: "01-24 x3 decides between 01='ci' and a non-ci 01"
- Date: 2026-10-08
- Worker: agent f109fa89-7239-4225-8772-015695d1ac39
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
  All @-offsets are 0-based repaired-stream indices. n(24)=52, n(01)=28.
  Never used canonical.py. R5005 not touched.
- Lock: code/crowd17/next-token/locks/disc-01-24-ci-X.lock (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"resolve iff (a) 24 is named with all three 01-24 windows parsing
(41-01-24-88 @40, m-01-24-ce-la @828, ce-01-24-89 @984); (b) the named 24
coheres with its full contact profile (24-ce x10, ne-24-ce x2, on-24-37 x2,
la-24 x4, 24-24 @806); (c) the verdict states the consequence for
ci-01-value explicitly"

Numbered pass/fail clauses (restated before testing, not modified after):

1. 24 is named (a value, not only a class) and each of the three 01-24
   windows (@40, @828, @984) parses grammatically under the named 24.
2. The named 24 coheres with its full contact profile: 24->87 x10,
   94-24-87 x2, 84-24-37 x2, 11-24 x4, 24-24 @806. Coheres = every item
   either parses directly under the named value or is fenced with a
   stated cause that does not depend on 24's value.
3. The verdict states the consequence for ci-01-value explicitly:
   what happens to general 01='ci', to 01='faisant', and to the fenced
   bound-"-ci" (ceci) hypothesis.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs). Confirmed the
   three 01-24 windows at @40, @828, @984 and only there.
2. Re-derived 24's full contact profile: 24->87 x10 (@73, @162, @179,
   @190, @643, @823, @829, @1486, @1766, @1774); 94-24-87 x2 (@162,
   @1774); 84-24-37 x2 (@311, @474); 11-24 x4 (@165, @732, @783, @1657);
   24-24 @806. n(24)=52 confirmed.
3. Adopted ne-24-profile's class grant (24 = finite verb; battery-level,
   UNRATIFIED by red team) as the starting point, per the brief.
   Tested candidate values against the three windows first (W2 @828 is
   the hardest: the brief's adverse "m-01-24 @828 resists most 24 values").
4. Swept all 52 windows of 24 under the surviving candidate for
   kill-grade counter-evidence. Killed rival values on the same frames.
5. Checked standing constraints (BATTERY-PROTOCOL.md section 7): no
   granted value collides with the naming; 84="fait" (noun) was killed
   and superseded by 84="on", so 24="faire" (verb lexeme) is free.

## The naming

**24 = "faire" (verb lexeme; forms "faire"/"fait"). 01 = "en" (local to
the three 01-24 windows; not a global 01 value).**

How the decision was reached (narrowing chain):

- W2 @828 `38 82 01 24 87 11` forces a ditransitive verb: 82="m" is the
  letter 'm' (banked GT); before vowel-initial 01 it is elided "m'"
  ("me"); 01="en" is vowel-initial, so "m'en" = "me"+"en" (elision is
  invisible in the cipher, per the f-qui-par residual note). "[38] m'en
  [24]" = "[38] makes (of it) for me" needs a verb taking both "me"
  (benefactive) and "en" (partitive). Only ditransitives qualify:
  {faire, donner, dire, rendre, laisser, ...}.
- The 10 infinitive-complement windows (24->85 x5, 24->89 x3, 24->80 x2)
  force an infinitive-taking verb. Of the ditransitives only the
  causatives "faire" and "laisser" take bare infinitives.
- W1 @40 `[91] 39 64 41 01 24 88` = "[91] a(39) qui(64) [41] en(01)
  [24] [88]": "qui" is the object of "a" ("a qui" = "to whom"), so 41
  is the SUBJECT of the relative clause, not a clitic. "a qui [41]
  en [24] [88]" needs "s'en [24]" or "[41-subject] en [24]" with a verb
  taking "en". "s'en laisser" is ungrammatical; "s'en faire" ("to worry
  / to make of it") is grammatical. "laisser" is killed at W1.
- "faire" is the unique survivor. Rival kills, each on the same frames:
  "dire" killed by the 10 infinitive windows ("dit [inf]"
  ungrammatical) and by @1492 ("a dit pour" ungrammatical vs "a fait
  pour"); "pouvoir"/"devoir"/"savoir" killed at W1 ("en"+pouvoir/devoir/
  savoir ungrammatical) and @1492 ("a pu/su/du pour" ungrammatical);
  "vouloir" killed at W1 and collides with 67="veut" (sole-polyvalence
  rule, section 7); "voir"/"entendre"/"aimer"-class killed at W2
  (ditransitive "me les" impossible); "aller" killed by la-24 x3
  ("la va" ungrammatical), @1492 ("a va pour"), @1497 ("est va"),
  W3 ("en va").

## Window-level evidence

### The three 01-24 windows (bar clause a)

W1 @40 (row a1_01): `91 39 64 [41] 01 [24] 88 43 81 30 62`
= "[91] a(39) qui(64) [41] en(01) fait(24) [88] [43] [81] pas(30) [62]".
Parse: "[91] a qui [41-subject] en fait [88] [43] [81] pas" =
"[91], to whom [41] makes [88] [43] [81] of it not" ("en fait [88]"
= "makes [88] of it", cf. "il en fait un drame"; "pas" with ne-drop,
the author's norm per ne-24-profile). PARSES. Load-bearing
assumptions, both stated: 41 is subject-capable (nominal; its exact
value stays open); [88]'s role after "en fait" is unfixed. 41="se" and
41="ne" are both unnecessary here and both fail globally ("fait se"
@1016 kills "se"; "fait ne" @1016 kills "ne"), so neither is proposed.

W2 @828 (row a5_06): `38 82 [01] [24] 87 11 77 76 59`
= "[38] m(82) en(01) fait(24) cela(87-11) le(77) [76] est(59)".
Parse: "[38-subject] m'en fait. Cela le [76] est." = "[38] makes (of
it) for me. This is [76] to it(?)" ("m'en" = "me"+"en", elision
invisible; clause boundary before "cela", the ne-24-profile account).
PARSES. This is the window the brief said "resists most 24 values":
it resists "pouvoir"/"devoir"/"savoir"/"dire"/"voir" (see rival kills)
and yields to "faire". Load-bearing assumption, stated: 38 is
subject-capable (candidates "il"/"on"/noun; value open; its n=7
profile does not rule this out). Residual, stated: the right edge
"cela le [76] est" is unresolved (76's value open; frame-76-tension
queued owns it) and does not touch the "m'en fait" core.

W3 @984 (row a6_01): `45 [01] [24] 89 48`
= "ce(45) en(01) fait(24) [89] [48]".
Parse: "ce en fait [89]" = "this has [89] made of it" ("en" = object
of the infinitive [89], clitic-climbed to causative "faire", cf. "ca
en fait rever"). PARSES. Rival parse at this window only: "ceci
fait [89]" (45-01 = "ceci", bound "-ci"; see consequence section).
Both are non-general-'ci'. PARSES either way.

### Contact profile (bar clause b)

24->87 x10: @73 "fait cela" (direct object); @162 "ne fait. Cela..."
(lone "ne", author's norm; see @165 below); @179 "fait ce qui"
("does what", cf. "il fait ce qui est necessaire"); @190 "fait ce
[98]" ("does this [98]", 66 nominal fenced as in ne-24-profile);
@643 "fait ce [61]"; @823 "fait. C'est..." (boundary, profile's
account); @829 "fait cela" (W2); @1486 "que l'on fait ce [08]"
("that one does this [08]"); @1766 "fait ce qui"; @1774 "ne fait.
Ce qui est [19]" (profile's clean window). ALL TEN COHERE, most
parsing directly as objects of "faire" (better than the profile's
all-boundary account).

94-24-87 x2 (@162, @1774): "ne fait" + clause boundary, lone-"ne"
per the author's norm (34/37 baseline, ne-24-profile). COHERE.

84-24-37 x2 (@311, @474): "qu'on fait [37]" / "on fait [37]".
"faire" takes infinitives (causative) and nouns; [37]'s fork is owned
by w1-314-ambig. COHERE under both forks (same fence as
ne-24-profile).

11-24 x4: CORRECTION to the count as stated. @165 is not "la"+"fait":
the string @161-168 is `94 24 87 11 24 82 84 53` = "ne fait. Cela
fait mon [53]." The "11" is the tail of granted "cela" (87-11), and
"82-84" is "mon" (possessive m+on), not "me on". This RESOLVES the
tail ne-24-profile fenced ("cela [24] m on"): "Cela fait mon [53]"
= "this makes my [53]". The true "la"+"fait" windows are x3 (@732,
@783, @1657), and all three parse DIRECTLY as object pronoun + "faire"
(no fencing needed, unlike under "pouvoir"):
- @732 `88 11 [24] 85`: "[88] la fait [85-stem]" = "[88] has it
  [85]-ed" (causative). CLEAN.
- @1657 `37 11 [24] 48`: "[37] la fait [48]" / "[37]. La fait [48]"
  = "[37] does it [48]". CLEAN ("la fait" core; 37's edge fenced to
  frame-37-reexam).
- @783 `89 11 [24] 42`: "la fait [42]" = "does it [42]" CLEAN
  locally; left edge "[89]" fenced (clause boundary likely; [89]'s
  class is verb-frame per conditional A8).

24-24 @806: `69 [24] [24] 41` = "fait fait", doubled. Fenced as
formula/list exactly like ne-24-profile (cf. 62-94 x9, doubled 06).

Further "faire"-confirming windows (lexeme across its forms):
- @1492 `92 39 [24] 00 66`: "[92] a(39) fait(24) pour(00) [66]" =
  "[92] has done for [66]". "a"+"fait" = compound past of "faire";
  39 is preposition "a" here ("a faire" also parses: "to do"), so
  a-39's "zero verb-'a'" record is untouched. "faire pour" kills
  "dire"/"savoir"/"pouvoir"/"devoir" ("a dit/su/pu/du pour" all
  ungrammatical). STRONG discriminator for "faire".
- @1497 `15 59 [24] 89`: "[15] est(59) fait(24) [89]" = "[15] is
  made [89]" (passive of "faire"; load-bearing on provisional
  59="est", flagged). "est"+"fait"(participle) forces the participle
  reading; consistent with one lexeme, inflectional (no new
  polyvalence declared).
- @654/@991 `49 [24] 26 30` x2: "ne [76] [49] fait [26] pas" (@654,
  with "ne" @653) / "[76] [49] fait [26] pas" (@991, ne-drop) =
  "[76] doesn't have [26] done for [49]" (causative + "ne...pas").
  RESOLVES the pair ne-24-profile fenced to noun-26, and votes the
  verb arm for noun-26 ([26] = infinitive complement of causative
  "faire").
- 24->85 x5 / 24->89 x3 / 24->80 x2: "fait [inf]" causative, x10.
  CLEAN.
- 24->30 x3 (@29 fenced word-internal per profile; @1268, @1728):
  "fait pas" with ne-drop, author's norm. CLEAN.

Fenced residuals (stated cause, none ignored):
- 24->82-16 x3 (@535, @1193, @1830; CORRECTION: ne-24-profile said
  x2): "fait me [16]" is ungrammatical, so under "faire" the
  "peut me [dire]"-shaped reading dies and 82-16 re-segments as one
  word ("m[16]"-word, object/subject of "faire": "[08] fait [m16]",
  "[07] fait [m16]", "[83] fait [m16]"). 16's value is open and owned
  by frame-82-16; this battery does not decide it. Consequence: the
  profile's "modal-shaped" leg is hypothesis-dependent and is
  weakened, not removed (flagged for frame-82-16).
- "que 24" x3 (@547, @955, @1693): finite-verb slots (profile's
  finding stands); subjects/"que"-roles unidentified. @955 sits in
  the granted "parce que" frame (96-87-46, A3). Same fence as
  ne-24-profile; not worse under "faire".
- @1083 "[89] fait [02]": "fait [02]" = imperative "do [02]"
  (no subject needed) with clause boundary after "[89]". Clean
  rescue; no re-litigation of A8.
- @1132 "[86] fait le [86]": "fait le [86]" parses iff 86 is nominal
  here, which tensions the A9 INF-class grant (class-level); or
  ellipsis. Fenced for red team / stem-86. One window, rescues exist.
- @1220 "[61] fait [48] pas": "[61] fait [48]" clean locally;
  "[48] pas" right edge fenced. @1522 "[31] fait la. La [48]...":
  "fait la" clean; "la la" right edge fenced. @1567 "[50-er] fait
  [74]": 29-24 word-boundary fence (same family as @29).
- @190 "pour [66] fait ce [98]": "[66]" nominal subject, 66's class
  open (profile's fence, unchanged). @1015 "ce [03] fait [41]":
  "[03]" nominal subject, 03's class open (stem-03 owns it).

No window forces 24="faire" false. Nothing in the profile requires a
modal reading once 82-16 re-segments.

## Per-clause pass/fail

1. 24 named with all three 01-24 windows parsing: PASS. 24="faire"
   (lexeme; "fait" 3sg in the windows). W1 "a qui [41] en fait [88]"
   parses; W2 "[38] m'en fait. Cela..." parses (the hard window,
   which kills "pouvoir"/"devoir"/"savoir"/"dire"/"voir"-class and
   "laisser"); W3 "ce en fait [89]" parses ("ceci fait [89]" also
   parses). 01="en" is the non-'ci' 01 at all three windows.
2. Named 24 coheres with the full contact profile: PASS. 24->87 x10
   (direct objects: "cela", "ce qui", "ce [98]/[61]/[08]", "c'est"-edge),
   ne-24-ce x2, on-24-37 x2, la-24 (x3 "la fait" direct + @165
   re-segmented "cela fait mon [53]"), 24-24 @806 (formula fence).
   Two corrections to ne-24-profile recorded (82-16 x3 not x2;
   @162/@165 tail resolved); the "modal-shaped" leg is weakened via
   the 82-16 re-segmentation (flagged, not deleted).
3. Consequence for ci-01-value stated explicitly: PASS (see below).

Adverses, answered:
- "24-ce x10 kills ci-dessus/ci-joint/ci-inclus": ANSWERED. 24="faire"
  is a finite verb; every ci-compound (ci-dessus, ci-joint, ci-inclus,
  ci-apres, ci-contre) is dead at 01-24, consistent with ci-01-value.
- "m-01-24 @828 resists most 24 values": ANSWERED. It resists
  "pouvoir"/"devoir"/"savoir"/"dire"/"voir"-class/"laisser"/"aller"
  (each killed on this frame or the profile) and parses as
  "[38] m'en fait" under 24="faire" + 01="en".
- "24's class is open (ne-24-profile PROMOTED 24's class,
  unratified)": BUILT ON. The class grant (finite verb) is adopted;
  the value "faire" is named at battery level, UNRATIFIED, needing
  red-team ratification like every battery promote. Dependency: if
  ne-24-profile's class grant is ever overturned, this verdict
  re-opens (same dependency ci-01-value carries).

## Verdict: PROMOTE (battery-level, unratified)

24="faire" (verb lexeme; forms "faire"/"fait" seen: finite "fait",
infinitive "faire", participle "fait"). 01="en" LOCAL to the three
01-24 windows. The discriminator decided: non-'ci' 01.

### Consequence for ci-01-value (explicit)

1. General 01="ci" stays KILLED, now mechanically explained:
   24="faire" is a finite verb; "ci" never precedes a finite verb
   (@40, @828) and no ci-compound can host a verb (@984).
2. General 01="faisant" stays KILLED: participle + finite "fait"
   with no subject is ungrammatical at all three windows.
3. The 01-24 x3 "leftover" is decided: all three windows parse fully
   under 01="en" + 24="faire". 'ci' is not needed anywhere in them.
4. Bound "-ci" in ceci compositions is UNTOUCHED: 87-01 x2 (@345,
   @1029) and 47-01 (@195) still read "ceci"; 45-01 @984 admits both
   "ce en fait" and "ceci fait". Ownership stays with ci-bound-01 and
   feeder-ceci-47-45 (both queued).
5. Scope limit: 01="en" is LOCAL to the three 01-24 windows, not a
   global 01 value. The ceci frames need bound "-ci", so a global
   01="en" fails there; unifying "en"/"-ci" would be a second
   polyvalence and is a RED-TEAM-ONLY question (section 7: 67 et/veut
   is the sole true polyvalence). Not declared here.
6. Cross-target notes (not decided here): @654/@991 vote the verb arm
   for noun-26 ([26] = infinitive under causative "faire"); the
   82-16 x11 cluster re-segments as "[m16]"-word under "faire"
   (flagged for frame-82-16); @1492/@1497 confirm the "faire" lexeme
   via "a fait"/"est fait" (the latter load-bearing on provisional
   59="est").

No standing red-team verdict is contradicted. A12 (37-01 unit) is
untouched. The le1033 "ceci" adverse-answer is preserved via the
bound-"-ci" fence. 37's value question stays with the red team.
