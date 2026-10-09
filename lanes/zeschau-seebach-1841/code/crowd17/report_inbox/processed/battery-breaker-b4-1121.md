# Battery report: breaker-b4-1121 — resolve '06 14 06' @1121

Worker: 50baef95-0474-4ffe-a448-d6dec79d51e7 | 2026-10-09T01:46:38Z–01:58Z
Target: `breaker-b4-1121` (priority 2). Lock `locks/breaker-b4-1121.lock` created
on start, deleted on completion. No prior lock existed.

## Bar (verbatim, pre-registered)

"resolve iff a clause boundary is demonstrated with punctuation-independent
evidence, or 14 takes a value grammatical between two promoted 'ent'
verb-endings; else confirm as a genuine word-boundary residual"

Numbered clauses (fixed before testing):
- C1: A clause boundary is demonstrated at @1120|1121 or @1121|1122 with
  punctuation-independent evidence (row-boundary coincidence, distributional
  clause-initial profile of 14, or parallel punctuated frame). PASS iff such
  evidence is produced.
- C2: 14 takes a value V such that the '06 14 06' surface at @1121 is
  grammatical French. PASS iff V is stated and the full local window parses
  under standing values with no ungranted assumption beyond the stated V.
- C3 (else): The breaker is confirmed as a genuine word-boundary residual —
  i.e. the anomaly is an artifact of segmentation assumptions, with the true
  segmentation stated and evidenced.

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
(1,847 pairs verified; `canonical.py` never used). R5005 untouched. @-offsets
are 0-indexed pair positions (queue convention). Standing values: 11=la,
70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (pencil); 06=ent (promoted);
12=n (banked); 87=ce, 64=qui, 00=pour, 30=pas (promoted); 59=est, 77=le
(provisional). 1841 diplomatic French throughout.

## Window evidence (@1121, row a6_07, row-relative position 8)

Surface pairs @1116–1131:
`11 88 70 12 06 | 14 | 06 11 52 37 43 00 86 52 37 86`
la [88] pre n ent [14] ent la [52] [37] [43] pour [86] [52] [37] [86]

Distributional facts (all re-derived, none trusted):
- n(14) = 15; @-offsets re-derived independently and match tout-slot-14
  exactly: 72, 84, 117, 141, 178, 339, 424, 458, 586, 623, 813, 896, 1121,
  1365, 1689.
- "14 06" bigrams: exactly 2 — @84 (`16 14 06 88`) and @1121. Both are
  "[14]ent"-shaped (14 word-initial before 'ent'), never "[14]" standalone
  before 'ent'.
- "06 14 06" trigram: unique to @1121 on the whole stream.
- "06 14" bigram: unique to @1121. "14 06" never recurs with a 06
  predecessor elsewhere.
- "70 12 06" trigram: unique @1120 ("pre-n-ent"). "12 06" x2: @1120 and
  @1709 (`26 12 06 29` = "[26] n-ent er", verb-adjacent) — consistent with
  12-06 = "nent" verb-ending material.
- @84 and @1121 are mid-row (row-relative 14 and 8); no row boundary within
  5 pairs on either side. The rubbed-out interlinear glosses (DECODE record
  note) supply no punctuation evidence anywhere on the stream.

Candidate parses of the trigram:
- (a) "[12]ent | [14] | ent-la…": word3 = "ent-la" — no such French word.
  DEAD (re-confirms tout-slot-14's finding; not re-litigated, cited).
- (b) "[12]ent[14] | ent-la…": same "ent-la" defect. DEAD.
- (c) "[12]ent | [14]ent | la…": "[14]ent" must be a French word. "souvent"
  (14="sou") gives "…prennent souvent la…" — textbook 1841 French
  ("prendre souvent la parole"). "content"/"présent"/"absent" as "[14]ent"
  are ungrammatical here ("prennent content la" — adjective with no
  agreement host). Only the adverb "souvent" fits the verb–adverb–article
  frame. LIVE.
- (d) One-word "[12]ent[14]ent…": no French word "…ent[14]ent…" with 12="n"
  banked ("entente" would need 12="t"). DEAD.
- Clause boundary @1120|1121 ("…prennent | souvent la…"): not a clause
  boundary — the adverb continues the clause. No boundary needed or
  evidenced. Boundary @1121|1122: strands "ent-la". DEAD.

The "souvent" parse (c) under standing values:
"…[70]-[12]-[06] (= pre-n-ent, 'prennent'-shaped, 3rd-plural verb) |
[14]-[06] (= sou-ent, 'souvent') | [11] (= la) [52]…"
Full local read: "…prennent souvent la [52]…" — grammatical with zero
ungranted assumptions beyond 14="sou" (window-local). Left-edge subject
agreement ("la [88]" vs plural "prennent") is 88's open class, fenced —
not this target's bar.

Global-consistency audit of 14="sou" (required before any value claim):
- KILLED globally: @72 "ce souvent [24-verb]" ungrammatical; @424 "ce
  souvent [62]" ungrammatical; @1365/@1689 "tout souvent [60]"
  ungrammatical; @813 "[65] sou er" ("souer" non-word). Four independent
  windows force 14="sou" false as a global value at kill grade.
- Compatible (non-decisive): @117 "et souvent [21]" grammatical; @84
  "[16] souvent [88]" unfalsifiable (16 open, 88 verb-class); @141/@458
  neutral (66 open).
- Net: "sou" is viable ONLY window-locally (@1121, and unfalsified @84).
  A global 14="sou" promotion is barred by the kills above; a
  window-local homophone ("sou" here vs 'le'-family elsewhere) needs
  red-team declaration (67 et/veut is the sole true polyvalence, §7).

Correction to the bar's presupposition (recorded, not hidden): the bar
says "between two promoted 'ent' verb-endings". Under parse (c), 06@1122
is the ADVERB's ending ("souvent"), not a verb ending. The tout-slot-14
battery established both 06s as 'ent' (value) but never established both
as verb-endings. The "two verb-endings" framing was itself part of the
segmentation artifact.

## Per-clause pass/fail

- C1 (clause boundary, punctuation-independent evidence): FAIL. No row
  boundary (mid-row a6_07 both sides), no distributional clause-initial
  profile for 14 at this window, and the smooth intra-clausal "prennent
  souvent la" parse removes any need for a boundary. Absence of evidence
  is not kill-grade against boundaries in general — it is fail-grade for
  C1's demonstration bar.
- C2 (14 takes a grammatical value in the surface): PASS, STRICTLY
  WINDOW-SCOPED. 14="sou" ("souvent") makes @1116–1127 fully grammatical
  with no ungranted assumption beyond the stated V. The pass does NOT
  extend to a global value: 14="sou" is killed globally (@72, @424,
  @1365/1689, @813 — see above). The bar's literal "two verb-endings"
  presupposition is corrected per the finding above.
- C3 (else: confirm genuine word-boundary residual): CONFIRMED. The
  anomaly is an artifact of the "14 = standalone word between two
  ent-endings" segmentation. True segmentation: 14 is word-internal,
  the initial syllable of "[14]ent" ("souvent"-shaped adverb). There is no
  structural anomaly left at @1121 — only the open question of 14's
  global value.

Adverses adjudicated: "word-level values all fail between two 'ent'
endings" — ANSWERED BY RE-FRAMING with stated cause (tout-slot-14's
result stands and is cited, not re-run): the adverse presupposed 14 is
word-level; the finding is that 14 is sub-word-level (syllabic) in this
window. No word-level value was found because none is there to find.

## Verdict

**null.** C1 fails; C2 passes only window-locally with 14="sou" killed as
a global value, so no promotable value or boundary is demonstrated at
battery grade; nothing is forced false at kill grade. The else-branch is
confirmed: B4 @1121 is a genuine word-boundary (segmentation) residual,
resolved locally as "…prennent souvent la…" with 14 word-internal in
"[14]ent" ("souvent"-shaped). No standing verdict contradicted or
downgraded; no red-team verdict touched; R5005 and sealed gates untouched.
The "souvent" parse is a strong lead, not a promotion — global 14="sou"
is dead, and any homophone split needs red-team declaration.

## Follow-ups (null regenerates work)

1. `souvent-14-06-retest` (P2): test the second "14 06" window @84 under
   14="sou": bar — "@80–90 parses as '[16] souvent [88]' with 16/88
   class-consistent, or 'souvent' is killed at @84 (which would make
   @1121's parse a coincidence, not a pattern)."
2. `prennent-70-12-06` (P2): test the souvent parse's left edge: bar —
   "'11 88 70 12 06' parses as (plural NP) + 'prennent' with subject
   agreement, or fence with stated cause (88's class open; 'la' may be
   word-internal to a preceding word)."
3. `le-14-kill-1121` (P2): 14='le' (leading global candidate from
   tout-slot-14) against its strongest breaker: bar — "demonstrate a
   grammatical '…ent le ent…' parse at @1121, or kill 14='le' at kill
   grade at this window. If 'le' dies here while 'souvent' holds at @84,
   escalate 14-homophony to the red team."
