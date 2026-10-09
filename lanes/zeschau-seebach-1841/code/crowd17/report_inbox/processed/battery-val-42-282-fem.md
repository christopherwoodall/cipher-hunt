# Battery report: val-42-282-fem — verdict: KILL

Target: `val-42-282-fem` — test "61 42 48" @282 as "[61] [42]e" with 48="e"
composing a feminine noun/adjective.
Date: 2026-10-09. Stream: repaired 1,847-pair / 96-type parse
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types
re-derived in-session, asserts held). `canonical.py` never used. R5005,
sealed gate instances, red-team adjudication queue untouched. Lock
`code/crowd17/next-token/locks/val-42-282-fem.lock` created on start
(2026-10-09T18:52:00Z); no prior/stale lock existed.

@-offsets below are 0-based pair indices. The brief's @282 is the 42
position; the trigram spans @281–283.

## Bar (verbatim, pre-registered)

"name the value iff "[42]e" is a licensed French feminine word parsing the
window"

Numbered clauses (fixed BEFORE the window census, not modified after):

- **C1:** "[42]e" parses the @281–283 window ("61 42 48") as a licensed
  French feminine word, with 48="e" composing word-finally.
- **C2:** A specific value for 42 is thereby named (the bar's "name the
  value" arm).

Verdict rule: **promote** iff C1 and C2 pass. **kill** iff a clause fails at
kill grade. **null** otherwise, with 1–3 follow-ups.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing. Created the lockfile on
   start (agent id + timestamp); no prior/stale lock.
2. Re-derived the repaired stream byte-exact per `repair_parse.py` (1,847
   pairs / 96 types asserted in-session).
3. Adopted (never re-litigated) standing values: pencil 11=la, 29=er, 40=e,
   46=que; 48="e" letter tier (R17-003); 42 noun-class (val-42-nominal
   PROMOTE); 61="premier" masculine at @281 (premier-admit-fence PROMOTE,
   conditioned ordinal slot, leg (b) "61 42" = ordinal + noun).
4. Tested the claim's segmentation "[61] [42]e" against French gender
   agreement under these standing values.

## Window-level evidence (@-offsets, 0-based)

**Locus @281–283 (row a2_03):** `... 278=37 279=61 280=20 | 281=61 282=42
283=48 | 284=52 285=89 286=28 ...`

- "61 42 48" occurs exactly **1x** stream-wide (@281–283). The "42 48"
  bigram is likewise 1x.
- **61 @281 = "premier" (masculine), standing.** premier-admit-fence
  (PROMOTE, 2026-10-09) fenced @281 into the conditioned ordinal-slot set
  via leg (b): "61 42" = ordinal + noun ("premier [noun]"), licensed by
  42's noun class. The feminine ordinal construction is separately
  established as "61 40" = "première" (val-61-premier PROMOTE); the "61 40"
  bigram is unique to @1556 and absent here. 61's global value is fenced
  (val-61-contact KILL); the only standing reading at @281 is masculine
  "premier".
- **48 = "e", letter tier (R17-003).** fem-e-48 (2026-10-09) licensed 48 as
  inflectional feminine -e in "32 48" x4 ("32e") and "19 48" x1 ("19e"),
  and established that 48 never occurs as a standalone word in any of its
  38 windows. The composition mechanism "[X]e" is therefore licensed in
  principle — but only where the frame admits a feminine word.
- **42 = noun class, value open** (val-42-nominal PROMOTE; val-42-estframes
  NULL; val-42-ne-noun KILL killed only the "[42]ne" composition, not
  "[42]e").

## Per-clause results

- **C1: FAIL at kill grade.** Under the claim's own segmentation "[61]
  [42]e", the left neighbor is 61="premier" — masculine (standing,
  premier-admit-fence leg (b)). A masculine ordinal cannot govern a
  feminine noun: "premier [42]e-feminine" is ungrammatical in French at any
  period, with no licensed exception. The feminine "[42]e" therefore
  cannot parse this window. The gender mismatch is deterministic, not a
  judgment call: the window forces the claim's parse false.
  - No rescue via re-gendering 61: the feminine "première" is spelled
    "61 40" (unique to @1556); 61 standalone at @281 is masculine
    "premier". No standing feminine reading of 61 exists at this locus.
  - No rescue via masculine "[42]e": the bar explicitly requires a
    feminine word.
- **C2: MOOT** (C1 failed at kill grade; no value can be named on a
  falsified parse).

## Verdict: KILL

The "[61] [42]e" feminine-composition hypothesis at @281–283 is dead: the
standing masculine "premier" at @281 cannot be followed by a feminine
"[42]e". The bar's licensing condition is unsatisfiable at this window.

## Adverses

None listed in the queue entry. Standing tensions noted, not re-litigated:
the "[42]ne" composition kill (val-42-ne-noun) concerns 94, not 48; the
42–06 verb-stem contact (stem-42-verb) is §7 red-team venue and does not
bear on the @281–283 window.

## Scope (stated, not hidden)

- Kills only the feminine "[42]e" composition hypothesis at @281–283.
- Untouched: 48="e" letter tier (R17-003); the "[X]e" feminine-composition
  mechanism licensed by fem-e-48 for 32/19; 42's noun class and open value;
  61's conditioned ordinal slot ("premier [noun]" remains the standing
  parse of "61 42" @281–282, with 42 masculine-or-unspecified); 61's
  global-value fence; the §7 red-team venues (42 polyvalence, 61 duality).
- No standing or red-team verdict contradicted or downgraded. §7 intact.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-42-282-fem.md` (this
  file).
- Queue: `val-42-282-fem` queued -> verdict/kill via temp-file + rename,
  own entry only; pre-write assert confirmed no prior verdict; JSON
  re-validated post-write.
- Lock `code/crowd17/next-token/locks/val-42-282-fem.lock`: created on
  start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
