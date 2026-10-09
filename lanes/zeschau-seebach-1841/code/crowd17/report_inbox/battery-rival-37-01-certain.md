# Battery report: rival-37-01-certain

- Target id: `rival-37-01-certain`
- Claim: "37-01 x3 is the local word 'certain' (37='cer', 01='tain'), NOT evidence for a global 01 value"
- Date: 2026-10-09
- Worker: battery worker (subagent c6aa2289-e3e7-42c7-924a-97df94a940e6)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  Re-derived in-session: 1,847 pairs, 96 types. All @-offsets below are 0-based
  repaired-stream indices of the 01 token (37 sits one index earlier).
  Never used canonical.py. R5005 not touched. No data invented.
- Lock: code/crowd17/next-token/locks/rival-37-01-certain.lock (created at
  start, deleted on completion; no prior lock for this id existed).

## Bar (verbatim, pre-registered before testing)

"resolve iff (a) all three windows parse with 'certain' grammatically
integrated (qui-certain-07 @940, qui-certain-74 @1634, er-certain-02 @1818 -
state how qui+adjective and er+certain integrate); (b) the verdict states the
consequence: either tain stays local (01 keeps ci/faisant globally) or
'certain' is killed and 37-01 returns to the ci-01-value bar"

Numbered pass/fail clauses (restated before testing, not modified after):

1. W1 @940: "qui [37-01=certain] [07]" parses as grammatical 1841 French.
2. W2 @1634: "qui [37-01=certain] [74]" parses as grammatical 1841 French.
3. W3 @1818: "er [37-01=certain] [02]" parses as grammatical 1841 French
   (state how er+certain integrate).
4. The verdict states the consequence: either "tain" stays local (01 keeps
   ci/faisant globally) or "certain" is killed and 37-01 returns to the
   ci-01-value bar.

## Method

1. Read BATTERY-PROTOCOL.md first.
2. Re-derived the repaired parse in-session (1,847 pairs / 96 types).
3. Byte-exact bigram search for 37-01: exactly 3 windows, 37 at 0-based
   @939, @1633, @1817 (01 at @940, @1634, @1818). Confirmed the three bar
   windows byte-identical.
4. Tested "certain" (37='cer', 01='tain') at each window against granted
   constraints: 64="qui" (protocol section 7, granted ground truth);
   29="er" (pencil ground truth).
5. Adopted as premises (not re-litigated): wordinternal-37-01 (PROMOTE,
   2026-10-09, status verdict in battery-queue.json) — its W1/W2 evidence
   explicitly tested and killed the "-tain" ending family including
   "qui certain"; ci-01-value (KILL, standing) for the global 01 values.

## Window-level evidence

### W1 @940 (row a5_10, mid-row)
Byte-confirmed: `@931..@948 = 83 56 69 26 00 33 21 64 [37] [01] 07 50 40 08 62 98 96 86`.
Target trigram+head: `64 37 01 07` = "qui [certain] [07]".
- "certain" is an adjective. A relative "qui" (granted) must be followed by
  a finite verb phrase. A one-word non-verb after "qui" is ungrammatical at
  kill grade in 1841 French.
- Rescue route A: nominal-37 ("qui [certain-noun]" — bare "certain" as noun).
  Bare "certain" without determiner is ungrammatical. Ungranted (adverses).
- Rescue route B: est-ellipsis ("qui [est] certain"). Est-ellipsis under
  "qui" is ungranted (adverses).
- Rescue route C: "certain" as determiner ("certains", some). The singular
  bare form is not a French determiner; "qui certain" does not parse this
  way. No integration.
- CLAUSE 1: FAIL at kill grade.

### W2 @1634 (row a8_03, mid-row)
Byte-confirmed: `@1625..@1642 = 46 56 69 26 00 33 21 64 [37] [01] 74 87 74 74 35 56 12 33`.
Target: `64 37 01 74` = "qui [certain] [74]".
- Same byte-identical left 8-gram "56 69 26 00 33 21 64 37" as W1.
- Identical kill: "qui certain [74]" — "qui" demands a finite verb; the
  adjective cannot stand as the relative-clause predicate; routes A, B, C
  fail identically (routes A/B ungranted per adverses).
- CLAUSE 2: FAIL at kill grade.

### W3 @1818 (row a8_10, mid-row)
Byte-confirmed: `@1809..@1826 = 04 61 15 93 50 42 06 29 [37] [01] 02 09 19 00 97 00 86 29`.
Target: `29 37 01 02` = "er [certain] [02]", left edge "42 06".
- "er" is the granted letter (29='er'). The only live composition is
  "06-29" as an infinitive tail ("[06]er"); the infinitive-as-subject route
  then needs a finite verb after the infinitive ("Vouloir, c'est
  pouvoir"). "certain" is an adjective, not a verb — the route dies.
- Determiner route: bare "certain" before 02 cannot license "certain [02]"
  as a noun phrase in 1841 French; "certain" is adjective-shaped, not
  determiner-shaped in the singular bare form.
- No stated integration of "er+certain" is grammatical: "er certain" is
  not a French word; "[certain]" cannot be the predicate of an infinitive
  subject.
- CLAUSE 3: FAIL at kill grade.

## Per-clause pass/fail

1. W1 @940: FAIL at kill grade ("qui certain" ungrammatical; both rescue
   routes ungranted).
2. W2 @1634: FAIL at kill grade (identical).
3. W3 @1818: FAIL at kill grade (no grammatical integration of "er+certain").
4. Consequence stated below.

## Adverses, answered

1. "qui certain needs nominal-37 or est-ellipsis (ungranted)": ANSWERED.
   Both routes named and confirmed ungranted; no third route exists under
   standing values. The "qui" + finite-verb constraint is granted (64).
2. "tain has no support outside 37-01": ANSWERED. Moot — it now has no
   support at 37-01 either. Kill-grade dead at all three windows.
3. "87-01/47-01/45-01 cannot be ce-tain - a global 01='tain' is already
   dead, only the local reading is live": ANSWERED. The local reading is
   dead too. This battery's kill agrees with wordinternal-37-01's PROMOTE,
   whose "-tain" ending family ("qui certain / lointain / fontaine /
   capitaine") was killed at W1/W2 at kill grade. No standing verdict is
   contradicted or downgraded; ci-01-value's kill (global) stands.

## Consequence (clause 4)

"certain" is KILLED. 37-01 returns to the ci-01-value bar. The "-tain"
syllable does NOT stay local — it is kill-grade dead at these windows.
The live word-internal account remains wordinternal-37-01's 01="fait"
(local syllable, distinct from the killed global 01="faisant"/"ci" —
"fait" != "faisant"; the killed general values are not resurrected).
01 keeps ci/faisant globally killed.

## Verdict: KILL

The local word "certain" (37='cer', 01='tain') fails at kill grade at all
three windows. Every bar clause that requires grammatical integration
fails; the stated consequence (clause 4) is the kill branch.
