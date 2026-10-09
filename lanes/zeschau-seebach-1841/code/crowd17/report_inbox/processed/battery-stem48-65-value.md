# Battery report: stem48-65-value — 2026-10-09

Worker: d00ca89b-6db4-48b4-9f43-7ffe143af0a7. Stream: repaired 1,847-pair parse
(code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per
code/side-keyhunt/repair_parse.py). @-offsets below are the pair index of 48 itself
(@1589 = 48; the 65 token is @1588). Lock: locks/stem48-65-value.lock created
2026-10-09T05:48:05Z (no fresh lock present). canonical.py not used. R5005,
sealed gates, red-team queue untouched.

## Standing facts (not re-litigated)

- 65 = NOUN-CLASS promoted (battery-prof-65.md, 2026-10-08); verb rival killed at
  kill grade. This battery names 65's syntactic role at @1589 only.
- A7-L2 frame ("tout me [48-verb]") narrowed by the red team to its exclusive
  legs @1229/@1589 (R17-024, next-token-redteam-r17.md); 48="e" is the general
  value; the verb-stem frame is conditioned, not a second polyvalence.
- 12="n" (letter), 30="pas" promoted (R17). 64="qui" granted unconditioned.

## Bar (verbatim, pre-registered 2026-10-09 BEFORE testing)

"65 named with the infinitive complement parsing under standing values; input to
the A7-L2 scope ruling."

## Numbered clauses (restated before testing; bar unmodified)

1. ROLE-NAMED: 65's syntactic role at @1589 is named (class + grammatical
   function), consistent with the standing promoted class 65=NOUN-CLASS
   (no re-litigation of the class verdict).
2. LEG-PARSES: the @1589 leg shape "[65] [STEM]er ce [08]" parses as a grammatical
   French (1841 diplomatic register) structure under standing §7 values, with the
   infinitive complement "[STEM]er ce" receiving a licensed syntactic role.
3. SCOPE-INPUT: the naming is recorded in a form usable by the A7-L2 scope ruling
   (what the leg's shape implies for the frame's live scope at @1589).

## Method

Re-derived the @1589 window byte-by-byte from the repaired stream (never
canonical.py). Applied standing values only (banked/granted/promoted; open
tokens left open). Tested candidate syntactic roles for 65 against 1841 French
grammar: (a) expressed subject of the infinitive (perception/causation
licensing, "pour"/"sans" licensing, interrogative-"qui" licensing, gapped-verb
licensing); (b) noun taking the infinitive as complement; (c) direct/indirect
object of the infinitive (fronted, dative-shift); (d) vocative + injunctive
infinitive; (e) appositive/nominalized-infinitive compound; (f) "quiconque"
re-segmentation. Checked lane precedent on "qui"+bare infinitive
(battery-at21-82-43-29: "qui emmener" ruled ungrammatical) and on
pronoun/noun+infinitive licensing ("à"/"de" required). Census of the "64 65"
bigram lane-wide.

## Evidence — the @1589 window

Row a8_02, stream @1582–1603:

`12 44 00 36 70 64 65 48 29 47 08 81 03 29 80 67 77 81 82 98 00 44`

Standing values applied:

`[12] [44] pour(00) [36]pre(70) qui(64) [65-noun] [STEM]er(48-29) ce(47) [08] [81]
[03]er [80-verbframe] et(67; follower 77 not infinitive-shaped) le(77) [81]
me(82) [98] pour(00) [44]`

- "64 65" (qui-before-65) is a STREAM HAPAX: exactly 1 occurrence in 1,847
  pairs (@1587–1588). The reverse "65 64" occurs x3 (@724/@1208/@1340), always
  65-as-relative-head with a finite verb after "qui" ("65 qui la pour",
  "65 qui est 32", "65 qui 52 38").
- The local trigram 48-29-47 = "[STEM]er ce" parses (infinitive + "ce"-object);
  this is the stem48 battery's result, uncontested here. The problem is 65
  and "qui", not the trigram.
- After "qui" (@1587), the next verb-shaped tokens are 80 (@1596, A8
  verb-frame) and 98 (@1601, "vient"-lead): 9–14 tokens downstream. A relative
  clause spanning to 80 would be verb-final — ungrammatical in French (SVO,
  no verb-final relatives).

## Candidate parses tested (all fail; stated cause each)

1. **65 = expressed subject of the infinitive, licensed by perception/causation
   verb** ("voir [NP] [inf]"): no perception/causation verb adjacent to 65
   (preceder is 64="qui"; 24=@1580 is 8 tokens left with "53 12 44 pour
   [36]pre qui" intervening — adjacency required). FAIL.
2. **65 = expressed subject, licensed by "pour" (00=@1584)**: "pour" governs
   "[36]pre", not 65; "qui [65]" cannot be folded into the governed NP (the
   relative still needs its verb). FAIL.
3. **"qui" = interrogative object of "[STEM]er", 65 = subject**
   ("whom [65] to-[STEM]"): French bars expressed subjects in "qui"+infinitive
   interrogatives; and "ce" would be a second accusative (no double
   accusatives in French). FAIL.
4. **"qui" = relative, "qui [65]" with elided copula**: French never elides the
   copula in relatives ("qui [est] [65]" ungrammatical as written). FAIL.
5. **65 = noun taking "[STEM]er ce" as bare infinitive complement**: French
   nouns take infinitive complements via "de"/"à" only (lane precedent:
   "à le faire", "de le voir" — preposition required); no bare-infinitive
   noun-complement construction exists. FAIL.
6. **65 = fronted direct object / dative-shifted indirect object of
   "[STEM]er"**: non-clitic objects follow the verb; French has no dative
   shift. FAIL.
7. **65 = vocative + injunctive infinitive** ("[65]! [STEM]er ce!"): leaves
   "qui [65]" unparsed (vocative after "qui" is unlicensed). FAIL.
8. **"quiconque" re-segmentation (64-65 = "qui"+"conque")**: contradicts the
   unconditioned grant 64="qui" (67 is the sole polyvalence); and
   "quiconque"+infinitive is ungrammatical anyway (needs finite verb).
   REJECTED (not escalated: rejected hypothesis, no standing verdict
   overwritten).
9. **65 = object of gapped perception-verb** ("qui [65] [24∅] [STEM]er ce",
   verb gapped from @1580): the ONLY fully grammatical candidate — but French
   gapping is not licensed across a relative-clause boundary without
   coordination ("…pour [36]pre, qui…" has no coordinator). FAIL on the
   gapping constraint.
10. **"qui"+bare infinitive generally**: lane precedent
    (battery-at21-82-43-29) already rules "qui"+bare infinitive without
    governing preposition ungrammatical; "qui [65] [STEM]er" is strictly worse.
    FAIL.

## Per-clause pass/fail

1. ROLE-NAMED: **FAIL.** No licensed syntactic role is nameable for 65 at
   @1589 under standing values. 65=NOUN-CLASS is held fixed (not re-litigated);
   every role candidate (subject-of-infinitive, complement-taker, object,
   vocative, appositive) fails on a hard grammatical constraint or a missing
   licensor. The "64 65" hapax means there is no parallel window to learn the
   construction from.
2. LEG-PARSES: **FAIL.** "[65] [STEM]er ce [08]" does not parse as "noun +
   infinitive-complement" or any other licensed structure. The LOCAL
   "[STEM]er ce" parses (stem48 battery, uncontested), but with 65 present the
   leg has no grammatical parse: "qui [65]" does not close (no finite verb,
   no preposition, interrogative blocked by intervening 65) and "[65-noun]
   [STEM]er" has no licensed construction.
3. SCOPE-INPUT: **PASS (input delivered).** The material asymmetry between the
   two exclusive legs is documented below for the A7-L2 scope ruling.

## Verdict: NULL

HEADLINE: 65's role at @1589 cannot be named — the window's global syntax does
not close under standing values. The stem48 battery proved the LOCAL trigram
requires the stem reading; this battery shows the leg WITH 65 has no licensed
parse: "qui [65]" is a stream hapax whose "qui" (granted) has no finite verb,
no governing preposition, and no interrogative reading (blocked by the
intervening 65), while "[65-noun] [STEM]er" matches no French construction
(nouns take infinitive complements via "de"/"à" only; the perception-verb
licensing has no governor; the one grammatical candidate — gapped
perception-verb — violates the gapping-across-relative-boundary constraint).

SCOPE-RULING INPUT (Clause 3): the two A7-L2 exclusive legs are asymmetric.
@1229 parses cleanly: "tout(79) me(82) [STEM]er ce(47) [33]er" — clitic "me" as
the infinitive's indirect object, "ce [33]er" (demonstrative +
infinitive-as-noun) as direct object. @1589's pre-stem slot holds a FULL NOUN
(65) with no licensed relation to the infinitive, preceded by an unclosable
"qui [65]" hapax. R17-024 narrowed A7-L2 to both legs; this battery does NOT
overturn that narrowing (it rules on 48's frame, this rules on 65's role), but
flags for the red team: @1589 is the weaker leg — if the scope ruling is ever
revisited, the @1589 leg's membership should be re-examined, since its
pre-stem syntax does not match the "tout me [48-verb]" shape (no "tout", no
clitic "me", noun unlicensed).

## Follow-up targets (null regenerates work)

1. **stem48-65-governor** (priority 2): find the governor of the @1589
   infinitive. Test whether 24 (@1580, finite-verb frame), 00 (@1584, "pour"),
   or 80 (@1596, A8 verb-frame) licenses "[65] [STEM]er ce [08]" with "qui
   [65]" closing. Bar: full-window grammatical parse with every token
   licensed, or the window confirmed as a syntax orphan with the orphan's
   locus named (65? qui? the 64-65 boundary?).
2. **stem48-qui-65-hapax** (priority 3): "64 65" is a stream hapax
   (@1587–1588). Test rival roles/attachments for "qui" at @1587 (relative vs
   interrogative vs indefinite) and rival left-attachments for 65, WITHOUT
   contradicting granted 64="qui"/70="pre" (value rivals such as "quiconque"
   belong to noun-65-value, not here). Bar: a licensed parse of @1585–1588
   under standing values, or all re-reads exhausted with stated cause.
3. **stem48-1229-1589-asymmetry** (priority 3): ruling-ready statement of the
   pre-stem asymmetry between the two A7-L2 exclusive legs (@1229: clitic
   object "me", clean parse; @1589: full noun 65, unlicensed role; "qui [65]"
   hapax). Bar: documented consequences for whether the conditioned A7-L2
   frame covers both legs or @1229 only, with @-offsets and the parses above
   as evidence. For the red-team scope docket.

## Provenance

n(48)=38, n(65)=25 re-derived from the repaired stream in-work. "64 65" x1
(@1587–1588), "65 64" x3 (@724/@1208/@1340) — census byte-exact. No invented
data, no invented constructions; every rejected parse carries its stated
grammatical cause. Lock created on start, deleted on completion (see queue
update note).
