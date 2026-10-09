# Battery report — stem-68-id (name the la-frame stem at @1720)

- Target id: `stem-68-id`
- Date: 2026-10-09
- Worker: 9b81061b-523e-4819-ada3-2305ed108467
- Lock: `code/crowd17/next-token/locks/stem-68-id.lock` created 2026-10-09T05:10:04Z; no prior lock; deleted on completion.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`. 1,847 pairs verified. `canonical.py` never used. R5005, sealed gates, red-team queue untouched. No invented numbers: every count re-derived in this run.

## Bar (verbatim from battery-queue.json)

"name 68's value iff its contact profile matches a verb stem with the @1720 frame parsing; else fence with stated cause"

## Bar restated as numbered clauses (pre-registered BEFORE testing, not modified after)

1. Name 68's value IF AND ONLY IF (a) 68's full contact profile (all 8 windows, re-derived) matches a verb stem, AND (b) the @1720 la-frame parses as verb+object with 68 as the stem.
2. If either arm fails, do NOT name a value; fence with stated cause (which arm failed, which window(s) force it).

## @-offset convention note

The brief's "@1720" is the 06 ("ent") position. On the 0-based repaired stream the frame is `47 68 06 11` at **@1718–1721** (68 at @1719, 06 at @1720, 11="la" at @1721). All @-offsets below are 0-based pair indices.

## Method

Fresh re-parse of the repaired stream. 68 n=8, census re-derived and byte-identical to the standing `battery-frame-qui-47` census (7 free + @1788 formula-bound). Each window graded against the verb-stem hypothesis using standing banked values only: 11=la, 79=tout, 00=pour, 47=ce (A4), 30=pas (F89), 06=ent (ent-06), 21=suite noun-class (N108), 65=noun class (R18), 59=est provisional, 37 predicative frame (A1), 89 verb-host (A8), 64=qui, 67 et/veut (sole polyvalence). 1841 diplomatic French for grammaticality judgments.

Re-derived windows (0-based):

- @114: `93 29 89 68 21 67 14` — "[89-verb-host] [68] suite(noun) et/veut [14]"
- @504: `40 56 39 68 21 67 77` — "[39] [68] suite(noun) et/veut [77]"
- @884: `08 31 79 68 37 03 02` — "tout [68] [37-PRED]"
- @1286: `32 98 55 68 00 11 17` — "[98-finite] [55] [68] pour la fois"
- @1384: `13 24 65 68 52 82 16` — "[65-noun] [68] [52]"
- @1442: `85 01 52 68 59 37 64` — "[68] est [37-PRED] qui"
- @1719: `30 64 47 68 06 11 52` — "pas qui ce [68] ent la [52]" (the la-frame)
- @1788: `82 96 21 68 47 03 00` — "suite(noun) [68] ce [03]" (formula-bound)

Stream facts: the "68-06" bigram occurs **exactly once** in the stream (@1719) — the la-frame is a singleton leg. The "47-?-11" ("ce X la") trigram occurs **exactly once** (@1718–1720) — no independent distributional support for either rival parse of the frame.

## Clause-by-clause evidence

**Clause 1(a) — contact profile vs verb stem: FAIL.**

- @884 "tout [68]": 79="tout" granted. "tout" + finite verb is ungrammatical in 1841 French; "tout" + infinitive is ungrammatical. ANTI-VERB.
- @1442 "[68] est [37-PRED]": 59="est" provisional + A1 predicative frame = subject + copula + predicative. A finite verb cannot be the subject of "est". **Forcing window against verb-stem status.** ANTI-VERB (strong).
- @114 / @504 "[68] suite": 21="suite" noun-class (N108). Bare "suite" as direct object of a verb is ungrammatical; noun/adjective + "suite" is the natural modifier frame. Nominal-leaning; anti-verb (weak).
- @1286: 68 sits in object position after finite 98 ("[98-finite] [55] [68] pour la fois") — nominal-compatible, neutral.
- @1384: "[65-noun-class] [68]" — "modal(24) noun(65) verb(68)" is strained; neutral.
- @1788 (formula-bound): "suite [68] ce" — nominal frame; neutral.
- The ONLY verb-shaped contact in the profile is the singleton "68-06" @1719, which is conditional on the very hypothesis under test (see clause 1(b)).

Tally: 0/8 windows require a verb; 2 windows (@884, @1442) are anti-verb, one of them forcing; the rest are neutral or nominal-leaning. **The contact profile does not match a verb stem.** This independently reproduces the standing battery-level `frame-qui-47` KILL of 68 verb-hood; no standing verdict is contradicted or downgraded.

**Clause 1(b) — the @1720 la-frame parses as verb+object with 68 as stem: FAIL (condition unmet).**

The ent-06 battery's la-frame argument is explicitly conditional: "[68]-06-11 parses ONLY as verb+object — conditional on 68 = verb stem." Clause 1(a) fails, so the condition fails and the verb+object parse is void. Moreover, under 68=verb-stem the window reads "pas qui ce [68]ent la": "ce" + 3pl "-ent" verb form is ungrammatical ("ce" selects 3sg). Under nominal 68 the window parses as the demonstrative frame "ce [68ent] la" ("this/that [noun]-ent, the [52]…"), which is grammatical. The verb+object parse is therefore not merely unlicensed — it is the worse parse of the two.

## Adverses (answered, never ignored)

- "68's class open" — ANSWERED with fence: verb-stem status is ruled out by the contact profile (forcing window @1442 "[68] est", second @884 "tout [68]"); 68 leans nominal per the standing frame-qui-47 battery KILL (never downgraded). Value is NOT nameable on current evidence: the only verb-shaped bigram ("68-06") is a stream singleton and its verb parse died with the verb-stem hypothesis. Class remains open; no red-team verdict exists on 68's class, so nothing is contradicted.

## Verdict: KILL (of the naming claim) + fence

The target's operative hypothesis — 68 is a verb stem whose value can be named via the @1720 la-frame — is forced false by the contact profile. Neither bar arm passes, so per the bar's own iff, **no value is named**. 68 is fenced: verb-stem ruled out (forcing: @1442 "[68] est" subject frame; second: @884 "tout [68]"), nominal-leaning, class and value open.

## Supervisor notes (not findings)

1. **Narrowing of an ent-06 supporting leg (battery-level, no red-team verdict touched):** the ent-06 battery's la-frame argument ("[68]-06-11 parses ONLY as verb+object") rested on the open condition "68 = verb stem". That condition now fails at battery grade, so the 68 leg of that argument is void; the @1121 "14-06-11" leg is untouched (14's class is its own open question). The 06="ent" promote itself stands — the letters-tier reading is unaffected.
2. The verb-vs-adverb call named in this target's evidence field is moot for @1719: with 68 nominal, "68-06" is neither verb ("68ent") nor adverb — it is noun-stem + "ent" letters, which the ent-06 promote permits (06 is the letters/syllable "ent", also used word-initially in "entreprenne").

## Follow-ups for the supervisor (kill verdict — none required; two proposed)

1. `laframe-1719-demonstrative` (p3): test the rival parse "ce [68ent] la" at @1718–1721 as a demonstrative+noun frame under 1841 diplomatic French. Bar: (a) the frame parses cleanly with 68 nominal; (b) 06="ent" composing noun-finally does not violate the ent-06 letters-tier promote. Note: "47-?-11" is a stream singleton — this is a one-window parse test, not a distributional one.
2. `noun-68-value-id` (p4): name 68's nominal value. Candidate pool: "-ent" nouns. Bar: ≥2 independent nominal legs under one value with zero contradictions (@1442 "[68] est [37]" subject leg + @114/@504 "[68] suite" modifier legs).
