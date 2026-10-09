# Battery report: sub02-wordinternal

**Target:** `sub02-wordinternal`
**Date:** 2026-10-09
**Verdict: KILL** — the uniform rightward-composing 02 theory is dead at kill grade. The class question is not dissolved.

## Bar (verbatim, pre-registered)

> compositional account dissolves class question

Restated as numbered pass/fail clauses before testing:
- **C1 (uniform composition):** 02 composes rightward as a letter/syllable cluster into a grammatical French word ("[02 X]") at every one of its 17 windows, under standing values.
- **C2 (dissolution):** with C1 holding, the word-level class question for 02 (verb/noun/conjunction split) dissolves without a §7 declaration.

## Method

Read BATTERY-PROTOCOL.md first. Lock `locks/sub02-wordinternal.lock` created on start
(worker aa8ac989-3042-46fb-a22a-b57dbadb0011, 2026-10-09T05:45:23Z). Stream re-derived
in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py`: 1,847 pairs / 96 types, n(02)=17
(byte-identical to the standing 02-class-609 census). `canonical.py` never touched.
R5005, sealed gates, red-team adjudication queue untouched.

Standing premises (protocol §7, never re-litigated):
- 64='qui' banked GT; 70='pre' banked GT (pencil); 11='la' banked GT.
- 79="tout" granted (A5); 00="pour" granted (A9, leg-1 class-level).
- 02-class-609 NULL (2026-10-09): 02's profile is an irreducible distributional split
  (verb-selecting at the two qui-windows @609/@750 0-based; verb-excluding at @305
  and @858); §7 split candidacy, no polyvalence declared.

## The 17 windows of 02 (0-based, byte-derived)

| @ (0b) | row | context (02's neighbors bolded via position) |
|---|---|---|
| 128 | a1_03 | 98 82 48 11 **02** 26 32 96 56 |
| 305 | a2_04 | 91 18 89 88 **02** 88 20 17 46 |
| 410 | a2_08 | 26 00 33 01 **02** 53 84 51 37 |
| 459 | a2_10 | 65 13 66 14 **02** 79 87 11 59 |
| 495 | a2_11 | 67 78 42 94 **02** 79 88 47 11 |
| 609 | a4_00 | 54 64 39 64 **02** 58 47 77 87 |
| 695 | a5_01 | 03 39 74 46 **02** 50 45 28 94 |
| 718 | a5_01 | 00 66 86 01 **02** 21 80 77 03 |
| 750 | a5_03 | 85 28 00 64 **02** 97 40 67 11 |
| 858 | a5_07 | 64 32 48 84 **02** 24 49 74 74 |
| 887 | a5_08 | 79 68 37 03 **02** 00 86 06 77 |
| 916 | a5_09 | 59 37 96 09 **02** 24 49 74 74 |
| 1084 | a6_05 | 06 52 89 24 **02** 55 81 00 33 |
| 1152 | a6_08 | 67 33 66 84 **02** 00 92 29 80 |
| 1299 | a7_03 | 80 04 62 16 **02** 70 37 08 43 |
| 1467 | a7_09 | 21 62 48 21 **02** 62 38 26 12 |
| 1819 | a8_10 | 06 29 37 01 **02** 09 19 00 97 |

02's successor set: {26, 88, 53, 79x2, 58, 50, 21, 97, 24x2, 55, 00x2, 70, 62, 09}.

## C1: FAIL at kill grade

The three named loci are composition-compatible (neighbors open):
- "02 58" @609 — 58's class open; nothing forces or forbids "[02 58]".
- "02 97" @750 — 97's class open; same.
- "02 26" @128 — 26 contested; same.

But a UNIFORM rightward-composing 02 must also compose at four windows where the
right neighbor is a granted complete French word that accepts no prefixation:

1. **@459 (a2_10):** right neighbor **79="tout"** (A5 granted). No French prefix
   attaches to "tout" ("retout", "détout", … are not French words). "[02]tout" is
   unformable for every possible 02 value. Phase-solid row (a2_10 favors the
   repaired phase; not in the phase sweep's rival or tie lists).
2. **@495 (a2_11):** right neighbor **79="tout"** again. Same kill. Phase tie
   (a2_11 +0.18 in the phase sweep) — caveat noted, kill conditional on phase.
3. **@887 (a5_08):** right neighbor **00="pour"** (A9 leg-1 class-level grant;
   the conditioned 00='contre' rival lives only after 96='par' — not here).
   No French prefix attaches to "pour" ("repour", "surpour", … are not French
   words). "[02]pour" is unformable for every possible 02 value. Phase-solid
   (a5_08 not rival/tie in the sweep).
4. **@1152 (a6_08):** right neighbor **00="pour"** again. Same kill. Phase tie
   (a6_08 +0.99) — caveat noted.

Two of the four kills (@459, @887) are phase-solid; the other two carry the
standing canonicality caveat. Even on the most conservative reading, **two
windows force the uniform rightward-composition mechanism false at kill grade**.
The mechanism cannot be rescued by any 02 value: the impossibility sits in the
granted right neighbor, not in 02.

Side note on @1299 ("02 70", 70='pre' banked GT): letter-level composition is
underdetermined there (not kill-grade; not needed).

## C2: not reached

The uniform theory is dead, so no compositional account dissolves the class
question. A locus-scoped composition (02 sub-lexical only at @609/@750/@128)
remains compatible with standing values — the neighbors there are open — but it
leaves the class question alive at the other 14 windows and therefore does not
satisfy the bar.

## Standing state

No red-team verdict on 02 exists; nothing contradicted or downgraded. The kill
is consistent with 02-class-609's §7 split candidacy (it closes one resolution
route — uniform sub-lexicality — without touching the split). §7 intact.

## Follow-ups proposed (kill — optional)

1. `phase02-kill-windows` (P3) — re-derive @495 (a2_11) and @1152 (a6_08) under
   offset-1 (both are phase ties in the sweep). If the "02 79"/"02 00" bigrams
   dissolve there, the kill narrows to the phase-solid @459/@887.
2. `val-58-609-lex` (P4) — once 58's class/value lands, test "02 58" @609 as a
   composed French verb word with named letters (locus probe; does not dissolve
   the class question).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-sub02-wordinternal.md`
- Queue: `battery-queue.json` `sub02-wordinternal` → status `verdict`,
  `verdict: {result: kill, report: ..., date: 2026-10-09}` (temp-file + rename,
  pre-write assert confirmed `queued`/verdictless, JSON re-validated post-write).
- Lock `locks/sub02-wordinternal.lock` deleted on completion.
