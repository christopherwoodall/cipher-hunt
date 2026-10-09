# Battery verdict: value-13-third-arm

## Bar (verbatim, pre-registered from battery-queue.json)

"(a) census all 12 of 13's windows with predecessor/successor classes stated; (b) each candidate value tested against the verb-follower set (13->24 x3, 13->93 x2) AND the @567 hard constraint (13 before promoted noun 76); (c) kill the candidate iff it fails @567"

Restated as numbered clauses:
- **C1:** census all 12 of 13's windows with predecessor/successor classes stated.
- **C2:** each candidate non-'les' value tested against the verb-follower set (13→24 x3, 13→93 x2) AND the @567/568 hard constraint.
- **C3:** kill any candidate that fails @567/568.

Context: both French 'les' arms for 13 are already kill-grade dead — the determiner arm (battery-subj-13-value, KILL: 13→24 x3 / 13→93 x2 force a determiner before a finite verb, categorically ungrammatical; class-level kill covering any plural determiner) and the object-pronoun arm (battery-pronoun-13-les, KILL). This battery tests the third arm: any non-'les' value.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/value-13-third-arm.lock` on start (agent id + UTC timestamp). Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py`. `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched. Offset convention: the bar's "@567" = 0-based stream index 567 = 1-based @568 (row a3_02), matching battery-subj-13-value's "@567 (@568, a3_02)" convention; both given below.

## C1 — census (PASS)

n(13) = 12, byte-confirmed. Predecessors: 65x3, 69x2, 45x2, 00x1, 97x1, 95x1, 35x1, 99x1 (matches the brief; sums to 12). Successors: 24x3, 66x2, 55x2, 93x2, 52x1, 76x1, 92x1 (sums to 12).

| # | @0b / @1b | row | predecessor (class) | successor (class) |
|---|-----------|-----|---------------------|-------------------|
| 1 | 68 / 69 | a1_01 | 69 (open) | 24 (verb-class, 'faire' battery-promoted) |
| 2 | 139 / 140 | a1_04 | 65 (noun-class, promoted) | 66 (open) |
| 3 | 456 / 457 | a2_10 | 65 (noun-class) | 66 (open) |
| 4 | 481 / 482 | a2_11 | 00 ('pour', A9 class-level) | 52 (open) |
| 5 | 567 / 568 | a3_02 | 97 (open) | 76 (noun, masculine, battery-promoted) |
| 6 | 575 / 576 | a3_02 | 45 ('ce' HOLD A11 / 'dict' lead R16-004) | 55 (open) |
| 7 | 822 / 823 | a5_05 | 95 (open) | 24 (verb-class) |
| 8 | 1166 / 1167 | a6_09 | 45 ('ce'/'dict') | 55 (open) |
| 9 | 1360 / 1361 | a7_06 | 35 (noun, battery-promoted) | 92 (verb class, subset-scoped R18) |
| 10 | 1381 / 1382 | a7_06 | 69 (open) | 24 (verb-class) |
| 11 | 1554 / 1555 | a8_01 | 99 (open) | 93 (verb class, battery-promoted) |
| 12 | 1684 / 1685 | a8_05 | 65 (noun-class) | 93 (verb class) |

The verb-follower set: 13→24 x3 (@69, @823, @1382), 13→93 x2 (@1555, @1685). The @567/568 hard wall: "97 [13] 76" with 76 a promoted noun.

## C2 — candidate tests (PASS: 15 candidates tested)

Each candidate tested against (i) the verb-follower set and (ii) @567/568 ("97 [13] 76").

| candidate | verb-follower test | @567/568 test | result |
|---|---|---|---|
| 'en' (adverbial pronoun) | "en [verb]" grammatical | "en [76-noun]" ungrammatical | KILL |
| 'y' (pronoun) | grammatical | "y [noun]" ungrammatical | KILL |
| 'se' (reflexive) | grammatical | "se [noun]" ungrammatical | KILL |
| 'on' (pronoun) | "on [verb]" grammatical | "on [noun]" ungrammatical | KILL |
| 'le/la/l'' (sing. determiner) | determiner + finite verb ungrammatical | — | KILL |
| 'des'/'ces'/'ses' (pl. determiner) | same class kill as subj-13-value | — | KILL |
| 'leur' (possessive) | determiner + finite verb ungrammatical | — | KILL |
| 'de'/'à' (preposition) | preposition + finite verb ungrammatical | — | KILL |
| 'ne' (negation) | "ne [verb]" grammatical | "ne [noun]" ungrammatical | KILL |
| 'me/te/nous/vous' (obj. pronoun) | grammatical | pronoun + noun ungrammatical | KILL |
| 'qui'/'que'/'dont' (relative) | "qui [verb]" grammatical | "qui [noun]" ungrammatical | KILL |
| adjective | adjective + finite verb ungrammatical | — | KILL |
| noun | "noun [verb]" grammatical (subject) | noun–noun adjacency ("[97] [noun] [76]") ungrammatical | KILL |
| subject pronoun ('il/ils') | grammatical | pronoun + noun ungrammatical | KILL |
| verb (finite/infinitive/participle) | verb + verb ungrammatical | — | KILL |
| adverb | "adv [verb]" marginal | adverb + noun ungrammatical | KILL |
| 'et'/'ou' (conjunction) | conjunction + bare finite verb ungrammatical | — | KILL |
| 'ce' (demonstrative) | "ce [24-faire]" ungrammatical | "ce [76]" grammatical | KILL (verb windows) |
| 'tout' | "tout [verb]" subject-strained; "65 [13] 66" adverb-after-noun ungrammatical; profile fully disjoint from granted 79="tout" (79 preds {92,64,02,33,94...} vs 13 preds {65,69,45...}; zero shared contexts) | — | KILL |

Notes:
- The determiner kills reuse battery-subj-13-value's class-level kill (any plural determiner) and extend it to singular determiners on identical grammatical grounds; not re-litigated beyond the verb-follower contact.
- The noun candidate is the only one surviving the verb-follower set (noun subject + finite verb), but it dies at the @567/568 wall: "[97] [noun] [76-noun]" is bare noun–noun adjacency, ungrammatical in 1841 French outside apposition/proper-name/lexicalized-compound — none byte-evidenced (97's profile: n=10, 10 distinct successors x1 each, no determiner/title shape). A "13+76" one-word rescue would contradict the standing battery promote of 76 as a group-level noun; not available at battery grade.
- The 'en' candidate is the strongest natural third arm and parses 11/12 windows; it dies only at the wall.

## C3 — per-candidate kills (FIRES)

All 15 uniform word-level candidates fail at least one of the two tests. **The uniform third arm is dead at kill grade**: no single French word value (non-'les') parses all 12 windows. The @567/568 wall is the decisive discriminator — it kills 9 candidates that survive the verb-follower set.

## Scope of the kill (narrow)

Killed: 13 taking a UNIFORM word-level non-'les' value. NOT killed and fenced as live space:
1. **Sub-lexical 13** (letter/syllable inside a longer word): underdetermined at battery grade — 13's neighbors are mostly open, so no composition can be named without inventing data. The two "78-45-13" windows (@576/@1167) are the natural test site ("verdict" + 13) once the 45='dict'-iff-78-medial lead firms up.
2. **§7 split**: 13 with different values at different windows (e.g. noun at the verb windows, something else at @568). Battery cannot declare polyvalence — escalated to the red team.

## Adverses answered

- "76=noun promoted (never downgraded)": used as the @567/568 wall premise only; never challenged, never re-litigated.
- "predecessor set heterogeneous (65x3, 69x2, 45x2, 00, 97, 95, 35, 99)": confirmed byte-exact; the heterogeneity is precisely why no compositional rescue (e.g. 13 composing with a uniform neighbor class) is available.

## Standing-state check

No red-team verdict on 13 exists; nothing contradicted or downgraded. 76=noun, 65=noun-class, 35=noun, 24 verb-class, 93 verb-class, 79="tout" (A5) used as premises only. §7 intact (no polyvalence declared).

## Follow-ups proposed (for supervisor queuing)

1. `letter-13-verdicts` (P3): test 13 as word-final letter at the two "78-45-13" windows (@576/@1167) under the 45='dict'-iff-78-medial lead; kill test is the determiner-number mismatch ("ce verdicts").
2. `split-13-redteam` (P2): package 13 as a §7 split candidate (verb-window values vs @568 nominal contact) for red-team adjudication.
3. `noun-97-568` (P3): name 97's class; a verbal or determiner 97 reframes @568's left edge and re-opens the wall.

## Bookkeeping

- Lock `locks/value-13-third-arm.lock` created on start, deleted on completion.
- `battery-queue.json` updated via temp-file + rename (`value-13-third-arm`: queued → verdict/kill, date 2026-10-09; pre-write assert confirmed queued/verdictless; JSON re-validated post-write).
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched.

## Verdict: KILL

No uniform word-level non-'les' value exists for 13. With both 'les' arms already dead, the uniform-value question for 13 is closed; the surviving space is sub-lexical 13 or a §7 split, both red-team territory.
