# Battery verdict: clitic-44-census

- Worker: battery worker clitic-44-census, agent bcf6712a-9fe6-4384-9304-2361c7d79c39
- Date: 2026-10-09 (lock created 2026-10-09T04:07:53Z)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per repair_parse.py). canonical.py NOT used. R5005 untouched. All @-offsets re-derived in-work; both conventions stated (0-based stream index / 1-based lane convention).

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"resolve iff all 15 windows of 44 are classified (whole-word nominal / word-internal stem / clitic-slot) with @1714 the sole clitic-slot window, or a second clitic-slot window is found and parsed under 'en'/'l''; deliver the classification table."

Numbered clauses (frozen before testing):
1. All 15 windows of 44 classified into exactly one of: whole-word nominal / word-internal stem / clitic-slot.
2. @1714 (0-based stream index; 1-based @1715) is the sole clitic-slot window.
3. No second clitic-slot window exists that parses under 'en' or 'l''.
4. The classification table is delivered.

## Method

Re-parsed the repaired stream in-work: 1,847 pairs, 96 distinct groups, n(44)=15 confirmed (0-based indices [208, 249, 527, 540, 797, 800, 1070, 1160, 1311, 1583, 1603, 1618, 1679, 1714, 1839] — byte-identical to noun-44's, stem-44-nominal's, and stem-44-1839's re-parses). Every classification uses standing values only per protocol §7; no value is named for 44; the stem-vs-whole adjudication is NOT re-litigated (standing verdicts are cited, not re-argued).

Standing context coordinated (not duplicated):
- pronoun-44-1714 (NULL, 2026-10-08): @1714 forces 44 into a clitic slot ('ne [44] est'), value ∈ {'en','l''} undiscriminated; both rivals fail all four global frame-types.
- stem-44-nominal (NULL, 2026-10-08): 2/15 windows force stem-level composition (@540, @1160), 13/15 force whole-word segmentation; §7 split owned by red-team poly-44-docket.
- stem-44-1839 (PROMOTE instance-scoped, 2026-10-08): 44 at @1839 is a whole-word nominal head.
- phon-44-elision: 'la 44' @1070 unelided, 'le 44' x2 unelided, zero elided 'l'44'' stream-wide — consonant-initial whole-word status at those windows.
- noun-44 (KILL, 2026-10-08): the noun VALUE claim is dead; @1714's clitic forcing stands — not re-litigated.

Offset convention note: the bar's "@1714" matches the 0-based convention of the parent reports (pronoun-44-1714, stem-44-1839). The same token is 1-based @1715. The table below states both.

## Classification table

| # | 0-based | 1-based | row | context (pre | 44 | suc) | slot class | basis |
|---|---------|---------|-----|----------------------|------------|-------|
| 1 | @208 | @209 | a2_00 | 42 06 77 \| 44 \| 50 88 19 | whole-word nominal | "le 44 [50]": 44 follows article 77='le' (provisional) as nominal head |
| 2 | @249 | @250 | a2_02 | 66 91 32 \| 44 \| 94 65 63 | whole-word nominal | "[32] 44" in the A1 predicative frame of 32; 44 not preceded by 'ne', in no clitic frame ("en ne"/"l' ne" ungrammatical); the 94-contact is fenced as a 94-residual (particle 'ne' strained before noun-class 65 — a 94 question, not a 44 slot question) |
| 3 | @527 | @528 | a3_00 | 81 97 47 \| 44 \| 59 37 64 | whole-word nominal | "ce 44 est": 44 follows determiner 47='ce' (A4), precedes 59='est' as nominal subject; "ce en est"/"ce l'est" ungrammatical — no clitic parse |
| 4 | @540 | @541 | a3_01 | 16 91 12 \| 44 \| 29 48 42 | word-internal stem | '44ere' = "[X]ère/[X]ere"-shaped (44+29='er'+48='e'); stem-forcing per stem-44-nominal (standing, not re-litigated) |
| 5 | @797 | @798 | a5_04 | 64 56 37 \| 44 \| 77 86 44 | whole-word nominal | "[37] 44 le [86] 44": 44 follows predicative 37 (A1); "44 le" = nominal + object clitic of [86] |
| 6 | @800 | @801 | a5_05 | 44 77 86 \| 44 \| 74 62 98 | whole-word nominal | "[86] 44 [74]": 44 in nominal head slot, no clitic frame |
| 7 | @1070 | @1071 | a6_05 | 70 39 11 \| 44 \| 74 42 98 | whole-word nominal | "la 44": unelided article + 44, consonant-initial (phon-44-elision, standing) |
| 8 | @1160 | @1161 | a6_09 | 17 77 82 \| 44 \| 83 21 67 | word-internal stem | 'm[44]': banked 82='m' composes leftward; stem-forcing per stem-44-nominal (standing, not re-litigated) |
| 9 | @1311 | @1312 | a7_04 | 52 30 92 \| 44 \| 00 36 74 | whole-word nominal | "[92] 44 pour": 44 is the nominal complement of 00='pour' (A9); 'en'/'l'' fail here ("en pour"/"l' pour" ungrammatical, per pronoun-44-1714's global frames) |
| 10 | @1583 | @1584 | a8_02 | 24 53 12 \| 44 \| 00 36 70 | whole-word nominal | "n 44 pour": same pour-complement frame |
| 11 | @1603 | @1604 | a8_02 | 82 98 00 \| 44 \| 70 39 11 | whole-word nominal | "pour 44 pre": nominal complement of 'pour' |
| 12 | @1618 | @1619 | a8_03 | 31 76 42 \| 44 \| 11 84 78 | whole-word nominal | "42 44" two-token adjacency; nominal head parallel to @1840 (standing) |
| 13 | @1679 | @1680 | a8_05 | 39 74 77 \| 44 \| 00 46 79 | whole-word nominal | "le 44 pour que": article + nominal head + pour-frame |
| 14 | @1714 | @1715 | a8_06 | 40 65 94 \| 44 \| 59 30 64 | CLITIC-SLOT | "ne [44] est": the forcing window; 44 between 94='ne' (battery-promoted) and 59='est' (provisional); no lexical noun can intervene; value ∈ {'en','l''} undiscriminated (pronoun-44-1714, standing) |
| 15 | @1839 | @1840 | a8_11 | 64 22 42 \| 44 \| 83 21 67 | whole-word nominal | whole-word nominal head, PROMOTE instance-scoped (stem-44-1839, standing) |

Totals: 12 whole-word nominal + 2 word-internal stem + 1 clitic-slot = 15. No window left unclassified.

## Clitic-slot exclusivity (clause 2/3 evidence)

- The '94 44' adjacency occurs exactly once stream-wide (verified by full-stream bigram scan): the forcing window @1714. No second 'ne 44' adjacency exists.
- Full preverbal-clitic hunt: French clitics ('en', 'l'') sit preverbally ("en [verb]", "l'[verb]", "ne [clitic] [verb]"). 44's successors are {50, 94, 59, 29, 77, 74, 83, 00, 70, 11}. The only verb-shaped successors are 59='est' (provisional) at @528 and @1715, and 29='er' (letter) at @541:
  - @528 "ce 44 est": 44 preceded by determiner 'ce' — "ce en est"/"ce l'est" ungrammatical. Not a clitic slot.
  - @541 "44 29": word-internal stem (forced). Not a clitic slot.
  - @1715 "ne 44 est": the sole clitic window.
- No other window admits a grammatical 'en'/'l'' parse in a clitic frame.

## Reconciliation note

stem-44-nominal's "13/15 whole-word" count includes @1714 as whole-word *morphologically* ('en'/'l'' are whole-word items); this census separates syntactic slot from segmentation: @1714 is whole-word in form and clitic in slot. No contradiction; the §7 split (poly-44-docket) is flagged, not decided, per the adverse.

## Per-clause verdicts

1. All 15 classified: PASS.
2. @1714 sole clitic-slot window: PASS — '94 44' x1 stream-wide; preverbal-clitic hunt finds no other candidate.
3. No second 'en'/'l'' clitic window: PASS — every other window fails a clitic parse on standing values (article/determiner/pour contexts; "ce en est", "en pour", "l' pour", "l' ne" all ungrammatical).
4. Classification table delivered: PASS.

## Adverses (answered, none ignored)

- "coordinate with stem-44-nominal (stem-vs-whole adjudication) and stem-44-1839 (@1839 instance)": HONORED — the two stem windows and the @1839 whole-word head are classified per those verdicts' findings; the stem-vs-whole adjudication is not re-opened.
- "classifies slots only, names no values, does not re-adjudicate stem-vs-whole": HONORED — no value named for 44 at any window; @1714's value remains ∈ {'en','l''} exactly as pronoun-44-1714 left it.

## Verdict: PROMOTE (census finding)

The complete 44 slot census is delivered and holds: @1714 (0-based; 1-based @1715) is the sole clitic-slot window; the other 14 windows are 12 whole-word nominal and 2 word-internal stem, all on standing values. This promote endorses the classification table as a finding; it names no value, re-grades no lead, and declares no polyvalence (§7 intact). No standing verdict contradicted or downgraded. canonical.py not used; R5005, sealed gates, and the red-team adjudication queue untouched.

## Follow-ups

None required: this is a promote verdict, not a null. The open questions (44's value at @1714; the §7 stem/whole split) already have queued/red-team venues (clitic-44-65-discriminator, poly-44-docket) — none duplicated.

## Provenance

Every number re-derived from the repaired 1,847-pair stream in-work: n(44)=15 at the 15 listed indices; '94 44' x1; predecessor/successor censuses byte-exact. No invented data. Lock created on start and deleted on completion.
