# Battery verdict: val-41-det-windows

**Worker:** be1951b8-a431-454b-87c1-5e51063e8597
**Date:** 2026-10-09
**Verdict: PROMOTE** (evidence-package / finding grade)

## Method
- Read BATTERY-PROTOCOL.md first; lock `locks/val-41-det-windows.lock` created on start, deleted on completion.
- Stream re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py`: 1,847 pairs / 96 groups verified. 1-based @-offsets.
- `canonical.py` never used; R5005, sealed gates, red-team queue untouched.
- Premises adopted (not re-litigated): class-41-contact NULL (41 = §7 split candidate: verb @40 vs determiner @238 vs letter-slot @61); donn-41-44 letter-slot findings; 65 = noun class (R18-001); 17='fois', 64='qui' granted; 98 = finite verb class (prof-98, pending ratification); 00='pour' (A9).

## Bar (verbatim, pre-registered)

> "collect all determiner-shaped 41 windows (@238 '[98] [41] fois(17)' plus any quantifier/'fois'-frame windows) with per-window parse; package for red team"

Restated as numbered clauses:
- **C1:** enumerate every determiner-shaped 41 window: @238 plus all quantifier-/'fois'-frame windows.
- **C2:** state a per-window parse for each.
- **C3:** package the determiner arm for the red team.

## Census (all 19 of 41's windows, 1-based; followers in bold)

| @ | Row | Window `pre 41 suc` | Determiner-shaped? |
|---|---|---|---|
| 6 | a1_00 | 47 **41** 06 | No — 47='ce' is itself a determiner; two determiners ungrammatical |
| 40 | a1_01 | 64 **41** 01 | No — verb-forced ("qui [verb]") |
| 60 | a1_01 | 12 **41** 08 | No — word-internal letter slot ("53 12 [41]") |
| 92 | a1_02 | 19 **41** 98 | No — between verb-lexeme 19 and finite 98; verb-adjacent |
| **238** | a2_01 | 98 **41** 17 | **YES — strong leg** (follower 17='fois') |
| 445 | a2_09 | 78 **41** 10 | Conditional — needs nominal 10 |
| 490 | a2_11 | 42 **41** 20 | Fenced — predicative-42 frame, follower 20 open |
| 590 | a3_02 | 97 **41** 41 | No — "41 41" doubling = letter roles |
| 591 | a4_00 | 41 **41** 09 | No — letter doubling |
| 809 | a5_05 | 24 **41** 12 | Fenced — 12='n' letter-pending; sub-word tier |
| 965 | a6_00 | 56 **41** 19 | No — follower 19 = verb lexeme; determiner needs a nominal head |
| 1017 | a6_02 | 24 **41** 15 | Conditional — "faire [det] [15]" needs nominal 15 |
| 1049 | a6_04 | 85 **41** 88 | No — follower 88 = verb class |
| **1112** | a6_06 | 73 **41** 65 | **Conditional** — follower 65 = noun class (granted) |
| 1473 | a7_10 | 12 **41** 53 | Fenced — 12='n' letter tier |
| 1500 | a7_11 | 89 **41** 74 | Conditional — "89 [det] [74]" needs nominal 74 |
| 1509 | a7_11 | 56 **41** 12 | Fenced — 12 letter tier |
| **1536** | a8_00 | 73 **41** 62 | **Conditional** — follower 62 nominal ("règne"/"trône", battery-null) |
| 1760 | a8_08 | 78 **41** 15 | Conditional — "[78] [det] [15]" needs nominal 15 |

**Fois/quantifier family:** "41" is followed by 17 ('fois') exactly **once** stream-wide (@238). No predecessor of 41 is a quantifier candidate at standing grade (predecessor set: {47, 64, 12, 19, 98, 78, 42, 97, 24, 56, 85, 73, 89} — none quantifier-shaped). The fois/quantifier sub-family = @238 alone.

**Note:** @1112 and @1536 share the identical 5-gram "63 00 66 73 41" ("pour [66] [73] [41]"), differing only in the nominal follower (65 vs 62) — one shared frame, two instantiations.

## Per-window parses (determiner-arm windows)

- **W1 @238 (a2_01):** `51 70 98 41 17 11 26` = "[98-fin] [41-det] fois la [26]" — finite verb + determiner + "fois": "vient [41] fois" = "une/chaque/deux fois"-shaped. **Strong leg**: verb-41 fails (two finite verbs), noun-41 fails (bare noun before "fois" ungrammatical) — class-41-contact's discrimination, adopted.
- **W2 @1112 (a6_06):** `63 00 66 73 41 65 38 30` = "[63] pour [66] [73] [41-det] [65-noun] [38]" — "pour [66] [73] [det] [65]". Grammatical iff 73 is clause-edge/preposition-compatible (73's class open; 73 n=6, profile in method note below).
- **W3 @1536 (a8_00):** `63 00 66 73 41 62 06 21` = "[63] pour [66] [73] [41-det] [62-ne]" — with 62 nominal: "[det] [62]ne" = "un/le [62]ne". Grammatical iff 62's nominal arm holds (val-62-ne-noun: "règne"/"trône").
- **W4 @1017 (a6_02):** `47 03 24 41 15 66 91` = "[03] faire [41-det] [15]" — "faire [det] [15-nominal]" ("faire une/le [15]"). Conditional on nominal 15.
- **W5 @1760 (a8_08):** `58 17 78 41 15 93 06` = "fois [78] [41-det] [15]". Conditional on nominal 15.
- **W6 @445 (a2_09):** `80 50 78 41 10 62 61` = "[78] [41-det] [10]". Conditional on nominal 10.
- **W7 @1500 (a7_11):** `59 24 89 41 74 84 33` = "[89] [41-det] [74]" — verb-frame + det + nominal head. Conditional on nominal 74.

73 profile (n=6): "00 66 73" x2 (@1111, @1535 — exactly the two det-candidate windows), "84 73 34" (@393), "33 73 37" (@778), "73 47 11" (@269), "86 66 73 34" (@1347). Class open; neutral toward determiner-41.

## Per-clause results
- **C1: PASS** — all 7 determiner-shaped windows collected (1 strong + 6 conditional); fois/quantifier sub-family exhausted (@238 sole).
- **C2: PASS** — per-window parses stated above, each with its gating dependency.
- **C3: PASS** — this report is the package. Intended consumer: queued `split-41-redteam` (P2) — the determiner arm's leg list.

## Adverses answered
- "41's verb role at @40 and letter role at @61 pull other ways — split candidacy territory" → answered by scoping: this battery packages the determiner ARM only. Verb-41 (@40) and letter-41 (@60, @590/@591, @1473) are recorded as the other arms of the §7 split candidacy and were not re-litigated. No polyvalence declared at battery level; §7 intact.

## Standing-state check
- class-41-contact NULL (2026-10-09): adopted, not contradicted — its @238 determiner forcing is this arm's anchor.
- No red-team verdict on 41 exists; nothing contradicted or downgraded.
- No value named for 41 (compatible det values at @238: une/chaque/deux/plusieurs — all unforced).

## Headline for the red team
The determiner arm of 41 has **one strong leg** (@238: "vient [det] fois") and **six conditional legs** (@1017, @1112, @1536, @445, @1500, @1760), all gated on the followers' nominal readings (15, 10, 74, 65, 62). The @1112/@1536 pair shares one frame ("63 00 66 73 41"), so the two conditionals partially collapse into one frame-level test. With verb-41 (@40) and letter-41 (@60) standing, the split candidacy now has all three arms battery-packaged.

## Follow-ups proposed
None required (promote, not null).
