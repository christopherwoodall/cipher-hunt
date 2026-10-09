# Battery report: cela-69-11-word

**Target:** `cela-69-11-word` (P2)
**Date:** 2026-10-09
**Verdict:** PROMOTE (locus-level; global 69 value stays open)

## Bar (verbatim from queue)

"'69 11' @1115-1116 parses as one word ('cela'-shaped, 69='ce'-class) with the clause boundary before 88, or the word-internal-la hypothesis is killed at this window (69: n=12, followers 26 x3 / 13 x2 / 24 x2 / 88 x2 / 14 / 11 / 74 / 64)"

## Bar restated as numbered clauses

1. '69 11' @1115-1116 parses as ONE word, 'cela'-shaped, with 69 taking a 'ce'-class value.
2. The clause boundary falls before 88 (i.e. "cela" is word-complete; 88 opens the next constituent).
3. (Alternative kill arm) The word-internal-'la' hypothesis is killed at this window.

## Method

Re-derived the full stream on the repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`;
upstream tokenization `[s[i:i+2] for i in range(o, len(s)-1, 2)]`).
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
Lock created on start, deleted on completion.

Locus context (row a6_07), pair index : group:

- 1113: 38 | 1114: 30 (=pas, promoted) | **1115: 69 | 1116: 11 (=la, ground truth)**
  | 1117: 88 | 1118: 70 (=pre) | 1119: 12 | 1120: 06 | 1121: 14 | 1122: 06
  | 1123: 11 (=la) | 1124: 52 | 1125: 37 | 1126: 43 | 1127: 00 (=pour)

## Window-level evidence

**E1 — The "cela" dissolution model is already granted.** Lane record:
87-11 = "cela" is the only granted *-11 compound (n=7; e.g. @73/@829
"fait(24) cela" direct object); 47-11 = "cela" granted (e.g. @500
"47 11 29 40" = "cela erre", subject). Rationale in both: "ce"+"la" as two
words is ungrammatical in French, so the groups fuse. The same
ungrammaticality applies to 69-11 IF 69 is 'ce'-class: "ce la" two-word is
impossible, "cela" one-word is the only grammatical reading.

**E2 — 69's distribution is 'ce'-compatible, contradiction-free (n=12).**
Followers re-derived: 26 x3, 13 x2, 88 x2, 24 x1, 14 x1, 11 x1, 74 x1,
64 x1. (Queue bar says "24 x2"; actual count is 24 x1 — stale count noted.)
"ce"-reads: 69->64 = "ce qui" (64=qui ground truth) — grammatical and
common; 69->26 x3 = "ce [noun]" (26=noun lead) x3 — grammatical for the
determiner face; 69->24 x1 = "ce [verb]" — grammatical for the pronoun face
("ce semble"-type). No follower forces a non-'ce' value.

**E3 — Left edge "38 30 [cela]".** Cleanest reading: 38="non" ->
"non pas cela" (corrective fragment, standard 1841 prose). 38's value is
OPEN (n=7; followers 82 x2 / 37 / 30 / 47 / 26 / 83 — "non"-compatible but
thin, not promoted here). The "cela"-word reading does not depend on 38's
value: any left parse still needs "69 11" to be either "cela" or
"ce"+"la"(ungrammatical).

**E4 — Right edge / clause boundary before 88.** "88 70-12-06 14-06 11" =
"88 prennent souvent la" frame is class-level coherent per the @1121
battery (70-12-06="prennent"-shaped, 14-06 adverb slot, 11="la" article;
14='sou' value dead globally, frame survives at class level). No rival
fusion exists: "cela"+88 cannot form a French word, and "cela [88]" as
"cela que [verb]" would need a subject that isn't there. 88's clause-head
value stays open (dedicated `prennent-88-subject` target still queued —
coordinated, not duplicated).

**E5 — Correction to the evidence premise.** The brief's "only locus where
'la' could be word-internal" is stale: 87-11 (n=7) and 47-11 (n=3) are
already granted "cela" compounds. @1115-1116 is the only *69*-11 locus, not
the only word-internal-'la' locus. This strengthens, not weakens, the
parse: the dissolution model is precedented.

## Per-clause pass/fail

1. **PASS.** '69 11' @1115-1116 = "cela", one word; 69 takes 'ce'-class
   value at this window. Granted dissolution model (E1), 'ce'-compatible
   distribution with zero contradictions (E2), "ce la" two-word
   ungrammatical.
2. **PASS (at battery grade).** Clause boundary before 88: "cela" is
   word-complete; no grammatical rightward fusion exists (E4); right side
   opens the independently coherent "88 prennent souvent la..." frame.
   88's exact head value is fenced as open, not assumed.
3. **N/A (kill arm does not fire).** The window supports, rather than
   forces false, the word-internal-'la' reading.

Adverses: none listed. Standing verdicts: no conflict — the granted
87-11/47-11 "cela" compounds already establish that syllabic 11 does not
contradict banked 11="la"; §7 polyvalence rule not implicated; no kill
touched.

## Verdict: PROMOTE (locus-level)

'69 11' @1115-1116 reads **"cela"** (one word). 11 is syllabic/word-internal
here. Clause boundary before 88.

**Explicitly fenced (NOT promoted):**
- 69 = "ce" GLOBALLY. A third "ce"-group beside banked 47="ce" and
  promoted 87="ce" is homophony and needs a global test + red-team
  authority. 69's other 11 windows are 'ce'-compatible, not 'ce'-forcing.
- 38 = "non" (working left-parse assumption only).
- 88's clause-head/subject value (see `prennent-88-subject`, queued).

## Recommended follow-up (global question stays open)

- `ce69-global` (P2): test 69="ce" across all 12 windows — "ce 26[noun]"
  x3 and "ce 64[qui]" as positive legs; weigh the homophony cost against
  banked 47="ce" / promoted 87="ce" (frequency-uniformity note); kill iff
  any window forces a non-'ce' value.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/cela-69-11-word.lock` created
  2026-10-09T02:47:11Z, deleted on completion.
- `battery-queue.json`: `cela-69-11-word` queued -> verdict/promote
  (temp-file + rename; pre-write assert confirmed no prior verdict).
- R5005, sealed gate instances, red-team adjudication queue untouched.
