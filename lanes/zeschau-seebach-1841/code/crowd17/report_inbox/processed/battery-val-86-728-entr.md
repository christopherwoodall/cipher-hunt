# Battery verdict: val-86-728-entr

- Target: `val-86-728-entr` (battery-queue.json, priority 3, status queued)
- Claim: name 86's value at @728: test 'entr' ('pour entrer' / 'entrer' x4 / 'entre[88]' compound)
- Adverses: none listed

## Bar (verbatim, pre-registered)

"value named iff the three 86 shapes ('pour [86]' x12, '[86]er' x4, '[86]e[88]' x1) converge on one stem with zero ungranted assumptions besides the value itself; 'entr' decides T3 (word-internal compound) and dissolves @730's finiteness question"

Numbered clauses:
- C1: The three 86 shapes converge on the stem 'entr' with zero ungranted assumptions (besides the value itself) → name 86='entr'.
- C2: 'entr' decides T3 (the word-internal compound at @728).
- C3: 'entr' dissolves @730's finiteness question.
- Else-arm (brief): if C1 fails, fence the value-naming.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/val-86-728-entr.lock` on start (agent 3d72415b-8973-4673-85ed-bf6ce98086fc, 2026-10-09T20:29:41Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 96 types, asserts held. `canonical.py` never used.
3. Byte-confirmed all loci below on the repaired stream.
4. Adopted, not re-litigated: `tier-86-867-prefix` PROMOTE (2026-10-09, queue verdict/promote) — 86 is prefix-tier at @867, stem-tier at the four "86 29" windows, tier-split is §7 red-team venue; `stem-86-29-value` NULL — "pour S+pre" ungrammatical for every -er stem S at the @867 frame; 70='pre' pencil GT; 29='er' pencil GT; 00='pour' granted (A9); 87='ce' granted; 48='e' promoted letter tier (R17-003); 86=['INF','cls'] registry. Naming precedent: parsing ≠ naming (`masc-noun-86-name`, `val-03-value-census`) — a value must be SELECTED over rivals, not merely compatible.

## Window-level evidence

Shape counts re-derived in-session (n(86)=32):
- 'pour [86]' x12: @553, @661, @728, @867, @889, @962, @1002, @1128, @1375, @1506, @1792, @1825.
- '[86]er' x4: @431, @1375, @1391, @1825.
- '[86]e[88]' x1: @728 (overlaps shape 1: "00 86 48 88").

### The @867 kill-grade block (shape 1)

@867 byte-confirmed: `@865=46('que') @866=00('pour') @867=86 @868=70('pre') @869=87('ce') @870=77('le')` = "que pour [86]pre ce le [89] e".

Under 86='entr', this window reads "pour entrpre ce le". Three readings, all dead:
- (a) Complete-word "entrer": "pour entrer pre ce le" — 70='pre' is a pencil-GT syllable, not a standalone word; "pre" dangles. Dead (adopted).
- (b) Word-internal "entr"+"pre" = "entrpre": not a French word. The standing tier finding licenses exactly one word-family for "Xpre": the -prendre compounds (comprendre, apprendre, surprendre, reprendre, entreprendre), with X ∈ {com, ap, sur, re, entre}. 'entr' is none of these. Dead at kill grade.
- (c) Stem-tier "pour S+pre": adopted `stem-86-29-value` NULL tested every -er stem S (including 'entrer') at this exact frame — all ungrammatical. Dead.

The only rescue is a conditioned split ('entr' everywhere except @867, where 86 is a -prendre prefix) — a §7 red-team act, i.e. an ungranted assumption at battery grade. The bar forbids it.

### @728 (shapes 1 + 3 overlap)

@728 byte-confirmed: `@726=11('la') @727=00('pour') @728=86 @729=48('e') @730=88 @731=11('la')` = "la pour entre[88] la".

Under 86='entr': "entre" + [88], word-internal per the bar's T3 framing. 88 is gov-class with no standing value/content. No French word of shape "entre"+[88] is constructible with standing values (entrevoir/entretenir/entreprendre all need ungranted 88 content). The compound is undecidable at battery grade — fenced, not killed.

### The 14 compatible windows

- '[86]er' x4 → "entrer": @431 ("[63] le entrer m [16]"), @1375 ("vient pour entrer [89] on"), @1391 ("er et entrer [89] [16]"), @1825 ("[97] pour entrer m [38]"). All parse.
- 'pour [86]' x10 (excl. @728, @867) → "pour entrer": @553, @661, @889, @962, @1002, @1128, @1375, @1506, @1792, @1825. The phrase parses at all ten. Two value-independent neighbor residuals noted, neither a shape-breaker: @889 ("pour entrer ent le tout" — the 06 attachment is independent of 86's value); @962 ("par pour entrer" — the "par pour" anomaly is upstream of 86, adopted from the pre-00 census).

## Per-clause pass/fail

- **C1 — FAIL**, on two independent grounds:
  - (1) @867 kill-grade excludes uniform 'entr' (see above). Convergence across the 'pour [86]' shape fails. The only rescue (§7 conditioned split) is an ungranted assumption under the bar.
  - (2) No selector: at the 14 compatible windows, 'entr' is compatible but not selected — every -er stem parses identically ("pour entrer"/"entrer" admit any stem; lane precedent: parsing ≠ naming). The sole potential selector is the @728 "entre"+[88] compound, which is undecidable (see C2).
- **C2 — FAIL**: the word-internal compound cannot be decided at battery grade; 88's content is open, so no complete French word is constructible with standing values.
- **C3 — moot**: depends on C2; @730's finiteness question stands untouched.

## Verdict: NULL (fence, evidentiary)

'entr' is not named. The value-naming is fenced — re-openable by (a) a conditioned re-test excluding @867, or (b) a named 88 completing the @728 compound. Uniform 86='entr' is kill-grade excluded at @867 (recorded as a finding, not a global kill: conditioned 'entr' at the stem-tier windows remains live but unselected).

## Scope

- Value-naming only, at the three shapes. Untouched: 86's INF class; stem-tier at the four "86 29" windows; prefix-tier at @867; the tier-split §7 candidacy and the queued `redteam-86-split-docket`; 88's class/value; @730's finiteness question (`fin-88-730-rerun`, `gov-88-730-modal`, `subj-88-730` all untouched); all standing and red-team verdicts — no contradiction, no downgrade, no re-litigation.
- Canonical-stream caveat stands (row a5_07/a4_08 offsets unvalidated).

## Follow-ups (for supervisor queuing; all verified ABSENT from battery-queue.json)

1. `val-86-entr-stemcond` (P3) — conditioned re-test: 'entr' at the stem-tier windows only ("86 29" x4 + "pour entrer" x10; @867 explicitly excluded per `tier-86-867-prefix`; @728 held as compound-pending). Bar: name 'entr' iff a standing selector picks it over rival -er stems with zero ungranted assumptions; else fence the conditioned naming. Feeds `redteam-86-split-docket`.
2. `val-88-730-content` (P4) — name 88's letter content at @730 with byte evidence; if 88 completes "entre"+[88] as a French word under standing values, re-fire 'entr' at @728 (this battery's C2/C3).
3. `sel-86-728-compound` (P4) — lexicon/corpus test: which French words have shape "entre"+X for plausible 88 values; narrows the 88-content search space for follow-up 2.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-86-728-entr.md`
- Queue: `val-86-728-entr` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-86-728-entr.tmp` + atomic rename; disk re-validated; own entry only; no downgrade)
- Lock `locks/val-86-728-entr.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
