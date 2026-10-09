# Battery verdict: seg-a1_01-constraint-sweep

## Bar (verbatim, pre-registered)

"does offset 1 introduce any NEW kill-grade violation, or is it constraint-clean across the full row? Test A15 C1-C3 on 84@in-row-7, 96=par follower set on '96 44'@2, predicative frames 42/32, 67 positional rule"

Restated as numbered pass/fail clauses:
1. A15 C1–C3 on 84@in-row-7 (offset-1 index 7): no condition violated.
2. 96=par follower set on '96 44' (offset-1 index 2): no kill-grade violation.
3. Predicative frames 42/32 (offset-1 indices 26/33): no kill-grade violation.
4. 67 positional rule: no violation (testable or vacuous).
5. Full-row sweep: all 35 offset-1 pairs constraint-clean, no NEW kill-grade violation anywhere.

Adverses: none listed.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/seg-a1_01-constraint-sweep.lock` on start.
Re-derived the repaired stream in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per `repair_parse.py`
(1,847 pairs / 96 types verified). `canonical.py` never touched. R5005, sealed
gates, red-team adjudication queue untouched.

Row a1_01 canonical offset is 0 (verified in `repaired_offsets.json`), 71 digits.
Offset-1 pairs = `[d[i:i+2] for i in range(1, len(d)-1, 2)]` = 35 pairs:

```
idx: pair
0:89 1:13 2:96 3:44 4:10 5:12 6:48 7:84 8:38 9:13 10:06 11:29 12:60
13:09 14:27 15:93 16:71 17:17 18:98 19:55 20:83 21:55 22:31 23:24
24:10 25:83 26:42 27:94 28:01 29:29 30:49 31:26 32:91 33:32 34:46
```

All 35 are members of the 96-type canonical inventory (zero novel groups).
Row a1_01 spans 1-based stream @36–@70; canonical pair 17 ('11') = 0-based
stream 52, pair 18 ('79') = 0-based stream 53 — byte-identical to the red-team
R18 banked contradiction "@52–53: 'la tout'" (0-based convention).

## Clause results

### C1 — A15 C1–C3 on 84@in-row-7: PASS

Offset-1 index 7 = '84', window "48 84 38" (48='e' letter-tier prom, 38 open).
- C1 (77='le' provisional): no 77 in the window; the condition is not engaged.
  No new violation.
- C2 (62/'on' collision resolved; 84 holds 'on' unconditioned): no 62 in the
  window; no second 'on' group introduced (§7 intact). No new violation.
- C3 (R1/R2 fenced residuals): untouched. No new violation.
- Contact check: "48 84" is already attested canonically (84 predecessors
  include 48 x1); "84 38" is novel (38 not in 84's canonical follower set)
  but "on [38]" is unconstrained — 38's value is open. Neither is kill-grade.

### C2 — 96=par follower set on '96 44'@2: PASS (novelty, not violation)

44 is not in 96's canonical follower inventory
({00:3, 56:1, 47:1, 87:3, 21:3, 43:2, 45:2, 40:1, 09:1, 48:1, 86:1, 82:2};
44 = 0/22) — the contact is novel. But "par [44]" is grammatical 1841 French:
clitic-44-census (promote) classifies 12/15 of 44's windows whole-word
nominal. A novel contact is not a kill-grade violation. Recorded as novelty.

### C3 — Predicative frames 42/32: PASS

- 42 (noun, class-level) at offset-1 index 26, window "83 42 94":
  "[83] [42-noun] ne". Under the 83='de' lead this is "de [42] ne" —
  grammatical. The A1 predicative grant is permissive (value open), not
  mandatory; 42 is not forced predicative here. "83 42" is a novel contact
  (83 not in 42's canonical predecessors) but unconstrained.
- 32 (verb, class-level) at offset-1 index 33, window "91 32 46":
  "[91] [32-verb] que" (46='que' GT) — verb + "que" is grammatical.
  "91 32" is attested canonically (x2); "32 46" is novel but grammatical.
- No kill-grade violation at either window.

### C4 — 67 positional rule: PASS (vacuous)

Zero 67 groups among the 35 offset-1 pairs; the rule
(67="veut" iff follower infinitive-shaped) has nothing to test. No violation.

### C5 — Full-row sweep: PASS, constraint-clean

Every banked/promoted/provisional value respected; every kill respected:
- 48 read only as 'e' (letter-tier prom), never est/ne/de (killed).
- 29='er' (GT) x2 followed by open 60/49 — unconstrained.
- 06='ent' (prom, R17-007) followed by 29: "06 29" attested canonically x4.
- 12='n' + 48='e' at indices 5–6 compose "ne" letter-internal, mirroring the
  battery-confirmed "prenne" letter composition (enne-family-12-94).
- 94='ne' STRONG LEAD (R17-001) at index 27: "42 [noun] ne [01]" — standard
  negation frame. "94 01" novel contact, unconstrained.
- 17='fois' (prom) at index 17: "[71] fois [98]"; "71 17" attested x1.
- 89 (A8 verb-frame, value open) row-initial + open 13 — fine.
- 24='faire' (battery-promoted) + open 10 — fine.
- 93 (verb class), 98 (finite verb, battery-promoted pending ratification):
  no forced ungrammaticality ("fois [98-verb] [55]" admits a clause boundary).
- 46='que' (GT) final, preceded by verb-class 32 — fine.
- No 11, 70, 82, 34, 40, 87, 64, 79, 00, 47, 59, 77, 45, 30, 20, 81 in offset-1;
  splits (20~17, 23~26), holds (19, 45 A11, 09~92 A6, 33+29 A10), A12 (37-01),
  A7-L2 — all untouched.
- Headline: the canonical banked contradiction "la tout" (0-based @52–53)
  DISSOLVES under offset-1 — neither '11' nor '79' survives as a group
  (digits re-pair to "17 98" = "fois [98]").

## Verdict: PROMOTE (sweep finding — promotes no value, kills nothing)

Offset-1 is constraint-clean across all 35 pairs of row a1_01: it introduces
zero new kill-grade violations and dissolves the "la tout" banked
contradiction. The re-segmentation is a viable mechanism behind the red-team
la-tout fence at battery grade. Whether to adopt offset-1 for row a1_01 is a
red-team adjudication act — not declared here.

## Standing-state check

No standing verdict contradicted or downgraded. §7 intact (no polyvalence
declared). No red-team verdict on a1_01's segmentation exists.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-a1_01-constraint-sweep.md`
- Queue: `seg-a1_01-constraint-sweep` → verdict/promote (temp-file + rename;
  pre-write assert confirmed queued/verdictless; JSON re-validated post-write).
- Lock created on start, deleted on completion.
