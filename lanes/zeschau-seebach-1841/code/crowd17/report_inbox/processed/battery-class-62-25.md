# Battery verdict: class-62-25

**Verdict: NULL** — no single class parses all 25 non-94, non-@46 windows of 62. The distribution splits into at least three behaviors (compound-verb prefix in "62 98" x5, verb-stem-final in "62 06" x2, nominal/adjectival in "X 62 48" x6), and @1482 ("vient 62 que") defeats every independent-word class at kill grade. @46 stays fenced as segmentation-open pending seg-par-pour-96-00.

## Bar (verbatim, pre-registered)

> CLAIM: name 62's class on the 25 windows with @46 fenced as segmentation-open
> BARS: one class parsing the 25 non-94, non-@46 windows; @46 fenced as segmentation-open
> ADVERSES: 'il' kill-grade dead; 'on' kill honored
> EVIDENCE: battery-class-62-nof94.md null follow-up #2
> PRIORITY: 2

Numbered clauses:
1. (a) One class parses the 25 non-94, non-@46 windows. **FAIL** — every candidate class is defeated (see per-class table).
2. (b) @46 fenced as segmentation-open. **PASS** — @46 ("30 62 96 00": "pas 62 par pour") is not re-litigated here; class-62-nof94 fenced it on the "96 00" ("par pour") collocation, ungrammatical under standing values at all 3 occurrences (@47, @465, @960), with dedicated follow-up `seg-par-pour-96-00` queued. Fence cause stated, not ignored.
3. (c) Adverses answered. **PASS** — 62='il' kill-grade dead (fullcensus) not revived; collision-62-84 KILL (62='on' unconditioned) honored, not re-litigated; no red-team verdict contradicted.

## Method

Read BATTERY-PROTOCOL.md first; lock created on start. Re-derived the full 62 census from the repaired 1,847-pair stream (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `repair_parse.py`): 35 windows confirmed. Excluded follower-94 (9 windows) and @46 (1 window) → 25 target windows. `canonical.py` never touched. Value key: pencil ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que), granted/promoted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce), provisional (59=est, 77=le), battery leads used only where stated (98="vient", 06="ent", 78="ver", 30="pas"). 1841 diplomatic French only. R5005, sealed gates, red-team queue untouched.

## The 25 windows (re-derived)

| @ | row | prev-62-next | gloss |
|---|---|--------------|-------|
| 11 | a1_00 | 93-62-98 | ? 62 vient <N> |
| 82 | a1_02 | 51-62-16 | vient 51 62 16 14 |
| 360 | a2_06 | 21-62-48 | la <N> 62 e <N> |
| 389 | a2_07 | 36-62-91 | 91 36 62 91 on |
| 425 | a2_09 | 14-62-48 | ce 14 62 e <N> |
| 446 | a2_09 | 10-62-61 | 41 10 62 61 est |
| 658 | a4_02 | 03-62-16 | pas 03 62 16 pour |
| 665 | a4_02 | 03-62-06 | ? 03 62 ent? pour |
| 802 | a5_05 | 74-62-98 | 44 74 62 vient 53 |
| 849 | a5_06 | 40-62-21 | par e 62 <N> 67 |
| 945 | a5_10 | 08-62-98 | e 08 62 vient par |
| 1065 | a6_04 | 21-62-18 | par <N> 62 18 pre |
| 1136 | a6_08 | 20-62-98 | 86 20 62 vient pour |
| 1141 | a6_08 | 78-62-16 | vient ver 62 16 er |
| 1297 | a7_03 | 04-62-16 | 80 04 62 16 02 |
| 1315 | a7_04 | 74-62-48 | 36 74 62 e vient |
| 1324 | a7_04 | 08-62-98 | 80 08 62 vient 56 |
| 1349 | a7_05 | 34-62-48 | 73 i 62 e le |
| 1454 | a7_09 | 92-62-61 | que 92 62 61 <N> |
| 1464 | a7_09 | 21-62-48 | 01 <N> 62 e <N> |
| 1468 | a7_09 | 02-62-38 | <N> 02 62 38 26 |
| 1482 | a7_10 | 98-62-46 | 16 vient 62 que le |
| 1536 | a8_00 | 41-62-06 | 73 41 62 ent? <N> |
| 1539 | a8_00 | 21-62-93 | ent? <N> 62 93 88 |
| 1569 | a8_01 | 74-62-48 | 24 74 62 e 56 |

Follower distribution: 48 x6, 98 x5, 16 x4, 61 x2, 06 x2, 91/21/18/38/46/93 x1. Three sub-families: "62 vient" x5, "X 62 e" x6, "X 62 ent?" x2.

## Per-class results

| Class | Result | Deciding evidence |
|---|---|---|
| Noun (independent word) | **DEAD** | @665 "03 <N> ent? pour" and @1536 "41 <N> ent? <N>": a noun followed by "ent?" (3pl verbal ending, battery-promoted 06="ent") as a separate word is ungrammatical; the only rescue is "62-06" as one word, which is a segmentation fence, not a noun parse. Strained additionally at @1482 ("vient <N> que le" — bare noun directly before "que"), @360/@1464/@1065 (double-noun adjacency "la <N> <N>e"). |
| Adjective | **DEAD** | @1482 "vient [adj] que le": an adjective directly before "que" is ungrammatical in 1841 French. Strained at @665/@1536 ([adj] + "ent?"), @849 ("par e [adj] <N>" — "e" is not a word), @1141 ("vient ver [adj] 16" — "vient" intransitive), @1349 ("i [adj]e le"). |
| Adverb | **DEAD** | @1482 "vient [adv] que le": ungrammatical as a class (the only rescue is the value-specific "bien que" concessive, which names a value, not a class — spun off as follow-up). Strained at @665/@1536, @360/@1464 (adverb between nouns). |
| Finite verb | **DEAD** | The five "62 98" windows (@11, @802, @945, @1136, @1324): "X 62 vient" puts two finite verbs in contact ("93 V vient"), ungrammatical. Also dead at @1482 ("vient V que"). |
| Infinitive | **DEAD** | Same five "62 98" windows: "X [inf] vient" — an infinitive directly before a finite verb with no licit frame is ungrammatical. |
| Preposition | **DEAD** | @11 "93 [prep] vient": preposition with no object before a finite verb. Dead broadly. |
| Determiner | **DEAD** | @360 "la <N> [det] e": determiner after a complete noun phrase. Dead broadly. |
| Clitic / 'en' / 'y' | **DEAD** | 'en' parses the five "62 vient" windows elegantly ("93 en vient" = "[subj] en vient") but dies at @1482 ("vient en que" — 'en' cannot precede 'que') and is strained at the six "X 62 e" windows ("<N> en e" — 'en' before "e", no verb). 'y' dies at @1482 identically. |
| Subject pronoun (non-il/on) | **DEAD** | Agreement: 98="vient" is 3sg (battery lead); plural pronouns ("ils/elles") contradict it. Remaining 3sg pronouns ('ce' taken by 47/87, 'ça/cela' untestable as class) die at @1482 ("vient [pron] que"). 'il'/'on' excluded by standing kills. |
| Verb prefix / stem (word-internal) | **NOT A CLASS PARSE** | The "62 98" x5 windows invite a compound-verb reading ("93 [62-vient] <N>": parvenir/devenir/revenir family) and "62 06" x2 invite "[stem]-62-ent" 3pl — but these make 62 word-internal, not an independent word of a class. This is the conditioned-split hypothesis: it needs red-team approval (§7 sole-polyvalence law) and is recorded as a lead, not a verdict. |

No class survives all 25. Clause 1 FAILs at kill grade for noun, adjective, finite verb, infinitive, preposition, determiner, clitic; adverb fails pending the value-specific 'bien' test (follow-up).

## Per-clause verdict

- Clause 1: **FAIL** — no one class parses the 25 windows; see table.
- Clause 2: **PASS** — @46 fenced as segmentation-open with stated cause (the "96 00" = "par pour" blocker; `seg-par-pour-96-00` queued by class-62-nof94).
- Clause 3: **PASS** — adverses honored.

## Verdict: NULL

The negative results are recorded at their proper grades. 62's distribution is irreducibly multi-behavioral at battery level: compound-verb prefix ("62 vient" x5), stem-final ("62 ent" x2), nominal/adjectival ("X 62 e" x6) — a conditioned split is the live hypothesis but only the red team can approve it (§7). Note: `redteam-62-conditioned` is already queued; this battery does not duplicate it.

## Follow-ups (null regenerates work)

1. `compound-62-vient` (P2): test 62 as verb-prefix in the five "62 98" windows (@11, @802, @945, @1136, @1324) against the French compound-"venir" family (parvenir/devenir/revenir/souvenir/prévenir). Bars: name the compound verb at all five windows with stated prefixes, or kill the prefix hypothesis. Does not name 62 globally.
2. `adv-62-bien-1482` (P2): test 62='bien' (adverb) via the "bien que" concessive rescue at @1482 ("16 vient bien que le ?"), then re-run the 25-window class test with the value fixed. Bars: all 25 parse under adverb-with-'bien', or the 'bien' value dies at kill grade.
3. `seg-62-48-word` (P3): test whether "62 48" x6 (@360, @425, @1315, @1349, @1464, @1569) is one word ("62e"). Resolves the word boundary currently blocking both the noun and adjective readings of the largest sub-family. Bars: byte-level left/right attachment profile decides one-word vs two-word, or fence with stated cause.
4. (Coordination, not a new target) `stem-62-ent-665-1536` was already proposed as follow-up #3 of class-62-nof94 — do not duplicate; it covers the "62 06" x2 windows.

## Bookkeeping

- Lock `locks/class-62-25.lock` created on start (agent id + UTC 2026-10-09T03:00:00Z); no stale lock present; deleted on completion.
- `battery-queue.json`: target `class-62-25` queued → verdict/null (own entry only, temp-file + rename; pre-write assert confirmed no prior verdict).
- R5005, sealed gates, red-team adjudication queue untouched. No standing verdict contradicted or downgraded. `canonical.py` never used.
