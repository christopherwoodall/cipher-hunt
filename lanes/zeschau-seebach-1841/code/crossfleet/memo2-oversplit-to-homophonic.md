# CROSS-FLEET MEMO 2 — over-splitting vs the solver's phonetic model

Date: 2026-10-07 (overwatch-2 audit)
From: overwatch coordinator (second deployment)
To: homophonic solver fleet (via parent relay)

## What
Round 6's Frenchman (code/crowd6/frenchman62/frenchman62_round6.md) established
that the cipher OVER-SPLITS relative to spoken syllables: "première" (2–3
spoken syllables) → 6 groups; "personne" (2) → 3 groups; 46=que writes /k/
separately before vowels. This voided two old 62="on" legs (the "il"-kill and
the merger corroboration).

## Gap
Your solver's phonetic projection layer assumes a mapping between groups and
phonetic units. If that mapping is calibrated to spoken-syllable granularity
(one group ≈ one spoken syllable), over-splitting breaks it: a single spoken
syllable may be written as 2+ groups, so the projection's unit inventory is
too coarse. Your log shows "143 values share a projected form" — check whether
the projection handles sub-syllabic splits (e.g., /k/ written separately).

## Why it matters
This is the same class of instrument-validity problem as the crib-inventory
memo you already adopted: if the phonetic model's units can't represent what
the encipherer actually wrote, the joint inference searches the wrong space.
The crib-learned inventory (which you adopted) gives you the right *units*;
this memo is about the *phonetic mapping* of those units.

## Suggested check
Take the ground-truth "première" (11-70-82-34-29-40 → la-pre-m-i-er-e, 6 groups
for ~2.5 spoken syllables) and verify your phonetic projection can represent
that exact splitting. If it can't, the projection needs a sub-syllabic tier
before the R5005 gate is reconsidered.
