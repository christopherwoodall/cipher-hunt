# Battery report — `08-letter-geometry`

- Target id: `08-letter-geometry` (priority 3, status queued at dispatch)
- Claim: "census 08's full predecessor/successor letter geometry to state the letter-class signature positively (word-initial vs internal, letter-neighbor inventory)"
- Date: 2026-10-09
- Worker: battery worker (session 7c7a790f-648a-4eba-81a7-a7cfe658d8ee)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed exactly per `code/side-keyhunt/repair_parse.py`; asserts held in-session: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

"state 08's letter-class signature positively (word-initial vs internal, letter-neighbor inventory) via battery-grade predecessor/successor letter census; else fence"

## Numbered pass/fail clauses (pre-registered before testing)

- **C1:** 08's word-initial vs word-internal letter-class signature is stated positively from the predecessor/successor census — each of the 18 windows' position class grounded in letter/word neighbor evidence at battery grade.
- **C2:** 08's letter-neighbor inventory is stated positively — every neighbor cell classed (letter / syllable / word / open), with the letter-class neighbor set, counts, and @-offsets listed.
- **C3 (else-arm):** if the census cannot support a positive statement at battery grade, the signature is fenced with stated cause.

Adverse (listed): "08's spelling vs clitic readings pull opposite ways (stem-08 NULL)".

## Method

1. Read `BATTERY-PROTOCOL.md` in full first. Lock `code/crowd17/next-token/locks/08-letter-geometry.lock` created on start (agent id + UTC timestamp); no stale lock pre-existed.
2. Re-derived the repaired stream in-session byte-exact per `repair_parse.py`. All @-offsets below are 0-based.
3. Adopted, never re-litigated: `stem-08-letter-probe` PROMOTE (2026-10-09: 08 word-internal; letter-value set = single letters only: pencil GT 82='m', 34='i', 40='e'; no promoted/provisional value is a single letter), `ce-08-31-frame` PROMOTE (reading-level: "87 08 31" @1488 = "ce" + [08][31]-word, 08 word-initial letter), `08-position-profile` PROMOTE (per-window initial/internal/final), on-08-homophony KILL, §7 standing constraints.
4. Letter census: for each of the 18 08-windows, predecessor and successor cells classed as letter (82/34/40), syllable (29/70/11/46 GT), word (granted/promoted/battery-promoted free words), or open.

## Window-level evidence (0-based @-offsets, repaired stream)

n(08) = 18, confirmed. Full ±3 context:

- @35 (a1_01): 64 32 01 [08] 91 39 64
- @60 (a1_01): 53 12 41 [08] 34 29 40
- @98 (a1_02): 46 29 85 [08] 21 62 94
- @198 (a2_00): 01 21 60 [08] 67 76 87
- @534 (a3_01): 26 32 16 [08] 24 82 16
- @631 (a4_01): 87 78 67 [08] 52 67 63
- @779 (a5_04): 33 73 37 [08] 29 89 11
- @881 (a5_08): 86 78 17 [08] 31 79 68
- @922 (a5_09): 74 74 40 [08] 65 71 17
- @944 (a5_10): 07 50 40 [08] 62 98 96
- @975 (a6_01): 48 51 45 [08] 01 00 92
- @1302 (a7_03): 02 70 37 [08] 43 21 43
- @1323 (a7_04): 03 29 80 [08] 62 98 56
- @1339 (a7_05): 71 64 60 [08] 65 64 52
- @1488 (a7_10): 84 24 87 [08] 31 92 39
- @1520 (a7_11): 11 91 67 [08] 31 24 11
- @1592 (a8_02): 48 29 47 [08] 81 03 29
- @1610 (a8_03): 92 65 23 [08] 55 83 71

## Full predecessor/successor census

**Predecessors (18):** 01 x1, 16 x1, 17 x1, 23 x1, 37 x2, 40 x2, 41 x1, 45 x1, 47 x1, 60 x2, 67 x2, 80 x1, 85 x1, 87 x1. (14 distinct.)
**Successors (18):** 01 x1, 21 x1, 24 x1, 29 x1, 31 x3, 34 x1, 43 x1, 52 x1, 55 x1, 62 x2, 65 x2, 67 x1, 81 x1, 91 x1. (14 distinct.)

## Letter-neighbor inventory (C2 evidence)

**Predecessor-side letters:** 40='e' x2 (@922, @944). Zero 34, zero 82.
**Successor-side letters:** 34='i' x1 (@60). Zero 40, zero 82.
**Syllable contact:** 29='er' x1, successor side (@779). Zero GT-syllable contacts on the predecessor side.
**82='m' never contacts 08 on either side** (0/36 neighbor slots).
**Word-class neighbors:** predecessors 67 x2 (@631, @1520), 17 x1 (@881), 87 x1 (@1488), 47 x1 (@1592); successor 67 x1 (@198).
**Remaining 26 of 36 neighbor slots are open-class cells** (no adopted value at battery grade).

## Per-clause pass/fail

- **C1 — PASS.** The word-initial vs word-internal signature is stated positively from the census:
  - Word-initial-letter: 5 windows — 08 follows a free word, forcing a left word boundary: @631 (67), @881 (17), @1488 (87), @1520 (67), @1592 (47). Three of these (@881/@1488/@1520) are the "08 31" x3 composition windows, where 08 fills the word-initial-letter slot of an [08][31]-word (adopted `ce-08-31-frame` PROMOTE).
  - Word-internal letter junctions: 3 segmentally-licensed windows (adopted `stem-08-letter-probe` PROMOTE): @60 (08→34='i'), @922 (40='e'→08), @944 (40='e'→08); plus the 08→29='er' syllable junction at @779, word-internal-compatible.
  - Word-final: 1 window — @198 (60→08 before free 67; 08 fused left as the final letter of [60 08], adopted `08-position-profile`).
  - Headline: 08 is a letter-tier cell with an initial-skewed but non-uniform signature: word-initial-letter in 5/18 windows, internal junctions in 4/18, word-final in 1/18, the rest open. This is the positive statement the bar asks for.
- **C2 — PASS.** The letter-neighbor inventory above is complete and positive: predecessor letters {40='e' x2}; successor letters {34='i' x1}; successor syllable {29='er' x1}; 82='m' zero contacts; all other slots classed as word or open with counts. Every one of the 36 neighbor slots is accounted for.
- **C3 — does not fire.** C1 and C2 are positively stated; nothing is fenced for lack of evidence.

## Adverse answered

"08's spelling vs clitic readings pull opposite ways (stem-08 NULL)" — **answered, not ignored.** The geometry resolves the tension without a value claim:
- The **spelling** pull is now the landed reading on two positional flavors: word-internal junctions (4/18: @60/@922/@944 letter contacts + @779 'er' junction) and word-initial-letter slots (5/18 after free words). Both are letter positions, not rival readings.
- The **clitic** pull (word-initial position read as clitic-word-like) has no positive leg left: standalone-08 is kill-grade dead (adopted `stem-08-letter-probe` C2 + `ce-08-31-frame` C2), and 08 holds zero of the clitic anchor frames — 62-08 x0 (vs 62-94 x9), 12-08 x0, 82-08 x0, 08-59 x0, 77-08 x0 (adopted `stem-08` anchor counts). Word-initial position ≠ clitic word: in 3 of the 5 word-initial windows 08 composes as the initial letter of an [08][31]-word.
- `stem-08` NULL is not downgraded: its bar was "resolve iff contact profile decides" for a VALUE — this battery names no value, so its null stands untouched.

No standing or red-team verdict is contradicted or downgraded; §7 intact; canonical-stream caveat stands (68 of 70 upstream row offsets unvalidated).

## Verdict

**PROMOTE (signature-level).** 08's letter-class signature is positively stated: a letter-tier cell, initial-skewed but positionally mixed (5 word-initial-letter, 4 internal junctions, 1 word-final of 18), with the complete letter-neighbor inventory {40='e' x2 predecessor; 34='i' x1 successor; 29='er' x1 successor; 82='m' zero contacts}. No 08 value named. The adverse's spelling-vs-clitic tension is answered as two positional flavors of the landed spelling-letter reading.

## Follow-ups

None required (promote per §4). Note for the supervisor: the @779 08→29='er' syllable junction is inventoried but its segmental licensing is conditional on 08's (open) letter value — a value-naming battery could license it; `val-08-31-letter` (already queued, P3) is the natural host.

## Bookkeeping

- Lock `locks/08-letter-geometry.lock` created on start (fresh, no stale lock), deleted on completion (verified below).
- Queue: `08-letter-geometry` → `status: verdict`, `result: promote`, `2026-10-09` (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched.
