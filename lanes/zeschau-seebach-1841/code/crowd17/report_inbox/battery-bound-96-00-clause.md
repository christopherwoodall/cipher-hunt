# Battery verdict: bound-96-00-clause

Target: `bound-96-00-clause` (priority 3).
Date: 2026-10-09.

## Bar (verbatim from battery-queue.json)

"the adverb arm revives iff a byte-evidenced clause boundary lets 'par' strand with an elided complement; fence iff no boundary evidence exists"

Restated as numbered clauses:

- **C1 (revive arm):** a byte-evidenced clause boundary exists between @47 (96='par') and @48 (00='pour'), letting 'par' strand with an elided complement — the 62-adverb arm revives.
- **C2 (fence arm):** no such boundary evidence exists — fence @47–@48 as boundary-less at battery grade; the 62-adverb arm stays closed.

Adverse: "elided complement ungrammatical in 1841 French -- state the evidence, do not assume".

## Method

Read BATTERY-PROTOCOL.md first. Lock `locks/bound-96-00-clause.lock` created
on start (agent id + UTC timestamp), deleted on completion.

Re-derived the repaired stream in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py`:
**1,847 pairs, 96 types confirmed**. `canonical.py` never touched. R5005,
sealed gates, red-team queue untouched.

Offsets below are 0-based stream indices unless stated. The target window is
0-based @44–48 = "81 30 62 96 00" (1-based @45–49), all on row a1_01.

Standing values used: 96='par' (banked GT), 00='pour' (A9-granted, leg-1
class-level), 30='pas' (promoted), 94='ne' (STRONG LEAD R17-001).

## Window census

"96 00" occurs exactly **3x** stream-wide (0-based), ±6 context:

1. **@47** (row a1_01): `... 24 88 43 | 81 30 62 96 00 | 92 79 37 11`
   = "[88] [43] [81] pas [62] par pour [92] tout [37] la"
2. **@465** (row a2_10): `... 02 79 87 11 59 42 | 96 00 | 33 79 80 06`
   = "tout ce la est [42] par pour [33] tout [80]-ent"
3. **@960** (row a6_00): `... 46 24 85 04 20 67 | 96 00 | 86 56 41 19`
   = "que [24] [85] [04] [20] [67] par pour [86] [56] [41] [19]"

All three are **mid-row**: no row boundary between the 96 token and the 00
token at any window. The cipher has no punctuation anywhere. No formula
boundary, no gloss anchor, and no byte-level segmentation marker exists at
any of the three contacts.

## Clause results

- **C1 (revive arm): FAIL.** No byte evidence for a clause boundary between
  @47 and @48, nor at the other two "96 00" contacts:
  - Row boundary: absent (all three windows fully mid-row: a1_01, a2_10, a6_00).
  - Punctuation/marker: the cipher carries none anywhere.
  - Corpus license: an elided prepositional complement ("par ___") is
    ungrammatical in French at any period — "par" requires an overt nominal
    complement. Stated as evidence, per the adverse: French prepositions do
    not strand with elided complements (unlike English preposition stranding);
    no 1841 diplomatic-French license exists. There is therefore no frame in
    which a boundary *would* license the observed string — the revive arm
    fails on evidence, not on unexamined alternatives.
  - Compositional one-word: "parpour" is not a French word.
- **C2 (fence arm): FIRES.** @47–@48 fenced as boundary-less at battery grade.
  The 62-adverb arm at @46 stays closed (its word-class inventory is now
  exhausted: adverb fenced by battery-adv-62-pas-par, participle fenced by
  battery-part-62-46-slot).

## Standing-state check

- No standing verdict contradicted or downgraded. §7 intact (no polyvalence
  declared; 67 et/veut remains the sole declared polyvalence).
- The "par pour" x3 string is a **systematic anomaly**, not a one-window
  artifact: 96's other successors (00 x3 vs 87 x3, 21 x3, 43 x2, 45 x2, 82 x2,
  ...) all admit complement parses under standing values. Only the 00
  follower is complement-less.
- Documented for the red team (not re-opened here): battery-contre-00 found
  00='contre' parses all three "96 00" windows as **"par contre"** (Littré-
  attested 19th-century French); the battery could not promote it because A9
  grants 00='pour'. Whether a conditioned 00 value after 96='par' is granted
  is a red-team act. This fence does not decide it.
- Canonicality caveat: a1_01's row offset is among the 68 unvalidated
  upstream offsets. seg-a1_01-constraint-sweep (PROMOTE, 2026-10-09) found
  offset-1 constraint-clean on a1_01, but adopting it is a red-team
  adjudication act — not tested here. Under the standing repaired stream the
  fence holds.

## Verdict: NULL (fence executed)

The revive arm fails on byte evidence; the fence arm fires. The @47–@48
contact is fenced as boundary-less at battery grade. The "par pour" x3
anomaly is packaged for the red team via the conditioned-00 question, which
this battery does not touch.

## Follow-ups proposed (for supervisor queuing)

1. `contre-00-condition-gate` (P3) — re-test "par pour" x3 iff the red team
   rules on a conditioned 00='contre' after 96='par' ("par contre" leg from
   battery-contre-00; do not duplicate it).
2. `par-96-complement-census` (P4) — census all 21 of 96's windows: is 96
   ever complement-less elsewhere? Hardens the "par pour" x3 uniqueness.
3. `pour-00-leftedge-census` (P4) — census 00's predecessors stream-wide: does
   00 ever open a clause? Tests whether the boundary arm could have a family
   elsewhere.

## Bookkeeping

- Lock `locks/bound-96-00-clause.lock` created on start, deleted on completion.
- `battery-queue.json`: `bound-96-00-clause` queued → verdict/null via
  temp-file + rename (pre-write assert: status queued, no prior verdict;
  JSON re-validated post-write).
- No standing verdict contradicted or downgraded. `canonical.py` never used.
  R5005, sealed gates, red-team queue untouched. §7 intact.
- Stream: 1,847 pairs / 96 types re-derived in-session; every number above
  traces to it.
