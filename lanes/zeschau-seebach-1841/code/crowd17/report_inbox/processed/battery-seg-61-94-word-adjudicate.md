# Battery verdict: seg-61-94-word-adjudicate

**Verdict: KILL** — the 55-61-94 family candidacy closes at battery grade.
No red-team ratification of a named French word with 61-94 as syllables
exists at either window. The only ever-named sub-claim (61="pren", the
"re-/com-/sur-prenne" family) is forced false at two banked windows by the
standing seg-61-pren-polyvalence KILL, and the frame-restricted rescue is
forbidden by section 7. No alternative named word survives.

## Bar (verbatim, pre-registered)

"promote iff the red team ratifies a named French word with 61-94 as
syllables at both windows; else the family candidacy closes"

## Numbered clauses (stated BEFORE testing, unchanged after data)

1. Promote arm: the red team has ratified a named French word with 61-94 as
   syllables at both windows (brief's @579 and @1170) — then PROMOTE the
   55-61-94 word claim as an established word-internal-94 family member.
2. Else arm: no such ratification exists in the standing R-series record —
   then the family candidacy CLOSES (terminal, not inconclusive).

Adverses (from brief): "no standing promote/lead/grant puts word-internal
94 after a non-12 syllable elsewhere". Answered below.

## Method

Read BATTERY-PROTOCOL.md in full first. Created
`code/crowd17/next-token/locks/seg-61-94-word-adjudicate.lock`
(agent 925514b7-be59-49ee-8960-2e7a0be04bb4, 2026-10-09T06:46:01Z) on start.
No stale lock existed. Parsed the repaired 1,847-pair / 96-type stream from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
with the upstream byte-exact tokenization
(`[s[i:i+2] for i in range(o, len(s)-1, 2)]`, same as
`code/side-keyhunt/repair_parse.py`). `canonical.py` never touched. R5005,
sealed gate instances, and the red-team adjudication queue never touched.
Every count below re-derived from the stream. No prior counts trusted.

## Window-level evidence (byte-verified on the repaired stream)

The two brief windows, 1-based @-offsets (94 is the brief's @-anchor):

- Window W1 (brief @579), row a3_02:
  `13@576 55@577 61@578 94@579 82@580 06@581 06@582`
- Window W2 (brief @1170), row a6_09:
  `13@1169 55@1170 61@1171 94@1172 87@1173 83@1174 21@1175`

Census facts re-derived:
- `55-61-94` trigram: exactly **2x** stream-wide (0-based 576, 1167).
- `61-94` bigram: exactly **2x** stream-wide (0-based 577, 1168) — no other
  61-94 contact exists. These two windows are the whole 61-94 population.

## Clause 1 (promote arm): FAIL — no red-team ratification

Searched the full standing R-series record for the next-token pipeline:
`code/crowd15/report_inbox/next-token-redteam.md` and
`code/crowd17/report_inbox/processed/next-token-redteam-r17.md`
(the latest R-record; no R18 exists).

- Zero ratifications of a named French word with 61-94 as syllables at
  either window. 61 appears in R17 only incidentally (re-derived context
  string "61 94 82 06 06 50" for R17-007 06="ent"; counts "62->94 x9";
  "42-94-59-37"). All crowd15 "61" hits are @-offset substrings (@1619,
  @1664, @611), not value claims.
- The only prenne-family red-team grant is R17-013 (prenne-subject,
  70-12-94 — the 12-family), which strengthens the 12-family fence and is
  consistent with closing the 61-family. It does not name a 61-94 word.
- Clause 1 FAILS. No promotion is possible at battery grade: promotions are
  ratified by the red team only, and the ratification does not exist.

## Clause 2 (else arm): FIRES — the candidacy closes

The close is kill-grade, not merely unfenced. The standing record forces
the only named sub-claim false:

1. **61="pren" is battery-KILLED as a global value**
   (`battery-seg-61-pren-polyvalence.md`, standing verdict/kill).
   @1556 (row a8_01): `93 61 40 17` with banked 40="e" (pencil) and
   17="fois" (promoted) gives "prene fois" — "prene" is not a French word;
   no French word ends in "pren". @367 (row a2_06): `49 61 70 17` with
   banked 70="pre" (pencil) and 17="fois" (promoted) gives "prenpre" —
   unreadable French. A rescue limiting 61="pren" to the 55-61-94 frame
   only would be a polyvalence, forbidden by section 7 (67 et/veut is the
   sole true polyvalence; only the red team may declare another).
2. **61 carries a promoted locus-level value incompatible with "pren"**
   (`battery-val-61-premier.md`, standing verdict/promote): @1556 =
   "première fois", 61="premier" (one-group spelling of 70-82-34-29) at
   that locus. The very window that kills "pren" reads 61 as "premier".
   61's global value stays fenced (val-61-contact KILL stands).
3. **The 55 side is closed too**: `seg-55-re-prefix` NULL (55="re"
   untested, circular), `subj-55-61-word` KILL, `name-55-61-core` NULL,
   `name-13-55-61` NULL, `unit-13-55-61-contact` NULL, `val-61-contact`
   KILL.
4. **No alternative named French word with 61-94 as syllables exists** in
   any standing battery or red-team record. Naming one now would invent
   data, which the protocol forbids.

The word claim's only statable sub-claim (the prenne family via 61="pren")
is forced false at two windows with banked neighbors. The bar's else arm
is terminal ("closes"), and section 4 defines null as inconclusive and
work-regenerating — a null with follow-ups would contradict the
pre-registered close. The candidacy closes at kill grade.

## Adverses answered

- "No standing promote/lead/grant puts word-internal 94 after a non-12
  syllable elsewhere": CONFIRMED by re-sweep of the standing verdicts.
  The only promoted word-internal-94 family is the 12-94 "prenne" family
  (enne-family-12-94 PROMOTE), excluded by the bar. No new adverse found.
- No standing red-team verdict is contradicted: the R-series contains no
  61-94 word ratification and no 61="pren" grant. Section 5 escalation is
  not triggered. The earlier `seg-61-94-word` and `seg-55-61-94-word`
  NULLs are untouched (different queue entries; nothing downgraded).

## Verdict: KILL

The 55-61-94 word claim (@579/@1170) is closed as a live non-12-pre-94
family candidate. The promote bar fails (no red-team ratification); the
else arm fires (candidacy closes); the close is kill-grade because two
windows force the only named sub-claim false and section 7 blocks the
rescue.

## Follow-ups

None queued. A kill closes the line; section 4 requires follow-ups only
for nulls. Re-open condition (red-team calls, not battery calls): the
red team fences @1556 and @367 with stated cause, or the red team
ratifies a named French word with 61-94 as syllables at both windows.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-61-94-word-adjudicate.md`
  (this file).
- Queue: `seg-61-94-word-adjudicate` queued -> verdict/kill, date
  2026-10-09 (own entry only, temp-file + rename; pre-write assert
  confirmed queued and verdictless; JSON re-validated post-write).
- Lock `locks/seg-61-94-word-adjudicate.lock` created on start, deleted on
  completion.
- Standing verdicts: none contradicted, none downgraded. R5005, sealed
  gate instances, red-team adjudication queue untouched.
