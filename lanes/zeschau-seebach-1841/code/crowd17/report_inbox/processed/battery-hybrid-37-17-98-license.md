# Battery verdict: hybrid-37-17-98-license — NULL (fence executed)

- Target id: `hybrid-37-17-98-license` (battery-queue.json, priority 4, status queued)
- Claim: Test whether the k=34 local reparse `37 17 98` ("[37] fois [98]") can be grammatically licensed as a locus-level reading — it is the cheapest clash-removing edit and mirrors the offset-1 dissolution.
- Date: 2026-10-09
- Worker: battery worker (subagent d70c4d3f-92a5-4504-9dc9-22d04e7f0948)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`; asserts held — 1,847 pairs, 96 types).
  `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/hybrid-37-17-98-license.lock`
  (created at start 2026-10-09T20:49:53Z, deleted on completion; no prior/stale lock).

## Bar (pre-registered BEFORE testing)

The queue entry's `bars` field is `None` (no pre-registered bar text). Per
BATTERY-PROTOCOL.md §2, the bar is taken from the claim as stated, fixed
before testing and not modified after:

> **C1.** The k=34 local reparse `37 17 98` ("[37] fois [98]") is
> grammatically licensed as a locus-level reading at battery grade — every
> word parses under standing values with zero ungranted assumptions.
> **C2.** Else arm: fence the locus-level licensing with stated cause
> (which sub-parse fails and on what standing result).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock on start, deleted on completion.
2. Re-derived the repaired stream in-session (asserts held).
3. Byte-verified the k=34 edit on row a1_01's raw 71 digits:
   `08913964410124884381306296009279371179855835531241083429401294926913246`
   - digits 34–35 = `11` (the doubled 1s); dropping digit 34 → 70 digits.
   - Off0 pairs 14–21: `92 79 37 11 79 85 58 35` (clash `11 79` at in-row 17–18).
   - Hybrid pairs 14–21: `92 79 37 17 98 55 83 55` — clash gone.
   - Locus = hybrid in-row pairs 15–19: **`79 37 17 98 55`**.
4. Standing values at the locus (adopted, not re-litigated):
   - 79 = 'tout' (A5, whole word); 37 = predicative-frame cell (A1), value open;
   - 17 = 'fois' (promoted); 98 = finite clause-head verb ('vient' LEAD,
     battery-promoted pending ratification; distributional function PROMOTE);
   - 55 = verb class (R19-079, "prend" bare finite stem), value open.
5. Tested every grammatical decomposition of `[37] fois [98]` against
   standing battery results (all adopted, none re-litigated).

## Window-level evidence

### The locus (byte-confirmed)

Hybrid in-row pairs 15–19 (global 0-based @50–54):
`79('tout') 37 17('fois') 98('vient'-lead) 55(verb-class)`.
Stream facts: `37 17` occurs **0×** stream-wide; `17 98` occurs **1×**
(@837); `98 55` occurs **1×** (@1284).

### Decomposition attempts (all fail at battery grade)

**A1. "[37] fois" = NP (determiner/number/adjective + "fois"), NP as subject
of "vient".** FAIL — three independent sub-failures:
- 37 as determiner: zero legs; anti-distributed — 37 *precedes*
  determiners (`37 11` ×2, `37 77` ×2 with 11='la' GT, 77='le' provisional).
- 37 as number: zero legs anywhere in n(37)=28 profile.
- 37 as attributive adjective: **FENCED at battery grade** —
  `adj-37-independent-slot` (2026-10-09): no clean "37 [granted-noun]"
  window exists; the sole candidate (@620, "37 76") is contaminated by the
  live S5 rival (37="le").

**A2. "37 17" as one word.** FAIL — `37 17` is 0× stream-wide and
`x17-wordbound-audit` (PROMOTE, 2026-10-09) establishes 17="fois" as
**uniformly standalone** (word boundary both sides, 15/15 windows). The
"toutefois"-type rival is fenced: A5 fixes 79="tout" as a whole word, and
"79 17" = "toutefois" was already fenced at @452/@1461.

**A3. "fois" as subject of "vient" ("fois vient").** FAIL at
grammaticality grade — `bare-subj-corpus` (PROMOTE, 2026-10-09): **zero**
bare common-noun finite-verb subjects in ~61M chars of 1841 French (77
genuine hits, all proper nouns). "fois" is a common noun.

**A4. "fois" as bare temporal adverbial.** FAIL — zero legs; all 15
standalone-"fois" windows sit in determined/quantified NPs ("la fois",
"une/deux/trois fois", "la première fois").

**A5. "tout [37]" = adverb + predicative adjective, then bare "fois".**
"tout [37]" is licensable in principle (A5 + A1-adjective), but "fois"
still needs a role → collapses to A3/A4. FAIL.

**A6. "[98] [55]" = "vient [55]".** FAIL — 55 is not in 98's licensed
complement inventory {83='de' ×5, 00='pour' ×3, 82='m' ×3}
(`boundary-98-839` PROMOTE, n=40 census); 55 is verb-class ("prend" finite
stem, R19-079), so "vient [55-fin]" strands two finite verbs with no
conjunction. Clause-boundary rescue ("vient. [55]…") needs a subject for
55 — none exists.

**A7. The off1 "mirror" via clause boundary ("[37] fois | [98] [55]").**
FAIL — the mirror is weaker than the claim implies:
`seg-a1_01-constraint-sweep` (PROMOTE) licensed off1's `71 17 98` only as
*constraint-clean* ("no forced ungrammaticality ('fois [98-verb] [55]'
admits a clause boundary)") — it never positively licensed "[71] fois
[98]" as a grammatical constituent. Here, "[37] fois" as a complete
constituent still needs A1 (fails) and "[98] [55]" still needs A6 (fails).

### Adverses

Queue entry lists `adverses: None`. External tension noted, not an
adverse: the hybrid parse itself was already **KILLED at battery grade**
by `seg-a1_01-hybrid-phase` (best clash-removing cut −4.83 nats vs the C2
bar). This battery fences only the narrower locus-level licensing
question and does not re-litigate that kill. No standing or red-team
verdict contradicted, downgraded, or re-litigated; §7 intact.

## Per-clause results

- **C1 (licensed at battery grade): FAIL** — all seven decompositions fail;
  no parse of `[37] fois [98]` survives under standing values with zero
  ungranted assumptions.
- **C2 (fence arm): FIRES** — the locus-level licensing is fenced with
  stated cause per decomposition above.

## Verdict: NULL (fence executed)

The k=34 local reparse's `37 17 98` window cannot be grammatically
licensed at battery grade. The fence is evidentiary: it re-opens if (i)
the red team adjudicates 37's class/value (S5 or the @620 adjective
re-run), (ii) a second selective leg names "fois" a licensable subject /
adverbial role, or (iii) 55 is re-classed so "vient [55]" parses.

## Follow-ups (§4; all verified ABSENT from battery-queue.json)

1. `hybrid-37-rerun-s5` (P4) — re-test the `37 17 98` licensing if the red
   team adjudicates 37's class/value (`s5-37-385-adjudicate` or
   `adj-37-76-rerun` queued); gated on the red-team ruling.
2. `fois-vient-subject-corpus` (P4) — corpus census of bare "fois" as
   subject of "venir" in 1841 French; a zero hardens A3 to grammaticality
   grade (currently adopted from `bare-subj-corpus`'s common-noun zero).
3. `vient-55-complement` (P4) — test whether verb-class 55 ("prend"-shaped)
   can follow "vient" under any licensed frame (e.g. infinitive re-class
   of 55 → "vient prendre"); a licensed "vient [55]" re-opens the right
   edge (A6).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-hybrid-37-17-98-license.md` (this file)
- Queue: `hybrid-37-17-98-license` queued → `verdict`/`null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; target-id-unique tmp
  `battery-queue.json.hybrid-37-17-98-license.tmp` + atomic rename;
  disk re-validated; own entry only; no downgrade)
- Lock `locks/hybrid-37-17-98-license.lock`: created on start, deleted on
  completion (verified gone). R5005, sealed gates, red-team adjudication
  queue untouched. Canonical-stream caveat stands (row a1_01 offsets
  unvalidated).
