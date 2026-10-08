# Battery report: ne-24-profile

- Target id: `ne-24-profile`
- Claim: "24's class via \"ne 24 ce\" frames"
- Date: 2026-10-08
- Worker: agent 615df811-ae3c-400a-89a1-2f9ef84c4ece
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
  All @-offsets are repaired-stream indices. n(24) = 52.

## Bar (verbatim, pre-registered before testing)

"profile iff 24's class named (verb/preposition) with 'ne 24 ce' x2 parsing +
24->87 x10/52 explained"

Numbered pass/fail clauses (restated, not modified):

1. 24's class is named as verb or preposition. The other arm is killed.
2. Both 'ne 24 ce' windows parse under the named class.
3. The 24->87 contact (x10/52) is explained under the named class.

## Method

1. Parsed the repaired stream. Extracted all 52 windows of 24 (±4 shown,
   ±10 for the two 'ne 24 ce' windows).
2. Ran predecessor and successor censuses for 24.
3. Re-derived the evidence counts: 'ne 24 ce' = 94-24-87 at @162 and @1774
   repaired (evidence's @161/@1773 are one pair off; same frames).
   24->87 x10/52 confirmed at @73, @162, @179, @190, @643, @823, @829,
   @1486, @1766, @1774. 46->24 x3 and 84->24 x3 confirmed.
4. Tested every window for a grammatical parse with 24 as finite verb vs
   24 as preposition.
5. Corpus baselines: lone-"ne" rate for 94 (94='ne' battery-promoted);
   ce-followership control on 59 ('est' provisional, finite verb).

## Window-level evidence

Finite-verb slots (subject or subordinator directly before 24):

- @547: `42 06 00 46 [24] 47 46 55 81` — "que [24] ce(47) que(46)".
  "que" + finite verb.
- @955: `86 96 87 46 [24] 85 04 20 67` — "par(96) ce(87) que(46)
  [24] [85-stem]". "que" + finite verb taking a verb stem.
- @1693: `14 60 27 46 [24] 85 58 15 23` — "que [24] [85-stem]".
- @311: `20 17 46 84 [24] 37 78 45 64` — "que(46) on(84) [24] [37]
  …". "qu'on [verb] [predicative?]".
- @474: `06 67 46 84 [24] 37 78 74 45` — "et/veut(67) que(46)
  on(84) [24] [37] …". Same frame as @311.
- @1486: `62 46 77 84 [24] 87 08 31 92` — "que(46) l'on(77-84)
  [24] ce(87) …". (77='le' provisional + 84='on' granted = "l'on".)

Infinitive-taking (24 followed by verb-shaped elements), 10/52:

- 24->85 x5: @732, @955, @1438, @1693, @1754 (85 = verb-stem, A3 frame grant).
- 24->89 x3: @221, @985, @1497 (89 = verb-frame, A8).
- 24->80 x2: @564, @672 (80 = verb-frame, A8).
- 24->82->16 x2: @535 `08 [24] 82 16 91`, @1830 `83 [24] 82 16 59`
  — "[24] m(82) [16]", modal + pronoun + infinitive shaped
  ("peut me [dire]"-shaped; 16's value is open under frame-82-16).

Postverbal "pas":

- 24->30 x3: @29 `34 [24] 30 03`, @1268 `88 [24] 30 20`,
  @1728 `88 [24] 30 15`. "[24] pas" with "ne" dropped or distant.

'ne 24 ce' x2:

- @1774: `37 78 62 94 [24] 87 64 59 19` — "[62-subj] ne [24].
  Ce qui est [19], …". 62 is subject-shaped (nest-subject battery,
  PROMOTED 2026-10-08). "ce qui est [19]" = "what is [19]", a clean new
  clause, so a clause boundary sits before 87. "ne [24]" with no "pas"
  nearby (no 30 within ±15): corpus baseline is 34/37 "94" windows with
  no "pas" in +1..+4, so lone-"ne" is this author's norm, not a strain.
- @162: `35 93 52 94 [24] 87 11 24 82 84 53 12` — "[…] ne [24].
  Cela [24] m …". Same lone-"ne" + clause-boundary parse as @1774.
  The subject (in 35-93-52) is unidentified: fenced, not forced.
  The tail "cela [24] m on …" is awkward and stays fenced; it is
  outside the 'ne 24 ce' frame.

24->87 x10/52, with 87's follower:

- @73: 87-11 "cela"; @162: 87-11 "cela"; @829: 87-11 "cela".
- @179: 87-64 "ce qui"; @1766: 87-64 "ce qui"; @1774: 87-64 "ce qui".
- @823: 87-59 "ce est" = "c'est".
- @190: 87-98 "ce [98]"; @643: 87-61 "ce [61]"; @1486: 87-08 "ce [08]".
- Followers of 87 vary (11 x3, 64 x3, 59, 98, 61, 08): 24-87 is not a
  fixed compound. Every follower is a clause-opening or NP-opening "ce".
- Control: 59 ('est' provisional, finite verb) -> 87 = 0/27. The 19%
  rate is distinctive to 24, not a generic finite-verb trait.

Preposition arm killed (kill grade): a preposition cannot follow "que"
(x3: @547, @955, @1693), "on" / "qu'on" / "que l'on" (x3: @311, @474,
@1486), or "ne" (x2: @162, @1774). Eight windows are ungrammatical
with 24 as a preposition.

## Per-clause pass/fail

1. Class named (verb/preposition): PASS. 24 is a finite verb,
   infinitive-taking (modal-shaped). The preposition arm is killed at
   kill grade by eight windows. No value is named: "peut" vs "sait" vs
   "doit" stays open for a value battery.
2. 'ne 24 ce' x2 parsing: PASS. Both windows parse as "[subject] ne
   [24]. Ce …" with a clause boundary before 87 and the author's normal
   lone-"ne" (34/37 baseline). @1774 is clean (62 subject-shaped,
   promoted). @162's subject is fenced as unidentified; its tail
   ("cela [24] m on …") is fenced outside the frame.
3. 24->87 x10/52 explained: PASS. 24 is often clause-final: the
   absolute "ne [24]" is a complete clause ("he cannot"-shaped), and
   demonstrative/relative "ce" (cela x3, ce-qui x3, c'est x1, ce+NP x3)
   opens the next clause. The 59-control (0/27) shows the rate is
   distinctive to 24, and the absolute-modal account explains why.

## Adverses

Listed adverse "24's profile unresolved": ANSWERED. Profile: finite
verb, infinitive-taking; 6 subordinate finite slots ("que 24" x3,
"qu'on 24" x2, "que l'on 24" x1); 10 infinitive-frame complements
(85 x5, 89 x3, 80 x2); "m"+infinitive x2; postverbal "pas" x3;
lone-"ne" x2; clause-final before "ce"-openers x10.

Fenced residuals (stated cause, none ignored):

- "la 24" x3: @732 `88 11 [24] 85`, @783 `89 11 [24] 42`,
  @1657 `37 11 [24] 48`. "la" as previous clause's object pronoun is
  available in each; 88-11 / 89-11 compounds untested. (The fourth,
  @165, dissolves: its "11" is the tail of granted "cela" = 87-11.)
- 24-24 @806 `@806: 69 [24] [24] 41`: doubled 24 reads as formula/list,
  fenced like other fixed pairs (cf. 62-94 x9, doubled 06 in
  94-82-06-06). Not kill-grade.
- @29 `34 [24] 30`: 34='i' is a letter; likely a word-internal
  boundary ("…i [24] pas"). Fenced.
- @190 `00 66 [24] 87`: "pour(00) [66] [24]" needs 66's class;
  "[66-subject] [24]" parses if 66 is nominal. Fenced.
- "49 24 26 30" x2 (@654, @991): "[24] [26] pas" parses as modal +
  infinitive + "pas" with the author's "ne"-drop iff 26 is verb-shaped;
  26's class is open (noun-26 null). Fenced to noun-26.
- "01 24" x3 (@41, @829, @985): parses as nominal-01 + finite-24;
  01's value is open and owned by disc-01-24-ci-X. Not duplicated here.
- "84 24 37 78" x2 (@311, @474): "on [24] [37-78 …]" is consistent
  with 24 as modal verb under both of w1-314-ambig's forks
  (word-internal 37-78 = infinitive complement, or predicative 37 =
  clause edge). Owned by w1-314-ambig. Not duplicated here.

## Verdict

**promote** — class-level. 24 = finite verb (infinitive-taking,
modal-shaped). The value ("peut"/"sait"/"doit"-class member) is NOT
named and NOT promoted; it belongs to a future value battery.
Downstream consumers: disc-01-24-ci-X (01-24 x3; consequence: 24 as
finite verb is compatible with nominal-01 subjects) and w1-314-ambig
(84-24-37-78 left context consistent with modal 24 under both forks).

No standing red-team verdict constrains 24's class; no contradiction
found, so no escalation. No polyvalence declared (67 et/veut remains
the sole true polyvalence per §7).
