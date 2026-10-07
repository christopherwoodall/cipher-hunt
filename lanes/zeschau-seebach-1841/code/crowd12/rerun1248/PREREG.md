# PREREG — @1248 P-C RE-RUN (round 12, work order 6)

Timestamp: 2026-10-07 ~16:25 CDT. Worker: 1248-RE-RUN executor.
Preregistered BEFORE any Guizot-DIP content was examined for this work order.
(No Guizot-DIP content read for WO6; corpus presence confirmed by byte size only.)

## Standing frame (from the record — F81, not new data)

- "peu" arm: STRENGTHENED 4/8 (P-A: 13/13 genuine "pour peu que"+subjunctive,
  11× RDM-1841 + 2× Guizot-DIP; P-B: shape S=(verb-offset 3, clause-length 4)
  matches the cipher clause; P-D FAIL, P-C no leg — sole v8 "X peu que" was
  comparative-adverbial "aussi", 06-incompatible).
- Infinitive-class "empêcher" arm: WEAK-FENCED 3/7 (E-A PASS: 28 distinct
  genuine infinitives; E-B FAIL, E-C FAIL).
- Sharpest gap: the double-pour stack "pour 33 16 pour 67 que" has NO era
  license in ~16.5MB (P-D and E-C both zero).
- **LABEL CORRECTION (R7/F81):** the 11-token frame is pairs[1244:1255],
  NOT "@1244–1256". Cipher-side verified byte-exact on the repaired
  1,847-pair parse (2026-10-07): pairs[1244:1255] =
  `00 33 16 00 67 46 26 30 06 65 46`; @470–473 = `06 67 46 84`;
  pre(06@470) = 80 @469 (so ISLET-3 "06='ent' iff pre=82" does NOT cover
  @471 — the live 06 reading there is verb-stem-class provisional, or
  unidentified).
- @1248 NEITHER-fence STANDS. Do not re-litigate round-11's fences
  (cela, médiatrice-class, 48="ne", H_verb, the three mergers, retired
  WO-6 bar, settled round-11 fences @1519/@1372/@902, 48's three fences).
- The red team adjudicates; this worker RECOMMENDS only.

## Task

(a) Hunt "[verb] peu que" hosts in Guizot-DIP
    (`code/side-period/corpus/guizot-memoires-t5-t6.txt`, Guizot's printed
    1840–42 despatches, ~2.0MB archive.org OCR) — pool-registered follow-up
    to round-11's unscored pool check, which found (unscored) "il (lui)
    importe peu que" and "se souciait peu que". Question: does Guizot-DIP
    license MORE verb hosts for the "peu" reading of @1248?
(b) The double-pour stack (pairs[1244:1255]) — license it or fence it
    explicitly, on an expanded era-French pool.

## Constraints honored

- Lane tokenizer verbatim (round-10/11 arm1248): lowercase, ’→', split
  letter'letter, `[a-zà-ÿ]+`. No manual-tiling bearing counts. Era French
  only: metternich-papiere (German) and levant-correspondence-1841-p3
  (English) and allgemeine-zeitung (German) and ADB-Zeschau (German)
  are EXCLUDED. v8 phrase counts: v8 OCR word-splits are VOID per F77 —
  v8 zeros carry no fence weight; v8 hits count only if the frame is
  unambiguous; the DP-1 fence rests on the non-v8 pool.

## New legs

### PC-1 — Guizot-DIP "[verb] peu que" host census (attestation kind)

Corpus: Guizot-DIP only (the WO-named corpus; diplomatic register —
the closest register match to the target despatch).

Method: exhaustive — every token position i with t[i]=='peu' and
t[i+1]=='que'; X = t[i-1]; context ±20 tokens; constituency-read EVERY
hit (no sampling).

- Genuine verb host: "peu que" governed by a verb-headed construction
  whose head verb is X or the head of X's phrase, with the que-clause as
  its complement/subject clause. Elided forms (n'→n, m'→m, etc.) read
  through the tokenizer.
- EXCLUDED (recorded for completeness, not verb hosts): comparative-
  adverbial hosts ("aussi/si/trop/plus/moins/autant peu que"), noun hosts
  ("le peu que"), sentence-boundary artefacts, OCR-suspect frames counted
  only if the "X peu que" frame itself is unambiguous.
- Known baseline (pool-registered, round-11 unscored — do NOT count toward
  the bar): "il lui importe peu que" (lemma: importer), "se souciait peu
  que" (lemma: se soucier).
- PASS → NEW LEG iff ≥1 genuine verb host with lemma ∉ {importer,
  se soucier} (distinct-lemma bar — inflections of the two known verbs do
  not re-count). → recommendation: peu arm gains an attestation-breadth
  leg in the diplomatic register; @471 ("06 peu que 84") hostability
  broadened in Guizot's own despatch idiom.
- FAIL → no leg. The two known hosts stand as the construction's
  diplomatic-register attestation. NOT adverse-grade: absence of further
  hosts ≠ ungrammaticality (the construction is textbook and
  primary-attested).
- 06-slot compatibility: DESCRIPTIVE ONLY, not a bar. For each host verb,
  record its form and assess against 06's live readings at @471
  (pre=80: verb-stem-class provisional; ISLET-3 "-ent" inapplicable since
  pre≠82). If no host is form-compatible with any live 06 reading, that
  is a fenced tension, not an adverse.

### DP-1 — double-pour stack license (structural kind)

Pool (era French; primary tier): RDM-1841 q1–q4 (~15.1MB), Guizot-DIP
(~2.0MB), nesselrode v7/v8/v9/v10 (~2.2MB diplomatic correspondence),
pozzo-di-borgo-correspondance v1 (~1.0MB). Secondary tier (reported
separately): guizot-memoires t1–t3 gutenberg (~2.6MB, era French memoir
register).

Strict patterns (round-11 P-D/E-C definitions, UNCHANGED):
- DP-peu: "pour W1 W2 pour peu que" (W1, W2 any two tokens)
- DP-inf: "pour W1 W2 pour INF que" (INF = lane is_inf heuristic:
  endswith er/ir/re, len>3)

Constituency-read every hit. Genuine = stacked purpose: "pour [phrase]
pour [peu/INF] que [clause]" inside one sentence (purpose phrase +
concessive/purpose locution); sentence-boundary artefacts excluded;
OCR-suspect frames counted only if the double-pour frame is unambiguous.

- PASS iff ≥1 genuine strict hit in either sub-pattern (either tier —
  tier reported) → NEW LEG: licenses the double-pour frame; arm
  attribution per which sub-pattern fired (DP-peu → peu arm; DP-inf →
  infinitive-class arm).
- FAIL (zero genuine in the expanded pool) → EXPLICIT FENCE:
  "double-pour stack pairs[1244:1255] UNLICENSED — zero genuine in ~20.4MB
  primary + ~2.6MB secondary era French across 11 corpora; fence stands
  for both arms; recorded as frame-unattested (NOT ungrammaticality
  evidence against either arm)". The fence rests on the non-v8 pool per
  the v8-OCR-void constraint; v8 counts reported separately with the
  void caveat.
- Secondary scan (DESCRIPTIVE ONLY, not a leg): k≠2 stack depths —
  "pour W1..Wk pour peu que" / "pour W1..Wk pour INF que", k∈{1,3,4,5} —
  to learn whether the stacked-pour family exists at other depths
  (sampling gap at k=2) or is wholly unattested.

## Verdict rule (pre-registered)

- PC-1 PASS → recommend NEW LEG for the peu arm (attestation-breadth,
  Guizot-DIP diplomatic register). Arm arithmetic for the red team:
  peu 4/8 → 5/9 (base legs unchanged; P-A/P-B stand as adjudicated).
- PC-1 FAIL → no change; the two known hosts stay pool-registered but
  unscored (they were never legs).
- DP-1 PASS → recommend NEW LEG (structural license), arm per sub-pattern.
- DP-1 FAIL → recommend EXPLICIT FENCE (double-pour stack unlicensed),
  both arms; the @1248 NEITHER-fence stands.
- No adverse bar is registered: a zero is a fence, not an adverse —
  neither arm's standing legs are contradicted by non-attestation.
- The @1248 NEITHER-fence stands regardless of this re-run's outcome:
  neither arm promotes on WO6 alone (single-work-order bar; lane ≥2-check
  rule for promotions).

## Outputs

- `code/crowd12/rerun1248/PREREG.md` (this file)
- `code/crowd12/rerun1248/rerun1248.py` (implements this prereg)
- `code/crowd12/rerun1248/rerun1248_raw.json` (all hit contexts)
- `code/crowd12/rerun1248/rerun1248_results.json` (adjudication)
- `code/crowd12/report_inbox/rerun1248-peu.md` (per REPORTING.md)
- Final report to parent: per-question findings + recommendations.
