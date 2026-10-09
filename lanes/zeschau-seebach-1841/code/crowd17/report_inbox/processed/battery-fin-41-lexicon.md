# Battery report: fin-41-lexicon

**Target:** `fin-41-lexicon` — "Finite-verb value candidates for 41 can be tested against the 'qui [41]' relative frame's subject/agreement shape to name 41's verb value."
**Worker:** da1a3816-6f03-4b4c-abd9-03f4c15ff811
**Date:** 2026-10-09. Verdict: **NULL**.

## Bar (verbatim from battery-queue.json)

"Test finite-verb value candidates for 41 against the 'qui [41]' relative frame's subject/agreement shape."

Numbered clauses (fixed before the discrimination run, not modified after):
- **C1:** At least one finite-verb value candidate for 41 exists on the lane record to test.
- **C2:** The 'qui [41]' frame's subject (qui's antecedent) is recoverable with a landed value, fixing the agreement shape (number/person).
- **C3:** The subject/agreement shape discriminates among the candidates — at least one candidate fails, naming 41's verb value.

## Method

Read BATTERY-PROTOCOL.md first; lock `locks/fin-41-lexicon.lock` created on
start, deleted on completion. Stream re-derived in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py`: 1,847 pairs / 96 types
verified. `canonical.py` never used. R5005, sealed gate instances, and the
red-team adjudication queue untouched. Offsets below are 0-based; the
target's "@40" is the 41 token at 0-based @39 (1-based @40).

## Window-level evidence

- **The `64 41` bigram occurs exactly once in the 1,847-pair stream:** 0-based
  @38–39 (row a1_01). The relative frame is a singleton.
- Full window @32–44: `64@32 32@33 01@34 | 08@35 91@36 39@37 64@38 41@39 01@40 24@41 88@42 43@43 81@44`.
- **Subject antecedent `08 91 39` @35–37 is a stream-hapax:** trigram
  `08 91 39` 1/1846 trigrams; bigram `91 39` 1/1846 bigrams. None of
  08/91/39 carries any banked, promoted, granted, provisional, or live
  value (§7 + full queue search). 39 n=13; its other 12 windows
  (@503, @600, @607, @692, @764, @1068, @1333, @1491, @1512, @1605, @1676)
  carry no value either.
- **64 ('qui') n=47 with 28 distinct followers; 41-follower occurs once.**
  No cross-window agreement calibration exists for this frame.
- **Finite-verb candidate census:** no finite-verb value candidate for 41
  exists on the lane record. 41="une" belongs to the determiner arm of the
  §7 split (verb @40 vs determiner @238, per class-41-contact); 41="se"/"ne"
  are non-finite; 'donne' at @58 was explicitly ruled "not a leg" (donn-41-44,
  prof-53 forced contradiction). Generating candidates from a French
  lexicon would be invention, not testing.
- Standing premises adopted: 64='qui' banked; 41 verb-forced at this window
  (class-41-contact); 01's value open ('en'/'tain'; 'ci' killed, per
  verb-41-value); 24='faire' battery-promoted (imp-80-set, per
  class-41-contact).

## Per-clause results

- **C1 — FAIL.** No finite-verb value candidate for 41 exists on the lane
  record (see census). There is nothing to test.
- **C2 — FAIL.** The subject (antecedent `08 91 39`) is a stream-hapax with
  no landed value; the relative clause's agreement number/person is
  unrecoverable at battery grade. The frame's singleton status means no
  distributional substitute is available.
- **C3 — FAIL.** With no candidates and no agreement constraint, the test
  cannot discriminate; "any finite verb fits." No value is named.

## Adverse answered

The target's adverse is confirmed, not ignored: "the lexicon test needs the
frame's subject/agreement shape to discriminate" — the test finds the shape
is not recoverable, so the need is unmet. The failure is epistemic, not a
refutation: this is a §2 untestable-as-written (missing inputs), not a
kill. No standing verdict is contradicted or downgraded; §7 intact.

## Verdict: NULL

Follow-ups proposed (all verified absent from battery-queue.json; `val-01-census`
and `qui-41-01-boundary` are already queued and were not duplicated):

1. `antec-08-91-39` (P3) — census 39 (n=13), 91 (n=21), 08 (n=18) to name
   the antecedent NP at @35–37; a landed agreement number re-opens this bar.
   Bars: "Name the value/class of the 08 91 39 NP via its 39/91/08 windows;
   report 41's implied agreement number." Evidence: hapax antecedent of the
   sole 'qui [41]' frame @38–39; C2 failed here. Adverses: the NP may be
   genuinely unrecoverable at battery grade; single-window roles don't carry.
2. `qui-subject-recoverability` (P3) — census all 47 qui-windows' antecedents
   for value recoverability; methodology check on the agreement-lexicon
   route as a whole. Bars: "For each of the 47 qui-windows, attempt
   antecedent naming from banked values; report the recoverability rate."
   Evidence: the qui-41 frame's subject proved unrecoverable. Adverses: low
   recoverability would close the route, not open it — still a result.
3. `fin-41-lexicon-r2` (P3) — gated re-run of this bar once 01's value lands
   (val-01-census) or the antecedent lands (antec-08-91-39); narrow bar:
   "test only the landed candidate set against the landed agreement shape."
   Evidence: this null. Adverses: neither gate may ever clear.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-fin-41-lexicon.md` (this file).
- Lock: `code/crowd17/next-token/locks/fin-41-lexicon.lock` created on start,
  deleted on completion.
- Queue entry `fin-41-lexicon` updated via temp-file + rename (status
  verdict, result null); no other entry touched.
