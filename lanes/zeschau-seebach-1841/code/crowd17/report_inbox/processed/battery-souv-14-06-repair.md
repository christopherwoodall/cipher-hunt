# Battery report: souv-14-06-repair

**Target:** `souv-14-06-repair` (priority 2)
**Claim:** re-test both '14 06' windows under the spelling-repaired value 14='souv'
**Verdict: KILL**
**Date:** 2026-10-09
**Worker:** 307b3b0a-7727-4f60-af5d-7480fcea17c3

## Bar (verbatim)

"@80-90 and @1116-1127 parse as '[16] souvent [88]' / 'prennent souvent la' with exact spelling and 16/88 class-consistent; kill iff 'souv' is distributionally untenable as a group value elsewhere"

## Bar restated as pass/fail clauses

- C1: @80-90 parses as "[16] souvent [88]" with exact spelling; 16 verb-class and 88 governor-class consistent.
- C2: @1116-1127 parses as "prennent souvent la" with exact spelling.
- C3 (kill clause): 'souv' is NOT distributionally untenable as a group value in any other 14 window. Kill iff a window forces it untenable.

## Method

- Read BATTERY-PROTOCOL.md first. Lock created on start, deleted on completion.
- Re-derived the full 1,847-pair stream from `data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json` (a5_03=0), parsed exactly as
  `repair_parse.py`. `canonical.py` never touched. R5005, sealed gates, and the
  red-team queue untouched.
- Full census of group 14: n=15 at @72, 84, 117, 141, 178, 339, 424, 458, 586,
  623, 813, 896, 1121, 1365, 1689 — matches the souvent-14-06-retest census byte-exactly.
- "14 06" bigrams stream-wide: exactly 2 (@84, @1121).

## Window-level evidence

**@80-90 (row a1_02):** `@83 16 | @84 14 | @85 06 | @86 88`.
Under 14='souv' + 06='ent' (promoted): 14-06 = "souv"+"ent" = "souvent",
exact spelling (s-o-u-v-e-n-t). 16 verb-class is distributionally supported
("m 16" x11 clitic+verb, "16 pour" x4 verb+pour-infinitive; souvent-14-06-retest).
88 governor-class is standing (registry gov/cls; battery-governor-88-value).
C1: PASS.

**@1116-1127 (row a6_07):** `@1118 70 | @1119 12 | @1120 06 | @1121 14 | @1122 06 | @1123 11`.
70='pre' (ground truth) + 12='n' (promoted) + 06='ent' = "prennent", exact
spelling (p-r-e-n-n-e-n-t). 14-06 = "souvent", exact. 11='la' (ground truth).
Full read: "prennent souvent la". C2: PASS.

**Distributional audit of the other thirteen 14 windows under 14='souv':**

| @ | row | context | assessment |
|---|---|---------|------------|
| 72 | a1_02 | 87 14 24 ("ce souv[24]") | tenable: word-initial "souv" + verb syllable (souvenir-family) |
| 117 | a1_03 | 67 14 21 60 | tenable on banked values (21='suite' is a lead only) |
| 141 | a1_04 | 66 14 74 | tenable, syllable-level |
| 178 | a1_05 | 69 14 24 | tenable, as @72 |
| 339 | a2_05 | 31 14 45 | tenable on banked values (45='ce/dict' is a lead only) |
| 424 | a2_09 | 47 14 62 ("ce souv[62]") | tenable: word-initial "souv" |
| 458 | a2_10 | 66 14 02 | tenable, syllable-level |
| 586 | a3_02 | 18 14 00 ("souv pour") | **KILL LEG — see below** |
| 623 | a4_01 | 82 14 59 ("m souv est") | tenable: boundary reading after 82 gives word-initial "souv" |
| 813 | a5_05 | 65 14 29 | supportive: "souv"+"er" = "souver", a real French stem (souverain) |
| 896 | a5_08 | 82 14 98 | tenable on banked values; becomes a second kill leg IF 98='vient' ratifies (currently battery lead only) |
| 1365 | a7_06 | 79 14 60 ("tout souv[60]") | tenable: word-initial "souv" |
| 1689 | a8_05 | 79 14 60 | tenable, as @1365 |

**The kill leg — @586 (row a3_02):** 14 sits immediately before 00='pour',
a granted value functioning as the standalone word "pour". Under 14='souv'
there is no grammatical placement:
- (a) 14 as standalone word "souv" — not a French word;
- (b) 14 word-final ("...souv" + " pour") — no French word ends in the
  syllable "souv". In French "souv" is exclusively word-INITIAL
  (souvent, souvenir, souverain, souvenance); it never closes a word;
- (c) 14 word-internal continuing into 00 ("souvpour") — not French.

Every option fails on banked values alone (00='pour' granted; the
"souv"-initial-only fact is lexical). C3: FAIL at kill grade — the bar's own
kill clause fires.

## Adverse

- spell-single-consonant (queued): clerk single-consonant spelling battery for
  'prenent'/'pasent' — a different question (global spelling rule, not a 14
  value claim). Not duplicated, not touched. Answered by non-overlap.

## Per-clause results

- C1 (parse @80-90): PASS
- C2 (parse @1116-1127): PASS
- C3 (distributional tenability elsewhere): FAIL at kill grade — @586 forces
  word-final/standalone "souv", which is not French.

## Verdict

**KILL.** The spelling repair (14='souv' giving exact "souvent") works at both
target windows, but the value is distributionally untenable: @586 (row a3_02)
places "souv" immediately before the granted word 00='pour', where French
allows no word-final or standalone "souv".

## Residuals (not follow-ups; kill verdict is terminal for this value)

- The [14]ent adverb frame shape survives at CLASS level (14-06 = X-"ent"
  adverb-shaped at @84/@1121 with verb-class 16 and governor-class 88 around
  it); only the VALUE 'souv' is killed. A different 14 value that yields a
  real X-ent adverb remains open.
- @896 becomes a second kill leg for any future 'souv'-family value if and
  when 98='vient' is ratified.
- @813 ("souv"+"er" = "souver") shows the "souv" syllable is real French —
  the failure is positional (word-final at @586), not phonotactic.

## Bookkeeping

- Lock `locks/souv-14-06-repair.lock` created 2026-10-09T02:47:18Z, deleted on completion.
- `battery-queue.json`: `souv-14-06-repair` queued → verdict/kill (own entry only,
  temp-file + rename; pre-write assert confirmed no prior verdict; JSON re-validated).
- Canonicality caveat stands: 68 of 70 upstream row offsets unvalidated; the
  @586 leg sits on row a3_02.
