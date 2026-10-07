# smithliaison — round-12 liaison report (2026-10-07)

**Role:** Smith-liaison executor, round-12 WO8. Read-mostly; rebuild side
unchanged; no solver work run by the liaison.

## Rebuild-side state delta since F78 (round-11 memo): NONE

- `code/side-homophonic-rebuild2/` — every file still dated 2026-10-07,
  19:18–19:26; **no new writes, no results/**, no red-team rulings beyond
  `RULINGS.md` (19:30:40, unchanged).
- Track A: reference validated, but step-3 sanity + diagnostic rescore
  NOT run (R4a hard-exit fix still unaddressed).
- Track B: PREREG.md only — no code, no training (R5b Guizot-offset
  exclusion bound; R5a hit-table inconsistency unaddressed).
- Track C: decode plumbing done; §4 hygiene gate and `score_boundaries.py`
  NOT run (R3a/R3b unaddressed).
- Tally unchanged: 0 KILL / 0 DEMOTE / 3 GO.

## Constraints banked (round-11 adjudication → scorer, round-12 delta memo)

Full memo: `code/crowd12/smithliaison/smith-constraints-round12.md`.
New scorer constraints from R1–R7 (RULINGS-ROUND11, docket CLOSED 7/7):

1. **06="ent" iff pre=82** (ISLET 3 tightened, n_eff=3, falsifiers
   unfired); @1355 «ne ment pas» rare-but-real in diplomatic genre —
   Les-Mis priors must not veto the genre reading.
2. **33 = infinitive-class** (C1 PASS; pre==00×8, suc==29×5, pre==67×1);
   @1450/@1623 lean-veut (LEAN); 67 fork stays SUPPORTED.
3. **-este verb scored set-valued** {manifeste, atteste, proteste,
   conteste, déteste}; no single -este ID as a fixed target.
4. **@1248 «pour 33 16 pour 67 que» double-pour stack is an ERA VETO**
   (0 in ~16.5MB 1840s formal French). Label correction: frame =
   pairs[1244:1255].
5. **@633 → et-CONDITIONAL(C1∧C2)** (deps travel with the reading).
6. **48 stays UNIDENTIFIED** — all paths fenced; the "de"-conditional
   is the only live word-reading but NOT settled (ML-1/ML-2 legs missing);
   scorer may not lean on it.

Retired: the round-11 memo's six live hazards are all closed. Watch-list
(open, not constraints): 48 ML-1/ML-2, @863 «de ce que» follow-up, -este
T1–T5 tie-breakers, 94-82-06-06 4-gram hypothesis.

## Search scope: ZERO, maintained

No joint search run; none recommended. C1 not run on the gapped family;
main-fleet scope stays zero per STATE.md until it passes.
