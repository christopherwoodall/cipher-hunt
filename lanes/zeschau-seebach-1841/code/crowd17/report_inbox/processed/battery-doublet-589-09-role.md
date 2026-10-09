# Battery verdict: doublet-589-09-role

**Target:** `doublet-589-09-role` (P3)
**Date:** 2026-10-09
**Worker:** battery worker doublet-589-09-role (subagent c6069a66-bdb9-4c7e-ad5f-1f97172dad16)
**Verdict:** NULL (split-shaped: no single class; single-class hypothesis kill-grade dead)

## Bar (verbatim, pre-registered)

"pass iff >=2 independent legs name one class; fence iff unclassifiable. Determines whether the frame re-parses as 'pour 97 41 41 | 09 pour 92' with 09 heading the second pour's left edge"

Restated as numbered clauses:
- C1: ≥2 independent legs name ONE class for 09 → PASS/FAIL.
- C2 (else-branch): fence iff 09 is unclassifiable → PASS/FAIL.
- C3: determine whether the @591 frame re-parses as 'pour 97 41 41 | 09 pour 92' with 09 heading the second pour's left edge.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/doublet-589-09-role.lock` on start
(agent id + UTC 2026-10-09T17:57:59Z), deleted on completion per protocol.
Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
tokenized like `code/side-keyhunt/repair_parse.py` (asserts: n=1847, 96 types).
`canonical.py` never used. R5005, sealed gate instances, and the red-team
adjudication queue untouched.

Standing values used (§7): GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on (A15 conditional),
47=ce; provisional 59=est, 77=le; battery-grade 98='vient', 94='ne' STRONG LEAD.
Kills honored: 09/92 "-ère" value (A6), 09-verb (lon-09-verb, not re-litigated).
Prior 09 batteries used as leads only: lon-09-verb (NULL, verb fenced),
noun-09-916 (NULL, @916 nominal parse passes locally, value unnameable),
rel-09-290 (NULL, @290 nominal frame), lon-09-reseg (NULL, S1 status quo
stands, S2–S5 unfalsifiable/unadoptable).

Offsets below are 0-based @ on the repaired stream.

## Window inventory (n=12, all re-derived)

| @ (0b) | row | context (09 bracketed) |
|---|---|---|
| 0 | a1_00 | [09] 00 97 51 |
| 173 | a1_05 | 48 21 60 [09] 87 86 21 |
| 289 | a2_03 | 28 00 97 [09] 64 29 40 |
| 518 | a3_00 | 87 77 80 [09] 70 91 77 |
| 591 | a4_00 | 97 41 41 [09] 00 92 79 |
| 680 | a5_00 | 77 45 23 [09] 07 00 92 |
| 915 | a5_09 | 59 37 96 [09] 02 24 |
| 1059 | a6_04 | 23 77 84 [09] 98 83 82 |
| 1223 | a7_01 | 24 48 30 [09] 20 57 64 |
| 1262 | a7_02 | 69 88 01 [09] 11 50 46 |
| 1765 | a8_08 | 06 77 84 [09] 24 87 64 |
| 1820 | a8_10 | 37 01 02 [09] 19 00 97 |

## Class census (standing values only)

**Forced nominal (1 leg):**
- **@915:** `59 37 96 [09] 02 24` = "est [37-pred] par [09] [02]". 96="par" is
  granted; "par" takes a nominal complement (noun/pronoun) — "par" + adverb or
  "par" + verb is ungrammatical. 09 is FORCED nominal here. (Local parse
  verified by noun-09-916; value-naming failed there, class-forcing stands.)
  09 word-internal with "par" needs a value assumption (fenced); "09 02" one
  word has no evidence.

**Nominal frame (1 leg, noun-vs-adjective open):**
- **@289:** `00 97 [09] 64 29` = "pour 97 [09] qui(64) er". 64="qui" granted;
  the relative pronoun needs a nominal antecedent, and the NP "97 09"
  immediately precedes it. 09 is inside a nominal frame. Its own class within
  the NP is ambiguous: head noun (if 97 is determiner/modifier) or postposed
  adjective (if 97 is the head noun) — cf. rel-09-290 follow-up
  `np-97-09-modifier`. Counts as a nominal-frame leg, not a forced-noun leg.

**Forced non-nominal, non-verbal (2 legs, same frame, conditional):**
- **@1059:** `23 77 84 [09] 98 83` = "[23] l'on [09] vient(batt) 83-m".
  09 sits between the subject pronoun "l'on" (77="le" provisional, 84="on"
  A15-conditional) and the finite verb 98='vient' (battery-grade). A bare noun
  between subject and finite verb is ungrammatical ("*l'on table vient";
  appositive rescue needs punctuation — new assumption, fenced). Verb-09 is
  fenced (lon-09-verb). Positive French shapes exist: adverbial pronouns —
  "l'on y vient" / "l'on en vient" are fully grammatical. 09 is FORCED
  adverbial-particle here, conditional on 77="le" + 84="on" standing.
- **@1765:** `06 77 84 [09] 24 87` = "ent l'on [09] [24] ce(87)". Same
  "l'on [09] V" frame (24 class-level finite-modal). Same forcing, same
  conditions. Independent locus, independent leg.
- lon-09-reseg's S1 (09 standalone) stands unkilled; S2–S5 (resegmentations)
  all need new assumptions. The frame analysis is adopted, not re-litigated.

**Class-open (8 windows):** @0 ("[09] pour 97" — interjection/adverb/detached
noun all unforced), @173 ("[60] 09 ce" — 60 open), @518 ("[80-V] 09 pre" —
direct object or adverb, unforced), @591 (doublet frame, see C3), @680
("[23] 09 07 pour" — unforced), @1223 ("[30] 09 20" — unforced), @1262
("[01] 09 la" — unforced), @1820 ("[02] 09 19 pour" — unforced).

## Per-clause findings

- **C1 (≥2 independent legs name one class): FAIL.** No single class covers
  the forcing windows: nominal is forced at @915 (granted "par") while
  non-nominal/non-verbal is forced at @1059 and @1765 ("l'on __ V" — a noun
  there is ungrammatical, verb-09 is fenced). The two adverbial-particle legs
  are real and independent, but promoting "adverbial" as 09's class would
  contradict @915. The single-class hypothesis is kill-grade dead
  (@915 vs @1059 suffice). 09 is split-shaped — the same non-uniformity
  pattern already established for 88 and 52 at battery level.
- **C2 (fence iff unclassifiable): does not fire as written.** 09 is not
  unclassifiable — it is positively split: nominal at @915 (+ nominal frame
  @289), adverbial-particle at @1059/@1765 (conditional on 77="le"
  provisional + 84="on" conditional grant). Per §2, the bar as written does
  not cover the split outcome; recording the split as the finding (counts as
  null, §4).
- **C3 (@591 re-parse): PARTIAL.** Boundaries confirmed on bytes:
  `00 | 97 | 41 | 41 | 09 | 00 | 92` — 09 is a standalone word (not
  word-internal with "41": the 41-census found no letter-tier composition
  forcing; not word-internal with "pour": 00="pour" granted whole-word A9).
  So the frame IS 'pour 97 41 41 | 09 | pour 92' segmentally. But whether 09
  "heads the second pour's left edge" is class-dependent: a nominal 09 could
  head ("[09] pour [92]" as head+complement is strained in French) or sit in
  apposition; an adverbial 09 modifies. With 09's class split, the heading
  question is undecidable at battery level → red-team venue (see follow-up 1).
  09's class at @591 itself stays open.

## Adverses

None stated on the target. Standing-state check: no red-team verdict on 09's
class exists; nothing contradicted or downgraded. 09-verb fence (lon-09-verb),
09/92 "-ère" kill (A6), 09~92 hold (A6), and §7 (67 sole true polyvalence —
no second value declared; the split is positional/class, same treatment as
the 88/52 batteries) all honored. The lon-09-reseg follow-up `pos-09-290-1060`
was verified ABSENT from the queue (proposed but never queued); its substance
is subsumed by follow-up 1 below.

## Verdict: NULL (split-shaped; single-class hypothesis kill-grade dead)

09 cannot be pinned to one class: nominal is forced at @915, adverbial-particle
at @1059/@1765, nominal-frame at @289, verb fenced stream-wide, 8 windows
open. This is a positive split finding, not an absence — 09 joins 88 and 52
as a split-shaped cell awaiting red-team positional adjudication.

## Follow-ups proposed (per §4; all IDs verified ABSENT from battery-queue.json)

1. `split-09-redteam-input` (P2, gather-only) — package this report's split
   evidence (@915 "par"-forced nominal vs @1059/@1765 "l'on __ V"-forced
   adverbial-particle, with the 77="le"/84="on" conditions stated) as red-team
   input for a 09 positional-split docket item, mirroring the 88/52
   treatment. Battery gathers; only the red team declares.
2. `adv-09-1059-1766-value` (P3) — name 09's adverbial value at the two
   "l'on __ V" windows ("y"/"en"-shaped candidates: "l'on y vient",
   "l'on en vient"); bar: value named with ≥2 legs or fenced; conditional on
   77="le" surviving (cf. lon-77-le-gate).
3. `noun-09-915-value` (P3) — name 09's nominal value at "par __" @915 under
   the split framing (noun-09-916's value-naming fence was pre-split; retry
   with the adverbial windows excluded from the candidate's distribution).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-doublet-589-09-role.md`
- Queue: `doublet-589-09-role` → `status: verdict`, `verdict: {result: null,
  report: ..., date: 2026-10-09}` (pre-write assert passed — was
  queued/verdictless; temp-file + rename; disk re-validated; own entry only;
  no downgrade).
- Lock: created on start (agent id + 2026-10-09T17:57:59Z), deleted on
  completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
