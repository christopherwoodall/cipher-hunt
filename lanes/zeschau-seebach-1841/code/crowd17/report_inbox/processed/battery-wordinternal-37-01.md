# Battery report: wordinternal-37-01

- Target id: `wordinternal-37-01`
- Claim: "37-01 word-internal ('-faisant' compound adjective vs '-ci'/'-tain' ending)"
- Date: 2026-10-09
- Worker: battery worker (subagent a497999b-dd23-4b6e-8fc9-09da56ccd3d6)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  Re-derived in-session: 1,847 pairs, 96 types. All @-offsets are 0-based
  repaired-stream indices marking the 37 token (01 sits one index later).
  n(37) = 28, n(01) = 28. Never used canonical.py. R5005 not touched.
- Lock: code/crowd17/next-token/locks/wordinternal-37-01.lock (created at
  start, deleted on completion; no prior lock for this id existed).
  Lock note: a concurrent fresh lock `sub02-wordinternal.lock`
  (agent aa8ac989-..., 2026-10-09T05:45:23Z) exists for a different
  word-internal target namespace; its windows do not overlap the three
  37-01 windows tested here. Noted, no action.

## Bar (verbatim, pre-registered before testing)

"the '37 01' x3 parse as one word with a stated internal segmentation and
zero contradiction; state the consequence for ci-01-value's kill if the
internal reading lands"

Numbered pass/fail clauses (restated before testing, not modified after):

1. W1 (@939, row a5_10: `...[21] qui(64) [37-01] [07]...`) parses with
   37-01 as ONE French word under the stated segmentation, zero
   contradiction.
2. W2 (@1633, row a8_03: `...[21] qui(64) [37-01] [74]...`) parses with
   the SAME one-word segmentation, zero contradiction.
3. W3 (@1817, row a8_10: `...[06] er(29) [37-01] [02]...`) parses with
   the SAME one-word segmentation, zero contradiction.
4. The reading is consistent with standing constraints: A12's 37-01
   unit grant is affirmed (not re-litigated); 37's global value
   (S5, frame-37-reexam) is neither named nor decided — the reading is
   LOCAL to the three windows (word-internal syllable, pre-a-la
   precedent).
5. The consequence for ci-01-value's kill is stated explicitly.

Stated internal segmentation (pre-registered with the clauses):
37 = [faire-compound stem] ("satis" / "contre"), 01 = "fait"
(/fɛ/, 3sg present of "faire"). The word is a "faire"-compound
FINITE VERB, 3rd singular present. Lead lexicalization: "satisfait"
(satisfies). Live alternative: "contrefait" (counterfeits, forges).
Both are transitive 3sg verbs; the bar does not require choosing
between them (same segmentation shape, same parses).

## Method

1. Re-derived the repaired parse in-session (1,847 pairs / 96 types).
2. Byte-exact bigram search for 37-01: exactly 3 windows, at
   37-positions @939, @1633, @1817. No other 37-01 adjacency
   stream-wide.
3. Extracted +-10 windows for all three; verified the byte-identical
   left 8-gram "56 69 26 00 33 21 64 37" at @932-939 and @1626-1633
   (A12's "21-64-37-01" 4-gram x2 confirmed at @937-940, @1631-1634).
4. Tested each named hypothesis family against standard French
   grammar at the three windows. The binding constraint: 64 = "qui"
   is GRANTED (protocol section 7); a relative "qui" must be followed
   by a finite verb phrase. A one-word non-verb after "qui" is
   ungrammatical at kill grade.
5. Tested the surviving finite-verb family ("faire"-compounds) at all
   three windows, including W3's left edge.

## Window-level evidence

### W1 @939 (a5_10)
`82 98 83 56 69 26 00 33 21 64 [37] [01] 07 50 40 08 62 98 96 86`
= "...pour(00) [33] [21], qui(64) [37-01] [07] [50] e(40) [08]..."
- Named disjuncts, all KILLED here: "qui satisfaisant /
  bienfaisant / malfaisant" (participle/adjective cannot follow
  relative "qui" -- "qui" demands a finite verb); "qui voici /
  merci / souci" ("-ci" ending); "qui certain / lointain /
  fontaine / capitaine" ("-tain" ending). Every named option forces
  the claim false at this window.
- Surviving reading: "...[21], qui satisfait/contrefait [07]..."
  = "...[21], who satisfies/counterfeits [07]...". Relative "qui" +
  3sg finite verb + direct-object [07]. GRAMMATICAL, zero strain.
  (With 33 = "dire"-family: "pour dire [21], qui satisfait [07]"
  = "to say [21], which satisfies [07]" -- fully clean.)

### W2 @1633 (a8_03)
`67 33 46 56 69 26 00 33 21 64 [37] [01] 74 87 74 74 35 56 12 33`
= "...pour(00) [33] [21], qui(64) [37-01] [74] ce(87) [74]..."
- Same byte-identical left 8-gram as W1; same verdict. Named
  disjuncts KILLED identically ("qui" + non-verb).
- Surviving reading: "...[21], qui satisfait/contrefait [74].
  Ce [74]..." GRAMMATICAL, zero contradiction.

### W3 @1817 (a8_10)
`52 80 04 61 15 93 50 42 06 29 [37] [01] 02 09 19 00 97 00 86 29`
= "...[42] [06]er(29) [37-01] [02] [09] [19] pour(00) [97]..."
- Parse: "[06]er satisfait/contrefait [02]" via the
  infinitive-as-subject construction: "[To-06] satisfies/forges
  [02]" (cf. "Vouloir, c'est pouvoir"; "Partir, c'est mourir un
  peu" -- bare infinitive subjects are grammatical French).
  3sg verb agrees with the singular infinitive subject; [02] is
  the direct object (both verbs transitive). GRAMMATICAL.
- Left edge fenced (not contradictory): [42]/[50]/[04]... precede
  with a clause boundary ("...[42]. [To-06] satisfies [02]...");
  42's value is open and A1's predicative legs are weak, so the
  edge is loose but forces nothing false.
- Fenced alternative (not load-bearing): if 06-29 is not a
  standalone infinitive but the tail of a longer infinitive
  (06 = "ent" is PROMOTED as verb ending; "enter"-tail as in
  "inventer"-shaped 42-06-29), the infinitive-subject parse still
  holds with the longer infinitive as subject. Queued as
  follow-up w3-06-29-leftedge; it does not threaten the bar.

### Cross-window consistency
- Same tokens at all three windows -> same word (protocol section 7:
  67 et/veut is the sole true polyvalence; no second polyvalence
  declared or needed). The finite-verb reading is UNIFORM across
  all three: no positional rule, no fork.
- 37's successor census: 78 x4, 43 x3, 64 x3, 01 x3, 11 x2, 77 x2
  -- the 01-follower is 3/28, exactly the three windows; nothing
  else in 37's profile forces a global syllable reading.
- 01's predecessor census: 37 x3 (these windows), 16/87/85/86/76
  x2 each -- the 37-predecessor is local; no other 01 window is
  touched by 01 = "fait" (syllable, local).

## Per-clause pass/fail

1. W1 one-word parse, stated segmentation, zero contradiction: PASS
   ("qui satisfait/contrefait [07]"). Named disjuncts killed at
   kill grade at this window.
2. W2 same: PASS ("qui satisfait/contrefait [74]").
3. W3 same: PASS ("[06]er satisfait/contrefait [02]",
   infinitive-subject; left edge fenced loose, non-contradictory).
4. Standing-constraint consistency: PASS. A12's unit grant
   AFFIRMED (one word = one unit; the grant was value-free and is
   untouched, not re-litigated). 37's global value (S5 "le" MEDIUM,
   frame-37-reexam escalated) is NOT named and NOT decided: the
   syllable reading is local to these three windows, per the
   pre-a-la precedent (a-39: word-internal "a" inside "prealable"
   coexists with 39 = "a/a"). No standing red-team verdict is
   contradicted or downgraded.
5. Consequence for ci-01-value's kill: PASS (stated below).

Adverses, answered:
- (a) "coordinate with noun-43 / frame-37-reexam": ANSWERED.
  noun-43's 01-windows (87-01 @1028, "par [43] ce [01]") do not
  overlap the three 37-01 windows; local 01 = "fait" does not touch
  them, and noun-43 (NULL, value unnamed) is unaffected.
  frame-37-reexam's standalone "qui 37" @675 (verb-position 37 as a
  word token) is consistent-with a verb-distribution 37 but is not
  load-bearing here; 37's class/value question stays with the red
  team -- this battery decides nothing about it.
- (b) "A12 promotes 37-01 as a unit (unit grant, not value)":
  ANSWERED. This reading affirms and concretizes the unit grant
  (the unit is one word); the grant itself is not re-litigated.

## Consequence for ci-01-value's kill (explicit)

1. The kill STANDS in full. 01 = "faisant" (general token value)
   and 01 = "ci" (general) remain killed. 01 = "fait" is a LOCAL
   syllable inside 37-01, and "fait" != "faisant": the killed
   general values are not resurrected.
2. The kill's explicitly-open word-internal question is now
   ANSWERED: 37-01 IS word-internal -- but NOT as a "-faisant"
   compound adjective ("satisfaisant"-shaped; killed at "qui" in
   W1/W2). It is a "faire"-compound FINITE VERB
   ("satisfait"-shaped: 37 = "satis"/"contre", 01 = "fait").
3. No interaction with the other local 01 readings: disc-01-24-ci-X's
   01 = "en" (local to the three 01-24 windows) and ci-bound-01's
   bound "-ci" (87-01/47-01/45-01 windows) occupy disjoint window
   sets. No unification is proposed (that would be a second
   polyvalence -- red-team-only per section 7).
4. Red-team note: 01 = "fait" (local syllable /fɛ/) vs the killed
   84 = "fait" (token value, superseded by 84 = "on") are distinct
   claims at distinct scopes (syllable vs token). No conflict;
   flagged so the syllable/token boundary stays explicit.

## Verdict: PROMOTE (narrowed; battery-level, unratified)

37-01 is word-internal: one word, a "faire"-compound 3sg finite
verb (37 = [compound stem], 01 = "fait"). Lead lexicalization
"satisfait" (satisfies); live alternative "contrefait"
(counterfeits/forges) -- discriminating the stem is red-team/S5
territory (s5-foundation), not decided here. The claim's named
disjuncts -- "-faisant" compound adjective, "-ci" ending, "-tain"
ending -- are KILLED at W1/W2 ("qui" + non-verb is ungrammatical
at kill grade). All five bar clauses pass; both adverses answered.

## Follow-up targets (residuals)

1. **satisfait-contrefait-lex** (P3): discriminate the compound stem
   ("satis" vs "contre") behind 37 in 37-01. Needs 37's stem value
   (red-team/S5 territory -- coordinate with s5-foundation, do not
   duplicate) or period-corpus attestation of "qui satisfait" /
   "qui contrefait" government with the observed followers
   ([07] @941, [74] @1635, [02] @1819).
2. **w3-06-29-leftedge** (P4): pin down W3's "[06]er" -- standalone
   infinitive vs tail of a longer infinitive ("inventer"-shaped
   42-06-29 under promoted 06 = "ent"). Decides whether the
   infinitive-subject parse is the only grammatical option or one
   of two; does not threaten this verdict either way.
