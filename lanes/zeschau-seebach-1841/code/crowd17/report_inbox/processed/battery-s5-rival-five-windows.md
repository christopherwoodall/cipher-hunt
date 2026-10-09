# Battery report — s5-rival-five-windows

- Target: `s5-rival-five-windows` (priority 2)
- Worker: 5ddc3572-3580-4689-aacc-a439d9581d60
- Date: 2026-10-08 (UTC 2026-10-09T01:51:37Z start)
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`).
  `canonical.py` never used. R5005 untouched.
- Lock: `code/crowd17/next-token/locks/s5-rival-five-windows.lock` created on
  start, deleted on completion. No stale lock existed.

## Bar (verbatim, pre-registered)

> promote-rival iff ONE value parses all five windows (@51, @1655, @529, @1357,
> @1444) grammatically using only banked/promoted neighbors (11=la, 64=qui,
> 79='tout', 47='ce'), with zero contradiction; else fence for red-team
> adjudication

## Bar restated as numbered pass/fail clauses (fixed before testing, unmodified after)

- **C1.** There exists a single value V for 37 such that "tout V" parses
  grammatically at @51 (79='tout' immediately left of 37).
- **C2.** The same V makes "V la" parse grammatically at @51 and @1655
  (11='la' immediately right of 37 in both).
- **C3.** The same V makes "V qui" parse grammatically at @529, @1357, and
  @1444 (64='qui' immediately right of 37 in all three).
- **C4.** All five windows parse with zero contradiction using only
  banked/promoted neighbors (11=la, 64=qui, 79='tout', 47='ce'): no extra
  value assumptions, no second polyvalence (§7: 67 et/veut is the sole true
  polyvalence).
- **Verdict rule.** promote-rival iff C1 ∧ C2 ∧ C3 ∧ C4 all pass; otherwise
  fence for red-team adjudication (null). The bar defines no kill branch.

## Method

1. Rebuilt the repaired stream in-memory (1,847 pairs; 28 occurrences of 37;
   positions verified: 51, 183, 278, 312, 385, 414, 475, 529, 620, 625, 676,
   778, 796, 885, 913, 939, 1125, 1130, 1179, 1301, 1357, 1444, 1633, 1655,
   1723, 1770, 1797, 1817).
2. Confirmed the five S5 windows are exactly the 37-11 bigrams (@51, @1655)
   and 37-64 bigrams (@529, @1357, @1444). No other 37-11 or 37-64 bigrams
   exist in the stream.
3. Screened every French lexical family that can follow "tout" (C1) against
   C2 ("V la") and C3 ("V qui") as local bigrams, then checked each full
   window for V-independent contradictions.

## Window-level evidence (@-offsets, repaired stream)

| @ | row | −2 −1 **[37]** +1 +2 +3 | key anchors |
|---|-----|------------------------|-------------|
| 51 | a1_01 | 92 79 **[37]** 11 79 85 | 79='tout' left; 11='la' right; **11 79 = "la tout" @52–53** |
| 1655 | a8_04 | 01 56 **[37]** 11 24 48 | 11='la' right |
| 529 | a3_00 | 44 59 **[37]** 64 26 32 | 64='qui' right |
| 1357 | a7_05 | 06 52 **[37]** 64 35 13 | 64='qui' right |
| 1444 | a7_09 | 68 59 **[37]** 64 77 84 | 64='qui' right |

Banked/promoted values used: 11=la, 64=qui, 79='tout' (§7). 47='ce' does not
sit adjacent to 37 in any of the five windows (nearest: @1659, @526).

## Findings

**F1 — @51 contains a V-independent kill-grade bigram.** Pairs @52–53 are
"11 79" = "la tout" under banked values (11=la from the "la première" crib;
79='tout' A5-banked). "la tout" is ungrammatical in French on every parse:

- article "la" (fem.) + adjective "tout" (masc.): gender clash — feminine
  requires "toute";
- article "la" + pronoun/noun/adverb "tout": *"la tout" is not a French
  constituent ("le tout" as noun is masculine; bare *"la tout" impossible);
- clitic "la" + "tout" + verb-stem (85): the only licit clitic–tout–verb
  pattern is "l'a tout mangé" (auxiliary between clitic and "tout"); bare
  "la tout <stem>" has no French parse;
- clause boundary "la | tout": "la" must complete a constituent — as article
  it needs a noun (next token is masculine "tout": clash); as enclitic it
  needs an imperative verb to its left, which forces 37=imperative AND a
  second boundary after 79 ("…tout. V-la! Tout 85…"). That reading abandons
  C1's "tout V" bigram, stacks 2–3 clause boundaries inside five tokens, and
  leans on 49=92 (a killed 09/92 "-ère"-split member) to end a clause cleanly.
  It is special pleading, not a zero-contradiction parse — C4 fails regardless.

Because "la tout" @52–53 does not involve 37 at all, **no value of 37 can make
@51 parse grammatically**. The bar's promote branch is unachievable as written.

**F2 — family screen: no lexical family passes C1∧C2∧C3 jointly, even ignoring
F1.** Families that can follow "tout" (C1):

- noun ("tout homme"): C2 "N la" ✗ kill-grade; C3 "N qui" ✓ (antecedent).
- adjective/adverb ("tout petit", "tout doucement"): C2 ✗; C3 ✗.
- infinitive verb ("tout savoir"): C1 ✓; C2 "V-inf la" ✗-incomplete — "la"
  as article needs a feminine noun (none among allowed neighbors; @51's next
  token is the clashing "tout"); as enclitic it is ungrammatical after an
  infinitive (proclitic "la V" is the order); C3 "V-inf qui" marginal-✓ only
  ("savoir qui?" — interrogative object needs a following clause, absent
  among allowed neighbors).
- "ce" ("tout ce"): C1 ✓; C2 "ce la" ✗ kill-grade.

The transitive-verb family is the closest rival (passes C1, marginal C3) but
dies on C2 — and @51's "la tout" kills it independently of family.

**F3 — distributional context (for follow-ups, no value declared).** 37 has
28 occurrences. Followers: 78×4, 43×3, 64×3, 01×3, 11×2, 77×2, 08×2, others
×1. Predecessors: 59×6, 52×4, 64×3, 24×2, 56×2, 79×1, others ×1. The five S5
windows (followers la/qui = 5/28) are a minority pattern, not the dominant
one. 37-01 bigrams exist at @939, @1633, @1817 (A12 37-01 unit frame — not
examined here, per target evidence note).

**Adverses.** S5 standing fence (37='le' MEDIUM, round-7): this battery does
not re-litigate 37='le' and declares no polyvalence (§7). Result (fence for
red-team adjudication) is consistent with the standing fence, not a
contradiction of it — no escalation-override needed, but the F1 "la tout"
anomaly is flagged for the red team since it touches banked 79@53 / the
a1_01 segmentation.

## Per-clause pass/fail

- C1 ("tout V" @51): CONDITIONAL PASS — satisfiable only by verb/"ce"
  families, which then fail C2.
- C2 ("V la" @51, @1655): **FAIL, kill grade** — @51's "V la tout" contains
  the V-independent "la tout" clash; elsewhere "V la" is incomplete (article
  + absent noun) or ungrammatical (clitic order) for every C1-passing family.
- C3 ("V qui" @529/@1357/@1444): CONDITIONAL PASS — only for noun (fails
  C1/C2) or transitive-verb + interrogative-"qui" (fails C2) readings.
- C4 (zero contradiction, banked/promoted neighbors only): **FAIL** — "la
  tout" @52–53 contradicts every parse; the boundary-stacked rescue needs
  imperative mood + multiple clause boundaries not in evidence.

## Verdict: NULL — fence for red-team adjudication

No single rival value parses all five windows grammatically with zero
contradiction. Headline for the red team: **the bar is unachievable as
written because @51's "la tout" bigram (@52–53) is kill-grade ungrammatical
under banked values independent of 37's value** — either 79@53's banking,
the a1_01 segmentation at @52–53, or the five-window framing needs
adjudication before any rival value for 37 can be promoted. This battery
declares no polyvalence and does not decide the S5 question (§7).

## Follow-up targets (null regenerates work)

### FU1 — s5-la-tout-adjudicate (priority 1)
- claim: resolve the V-independent "la tout" clash at @52–53 (row a1_01):
  determine whether 79@53's 'tout' banking, the repaired a1_01 segmentation,
  or a principled boundary/ellipsis analysis accounts for "11 79" adjacency;
  if none does, the five-window bar cannot be satisfied by any 37 value.
- bars: pass iff "la tout" @52–53 is shown grammatical under banked values
  with a stated, non-ad-hoc analysis, or 79@53 / the segmentation is
  corrected with evidence; else fence with the contradiction documented for
  the red team.
- adverses: S5 standing fence; banked values (11=la, 79='tout') are not
  re-litigated at battery level — fence, never decide (§7).
- evidence: this report, F1; window table @51 row above; repaired stream
  pairs @50–54 = 79 37 11 79 85.

### FU2 — s5-verb-rival-four-windows (priority 2)
- claim: test the transitive-verb rival family for 37 on the four windows
  excluding @51's "la tout" tail — "tout V-inf" (@51), "V la" (@1655),
  "V qui" as interrogative-object or relative (@529/@1357/@1444) — and
  determine whether one verb form satisfies all four bigrams.
- bars: promote-rival iff ONE verb form parses "tout V" (@51), "V la" with
  la=article+noun (noun source stated) or licit clitic (@1655), and "V qui"
  (@529/@1357/@1444) with zero contradiction on banked/promoted neighbors
  only; else fence.
- adverses: S5 standing fence (37='le' MEDIUM, round-7); no polyvalence
  declared at battery level (§7); FU1's "la tout" question stays open and
  bounds any promotion.
- evidence: this report, F2 family screen; 37-11 bigrams @51/@1655, 37-64
  bigrams @529/@1357/@1444.

### FU3 — s5-37-distributional-profile (priority 3)
- claim: publish the full 28-occurrence neighbor profile of 37 (followers:
  78×4, 43×3, 64×3, 01×3, 11×2, 77×2, 08×2, 06/61/76/33/44/03/96/86/91×1;
  predecessors: 59×6, 52×4, 64×3, 24×2, 56×2, 79/23/91/38/51/88/73/68/70/26/
  29×1) to bound the rival-value search space; check whether the S5 windows
  (la/qui followers, 5/28) are representative or outliers, and examine the
  unexamined 37-01 bigrams @939/@1633/@1817 against the A12 37-01 unit grant.
- bars: pass = complete, stream-traced neighbor table for all 28
  occurrences plus a representativeness judgment for the five S5 windows;
  no value declared at battery level.
- adverses: 1690 frequency uniformity necessary-not-sufficient (§7);
  distributional evidence never promotes alone.
- evidence: this report, F3; repaired-stream 37 positions list above.
