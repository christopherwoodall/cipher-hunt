# Battery report: w2-5561-nece-frame

Target: `w2-5561-nece-frame`. Claim: fence W2 as a "ne ce"-driven residual,
or test whether any 55-61 value parses once ne-ce-1169's fence is accounted for.
Date: 2026-10-09. Worker: battery worker (subagent 6b722683).
Lock `locks/w2-5561-nece-frame.lock` created 2026-10-09T08:38:57Z (no stale
lock for this id; locks/ held unrelated live locks only); deleted on completion.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"resolve iff W2 fenced as a 'ne ce'-driven residual with stated cause, or a
55-61 value parses with the ne-ce-1169 fence accounted for"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. W2 is fenced as a "ne ce"-driven residual with stated cause.
2. A 55-61 value parses at W2 with the ne-ce-1169 fence accounted for.

Adverses (from queue): none listed.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed byte-exact per `code/side-keyhunt/repair_parse.py` (asserted 1,847
pairs / 96 types before testing). `canonical.py` never used. R5005, sealed
gate instances, red-team adjudication queue untouched. Every number below
re-derived in-session; no prior counts trusted.

Read first (adopted, not re-litigated): battery-x-55-61-candidate-list.md
(KILL, 2026-10-09) and battery-ne-ce-1169.md (NULL, 2026-10-08), per the
task brief.

Standing values used (protocol section 7): banked GT 11=la, 82=m, 40=e,
46=que, 70=pre, 34=i, 29=er; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout,
00=pour, 84=on, 47=ce; provisional 59=est, 77=le. Battery-promoted 94="ne"
(STRONG LEAD, R17-001) + 21 = noun class, 65 = noun class (registry).
61-94 word-final and 94-87 word-initial segmentation routes are explicitly
off-limits to this target: they belong to ne-ce-1169's follow-ups
(seg-61-94-word: null; nece-94-87-initial: kill) and to the queued
redteam-94-functional-split (priority 1). The 55-61-94 word-unit route
belongs to seg-55-61-94-word (null).

## Window-level evidence (re-derived)

W2 = @1167-1168, row a6_09 (offset 0, 41 raw digits, 20 pairs):

```
@1160:44 @1161:83 @1162:21 @1163:67 @1164:78 @1165:45 @1166:13
@1167:55 @1168:61 | @1169:94 @1170:87 @1171:83 @1172:21 @1173:85 @1174:36 @1175:74
```

Raw bytes of row a6_09: `00922980177782448321677845135561948783214`.
"5561" at raw index 28 (even) -> pairs 14/15 of the row; "9487" at raw
index 32 (even) -> pairs 16/17. Both pair-phase-aligned at even indices:
the 94-87 bigram is a real stream bigram, not an offset/phase artifact.

Under standing values: `...78-45("verdict" LEAD) 13(open) X(55-61) ne(94)
ce(87) 83(open) 21(noun-class) 85(open) 36 74` — i.e. "[verdict] [13] X
**ne ce** [83] [21-noun] ...".

Re-derived stream census: the 94-87 bigram occurs exactly **1x stream-wide**
(@1169-1170; 1/1847). 94's 37 windows confirmed (ne-ce-1169 census adopted
for the list; re-checked the bigram count only). The "ne ce" adjacency is
the fenced ne-ce-1169 hapax, sitting at @1169-1170 — immediately AFTER X's
span (@1167-1168), i.e. **outside X's span**.

## Clause 1 test — fence W2 as "ne ce"-driven residual, stated cause

Stated cause (adopted from ne-ce-1169, re-verified byte-side above): under
94='ne' STRONG LEAD + 87='ce' granted, @1169-1170 reads "ne ce". In 1841
diplomatic French this is ungrammatical: 'ne' is a preverbal negator clitic
that must immediately precede the verb (only clitic pronouns may intervene);
'ce' is a demonstrative pronoun/determiner, never a preverbal clitic
pronoun. No period construction places "ne" directly before "ce" as two
words (inversion "n'est-ce" puts the verb between; grammatical order is
"ce ne"). The right context (83 open with a 'de' lead, 21 noun-class) does
not rescue it: "ne ce de ..." is no better. The left context ("...verdict
[13] X") sits before the bigram and cannot license it.

Because the bigram is outside X's span, W2's grammaticality is
**X-independent**: every candidate class of X (verb, noun, adjective,
adverb, relative "qui", clitic, determiner) leaves "ne ce [83] [21]"
unparsed behind it. No value of X repairs the frame; no value of X changes
the frame. The window is therefore fenced as a "ne ce"-driven residual —
the driver is the fenced 94-87 hapax, not any property of 55-61.

Clause 1: **PASS**.

## Clause 2 test — does any 55-61 value parse at W2 with the fence accounted for?

With the ne-ce-1169 fence accounted for (94-87 kept as the fenced "ne ce"
bigram outside X's span, X-independent):

- The detachable-slot candidate space is already exhausted at kill grade
  (battery-x-55-61-candidate-list, adopted): at W2 specifically, a finite
  verb X gives "V ne ce" (kill grade); a noun X does not repair "ne ce";
  every other class dies at W1 or W3. Zero candidates survive W2 under the
  fence.
- Structural repair of the "ne ce" frame itself requires re-segmentation
  consuming 94 (61-94 word-final "...ne") or 87 ("néce-" word-initial):
  that OVERTURNS the fence rather than accounting for it. Those routes live
  with ne-ce-1169's follow-ups (seg-61-94-word: null, unresolved;
  nece-94-87-initial: kill) and with the queued redteam-94-functional-split
  — declaring them here would re-litigate battery verdicts, contradict the
  94='ne' STRONG LEAD caveats at battery level, and violate §7 (no second
  94 value without red-team declaration).
- The 55-61-94 word-unit ("reprenne" family) likewise dissolves the fenced
  bigram and belongs to seg-55-61-94-word (null) — off-limits.

No 55-61 value parses at W2 with the fence accounted for.

Clause 2: **FAIL (kill grade)** — the "55-61 value parses at W2" reading is
dead: the candidate space is exhausted, and the only structural rescues
overturn the fence and live elsewhere in the pipeline.

## Verdict: KILL

The bar's resolution arm is met via clause 1: **W2 is fenced as a "ne
ce"-driven residual with stated cause** (stream-unique 94-87 hapax at
@1169-1170, pair-phase-aligned, ungrammatical as negator + demonstrative in
1841 diplomatic French, outside X's span, hence X-independent). The "any
55-61 value parses at W2" arm is kill-grade dead (clause 2). This closes the
W2 loop chartered by x-55-61-candidate-list's kill verdict: W2 is a
"ne ce" residual, not a 55-61 window. Recorded as kill per lane precedent
(le611-reparse, frame-vient-parvenir): the window's value-parse reading is
killed and the fence is the resolution.

## Standing-verdict check

- ne-ce-1169 (null): adopted and untouched; this fence is inside its caveats.
- x-55-61-candidate-list (kill): consistent; this closes its W2 redirect end.
- 94='ne' STRONG LEAD (R17-001) / §7: untouched; no second 94 value declared,
  no polyvalence claimed. No standing or red-team verdict contradicted or
  downgraded.

## Follow-ups proposed (kill verdict — none required; residual cause already live)

No new targets queued. The W2 residual's ultimate cause (the "ne ce" hapax
itself) is already covered by live machinery: seg-61-94-word (null —
W2-rescue route unresolved), seg-55-61-94-word (null), redteam-94-functional-split
(queued, priority 1). Sibling w1-55-61-reseg (queued, priority 3) covers W1
re-segmentation. Nothing to regenerate.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-w2-5561-nece-frame.md
- Queue: `w2-5561-nece-frame` queued -> verdict/kill via temp-file + rename
  (pre-write assert confirmed queued/verdictless; JSON re-validated
  post-write; own entry only; no downgrade).
- Lock created on start (2026-10-09T08:38:57Z), deleted on completion.
- `canonical.py` never used. R5005, sealed gates, red-team adjudication queue
  untouched.
