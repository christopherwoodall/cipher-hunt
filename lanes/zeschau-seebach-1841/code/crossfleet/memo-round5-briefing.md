# CROSS-FLEET MEMO — round-5 briefing: side-fleet intel the main fleet needs

Date: 2026-10-07 (overwatch audit)
From: overwatch coordinator
To: round-5 coordinator (via parent relay — check these are in the round-5 brief)

## 1. Petit-chiffre structural intel (key-hunt fleet) — NOT in NOTES.md/STATE.md
R5005's 96-group shape belongs to the documented French *petit-chiffre* tier
(~100-cell routine-correspondence class; cf. Petit Chiffre de la Grande Armée,
144 groups, transcribed at `code/side-keyhunt/tables/petit-chiffre-grande-armee.json`
— RULED OUT as the key, 0/7 anchors, stands as family reference only).
Structural priors for round 5:
- Sparse homophones on frequent syllables (a 1690 royal order *mandated*
  homophone use) — consistent with F33's conditioned polyvalence (3/25 groups).
- French tradition used nulls, but the petit-chiffre table has NONE —
  matches upstream's null-digit negative. Don't hunt nulls.
- Word-family packing: one group = an inflected family (supports 06/86
  complementary distribution as stem allomorphs, not separate syllables).
- Two-part tables (chiffrante/déchiffrante); grand/petit tiering was formal doctrine.
Full writeup: `code/side-keyhunt/tables.md`, verdict:
`code/side-keyhunt/verdict-petit-chiffre.md`.

## 2. Published-key negative (key-hunt fleet)
No published French diplomatic syllabary/code table of 1830–1848 exists in the
searchable literature (Kahn's French material is Rossignol-era; DECODE's own
R5005–R5008 records have empty Key: fields, verified live). Round 5 should NOT
spend effort on literature key-hunting — that channel is exhausted (search log:
`code/side-keyhunt/search-log.md`, 20 queries + 13 source checks).

## 3. Crib-learned inventory prescription (word-pattern fleet) — see F34
Standard-French syllable units are falsified for this cipher (ground-truth
"première" tail → zero lexicon hits). Any round-5 instrument that assumes
standard syllabification (legs, drags, scorers) must be rebuilt on a
crib-derived inventory. Reusable: the 11,870-word pattern lexicon
(`code/side-wordpattern/lexicon/`) and the polyvalence-expansion method with
red-team-amended restrictions R1–R8
(`code/side-wordpattern/redteam/ADJUDICATION.md`). Do NOT reuse: the 26 killed
proposals, or the tester's §6 K≥3 synthetic numbers (don't reproduce — regenerate).

## 4. Sidepath loop outputs (pre-parse-repair — caveat)
Skeleton at 30.66% stream coverage (`code/sidepath/skeleton.json`,
sha256 18d48ccd…9373f); canonical recounts n24=52, n52=27, n62=34
(supersede older 42/13/32 — BUT these are pre-repair counts, re-verify on the
1,847-pair parse); "montrera" as 94="re" support (S=0.917, independent of the
main fleet); methodology lesson: future drags need ANCHOR-PRESERVING controls
(shuffling de-anchors windows → controls accept MORE than real).

## 5. Already in STATE.md — confirm absorbed
Parse repair F32 (1,847 pairs, REINDEX.md), qscore fix, external acquisition
ON HOLD, round-5 work orders 1–10.
