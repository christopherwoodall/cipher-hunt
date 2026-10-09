# Battery report: nece-94-87-initial

Target: `nece-94-87-initial`. Claim: 94-87 is word-initial 'nece-' (necessaire/necessite family) at @1169.
Date: 2026-10-08. Worker: 3bcd1f23-e550-4ffe-9fbc-0ef4b35f5ab1 (battery worker).
Lock `locks/nece-94-87-initial.lock` created 2026-10-09T02:36:38Z (no stale lock); deleted on completion.

## Bar (verbatim from battery-queue.json)

"(a) profile 83's successors for 'ss'-shaped continuations of 'necessaire/necessite'; (b) parse '... [13-55-61] necessaire [83 ...]' at @1164-1173 with stated agreement and frame; (c) do not disturb the 87='ce' grant (syllabic reading only)."

## Bar as numbered clauses

1. 83's successor profile contains 'ss'-shaped continuations compatible with 'nécessaire'/'nécessité' (i.e. a vowel/'a'-initial continuation after 'ss').
2. The window @1164–1173 parses as '... [13-55-61] nécessaire [83 ...]' with stated agreement and frame.
3. The 87='ce' grant is undisturbed (syllabic 'ce' reading only).

## Method

Re-derived everything from the repaired 1,847-pair stream (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` never touched. R5005, sealed gates, and the red-team adjudication queue untouched. 1841 diplomatic French only.

Window @1164–1173 (row a6_09/a6_10 boundary): `78 45 13 55 61 94 87 83 21 85`.

## Window-level evidence

- **94-87 bigram**: stream-unique at @1169 (1/1847). Confirmed on repaired stream.
- **94-87-83 trigram**: stream-unique at @1169. The 'néce-' onset exists nowhere else.
- **83 census**: n=15. Followers: 82 x3, 21 x3, 86 x2, 70/54/59/56/92/71/24 x1. Predecessors: 98 x5, 87 x2, 55 x2, 44 x2, 64/77/39/38 x1.
- **83 windows** (context ±2): @228 `46 98 83 82 96`, @614 `77 87 83 70 88`, @898 `14 98 83 86 16`, @907 `18 55 83 54 49`, @911 `49 64 83 59 37`, @931 `82 98 83 56 69`, @1061 `09 98 83 82 96`, @1161 `82 44 83 21 67`, @1171 `94 87 83 21 85`, @1217 `36 77 83 92 61`, @1334 `52 39 83 86 71`, @1612 `08 55 83 71 48`, @1784 `23 98 83 82 96`, @1829 `82 38 83 24 82`, @1840 `42 44 83 21 67`.
- **21**: matrix registry `cells/21 = ["noun", "cls"]` — noun class stands (never-downgrade).
- **83 'de' lead**: held per R17; the 98-83-82-96 trigram x3 (@228, @1061, @1784) is the "vient de me parvenir" formula candidate (98='vient' battery-promoted; parvenir-thirds finder ran an 83='de' cross-check).
- **French lexicon**: the only 'néce'-initial words are the 'nécess-' family (nécessaire, nécessité, nécessiter, nécessairement, nécessiteux). Every one continues 'néce' with 'ss' + vowel ('-aire', '-ité', '-iter', ...). No French word ends at 'néce'.

## Per-clause pass/fail

**Clause (a): FAIL.** No 'ss'-shaped continuation exists in 83's successor profile. The continuations of 'ss' in the 'nécess-' family are vowel-initial ('-aire', '-ité'). 83's followers with known values: 82='m' x3 ('ssm' — impossible French syllable sequence), 21=NOUN x3 (not a suffix), 86=INF-class x2, 70='pre', 59='est' provisional, 24=finite verb. None is 'a'-initial. Open followers (54, 56, 92, 71) cannot rescue the clause: the local window's successor @1172=21 is noun-classed and cannot be '-aire'/'-ité'. A global 83='ss' value is additionally rejected distributionally ('ssm' x3).

**Clause (b): FAIL.** No grammatical parse of 'nécessaire'/'nécessité' is constructible at @1164–1173:
- Segmentation 94-87='néce', 83='ss', 21=suffix fails: 21 is noun-classed (standing matrix cell), and '-aire'/'-ité'/'-re' are not nouns.
- Segmentation 83='ssaire' (word complete at @1171, 21 a new word) fails globally: @228 `46 98 83 82 96` would read 'que vient nécessaire me par' — ungrammatical; @898 'vient nécessaire' likewise. Positional 'ssaire'-only-at-@1171 would be a second 83 value, barred by the §7 sole-polyvalence law (67 et/veut is the sole polyvalence).
- The frame's head '[13-55-61]' cannot be named: dict-frame-78-45-13-55-61 nulled 13-55-61 as one unit, so agreement (gender vacuous for epicene 'nécessaire'; number conditional) cannot be stated.
- 83='ss' at @1171 would additionally break the standing 83='de' lead in the 98-83-82-96 formula (R17; parvenir-thirds cross-check).

**Clause (c): PASS (vacuous).** The parse fails before the grant is at issue; nothing in this battery disturbs 87='ce' (the syllabic 'ce' reading was never reached).

## Adverses

- **83's value open**: remains open. 'ss' rejected distributionally (cause stated above); 'de' lead (R17) stands unchallenged.
- **Agreement/frame unchecked**: remains unchecked — follows from clause (b) failure; the frame cannot be built.
- **§7 sole-polyvalence**: satisfied. 94='né' is accent-insensitive 'ne' (R17-001 94='ne' STRONG LEAD covers it); no second 94 value was declared or needed.

## Verdict: KILL

Bar clauses (a) and (b) fail at kill grade: the distributional test on 83's successors rejects 'ss' at the lane's standard ('ssm' x3, zero 'a'-initial followers), and the @1169–1172 window forces the claim false — no 'néce'-family word can complete without contradicting the standing 21=NOUN cell. This kills only the word-initial 'néce-' rescue (rescue-2 of ne-ce-1169 null). It does not disturb 94='ne' STRONG LEAD (R17-001), the 87='ce' grant, or 21=NOUN.

## Caveats

- 21=NOUN is a battery-level promotion (unratified). If the red team re-values 21, @1169–1172 should be re-examined.
- 98='vient' is battery-level (unratified); the 83='de' lead is R17-held, not a verdict.

## Follow-ups

None newly proposed. Rescue-1 from the ne-ce-1169 null (61-94 as word-final 'ne', prenne/donne family) is already queued as `seg-61-94-word` — this kill leaves it as the surviving hypothesis for @1169.
