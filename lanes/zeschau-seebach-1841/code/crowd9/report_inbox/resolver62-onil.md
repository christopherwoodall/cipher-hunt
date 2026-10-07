# 62-RESOLVER round 9 — N35 independent-cell on/il battery (WO3)

**Verdict: HOLD (outcome (c)).** No cell met its pre-registered bar. 62="on"
stays fenced STRONG LEAD; 62="il" stays DISFAVORED-STRONG (not killed).
The Mehemet-Ali / @1248 blocker is NOT lifted — the 62 resolution did not advance.

## Battery (pre-registered in `code/crowd9/resolver62/PREREG.md`, data-blind)
Repaired 1,847-pair stream; n62=35 re-derived and asserted in code.
Era: Nesselrode v8 only (92,594 tokens), frenchman tokenizer verbatim.
Exact two-sided binomial throughout. Bars: leg needs compatible(p≥0.10)
with one hypothesis AND incompatible(p<0.01) with the other; kill of "il"
needs ≥2 cells at p<0.005 vs H_il with p≥0.10 vs H_on.

| cell | cipher | era (v8) | E_on | E_il | p_two(on) | p_two(il) | verdict |
|---|---|---|---|---|---|---|---|
| C1 62→59 ("il est"/"on est") | 0/35 | on→est 18/560, il→est 126/1363 | 1.13 | 3.24 | 0.630 | 0.072 | NULL |
| C2 59→62 ("est-il"/*"est-on") | 0/27 | est→il 6/1233, est→on 0/1233 | 0.00 | 0.13 | 1.0 | 1.0 | NULL |
| C3 62-l'-59 \| 62-l' ("il l'est"/*"on l'est") | 0/1 (@1539→88) | on-l'-est 0/12, il-l'-est 1/12 | 0.00 | 0.08 | 1.0 | 1.0 | NULL |
| C4 62→l' (weak control) | 1/35 (@1539) | on→l' 12/560, il→l' 12/1363 | 0.75 | 0.31 | 0.531 | 0.266 | NULL |

- Overlap audit: zero shared pair positions across C1/C2/C3 windows. N35 clean.
- N22: no 29/82/34/40 cells. No ear, no L_A/L_B/62→94/62→48 recycling.
- Fences (all pre-registered): C1/C2/C3 conditional on 59="est" (provisional);
  C3 also on M_hom {93,8}="l'" (LEAD); C2 on hyphen-tokenization assumption.

## The discrimination gap, named precisely
1. **Cipher-side event starvation.** The sharpest anchored asymmetry is C1:
   E[62→59|"il"]=3.24 vs E[62→59|"on"]=1.13, but observed 0/35 cannot separate
   E≈1 from E≈3 at the bars (p_two_il=0.072 — a lean against "il", honestly
   below the 0.01 bar; not moved post-hoc).
2. **Era-side power.** The inversion cell is correctly signed ("est-il" 6× vs
   "est-on" 0× in v8) but E_il=0.13 over n59=27 — untestable at this corpus size.
3. **One l' window.** Only a single 62→l' window exists (@1539, followed by 88,
   not 59), so the "il l'est"/*"on l'est" trigram cannot be tested; era confirms
   the asymmetry direction ("il l'est" 1×, "on l'est" 0× in v8).
4. **The l'-cell does not otherwise discriminate.** The sole (93|8)→59 "l'est"
   window in the stream is the M_hom leg window itself (@101–103 = 94-93-59).

## One fenced n=1 observation (descriptive, NOT a leg)
PAIRS[100]=62, so @100–103 reads **62-94-93-59 = "[62] ne l'est"** (94="ne"
prov-strong, {93,8}="l'" LEAD, 59="est" provisional). Under 62="il" this is the
idiomatic "il ne l'est (pas)"; under 62="on", "on ne l'est" is ~absent from
formal prose. The discriminating datum (position 100's value) is new — the
101–103 window is M_hom's leg, re-entered for context only (N35: one datum,
two uses — the new use is independently licensed but n=1, so no leg).

## Descriptives
- D2: L_A (93|8)→62 predecessors @10/@944/@1323/@1685 = {18, 40, 80, 13} —
  none is 46="que"; no "que l'on" frame among the four (shares L_A windows).
- S1 (01-pool sensitivity): 62→01=0, {59,01}→62=0 — same nulls as the 59-only cells.

## For the red team to rule on
1. HOLD stands — no bar met for promotion (needs ≥2 new legs FOR "on": have 0)
   or for killing "il" (needs ≥2 cells at p<0.005 vs H_il: have 0). Confirm no
   status movement for either value.
2. The n=1 @100 "62 ne l'est" observation: admissible as a fenced lean, or
   excluded as M_hom-window recycling? (Worker's position: admissible-fenced,
   zero leg weight.)
3. C1's p_two_il=0.072: confirm it stays a sub-bar lean — no quiet upgrade.
4. Bank C1–C4 as tested-NULL (with their fences) so future batteries don't
   re-run them as if fresh; the gap components (1)–(3) above are the
   named targets for any future on/il attempt (bigger era slice for C2,
   more cipher events for C1/C3 — neither obtainable from this despatch alone).
5. Mehemet-Ali stays LEAD-weak; @1248 still needs its own ≥2-leg arm — the
   WO3 blocker is carried forward, not resolved.

Artifacts: `code/crowd9/resolver62/PREREG.md`, `battery.py`, `results.json`
(all numbers reproducible from the repaired stream + nesselrode-v8.txt).
