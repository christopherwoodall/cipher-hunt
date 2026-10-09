# Battery `reseg-1564-26pas` — verdict: KILL

## Bar (verbatim, pre-registered)
"name 26's letter content with byte evidence or fence the arm (@995 '26 30 03 60' is a second instance)."

Numbered clauses:
- C1: name 26's letter content with byte evidence, such that "26 30" reads as one French word "Xpas" (e.g. "repas").
- C2 (alternative): fence the word-internal arm with stated cause.

## Method
Re-derived the repaired 1,847-pair / 96-type stream in-session per `repair_parse.py`
(`repaired_offsets.json` + `data/upstream-ct_R5005.txt`); asserts held (1,847 pairs,
96 types). `canonical.py` never used. Census of the `26 30` bigram stream-wide,
then a French-lexicon inventory test: for the word-internal arm to hold, some
letter content X for 26 must make "Xpas" a grammatical French word in every
window under standing values.

## Findings

**Census:** `26 30` occurs 4x, all genuine in-row bigrams (row-boundary artifacts
excluded by per-row span check): n(26)=17, n(30)=19.

| @ | row | context |
|---|-----|---------|
| 655 | a4_02 | `94 76 49 24 26 30 03 62 16 00` |
| 992 | a6_01 | `48 01 76 49 24 26 30 03 60` (the bar's "second instance"; bar labeled @995, same window) |
| 1250 | a7_02 | `67 46 26 30 06 65 46 01` |
| 1560 | a8_01 | `93 61 40 17 11 26 30 06 60 71 50` |

**Lexicon inventory:** French orthographic words ending in "pas" are
{pas, repas, trépas, appas, compas} — **all masculine** (appas m.pl.). No
feminine "Xpas" exists, so 26's candidate content X is restricted to
{re, tré, ap, com} (or the arm is void).

**Kill at @1560:** `17 11 26 30` = "fois **la** Xpas". 11="la" is pencil
ground truth; 17="fois" is promoted. "la" as object pronoun needs a verb
host — none is adjacent — so the article reading is forced, demanding a
feminine singular noun. Every X in the inventory is masculine. **No letter
content for 26 survives this window.** Kill-grade, reading-independent.

**Corroborating kill at @1250:** `46 26 30` = "**que** Xpas". 46="que" is
pencil ground truth. "que" + bare Xpas as subject is unlicensed in 1841
French (determiner-less subjects barred) for every X.

**Supporting leg at @655/@992:** `24 26 30` = "**en** Xpas". 24="en" is
battery-grade (R24). No X yields a grammatical "en + [noun]" collocation
("en repas" and kin are unattested and ungrammatical).

C1 FAILS at kill grade: two independent windows force the word-internal
"Xpas" reading false for every admissible X. C2 fires on the kill's terms —
the arm is not merely fenced, it is dead.

**Class corroboration (not load-bearing):** 26 is noun-shaped at independent
windows — "69 26" = "ce [26-noun]" ×3 (@406/@934/@1628, kernel frame),
"64 26 37" = "qui [26] [pred]" @1769 — consistent with standalone word-26
and hostile to the word-internal arm.

## Scope
Kills only the word-internal "26 30" = "Xpas" arm. Untouched: 26's value/class
(noun lead stands), 30's value, the "26 | 30" word-boundary parse, and the
discontinuous "94 ... 30" ne…pas geometry visible at @655/@992 (clausal-ne
battery's venue, not decided here). No standing/red-team verdict contradicted;
§7 intact. Canonical-stream caveat stands.

## Verdict: KILL
Per §4 (kill), no follow-ups required. Natural next questions for the
supervisor: (a) the "24 26 | 30" boundary parse at @655/@992; (b) whether the
"94 ... 30" span licenses a discontinuous ne…pas reading.

## Bookkeeping
- Stream re-derived in-session; asserts held; `canonical.py` never used.
- Queue: `reseg-1564-26pas` → `status: verdict`, `result: kill`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  disk re-read confirms verdict/kill; own entry only; no downgrade).
- Lock created on start, deleted on completion. R5005, sealed gates, red-team
  adjudication queue untouched.
