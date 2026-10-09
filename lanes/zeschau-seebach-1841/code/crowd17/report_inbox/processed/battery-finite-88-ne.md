# Battery finite-88-ne — verdict: NULL

**Target:** `finite-88-ne` (clean re-run; prior worker died in a runtime restart, orphaned lock cleared).

**Bar (verbatim from queue):** "name 88's finite form at @1706 ("[62] ne [88]") with 26's class stated"

**Numbered clauses:**
1. C1: 88's finite form at @1706 is NAMED (a specific French verb form).
2. C2: 26's class is STATED (its grammatical role at this window is given).

**Method:** Fresh byte-exact re-parse of the repaired 1,847-pair stream
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`;
verified 1,847 pairs / 96 types). `canonical.py` never used. R5005, sealed
gates, red-team queue untouched. Lock created on start with agent id + UTC
timestamp.

## Window evidence (0-based offsets)

@1706-1711: `62 94 88 26 12 06` (row a8_06). The full window @1704-1712:
`20 62 94 88 26 12 06`.

**Census facts (all re-derived):**
- 88: n=23. `94-88` occurs exactly ONCE stream-wide (@1707-1708). @1706 is the
  only "ne [88]" window.
- 62: n=35. Followers: 94 x9, 48 x6, 98 x5, 16 x4. `62-94-88` x1 (@1706).
- 26: n=17. `26-12-06` occurs exactly ONCE stream-wide (@1709-1711).
- 12-06 as a contact: byte-established 3pl ending cluster "nent" —
  `70-12-06` = "prennent" (70="pre", 12="n", 06="ent"; exact spelling
  confirmed by battery souvent-14-06-retest C2 PASS, 2026-10-08).

**Standing constraints applied:**
- 94="ne": battery-promoted only (NOT red-team ratified) — every "ne"-frame
  conclusion below carries this caveat.
- 62="il": dead globally at kill grade (battery-il-62, processed).
  62="on": killed. Per battery-class-62-25 (report_inbox, 2026-10-08): no
  independent-word class survives all 25 non-94 windows (@46 "pas 62 par"
  defeats every independent-word class); plural pronouns ("ils/elles")
  contradict 98="vient" 3sg at the 62-98 x5 windows.
- 26: noun-class LEAD (battery), value open. 26's class is the listed adverse.

## Analysis

**The only grammatical parse using all six groups is the fused 3pl reading:**
`62 ne [88-26]nent` = "[subject] ne [verb]-3pl".

- Reading 88 as a standalone finite verb ("62 ne [88]" + "26 12 06" as
  following material) leaves `26 12 06` unparseable: after a finite verb,
  "[noun] n'ent" is not 1841 French, and no noun in the battery's lexicon
  ends in the "nent" cluster as a separate word.
- Reading 88 as participle/infinitive under "ne" is ungrammatical
  ("ne" + participle excluded per battery-participle-60).
- The `12-06` = "nent" 3pl-ending parallel with "prennent" (70-12-06) is
  byte-exact: 26-12-06 = [26]+"nent", a 3pl verb form; 88-26-12-06 =
  [88]+[26]+"nent" = "[88][26]nnent" (cf. "prennent" = pre+n+ent).
- Candidate French shapes: viennent / tiennent / reviennent / deviennent /
  contiennent ("[88-26]" = vi/ti/revi/devi/conti + "en").

**Why the bar still fails at battery grade:**
- C1 FAIL (epistemic, not kill-grade): the finite form is demonstrably the
  FUSED unit 88-26-12-06 ("[88][26]nent", 3pl), but its lexical value cannot
  be named — 88's value is open and 26's value is open. Naming requires two
  open values to resolve jointly. "88 alone" has no finite form here.
- C2 FAIL (needs red-team authority): 26 must be WORD-INTERNAL here (stem
  extension, e.g. "-en-" in "[88]ennent"), which contradicts its noun-class
  LEAD elsewhere. That is a conditioned/positional behavior claim, and §7
  (67 et/veut is the sole true polyvalence) reserves it to the red team.
- Correlated cost: "62 ne [3pl]" needs 62 as a plural subject at this window,
  while 62-98 x5 needs 62 singular-compatible (98="vient" 3sg) — a second
  conditioned claim, also red-team's.

**Adverse answered:** 26's class is NOT resolved — fenced with stated cause:
noun-class lead holds elsewhere; word-internal here is a conditioned claim
requiring red-team authority. Not ignored, not decided.

## Verdict: NULL

C1 and C2 both fail; failures are epistemic (underdetermination + authority
limits), not falsifications. Not a kill: the fused-3pl parse is the unique
grammatical reading and nothing in the bytes rejects it.

## Follow-ups (for supervisor queuing)

1. `verb88-26-stem` (P2): test 88-26 as a verb stem across 88's 23 windows —
   which 3pl "-nent" verbs (viennent/tiennent/reviennent/deviennent) fit
   88-26's distribution; name the stem value iff one covers all 23 with
   zero hard contradictions.
2. `fuse-88-26-redteam` (P2): package for red-team adjudication: 88-26-12-06
   fusion, 26 word-internal (conditioned vs noun lead), 62 plural-subject
   (conditioned vs 62-98 3sg) — §7 authority required.
3. `subj-62-plural-94` (P3): test 62 as plural subject across the 62-94 x9
   windows; kill iff any window forces singular.

**Bookkeeping:** `battery-queue.json` `finite-88-ne` → status `verdict`,
result `null` (temp-file + rename, own entry only, pre-write assert confirmed
no prior verdict). Lock deleted on completion.
