# Battery report: det-pl-544 — plural-determiner hunt for @544's subject

Target: `det-pl-544`. Claim: a plural-determiner subject for @544's '[42]ent' is found, or confirmed absent. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed like `code/side-keyhunt/repair_parse.py`.
Never used `canonical.py`. R5005 untouched. No invented data.
@-offsets are 1-based. Lock `locks/det-pl-544.lock` held for this run only.

Source: subj-42-w3 null (2026-10-08) follow-up #1.

## Bar (verbatim, pre-registered before testing)

"name a grammatical plural subject with determiner, or confirm none exists in-window"

Numbered clauses (fixed before testing):

1. A grammatical plural subject with determiner for @544's "[42]ent" is named
   in-window (determiner + plural noun, agreeing with the 3pl verb).
2. OR: confirmed — no plural-determiner subject exists in-window.

Window: @505-544 (36 pairs of left context, matching the source null's scan).
Right context @545-560 checked for post-verbal subjects; none (inversion
needs a clitic; "@545-547 = ent pour que" continues the subordinate clause).

## Method

Re-derived the full @505-544 span on the repaired stream. Substituted all
banked/granted/provisional/battery-promoted values. Enumerated every
determiner-headed NP in-window. Tested each unknown token for plural-
determiner candidacy against the 91-kill (determiner-before-article is
ungrammatical). Full 91 census (n=21) for the determiner kill and the
word-boundary test. Tested the queue's adverse (12 @540 word-internal) two
ways: 12-left-attached ("91n[44]ere") and 12-word-initial ("n[44]ere").

Standing values used: banked 11=la, 70=pre, 82=m, 29=er, 46=que; granted
87=ce, 64=qui, 00=pour, 47=ce; provisional 59=est, 77=le; battery-promoted
12=n, 48=e, 06=ent (pending ratification).

## Window-level evidence (@-offsets, 1-based)

**Full @505-544 span** (row a3_00/a3_01):
`68 21 67 77 62 94 64 98 65 88 56 87 77 80 09 70 91 77 06 55 81 97 47 44 59 37 64 26 32 16 08 24 82 16 91 12 44 29 48 42`
(@544=42, @545=06='ent', @546=00='pour', @547=46='que').

**Determiner inventory in-window** (every determiner-headed NP is singular):
- @508/@517/@522: 77=le (provisional) — singular masculine. @516-517:
  87-77 = "ce le [80]" (A8 frame, 80 verb). @522-523: 77-06 = "le [06]".
  None plural.
- @516: 87=ce (granted); @527: 47=ce (granted) — singular demonstratives.
  @527-530: "47 44 59 37" = "ce [44] est [37]" — 44 is the SINGULAR subject
  of 'est' here, fencing 44 as the plural subject two clauses later.
- @521/@539: 91 — determiner reading KILLED (see below).
- @540: 12='n' letter (battery-promoted) — cannot be a determiner.
- All other in-window tokens: no determiner-like distribution evidence; no
  token heads a plural NP left of @544.

**91 determiner-kill (re-derived, stream-wide):** 91 n=21. Successors include
91-11 x2 (@1006, @1669) and 91-77 x1 (@521): a plural determiner directly
before an article would be "les la"/"les le" — ungrammatical. 91 cannot be a
(plural) determiner. Its full successor set
{11x2, 77, 53x2, 65x2, 32x2, 67x2, 39, 37, 18, 36, 84, 79, 85, 51, 61, 12x1}
is word-initial tokens — 91 is word-final, an independent word.

**The only subject-adjacent NP (@539-543):** "91 12 44 29 48". 91 is not a
determiner (kill above); 12 is a letter, not a determiner. So even if
44-29-48 were plural-marked (it is not: no -s; the '-ere' suffixing is hapax
— 29-48 x1 and 44-29 x1 stream-wide — and gender-blocked per subj-42-w3),
there is no determiner before it. A bare "-eres" noun as subject is
ungrammatical in French.

**Rival plural-subject check:** the relative pronoun 64=qui @531 is the only
plural-capable subject candidate in reach — but 'qui' is a pronoun, not a
determiner-headed NP, so it is outside this bar (queued separately as
subj-42-qui).

## Per-clause pass/fail

- Clause 1 (name a grammatical plural subject with determiner): FAIL. No
  plural determiner exists in-window: the three determiner values present
  (77, 87, 47) are all singular; 91's determiner reading is killed by
  91-11 x2 / 91-77 x1; 12 is a letter. The nearest NP ("91 12 44 29 48")
  has no determiner and no plural marking.
- Clause 2 (confirm none exists in-window): PASS. Every determiner-headed NP
  in @505-544 is singular; the 91 and 12 determiner hypotheses are
  independently killed; no unknown token patterns as a plural determiner
  in-window.

## Adverses

The queue's adverse — "test whether 12 @540 can be word-internal
('n[44]ere' one-word parse)" — is ANSWERED, two ways:

(a) 12 left-attached ("91n[44]ere" one word): REJECTED. 91 is word-final —
    91-11 x2 and 91-77 x1 establish a word boundary after 91, and 91's
    21 successors are all word-initial tokens (the single 91-12 @539 is a
    hapax). 91 never precedes any other letter {48, 40, 34, 82} in 21
    windows, so a mid-word "91n" composition is an unsupported special
    plea. Boundary is 91|12.
(b) 12 word-initial ("n[44]ere" one word): COMPATIBLE — 12='n' opens the
    word "n[44]ere" (or proclitic "n'" before a vowel-initial 44). This
    parse is allowed but changes nothing for the bar: the word before it
    is 91, which is not a determiner.

The other 12-44 window (@1583: "53 12 44 00 36") is noted; it does not
decide the boundary either way and is not needed.

## Verdict

**promote** — via the confirm-absence disjunct (precedent: orphan-1502
promoted on a confirm-negative bar). Clause 2 passes: no plural-determiner
subject exists in @505-544; the 91-determiner and 12-determiner hypotheses
are killed with stream-wide evidence; the adverse is answered (91|12
boundary established, "n[44]ere" one-word parse allowed but
determiner-free). The claim "found, or confirmed absent" is satisfied by
confirmed absence.

Caveats: 06='ent' and 12='n' are battery-promoted pending ratification;
77='le' and 59='est' are provisional; the canonicality caveat stands. No
standing red-team verdict is contradicted (42's value open, A1 frame grant
untouched, 91's value open). Nothing needs escalation. The 3pl subject of
"[42]ent" remains open — subj-42-qui ('qui' @531) and gender-44 are the live
follow-on targets, both already queued.
