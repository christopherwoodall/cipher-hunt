# Battery report: part-88-86

**Target:** `part-88-86` — "Test 88 as past participle at @86; the souvent-skeleton 'a souvent [pp]' needs a 88-participle leg re-examined under the adverb-stem rival."
**Date:** 2026-10-09. Worker: 824734e5-b5b5-4f41-9eff-6c0666798e97.
**Stream:** repaired 1,847-pair / 96-type parse (`repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed exactly as `repair_parse.py`; 1,847 pairs / 96 types re-derived and asserted in-session). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

1. "Test the @86 window ('a souvent 88'-shaped) against the adverb-stem rival reading."
2. "Promote/narrowed if participle reading is forced; null with follow-ups otherwise."

Numbered clauses (fixed before testing):
- C1: Test the @86 window against the adverb-stem rival reading.
- C2: Promote/narrowed iff the participle reading is FORCED (unique survivor, zero ungranted assumptions); else NULL with 1–3 follow-ups.

## Window evidence (@86, row a1_02, mid-row)

Surface @80–90 (0-based), byte-confirmed, all row a1_02 (no row boundary in window):
`98 51 62 16 14 06 88 77 66 98 19`
i.e. @83=16, @84=14, @85=06, @86=88, @87=77, @88=66, @89=98.

Distributional facts (re-derived):
- "14 06" bigrams stream-wide: exactly 2 — @84 and @1121.
- @86 is the ONLY window with 16 three-back of 88 ("16 14 06 88" shape). The only other "16 88" contact is the adjacent bigram @903–904 (row a5_09: `...16 88 18...`), a different shape.
- 88's minus-1 slot stream-wide: 39×2, 69×2, 24, 06, 50, 89, 02, 54 — no auxiliary-shaped predecessor anywhere.

Standing premises (adopted, not re-litigated):
- 06='ent' (R17 red-team promote; registry).
- 88 = verb/governor class (registry ["gov","cls"]; battery-governor-88-value PROMOTE, battery grade, pending ratification).
- 16: no registry entry; global finite-verb class FENCED (val-16-a-vs-est NULL; val-16-187-bound NULL); locus-level 'a'/'est' values only at the two 16-91 windows @537/@1370 (val-91-pp-adj).
- 14: no registry entry; verb class FENCED lane-wide (stem-14-84-retest NULL).
- 77='le' provisional; 62='il' KILLED at kill grade (R19-106/R20-125).

## The "a souvent [pp]" skeleton and its three premises

The participle reading parses @83–88 as "a souvent [88-pp]" (16='a' auxiliary + "souvent" adverb + 88 past participle), with "le [66]" @87–88 as the direct object: "a souvent [pp] le [66]" — clean French shape ("a souvent vu le château"); the right context supports it. But shape is not force. The reading needs:

- **P1 — the adverb "souvent" = 14+06.** 14="sou" KILLED at kill grade by spelling ("souent" ≠ "souvent", souvent-14-06-retest). 14="souv" KILLED at kill grade (@586 forces word-final/standalone "souv", not French, souv-14-06-repair). No licensed adverb value for 14 exists. The class-level "X-'ent' adverb" shape survives (souv residual), but no value is named.
- **P2 — 16='a' (auxiliary) at @83.** Locus-level 'a' exists only at @537/@1370 (val-91-pp-adj); untested at @83. (Battery precedent for the shape exists: "m'a [91-pp]" passé composé at the 16-91 windows — but that grant does not transfer.)
- **P3 — 88 = past participle.** New class claim against standing 88=["gov","cls"]; a finite/participle class split for 88 is §7 red-team venue. No independent pp-shaped 88 window exists.
- **P4 — subject-capable 62 at @82.** 62='il' killed; 62 open.

## The adverb-stem rival

14 as adverb-stem (class-level "14-06 = X-'ent'" shape, surviving per the souv residual) with 88 in its standing verb/governor class; the "[88] le [66]" transitive frame at @86 is battery-validated (battery-governor-88-value L4). The rival is not dead at class level — but it yields no forced parse either: "[16] [adverb] [88-fin]" is ungrammatical under every standing 16 value (16 verb-class → two finite verbs; 16='a' aux → aux + finite).

## Per-clause results

- **C1: PASS (tested).** The @86 window was tested against the adverb-stem rival. Neither reading is forced: the participle reading's adverb premise (P1) is dead under both tested values, and the adverb-stem rival survives only at class level without a grammatical full parse.
- **C2: FAIL → NULL.** The participle reading is not forced — it needs P1 (both tested values killed, replacement unnamed), P2 (16='a' untested at @83), P3 (§7 class split, red-team venue), and P4 (62 open). Four ungranted assumptions/venue items; not battery grade.

Kill not warranted: no window forces 88≠pp at @86 at kill grade; the failure is unforced-ness (missing premises), not a forced contradiction. The bar's else-branch specifies null.

## Adverses

None listed in the queue entry. Standing constraints respected: 06='ent' upheld; 88's gov-class used, not contradicted; the "sou"/"souv" kills and the 14 verb-class fence adopted, not re-litigated; no red-team verdict touched.

## Scope

Locus-level @86 only. Untouched: 88's standing verb/governor class, 06='ent', the 14 verb-class fence, the "sou"/"souv" kills, 16's fences and locus grants, 62='il' kill, §7. No standing or red-team verdict contradicted or downgraded. Canonical-stream caveat stands (row a1_02 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json; for supervisor queuing)

1. `xent-14-adverb-value` (P4) — name a 14 value yielding a real French X-ent adverb (the souv-14-06-repair residual opening: "a different 14 value that yields a real X-ent adverb remains open"). Re-arms the souvent-skeleton and this target iff named; kill-grade constraints: must spell exactly with 06='ent' and survive @586 (no word-final failure of the "souv" type).
2. `pp-88-frame-census` (P4) — census all 23 88-windows for past-participle-shaped frames (auxiliary 'a'/'est' + 88; preceding-DO agreement geometry); include the @903–904 "16 88" adjacency as a second candidate locus. A second pp-shaped window gives the 88-participle class claim distributional legs independent of @86; feeds the §7 split venue.
3. `aux-16-83` (P4) — test 16='a' as auxiliary specifically at @83 (distinct from the fenced global finite-verb class and from the @537/@1370 locus grants; val-16-84-role NULL did not decide it). The participle reading needs auxiliary-16.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/part-88-86.lock` created 2026-10-09T21:36:00Z (agent 824734e5-b5b5-4f41-9eff-6c0666798e97 + timestamp; no stale lock), deleted on completion (verified gone).
- `battery-queue.json`: `part-88-86` queued/verdictless → `status: verdict`, `result: null`, date 2026-10-09. Pre-write assert passed (was queued, verdict None). Written through target-id-unique temp `battery-queue.json.part-88-86.tmp` + atomic rename; no tmp leftover; JSON re-validated post-write; own entry only; no downgrade.
- Report: `code/crowd17/report_inbox/battery-part-88-86.md`.
