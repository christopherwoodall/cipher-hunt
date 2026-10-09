# Battery report: dire-33-asymmetry-no21

- Target id: `dire-33-asymmetry-no21`
- Claim: "test the dire/croire asymmetry at 33's full window set without 21's value: census 33 on the repaired stream, name which windows force dire-shaped vs croire-shaped frames independent of 21"
- Date: 2026-10-09
- Worker: battery worker (subagent 058f7fae-4556-42eb-925c-0dea2d44da7f)
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json`
  + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  1,847 pairs / 96 types re-derived in-session, asserts held). `canonical.py`
  never used. R5005, sealed gate instances, and the red-team adjudication
  queue untouched. Lock `code/crowd17/next-token/locks/dire-33-asymmetry-no21.lock`
  created on start, deleted on completion.

## Parentage

Follow-up 1 of the NULL `croire-33-noun21` (2026-10-09): the '33-21' x3
dire/croire asymmetry gate (@937/@1422/@1631) fenced because 21's value is
unresolved and its battery-grade value search is kill-closed
(val-21-reopen, 2026-10-09). This battery tests the alternative: land the
asymmetry at 33's other windows without 21's value; fence as 21-load-bearing
if not.

## Bar (verbatim, pre-registered before testing)

"land the asymmetry without 21, or fence it as 21-load-bearing"

Restated as numbered pass/fail clauses (fixed BEFORE the stream census, not
modified after):

- **C1:** At least one window among 33's 25 selects a dire-shaped frame that
  fails under croire (or vice versa) via evidence INDEPENDENT of 21's value.
- **C2:** If C1 lands, the asymmetry is recorded (which windows, which
  direction) at battery grade.
- **Resolve-arm:** C1 met AND C2 recorded → PROMOTE (the asymmetry finding,
  not a value). **Else-arm:** no window discriminates without 21 → NULL with
  the fence stated (21-load-bearing).

## Method

1. Read BATTERY-PROTOCOL.md first; created/deleted the lock.
2. Re-derived the repaired stream in-session from
   `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
   parsed per `repair_parse.py` (pair up from row offset, drop trailing odd
   digit). Verified: **1,847 pairs, 96 types**. `canonical.py` never touched.
3. Full census of 33: **n(33) = 25**, byte-exact on the repaired stream.
4. Tested every structural family under 33="dire" vs 33="croire" using French
   valency facts of 1841 diplomatic French that do not depend on 21's value:
   dative indirect-object licensing ("dire à [NP]" vs "croire [NP]"),
   substantivization ("le dire" as noun), bare-infinitive complementarity,
   and the stem/whole division per the A10 HOLD (33+29 stem/whole).
5. Coordinated with (never re-litigated or downgraded): croire-33-tiebreak
   (NULL, 2026-10-08 — exhaustive 25-window sweep, tie recorded),
   val-33-verb (NULL, 2026-10-08 — stem face and whole face select disjoint
   single-string values; 'penser' bridges as one lexeme), croire-33-noun21
   (NULL, 2026-10-09 — gate fenced on 21's kill-closed value search),
   croire-33-compound85 (NULL, 2026-10-09 — compound asymmetry fenced on 85's
   trigger), A10 HOLD, §7 (67 et/veut sole true polyvalence).

## Census (repaired stream, 0-based @, center = 33; ±4 context; row ids)

- @24: `82 43 29 47 33 55 81 00 34` [a1_00]
- @186: `23 37 06 00 33 16 00 66 24` [a1_05]
- @265: `74 45 93 52 33 42 06 73 47` [a2_02]
- @273: `47 11 06 67 33 29 89 84 91` [a2_03]
- @408: `34 69 26 00 33 01 02 53 84` [a2_08]
- @467: `59 42 96 00 33 79 80 06 67` [a2_10]
- @626: `82 14 59 37 33 29 87 78 67` [a4_01]
- @776: `07 06 94 15 33 73 37 08 29` [a5_04]
- @846: `26 12 16 00 33 96 40 62 21` [a5_06]
- @936: `56 69 26 00 33 21 64 37 01` [a5_10]
- @1000: `67 11 96 82 33 00 86 56 47` [a6_02]
- @1088: `02 55 81 00 33 79 80 06 43` [a6_05]
- @1149: `98 98 86 67 33 66 84 02 00` [a6_08]
- @1232: `82 48 29 47 33 29 85 56 10` [a7_01]
- @1245: `81 87 11 00 33 16 00 67 46` [a7_01]
- @1421: `32 84 79 15 33 21 67 33 29` [a7_08]
- @1424: `15 33 21 67 33 29 87 63 91` [a7_08]
- @1451: `84 59 36 67 33 46 92 62 61` [a7_09]
- @1477: `53 60 06 67 33 29 82 16 98` [a7_10]
- @1502: `89 41 74 84 33 42 33 00 86` [a7_11]
- @1504: `74 84 33 42 33 00 86 56 41` [a7_11]
- @1624: `84 78 66 67 33 46 56 69 26` [a8_03]
- @1630: `56 69 26 00 33 21 64 37 01` [a8_03]
- @1642: `74 35 56 12 33 98 60 03 64` [a8_04]
- @1700: `15 23 91 85 33 94 30 20 62` [a8_06]

Matches the tiebreak's census byte-exactly (same 25 windows, same bigram
counts: `00 33` x8, `67 33` x6, `33 29` x5, `33 21` x3, `67 33 46` x2).

## Window-level evidence (asymmetry test, 21 held unvalued)

**F1 — `00 33` x8 ("pour [33]").** Both candidates parse as clean infinitives.
Tie. Independent of 21. (val-33-verb F1 adopted.)

**F2 — `67 33` x6.** 67 positional rule: 67="veut" iff follower
infinitive-shaped. Under dire-whole ("dire") 33 is infinitive-shaped; under
croire-whole ("croire") 33 is infinitive-shaped. Both → veut. Symmetric.
Independent of 21.

**F3 — `33 29` x5 (stem windows).** Kill both equally: neither "di"+"er" nor
"croi"+"er" is an -er stem; only stems like 'laiss-'/'pens-' survive. Tie by
A10 HOLD (stem face out of scope for the whole-frame test). Independent of 21.

**F4 — `67 33 46` x2 (@1451, @1624).** "veut/et [33] que": "veut dire que" ✓,
"veut croire que" ✓. Tie. Independent of 21.

**F5 — `33 21` x3 (@937, @1422, @1631).** Both verbs take noun objects, so no
asymmetry is available without 21's specific value. @1421/1424 = "…15 33 21
67…" byte-adjacent to the F3 window @1424. This is the parent's gated frame:
**21-load-bearing by design** (croire-33-noun21).

**F6 — `33 42` x2 (@265, @1502-1504 chain).** 42 open (A1 predicative): both
readings symmetric. Independent of 21; tie.

**F7 — @24 `47 33 55` ("ce [33] [55]").** "se dire" ✓ / "se croire" ✓. Tie.

**F8 — singletons.** @776 `15 33 73 37`: 73 and 37 open (37 predicative A1);
croire's predicative-on-object complement ("croire X coupable") and dire's
("dire de X qu'il est…") need 73's value — open-neighbor, not asymmetry.
@1000 `82 33 00 86`: "m'[33] pour [86]er" equally strained under both.
@1149 `67 33 66`: "veut/et [33] [66]" symmetric. @1502 ("on"+infinitive)
and @1642 ("n'"+consonant-initial infinitive) are symmetric failures fenced
to 84/12 by the tiebreak (croire-33-residuals adopted).

**F9 — @1700 `85 33 94 30`.** The ONLY structural asymmetry not requiring
21: dire-family compounds (contredire, médire, redire) have no croire
counterparts. But its trigger is **85's value**, not 21's: stem-85 returned
NULL (2026-10-08); croire-33-compound85 already fenced it on 85's trigger.
Not re-litigated; it is a gated asymmetry, not a live one.

**New 21-independent valency probes (added by this battery):**

- **Dative probe.** French "dire" licenses "dire à [NP]" (indirect object);
  "croire" takes direct "croire [NP]". No cipher value for "à" is named in
  §7 or standing values, and no 33 window shows a dative frame (@1000's
  `33 00` is "pour", A9 grant — not dative). No discrimination available
  at standing grade. → negative.
- **Substantivization probe.** "dire" substantivizes ("le dire", "au dire
  de X"); "croire" has no productive "le croire" noun. 33's predecessor
  set (re-derived): {23, 00, 74, 47, 34, 59, 82, 26, 67, 98, 48, 81, 02,
  32, 15, 89, 84, 12} — no 11 ('la'), no 77 ('le'), no 96 ('par'). No
  determiner/preposition-before-33 geometry exists anywhere, so the
  substantivization test finds nothing to discriminate. → negative.
- **Bare-infinitive probe.** Neither "dire" nor "croire" takes a bare
  infinitive complement ("dire faire" ✗, "croire faire" ✗). No 33 window
  has an infinitive follower. Symmetric. → negative.

## Per-clause results

- **C1: FAIL.** No window among the 25 selects a dire-shaped frame that
  fails under croire (or vice versa) without 21's value. Every family
  either parses under both (F1, F2, F4, F6, F7, singletons) or fails under
  both (F3, @1502, @1642); F5 is 21-load-bearing by design; F9 is trigger-
  gated on 85's value (owned by croire-33-compound85).
- **C2: MOOT** — nothing lands, nothing recorded.
- **Resolve-arm: not met. Else-arm: TAKEN — verdict NULL, fenced as
  21-load-bearing.**

## Fence (stated cause)

The dire/croire asymmetry at 33's window set is **21-load-bearing**: the
only documented asymmetry avenue (the '33-21' x3 noun test) needs 21's
specific value, whose battery-grade search is kill-closed (val-21-reopen);
every other avenue is grammatically symmetric under both candidates on the
re-derived 25-window census, including the two new 21-independent probes
(dative, substantivization — both negative at standing grade). The one
non-21 structural asymmetry (@1700 dire-family compounds) is gated on 85's
value, not on 21, and is already queued as compound85-locus-reread. The
asymmetry re-opens only if the red team names 21's value
(croire-33-noun21-redteam-gated, already queued) or if a named 85 revives
the compound lead.

## Standing-verdict check

No standing verdict contradicted or downgraded: A10 HOLD reinforced (stem
face kills both equally, re-derived); croire-33-tiebreak's recorded tie
CONFIRMED from the 21-independence angle; val-33-verb's penser-bridge
untouched; croire-33-noun21's fence confirmed (this battery was its
follow-up). §7 intact. No red-team contradiction, no escalation.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `io-slot-33-dative` (P3) — probe whether the cipher has any licensed
   "à" position: census the standing values and open windows for an
   à-positional; if one sits adjacent to a 33 window, re-test the
   dative asymmetry ("dire à [NP]" vs "croire [NP]") at battery grade.
   Bar: land the asymmetry iff a 33 window admits "à"+NP with zero new
   assumptions; else fence the dative avenue permanently.
2. `val-73-776-frame` (P3) — name 73 at @776's `[15] [33] [73] [37]`:
   if 73 resolves nominal, test "croire [73] [37-pred]" vs "dire [73]
   [37-pred]" selectionally — "croire [NP] [adjectif]" is licensed French
   ("le croire capable"); "dire [NP] [adjectif]" is not standard ("dire
   de [NP] qu'il est…"). Bar: land the asymmetry iff 73's named value
   yields a frame grammatical under exactly one candidate.
