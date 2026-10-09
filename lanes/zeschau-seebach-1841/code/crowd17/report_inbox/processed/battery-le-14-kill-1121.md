# Battery report: le-14-kill-1121 — 14='le' against its strongest breaker @1121

Worker: a47b8538-7f99-46cb-859b-3d3360b7b033 | 2026-10-09T02:20:00Z–02:3xZ
Target: `le-14-kill-1121` (priority 2). Lock `locks/le-14-kill-1121.lock` created
on start, deleted on completion. No prior lock existed. Sibling workers
`souvent-14-06-retest` and `prennent-70-12-06` hold live locks — running in
parallel; no duplication (their bars are @84 and the left edge, not this bar).

## Bar (verbatim, pre-registered before testing)

"demonstrate a grammatical '...ent le ent...' parse at @1121, or kill 14='le'
at kill grade at this window"

Numbered clauses (fixed before testing):
- C1: A grammatical '...ent le ent...' parse exists at @1121 with 14='le'.
  PASS iff a full local-window parse is stated, grammatical under standing
  values + 14='le', with no ungranted assumption.
- C2: 14='le' is killed at kill grade at this window — every segmentation of
  the @1121 window with 14='le' is ungrammatical on closed grounds (no
  dependence on open values 88, 37, 52, 43, 86). PASS iff the enumeration is
  exhaustive and each branch dies without an open-value load.
- C3: Adverses adjudicated — the homophony-escalation condition ('le' dead
  here AND 'souvent' holds at @84) is resolved or its pending leg named;
  escalation issued or deferred with stated cause.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
(1,847 pairs, 96 distinct — re-verified this run). `canonical.py` never used.
R5005 untouched. @-offsets are 0-indexed pair positions. Standing values:
11=la (pencil), 70=pre, 12=n (banked), 06=ent (promoted), 00=pour (promoted),
77=le (provisional), 59=est (provisional). breaker-b4-1121 (null, 2026-10-08)
is cited as a premise, not re-litigated: its window facts were re-derived
below and match exactly.

## Window evidence (@1121, row a6_07, row-relative 8 of 20)

Surface @1114–1132 (re-derived):
`30 69 | 11 88 70 12 06 | 14 | 06 11 52 37 43 00 86 52 37 86 | 24`
[30] [69] la [88] pre n ent [14] ent la [52] [37] [43] pour [86] [52] [37] [86] [24-verb]

Distributional facts (re-derived, match breaker-b4-1121 exactly):
- n(14)=15; positions 72, 84, 117, 141, 178, 339, 424, 458, 586, 623, 813,
  896, 1121, 1365, 1689.
- "06 14 06" trigram: UNIQUE to @1121 on the whole 1,847-pair stream.
- "14 06" bigram: exactly 2 — @84 and @1121.
- Row a6_07 spans pairs 1113–1132; @1121 is mid-row (no boundary within 5
  pairs either side) — no row-boundary rescue available.

## Parse enumeration with 14='le' (C2's exhaustive test)

Span under test @1118–1124: `70 12 06 14 06 11` = "pre n ent le ent la".

1. 14='le' word-initial, standalone word, "…ent le ent…":
   - As article: "le" before a vowel-initial 'ent'-syllable word, unelided.
     French elision le→l' before vowels is categorical in 1841 diplomatic
     French; every 'ent'-initial French word (entier, entre, entrée,
     entretien, enthousiasme, entremise…) is vowel-initial. "le ent" is
     ungrammatical regardless of 37's value. DEAD on closed grounds.
     (Note: if the scribe meant "l'ent", the claim would be 14='l\u2019',
     not the tested 14='le'.)
   - As object pronoun: postposed after finite "prennent" ("…prennent le
     ent…"). French object pronouns are preverbal outside the affirmative
     imperative; "prennent" is not the 2pl imperative form ("prenez").
     DEAD on closed grounds.
2. 14='le' word-internal: "leent" (le+ent) or "entle" (ent+le) — no French
   word. DEAD.
3. 14='le' word-final after 06@1120: "…entle" — non-word. DEAD.
4. Clause boundaries at 06@1120|14, 14|06@1122, 06@1122|11@1123:
   - "…ent | le ent…": clause-initial "le" cannot be subject; "le ent"
     re-hits the elision defect (branch 1).
   - "…ent le | ent la…": left strand is verb + postposed pronoun (branch 1);
     right strand "ent la" is a non-word.
   - "…ent le ent | la…": the "ent le ent" unit must still parse — branch 1.
   All DEAD; and no row boundary exists here anyway (mid-row a6_07).

No branch depends on 88, 37, 52, 43, or 86. The rival parse
"…prennent souvent la…" (14="sou" window-local, breaker-b4-1121) IS
grammatical with zero ungranted assumptions — so this window is resolvable
and the kill is specific to 14='le', not an artifact of an unparseable
window. (14="sou" is killed as a GLOBAL value by that same report; the
window-local value question is separate and not this bar.)

## Per-clause pass/fail

- C1 (grammatical '...ent le ent...' parse with 14='le'): FAIL. No branch of
  the enumeration parses.
- C2 (kill 14='le' at kill grade at this window): PASS. The enumeration is
  exhaustive over segmentations and boundary placements; every branch dies
  on closed French-grammar grounds (elision rule, pronoun word order, word
  inventory) with no open-value load. A uniform global 14='le' must parse at
  every window; @1121 forces it false.
- C3 (adverses): ESCALATION ARMED, CONDITIONAL. 'le' died here (C2). The
  second conjunct — "'souvent' holds at @84" — is pending:
  `souvent-14-06-retest` still holds a live lock (running in parallel).
  If it promotes, the supervisor escalates 14-homophony to the red team.
  Battery declares nothing; homophony (beyond 67 et/veut, the sole true
  polyvalence per §7) is a red-team act.

## Verdict

**kill.** 14='le' is killed as a window-independent (global) value at @1121
at kill grade. No standing red-team verdict is contradicted (no red-team
ruling touches 14; 06='ent' was used as a premise; 77='le' provisional is
untouched). Consequence: the 14~77 'le'-homophony battery that tout-slot-14
flagged as conditional on a 14='le' promotion is now MOOT. The surviving
'le' legs at @72 ('ce le [verb]', A8 frame), @117 ('et le [21]'), and @178
(clitic leg) are now evidence for a homophony question, not a global value —
folded into the armed C3 escalation.

## Follow-ups

None mandatory for a kill (§4). One conditional note for the supervisor
(not a new target): if `souvent-14-06-retest` promotes 14="sou"-window-local
at @84, queue a red-team escalation target on 14-homophony (14='le' legs at
@72/@117/@178 vs 14≠'le' at @1121 vs 14="sou" window-local at @84/@1121).
