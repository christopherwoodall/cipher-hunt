# Battery report: imp-80-set

- Target id: `imp-80-set`
- Claim: "80's imperative set grows and 03 resolves to close @1032"
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
  All @-offsets are 0-based repaired-stream indices. n(80)=17, n(03)=20.
  Never used canonical.py. R5005, sealed gates, red-team queue untouched.
- Lock: code/crowd17/next-token/locks/imp-80-set.lock (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"(a) grow 80's imperative set beyond n=2 with windows consistent with mood
alternation; (b) resolve 03 at @1032 to close the clause; evidence gathered
for red-team adjudication"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (a) At least one additional window beyond the known '80-77' x2
   (@720/@1032) is shown to be imperative-80 at battery grade, consistent
   with a single-lexeme mood alternation (infinitive / finite / imperative).
2. (b) 03's role at @1032 is resolved (class at minimum; value if the bytes
   allow) and the full clause "87 01 03 29 80 77 11 70 82 34 29 40 17"
   receives a complete grammatical parse with no ungranted assumption beyond
   the stated provisional values.
3. Adverse honored: no polyvalence declared at battery level (§7; 67 et/veut
   stays the sole true polyvalence). Evidence that bears on it is gathered
   and escalated, not ruled on.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs / 96 types confirmed).
2. Full census of 80 (n=17) with ±3 context; full census of 03 (n=20).
3. Tested every 80 window against imperative diagnostics: (i) enclitic object
   pronoun after the verb (the '80-77' = "[80]-le" pattern); (ii) bare verb in
   clause-initial or post-boundary position; (iii) incompatibility screen of
   80's finite/infinitive slots against a single-lexeme reading.
4. Tested 03 at @1032 via the three "03 29 80" frames (@1030/@1320/@1594) and
   03's global profile; checked standing kills that constrain the clause
   (ce-inf-1841: 'ce'+infinitive kill-grade dead; ci-01-value: 01='ci' killed).
5. Checked standing constraints (§7): banked 11=la, 70=pre, 82=m, 34=i,
   29=er, 40=e, 46=que; granted 87=ce, 96=par, 00=pour, 79=tout, 47=ce;
   promoted 06='ent', 24='faire' (battery-level), 77='le' (provisional).

## Findings — 80's full role inventory (re-derived)

| @ | window | role under single-lexeme hypothesis |
|---|---|---|
| 441 | 43 98 80 50 | "vient [80]" — post-'venir' slot (infinitive or noun) |
| 469 | 33 79 80 06 | "[INF] tout [80]ent" — finite 3pl ('-ent' ending, 06 promoted) |
| 517 | 87 77 80 09 | "ce le [80]" — finite/infinitive verb slot |
| 565 | 43 24 80 97 | "[43] faire [80]" (24='faire') — post-'faire' infinitive slot |
| 663 | 86 50 80 03 | "[80] [03]" |
| 673 | 86 24 80 03 | "faire [80] [03]" — post-'faire' infinitive slot |
| 720 | 02 21 80 77 | "[80]-le" — IMPERATIVE + enclitic 'le' |
| 768 | 66 98 80 10 | "vient [80]" — post-'venir' slot (2nd) |
| 1011 | 18 79 80 78 | "tout [80] [78]" |
| 1032 | 03 29 80 77 | "[03]er [80]-le" — IMPERATIVE + enclitic 'le' |
| 1090 | 33 79 80 06 | "[INF] tout [80]ent" — finite 3pl (2nd, byte-identical frame to @469) |
| 1156 | 92 29 80 17 | "[92]er [80] fois" — bare 80 before 'fois' (17 promoted) |
| 1295 | 94 52 80 04 | "ne [52] [80]" — finite slot after 'ne [52]' |
| 1322 | 03 29 80 08 | "[03]er [80]" — bare 80 after infinitive |
| 1596 | 03 29 80 67 | "[03]er [80] et" — bare 80 before 'et' (67='et': follower 77 not infinitive-shaped, positional rule) |
| 1662 | 98 98 80 22 | "vient [80]" — post-'venir' slot (3rd) |
| 1808 | 94 52 80 04 | "ne [52] [80]" — finite slot (2nd, byte-identical frame to @1295) |

## Clause 1 (grow the imperative set): FAIL as stated

- The enclitic diagnostic ('80-77' = "[80]-le", the only grammatical
  verb+enclitic order among 80's followers) returns exactly n=2
  (@720/@1032). 80's full follower inventory is {50, 06, 09, 97, 03,
  77 x2, 10, 78, 17, 04, 08, 67, 22}: 06='ent' is a finite ending, not an
  enclitic; 03 is a content word (see below — "pas [03]" x3, "[03] qui"
  x4 kill any clitic reading); no other follower is a clitic-shaped group
  with standing. The enclitic imperative set cannot grow beyond n=2 on
  byte count.
- Bare-verb candidates @1156 ("[92]er [80] fois"), @1596 ("[03]er [80]
  et le"), @1322 ("faire [03]er [80]") are imperative-CONSISTENT only with
  an ungranted clause-boundary assumption each (no punctuation survives in
  the cipher; none of the three has an independent boundary marker).
  Not battery-grade. Recorded as evidence, not as growth.

## Clause 2 (resolve 03 at @1032): CLASS-RESOLVED, value open

- "03 29" = infinitive "[03]er" with 03 the VERB STEM. Proof: @1322
  "24 03 29" = "faire [03]er" — causative 'faire' (24='faire',
  battery-promoted, disc-01-24-ci-X) directly followed by the infinitive;
  the same "03 29 80" frame recurs at @1030 and @1594. 03's class at @1032
  is verb stem. Its global value stays open (stem-03 queued).
- Full clause @1028-1038: "87 01 03 29 80 77 11 70 82 34 29 40 17"
  = "ce [01] [03]er [80]-le la première fois"
  (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e GT → "la première";
  17=fois promoted; 77='le' provisional; 87='ce' granted).
- Hard constraints on the parse: (i) ce-inf-1841 killed 'ce'+infinitive at
  kill grade with period-corpus evidence — "03 29" cannot be governed by
  "ce" directly, so 01 must mediate or a boundary must intervene;
  (ii) 01='ci' is killed (ci-01-value) — the queued
  residual-1029-infinitive's "@1029 'ceci [03]er [80]-le'" premise is STALE
  and should be re-briefed; (iii) 01='en' is local to the three 01-24
  windows only (disc-01-24-ci-X), 01='tain' local to 37-01 x3 ("certain",
  rival-37-01-certain) — 01's value at @1029 is OPEN.
- Closest battery-grade close (grammatical skeleton, two open slots):
  "ce [01] — [03]er! [80]-le, la première fois!"
  (exclamatory infinitive + imperative with enclitic 'le', adverbial "la
  première fois"). Open: 01's value ("c'en …" if 'en'; "ce se [03]er" if
  'se' — note 'se' is killed only at 01-24, so conditioned use stays a
  red-team question), 03's stem value.
- Note @720's parallel: "02 21 80 77 03 91" — "[80]-le" followed by 03
  ("[80]-le [03] [91]"), the same two open groups in the same order,
  supporting that 03 is clause-level content, not part of the imperative.

## Clause 3 (adverse): HONORED

No polyvalence declared. But the following is gathered for the red team
because it is the §7 question in miniature:

- 80's roles are morphologically incompatible with ONE French lexeme at
  group granularity: imperative full-form ("80-le" x2, enclitic requires a
  complete imperative form), finite 3pl ("80-ent" x2, stem+'-ent'),
  post-'vient'/'faire' infinitive slot (x5), "ce le [80]" finite slot,
  "ne [52] [80]" finite slot (x2). A single lexeme's imperative, infinitive,
  and 3pl forms never coincide in French; a stem reading of 80 is
  contradicted by "80-le" (enclitics attach to full forms, not bare stems).
  This feeds the queued P1 `poly-80-docket` (verb/determiner split) — no
  duplicate created; this report is cited as new morphological evidence.
- 03's global profile is likewise split: verb stem in "[03]er" x3
  (@1030/@1320/@1594) vs content word in "[03] qui" x4
  (@31/@336/@674/@1645), "pas [03]" x3 (@31/@657/@994), "ce [03] [24]"
  (@1014), "[03]e" (@1237 "03 40"). A monovalent 03 covers at most one
  family. Noted for `stem-03`; not declared.

## Verdict: NULL

(a) fails as stated — the imperative set stands at n=2 on the enclitic
diagnostic, with three mood-consistent but boundary-assumed candidates
(@1156/@1322/@1596) held as evidence. (b) resolves 03's class (verb stem
of "[03]er") and closes the clause skeleton, but 01's value and 03's value
stay open, so the clause is not fully closed. Substantial §7-relevant
evidence gathered for red-team adjudication (80's morphological
incompatibility inventory; 03's split profile; stale "ceci" premise in
residual-1029-infinitive flagged for re-brief).

## Follow-ups proposed (for supervisor queuing)

1. `stem-03-value` (P2) — name 03's verb-stem value using the three
   "[03]er" infinitives (@1030/@1320/@1594); constrain via causative
   "faire [03]er" @1322 and the "80-le" imperative at @1032/@720.
   Coordinates with (does not duplicate) queued `stem-03` (class bar).
2. `ce01-slot-1029` (P2) — discriminate 01's value at @1029 ("c'en" vs
   "ce se" vs clause-boundary) against 01's full 28-window profile;
   'ci' killed, 'en'/'tain' local elsewhere. Closes the last open slot of
   the @1032 clause.
3. `imp-80-bare-1156-1596` (P3) — test the two bare-verb imperative
   candidates (@1156 "[92]er [80] fois", @1596 "[03]er [80] et le") with
   independent clause-boundary evidence; promote either to the imperative
   set iff the boundary is byte-grounded, else fence.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-imp-80-set.md (this file).
- battery-queue.json: `imp-80-set` queued → verdict/null (temp-file +
  rename, own entry only, pre-write assert confirmed no prior verdict;
  JSON re-validated after write).
- Lock created on start (agent id + UTC timestamp), deleted on completion.
- No standing verdict contradicted or downgraded. No second polyvalence
  declared. R5005, sealed gates, red-team queue untouched. canonical.py
  never used; every number re-derived on the repaired 1,847-pair stream.
