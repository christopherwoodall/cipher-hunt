# Battery `wordbound-41-59-seg` — verdict: PROMOTE

## Bar (verbatim, pre-registered)

> "pass iff neighbor-class boundary rules select exactly one segmentation (@59-62 vs @59-63) over @58-64, else fence the segmentation as unforced"

Numbered clauses (pre-registered before testing, not modified after):

- **C1** — Neighbor-class boundary rules select exactly one segmentation (@59–62 or @59–63) over @58–64 → PASS (promote).
- **C2** — Else (no unique selection) → fence the segmentation as unforced → NULL.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing. Created
   `code/crowd17/next-token/locks/wordbound-41-59-seg.lock` on start
   (agent 39c7bddd-65c7-48da-8d9d-b82000ff2342 + 2026-10-09T21:32:00Z); no stale
   lock for this target existed.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py`
   (`[s[i:i+2] for i in range(o, len(s)-1, 2)]`, offsets from
   `code/side-keyhunt/repaired_offsets.json`, rows from `data/upstream-ct_R5005.txt`).
   Asserts held: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed
   gate instances, and the red-team adjudication queue untouched.
3. Adopted, never re-litigated: protocol §7 standings; 08-position-profile PROMOTE
   (battery-grade boundary rules); 94='ne' STRONG LEAD; ce-08-31-frame
   (standalone single letter kill-grade dead); letter-41-dist2-tri NULL
   (W1 letter arm fenced pending 08's banking); letter-41-08-rerun NULL
   (08's letter value unbanked at ratified grade — 08='t' is battery-grade only,
   so 08 is treated as value-open here).

## Locus byte-confirmed (0-based, row a1_01)

`@54–67 = 85 58 35 53 12 41 08 34 29 40 12 94 92 69`

i.e. `@58=12('n') | @59=41 @60=08 @61=34('i') @62=29('er') @63=40('e') | @64=12('n') | @65=94('ne')`.

The two candidate segmentations (under the letter-tier hypothesis for 41/08):
- **A: @59–62** = "41,08,i,er" (??ier-shaped word)
- **B: @59–63** = "41,08,i,er,e" (??ière-shaped word; the "prière" reading needs this)

## Adopted neighbor-class boundary rules (battery grade)

- **R1** (08-position-profile PROMOTE): a word boundary is forced after/before a
  banked/promoted free word (17=fois, 47=ce, 67, 87=ce).
- **R2** (08-position-profile PROMOTE): a bound letter after 08 (34='i', 29='er')
  constrains 08 to initial-or-internal — never word-final.
- **R3** (08-position-profile PROMOTE): 40='e' has no battery-grade bound/free
  ruling → boundaries adjacent to 40 are boundary-dependent, not forced.
- **R4** (ce-08-31-frame, kill grade): a standalone single letter cannot be a
  word — every letter-tier cell must compose into a multi-letter word or a
  licensed elision.
- **R5** (protocol §7): 94='ne' STRONG LEAD — 94 is the complete word "ne".

## Findings

### Right edge (@63|64|65): segmentation B is eliminated

@65=94 is the complete word "ne" (R5). @64=12='n' is a letter-tier cell. Rightward
fusion is unlicensed on two independent grounds:
1. "n"+"ne" = "nne" is not a French word (no composition).
2. Elided "n'" (cf. @702 "12 98" = "n'importe") requires a vowel-initial follower;
   "ne" is consonant-initial ('n'). No elision.

Therefore the boundary **@64|65 is forced by neighbor-class incompatibility**
(letter 'n' vs complete word "ne"), and @64 must be word-final.

- Under **B** (@59–63 word), @64='n' would stand as a single-letter word →
  kill-grade dead by R4. **B is eliminated.**
- Under **A** (@59–62 word), @63–64 = "e"+"n" = **"en"**, a French word. Viable.
  (Note: the resulting "en ne" @63–65 is attested 43× in the lane's 1841 corpus,
  in the "en ne + participle/verb" frame — e.g. "en ne faisant", "en ne pourra";
  grammatical, with @66=92 needing a verbal reading, which is open.)

R2 is satisfied by A (08 internal in "41,08,i,er"). R3 does not forbid 40='e' as
word-initial of "en".

### Left edge (@58|59): no third segmentation

@58=12='n'. Rightward fusion into the 41-word would give @58–62 = "n,41,08,i,er"
("n??ier"-shaped). Corpus check (97 files, ~61M chars): **zero genuine common
French words** of this shape — the only hits are proper-noun/OCR noise
("Napier" 299× = Commodore Napier; "Nodier" 93× = Charles Nodier; "nizier",
"ndiier", "nalier", "narier" ≤12×, fragments). Rightward fusion is dead, so the
boundary **@58|59 is forced** and @58 is word-final of a leftward word
("...53 n"; 53 unvalued — possible, not ruled out). The 41-word starts exactly
@59; @58–62 and @58–63 ("n??ière": none, adopted from parent) are not viable.

### Middle (@62|63): unique survivor

B is eliminated (right edge). A (@59–62) is the unique compositionally viable
segmentation. The word inventory under A (08 value-open at ratified grade):
**acier** (45 corpus hits), **osier** (7), **trier** (12), **crier** (133),
**prier** (214), **scier** (4) — 41 unforged among {ac,os,tr,cr,pr,sc}.
(For reference only: under unratified battery-grade 08='t', the inventory would
be {entier, sentier}; not used — 08 stays open per the gate-trigger rule.)

## Per-clause pass/fail

- **C1: PASS** — Neighbor-class boundary rules (R4+R5 forcing @64|65; R4 killing
  single-letter 'n'; corpus killing @58–62 rightward fusion) select exactly one
  segmentation: **@59–62**. The "prière" reading, which requires @59–63, is
  **not segmentally viable**.
- **C2:** moot (C1 passed).

## Adverse answered

- **"The 6 @59-62 rivals (acier/osier/trier/crier/prier/scier) fence honestly":**
  confirmed with corpus counts (above). They are fenced honestly — acknowledged,
  not hidden. They block WORD-NAMING (41's value stays unforged), which is
  letter-41-08-rerun's (fenced) bar, not this bar. This bar tests SEGMENTATION
  selection only; the rivals do not un-select @59–62. The word's identity remains
  open with 6 rivals.

## Verdict

**PROMOTE** — the segmentation at W1 is forced to **@59–62** under the letter-tier
hypothesis. The @59–63 segmentation (and with it the "prière" reading) is fenced
as segmentally non-viable.

## Scope

- **Conditional on the letter-tier hypothesis** for 41/08 at W1. This does NOT
  adjudicate 41's class (split package untouched, R20-108), does NOT bank 08's
  value (stays open at ratified grade), and does NOT overturn letter-41-dist2-tri's
  NULL ("keep 41 outside the letter tier" — an evidentiary fence pending 08's
  banking, compatible with this conditional result).
- Decides letter-41-dist2-tri follow-up 3's question: "prière" (41=p) is not
  segmentally viable.
- Untouched: all standing/red-team verdicts, §7, R5005, sealed gates, red-team
  adjudication queue. Canonical-stream caveat stands (row a1_01 offset
  unvalidated).
- No follow-ups (promote per §4). Word-naming awaits the already-queued
  `letter-41-08-rerun-rearm` (fires once a red-team round banks 08's value);
  not duplicated.

## Bookkeeping

- Lock created: `code/crowd17/next-token/locks/wordbound-41-59-seg.lock`
  (agent 39c7bddd-65c7-48da-8d9d-b82000ff2342 + 2026-10-09T21:32:00Z); no stale
  lock present. Deleted on completion (verified below).
- Report: `code/crowd17/report_inbox/battery-wordbound-41-59-seg.md` (this file).
- Queue: target `wordbound-41-59-seg` set to status `verdict` (PROMOTE) —
  own-entry-only temp-file+rename write, pre-write assert queued/verdictless,
  JSON re-validated, no downgrade.
