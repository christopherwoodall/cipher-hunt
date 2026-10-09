# Battery verdict: est-ce-104

Worker: d8a5cdf4-770c-4aed-926e-07b409367149. Date: 2026-10-09.
Lock: code/crowd17/next-token/locks/est-ce-104.lock (created 2026-10-09T03:26:34Z; no prior lock).
Target id: est-ce-104. Queue status at take: queued, priority 3, no verdict.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005, sealed gates, red-team adjudication queue untouched.
No data invented. @-offsets are 0-based stream indices.

## Bar (pre-registered verbatim from battery-queue.json, BEFORE testing)

"28 named with 'est-ce [28] pour que' parsing (input bar for est-59-frames)"

Numbered clauses:
1. 28 is named (a value, not a class).
2. @104 parses as 'est-ce [28] pour que' under that value in 1841 French.

## Method

1. Re-derived the full 28 census on the repaired stream: n=6 at
   @105/@286/@698/@747/@1573/@1751 (0-based group indices of 28 itself).
2. Re-derived 45's follower distribution (n=22) and both 45-28 contacts.
3. Grepped the report inbox for any prior naming of 28: none found
   (the three "28=" grep hits are offset artifacts, not value claims).
4. Tested the candidate value set {donc, bien, aussi, encore, là, tout}
   against all six windows for 1841-French grammaticality.

## Window-level evidence

**@104 (a1_03): the claim window.**
`[100]62 [101]94 [102]93 [103]59 [104]45 [105]28 [106]00 [107]46 [108]11 [109]21`
= "62 ne [93] est-ce [28] pour que la [21]..."
(59='est' provisional, 45='ce' HOLD per A11, 00='pour' promoted,
46='que' GT, 11='la' GT). The 'est-ce [28] pour que' reading is the
claim; it requires 28 to be a word that can sit between "est-ce" and
"pour que".

**45's follower distribution (n=22, re-derived):**
93 x3, 64 x3, 23 x3, 28 x2, 13 x2, 91 x1, 54 x1, 88 x1, 46 x1, 94 x1.
The single 45-46 ("ce que") contact is @437 ("78 63 45 46 43", a2_09) —
NOT at an "est-ce" site. So the adverse's premise ("'est-ce' normally
takes 46") is distributionally false in this corpus: 45 takes ten
distinct followers and 46 is among the rarest. The grammatical question
remains, but the distributional objection does not.

**The other five 28 windows:**
- @286 (a2_03): "52 89 28 00 97 09" = "[89] [28] pour [97]..."
- @698 (a5_01): "50 45 28 94 60 12" = "[45] [28] ne [60]..." (94='ne' STRONG LEAD)
- @747 (a5_02): "81 85 28 00 64 02" = "[85] [28] pour qui [02]..."
  (85 verb-stem A3, 64='qui' GT)
- @1573 (a8_01): "56 32 28 52 82" = "[32] [28] [52]..." (32 verb-class)
- @1751 (a8_08): "34 07 28 89 26" = "[07] [28] [89]..."

**Candidate value matrix (1841 French):**

| value | @104 "est-ce X pour que" | @698 "ce X ne" | @286/@747 "X pour (qui)" |
|---|---|---|---|
| donc | PASS ("est-ce donc pour que") | FAIL ("ce donc" ungrammatical) | PASS |
| bien | PASS ("est-ce bien pour que") | MARGINAL ("ce bien ne" = "this good does not") | WEAK |
| aussi | PASS | FAIL ("ce aussi" ungrammatical) | PASS |
| encore | PASS | FAIL | PASS |
| là | PASS ("est-ce là pour que") | MARGINAL ("ce-là" archaic) | WEAK |
| tout | FAIL | FAIL | FAIL |

No candidate parses all six windows. 'donc' is the best fit (4/6 clean,
2 marginal-free) but is killed at @698 by the "ce donc" contact —
unless 45 is not 'ce' at @697 (see follow-up 2).

## Per-clause pass/fail

1. **28 named: FAIL (epistemic).** No value covers the six-window
   distribution; the failure is lack of evidence, not falsification.
2. **@104 parses as 'est-ce [28] pour que': UNTESTED-pending-1.**
   The frame is grammatical for several candidates (donc/bien/aussi/
   encore/là), but without a named value the clause cannot pass.

## Adverses answered

- "28 unknown": CONFIRMED — no battery has named 28; it stays unknown.
  This is the verdict driver, not a dodge.
- "'est-ce' normally takes 46 not 28": ANSWERED — re-derived 45's
  follower distribution shows 46 is one of 45's rarest followers (x1,
  @437, not an "est-ce" site); 45-28 x2 (@104, @697). The distributional
  premise is false in this corpus. The grammatical premise (a named
  value must fit "est-ce X pour que") stands and is unmet.

## Verdict: NULL

28 cannot be named at battery grade: n=6, no cross-window naming leg,
best candidate ('donc') killed at @698. The @104 'est-ce [28] pour que'
frame stays open as an input to est-59-frames but contributes no value.
No standing verdict contradicted or downgraded.

## Follow-ups proposed (for supervisor queuing)

1. `donc-28-triangulate` (P2): test 28='donc' on the four non-"ce"
   windows (@286/@747/@1573/@1751) with @698's "ce donc" failure held
   as a separate contact question; kill 'donc' iff @698's 45 is 'ce'.
2. `ce28-contact` (P2): adjudicate the "45 28" bigram x2 (@104/@697) —
   is 45='ce' at @697 ("02 50 45 28 94")? If 45 is not 'ce' there, the
   @698 constraint on 28 loosens and 'donc' revives.
3. `x-pour-que-paradigm` (P3): census "X 00 46" trigrams stream-wide to
   build the corpus-internal paradigm of values preceding "pour que";
   discriminates donc/bien/aussi/encore/là by distribution.

## Bookkeeping

Report: code/crowd17/report_inbox/battery-est-ce-104.md. Queue updated
via temp-file + rename (est-ce-104: queued -> verdict/null; pre-write
assert confirmed no prior verdict; JSON re-validated). Lock deleted.
