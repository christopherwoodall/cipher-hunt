# Battery verdict: s5-la-tout-adjudicate

**Target:** `s5-la-tout-adjudicate` (priority 1)
**Date:** 2026-10-08
**Worker:** a659c4ee-7b58-4f72-8169-ca8bdeb676e1

## Bar (verbatim from battery-queue.json)

> pass iff 'la tout' @52-53 is shown grammatical under banked values with a stated, non-ad-hoc analysis, or 79@53 / the segmentation is corrected with evidence; else fence with the contradiction documented for the red team.

Numbered clauses:
1. 'la tout' @52-53 shown grammatical under banked values (11=la, 79='tout') with a stated, non-ad-hoc analysis — OR —
2. 79@53's 'tout' value or the a1_01 segmentation corrected with evidence.
3. Failing (1) and (2): fence, documenting the contradiction for the red team.

Adverses (must be answered, not ignored): S5 standing fence; banked values
(11=la, 79='tout') are not re-litigated at battery level — fence, never decide
(§7); the five-window bar cannot be satisfied by any 37 value until this resolves.

## Method

Read BATTERY-PROTOCOL.md first; created
`code/crowd17/next-token/locks/s5-la-tout-adjudicate.lock` on start. All counts
re-derived from the repaired 1,847-pair stream
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed
per `code/side-keyhunt/repair_parse.py`; `canonical.py` never touched). R5005,
sealed gates, and the red-team queue untouched.

## Window-level evidence

Row a1_01 raw digits (71 digits, odd length):
`08913964410124884381306296009279371179855835531241083429401294926913246`
Repaired offset for a1_01: **0** (bedrock grade PROBABLE, LOO +6.49 nats —
`code/crowd18/report_inbox/processed/offset-validation.md`; bedrock ruling
2026-10-08: no offset currently requires change).

Under offset 0, a1_01 occupies global pairs @35–@69; the window is global
@49–@54: `92 79 37 11 79 85` = `...[92] tout [37] la tout [85]...`.
The clash bigram is **@52–53 = `11 79` = "la tout"**.

Fresh distributional facts (re-derived):
- `11 79` bigram is a **hapax**: 1 occurrence on the whole stream, at @52
  (11 has 45 followers; 79 has 18 occurrences).
- 79's top predecessors: 92 x2, 64 x2, 02 x2, 33 x2, 94 x2, 11 x1 — no
  determiner-frame pattern anywhere else.
- 11's top followers: 00 x4, 24 x4, 92 x3, 52 x3 — all verb/particle-shaped;
  79 is 11's only nominal/adverbial follower.

## Per-clause results

**Clause 1 (grammatical analysis under banked values): FAIL.**
Exhausted the 1841 diplomatic French parse space for "la tout":
- article "la" (fem.) + adjective "tout" (masc.): gender clash; feminine
  requires "toute".
- article "la" + pronoun/noun/adverb "tout": *"la tout"* is not a French
  constituent ("le tout" as nominal is masculine; *"la tout"* impossible).
- clitic "la" + "tout" + verb-stem (85): the only licit clitic–tout–verb
  pattern is "l'a tout mangé" (auxiliary between clitic and "tout"); bare
  "la tout <stem>" has no parse.
- "tout" as adverb before 85 (verb-stem, A3 frame): "tout" never modifies a
  finite/infinitive verb directly in 1841 French.
- clause boundary "la | tout": "la" must complete a constituent — as article
  it needs a feminine noun (next token is masculine "tout": clash); as enclitic
  it needs a preceding imperative (forces 37=imperative AND a second boundary
  after 79: "…tout. V-la! Tout 85…"), stacking 2–3 boundaries in five tokens —
  special pleading, not a stated principled analysis.
- ellipsis rescue ("la [chose] tout [entière]"): ad hoc, no 1841 diplomatic
  precedent, barred by the bar's own "non-ad-hoc" requirement.
- word-internal rescue (79@53 as syllable "tout-" of a longer word with 85):
  re-litigates the A5 banking granularity (79 banked as word 'tout') — barred
  by §7 at battery level.

**Clause 2 (value/segmentation correction with evidence): FAIL at battery
grade.** a1_01 offset 0 is bedrock-PROBABLE (+6.49 LOO) with "no offset
currently requires change." Offset 1 *would* dissolve the clash (no 11–79
adjacency anywhere in the row under offset 1), but adopting it on the strength
of one window is ad hoc: it re-pairs all 35 pairs of the row and must overcome
the bedrock LOO margin with independent evidence, which this battery does not
have. 79@53's 'tout' value cannot be corrected without re-litigating banked
A5 — barred by §7.

**Clause 3 (fence): PASS.** The contradiction is real, V-independent (11–79
does not involve 37), segmentation-robust under the standing offset, and
unresolvable at battery level without violating §7 or the bedrock offset
grades.

## Verdict: NULL

Neither pass branch is achievable at battery grade. Fenced per clause 3.

**Headline for the red team:** banked 11='la' (pencil ground truth) +
banked 79='tout' (A5) produce a kill-grade ungrammatical hapax bigram at
@52–53 on a bedrock-PROBABLE row. The three exits are: (a) revise a banking,
(b) revise the a1_01 segmentation against the +6.49 LOO grade, or
(c) accept an unexplained hapax. Battery level cannot choose.

No standing verdict contradicted or downgraded. The S5 fence is untouched;
the five-window bar remains unsatisfiable by any 37 value until the red team
rules.

## Follow-ups (null regenerates work)

1. `redteam-la-tout-fence` (P1, red-team venue): present the fenced
   contradiction — banked 11='la' + banked 79='tout' → kill-grade "la tout"
   hapax @52–53 on PROBABLE-offset a1_01; ask red team to choose between
   banking revision, segmentation revision, or accepted hapax.
2. `seg-a1_01-offset1-test` (P2): full-row battery testing a1_01 offset 1
   vs 0 with independent evidence (formula checks, crib-adjacent rows);
   offset 1 dissolves the clash but must beat the +6.49 LOO bedrock grade —
   do not run as a single-window rescue.
3. `homophone-79-split` (P2): test whether 79 needs a declared homophone
   split (word-'tout' vs syllable-'tout'); §7 — needs red-team declaration,
   do not declare at battery level.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-s5-la-tout-adjudicate.md` (this file)
- Queue: `battery-queue.json` — target `s5-la-tout-adjudicate` → status
  `verdict`, result `null`, date 2026-10-08 (own entry only, temp-file +
  rename; no prior verdict existed, no downgrade)
- Lock `locks/s5-la-tout-adjudicate.lock` created on start with agent id +
  UTC timestamp, deleted on completion.
