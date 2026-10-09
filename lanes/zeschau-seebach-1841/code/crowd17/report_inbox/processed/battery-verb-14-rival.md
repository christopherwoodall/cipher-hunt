# Battery report: verb-14-rival

- Target id: `verb-14-rival`
- Claim: 14 = infinitive/verb-stem rival tested across the verb frames
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserted in-session: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/verb-14-rival.lock` (created on start, deleted on completion).

## Bar (verbatim, pre-registered before testing)

"name 14=verb iff B2, B3, @72, @178, B1, B4 all parse as verb frames with <=10% orphan; else kill the rival"

Numbered pass/fail clauses (restated before testing, not modified after):

1. B2 @623 (`82 14 59`) parses as a verb frame with 14 as verb (finite or infinitive).
2. B3 @896 (`82 14 98`) parses as a verb frame with 14 as verb.
3. @72 (`87 14 24`) parses as a verb frame with 14 as verb.
4. @178 (`69 14 24`) parses as a verb frame with 14 as verb.
5. B1 @424 (`47 14 62`) parses as a verb frame with 14 as verb.
6. B4 @1121 (`06 14 06`) parses as a verb frame with 14 as verb.
7. Else-branch: if any clause 1-6 fails, the rival 14=verb is killed.

Breaker definitions adopted from tout-slot-14 (NULL, 2026-10-08), used as premises per the adverse, not re-litigated: B1 @424 `29 47 14 62 48 76`; B2 @623 `76 82 14 59 37 33`; B3 @896 `98 82 14 98 83 86`; B4 @1121 `12 06 14 06 11 52`.

## Window-level evidence (0-based @-offsets, re-derived in-session)

Standing premises used (not re-litigated): 24 = finite verb class-level (ne-24-profile PROMOTE); 06 = 'ent' promoted; 59 = 'est' provisional; 98 = finite-verb class (prof-98 PROMOTE), 'vient' battery-promoted lead (vient-98-name); 69 = noun class (battery PROMOTE); frame-62-94-79's kills hold (14='me', 14='est', 14=verb-in-tout-frame); stem-14-84-retest (NULL 2026-10-09) fenced 14's verb class lane-wide; 82 = 'm' is a banked LETTER ("82 14" = "mle", not a word — adopted from clitic-14-82-breakers NULL 2026-10-09).

- **C1 B2 @623** (row a4_01): `76 82 14 59 37 33` = "[76] m [14] est [37-pred] [33]er".
  - 14=finite verb: "m [V-fin] est" — two adjacent finite verbs; an object clitic "m'" before a finite verb demands that verb be the clause's single finite verb. Ungrammatical. FAIL.
  - 14=infinitive: "m' [14-inf] est [37-pred]" — an infinitive subject with a clitic complement is grammatical in principle ("m'informer est utile"), but the window continues "[37] 33": predicative + bare infinitive "[37-pred] [33]er" with no governor. No clean full-window parse. FAIL / fenced.
- **C2 B3 @896** (row a5_08): `01 98 82 14 98 83 86` = "[01] [98] m [14] [98] de [86]".
  - Under 98='vient': "vient m' [14] vient de [86]" — two finite "vient"s in one run with no clause-boundary license; double finite verb is ungrammatical. The "vient me [inf]" pull (tout-slot-14's B3 note) requires ignoring the second, byte-present 98. FAIL.
  - 14=finite verb: "vient m' [V-fin] vient" — three verbs in sequence. FAIL.
  - Rescue via an unmarked clause boundary between 14 and the second 98 is an ungranted assumption (clause-boundary-after-article was kill-grade retired today by clause-boundary-precedent; a bare inter-verbal boundary has no byte license here). Fenced, not parsed.
- **C3 @72** (row a1_02): `87 14 24` = "ce [14] [24-fin]".
  - 14=finite verb: "ce [V-fin] [V-fin]" — two adjacent finite verbs; "ce" cannot subject a lexical verb. Ungrammatical at kill grade. FAIL.
  - 14=infinitive: "ce [inf] [24-fin]" — infinitive with no governor and no subject. Ungrammatical at kill grade. FAIL.
- **C4 @178** (row a1_05): `69 14 24` = "[69-noun] [14] [24-fin]".
  - 14=finite verb: "[N] [V-fin] [V-fin]" — adjacent double finite verb. Ungrammatical at kill grade. FAIL.
  - 14=infinitive: "[N] [inf] [V-fin]" — ungoverned infinitive between noun and finite verb. Ungrammatical at kill grade. FAIL.
- **C5 B1 @424** (row a2_09): `47 14 62` = "ce [14] [62]".
  - 14=finite verb: "ce [V-fin] [62]" — "ce" cannot subject a lexical verb; and 62's verb reading is unpromoted (62 nominal/verb-stem scope is red-team territory). FAIL.
  - 14=infinitive: "ce [inf]" without a preposition — ungrammatical. FAIL.
  - Gated on 62's value per tout-slot-14 C2 (62 open). Fenced, not parsed.
- **C6 B4 @1121** (row a6_07): `12 06 14 06` = "n ent [14] ent".
  - No word-level value parses between two promoted 3pl finite endings (breaker-b4-1121, fenced as structural anomaly). 14=verb gives three adjacent verbs — ungrammatical at kill grade. FAIL.

## Per-clause pass/fail

1. B2: FAIL (fenced; no clean full-window verb-frame parse).
2. B3: FAIL (fenced; double finite "vient" kills both arms).
3. @72: FAIL at kill grade.
4. @178: FAIL at kill grade.
5. B1: FAIL (fenced on 62's open value).
6. B4: FAIL at kill grade.
7. Else-branch fires: 0/6 windows parse as verb frames.

## Adverses answered

- Coordinate with tout-slot-14's breaker fencing: done — adopted B1 gated-on-62, B2/B3 fenced, B4 fenced as structural anomaly; nothing re-litigated.
- Do not re-litigate frame-62-94-79's kills (14='me', 14='est', 14=verb-in-frame): used as premises. Additionally, 14='me' is independently dead at B2/B3 at the letter level: 82='m' is a banked letter, so "82 14" = "mle", not "me" + anything (adopted from clitic-14-82-breakers, stated not hidden).

## Verdict: KILL

The rival 14=infinitive/verb-stem is killed at battery grade: 0/6 bar windows parse as verb frames, with @72, @178, and B4 failing at kill grade. Consistent with and strengthening stem-14-84-retest's lane-wide verb-class fence (NULL). No standing red-team verdict contradicted or downgraded; §7 intact.

Remaining 14 questions are owned by already-queued targets: det-14-census (determiner @117), det14-elsewhere (fenced), le14-adj60-tail (frame tail), frame-62-94-79-reparse. No new follow-ups proposed; the kill is terminal for the rival.

## Bookkeeping

- Queue: `battery-queue.json` `verb-14-rival` → status `verdict`, result `kill`, date 2026-10-09 (temp-file + rename; pre-write assert confirmed queued/verdictless; JSON re-validated; no other entry touched; no downgrade).
- Lock created on start, deleted on completion.
