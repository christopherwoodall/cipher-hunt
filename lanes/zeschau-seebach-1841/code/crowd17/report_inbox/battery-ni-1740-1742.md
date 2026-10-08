# Battery report: ni-1740-1742

Target: ni-1740-1742.
Claim: exactly one boundary parse covers '86 12 34 94 82 46' (@1739-1744).

## Bar (pre-registered verbatim)

"resolve iff one parse holds with banked values and zero contradiction; else fence BOTH readings for the 12/94 duality adjudication (red team)"

Numbered clauses:

1. Exactly one boundary parse covers @1739-1744 ("86 12 34 94 82 46") with banked values and zero contradiction.
2. Else: fence BOTH candidate readings for the red-team 12/94 duality adjudication, each with its failure cause stated.

## Method

Repaired 1,847-pair stream only (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per repair_parse.py). canonical.py not used.
R5005 not touched. Window @1739-1744 confirmed on stream: 86 12 34 94 82 46
(row a8_07). Standing values used: banked GT 34="i", 82="m", 46="que";
granted 12="n" (letter tier, R17-002), 06="ent" (conditional, R17-007, context
only); STRONG LEAD 94="ne" (R17-001, conditional, tested arguendo); INF-class
86 (A9, class-level). Census counts below are stream counts from the repaired
parse.

## Window evidence (@-offsets)

- @1739-1744 = 86 | 12 | 34 | 94 | 82 | 46. Left: @1736-1738 = 12 48 52
  ("ne" analytic, 12-48 x5 per R17). Right: @1745-1749 = 56 40 06 65 34
  ("[56]e ent [65] i").
- Bigram census: 12-34 occurs exactly 1x stream-wide (@1740). 86-12 1x
  (@1739). 34-94 1x (@1741). 82-46 1x (@1743). No second "ni" exists anywhere.
- 94-82 occurs 4x: @578, @1182, @1353, @1742. The first three are all
  94-82-06-06 = "ne m'entent" (R17-007 frame: "me" elides to "m'" before
  vowel-initial 06="ent"). @1742 is the sole 94-82 followed by 46="que"
  (consonant-initial): no elision possible there.

Reading P1: 86 | 12-34="ni" | 94="ne" | 82="m" | 46="que".
- "ni" as a word is the correlative conjunction "ni...ni". It needs a
  partner. 12-34 is a hapax: no partner exists. Single "ni" is
  ungrammatical French. P1 FAILS.
- "ne me": banked 82="m" (pencil GT). "me" is 82-48 (R17-003); no 48 is
  present. Elision "m'" needs a following vowel; 46="que" is
  consonant-initial. "m" is stranded. P1 FAILS.
- "ni ne" juxtaposition is ungrammatical. P1 FAILS.
- Result: P1 holds zero parses. Kill-grade failure (forces ungrammatical
  French on banked values).

Reading P2: 86 | 12="n" | 34="i" | 94="ne" | 82="m" | 46="que".
- 12="n" as a word: "n" is not a French word. As final letter of 86's word
  ("...[86]n"), 34="i" stands alone as a word: "i" is not a French word.
  P2 FAILS.
- Variant 86-12-34 = one word ("...ni", participle-shaped): 86-12 is a
  hapax bigram (no unit support), and "ne m que" stays verbless with "m"
  stranded (same letter-level failure as P1). P2 FAILS.
- Variant 12-34-94 as letters ("nine"/"ine"): no French word; also needs
  94 as letters against the standing "ne" frame with no basis. P2 FAILS.
- Result: P2 holds zero parses.

## Per-clause pass/fail

1. FAIL. Zero boundary parses cover @1739-1744 with banked values and zero
   contradiction. P1 fails on three independent grounds (hapax "ni" with no
   correlative partner; banked 82="m" kills "ne me"; "ni ne" ungrammatical).
   P2 fails ("i"/"n" stranded as non-words; participle variant still
   verbless). The claim "exactly one" is forced false by the window.
2. EXECUTED. Both readings fenced below for the red-team 12/94 duality
   adjudication. Scope kept to @1739-1744; prenne-70-12-94's ownership of the
   general 12/94 duality is not touched (no bar overlap).

## Verdict: kill

The claim is false at kill grade: the window admits zero clean parses, not
one. Both candidate readings are fenced, not promoted around.

Fence record for red team:
- F-P1 ("ni" word reading): fenced. Causes: (a) 12-34 hapax, no "ni...ni"
  partner stream-wide; (b) 82="m" banked kills "ne me" (needs absent 48;
  elision blocked by consonantal "que").
- F-P2 ("n"+"i" letter split): fenced. Causes: (a) "n"/"i" stranded as
  non-words; (b) word-internal variants leave "ne m que" verbless.
- Note for red team: @1742 is the odd one out among the four 94-82 windows
  (the other three are "ne m'entent" 94-82-06-06). This independently
  confirms R17-001's "verbless 'ne me que'" strain note.

Red-team consistency check:
- R17-002 (12="n" letter-tier grant, leg "12-34 'ni' @1740"): NOT
  contradicted. The grant is the LETTER "n"; this battery affirms 12="n"
  as letters and kills only the WORD-"ni" reading, which R17-002 never
  granted.
- R17-001 (94="ne" STRONG LEAD, "verbless 'ne me que'" strain): NOT
  contradicted. Both readings were tested with 94="ne" arguendo; they fail
  on French grammar and banked 82="m", independent of 94's unsettled status.

## Follow-ups (for the red-team fence)

1. rightedge-56-1745. Claim: "56-40-06 @1745-1747 reads '[56]ent' (3pl
   verb), closing the 'que' subordinate clause." Bars: (a) 56 named from its
   contact profile; (b) "que [56]e ent" parses as conjunction + 3pl verb
   with zero contradiction; (c) result states the consequence for the
   @1742-1744 fence (fixes the right edge, isolates the left-edge failure).
   Evidence: 56-40-06 @1745-1747; 06="ent" granted conditional (R17-007).
   Adverses: 56's value open.
2. leftedge-52-86-1736. Claim: "@1736-1739 'ne [52] [86]' parses as the main
   clause hosting the fenced window." Bars: (a) 52 named with "ne [52] [86]"
   parsing (12-48 analytic "ne" + INF-class 86); (b) the clause boundary
   before @1742 stated or fenced; (c) zero contradiction with A9's 86 grant.
   Evidence: @1736-1737 = 12-48 ("ne", 1 of x5); 86 INF-class (A9).
   Adverses: 52's value open; 86 stem/whole caveat.

Lock: worker 06cd27e6-6b91-47b2-bc1a-c6bea1d08b01, 2026-10-08T17:17:37Z.
No lock staleness (fresh lock, own run).
