# Battery verdict: val-73-verbclass

- Target: `val-73-verbclass` (battery-queue.json, priority 3, status queued)
- Claim: name 73's verb class/value from the verb-shaped windows: cohort test on 'on [X]' successor profiles across the stream (84→59 ×4 'on est' template cohort) plus the '66 73 41' ×2 / '66 73 34' trigram family.
- Date: 2026-10-09
- Worker: battery worker (subagent 711d5f4a-5e13-4fb6-8a97-0162991d5c98)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` per `code/side-keyhunt/repair_parse.py` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.
- Adverse listed: "66's value open" — answered below (§Trigram arm).

## Bar (verbatim, pre-registered before testing)

"name a single value iff it parses all six 73 windows with zero contradiction; else fence the verb arm with the surviving candidate set"

Restated as numbered pass/fail clauses (fixed BEFORE the stream census):

- **C1:** Name a single value for 73 — passes iff the value parses all six 73 windows with zero contradiction.
- **C2 (else-arm):** Fence the verb value-naming arm, recording the surviving candidate set with stated cause.

## Method

1. Read BATTERY-PROTOCOL.md in full; verified target `val-73-verbclass` queued/verdictless (pre-write assert); created `locks/val-73-verbclass.lock` on start.
2. Re-derived the repaired stream in-session; byte-confirmed all six 73 windows (0-based @268, @392, @777, @1110, @1347, @1534) — identical to the parent `val-73-776-frame` census.
3. Cohort test A: full "on [X]" (84-successor) inventory; class tally of resolved successors.
4. Cohort test B: successor-profile comparison of 73 vs the verb cohort (59, 24, 91).
5. Cohort test C: tight-frame cohorts — "on [Y] 34", "[06] [Y] ce", "66 [X] 41", "66 [X] 34".
6. Value screen: tested finite-verb candidates against all six windows under standing values (§7).
7. Adopted, never re-litigated: parent `val-73-776-frame` NULL (W1/W2 verb-shaped screens, A15 conditions at @392, letter-screen), A15 (84="on"), A4 (47="ce"), A1 (37 predicative), A10 HOLD (33+29 stem/whole), `verb-91-277-frame` PROMOTE (91 = finite-verb class at @277, 2026-10-09), val-03-value-census precedent (parsing ≠ naming).

## Findings

### The six windows (byte-confirmed, repaired stream)

- @268: `93 52 33 42 06 73 47 11 06 67 33` [a2_02] — frame `06 73 47` = "[06] [73] ce"
- @392: `91 36 62 91 84 73 34 67 64 79 82` [a2_07] — frame `84 73 34` = "on [73] i"
- @777: `07 06 94 15 33 73 37 08 29 89 11` [a5_04] — frame `33 73 37`
- @1110: `78 65 63 00 66 73 41 65 38 30 69` [a6_06] — frame `66 73 41`
- @1347: `52 38 47 86 66 73 34 62 48 77 78` [a7_05] — frame `66 73 34`
- @1534: `21 65 63 00 66 73 41 62 06 21 62` [a8_00] — frame `66 73 41`

### Cohort test A — "on [X]" successor inventory

Full 84-successor census: {2:2, 6:1, 9:2, 24:3, 26:1, 29:1, 33:1, 51:1, 53:1, 59:4, 64:1, 73:1, 74:1, 78:1, 79:1, 91:1, 92:2}.

- Template cohort confirmed: 84→59 ×4 "on est" at @1189, @1290, @1447, @1803 (successors of "est" there: 46, 35×2, 36).
- 84→24 ×3 (24 = finite-verb class, R17-009): @310, @473, @1485.
- 84→91 ×1 = @277, the window where 91's finite-verb class was named at battery grade today.
- 84→79 ×1 ("on tout") at @1418: `34 52 32 84 79 15 33 21` — the SOLE class-resolved non-verb successor.
- Remainder: class-open cells (74, 78, and open successors).

Class-resolved tally: **8 verb-selecting vs 1 non-verb**. The "on [X]" frame is strongly verb-selecting at battery grade, and 73 sits in it. Verb-CLASS for 73 at @392 confirmed (reinforces parent W1; no new assumption).

### Cohort test B — successor profiles

Global successor sets: 73 → {47:1, 34:2, 37:1, 41:2}; 59 ("est") → {45, 46, 32, 42, 37×6, 34, 30, 39, 38, 35×3, 36, 24, 19}; 24 → {30×3, 88, 56, 87×10, 82×4, 89×3, 37×2, 47, 80×2, 26×2, 85×5, 42, 24, 41×2, 65×2, 49×2, 6, 2, 77, 48×2, 3, 0, 11, 74, 53}.

Every one of 73's successors occurs in a verb-cohort member's successor set (34 ∈ 59's; 37 ∈ 59's/24's; 47 ∈ 24's; 41 ∈ 24's). Compatible with the verb cohort — but compatibility is not selection: **zero value discrimination**. No verb value is picked out by the profile.

### Cohort test C — tight frames (all unique to 73, no cohort exists)

- "on [Y] 34" (84 Y 34): exactly 1× stream-wide — Y=73 (@391). No cohort.
- "[06] [Y] ce" (06 Y 47): exactly 1× — Y=73 (@267). No cohort.
- "66 [X] 41": exactly 2× — X=73 both (@1109, @1533). No cohort.
- "66 [X] 34": exactly 1× — X=73 (@1346). No cohort.

**Adverse answered:** "66's value open" — because 66 is open, the trigram family (`66 73 41` ×2, `66 73 34`) contributes no class or value information about 73. Recorded as uninformative, not ignored. Its only future use is via the already-queued `w73-66-trigram` (fires iff 66 resolves).

### Value screen — C1 fails

No single finite-verb value parses all six windows with zero contradiction:

- @392 "on [73] i" and @268 "[06] [73] ce": accept every 3sg verb identically — dit, fait, pense, and "est"-type all parse; "veut"-type is KILLED at @268 ("veut ce" with pronominal "ce" is ungrammatical; A4). Parsing ≠ naming (val-03-value-census precedent): zero selective legs among the survivors.
- @777 "33 [73] 37": blocks EVERY uniform finite-verb value under standing 33-class. A10 HOLD fixes 33+29 as stem/whole; a bare stem cannot serve as the subject of "[V-fin] [37-pred]", so "[33] [V-fin] [pred]" is ungrammatical for any verb value. The rescues are (a) nominal-33 at @777 — red-team venue, no battery path; (b) conditioned split (verb-shaped 73 at @392/@268 vs non-verb at @777) — §7, red-team venue. Neither is available to this battery.
- Uniform non-finite 73 is already dead (parent: "on" + infinitive/bare stem ungrammatical at @392). Uniform letter-tier is already dead (parent's screen: no single letter coheres across all six).

**C1: FAIL.** The cohort test confirms verb-class but cannot name a value; @777 structurally blocks every uniform finite-verb candidate.

### C2 — fence the verb arm (else-arm FIRES)

The verb value-naming arm for 73 is FENCED with the surviving candidate set:

- **Surviving (unkilled, unnameable):** dit/fait/pense-type 3sg verbs — parse @392 and @268 identically, zero selective legs; "est"-type — compatible (34 ∈ 59's successor set) but unselectable.
- **Killed:** "veut"-type at @268 ("veut ce" ✗); uniform non-finite 73 (on-frame); uniform letter-tier 73 (parent screen).
- **Fenced (structural, not value-specific):** uniform finite-verb 73 — blocked at @777 under standing 33-class.
- **Re-open conditions:** red-team names 33 nominal at @777, or red-team declares the §7 conditioned split. No battery path exists.

## Verdict: NULL

C1 FAIL / C2 FIRES. The "on [X]" cohort test delivers verb-class confirmation (8:1 verb-selecting among class-resolved successors; 73 patterns with 59/24/91) but zero value discrimination; the tight frames are all unique to 73; @777 blocks every uniform finite-verb value under standing 33-class.

## Scope

Value-naming only. Untouched: 73's verb-class at @392/@268 (reinforced, not newly claimed), parent `val-73-776-frame` NULL, `w73-66-trigram` (queued), `nom73-contingent-rerun` (queued), A15/A4/A1/A10 standing grants, §7 (no split declared). No standing or red-team verdict contradicted or downgraded. Canonical-stream caveat stands (row a2_02/a2_07/a5_04/a6_06/a7_05/a8_00 offsets unvalidated).

## Follow-ups (all verified ABSENT from battery-queue.json; left for supervisor)

1. `val-33-777-subject` (P4) — test whether 33 can host a nominal/subject reading at @777 under standing values; a named nominal-33 re-opens the uniform finite-verb arm for 73. Bar: name 33 nominal at @777 with zero new assumptions, else fence the rescue.
2. `seg-73-777-split` (P4, gather-only) — package the @777 structural block (verb-shaped 73 at @392/@268 vs unparseable finite-73 at @777 under stem-33) as §7 conditioned-split input for the red team. Bar: package delivered; no battery-level split declaration.
3. `on79-1418-frame` (P4) — resolve the lone non-verb "on [X]" window ("on tout" @1418); a verb-rescue there sharpens the cohort's verb-selectivity to 9:0, a confirmed anomaly fences the cohort claim instead. Bar: parse "84 79 15" at battery grade or fence as written.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-73-verbclass.md`
- Queue: `val-73-verbclass` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-73-verbclass.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/val-73-verbclass.lock`: created 2026-10-09T20:30:00Z (agent 711d5f4a-5e13-4fb6-8a97-0162991d5c98, no stale lock), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
