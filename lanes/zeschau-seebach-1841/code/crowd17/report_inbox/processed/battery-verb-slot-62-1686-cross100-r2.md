# Battery report: verb-slot-62-1686-cross100 — SECOND REPORT (r2, double-dispatch)

**Double-dispatch note:** this target was dispatched twice within seconds
(supervisor + topup-hook race; locks created 20:49:54Z by worker
db54b11b-09fc-4613-b5c0-587059410e3a and 20:50:00Z by worker
98fa3349-a171-481c-9c57-908248212940, same lock path — the second write
won). The first worker completed first and recorded
`verdict`/`promote` in battery-queue.json with its report at
`code/crowd17/report_inbox/battery-verb-slot-62-1686-cross100.md`. Per the
never-downgrade / no-op-on-existing-verdict rule, this worker did NOT touch
the queue entry. This file is the second worker's independent analysis,
archived as r2.

- Target id: `verb-slot-62-1686-cross100`
- Claim: contrast parse: under provisional 59='est', test whether @100's
  '62 94 93 59 45 28 00 46' parses cleanly as a ne...que bracket
- Date: 2026-10-09
- Worker: battery worker (subagent db54b11b-09fc-4613-b5c0-587059410e3a),
  independent run
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session).
  `canonical.py` never used. R5005, sealed gate instances, red-team
  adjudication queue untouched.
- Prior: `battery-verb-slot-62-1686-neque.md` NULL 2026-10-09 (fenced
  @1686-1694 empty verb slot; follow-up 1 is this target). Working
  conclusion under test: "the empty-verb-slot is window-local, not
  geometry-wide — @100's bracket holds a licensed verb (59='est'
  provisional) inside its span, so the geometry CAN host a verb."

Terms (ASD-STE100): "bracket geometry" = adjacent "62 94" followed by a
"46" within 12 groups (the ne...que-shaped span). "Licensed verb" = a
finite-verb value granted or provisional in a standing verdict.

## Standing record adopted (not re-litigated)

- **62='il' is KILLED at kill grade** (R19-097/R19-106; confirmed R20-125).
  62 is value-open; no parse here may assign or lean on 62='il'.
- **94='ne' is STRONG LEAD, not granted** (R17-001 rejected the promote;
  R19-167, R20-007 confirm). C3 below grants it as a working premise only;
  any pass would be conditional.
- **59='est' is provisional** (R20-066; standing). The ONLY licensed
  finite-verb value in §7.
- 46='que' pencil ground truth. 00='pour' granted (A9, leg-1 class-level).
  45='ce' hold (A11). 93, 28 value/class open. §7 intact; no standing
  red-team verdict contradicted.

## Bar (verbatim, pre-registered before testing)

"discriminates isolated-@1686 residual vs a geometry that fails even with
its licensed verb present"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (span integrity):** the repaired stream yields
   `62 94 93 59 45 28 00 46` at offsets 100-107 (46 at +7 from the
   `62 94` locus @100).
2. **C2 (licensed verb present):** 59 occupies @103 inside the span, so the
   geometry's only licensed finite verb (59='est', provisional, R20-066)
   is present.
3. **C3 (clean ne...que parse):** granting 94='ne' as working lead
   (ungranted, R17-001) and using only standing values (46='que' banked;
   59='est' provisional; 00='pour' granted A9; 45='ce' A11 hold; 62 != 'il'
   per kill R19-097/R19-106/R20-125), the @101-107 sequence parses cleanly
   as a French "ne ... que" restrictive bracket with 59='est' the finite
   verb, zero ungranted assumptions. FAIL = the geometry fails even with
   its licensed verb present.
4. **C4 (discrimination fires):** C1-C3 all pass -> isolated-@1686 residual
   stands (geometry hosts its verb elsewhere); C3 fails with C1-C2
   passing -> geometry-wide failure (the @1686 residual is not isolated).
   Either way the bar's discrimination is executed.

Adverses: "62='il' kill-grade (R19-097/R19-106, R20-125); 94='ne' strong
lead not granted" — answered in §Adverses below, never ignored.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the shared lock path on start
   (agent id + 2026-10-09T20:49:54Z); it was overwritten 6s later by the
   racing worker; no lock remained at completion — nothing left to delete.
2. Re-derived the repaired stream byte-exact in-session
   (`repair_parse.py` logic; upstream-offsets a5_03 flipped 1->0 asserted;
   1847 pairs / 96 types asserted).
3. Verified C1/C2 windows byte-exact; census of all 9 `62 94` loci:
   [100, 508, 761, 840, 1329, 1362, 1686, 1704, 1772] (matches prior
   report).
4. Structural French parse test of @101-107 under the clause premises;
   competitor-role census for `00 46` (4 loci) and `59 45` (1 locus);
   distributional check of open tokens 93 (14x) and 28 (6x).

## Window-level evidence (repaired stream, byte-exact)

- @95-112: `46 29 85 08 21 | 62 94 93 59 45 28 00 46 | 11 21 67 93`
  (@100-107 confirmed: `62 94 93 59 45 28 00 46`; 46 at +7 from @100).
- Bracket geometries (`62 94` + closing 46 within 12): exactly 2 — @100
  and @1686 (prior census confirmed).
- `59 45` bigram: occurs exactly ONCE in the 1,847-pair stream — at
  @103-104. Stream-unique.
- `00 46` bigram: 4 loci — @106 (`45 28 00 46 11 21 67 93`), @545
  (`42 06 00 46 24 47 46 55`), @1545 (`78 43 00 46 70 12 94 92`),
  @1680 (`77 44 00 46 79 65 13 93`).
- 93: 14x; top pre-partners 45(3), 13(2), 15(2); top post-partners 62(2),
  52(2), 59(1, this window only). Class open; too sparse for a licensed
  subject role.
- 28: 6x; post-partners 00(3), 94(1), 52(1), 89(1). Class open.

## Per-clause pass/fail

1. **C1: PASS** — @100-107 = `62 94 93 59 45 28 00 46`, 46 at +7.
   Byte-exact.
2. **C2: PASS** — 59 at @103 inside the span; the geometry's only licensed
   finite verb (59='est' provisional) is present.
3. **C3: FAIL at structural grade.** The @101-107 sequence
   `94(ne-lead) 93(?) 59(est) 45(ce) 28(?) 00(pour) 46(que)` does not parse
   cleanly as a French restrictive "ne ... que" with 59='est' the finite
   verb, even granting 94='ne' and 59='est' as working premises:
   - (a) **"est-ce" inversion order.** The span reads 59 then 45 = "est ce",
     verb-subject inversion = interrogative order in modern French. A
     declarative restrictive "ne ... est-ce ... que" is not clean French.
     The `59 45` bigram is stream-unique (1/1847 pairs) — no declarative
     precedent anywhere.
   - (b) **"pour que" competitor for 46.** 00='pour' (granted A9) sits
     adjacent to 46='que' at @106-107, forming the idiomatic "pour que"
     subordinator. If 46 is the "pour que" complementizer, there is no
     restrictive que in the span and the ne...que bracket collapses. 4x
     `00 46` in-stream; the unit is live.
   - (c) **Kill-grade 62 constraint bites.** The only natural French
     subject for "ne ... est ... que" at this locus would be 'il' at 62 —
     killed at kill grade (R19-097/R19-106, R20-125). 93 (open, 14x,
     sparse) cannot carry the subject role with zero ungranted
     assumptions.
   - (d) **Two open-class tokens need roles.** 93 and 28 are value/class
     open; a "clean" parse needs both in licensed roles with zero
     ungranted assumptions — impossible under standing values.
   Strikes (a), (b), (c) are structural and independent of the 94='ne'
   lead: even if 94='ne' were granted tomorrow, this span still would not
   parse cleanly as ne...que.
4. **C4: FIRES (arm B)** — C1-C2 pass, C3 fails: the geometry fails even
   with its licensed verb present.

## Adverses

- **62='il' kill-grade (R19-097/R19-106, R20-125): ANSWERED.** The C3 test
  excluded 62 from any subject role; 62 stays value-open. The kill bites
  as strike (c): it removes the only natural subject, which is part of
  why the clean parse fails. Not re-litigated; used as constraint.
- **94='ne' strong lead not granted: ANSWERED (fenced).** C3 granted it as
  working premise only, and the failure is structural (strikes a-c hold
  regardless of 94's eventual status). Even a future 94='ne' grant would
  not rescue this span's ne...que parse. Red-team call on the lead itself
  remains open; `neque-94lead-gate` is already queued.

## Verdict (independent, r2 — NOT applied to queue)

**KILL** of the working hypothesis under test ("the @100 bracket parses
cleanly as ne...que with 59='est' its licensed verb, so @1686's empty slot
is an isolated/window-local residual"). **Arm B of the bar fires: a
geometry that fails even with its licensed verb present.** The @1686
residual is NOT isolated: the ne...que geometry fails at @100 too (for
different reasons than @1686 — @1686 has no licensed verb; @100 has the
verb but the geometry still does not parse).

**Verdict-label note vs r1:** the first worker recorded PROMOTE ("the
discrimination is decisively made at battery grade"). Both workers agree
on substance — @100's bracket does NOT parse cleanly as ne...que despite
holding the only licensed finite verb; the geometry fails structurally at
both windows. We differ only on the label: this worker reads the bar's
arm-B outcome as killing the isolated-residual hypothesis (C3 fails at
structural grade = a window forces the hypothesis false), hence KILL;
r1 reads the decisive discrimination itself as the promotable result.
Substance identical; label differs. Queue verdict (promote, r1) stands —
never downgraded.

## Follow-ups proposed (for supervisor consideration)

1. `pourque-00-46-role` (P3) — Claim: 46 at @107 is the "pour que"
   complementizer, not a restrictive que; the @100 span is a purpose
   clause, not a ne...que bracket. Bars: "46's role is decided by
   adjacency: 00 46 is adjacent (granted 'pour' + banked 'que') and the
   post-46 clause (@108+: 11 21 67 ...) is tested for subjunctive shape at
   >=3 of the 4 `00 46` loci". Priority 3. Evidence: this report (strikes
   a-b). Adverses: 67 et/veut polyvalence; 93/28 open; 94='ne' lead
   ungranted.
2. `estce-59-45-inversion` (P4) — Claim: the stream-unique `59 45` bigram
   at @103-104 is interrogative inversion ("est-ce"), incompatible with a
   declarative ne...que bracket. Bars: "no declarative `59 45` bigram
   exists in the 1,847-pair stream; inversion reading is the only French
   grammar fit". Priority 4. Evidence: this report (strike a). Adverses:
   59='est' provisional only; French-grammar premise unlicensed by
   red-team.
3. `neque-94lead-gate` — already queued. Not re-proposed. Note for the
   gate: this report fences that even a 94='ne' grant would not rescue the
   @100 span's parse (structural strikes a-c).

## Bookkeeping

- Report: this file (r2 archive; the queue-pointed report is the r1 file).
- Queue: NOT touched by this worker — entry already `verdict`/`promote`
  (r1). No downgrade, no rewrite, no tmp write performed.
- Lock: shared path overwritten by racing worker at 20:50:00Z; no lock
  remained at completion — nothing to delete.
- R5005, sealed gate instances, red-team adjudication queue untouched.
- Incidental: `code/crowd17/next-token/` holds two generic-named tmp
  files (`tmp2_tyqwx4`, `tmpjcco1ygz.tmp`) not created by this worker —
  flagged for supervisor awareness, not cleaned (out of this target's
  scope).
