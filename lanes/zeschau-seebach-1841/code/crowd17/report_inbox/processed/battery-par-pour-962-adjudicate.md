# Battery verdict: par-pour-962-adjudicate — "96 00" adjacency

Date: 2026-10-09. Worker: ecda4186-ea15-430c-8345-59b7158dc42c (clean re-run;
prior worker died in a runtime restart, lock cleared, no partial work found).

## Bar (verbatim from battery-queue.json)

"under granted 96=par / 00=pour, state whether any rescue parses (ellipsis,
re-segmentation, 96/00 re-value with red-team polyvalence declaration); kill
each rescue or fence the adjacency with cause. Gate for the le-86 subset
re-run."

### Numbered clauses (operative, pre-registered)

1. Ellipsis rescue: "et par [X] pour le [56]" parses with an elided,
   recoverable X — or the rescue is killed.
2. Re-segmentation rescue: some re-segmentation of "96 00" (one word,
   96 syllabic, 00 syllabic) parses on bytes — or the rescue is killed.
3. Re-value rescue: 96/00 re-valuation is statable — at battery level this
   needs red-team polyvalence declaration, so the clause is satisfiable
   only as a red-team escalation note, not a battery finding.
4. If no rescue parses: fence the adjacency with stated cause.

Listed adverses: none.

## Method

Parsed the repaired 1,847-pair stream exactly per
code/side-keyhunt/repair_parse.py (repaired_offsets.json +
data/upstream-ct_R5005.txt); canonical.py never touched. Full "96 00"
bigram census re-derived (n=3: @47, @465, @960 — 0-based). 96 follower
profile and 00 follower/predecessor profiles re-derived. Banked values used:
pencil 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce,
64=qui, 96=par, 17=fois, 79=tout, 00=pour, 47=ce, 84=on; provisional 59=est,
77=le. No R5005 contact, no sealed gates, no red-team queue contact.
1841 diplomatic French throughout.

## The adjacency (byte-exact)

- @960-961, row a6_00: "…67 96 00 86 56 41…" = "…et par pour [86] [56]…"
  (67="et": 96 not infinitive-shaped, positional rule).
- @47, row a1_01: "…62 96 00 92 79…" = "…[62] par pour [92] tout…"
- @465, row a2_10: "…42 96 00 33 79…" = "…[42] par pour [33] tout…"

96: n=21. Followers: 00 x3, 87 x3, 21 x3, 43 x2, 45 x2, 82 x2, 56 x1,
47 x1, 40 x1, 09 x1, 48 x1, 86 x1.
00: n=55. Followers: 86 x12, 33 x8, 66 x7, 92 x6, 97 x4, 11 x4, 46 x4,
36 x3, others x1.

96="par" parses 18/21 follower frames cleanly ("par ce" x4 incl. 87/47,
"par [noun]" with 21/43/56 nominal-class followers, "par le" @948).
The 3 failures are exactly the "96 00" windows. 00="pour" parses as
preposition+"pour"+INF in its dominant frames (00-33 x8, 00-86 x12);
at @465 "00 33" = "pour [33]" is already grammatical word-"pour" +
infinitive-class — the defect there is purely the "par" before it.

## Clause 1 — ellipsis: KILLED

"et par [X] pour le [56]" needs an elided complement of "par"
recoverable from context. French licenses no prepositional-complement
ellipsis (no VP-ellipsis equivalent; a "par"-complement cannot be
gapped). The nearest "par"-complement in the clause ("par ce que [24]"
@952-955, seven groups back) is not parallel and not recoverable by any
1841 ellipsis rule. Worse, the defect is systematic (3x) with different
would-be complements each time — no single elided element works across
@47/@465/@960. Kill-grade on grammar alone.

## Clause 2 — re-segmentation: KILLED

- 2a. "96 00" as one word: no French word "parpour" exists. KILLED.
- 2b. 96 syllabic (word-final "…par" + "pour…"): no French word of shape
  [X]par-pour[Y]; word-final "-par" is vanishingly rare and no candidate
  fits any of the three windows. KILLED.
- 2c. 00 syllabic ("pour-" prefix: "pourvoir"/"pourtant"/"pourquoi"):
  undemonstrable at battery grade. It needs 86="voi" at @962 (unratified
  battery lead), "par pourvoir le [56]" is strained ("pourvoir" needs
  "de" for the thing provided; absolute use is archaic even in 1841),
  and it fails to generalize: at @465 "00 33" is already grammatical
  word-"pour" + infinitive, so a prefix reading cannot be the uniform
  account of the adjacency. KILLED as a general rescue (@960 stays
  ambiguous "pourvoir"/"pour voir" per voir-86-sweep — cited, not
  re-litigated).

## Clause 3 — re-value: red-team escalation only

The defect localizes to 96, not 00 (00 parses as word-"pour" at @465).
The frame "96 00 X" (X = 92/33/86, then "tout"/noun) fits
"[ADJ] pour + INF/N": "prêt pour [INF]" is the canonical French frame
("et prêt pour le [56]", "[42] prêt pour penser"). 96="par" holds in
18/21 windows; the 3 "96 00" windows form an exceptionless conditioned
residue — the classic polyvalence signature. But 96="par" is GRANTED and
§7 bars battery-level polyvalence declaration (67 et/veut sole). Naming
the adjective ("prêt"/"bon"/"fait") from 3 windows with open neighbors
is underdetermined at battery grade. Recorded as red-team candidacy
only: `poly-96-par-adj` proposed below. No standing grant touched.

## Clause 4 — fence: TAKEN

The "96 00" x3 adjacency is fenced as a systematic residual with cause:
ungrammatical under granted 96=par / 00=pour at all three windows;
ellipsis killed on 1841 grammar; re-segmentation killed on bytes/lexicon;
the surviving hypothesis (96 conditioned second value) needs red-team
polyvalence authority. The fence is distributionally grounded: the
residue is exactly the "96 00" bigram, no more, no fewer.

## Gate consequence

le-86-subset-rerun (queued) is CONDITIONAL on this target "resolving
#16's L2 in favor of the determiner frame." This verdict does NOT so
resolve it — the "par pour" defect stands fenced, not dissolved. The
gate stays closed; the rerun must not run on this verdict.

## Verdict: NULL (fence executed per the bar's else-arm)

No rescue parses at battery grade; the adjacency is fenced with cause.
This is not a kill of any value: 96="par" and 00="pour" keep their
grants outside the fenced trigram.

## Follow-up targets (null regenerates work)

1. `poly-96-par-adj` (priority 2): red-team polyvalence adjudication —
   96="par" (18/21 windows, frames listed above) vs adjective
   ("prêt"-shaped) at exactly "96 00" x3 (@47/@465/@960). Package all
   21 windows of 96 with the "pour"+follower frames.
2. `pour-prefix-00-census` (priority 3): census 00's 55 windows for
   syllabic "pour-" legs ("pourvoir"/"pourtant"-shaped) to close rescue
   2c terminally.
3. Coordinate note (not a new target): le-86-subset-rerun stays queued
   with its condition unmet — gate closed per §Gate consequence above.

R5005, sealed gate instances, and the red-team adjudication queue were
not touched. No standing verdict contradicted or downgraded. 96
polyvalence NOT declared.
