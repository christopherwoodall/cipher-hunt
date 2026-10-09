# Battery report: val-80-768-inf

- Target id: `val-80-768-inf`
- Claim: "Name 80's infinitive value at @768 via the 'vient [80-inf]' frame (e.g. transitivity/agreement probes against the '80 10 22' tail)."
- Date: 2026-10-09
- Worker: battery worker (subagent e984ea14-9e67-4032-8889-8c536bd1531e)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Parent: follow-up of `frame66-vient-80` (PROMOTE, 2026-10-09).
- All @-offsets below are 0-based.

Terms (ASD-STE100): "infinitive-shaped" = the group fills a governed-infinitive slot ("vient [80]" = "[subject] comes to [80]"). "Locus-bound" = the reading is licensed at the window but the value cannot be named beyond it. "Battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

"One candidate value parsing all three '[98] 80' windows, or fence the value as locus-bound."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** One candidate infinitive value parses all three '[98] 80' windows grammatically under standing values, with stated assumptions and no standing or red-team verdict contradicted.
2. **C2 (else-arm):** If no single value is nameable, fence 80's infinitive value as locus-bound with stated cause.

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-80-768-inf.lock` on start (agent id + 2026-10-09T19:08:00Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Adopted (not re-litigated): parent `frame66-vient-80` PROMOTE — 80 infinitive-shaped at @768 under A8 verb-frame grant, all six rivals killed (finite/noun/determiner/imperative/adverb/infinitive-subject). 80's other faces (adjective/modifier @469, determiner @1156, poly-80-docket FENCED R20-121) are red-team venue — untouched.
4. Standing values used: banked GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77=le); battery LEADs (98=vient, 94=ne, 78=ver, 48=e letter-tier, 06=ent); noun-class (43, 65; 66 nominal subject per parent).
5. Candidate generation: corpus "vient + X" collocate census over `code/side-period/corpus` (98 files); transitivity probe per the bar's suggested e.g.

## Window-level evidence (byte-exact)

The '98 80' bigram occurs exactly **3x** stream-wide: @440/441, @767/768, @1661/1662 (0-based; the 80 positions are @441, @768, @1662, matching the parent's labels).

- **W1 @440:** `16 78 63 45 46 43 | 98 80 | 50 78 41 10 62` = "…ce[45] que[46] [43-N] vient[98] [80-inf] [50] ver[78] [41] [10] [62]…" — relative clause, subject = 43 (noun-class). 80 in governed-infinitive slot. Finite-80 dies (two adjacent finite verbs); noun-80 dies ('venir' takes no bare-noun complement) — parent's rival kills transfer.
- **W2 @767:** `39 88 66 | 98 80 | 10 22 94 07 06` = "…a[39] [88] [66-subj] vient[98] [80-inf] [10] [22] ne[94] [07] ent[06]…" — subject = 66 (parent). Tail "10 22 ne 07ent".
- **W3 @1661:** `01 56 37 11 24 48 47 98 | 98 80 | 22 94 84 64 06` = "…e[48] ce[47] vient[98] vient[98] [80-inf] [22] ne[94] on[84] qui[64] ent[06]…" — double-98 noted: first 98 finite 'vient' with subject "ce"; second 98 finite 'vient' (asyndetic restart — syntax not adjudicated here). 80 remains in the governed-infinitive slot of the second; finite/noun rivals die as at W1.

80 is uniformly infinitive-shaped across the three windows (same post-"vient" slot, same dead rivals).

## Candidate test

Corpus "vient + X" (98 files, ~57M chars): bare "vient + infinitive" is rare. Top bare collocates are prepositions/pronouns/adverbs; infinitive hits: **faire(8), chercher(6), demander(4), tomber(4), prendre(3)** out of 986 bare "vient + X" tokens. ("vient" overwhelmingly takes "de"/"d'" — 839/1018 — the recent-past construction, not our frame.) No dominant infinitive collocate exists.

Each of faire / chercher / demander / prendre parses **all three windows** with an identical assumption profile:
- Transitive arm: W1 object=50, W2 object=10, W3 object=22 — all value-open groups, all admissible.
- Intransitive arm: tails parse adverbially/clausally with no contradiction.
The bar's suggested transitivity probe is **non-discriminating**: every window licenses both arms. The agreement probe is unavailable (infinitives do not agree). No window forces or eliminates any candidate — W1's 50, W2's 10, W3's 22 are all open.

Corpus frequency is not a battery-grade naming leg (lane precedent, val-37ent-adjective): "faire" at 8/986 does not clear the naming bar, and four rivals tie it within noise.

## Per-clause pass/fail

- **C1: FAIL.** No single infinitive value is nameable: at least four common infinitives parse all three windows with identical assumption profiles, no window discriminates among them, and the corpus yields no dominant collocate. Naming any one value would be arbitrary.
- **C2: FIRES.** 80's infinitive value is fenced as **locus-bound**: the infinitive READING is licensed at the three '[98] 80' windows (uniform post-"vient" slot, rivals killed per the parent), but the VALUE cannot be named beyond the locus.

## Verdict: NULL (fence executed)

Per lane precedent (name-or-fence fences resolve to NULL, not KILL): the value question is fenced, the reading stands.

## Scope (stated, not hidden)

- Value-fence only, scoped to the three '[98] 80' windows. Untouched: the parent's @768 infinitive-shape PROMOTE, A8 verb-frame grant, 80's other faces (adjective @469, determiner @1156 — red-team venue, poly-80-docket FENCED R20-121), 98='vient' LEAD, 94='ne' STRONG LEAD.
- W3's double-98 syntax (restart vs. reanalysis) is noted, not adjudicated — 98's first-instance role left open; it does not affect 80's slot.
- §7 intact: no split or polyvalence declared. No standing/red-team verdict contradicted or downgraded.
- Canonical-stream caveat stands (68/70 offsets unvalidated); W2 sits on the gloss-validated row a5_03 per the parent.

## Follow-ups (nulls regenerate work; all verified ABSENT from battery-queue.json)

1. **trans-80-768** (P3): narrow 80's transitivity — test whether 50 (W1), 10 (W2), 22 (W3) can serve as direct objects via their other windows' class evidence; a forced-transitive or forced-intransitive 80 shrinks the infinitive candidate class.
2. **val-80-517-lefaire** (P4): test @517 "le[77] [80]" — if 80="faire", "le faire" is the classic nominalized infinitive; a licensed "le [80-inf]" parse gives an independent leg for a "faire" candidacy (or kills it).
3. **subj-98-441-1662** (P4): resolve the "vient" subjects at W1 (43-noun?) and W3 (double-98: restart vs. reanalysis) — subject identity selectionally constrains the infinitive under motion-verb "venir".

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-80-768-inf.md` (this file).
- Queue: `val-80-768-inf` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; valid-doc repair + own-entry-only temp-file + rename; JSON re-validated post-write; no downgrade).
- Lock `code/crowd17/next-token/locks/val-80-768-inf.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
- **Pipeline flag:** `battery-queue.json` was found with a corrupted tail (stray `]}` appended after a complete 1559-target document — concurrent-writer artifact). Repaired by truncating to the valid document before writing; no target data was missing from the valid doc. Supervisor should audit for any lost concurrent appends per the last-writer-wins lesson (AGENTS.md).
