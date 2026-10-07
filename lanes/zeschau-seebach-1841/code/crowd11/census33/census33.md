# 33-CLASS CENSUS — analysis note (round 11, work order 3)

Executor: 33 CLASS CENSUSER. Prereg: `PREREG.md` (2026-10-07 20:59:25 UTC).
Code: `census33.py`. Results: `census33_results.json`.

## Census (repaired 1,847-pair stream; n33=25; 23 in-census, 2 decider-excluded)

| pos | pre | suc | inf | nom | notes |
|-----|-----|-----|-----|-----|-------|
| 24 | 47 | 55 | – | N3/N6 | pre=47 "ce"-lead |
| 186 | 00 | 16 | I1 | – | pour-lead |
| 265 | 52 | 42 | – | – | unclassified |
| 273 | 67(et@272) | 29 | I4 | – | "et 33-er" |
| 408 | 00 | 01 | I1 | – | pour-lead |
| 467 | 00 | 79 | I1 | – | pour-lead |
| 626 | 37 | 29 | I4 | – | stem+er |
| 776 | 15 | 73 | – | – | unclassified |
| 846 | 00 | 96 | I1 | – | pour-lead |
| 936 | 00 | 21 | I1 | – | pour-lead |
| 1000 | 82 | 00 | – | – | unclassified ("m pour"?) |
| 1088 | 00 | 79 | I1 | – | pour-lead |
| 1149 | 67(et@1148) | 66 | – | – | unclassified |
| 1232 | 47 | 29 | I4 | N3/N6 | mixed: "ce"-lead + stem+er |
| 1245 | 00 | 16 | I1 | – | "ce la pour 33" |
| 1421 | 15 | 21 | – | – | unclassified |
| 1424 | 67(veut@1423) | 29 | I2,I4 | – | "veut 33-er" |
| 1477 | 67(et@1476) | 29 | I4 | – | "et 33-er" |
| 1502 | 84 | 42 | – | – | unclassified |
| 1504 | 42 | 00 | – | – | unclassified |
| 1630 | 00 | 21 | I1 | – | pour-lead |
| 1642 | 12 | 98 | – | – | unclassified |
| 1700 | 85 | 94 | – | – | unclassified |
| 1451 | 67(open@1450) | 46 | – | – | EXCLUDED (decider; suc=46 ambiguous) |
| 1624 | 67(open@1623) | 46 | – | – | EXCLUDED (decider; suc=46 ambiguous) |

## Bar audit

- Infinitive kinds fired: **I1 ×8** (E=0.68, p≈0.0), **I4 ×5** (E=0.56,
  p=0.0002), **I2 ×1** — three independent kinds.
- Nominal: N3/N6 ×2 (E=0.75, p=0.17 — chance-consistent); **N1=0, N2=0,
  N4=0, N5=0**.
- **C1: PASS** (≥2 inf kinds; zero GT-anchored nominal; zero N5).
  C2 fails (14 inf hits). → **33 = infinitive-class.**

Notable internal consistency: the three et-classified 67-windows with
suc==33 read "et 33-er" ×2 (@273, @1477) — et coordinating infinitives,
exactly what infinitive-class 33 predicts; the one veut-classified window
reads "veut 33-er" (@1424) — textbook modal+infinitive. The fork's own
classified windows corroborate the census verdict.

## Era class-matched frames (Nesselrode v8, NW=92,123)

- "veut * que" n=2: **"il veut prouver que les journalistes…"**
  (compositional infinitive+que ✓); "il veut coûte que coûte faire"
  (frozen idiom, discounted).
- "et * que" n=16, middles: ce×4, espérait, dès, verbalement, certain,
  croyez, tandis, crains, dire, dmitri, puis, pour, veut. Clean nominals
  5/16 (ce×4, dmitri); "et dire que" is the frozen infinitive idiom (n=1).
- Honest note: era counts do not discriminate the arms (1 vs 1 on the
  infinitive reading). The decider evidence is the census, not the era
  count; the era frames are consistency checks.

## Decider application (F74)

**C1 passes → lean-veut at @1450/@1623: 67="veut" lives.**
"veut [infinitive] que" is era-compositional ("veut prouver que"); the
et-arm would need "et [infinitive] que", attested only as a frozen idiom.
Grade: **LEAN** (one new bar; lane ≥2-check rule). No status change to
67="veut" (stays provisional); fork stays SUPPORTED; @1248 scope amendment
untouched; E7's failed L1/L2 not re-litigated.

Sensitivity: the decider windows' own 33s (@1451: pre=67-open, suc=46;
@1624: pre=67-open, suc=46) are per-prereg AMBIGUOUS and unscored —
anti-circularity held. Consistency datum (not a leg): @1624's pre-chain
66-67, and 66-class includes infinitive (F65).

## Frenchman register check

1. "pour + infinitive" — standing; no veto. ✓
2. "veut prouver que" — v8-attested compositional; Gate-4/cela concerns
   do not touch infinitives. ✓
3. "et X que" middles hand-classed; "et dire que" flagged frozen. ✓
4. "stem + er = infinitive spelling" — F22 standing. ✓
5. No cela-class (F73/EV11), no @1248 use (EV12), no settled-kill
   re-litigation. ✓

## What's still missing

1. **Second independent leg** for 67="veut" at @1450/@1623 (lean→
   classification): pre-side of 36 (@1449) / 66 (@1622), or another
   infinitive-governed 33 frame.
2. **33's specific value**: the 8 "pour 33" frames are an identification
   battery waiting to happen (era "pour [inf]" rates on v8).
3. 9 unclassified 33-windows (@265/@776/@1000/@1149/@1421/@1502/@1504/
   @1642/@1700) — class silence, not counterevidence.
4. Red-team adjudication of this package (recommendation, not a merge).
