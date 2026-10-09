# Battery report: ne-alone-02-74

- Target: `ne-alone-02-74`
- Verdict: **KILL**
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`), re-derived for this battery. 1,847 pairs / 96 types confirmed. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Note on offsets: the brief cites @494/@785 (1-based); 0-based they are @493 and @784. All offsets below are 0-based.

## Bar (verbatim from battery-queue.json)

(1) both windows parse as '[42] ne [verb]...' with 'pas' located downstream or 'ne'-alone justified against the 1840s modal list (pouvoir/savoir/oser/cesser); (2) 02/74 show verb-frame contact somewhere (A8 80/89-class, 29='er', 85-stem, or infinitive complement); (3) the '74 74' x6 self-loop (@417, @816, @861, @919, @1053, @1637) parses under the winning value or is fenced as formula; (4) @1795 '42 n'est 37' stays consistent. 42 is NOT re-valued (A1 grant holds)

## Numbered clauses

- C1: @493 ('42 94 02') and @784 ('42 94 74') parse as '[42] ne [verb]...', with 30='pas' located downstream in the same clause, OR bare-'ne' justified against the 1840s modal/fixed-frame list.
- C2: 02 and 74 show verb-frame contact somewhere: a follower in A8 80/89-class, 29='er', 85-stem, or an infinitive complement (33-class).
- C3: the '74 74' x6 self-loop (@417/@816/@861/@919/@1053/@1637) parses under the winning value, or is fenced as formula with stated cause.
- C4: @1794 ('42 94 59 37', 1-based @1795) '42 n'est 37' stays consistent with the A1 grant.

## Method

Fresh byte-exact re-parse of the repaired stream. Full census of 02 (n=17) and 74 (n=34) with predecessor/follower distributions; row-bounded downstream-'pas' search; the three '94 74' windows and both '42 94 X' target windows examined at byte level.

## Window evidence

- @493 (row a2_11): `30 01 19 64 76 42 41 20 67 78 | 42 94 02 | 79 88 47 11 29 40` — '42 94 02' with 79='tout' after 02. Row spans 477..501; **no 30 downstream in the row**; nearest 30 anywhere is @560 ('86 94 59 30 67 11', a different clause, 67 tokens away).
- @784 (row a5_04): `11 24 42 | 94 74 | 65 84 06 77 64 46` — '42 94 74' with 65 (noun-class) and 84='on' after 74. Row spans 774..799; **no 30 downstream in the row**; nearest 30 anywhere is @993 (~200 tokens away).
- @1794 (row a8_09): `42 94 59 37 91 79` — the 94-59 'n'est' control (R17-001: 94-59 x3). Consistent; no 02/74 involvement.
- '42 94' is a closed set: @493 (02), @784 (74), @1794 (59). No other '42 94' windows exist.
- 02 (n=17): prev 01 x3, 64 x2, 84 x2, 11, 88, 14, 94 x1 (@495), 46. Foll 79 x2, 24 x2, 00 x2, 26, 88, 53, 58, 50, 21, 97. **Zero followers in {80, 89, 29, 85, 33} across all 17 windows.**
- 74 (n=34): prev 74 x6, 49 x5, 94 x3 (@350, @786, @1103), 39 x2, 44 x2, 36 x2. Foll 74 x6, 45 x3, 46 x3, 62 x3, 67 x2, 77 x2, 65 x2, 47 x2, 48, 49. **Zero followers in {80, 89, 29, 85, 33} across all 34 windows.**
- '74 74' x6: @417 `49 74 74 46 49 36`; @816 `49 74 74 47 78 40`; @861 `49 74 74 48 47 46`; @919 `49 74 74 40 08 65`; @1053 `29 74 74 45 23 77`; @1637 `87 74 74 35 56 12`. Four of six are '49 74 74 [46/47/48/40]' — pronoun-particle chains, not verb frames.
- Other '94 74' windows: @350 `70 12 94 74 67 78 40` ('ne [74] et/veut' — second verb adjacent, no modal frame); @1103 `82 94 74 47 78 65` ('ne [74] ce' — 'ce' is not an infinitive; ungrammatical under any modal reading).
- 02's nearest misses: '02 88' x1 (@305, governor-class, not A8 80/89), '02 24' x2 (@858/@916, 24=verb-class *following* 02 — a verb after 02, not 02 in a verb frame; reads as '[02] [verb]', pointing away from a verbal 02). '02 00' x2 (@887/@1152, 00='pour' — prepositional follower, not verbal).

## Per-clause pass/fail

- **C1: FAIL.** No 'pas' (30) in either target clause (row-bounded search; nearest tokens are in unrelated clauses 67+ tokens away). The ne-alone fallback arm requires 02/74 to be modal/fixed-frame verbs, which C2 independently rejects; the modal list cannot rescue a non-verb. The A1-predicative-42 subject account is moot once the verb slot fails.
- **C2: FAIL at distributional grade.** 51 combined windows of 02+74 contain zero verb-frame contact in the bar's stated test set (no 80/89, no 29='er', no 85-stem, no 33 infinitive). The lane's distributional standard rejects the verb claim. 74's profile actively resists verb-shape (self-loop x6, pronoun/particle followers 45/46/62/77/47, 49-prev x5 in formulaic chains).
- **C3: FAIL / no winning value.** '74 74' x6 does not parse as 'verb verb' under any French frame present in the windows (four of six sit in '49 74 74 [pronoun-particle]' chains). With the verb value dead at C2, there is nothing to attach a formula fence to at battery level.
- **C4: PASS.** @1794 '42 94 59 37' is the standing 94-59 'n'est' control; consistent, untouched by this verdict.

## Verdict: KILL

The claim's core — 02 and 74 are the negated verbs in '42 ne 02' / '42 ne 74' — is rejected at the lane's distributional standard: no 'pas' in either clause, and 51 windows of 02+74 with zero verb-frame contact in the bar's stated test set. No standing red-team verdict is contradicted or downgraded: 94='ne' keeps its R17-001 STRONG LEAD grading (this kill does not touch it), the A1 predicative grant on 42 holds, and C4's control window is undisturbed.

## Adverses answered

- 02's followers (79/24/00 x2...) and 74's followers (74 x6, 45, 46, 62...): confirmed byte-exact; none is a verb marker in the bar's test set. Answered by the census.
- '74 74' x6 resists verb-shape: confirmed; the resistance is part of the kill evidence (C3).
- A1-predicative 42 needs a clause/subject account for '42 ne': moot — the verb slot fails first, so no subject account is owed by this battery.

## Proposed follow-ups (for supervisor queuing)

1. `noun-74-formula` (P3): test 74 as a nominal/formula head — '49 74 74 [46/47/48/40]' chains x4, 49-prev x5, self-loop x6; promote iff a French nominal/formula frame parses the chains; kill iff 74 shows verb-frame contact.
2. `subj-42-ne-frame` (P2): given the @1794 '42 n'est 37' control, test what fills the X slot in the closed '42 94 X' set ({02, 74, 59}): if X is nominal-shaped in all three, the '42 94' frame is copular/negative-nominal rather than verbal; fence or name accordingly.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/ne-alone-02-74.lock` created on start, deleted on completion.
- `battery-queue.json`: `ne-alone-02-74` → status `verdict`, result `kill` (temp-file + rename, own entry only, pre-write assert confirmed no prior verdict, JSON re-validated).
