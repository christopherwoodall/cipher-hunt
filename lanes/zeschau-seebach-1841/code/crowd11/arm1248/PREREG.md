# PREREG — @1248 ARM STRENGTHENER (round 11, work order 5)

Timestamp: 2026-10-07 ~16:05 CDT. Worker: arm1248 (strengthener).
Preregistered BEFORE any new-corpus data was examined for this work order.
(File sizes listed to confirm corpus presence only; no content read.)

## Standing frame (from the record — F73, not new data)

- @1248 NEITHER-fence STANDS. Two WEAK fenced arms: "peu" 2/4 (L2+L3;
  L1 FAIL hapax, L4 INDETERMINATE) and infinitive-class "empêcher" 2/4
  (L2+L3; L1 FAIL singleton, L4 INDETERMINATE).
- "cela" REFUTED on substance — no re-litigation. Médiatrice-class DEAD —
  no re-litigation. Gate-4 REVISED bound: {peu}-class + infinitive only.
- Any @1248-scoped reading is n_eff=1 (00->67 singleton @1248).
- 62-WO3 blocker REFUTED for @1248 (zero group-62 in ±6) — not re-tested.

## Task

Strengthen the two weak arms with GENUINELY NEW legs (new era attestations,
new structural arguments, new window interactions), or leave them fenced
with an honest missing-leg inventory. No re-running of round-10 legs.

## New-corpus pool (attestation-kind legs only — NOT rate bars)

Constraint honored: rate bars stay Nesselrode-v8-only. Every leg below is
pre-registered as ATTESTATION-kind (≥1 genuine hit, constituency-read) or
STRUCTURAL/WINDOW-kind. None is a rate bar.

- **RDM-1841**: revue-deux-mondes-1841-q1..q4.txt (Paris, Jan–Dec 1841,
  ~12.3 MB, Internet Archive OCR). Register: formal 1841 prose
  (literary/political) — same year as the despatch; the constructions at
  issue ("pour peu que", "pour INF que") are pan-register formal-French
  grammar, not genre-bound. Executor register assessment; flagged for
  frenchman review (I do not claim his authority).
- **Guizot-DIP**: guizot-memoires-t5-t6.txt (Mémoires t.5–6, 1858–67;
  printed foreign-minister despatches/instructions Oct 1840–42, ~2.0 MB,
  archive.org OCR). Register: diplomatic despatches — closest register
  match to the target despatch. CAVEAT pre-registered: OCR noise; every
  hit constituency-read, OCR-suspect hits marked PROVISIONAL and counted
  only if the "pour [X] que" frame itself is unambiguous.
- v8 (nesselrode-v8.txt) reused ONLY where pre-registered below (E-B, P-C,
  and as one member of E-C's pool).

Tokenizer: lane tokenizer verbatim (lowercase, "'" splitting,
`[a-zà-ÿ]+`), same as round 10. No manual-tiling bearing counts.

## New legs — "peu" arm (base 2/4: L2 era-constituency, L3 cipher-contact)

**P-A — second-corpus attestation of "pour peu que".**
Search pool {RDM-1841, Guizot-DIP} for "pour peu que". Constituency
standard (same as round-10 L2): the hit must parse as the concessive
locution governing a subjunctive clause; clause-boundary artefacts
excluded; OCR-suspect hits provisional (count iff frame unambiguous).
- PASS → NEW LEG (attestation-breadth kind): arm no longer hapax-anchored.
- FAIL (zero genuine) → no leg; report notes the hapax concern deepens
  (NOT adverse-grade: absence ≠ ungrammaticality; the construction is
  textbook and primary-attested).

**P-B — construction-shape stability (structural kind).**
Known exemplar (primary, round-10): "pour peu que l'hiver soit rigoureux"
→ verb offset from "que" = 3 (l=1, hiver=2, soit=3); clause length
(que-exclusive, words) = 4. Cipher clause: 46@1249 "que", content
26-30-06-65, closed by 46@1254 → verb-morphology group 06 at offset 3,
clause length 4 groups.
- Pre-registered shape S = (verb-offset 3, clause-length 4).
- Among P-A's NEW "pour peu que" hits: PASS iff ≥1 hit has verb-offset 3
  AND clause-length 4 (constituency-read) → the construction has a stable
  era shape and the cipher clause matches it → NEW LEG.
- If P-A yields zero new hits → UNSCORABLE (not fail).
- If new hits exist but none matches S → FAIL (shape not stable; the
  cipher's 4-group/offset-3 match to the single primary exemplar is
  then coincidence-grade).
- Bears on round-10 L4's open question (subjunctive host); does NOT
  retro-score L4. Caveat: 06's verb-identity is itself fenced/provisional
  (06-islet n_eff=3); this leg licenses the position/shape, not the mood.

**P-C — @471 cross-window hostability (window-interaction, discriminating
both ways).**
Second 67→46 window: @470-473 = 06-67-46-84. Under "peu": "06 peu que 84"
needs an era host ("[X] peu que" with X verb-compatible).
- v8 search: all "X peu que" (X any word), constituency-read each.
- PASS (supporting) iff ≥1 genuine host AND compatible with 06's standing
  readings (verb-final "-ent" per fenced 06-islet, or verb-stem per
  round-10) → NEW LEG.
- ADVERSE iff zero genuine "[X] peu que" hosts in v8 at all → the second
  67→46 window is unhostable under "peu" (recorded against the arm).
- Note: "importe peu que" is the canonical candidate host; the test is
  whether v8 actually instantiates any "[verb] peu que".

**P-D — stacked-pour license for peu (structural kind).**
Cipher stack @1244–1248: "pour 33 16 pour peu que". Pool {v8, RDM-1841,
Guizot-DIP}: regex "pour W1 W2 pour peu que" (W1 W2 any two words),
constituency-read (genuine = purpose phrase + concessive locution;
sentence-boundary artefacts excluded).
- PASS iff ≥1 genuine → NEW LEG (licenses the double-pour frame).
- FAIL → no leg.

## New legs — infinitive-class "empêcher" arm (base 2/4: L2, L3)

**E-A — class breadth in new corpus (attestation kind).**
Pool {RDM-1841, Guizot-DIP}: "pour INF que" middles (INF = lane heuristic
-er/-ir/-re, len>3), constituency-read each (genuine = purpose infinitive
+ que-clause; boundary artefacts excluded).
- PASS iff ≥2 DISTINCT infinitives attested (lemmas; empêcher may be one)
  → NEW LEG: the class is no longer singleton-anchored. Directly attacks
  round-10 L1's failure mode with new-corpus breadth (attestation-kind,
  not a rate bar — the v8 L1 bar stays failed).
- FAIL → no leg.

**E-B — @471 modal+infinitive unification (window-interaction kind).**
@470-473 = 06-67-46-84. Under infinitive-class: "06 empêcher que 84" =
modal/auxiliary + "empêcher" + que-clause ("veut/peut/doit empêcher que").
- v8 regex (case-insensitive, constituency-read):
  MODAL ∈ {vouloir: veut/veulent/voulait/voulaient/voudrait/voudraient/veux,
  pouvoir: peut/peuvent/pouvait/pouvaient/pourrait/pourraient/peux,
  devoir: doit/doivent/devait/devaient/devrait/devraient/dois,
  falloir: faut/fallait/faudrait} + "empêcher que".
- PASS iff ≥1 genuine (modal + infinitive "empêcher" + que-clause) → NEW
  LEG: the second 67→46 window is hostable under the infinitive-class
  arm (unlike cela, which died at @471).
- Cipher-side 06 modal-compatibility: DESCRIPTIVE ONLY (no bar) — report
  06's positional profile; 06's standing readings are verb-morphology
  ("-ent" final / verb-stem), so no a-priori contradiction; note
  explicitly that 06's value is unidentified.
- FAIL → no leg.

**E-C — stacked-pour license for empêcher (structural kind).**
Cipher stack @1244–1248: "pour 33 16 pour empêcher que". Pool {v8,
RDM-1841, Guizot-DIP}: regex "pour W1 W2 pour INF que" (INF = -er/-ir/-re
heuristic), constituency-read (genuine stacked purpose: "pour [phrase]
pour [INF] que [clause]"; sentence-boundary artefacts excluded).
- PASS iff ≥1 genuine → NEW LEG (licenses "pour 33 16 pour empêcher que").
- FAIL → no leg. (L4's agent-subject gap — matrix subject before @1244 —
  remains open regardless; inventoried as missing.)

## Verdict rule (pre-registered)

Per arm, counting ONLY the new legs above (base legs stand as adjudicated):
- **STRENGTHENED**: ≥2 new legs PASS and zero ADVERSE → arm banked
  stronger at the new total; report the new legs and what they license.
- **WEAK-FENCED (unchanged)**: exactly 1 new leg PASS, zero adverse →
  stays fenced; missing-leg inventory updated.
- **FENCED-ADVERSE**: ≥1 new leg ADVERSE (only P-C can fire adverse) →
  arm fenced with the adverse on record (arm weakened, not strengthened).
- **NULL**: 0 new PASS, 0 adverse → fenced; full missing-leg inventory.

No new leg may re-score round-10 L1–L4. P-B may be cited as bearing on
L4's open question, nothing more.

## Outputs

- `code/crowd11/arm1248/arm1248_strengthen.py` (implements this prereg)
- `code/crowd11/arm1248/arm1248_strengthen_results.json`
- `code/crowd11/report_inbox/arm1248-strengthen.md` (per REPORTING.md)
- Final report to parent: per-arm verdicts + missing-leg inventory.
