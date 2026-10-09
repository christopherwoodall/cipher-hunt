# Battery report: `inf97-526-vs-567`

Date: 2026-10-09. Worker: battery worker (subagent).

## Bar (verbatim, pre-registered)

> "promote noun-97 class iff both windows parse under one noun value with zero ungranted assumptions besides noun-97 itself; else fence. Does not duplicate locked nom-97-526-adverb."

Restated as numbered pass/fail clauses (before testing):

- **C1:** Window 1 (@525 1-based, "[81] [97] ce(47) [44] est(59)") parses under a single noun value V for 97 with zero ungranted assumptions besides "97 is nominal".
- **C2:** Window 2 (@567 1-based, "[80] [97] 13 [76]") parses under the same noun value V with zero ungranted assumptions besides "97 is nominal".
- **C3 (bar verdict):** promote noun-97 class iff C1 AND C2 pass; else fence (NULL).

Index note: the brief's @-offsets are 1-based cell indices. 1-based @526 = 0-based @525 (97); 1-based @567 = 0-based @566 (97).

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session (`repaired_offsets.json` + `upstream-ct_R5005.txt`, parsed like `repair_parse.py`); asserts held (1,847 pairs, 96 types, crib "la premiere" ×2 pair-aligned). `canonical.py` never used.

Windows byte-confirmed:

- **W1** (row a3_00): `... 91 @520 | 77 @521 | 06 @522 | 55 @523 | 81 @524 | 97 @525 | 47 @526 | 44 @527 | 59 @528 | 37 @529 | 64 @530 | 26 @531 | 32 @532`
- **W2** (row a4_00): `... 67 @561 | 11 @562 | 43 @563 | 24 @564 | 80 @565 | 97 @566 | 13 @567 | 76 @568 | 45 @569 | 94 @570 | 52 @571 | 87 @572 | 78 @573`

Standing premises adopted (not re-litigated):

- 47 = 'ce' (promoted, determiner-capable, A4).
- 59 = 'est' (provisional — positional role in the copula frame adopted from `nom-97-526-adverb`).
- 81: nominal at window level @524 (battery PROMOTE, `nom-97-526-adverb`, 2026-10-09); adverbial-81 dead at this window. 81 unvalued in registry. Consistent with R19-123's global noun-81 fence (window-level finding, not a value claim).
- 80: A8 verb-frame (value open); global verb/determiner split red-team venue (`poly-80-docket`).
- 76 = noun, promoted (masculine, R19 upgrade lead→prom).
- 97: class open — INF/NOM tie survives (`frame-97-profile` infinitive promote; `noun-97-568` KILL kept the tie alive; nominal leg hardened by `nom-97-526-adverb`).
- 13: word-final-13 ("s" of "verdicts") killed at the "78 45 13" windows (`letter-13-verdicts` KILL, 2026-10-09); word-internal and §7-split arms unresolved/red-team venue. 13 unvalued in registry.
- 44, 43-followers, 26: unvalued; not load-bearing here.
- §7: 67 sole true polyvalence; R24 (24='en' iff follower=85, else finite/modal) adopted but not load-bearing.
- Canonical-stream caveat stands (rows a3_00/a4_00 offsets unvalidated).

## Findings

**C1 — W1 (@525): PASS (conditional on the bar's allowed assumption).** Under nominal-97, W1 reads "[81-nominal] [97-noun] ce(47) [44] est(59)" — the adopted `nom-97-526-adverb` parse: appositive NP ("[81] [97-noun]") followed by the "ce [44] est [37]"-shaped copula. Any French noun value V for 97 fits this shape structurally (apposition to nominal-81, copula subject position); no further ungranted assumption beyond noun-97 is needed. The "55 81" ×6 collocation and the determiner-position reading of 55 loads on unvalued 55, but the C1 parse as framed needs only 81-nominal (battery-grade at this window) + 47/59 premises. No specific V is forced — naming any one would invent a value (§3); the bar tests class, not value.

**C2 — W2 (@566): FAIL.** W2 reads "[80-verb] [97-noun] 13 [76-noun]". Every licensed parse of this trigram requires 13's class:
- 13 as post-nominal adjective: 13's class open → ungranted assumption.
- 13 as word-final letter ("97s", plural noun): sub-lexical-13 kill was geometry-specific (`letter-13-verdicts` killed the verdict-window reading only); here a word-final reading is unlicensed and would still be an ungranted assumption.
- 13 word-internal / split-13 (§7, red-team venue): ungranted at battery grade.
- 13 attaching rightward to 76: a letter reading — ungranted.

13 is unvalued in the registry; no battery-grade 13 class exists anywhere in the lane. The bar permits only noun-97 itself as an ungranted assumption, so no noun value V — and no reading — can satisfy C2 at battery grade today. This is independent of V's identity: the failure belongs to 13, not 97.

**C3: C1 passes, C2 fails → fence executed (NULL).** The joint class test is undecidable at battery grade because one of the two windows is blocked by 13's open class, not by anything about 97. Nothing about noun-97 is falsified here: the failure is 13's, and the INF/NOM tie survives exactly as before. No standing or red-team verdict is contradicted or downgraded (A8, R19-120/122/123, R24, `frame-97-profile`, `noun-97-568`, `nom-97-526-adverb`, `letter-13-verdicts` all adopted as premises); §7 intact; no polyvalence declared.

## Verdict: NULL

The joint noun-97 class promotion is fenced with stated cause: C2 cannot be satisfied at battery grade under the bar's zero-ungranted-assumptions standard because 13's class at @567 is ungranted and cannot be bypassed. Noun-97 remains a live, evidence-backed tie arm (W1's parse still stands on battery-grade premises).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-13-567` (P3) — name 13's class at @567 ("[97] 13 [76]" window); the direct blocker for this joint test. Bar: post-nominal-adjective / word-final-letter / word-internal, with byte evidence at battery grade; fence if none licensed.
2. `inf97-526-vs-567-rerun` (P4) — gated re-fire of this bar's C2 once 13's class at @567 is named at battery grade or above (or split-13 adjudicated).
3. `nom-97-526-class` (P3) — promote noun-97 from the @525 window alone; W1's parse is unblocked and does not duplicate `nom-97-526-adverb` (which hardened the reading without promoting the class).

## Bookkeeping

- Report: this file.
- Queue: `inf97-526-vs-567` → `status: verdict`, `result: null`, 2026-10-09.
- Lock: created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
