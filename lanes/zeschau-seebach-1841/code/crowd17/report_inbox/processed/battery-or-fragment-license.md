# Battery `or-fragment-license` — verdict: PROMOTE

Follow-up from `battery-particle-20-value-rivals` NULL (2026-10-09).

## Bar (verbatim, pre-registered)

`>=3 genuine diplomatic attestations licenses 'or' at @760's fragment reading; confirmed zero across the diplomatic cut narrows the rival set`

Numbered clauses:
- **C1 (license arm):** ≥3 genuine diplomatic attestations of clause-initial argumentative "Or" after a verbless fragment → license 'or' at @760's fragment reading. PASS.
- **C2 (narrowing arm):** confirmed zero across the diplomatic cut → narrows the rival set. Does not fire (C1 fired).

## Method

- Diplomatic cut: the 9 lane-diplomatic files (levant-correspondence-1841-p3, metternich-papiere-v4, metternich-papiere-v6, pozzo-di-borgo-correspondance-v1, talleyrand-memoires-v1, guizot-memoires-t1/t2/t3-gutenberg, guizot-memoires-t5-t6) — 11,279,895 chars total.
- Clause splitter: same as parent battery — split on `[.;:!?…]+` or paragraph breaks only; single newlines are OCR line-wraps, not boundaries.
- Finite-verb detector: `finite_forms.FINITE2` (~4,250 forms) — same as parent.
- Found 135 clause-initial "Or" tokens; 22 with detector-verbless prev clause.
- **Hand-audited all 22.** The detector false-positives on elided forms ("l'a", "c'est", "s'établisse" tokenize whole and miss the finite stem) and on verbs outside its 150-verb list ("prescrivent", "tend", "faudrait", "rencontre", "était/comptais" via "C'était"); 12 of 22 excluded on hand-audit because the prev clause is in fact finite. 5 were OCR junk (English/German text, page numbers). Genuine/Fragment status below is the hand-audit call, not the detector's.
- Script: `code/crowd17/next-token/orfragment_census.py`; raw candidates: `orfragment_candidates.json`.
- `canonical.py` never used. R5005 untouched.

## Window-level evidence (corpus loci)

All three genuine attestations are clause-initial argumentative "Or" after a genuinely verbless French fragment, in diplomatic correspondence:

1. **metternich-papiere-v6.txt, clause 1862** — `mal connu qu'avec l'inconnu: or, le passé est connu, tandis que l'avenir ne l'est pas.` Prev is a verbless fragment; "or" follows a colon. GENUINE.
2. **metternich-papiere-v6.txt, clause 6111** — prev `Portugal; contre-balancer en Espagne l'influence française, et introduire dans la Péninsule le régime représentatif moderne.` (enumerative infinitive fragment); cur `Or, en voulant ces trois choses, il ne peut arriver qu'à un désordre sans fin.` GENUINE.
3. **metternich-papiere-v6.txt, clause 17165** — prev `sa rivale, en vertu d'un acte de la volonté du dernier Roi.` (enumerative NP fragment); cur `Or, comme dans un même pays il ne peut y avoir deux Rois investis des mêmes droits, et comme les protestations de Don Carlos avaient aussi peu [de prise]…` GENUINE.

Near-miss recorded, not counted: metternich-papiere-v4.txt clause 2370 (`reconcilier l'opinion de son pays… Or, il est certain que…`) — the infinitive fragment sits after OCR page-break junk ("88, … 686."), so its fragment status may be a page-split artifact; DOUBTFUL, excluded from the count.

## Per-clause pass/fail

- **C1 PASS** — exactly 3 genuine diplomatic attestations (≥3 bar met). The 'or'-after-verbless-fragment construction is licensed in diplomatic French.
- **C2** does not fire.

## Verdict: PROMOTE

The license claim holds at battery grade: 'or' after verbless fragments is attested in diplomatic 1841 prose (3 genuine instances).

**Scope caveat (headlined):** none of the three attestations has @760's exact left geometry — an ordinal-ellipsis-final clause ("…la première"). The parent's F2 census found mais=5 / or=0 in that exact frame, and this battery adds no 'or' there. So the general fragment license is PROMOTED, but 'or' at @760's specific ordinal-final geometry remains unattested; the 'mais'-at-@760 leg keeps its distributional edge.

## Adverses

None listed.

## Bookkeeping

- Queue: `or-fragment-license` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; re-validated from disk; own entry only; no downgrade).
- Lock created on start, deleted on completion. R5005, sealed gates, red-team adjudication queue untouched.
- No standing/red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands.
- No follow-ups required per §4 (promote).
