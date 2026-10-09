# Battery report: 29-initial-word-census

- Target id: `29-initial-word-census`
- Claim: "census of stream [29]-initial words to inventory the word-initial arm's licensed shapes"
- Date: 2026-10-09
- Worker: battery worker (subagent de7a9e4c-c01e-4611-b518-1b00bbf0c858)
- Stream: repaired 1,847-pair / 96-type parse from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, re-derived in-session (asserts: 1847 pairs, 96 types; parse logic identical to `code/side-keyhunt/repair_parse.py`). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/29-initial-word-census.lock` (created at start, agent id + UTC timestamp; deleted on completion; no prior lock existed).

Terms (ASD-STE100): "word-initial 29" = a word boundary sits immediately before 29, i.e. 29 begins a word-unit. "Licensed" = composed only of banked, granted, held, or battery-promoted values; open-group letters are never invented. "@" = 0-based stream index.

## Bar (queue verbatim, pre-registered before testing)

"inventory every [29]-initial word-unit on the repaired stream with French-word existence stated per unit; feeds the W3 word-initial arm"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) Inventory every [29]-initial word-unit on the repaired stream: census all 45 occurrences of 29; classify each by left-boundary evidence using only standing values; enumerate each word-initial occurrence with byte-exact context.
2. (C2) French-word existence stated per unit: for each distinct word-initial word-unit shape, state (from standing letter values + the lane side-period corpus + 1841 French morphology) whether a French word exists, does not exist, or cannot be stated.

No adverses listed on the target.

## Method

1. Read `BATTERY-PROTOCOL.md` and the queue entry fully before testing. Copied the bar verbatim above before running any census code.
2. Re-derived the repaired stream in-session; census of all 29s (n=45 confirmed). Follower inventory re-derived: 40 x9, 89 x5, 47 x4, 80 x4, 42 x3, 85 x3, 87 x3, 82 x3, 67 x2, 48 x1, 88 x1, 60 x1, 49/74/45/69/24/37 x1 — byte-identical to left-64-29-boundary's inventory.
3. Boundary rule (standing values only): 29 is word-initial iff its predecessor is a whole-word unit from §7 — banked GT {11=la, 46=que}, promoted/granted {87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce, 94=ne, 30=pas}, provisional {77=le, 59=est}, HOLD {45=ce}. Syllables/letters (70, 82, 34, 29, 40, 48, 12) and open-value predecessors cannot license a boundary -> indeterminate/word-internal. 62='on' is NOT a licensor (A15/C2 + collision-62-84 kill: 62='on' unconditioned eliminated). 67={et,veut} polyvalent whole word noted but never precedes 29.
4. French-existence checks against `code/side-period/corpus/` (Dumas, Hugo, Guizot, Labiche, Nesselrode, levant-correspondence 1841) plus standard 1841 morphology. Corpus hits hand-classified (genuine vs OCR/elision artifact), following the ere-word-65-frames precedent.
5. Adopted as premises (not re-litigated): 29='er' banked GT; 40='e' banked GT; 64='qui' granted word; 65 begins a new word after 40 (enne-word-64, battery-held); the left-64-29-boundary NULL (W1/W2 word-initial via byte-identical third [29 40 65] at 1b@1711; W3 fenced).

## Window-level evidence

### Complete census (C1): all 45 29-offsets, 0-based

Word-initial (granted whole-word predecessor): 9 windows. Indeterminate/word-internal: 36 windows (predecessors: 33 x5, 86 x4, 06 x4, 34 x3 — of which 2 are the GT "première" 11-70-82-34-29-40 @758/@1038, word-internal — 03 x3, 48 x2, 43/93/63/36/44/01/10/08/14/88/40/16/92/31/50 x1). No 29 at stream start. Full per-window table with +/-8 contexts is in the worker script output (`/tmp/29census.py` run, offsets listed below).

The 9 word-initial windows:

| # | 0b@ | row | left context (whole word) | right context | licensable unit letters |
|---|---|---|---|---|---|
| W-A | 78 | a1_02 | `11 00 11` "la pour la" | `29 42 98 51 62 …` | "er"+[42:?] |
| W-B | 96 | a1_02 | `46` "que" | `29 85 08 21 62 …` | "er"+[85:?] |
| W-C | 147 | a1_04 | `84` "on" | `29 87 64 96 …` | "er" (87='ce' follows) |
| W-D | 218 | a2_01 | `59 46` "est que" | `29 42 16 24 89 …` | "er"+[42:?] |
| W-E | 291 | a2_03 | `64` "qui" | `29 40 65 16 …` | "ere"+[65:?] |
| W-F | 500 | a2_11 | `11` "la" | `29 40 56 39 68 …` | "ere"+[56:?] |
| W-G | 685 | a5_00 | `64` "qui" | `29 40 65 94 …` | "ere"+[65:?] |
| W-H | 689 | a5_00 | `94` "ne" | `29 60 03 39 74 …` | "er"+[60:?] |
| W-I | 1200 | a7_00 | `64` "qui" | `29 45 58 47 …` | "er" (45='ce' HOLD follows) |

Byte-exact windows (0-based, +/-8):

- W-A @78: `56 87 14 24 87 11 00 11 [29] 42 98 51 62 16 14 06 88`
- W-B @96: `66 98 19 41 98 81 97 46 [29] 85 08 21 62 94 93 59 45`
- W-C @147: `13 66 14 74 67 64 77 84 [29] 87 64 96 47 46 66 84 26`
- W-D @218: `88 19 74 77 78 06 59 46 [29] 42 16 24 89 61 96 87 46`
- W-E @291: `48 52 89 28 00 97 09 64 [29] 40 65 16 01 11 78 40 97`
- W-F @500: `78 42 94 02 79 88 47 11 [29] 40 56 39 68 21 67 77 62`
- W-G @685: `77 45 23 09 07 00 92 64 [29] 40 65 94 29 60 03 39 74`
- W-H @689: `23 09 07 00 92 64 29 40 65 94 [29] 60 03 39 74 46 02`
- W-I @1200: `07 24 82 16 96 82 16 64 [29] 45 58 47 43 55 61 21 65`

### French-word existence per distinct shape (C2)

Six distinct word-initial word-unit shapes; existence stated per unit:

1. **Bare [29] = "er"** (W-C @147 "on er ce qui…"; W-I @1200 "qui er ce [58]…", the fenced W3).
   French existence: **NO.** "er" is not a French word. Corpus check: zero genuine standalone "er" tokens in the French side-period files — the only hits are "1er"/"1er." (premier abbreviation), "'er"/"'er-" (elision fragments), and one line-break OCR fragment ("l'on er pro-" = broken "…er pro…"). W-I is the already-fenced W3; W-C is its twin ("on"+"er"+"ce"), a second bare-"er" word-initial window, likewise unparseable at battery level.
2. **[29 42 …] = "er"+[42:?]** (W-A @78, W-D @218; two occurrences, same licensed shape).
   French existence: **UNSTATEABLE.** 42's letters are open; no French word can be named or excluded without invention. Rightward unit boundary unlicensable (no granted word intervenes before 77='le' far downstream).
3. **[29 85 …] = "er"+[85:?]** (W-B @96 "que er[85]…").
   French existence: **UNSTATEABLE.** 85's value is open (A3 verb-stem frame grant only). Er-initial French verbs exist ("errer", "ériger") but naming one is invention.
4. **[29 40 65] = "ere"+[65:?]** (W-E @291, W-G @685; the W1/W2 trigram).
   French existence: **LICENSED SHAPE, WORD UNNAMEABLE.** The "…èrent" 3pl past-historic shape is French (per left-64-29-boundary: the standalone word unit "[X]èrent", anchored by the byte-identical third occurrence at 1b@1711 with no preceding 64). 65's stem letters are open (noun class battery-promoted, value unnamed), so the word itself cannot be named.
5. **[29 40 56 …] = "ere"+[56:?]** (W-F @500 "la ere[56]…").
   French existence: **UNSTATEABLE.** 56's letters are open. Note: bare "ère" (era) is a French word, but the word boundary after 40 is unlicensed — 56 follows with no boundary evidence — so "ère"-as-whole-word is fenced with stated cause, not adopted.
6. **[29 60 …] = "er"+[60:?]** (W-H @689 "ne er[60]…").
   French existence: **UNSTATEABLE.** 60's letters are open (60 is a stream hapax-follower of 29).

Result: **zero named French words** among the 9 word-initial 29s. The standing claim "29 never occurs word-initial with a *named* French word" is confirmed on the full repaired stream.

## Per-clause pass/fail

- C1: PASS — all 45 29-offsets censused on the repaired stream; 9 licensed word-initial with byte-exact contexts; the other 36 explicitly fenced as indeterminate/word-internal with the cause stated per predecessor class (incl. the 2 GT "première" word-internal windows @758/@1038).
- C2: PASS — French-word existence stated for all 6 distinct word-unit shapes: 2 negative ("er" x2, corpus-checked), 1 licensed-shape-positive-but-unnameable ([29 40 65] "…èrent"), 3 unstateable with the blocking open group named (42, 85, 56, 60).

## Verdict: PROMOTE

Per §4: all bar clauses pass, no adverses listed. The promotion ratifies the census as complete and the per-unit French-existence statements as battery-grade — it promotes no value and names no word. No standing or red-team verdict contradicted or downgraded (§7 intact). Canonical-stream caveat stands (row offsets a1_02/a1_04/a2_01/a2_11/a7_00 are among the 68 unvalidated upstream offsets).

### Headline findings (for the supervisor)

1. **The word-initial arm's licensed inventory is complete: 9 windows, 6 shapes, 0 named French words.** The arm survives only as licensed shapes ("…èrent" x2, "er"+open x5, "ere"+open x1, bare "er" x2).
2. **W3 has a twin: W-C @147 ("on er ce qui")** — a second bare-"er" word-initial window, unparseable at battery level for the same cause as W3. The two bare-"er" windows (@147, @1200) are the arm's only fully-licensed units, and neither is a French word.
3. **[29 42] x2 (@78, @218) and [29 85] @96 / [29 60] @689** are the arm's only live naming prospects; each is gated on one open group (42, 85, 60). No follow-ups are mandated by a null (verdict is promote, not null); the gating groups are flagged here for the supervisor's discretion, not queued.

## Standing constraints observed

Did not touch R5005, sealed gate instances, or the red-team adjudication queue. No values promoted or killed. No invented numbers: every offset re-derived on the repaired 1,847-pair stream; every corpus claim hand-checked with cause. Bar pre-registered verbatim before any census code ran.
