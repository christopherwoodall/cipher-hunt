# Battery report: antecedent-44-l-prime — verdict: NULL (fence executed)

**Target:** `antecedent-44-l-prime` (priority 3). Worker session 9b94126d-b2b2-404c-bb9c-aa34d3464de5 (supervisor-dispatched). Date: 2026-10-09.
**Stream:** repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types, asserts hold). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. No data invented.
**Lock:** `code/crowd17/next-token/locks/antecedent-44-l-prime.lock` created on start (UTC timestamp written), deleted on completion.
**Offset convention:** 0-based stream indices (queue convention, matching the bar's @1640–1711/@1712 as used by the parent discriminator battery). Key 1-based lane equivalents given.

## Bar (verbatim from battery-queue.json — pre-registered BEFORE testing)

"resolve iff a predicative adjective or noun antecedent for l' is identified within the @1712 clause or the @1640-1711 discourse with byte offsets, else fence l' as discourse-anaphoric (antecedent outside the scanned window)"

## Bar as numbered pass/fail clauses (frozen before testing; not modified after seeing data)

1. **C1 (resolve arm):** a predicative adjective or noun antecedent for l' (44 at 0b1714 / 1-based @1715) is identified — with byte offsets — either (a) within the @1712 clause (the clause containing 0b1712=65, row a8_06: `40 65 94 44 59 30 64 47 68 …`), or (b) within the 0b1640–1711 discourse.
2. **C2 (fence arm):** if C1 fails, fence l' as discourse-anaphoric: the antecedent lies outside the scanned window.

## Method

1. Read `BATTERY-PROTOCOL.md` in full. Read the parent battery `battery-clitic-44-65-discriminator.md` (processed/, PROMOTE 2026-10-08) and its evidence note: "none identified in @1640-1711". Read `battery-val-44-1712-pronoun.md` (PROMOTE 2026-10-09: 44='l'' window-local at 0b1714; the frame is anaphoric, semantically empty for 65) and `battery-clitic-44-census.md` (PROMOTE 2026-10-09: 0b1714 is 44's sole clitic-slot window).
2. Re-derived the repaired stream in-session (1,847 pairs / 96 types, byte-exact). Re-derived the forcing window: 0b1711=40, 0b1712=65, 0b1713=94, 0b1714=44, 0b1715=59, 0b1716=30, 0b1717=64 (row a8_06) = "[40] [65-noun] ne l' est pas qui …" (1-based @1712–@1718).
3. Standing values used as granted, never re-litigated (per adverses): 94='ne' (battery-promoted), 59='est' (provisional), 30='pas' (battery-promoted), 65=noun-class (R18-001, value unnamed per adverse), 64='qui', 47='ce' (A4), 12='n', 06='ent', 40='e', 29='er' (letter grants), A1 predicative frames 37/32/42 (value open).
4. Exhaustive candidate sweep: every token in 0b1640–1711 plus the full @1712 clause (0b1708–1725, a8_06 tail + a8_07 head) was tested against the antecedent shape — must be (i) an adjective or noun, (ii) in a predicative frame (copular predication or equivalent), (iii) byte-offset identified. Adjective/noun-class standing data consulted per candidate (adj-91 batteries, noun26-38-profile, est-59-frame-census, fem32e batteries).

## Window-level evidence (all @-offsets 0-based, re-derived)

**The forcing clause (row a8_06 → a8_07):**
- 0b1708–1718 (1b1709–1719): `12 06 29 40 65 94 44 59 30 64 47` = "n entere [65] ne l' est pas qui ce" — wait, 0b1719 is a8_07's first token (68). a8_06 = 0b1693–1718: `24 85 58 15 23 91 85 33 94 30 20 62 94 88 26 12 06 29 40 65 94 44 59 30 64 47`.
- 0b1719–1725 (a8_07 head): `68 06 11 52 37 43` = "[68] [06] la [52] [37] [43]" (relative clause "qui ce …" continues).

**Discourse structural facts (decisive):**
- **Zero 59 ('est') in 0b1640–1712** (full-scan verified). There is no explicit copular predication anywhere in the 72-token discourse preceding the forcing window.
- **Exactly one A1-frame token in 0b1640–1711: 37 at 0b1655** (1b1656), context 0b1652–1658 = `16 01 56 37 11 24 48`. No 32, no 42 in the discourse.

**Candidate-by-candidate adjudication (discourse 0b1640–1711):**

| # | Token | 0b (1b) | Context | Predicative? | Verdict |
|---|---|---|---|---|---|
| 1 | 37 | 1655 (1656) | `16 01 56 37 11 24 48` | A1 frame granted but no copula in discourse; 37's class/value unidentified; "56 37 11" is not a predication frame | FAIL — not identifiable as predicative |
| 2 | 38 | 1650 (1651) | `03 38 82` | 38 = verb-form class-level (battery-noun26-38-profile PROMOTE, adopted) — not adjective/noun | FAIL — wrong class |
| 3 | 91 | 1668 (1669) | `64 06 91 11 78` | adj-91-723-second-leg NULL: @1668 (0b) explicitly "none adjective-shaped" — 91 in head position, not modifier | FAIL — not adjective-shaped here |
| 4 | 91 | 1698 (1699) | `23 91 85 33` | same battery: @1698 "91 before granted verb stem [85]" — not adjective-shaped; adverb arm possible but unpredicated | FAIL — not predicative |
| 5 | 78 | 1670 (1671) | `91 11 78` | value open ("78+45=verdict" killed); "la [78]" nominal-shaped, no predication | FAIL |
| 6 | 74 | 1677 (1678) | `03 39 74` | class fenced open (noun-74-census NULL); "[03] à [74]" — no predication | FAIL |
| 7 | 60 | 1644/1674/1690 | various | verb-class (battery-grade) — wrong class | FAIL |
| 8 | 92 | 1673 (1674) | `55 81 92 60` | verb-class — wrong class | FAIL |
| 9 | 88 | 1705 (1706) | `62 94 88 26` | verb-class (prof-88 PROMOTE 2026-10-09: "il ne [88-verb]") — wrong class | FAIL |
| 10 | 98 | 1643/1659/1660 | various | 'vient' finite verb — wrong class | FAIL |
| 11 | 65 | 1683 (1684) | `79 65 13 93` = "tout 65 [13]" | 65 noun-class but 13's class unidentified (red-team docket: 13 leftward nominal-closing); no copula — "tout 65 [13]" is not a predication frame | FAIL — antecedent not identifiable |
| 12 | 33 | 1642/1700 | `12 33 98`, `85 33 94` | class unknown; no predication frame | FAIL |
| 13 | 56 | 1640/1654 | `56 12 33`, `01 56 37` | noun/verb split is red-team venue; no predication frame | FAIL |
| 14 | "29 40" | 1710–1711 (1711–1712) | `12 06 29 40 65` = "n entere [65]" (F-post-ere frame, "29 40 65" x3 stream-wide) | syllable pair "er"+"e"; value unknown; no copula; cannot be identified as a predicative adjective/noun — nearest unexamined in-clause candidate, but unidentified | FAIL (flagged for follow-up 2) |
| 15 | 26 | 1706 (1707) | `94 88 26 12` | unknown; object-of-verb position, not predicative | FAIL |

**Candidate-by-candidate adjudication (the @1712 clause, right context 0b1717–1725):**
| # | Token | 0b (1b) | Context | Verdict |
|---|---|---|---|---|
| 16 | 37 | 1723 (1724) | `11 52 37 43` inside "qui ce …" relative | A1 frame but no copula; unidentified — FAIL |
| 17 | 52 | 1722 (1723) | `11 52 37` | adjective/adverb split (red-team venue); no predication — FAIL |
| 18 | 65 | 1712 (1713) | subject of "ne l'est pas" | subject ≠ antecedent; value unnamed per adverse — excluded |

**Out-of-scope characterization (for the follow-up, not this bar):** the nearest predicative-59 frames before the window are 0b1443 (`52 68 59 37`, 271 tokens back) and 0b1448 (`77 84 59 36`), and the nearest subject-65 copular predication is 0b1207–1212 (`21 65 64 59 32 48` = "[21] 65 qui est 32e", 507 tokens back — feminine "32e" predicated of 65 itself, which would make l'="32e" a same-subject contradiction unless the intervening discourse licenses the contrast).

## Per-clause pass/fail

- **C1 (resolve arm): FAIL.** 18 candidates examined across the discourse and the clause; every one fails on class (2, 7, 8, 9, 10), on frame (1, 3, 4, 5, 6, 11, 12, 13, 15, 16, 17), on the adverse (18), or on identifiability (14). No predicative adjective or noun antecedent is identified with byte offsets in scope. In particular: no copula exists in the 72-token discourse (zero 59 in 0b1640–1712), so no explicit predication is available to anchor l'.
- **C2 (fence arm): EXECUTED.** l' at 0b1714 is fenced as **discourse-anaphoric**: its predicative antecedent lies outside the scanned window (before 0b1640 or in an unparsed predication). This is consistent with — and sharpens — the parent discriminator's fenced caveat and val-44-1712-pronoun's "anaphoric, semantically empty for 65" finding.

## Adverses (answered, none ignored)

- "do not re-litigate 94/59/30": HONORED — used as granted throughout (94='ne', 59='est', 30='pas'); no re-argument.
- "65's value stays unnamed": HONORED — only 65's R18 noun-class used; candidate 18 (65-as-antecedent) excluded on this ground.

## Verdict: NULL (fence executed)

No standing or red-team verdict contradicted or downgraded. §7 intact (no polyvalence declared; 44='l'' remains window-local per the discriminator). `canonical.py` never used; R5005, sealed gates, red-team queue untouched.

## Follow-ups proposed (null mandate; all verified absent from battery-queue.json)

1. **`antecedent-44-wider-discourse`** (P3): scan 0b0–1639 for predicative "est"-frames ("59 37/32/42", "59 36/35/38/39/30"); adjudicate the two known out-of-scope candidates — 0b1207–1212 "65 qui est 32e" (same-subject contradiction analysis: does the 0b1213–1639 discourse license "65 ne l'est pas" after "65 est 32e"?) and 0b1443 "59 37" / 0b1448 "59 36" (subject compatibility with 65); resolve iff a compatible nearer antecedent is identified.
2. **`ere-29-40-nominal`** (P4): test whether "29 40" at 0b1710–1711 (F-post-ere frame, "29 40 65" x3 stream-wide) composes a predicative "-ère"-shaped noun/adjective with its left neighbor — the nearest unexamined in-clause antecedent candidate; kill iff no French "-ère" word fits the "12 06" left edge.
3. **`lprime-gender-44`** (P4): conditional on follow-up 1 or 2 identifying an antecedent — fix l''s gender (le vs la) from predicative agreement; kill-grade test of the standing masculine-44 lean.

## Provenance

Every number re-derived from the repaired 1,847-pair stream in-work: forcing window 0b1711–1717 byte-exact; zero 59 in 0b1640–1712 (full scan); single A1 token 37@0b1655; candidate contexts byte-exact; nearest out-of-scope predicative-59 frames at 0b1443/0b1448/0b1207–1212. No invented data. Lock created on start with UTC timestamp, deleted on completion (see bookkeeping below).
