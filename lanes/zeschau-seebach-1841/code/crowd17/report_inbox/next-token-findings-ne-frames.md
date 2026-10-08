# Next-token findings: ne-frames (94 followers)

Wave-2 finder beat. Restarted clean 2026-10-08 after the prior worker died
with the agent daemon (~2026-10-08 04:26 UTC); no partial report existed.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed like repair_parse.py). Never canonical.py.
R5005 untouched. No data invented.

## Method

Extracted all 37 windows of 94, +/-3 groups, with @-offsets in the repaired
stream. Clustered by follower FIRST. De-duplicated formula windows before
counting productive frames. Predictions use 1840s diplomatic French.
Standing constraints respected: 48="est"/"ne"/"de" kills, the {48,94}
homophone-set kill, 84="on" (A15), banked GT values, and 45="ce" (A11) are
not re-litigated. The 94="ne" letter-battery runs concurrently; this report
verifies frames independently of the forks pre-finder and does not verdict
the battery.

## Pre-finder correction (independent verification)

The forks pre-finder (report_inbox/processed/next-token-findings-forks.md)
reported "n'est x3 (@101, @558, @762)". In the repaired stream @101 is
"62-94-93-59" = "on ne [93] est" -- an INDIRECT frame, not a direct 94->59
hit. The true third direct 94->59 is @1795 ("42-94-59-37"). The x3 count
survives, but with a different third member, and the third member is the
strongest of the three: 42 and 37 are both predicative-frame groups (A1),
so @1795 reads "42 n'est 37" -- a predicative triple. @101 becomes a bonus
4th "ne...est" frame (ranked below as F7). Window inventory (37) matches
the pre-finder exactly, byte for byte.

## Follower clusters (94 -> X, n=37)

82 x4 | 74 x3 | 59 x3 | 52 x3 | 92 x2 | 24 x2 | 76 x2 | 79 x2 |
93, 65, 06, 02, 64, 29, 60, 07, 15, 26, 87, 70, 84, 30, 88, 44 x1 each.
Predecessor top: 62 x9 ("62-94"), 12/42/82 x3 each, 61/65/22/78/35 x2 each.

## Ranked frames (confidence x testability)

F1 "n'est" x3 -- @558 ("86-94-59-30"), @762 ("62-94-59-39", inside
"la premiere [20] on n'est [39]" at @756-764), @1795 ("42-94-59-37").
Three independent predecessors (86, 62, 42). HIGH.
F2 "ne pas [inf]" x2 byte-identical -- @1293 and @1806:
"84 59 35 94 52 80 04". The only byte-identical 7-gram repeat in the 37
windows. De-duplicated to one frame-type. HIGH.
F3 "on ne prend pas" -- @1330: "30 06 62 94 70 52 39 83".
"70 52" occurs nowhere else in the stream (single-instance leg), but
composition is clean with attested "prend"->"pre" cutting. MEDIUM-HIGH.
F4 "i ne m' que" -- @1742: "86 12 34 94 82 46 56". Both neighbors banked
(34=i, 46=que). The cleanest "ne m'" frame. HIGH.
F5 "le ver ne m' 06" x2 -- @1182 ("37 77 78 94 82 06 06") and @1353
("48 77 78 94 82 06 52"). 5-gram "77 78 94 82 06" repeats; tails differ
(06-06 vs 06-52), so two instances, one frame-type. Supports 78="ver"
(forks P2) and 94="ne" jointly. MEDIUM-HIGH.
F6 formula "61 ne m' 06 06" -- @578: "13 55 61 94 82 06 06". The
"94-82-06-06" formula; doubled 06 resists "ne m'en en". Feeds the
frame-94-82-06-06 battery (06's value decides). MEDIUM.
F7 "on ne 93 est" -- @101: "08 21 62 94 93 59 45" (pre-finder's misread
third n'est, re-classed). Discriminating frame: predicts 93 is verb-shaped
(93 takes 29="er" once, followed by 59 once; n=14, profile inconclusive).
MEDIUM.
F8 "ne 24 ce" x2 -- @161 ("52-94-24-87") and @1773 ("62-94-24-87").
Frame-type x2 with different predecessors. 24's profile: 52 occurrences,
top follower 87="ce" x10. Unresolved; predicts 24 verb/preposition-shaped.
MEDIUM-LOW.
F9 "62-94-79-14-60" x2 -- @1363 and @1687 (near-identical: "13 92" vs
"13 93" prefix). One frame-type, two instances. If 79="tout": "on ne tout
[14][60]" -- unparsed. New unresolved frame-type. MEDIUM-LOW.
F10 conditioned "en" islets x4 -- @651 and @1576 ("52-82-94-76", 5-gram
repeat, "m'en 76"), @1102 ("82-94-74-47", "m'en 74 ce"), @1169
("61-94-87-83", "61 en ce 83"). All four have pre=82 or suc=87; ZERO
94->82 frames have pre=82 (all four have pre=61/78/78/34) and zero
"en"-compatible frames exist outside the conditioning. This re-derives the
morphologist's conditioned "ne"/"en" split independently from frame
extraction alone: the two families are disjoint in my inventory. HIGH as
confirmation; not a contradiction of 94="ne".

## Nulls and anomalies (results, not gaps)

A1 @509: "67 77 62 94 64 98 65" = "on ne qui". Parses under no reading.
True anomaly, 1/37. Morphologist concurs.
A2 @688: "29 40 65 94 29 60 03" = "65 ne er" ("ne"+"er" adjacent). Shared
with the n-e battery (see N3).
A3 @771/@774 mirror: "80 10 22 94 07 06 94" and "94 07 06 94 15 33 73".
Two 94s three apart sharing "07 06" ("ne 07 06 ne"). Unparsed. One
frame-type; flag to the formula finder.
A4 @161: "52-94-24-87" order is reversed vs F2 ("pas ne 24 ce"); folded
into F8.
A5 @1664: "98 80 22 94 84 64 06" = "22 ne on qui". "ne on" adjacency is
A15-C3 fenced territory (R1/R2 windows); noted, not adjudicated.
A6 unresolved singles: @250 ("44-94-65"), @349 ("12-94-74"), @494
("42-94-02"), @699 ("28-94-60"), @785 ("42-94-74"), @841 ("62-94-26"),
@1701 ("33-94-30"), @1705 ("62-94-88"), @1713 ("65-94-44"),
@65/@1549 ("12-94-92" x2, see N1).

## Notes for the n-e-12-48 battery (flagged, not adjudicated)

N1: "12-94" x3 (@65, @349, @1549); "12-94-92" x2 (@65, @1549). If 12="n"
(letter), this is "n"+"ne" adjacency -- needs a within-word reading. If
12="ne" (the weak pas-lead word reading), "ne ne" is impossible French.
The three windows discriminate between 12's hypotheses; they are the
n-e battery's frame-type, not this beat's.
N2: zero 94-48 adjacency in all 37 windows; 48 appears once in the +/-3
field (@1353: "48 77 78 94", three groups before 94). The ne-distributed
pair pattern (94="ne" word vs 48="e" letter in disjoint slots) is
undisturbed by these frames.
N3: A2 ("65 ne er") is a shared anomaly: as words it is ungrammatical,
so it points at within-word letter mixing -- common ground for both
batteries, not evidence for either.

## Cipher-testable consequences

1. F2's byte-identical "35-94-52-80-04" x2 predicts the 80/89 class after
   "ne pas" is infinitive-shaped; cross-check against the A8 verb-frames.
2. F1 predicts 30/39/37 after "n'est" are predicative/adjectival; @1795's
   "42 n'est 37" is the cleanest test ("42" and "37" both A1-predicative).
3. F4 predicts 82="m" clitic behavior; 82's other followers should be
   verb-shaped.
4. F7 predicts 93 verb-shaped; test 93's contact profile (currently n=14,
   inconclusive).
5. F8 predicts 24 verb/preposition-shaped ("ne 24 ce" x2; 24->87 x10/52).

## Ranked battery targets for the supervisor

1. 59="est" predicative battery via F1 followers (30/39/37 after n'est;
   @1795 "42 n'est 37" is the flagship).
2. 24 profile battery ("ne 24 ce" x2; 24->87 x10/52; 24's predecessors
   include 46="que" x3 and 84="on" x3).
3. 93 verb-shape discriminator (F7 consequence; narrow bar: 93 takes
   infinitive/valency markers).
4. "62-94-79-14-60" frame battery (F9; new unresolved frame-type x2).
5. A3 mirror "94-07-06-94" to the formula finder (@771/@774).

## Bottom line

Independent frame verification CONFIRMS the pre-finder's picture with one
citation correction: "n'est" x3 holds, but the third is @1795 ("42 n'est
37"), not @101; @101 is a bonus indirect frame ("on ne 93 est"). Six
clean "ne" frame-types (F1-F6, 12 instances), the conditioned "en" islets
re-derived disjointly (F10, 4 instances), three unresolved frame-types
(F7-F9), three true anomalies (A1-A3). Zero forced contradictions of
94="ne" in the 37 windows. No settled kills re-litigated.
