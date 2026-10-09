# Battery npframe-60-1366 — mirror class adjudication at @1366

Worker: battery (agent 35bb6382-161c-4bdd-ac80-3ad4a8640360). Date: 2026-10-09.
Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed like
`code/side-keyhunt/repair_parse.py`; n=1847 and 96 types asserted in-session).
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
Lock `code/crowd17/next-token/locks/npframe-60-1366.lock` created on start
(agent id + UTC), deleted on completion.

## Bar (verbatim from queue, pre-registered BEFORE testing)

"mirror class adjudication at the '14 60 03' trigram — does any verbal 60 parse with <=1 unstated assumption; completes the X-60-03 NP-frame set"

## Numbered clauses (fixed before examining @1366 in detail, mirroring npframe-60-1674)

1. (C1) Enumerate verbal-60 candidates — finite verb, infinitive, past
   participle, present participle — against "14 60 03" using only
   banked/granted/promoted/provisional values (11="la" banked, 82="m"
   banked, 94="ne" STRONG LEAD R17-001, 79="tout" granted A5, 30="pas"
   battery-promoted, 64="qui" granted, 77="le" provisional).
2. (C2) A candidate counts iff the resulting French is grammatical in
   1841 diplomatic French with the 60 verbal hypothesis as the single
   unstated assumption. Any further value, boundary, or
   re-segmentation not in the standing set is a second unstated
   assumption and is over budget. The 60 hypothesis itself is the 1.
3. (C3) If any candidate parses within budget, record which verbal class
   @1366 admits. If none parses, @1366 is a non-verbal-60 frame within
   budget; the 454/690/1643/1673 map gains its fourth entry. No
   polyvalence is declared here (§7: 67 et/veut remains the sole true
   polyvalence).
4. (C4) Adverses answered: 14's class open (the budget block); coordinate
   with (do not duplicate) en14-three-window.

## Window (re-derived, 0-based @-offsets)

@1359–1369: `35 13 92 62 94 79 14 60 03 30 82` (row a7_06).
Target trigram @1365–1367: `14 60 03`.
Reads: "...[35] [13] [92] [62] ne[94] tout[79] [14] [60] [03]
pas[30] m[82]..."

Structural note: 94 and 30 form a ne...pas negation frame —
"ne tout [14] [60] [03] pas" — the finite verb of the clause must sit
between "tout [14]" and "pas" or license the adjacency some other way.

## Census context (re-derived)

- 'X 60 03' trigrams in the stream: exactly 4 — @689 ('29 60 03',
  a5_00), @1365 ('14 60 03', a7_06), @1643 ('98 60 03', a8_04),
  @1673 ('92 60 03', a8_05). This battery completes the map's fourth
  and final trigram.
- 60 occurs 18 times total (matches ledit-60-corrob's re-derived
  census).
- Map so far (npframe-60-454, npframe-60-690, npframe-60-1674):
  @454: yes (participial "ledit [65]"); @690: no (form-independent);
  @1643: hostile-strained; @1673: no (conditional on 92's open class).

## Phase check (in-session, not pre-registered but stated)

Under a7_06's rival offset-1, the row re-pairs to 28 pairs with the
trigram at 1365 byte-identical ('14 60 03', 1847 pairs / 96 types
preserved). The window is phase-robust — no canonical-offset escape
for the null.

## Per-candidate results

**(a) 60 = finite verb.** Two conceivable subjects.
(a1) "tout [14] [60-V] [03] pas" ("tout [14]" as subject): needs 14
nominal — 1 unstated assumption on top of the hypothesis = 2 total.
Over budget.
(a2) [62] as subject ("[62] ne tout [14] [60-V] [03] pas"): fails at
word-order grade before the budget — "tout" is not a clitic and cannot
stand between "ne" and the finite verb. FAIL independent of budget.
FAIL within budget.

**(b) 60 = infinitive.** An infinitive needs a governor. Preceding span
is "ne tout [14]"; "tout" governs no infinitive, no preposition is
present. Reading 14 as a governing preposition ("à"-like) is 1
unstated assumption + hypothesis = 2. Over budget. FAIL within budget.

**(c) 60 = past participle.** The npframe-60-454 (c) parse required an
article immediately before 60 ("le dit [65]"). Here the pre-60 token is
14. 14-as-article ('le') is 1 unstated assumption + hypothesis = 2 —
and 14='le' globally is kill-grade dead (le-14-kill-1121; only
locus-level determiner legs @117/@1365?/@1689). Post-nominal epithet
("tout [14-NP] [60-pp]") needs 14 nominal (same budget failure). 14-as-
auxiliary is not a French construction. FAIL within budget.

**(d) 60 = present participle.** Post-nominal epithet or detached clause
both need a nominal host for "tout [14]" — 14 nominal = 1 unstated
assumption + hypothesis = 2. Over budget. FAIL within budget.

## Budget audit

Every conceivable verbal parse at @1366 spends the 60 hypothesis (1)
plus ≥1 further unstated assumption — uniformly, the open class of 14.
No parse contradicts a standing value; the block is entirely 14's open
class (verb-stem fenced lane-wide per stem-14-84-retest; global 'le'
killed per le-14-kill-1121; determiner/clitic loci only).

The nominal-60 rival ("tout le [60-N] [03]", mirroring the 454 shape
with 14 as the article) is the grammatically cleaner reading but is
NOT adopted or scored here — the bar only asks the verbal-60 question,
and 14's locus-level determiner leg does not name it globally.

## Verdict: NULL

No verbal 60 class parses "14 60 03" at @1366 within the
≤1-unstated-assumption budget. The bar carries no promote clause and
no kill clause (it is a mapping question, same shape as
npframe-60-690/1674), and no standing verdict is contradicted — so
NULL, not KILL.

**Mapping result (the deliverable):** the NP-frame map now reads —
@454: yes (participial "ledit [65]", 1 assumption); @690: no
(form-independent); @1643: hostile-strained; @1673: no (conditional on
92's open class); @1366: **no (conditional entirely on 14's open class;
one stated nominal-14 assumption would admit parses, but that is 2
total with the hypothesis — over budget)**. Feeds the P1
poly-60-redteam docket; no polyvalence declared (§7).

## Adverses

1. "14's class open" — ANSWERED: the open class is the uniform budget
   block at all four candidates; stated, not ignored.
2. "Coordinate with queued en14-three-window, do not duplicate" —
   ANSWERED: en14-three-window is PRESENT in the queue and owns the
   14='en' arm; this battery tested no 14 value and budgeted 14's class
   as open. No duplication.

## Follow-ups proposed (for supervisor queuing)

1. `npframe-60-1366-rerun` (P4) — re-run this mirror adjudication iff a
   14-class verdict (nominal, determiner, or clitic, battery or
   red-team) ever lands; the budget math then re-tests with 14 named.
2. `npframe-60-322` (P3) — already PRESENT in queue (proposed by
   npframe-60-1674); not duplicated here.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-npframe-60-1366.md`.
- Queue: own entry only, temp-file + rename; pre-write assert confirmed
  no prior verdict; JSON re-validated after write.
- Lock created on start, deleted on completion.
- No standing verdict contradicted or downgraded. No red-team
  escalation needed (no contradiction found). §7 intact.
