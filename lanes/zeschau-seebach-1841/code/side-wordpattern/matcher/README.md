# matcher/ — Seebach word-pattern matcher (pattern-matcher worker, 2026-10-07)

## What it does
Segments the cipher pair stream into words from the segmenter's STRUCT
boundary probabilities (`code/crowd3/segmenter_results.json`), computes each
word's group-repetition pattern, looks up `(n_syllables, pattern)` in the
French pattern lexicon (`../lexicon/`, orth + phonetic), filters by anchor
consistency across 4 tiers (T0 GT → T3 all), ranks by era frequency.

## Files
- `matcher.py` — the instrument (stdlib only). Run: `python3 matcher.py`
- `match_results.json` — full per-word results (tiers, survivors, proposals,
  leads, nulls, anchor evidence, polyvalence flags)

## Anchor statuses used
GT: 11=la 70=pre 82=m 34=i 29=er 40=e 46=que ·
PROV-STRONG: 87=ce 64=qui 96=par 94=ne ·
PROV: 67=veut (06=verb-stem class: unusable as syllable anchor) ·
LEAD: 62=on 78=me 52=pas 24=en.
Polyvalent groups flagged: 06, 94, 52.

## By-ear variants implemented (all 4 spec'd + inventory notes)
V-orth, V-phon, V-orth-entdrop, V-phon-entdrop, V-orth-iersplit,
V-phon-iersplit, V-phon-finalmerge, V-orth-finalmerge.
Interior schwa kept/dropped is already covered by orth-vs-phon
(`phon_syllable` drops schwa: petit→p|tit). No CV-split variant exists:
ground-truth "première" is written pre|m|i|er|e (5 groups) vs lexicon
pre|mi|è|re (4) — unmatchable by (n,pattern); recorded as instrument limit.

## Verdict (see report_inbox/pattern-matcher-proposals.md)
HONEST NULL — no crib proposal promoted. Ground-truth control fails:
the "première" tail @1035–1038 (82-34-29-40, four GT anchors) returns zero
candidates at every tier — the encipherer's by-ear units (m, i as standalone
syllables) are absent from the lexicon's syllable inventory ('m' occurs as a
syllable in exactly 1 of 11,870 entries). All "unique survivor" hits are
hapax accidents (freq 1–5), register pollution ("susquehanna"), or echoes of
a single provisional anchor ("quiconque" ×7 from 64=qui alone); zero have ≥2
GT anchors; the set is unstable under the 0.5→0.7 cut (4/11 survive).
All would-be proposals stamped PROVISIONAL-PENDING-POLYVALENCE-VERDICT
(tester verdict not yet landed).
