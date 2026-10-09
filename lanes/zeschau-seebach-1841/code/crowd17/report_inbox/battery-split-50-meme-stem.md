# Battery `split-50-meme-stem` — verdict: PROMOTE (package only; §7 docket undecided)

Gather-only red-team input package for a 50 split/non-uniformity docket
item, mirroring the 52 treatment (`battery-split-52-redteam-input`,
PROCESSED) and the 97/09 splits. Locus-level evidence only. No value
named for 50, no split declared, no polyvalence claimed (red-team venue).
The non-uniformity observation is distributional, not a class claim.
Docket item is NOT decided at battery level.

## Bar tested (verbatim, pre-registered before testing)

"package the S7 venue question for the red team if the shape confirms
(cf. the 52/97/09 battery splits); fence, don't declare"

## Bar restated as numbered pass/fail clauses

- C1: The split shape confirms at battery grade — "même"-word parses at
  W3 (@380) and W9 (@1264) under standing values; verb-stem is forced at
  W10 (@1565) with "même" kill-grade dead there; the two arms are
  incompatible as a uniform named value.
- C2: The §7 venue question is packaged for the red team in the
  established split-package format (locus-level evidence, byte-exact
  0-based offsets, row labels, arms stated, adjudication question
  framed — not decided).
- C3: Fence — no split declared at battery level (the listed adverse:
  a battery must not declare splits; red-team venue only).

Adverses listed: "a battery must not declare splits: red-team venue only".

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/split-50-meme-stem.lock` on start
   (agent id + 2026-10-09T21:23:24Z); no prior/stale lock.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs /
   96 types asserted). `canonical.py` never used.
3. Adopted, not re-litigated, from parent `val-50-crosswindow` (NULL,
   2026-10-09): the 11-window census; the open-class uniform candidates
   (tente, porte, donne, danse, garde, …) parse all windows but are
   unnameable (parsing ≠ naming); W5 (@582) costs every candidate the
   same 1 unstated assumption; 50="ver" kill stands.
4. Tested the "même" fit at W3/W9 and the stem-forcing at W10 directly
   on the bytes, with corpus checks on the lane's 1841 corpus.
5. Standing values used as premises: pencil 11=la, 82=m, 29=er;
   24=finite-verb class (R17-009). 1841 diplomatic French throughout.

## Findings — arm packages

### Arm A — "même"-word at the two "la 50" loci (C1, part 1)

"11 50" ("la [50]") occurs exactly 2× stream-wide (census, byte-exact):

- `@379=11 @380=50 (a2_07)` — context:
  `@377=82 @378=48 @379=11 @380=50 @381=82 @382=16 @383=52`
  = "m [48] pour la [50] m [16] [52]…"
- `@1263=11 @1264=50 (a7_02)` — context:
  `@1261=09 @1262=01 @1263=11 @1264=50 @1265=46 @1266=69 @1267=88`
  = "[09] [01] la [50] que [69] [88]…"

With 50="même":

- W3: "…pour la même m'[16] [52]…" — "la même" (feminine, agrees with
  "la"); "m'" (82 pencil) elided object clitic before [16]. Parses with
  ≤1 unstated assumption ([16] vowel-initial for the "m'" elision, or a
  clause boundary between the complete PP "pour la même" and the new
  clause "m'[16]…").
- W9: "…la même que [69]…" — the standard French idiom "la même que"
  ("the same as"). Zero unstated assumptions; the idiom is attested
  8× in the lane's 1841 corpus ("la même que" token count).

Legs: (i) gender agreement la/même at both loci; (ii) the W9 idiom is
corpus-attested; (iii) "même" is a high-frequency word in the corpus
(22,788 tokens). The parent's idiomaticity ranking ("même" fits W3/W9
better than any stem candidate) is adopted, not re-litigated.

**Arm A PASS** — "même"-word parses at both "la 50" loci.

### Arm B — verb-stem forced at the single "50 29" locus (C1, part 2)

"50 29" ("[50]er") occurs exactly 1× stream-wide (census, byte-exact):

- `@1565=50 @1566=29 (a8_01)` — context:
  `@1563=71 @1564=60 @1565=50 @1566=29 @1567=24 @1568=74`
  = "[71] [60] [50]er [24] [74]…" (29="er" pencil ground truth)

With 50="même": "[71] mêmer [24]" — "mêmer" is **not a French word**.
Corpus check (lane's 1841 corpus, ~61M chars): **0 tokens** of "mêmer"
in 0 files. Kill-grade dead for "même" at W10.

With 50=verb stem (e.g. "tent-"): "[71] tenter [24]" — clean infinitive
(29="er" GT), [24] finite-verb class (R17-009). Parses with zero new
assumptions.

No rescue via composition: "71 50" = "[71] même" still leaves
"même"+"er" adjacent (adopted from parent; the corpus zero covers every
"même"+"er" spelling).

Legs: (i) "mêmer" corpus zero = kill-grade exclusion of "même";
(ii) stem+infinitive parse clean under pencil GT alone.

**Arm B PASS** — verb-stem forced at W10; "même" dead there.

### Incompatibility (C1, part 3)

- "même" is the unique idiomatic fit at W3/W9 and is kill-grade dead
  at W10. No single named value covers both arms.
- The uniform alternative is the parent's open class (feminine
  noun / -er verb stem: tente, porte, donne, danse, …) — every member
  parses all 11 windows identically, so none is nameable at battery
  grade (parent's C1 fail, adopted).
- The choice before the red team: (a) uniform open-class value
  (unnameable at battery grade), or (b) split — "même"-word at the two
  "la 50" loci vs verb-stem at the single "[50]er" locus.

**C1 PASS** — the split shape confirms at battery grade.

### The §7 venue question, framed not decided (C2)

For red-team adjudication:

> Does 50 split into a "même"-word tier at the two "la 50" loci
> (@380 a2_07, @1264 a7_02) and a verb-stem tier at the single "50 29"
> locus (@1565 a8_01) — a second polyvalence-class claim under §7 —
> or does a uniform (currently unnameable) open-class value hold
> across all 11 windows?

Evidence for the docket: Arm A and Arm B packages above (byte-exact
offsets, row labels, corpus counts: "même" 22,788 tokens; "la même que"
8 tokens; "mêmer" 0 tokens). Bigram exhaustiveness: "11 50" 2× (both
in Arm A), "50 29" 1× (Arm B). The remaining 8 of 50's 11 windows
(@209, @331, @442, @582, @662, @696, @942, @1813) are out of this
package's scope — the parent's per-window analysis stands for them.

**C2 PASS** — package delivered above.

### C3 — fence, adverse answered

No split is declared here. No 50 value is named. No polyvalence is
claimed. The listed adverse ("a battery must not declare splits:
red-team venue only") is answered by packaging only: this report
decides nothing; the docket item stays with the red team.

**C3 PASS.**

## Verdict: PROMOTE

All bar clauses pass and the listed adverse is answered. "Promote" here
means only this: the gather-only package is complete and handed to the
red team as input for the 50 split/non-uniformity docket item. It is not
a promotion of any 50 value, not a split declaration, and not a
battery-level decision of the docket item. No follow-ups per §4
(promote; no null).

## Scope / caveats

- Locus-level characterization only, mirroring the 52 treatment
  (`battery-split-52-redteam-input`).
- Canonical-stream caveat stands: pencil gloss on row a5_03; 68 of 70
  upstream row offsets unvalidated.
- W5 (@582, "ne mentent" rival) not re-litigated — the queued
  `mentent-580-rival` owns it.
- The parent's open-class enumeration and W5 assumption accounting are
  adopted, not re-decided.
- No standing/red-team verdict contradicted or downgraded; §7 intact.
- R5005, sealed gate instances, red-team adjudication queue untouched.

## Bookkeeping

- Stream re-derived in-session; asserts held (1,847 pairs, 96 types).
- `canonical.py` never used.
- Report: `code/crowd17/report_inbox/battery-split-50-meme-stem.md`
  (this file).
- `battery-queue.json`: `split-50-meme-stem` queued → verdict/promote
  via target-id-unique temp file + atomic rename; pre-write assert
  confirmed queued/verdictless; post-write JSON re-validated; own entry
  only; no downgrade.
- Lock `locks/split-50-meme-stem.lock`: created on start, deleted on
  completion (verified gone).
