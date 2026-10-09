# Battery report: det-14-census (14 determiner-shaped legs)

- Target id: `det-14-census`
- Claim: "Test 14 as determiner-shaped at the surviving legs @72/@117/@178;
  the §7 homophony question for red team (flagged in stem-14-id)."
- Date: 2026-10-09. Worker: battery worker (agent
  8ed65872-645b-4e51-974c-430f19cc35ff). Lock
  `code/crowd17/next-token/locks/det-14-census.lock` created 2026-10-09T06:05:33Z;
  no prior/stale lock existed; deleted on completion after queue confirm.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json`
  + `data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
  (`load_rows` + `parse`). 1,847 pairs / 96 groups re-derived. R5005 untouched.
  `canonical.py` never used. No invented data.
- Coordinates with (not duplicating): stem-14-id (fenced 14's verb class
  lane-wide), stem-14-84-retest (NULL/fence), tout-slot-14 (NULL, tie on
  determiner legs), le-14-kill-1121 (killed 14='le' as a GLOBAL value),
  ce-le-verb-frame (NULL/fence: "ce le [verb]" ungrammatical), ent14ent-residual-
  adjudicate (KILL: "06-14-06" @1121 unresolvable at battery grade).

Indexing convention: @-offsets are 0-indexed pair indices into the repaired
stream, citing the 14 pair itself.

## Bar (pre-registered verbatim, from battery-queue.json)

"Stream-only evidence at @72/@117/@178 for 14 determiner shape."
"If homophony with the stem-14 reading is irreducible, package the §7 question
for red team; battery declares no polyvalence."

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. Collect and adjudicate stream-only evidence at @72, @117, and @178 for a
   determiner-shaped 14.
2. If homophony with the stem-14 reading is irreducible, package the §7
   question for red team; battery declares no polyvalence.

## Method

Fresh byte-exact re-parse of the repaired stream in-work; no prior counts
trusted. All three windows re-read at +-6 pairs with standing values.
Standing values used (none decided here): banked ground truth 11=la, 70=pre,
82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois,
79=tout (A5), 00=pour (A9), 84=on (A15), 47=ce (A4 allophone tier); provisional
59=est, 77="le"; class-level 65=NOUN, 21=NOUN (battery-promote), 69=NOUN
(battery-promote), 24=finite modal verb (class-level promote), 67 et/veut
positional rule (67="veut" iff follower infinitive-shaped). §7 respected: no
polyvalence declared.

## Window-level evidence (@-offsets, repaired stream)

- @72 (row a1_02): @66-80 =
  `92 69 13 24 56 87 14 24 87 11 00 11 29 42 98`.
  The contact: `87 14 24` = "ce [14] [24-verb]".
  - 14='le' as determiner: "ce le" = two determiners in a row —
    ungrammatical in 1841 French (ce-le-verb-frame candidate 2 FAIL).
  - 14='le' as object clitic: "ce le [verb]" — bare "ce" cannot subject a
    lexical verb and cannot stack with object clitic "le" before any verb,
    in French of any period (ce-le-verb-frame candidate 1 FAIL at battery
    grade, 2026-10-09).
  - No rescue: 87='ce' is granted; 24 is finite-verb class (no nominal head
    for a determiner reading); leftward composition "ce"+"le" is no French
    word; a clause boundary "ce le | [24]" leaves an ungrammatical fragment.
  - **LEG DEAD.** Correction of standing work: stem-14-id called this window
    "clean under 14='le' (A8 'ce le [verb]' frame)" and tout-slot-14 recorded
    it as "RESOLVES under 14='le'". Both rested on a "ce le [verb]" frame
    that the later battery ce-le-verb-frame (2026-10-09) tested and found
    ungrammatical. The leg is dead under the newest battery finding, which
    this battery adopts as a premise (not re-litigated).

- @117 (row a1_03): @111-125 =
  `93 29 89 68 21 67 14 21 60 90 19 58 66 98 82`.
  The contact: `67 14 21` = "et [14] [21-noun]".
  - 67='et' by the positional rule (follower 14 is not infinitive-shaped).
  - 21 = NOUN class (battery-promote, standing). "et le [21]" = conjunction
    + determiner + noun: clean and grammatical.
  - Granularity: the slot forces determiner/adjective/quantifier (something
    that precedes a noun after "et"); the value 'le' is the leading value
    (consistent with provisional 77='le' and the 14~77 homophony note), but
    is not forced — an adjective or quantifier reading is also grammatical.
  - **DETERMINER-SHAPED (class level), locus-level. 'le' leading, not forced.**

- @178 (row a1_05): @168-181 =
  `53 12 48 21 60 09 87 86 21 69 14 24 87 64`.
  The contact: `69 14 24` = "[69-noun] [14] [24-verb]".
  - 69 = NOUN class (battery-promote, 10-11 of 12 windows). "[69] le [verb]"
    = nominal subject + object clitic "le" + finite verb: grammatical
    ("l'homme le sait"-shaped).
  - This is CLITIC-'le', not determiner-'le': a determiner reading
    ("[69] le [24-verb]") would need a nominal head after "le", but 24 is
    finite-verb class. Determiner-shaped: NO. Clitic-shaped: YES.
  - This matches tout-slot-14's read of @178 as "the clitic reading's best
    leg"; the 69-noun promote (newer) makes the subject-capable reading
    cleaner than tout-slot-14's fence ("69 open") allowed.

## Per-clause pass/fail

1. Evidence collected and adjudicated at all three windows — **PASS** (result:
   @117 determiner-shaped at class level; @178 clitic-shaped, not determiner;
   @72 dead). The stem-14-id "surviving legs" list is reduced: one leg
   (@117) survives in determiner shape, one (@178) is reclassified as
   clitic, one (@72) is dead.
2. **CONDITION NOT MET — nothing to package.** The homophony question (is
   'le'-14 the same cell as verb-stem-14, i.e. a second polyvalence?) no
   longer has a live second member: the verb-stem reading of 14 is FENCED
   lane-wide (stem-14-84-retest, NULL, 2026-10-09), and 14='le' as a GLOBAL
   value is kill-grade dead (le-14-kill-1121 @1121). What remains is
   locus-level 'le' (determiner @117, clitic @178) — one French word, two
   normal syntactic functions, which is not a §7 polyvalence. Battery
   declares no polyvalence, per the bar.

Adverses: None listed. No standing red-team verdict contradicted or
downgraded: le-14-kill-1121 (global 'le' killed) stands; stem-14 fences
stand; tout-slot-14's tie is refined, not contradicted (its @72 "RESOLVES"
premise is superseded by the newer ce-le-verb-frame finding, stated
explicitly above).

## Verdict

**PROMOTE (finding grade, locus-level):** 14 is determiner-shaped at @117
("et le [21-noun]", row a1_03; class-level determination, value 'le' leading
but not forced). The §7 homophony question flagged in stem-14-id dissolves:
the verb-stem rival is fenced lane-wide, global 'le' is kill-grade dead, so
no irreducible homophony exists to package. The @72 'le'-leg from stem-14-id /
tout-slot-14 is dead (superseded by ce-le-verb-frame); @178 is clitic-'le',
not determiner-shaped.

Caveats: row offsets a1_02/a1_03/a1_05 are unvalidated (canonicality caveat
stands; only a5_03 is gloss-anchored). A rival offset for any of these rows
could re-phase the contacts.

## Follow-ups (optional; verdict is promote, so none required)

1. `det-14-locus-117` (P4): stress-test the @117 determiner leg against the
   offset-1 re-phase of row a1_03 (cf. seg-a1_01 for a1_01): does "67 14 21"
   survive as a contact under the rival phase?
2. `det-14-clitic-178` (P4): name the subject of "69 le [24-verb]" at @178 —
   is 69 the subject, or does the clause "ce 86 21 69" absorb it?
