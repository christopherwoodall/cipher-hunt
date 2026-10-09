# Battery report: w4-21-leftedge — "21's value completes W4's left edge"

- Target id: `w4-21-leftedge`
- Date: 2026-10-09
- Lock: `code/crowd17/next-token/locks/w4-21-leftedge.lock` (created at start, deleted at completion; no prior lock existed).
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; n=1847 asserted, 96 types asserted).
  `canonical.py` never used. R5005 untouched. All @-offsets are 0-based repaired-stream pair indices.

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"(a) 21 named with >=2 frame-legs, or recorded as gate; (b) '...[21-phrase] et vers ce...' parallelism stated or the gate named"

## Numbered clauses (frozen before testing, not modified after)

1. (C1) 21's VALUE is named with >=2 frame-legs, OR 21's value is recorded as an
   open gate with the owning question named.
2. (C2) The '...[21-phrase] et vers ce...' parallelism at W4's left edge is
   stated with byte evidence, OR the gate is named.
3. (C3) The listed adverse (83's value open, 'de' lead held) is answered, not ignored.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs / 96 types asserted).
2. Located W4's left edge byte-exactly: the 5-gram `44 83 21 67 78` at @1160
   (row a6_09): `... 17 77 82 44 83 21 67 78 45 13 55 ...` — i.e. "... 44 83 21 et
   ver ce [13-55-61] ..." (the brief's "vers ce" is the 78-45 dict window).
   The 5-gram occurs exactly **2x stream-wide**: @1160 (a6_09, `78 45` after)
   and @1839 (a8_11: `82 16 59 36 69 64 22 42 44 83 21 67 78 49 74 93`,
   `78 49` after).
3. Re-read the lane's 21 record: noun class battery-promoted (de-frame-21-class,
   8 det/prep legs); value "suite" KILLED at bar grade by suite-21-qui-que
   (@134 "qui suite 65" and @1529 "que suite 65" ungrammatical); rival-21-feminine
   returned NULL ("suite" uniquely won the idiom controls; no rival named);
   val-21-reopen (re-run the value search) still queued. Det/prep-preceded 21
   windows re-verified: @109 @231 @359 @1064 @1162 @1172 @1787 @1841.
4. Ran a heuristic candidate sweep against the five anchored idiom frames from
   name-21-obj ("on donne X" @171, "par X" x3 @231/@1064/@1787, "la X" x2
   @109/@359, "de X" x2 @1162/@1841 under the 83='de' lead, "X veut [inf]" x2
   @1423/@1457). New feminine candidates ("parole", "forme", "fin", "mesure",
   "preuve", "valeur", "voix") each fail at least one anchored control at the
   idiom level ("par parole", "par forme", "donner fin", "donner mesure"
   unidiomatic; "donner forme" requires an unevidenced "à"). Nothing lives
   beyond the killed "suite"; no >=2-frame naming is possible at battery grade.
5. Applied the §7 positional rule at the two formula windows: 67's follower 78
   is not infinitive-shaped in either window, so 67="et" (coordination), not "veut".

## Window-level evidence

- W4 left edge @1160 (a6_09): `1157:77 1158:82(m) 1159:44 1160:83 1161:21
  1162:67(et) 1163:78 1164:45(ce) 1165:13 1166:55 1167:61 ...` — the left span
  "le m ... 44 de [21] et" requires 21's value (and 83's) to license a complete
  clause or NP; without them the edge is a forced residual.
- Second formula window @1839 (a8_11): `... 42 44 83 21 67 78 49 74 93` —
  same `44 83 21 67 78` shape; 78's right neighbor differs (49 vs 45). The
  parallelism is byte-level, not an idiom reading.
- '21 67' x8 stream-wide; in the two formula windows 67="et" coordinates 21's
  phrase with the 78-headed right span. Whether 'et' coordinates an antecedent
  NP is owned by queued w4-left-edge-21-83 (not duplicated here).

## Per-clause pass/fail

1. **C1 — GATE RECORDED.** 21's value is not nameable at battery grade:
   "suite" kill-grade dead; rival shootout null; heuristic sweep of new
   feminine candidates fails the anchored idiom controls. The naming question
   is owned by queued `val-21-reopen`; no duplicate value search was run here.
2. **C2 — PARALLELISM STATED.** The `44 83 21 67 78` 5-gram occurs exactly 2x
   (@1160, @1839); 67="et" in both by the §7 rule; right neighbors diverge
   (78-45 dict window at W4 vs 78-49 at W4'). The 'et'-coordination parse and
   the antecedent-NP question sit with queued `w4-left-edge-21-83`.
3. **C3 — ADVERSE ANSWERED.** 83's value open: W4's left edge leans on the
   83='de' lead for the "de [21]" leg (name-21-obj leg D). Under the syllabic
   '-de' fork that leg dissolves, weakening any noun value leaning on it. The
   fence is stated, not hidden: 21's naming at W4 is jointly gated on 83.

## Verdict: NULL

The claim ("21's value completes W4's left edge") is not establishable: 21's
value is an open gate. Both bar clauses resolve via their gate paths — the
gate is named (val-21-reopen owns the naming; w4-left-edge-21-83 owns the
'et'-coordination parse) and the parallelism is stated. No standing or red-team
verdict is contradicted or downgraded; §7 intact. Canonicality caveat stands
(all @-offsets on the canonical stream; the fences hold per protocol).

## Follow-ups (null regenerates work; already-queued targets NOT duplicated)

1. **w4-leftedge-rerun-21** (priority 3): re-test W4's left edge @1158-1168 and
   the @1837-1845 formula window once `val-21-reopen` names 21's value or 83's
   value promotes. Bar: produce the full left-edge parse with the named value,
   or re-fence with the then-current failure stated. Coordinate with
   w4-left-edge-21-83 (owns the 'et' parse) — do not duplicate its bar.

Note: `val-21-reopen` (names 21's value) and `w4-left-edge-21-83` (tests 'et'
coordination) are already queued and cover this null's two gate arms; no other
new targets proposed.

## Bookkeeping

- Lock created at start, deleted on completion (verified gone).
- `battery-queue.json`: own entry only, temp-file + rename; pre-write assert
  confirmed status `queued`/verdictless (no downgrade); JSON re-validated after write.
- R5005, sealed gates, red-team adjudication queue untouched. `canonical.py` never used.
