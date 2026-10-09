# Battery report: neque-82-frame-family — verdict: KILL

**Target:** neque-82-frame-family — "'94 82' ('ne m...', 82='m' banked) is a distinct licensed frame family, 4x stream-wide"
**Worker:** ffffe6a1-3a66-4a39-9010-c38b90b65770 | **Date:** 2026-10-09
**Stream:** repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts hold: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team queue untouched. Lock `code/crowd17/next-token/locks/neque-82-frame-family.lock` created 2026-10-09T10:32:25Z; no stale lock; deleted on completion.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"(a) @1182 (slotlen 8) and @1742 (slotlen 1) parse as the same frame under standing values; (b) the @578 57-pair window and the @1353 nested window (which runs into the 79-twin) carry the same '94 82' opening signature. Kill iff the four instances force incompatible readings of the slot after 82"

## Bar as numbered clauses (fixed before the census)

1. **C1:** @1182 (slotlen 8) and @1742 (slotlen 1) parse as the same frame under standing values.
2. **C2:** the @578 57-pair window and the @1353 nested window (which runs into the 79-twin) carry the same '94 82' opening signature.
3. **C3 (kill clause):** KILL iff the four instances force incompatible readings of the slot after 82.

Adverses: none listed.

## Census (re-derived in-session)

'94 82' bigram occurs exactly **4x** stream-wide (reproduces seg-94-82-06-f2's census):

| @ | window | row | follower of 82 | left of 94 |
|---|---|---|---|---|
| 578 | `55 61 [94 82] 06 06 50 10 19 18 14 00 97 ...` | a3_02 | 06 | 61 |
| 1182 | `77 78 [94 82] 06 06 59 42 06 84 59 46` | a6_10 | 06 | 78 |
| 1353 | `77 78 [94 82] 06 52 37 64 35 13 92 62 94 79 14 60 ...` | a7_05 | 06 | 78 |
| 1742 | `12 34 [94 82] 46 56 40 06 65 ...` | a8_07 | **46** | 34 |

Slotlen check: @1182 = 8 groups from 82's follower through the closing 46 (`06 06 59 42 06 84 59 46`); @1742 = 1 group (`46`). Both close with banked 46='que'. The @578 57-pair window (pairs 550–606) contains '94 82'. The @1353 window nests the 79-twin: `62 94 79 14 60` at @1362–1366 (twin at @1686–1690, row a8_05).

Standing values used: banked 82='m', 46='que', 34='i'; 94='ne' per R17-001 STRONG LEAD used **arguendo only** (the 2026-10-09 quantified 94 battery supports a particle/syllabic split, not uniform 'ne'; nothing here depends on 94='ne' being true). 06='ent' iff pre=82 per R17-007/F61 conditional (context-only, as in ni-1740-1742).

## Window-level evidence

**@1742** (`12 34 94 82 46 56`, a8_07): ni-1740-1742 (standing KILL) established zero clean parses with banked values — "ni" hapax with no correlative partner; banked 82='m' kills "ne me" (needs absent 48; elision "m'" blocked by consonant-initial 46='que'); "m" stranded (not a French word; sub-lexical edges excluded in seg-94-82-06-f2); "ne m que" verbless. Both readings fenced for the red-team 12/94 duality adjudication. That battery's own note: "@1742 is the odd one out among the four 94-82 windows."

**@1182** (`77 78 94 82 06 06 59 42 06 84 59 46`, a6_10): under 94='ne' arguendo the "ne m'ent..." reading hits the F66 fence ("ne mentent/entendent est" ungrammatical with provisional 59='est'); seg-94-82-06 (NULL, 2026-10-08) fenced the uniform "ne|ment" segmentation at kill-adjacent grade (≥2 ungranted assumptions: 50's role at frame A, local 59 re-read at frame C).

**@578** (`55 61 94 82 06 06 50 10 19 18 14 00`, a3_02): "ne m'entent [50]..." — the "mentent [50]" word-ID is F72-refuted; 50's role ungranted (seg-94-82-06 frame A, fenced admissible).

**@1353** (`77 78 94 82 06 52 37 64 ...`, a7_05): "ne ment pas" parses clean at trigram level (52='pas' bounded to negation frames) — the only clean "ne m'ent..." instance (seg-94-82-06 frame D).

## Per-clause pass/fail

1. **C1: FAIL.** @1742 admits zero clean parses as "ne m..." (kill-grade, ni-1740-1742); @1182's "ne m'ent..." is F66-fenced. No single frame parse covers both under standing values — and under strict §7 (94 unvalued) the "same frame" cannot even be stated with values.
2. **C2: PASS (literal).** Both windows contain the '94 82' bigram (byte-verified); @1353's window runs into the 79-twin `62 94 79 14 60` @1362–1366. The signature is shared as a bigram; the reading is not (see C3).
3. **C3: FIRES.** The family reading "'94 82' = ne m..." requires 82 to compose rightward ("m'" elision or "me"). The slot after 82 forces incompatible readings:
   - @578/@1182/@1353: follower 06 — vowel-initial "ent" under R17-007/F61, so "ne m'ent..." is phonologically licensable (grammaticality fenced per-window, but the opening is licensable).
   - @1742: follower **46='que' (banked, consonant-initial)** — elision impossible, "me" impossible (no 48; banked 82='m'), "m" stranded, "mque" not a word. The family opening is forced false here at kill grade.
   
   No rescue: reading 94 as particle/syllable (per the quantified 94 battery) abandons "ne" at @1742 and breaks the family the other way; reading "ne|ment" (seg-94-82-06's fenced rival) also dies at @1742 (no 06 to supply "ment"). Under every candidate uniform reading, the banked 46 follower forces a different — unparseable — reading than the 06-follower instances.

## Verdict: KILL

The '94 82' bigram is 4x by census but is **not** one licensed "ne m..." frame family. @1742's banked 'que' follower forces a reading of the slot after 82 that is incompatible with the "m'"-elision the family requires at the other three instances. This extends (does not contradict) ni-1740-1742's "odd one out" note and seg-94-82-06's fences; R17-001, R17-007/F61, F66, F72 untouched; §7 intact; no standing or red-team verdict contradicted or downgraded.

## Supervisor note (kills do not regenerate per §4)

The natural next step is the already-proposed `islet-94-82-1742` (seg-94-82-06-f2 follow-up F2b): "94-82-46 @1742 decides whether 94-82 is a fixed islet or 94 is left-free." If not yet queued, it remains the live question this kill sharpens.

## Bookkeeping

- `battery-queue.json`: `neque-82-frame-family` queued → verdict/kill (temp-file + rename, own entry only, pre-write assert confirmed no prior verdict, JSON re-validated).
- Lock created on start, deleted on completion. No standing verdict contradicted or downgraded. R5005, sealed gates, red-team queue untouched.
