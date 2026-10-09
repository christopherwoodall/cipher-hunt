# Battery `profile-52-host-word` — decide the 'pre[52]a' host word at @1334

- Target id: `profile-52-host-word` (priority 3)
- Date: 2026-10-09
- Worker session: 550853d6-3474-4213-a59f-9661a49f5c58
- Lock: `code/crowd17/next-token/locks/profile-52-host-word.lock` (created 2026-10-09T06:52:09Z, deleted on completion)
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`); 1,847 pairs / 96 types re-derived in-session. `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Offset convention: this report uses **1-based** @-offsets for the locus (the target's "@1334" = 1-based index of 39). 0-based equivalents stated where prior batteries used them.

## Bar (verbatim from battery-queue.json)

"name a French 'pre?a' lexeme governing 'de+INF' (e.g. test 52='scri' -> 'prescrira de [INF]') across 52's 27 windows, or kill the word-internal-39 reading at @1334"

## Bar restated as numbered pass/fail clauses (pre-registered before testing)

1. **C1:** A French lexeme of the form "pre" + [52-syllable] + "a" (70='pre' banked GT; 39='a' word-internal per a-39) governing "de + infinitive" in 1841 French exists, and exactly one such lexeme is nameable (uniqueness required to "name a lexeme").
2. **C2:** The named 52-syllable survives across 52's 27 windows — no window forces 52 ≠ that syllable at kill grade under standing values.
3. **C3 (else-branch):** If C1–C2 fail, kill the word-internal-39 reading at @1334 (1-based; 0-based @1333): i.e., show that no "pre[52]a de [INF]" parse is available, forcing 39 to the separate word 'a'/'à' and reviving the de83-39-1334 "a de [INF]" collision.

Adverse (coordination, not duplication): unit-52-37-name (52-37 bigram, verdict NULL) and de-83-sweep (verdict NULL) are queued/decided; their bars are adopted as premises, not re-run. This battery's fences feed de-83-sweep.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs, 96 types asserted; n(52)=27 verified byte-exact).
2. Located the locus: 1-based @1332=70, @1333=52, @1334=39, @1335=83, @1336=86 (0-based @1331–@1335). Verified "70-52" and "52-39" are each stream hapaxes (1x) — the trigram "70-52-39" occurs exactly once.
3. Enumerated French lexemes of the form pre+X+a governing "de + INF" (1841 grammar).
4. Tested each candidate syllable X against 52's 27 windows for kill-grade incompatibility under standing values (banked GT, granted, promoted, provisional).
5. Checked the 52-37 unit standing (unit-52-37-name NULL; la-frame-52-37-43-noun NULL) for the conditional decider.
6. Recorded phase/row-boundary caveats.

## Window-level evidence

### The @1334 locus (1-based)

0-based @1328–@1340: `06 62 94 70 | 52 39 83 86 71 64 60 08 65`
1-based @1329–@1341, with row boundary marked:

| 1-based | group | row | standing |
|---|---|---|---|
| 1329 | 06 | a7_04 | 'ent' / syllabic |
| 1330 | 62 | a7_04 | open (règne/trône tie) |
| 1331 | 94 | a7_04 | 'ne' (promoted) |
| 1332 | 70 | a7_04 | 'pre' (banked GT) |
| **1333** | **52** | **a7_05** | **open — the host syllable** |
| 1334 | 39 | a7_05 | 'a' (word-internal 'a' per a-39) |
| 1335 | 83 | a7_05 | 'de' (lead, unratified) |
| 1336 | 86 | a7_05 | INF class (registry) |
| 1337 | 71 | a7_05 | open |
| 1338 | 64 | a7_05 | 'qui' (banked GT) |

Wider left context (1-based): `... 56 1328:30(pas) 06 62 94(ne) 70(pre) | 52 39 83 86 ...`
= "…[56] pas [06] [62] ne pre[52]a de [86-INF] [71] qui [60] [08] [65] qui…"

**New observation (not in de-83-residuals or de83-39-1334): the "70-52-39" trigram straddles the a7_04/a7_05 transcription-row boundary** — 70='pre' is the last pair of row a7_04; 52 is the first pair of row a7_05. The host word "pre[52]a", if real, is a cross-row word. The lane treats the stream as continuous ciphertext (row breaks are transcription artifacts), so this is a caveat, not a kill — but it compounds the phase-fragility: the locus depends on TWO unvalidated row offsets (a7_04 and a7_05), not one.

Phase caveat (adopted from de83-39-1334, not re-litigated): under a7_05's offset-1 re-parse the row contains no 39 and no 83 — the "39 83" bigram dissolves. The locus lives on the canonical stream per protocol.

The "ne" at 1-based @1331 directly precedes "pre[52]a" with no "pas" after it (the "pas" at @1328 precedes "ne" — wrong order for ne…pas). The "ne" is therefore literary/explétif or pairs distantly. This strains all finite-verb candidates equally; it discriminates none of them.

### Candidate lexemes (pre+X+a governing de+INF, 1841 French)

| 52 = X | lexeme | verb | de+INF government | standing |
|---|---|---|---|---|
| 'scri' | **prescrira** (fut. 3sg) | prescrire | "prescrire de + INF" ✓ well-attested ("lui prescrira de se reposer") | viable |
| 'ser' | **préserva** (passé simple 3sg) | préserver | "préserver de + INF" ✓ ("les préservera de tomber") | viable |
| 'voi' | **prévoira** (fut. 3sg) | prévoir | "prévoir de + INF" ✓ ("prévoira de partir") | viable |

Rejected: prépara/présenta/précéda/préféra/préleva/prédira (no "de" government — "préparer à", "préférer" + bare INF, etc.); présagea (X='sage' structurally fits but "présager" takes no "de"); préléva; "préviendra" (X='viendr', "prévenir de + INF" marginal — noted, not counted).

**Result: three solid candidates, irreducible at battery grade.**

### 52's 27 windows vs. the candidates

Full 1-based census of 52 (neighbor pairs): @161 (93-52-94), @265 (93-52-33), @285 (48-52-89), @384 (16-52-38), @483 (13-52-30), @572 (94-52-87), @633 (08-52-67), @650 (78-52-82), @1008 (11-52-35), @1082 (06-52-89), @1101 (86-52-82), @1125 (11-52-37), @1130 (86-52-37), @1295 (94-52-80), @1309 (74-52-30), @1333 (70-52-39, the locus), @1343 (64-52-38), @1357 (06-52-37), @1386 (68-52-82), @1410 (46-52-42), @1417 (74-52-32), @1436 (64-52-82), @1442 (01-52-68), @1575 (28-52-82), @1723 (11-52-37), @1739 (48-52-86), @1808 (94-52-80).

Spot-checked the most constraining windows for kill-grade incompatibility with X ∈ {scri, ser, voi}:
- @285 (48='e' word-final left): 52 word-initial — 'scri'/'ser'/'voi' all valid French word-initial syllables. No kill.
- @572 (94='ne' left, 87='ce' right): 52's host word open; no syllable forced. No kill.
- @1008 (11='la' left): "la scri…/ser…/voi…" — host word open. No kill.
- @1295/@1808 (94='ne' left, 80 A8-frame right): "ne [52] [80]" — strained under any X (ne + syllable), but the strain is window-structural, not X-specific. No kill.
- @1125/@1130/@1357/@1723 (52-37): 52's syllable here is owned by the 52-37 unit question (see conditional decider below); under the syllabary-uniformity default it constrains 52 globally, but the unit itself is undecided (NULL). No kill now.

**No window forces 52 ≠ 'scri'/'ser'/'voi' at kill grade.** 52 is open-class at every window and all host words are open; kill-grade syllable exclusion is unavailable.

### The 52-37 conditional decider (adopted premises, not re-litigated)

- unit-52-37-name (NULL): the 52-37 unit's live name candidates are {même, seule} (after "dite" was killed by dite-52-37-anaphora).
- la-frame-52-37-43-noun (NULL): 52 is adjective-shaped in the "la 52-37" frames; the {même, seule} tie is owned by queued adj-52-37-value-rerun.
- **Conditional:** IF adj-52-37-value-rerun resolves 52-37 → "même"/"seule", THEN 52 = 'mê'/'seu'. Under the syllabary-uniformity default (each group has one phonetic value — the basis of 70='pre', 11='la', etc.), 52='mê'/'seu' contradicts 52 ∈ {scri, ser, voi} at EVERY window including @1334. All three pre-X-a candidates die; "pre-mê-a"/"pre-seu-a" is not French; the word-internal-39 reading at @1334 dies; 39 falls back to the separate word 'a'/'à'; and the de83-39-1334 "a de [INF]" collision becomes LIVE (conditional on 83='de' ratifying). This chain is recorded here as the decider, not executed — the antecedent is queued, not verdict.

## Per-clause pass/fail

- **C1 — FAIL on uniqueness (PASS on existence).** Three French lexemes of the form pre+X+a governing de+INF exist (prescrira, préserva, prévoira). The bar asks to "name a French 'pre?a' lexeme" (singular); the three-way tie is irreducible at battery grade — no window, frame, or standing value discriminates {scri, ser, voi}. Naming one would be a guess.
- **C2 — MOOT.** With no single X named, there is no syllable to sweep; moreover the sweep could not discriminate anyway (no window kills any candidate at kill grade — §"27 windows" above).
- **C3 — FAIL (cannot kill).** The word-internal-39 reading at @1334 is viable: "pre[52]a de [86-INF]" parses cleanly under any of the three lexemes ("prescrira de [INF]" / "préserva de [INF]" / "prévoira de [INF]"). No kill-grade incompatibility exists at the locus. The reading stays live; the de83-39-1334 collision stays conditional.

## Adverses answered

- **unit-52-37-name:** adopted as premise (52-37 unit NULL, {même, seule} candidates live); not re-litigated. Its queued tie-break (adj-52-37-value-rerun) is recorded above as the conditional decider for this target's reading. No duplication.
- **de-83-sweep:** not pre-empted. This battery's output feeds it: @1334's host word is now a recorded three-way tie ({prescrira, préserva, prévoira}); if the tie ever resolves against all three (via the 52-37 conditional), @1334 turns hostile to 83='de' per the de83-39-1334 collision matrix. No duplication of its 15-window sweep.

## Verdict: NULL

The host word cannot be uniquely named (three-way tie: prescrira / préserva / prévoira — all valid 1841 "de + INF" governors) and the word-internal-39 reading cannot be killed (the locus parses cleanly under any of the three). New material vs. prior batteries: (1) the three-candidate tie is now explicit with the de+INF government verified per lexeme; (2) the "70-52-39" trigram straddles the a7_04/a7_05 row boundary (caveat — cross-row word, two unvalidated offsets involved); (3) the clean conditional decider is the queued adj-52-37-value-rerun ({même, seule} → kills all three candidates → kills the reading → revives the de83-39-1334 collision iff 83='de' ratifies). No standing or red-team verdict contradicted; §7 intact (no polyvalence declared — syllable recurrence across words is normal syllabary behavior).

## Follow-up targets (null regenerates work; all verified absent from queue)

1. **`lex-52-deinf-register`** (P3): 1841 diplomatic-register corpus check — which of {"prescrira de", "préserva de", "prévoira de"} + INF is actually attested in 1841 diplomatic French? Register/attestation fit may break the three-way tie where the stream cannot. Bar: cite dated diplomatic attestations; drop candidates with zero attestation; kill the tie-break iff none attested.
2. **`syll-52-locus-1334`** (P3): locus-only syllable-composition test — do the lane's syllable-composition precedents (from the wordinternal battery family) constrain 52 at the @1334 locus (70='pre' left, 39='a' right) to a subset of {scri, ser, voi}? Narrower than this battery: single locus, no 27-window uniformity burden. Bar: name the surviving subset with the precedent cited per exclusion; kill a candidate iff a precedent excludes it at this locus.
3. **`phase-a7_05-1334`** (P4): offset-1 constraint sweep of rows a7_04/a7_05 (the locus straddles both). Bar: the sweep either hardens the "70-52-39" trigram (both rival phases keep it) or dissolves it (either rival phase breaks it), settling the phase-fragility flagged by de83-39-1334 and the row-boundary caveat above.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-profile-52-host-word.md`
- Queue: `profile-52-host-word` → status `verdict`, result `null`, date 2026-10-09 (temp-file + rename; pre-write assert passed — status was `queued`, verdict null; JSON re-validated; only this entry touched; no downgrade).
- Lock created on start, deleted on completion.
- `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
