# Annealer results — zeschau-seebach-1841 (2026-10-07)

Simulated annealing over the full 96-group → syllable assignment, 8 anchors pinned, scored by a French syllable-bigram model.

## Method
- Model: syllable unigrams/bigrams from Tocqueville *De la démocratie en Amérique* T1 (1835) + T2 (1840), Gutenberg 30513/30514; rule-based orthographic French syllabifier (maximal-onset); Laplace α=0.05.
- Era/register: 1835–1840 formal political prose — the closest available match to 1841 diplomatic French. Les Mis (1862, literary) used ONLY as the synthetic-control plaintext, keeping training and control independent.
- Inventory: top-400 syllable types + 26 single letters (413 units); token coverage of reference 0.8893.
- Annealing: 24 restarts × 60000 iters, geometric T 2.0→0.01; move = reassign one free group (uniform or frequency-weighted proposal); delta-scored; best-key-per-restart retained. Anchors pinned: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que, 87=ce.

## Real ciphertext
- Pair/group counts re-verified: 1846 pairs, 96 groups.
- Random-key baseline (anchors pinned, 300 draws): -7.6304 ± 0.2401 per-pair logp.
- Best restart: -3.3716 per-pair logp (z = +17.7 vs baseline).
- Per-restart best scores: -3.834, -3.884, -3.880, -3.656, -3.524, -3.557, -3.759, -3.654, -3.771, -3.673, -3.899, -3.749, -3.754, -3.372, -3.677, -3.645, -3.756, -3.419, -3.691, -3.629, -3.728, -3.815, -3.726, -3.863

## Stability table (modal assignment across restarts, free groups only)
| group | modal syllable | recurrence | runner-ups |
|---|---|---|---|
| 06 | de | 24/24 | — |
| 16 | de | 24/24 | — |
| 24 | de | 24/24 | — |
| 38 | de | 24/24 | — |
| 48 | de | 24/24 | — |
| 50 | de | 24/24 | — |
| 91 | de | 24/24 | — |
| 94 | de | 24/24 | — |
| 96 | de | 24/24 | — |
| 98 | de | 24/24 | — |
| 01 | de | 23/24 | re×1 |
| 14 | de | 23/24 | la×1 |
| 44 | de | 23/24 | re×1 |
| 63 | de | 23/24 | la×1 |
| 17 | de | 22/24 | le×1, la×1 |
| 64 | de | 22/24 | la×2 |
| 74 | de | 22/24 | me×1, la×1 |
| 33 | de | 21/24 | la×2, le×1 |
| 42 | la | 21/24 | re×3 |
| 43 | de | 21/24 | la×2, le×1 |
| 88 | de | 21/24 | la×2, re×1 |
| 49 | la | 20/24 | de×2, le×1, gran×1 |
| 52 | de | 20/24 | la×4 |
| 58 | de | 20/24 | la×4 |
| 78 | de | 20/24 | la×3, re×1 |
| 79 | de | 20/24 | la×4 |
| 95 | le | 20/24 | te×4 |
| 04 | de | 19/24 | la×3, ter×1, re×1 |
| 09 | de | 19/24 | re×3, la×2 |
| 19 | la | 19/24 | re×4, de×1 |
| 26 | de | 19/24 | la×5 |
| 30 | la | 19/24 | re×3, de×2 |
| 32 | la | 19/24 | gran×3, re×2 |
| 36 | de | 19/24 | la×5 |
| 47 | la | 19/24 | de×4, re×1 |
| 56 | de | 19/24 | la×5 |
| 76 | de | 19/24 | la×5 |
| 85 | la | 19/24 | de×5 |
| 90 | de | 19/24 | guer×3, ter×1, tion×1 |
| 92 | de | 19/24 | la×3, le×1, re×1 |
| 93 | de | 19/24 | la×3, re×2 |
| 41 | de | 18/24 | re×3, la×3 |
| 51 | de | 18/24 | la×4, re×2 |
| 59 | de | 18/24 | la×5, re×1 |
| 80 | la | 18/24 | de×6 |
| 99 | la | 18/24 | de×2, ment×1, mo×1 |
| 02 | la | 17/24 | de×5, le×1, re×1 |
| 10 | de | 17/24 | la×7 |
| 21 | de | 17/24 | la×7 |
| 37 | la | 17/24 | re×4, de×3 |
| 45 | la | 17/24 | re×4, de×3 |
| 53 | de | 17/24 | la×4, re×3 |
| 81 | de | 17/24 | la×7 |
| 83 | la | 17/24 | de×7 |
| 03 | de | 16/24 | le×7, la×1 |
| 07 | la | 16/24 | de×8 |
| 12 | la | 16/24 | de×3, gran×2, le×2 |
| 15 | la | 16/24 | re×5, de×2, gran×1 |
| 22 | de | 16/24 | la×6, le×2 |
| 35 | la | 16/24 | de×6, re×2 |
| 60 | la | 16/24 | de×7, re×1 |
| 65 | la | 16/24 | re×4, le×2, de×2 |
| 73 | de | 16/24 | ses×2, la×2, ment×2 |
| 08 | de | 15/24 | le×5, la×3, re×1 |
| 54 | re | 15/24 | de×7, la×2 |
| 68 | de | 15/24 | re×7, la×2 |
| 20 | de | 14/24 | la×7, re×3 |
| 23 | de | 14/24 | re×6, la×2, et×1 |
| 62 | la | 14/24 | re×8, le×1, gran×1 |
| 28 | de | 13/24 | re×5, la×3, gran×2 |
| 31 | la | 13/24 | de×11 |
| 39 | la | 13/24 | de×8, ment×2, ce×1 |
| 55 | la | 13/24 | de×11 |
| 71 | re | 13/24 | la×7, de×3, gran×1 |
| 77 | la | 13/24 | de×10, re×1 |
| 18 | re | 12/24 | de×6, la×6 |
| 57 | la | 12/24 | gran×3, tion×3, ment×2 |
| 61 | re | 12/24 | de×8, la×4 |
| 69 | la | 12/24 | de×10, le×2 |
| 86 | de | 12/24 | le×5, la×4, re×3 |
| 00 | la | 11/24 | re×8, de×5 |
| 13 | de | 11/24 | re×7, gran×2, ment×2 |
| 27 | quel | 11/24 | pres×6, cha×5, ti×1 |
| 66 | de | 11/24 | re×7, la×5, le×1 |
| 67 | de | 11/24 | la×7, re×6 |
| 89 | de | 11/24 | la×11, et×1, re×1 |
| 97 | de | 11/24 | la×6, re×6, le×1 |
| 84 | de | 9/24 | la×8, le×4, re×3 |

Groups with recurrence ≥12/24: 06=de(24), 16=de(24), 24=de(24), 38=de(24), 48=de(24), 50=de(24), 91=de(24), 94=de(24), 96=de(24), 98=de(24), 01=de(23), 14=de(23), 44=de(23), 63=de(23), 17=de(22), 64=de(22), 74=de(22), 33=de(21), 42=la(21), 43=de(21), 88=de(21), 49=la(20), 52=de(20), 58=de(20), 78=de(20), 79=de(20), 95=le(20), 04=de(19), 09=de(19), 19=la(19), 26=de(19), 30=la(19), 32=la(19), 36=de(19), 47=la(19), 56=de(19), 76=de(19), 85=la(19), 90=de(19), 92=de(19), 93=de(19), 41=de(18), 51=de(18), 59=de(18), 80=la(18), 99=la(18), 02=la(17), 10=de(17), 21=de(17), 37=la(17), 45=la(17), 53=de(17), 81=de(17), 83=la(17), 03=de(16), 07=la(16), 12=la(16), 15=la(16), 22=de(16), 35=la(16), 60=la(16), 65=la(16), 73=de(16), 08=de(15), 54=re(15), 68=de(15), 20=de(14), 23=de(14), 62=la(14), 28=de(13), 31=la(13), 39=la(13), 55=la(13), 71=re(13), 77=la(13), 18=re(12), 57=la(12), 61=re(12), 69=la(12), 86=de(12)

## Synthetic control
- Plaintext: Les Misérables T1 syllabified; 96-group planted syllabary (anchor groups pinned to true values, 88 others → random top-frequency syllables).
- Control baseline: -7.5969 ± 0.2845; best control restart: -2.8981 (z = +16.5).
- Recovery of planted assignment (modal vote, 88 present non-anchor groups): **1/88 = 1.1%**.
- Recovery by single best restart: 1/88 = 1.1%.

## Verdict
- Control: method FAILS to recover the planted syllabary → method is UNINFORMATIVE on this problem class; real-ciphertext results are a NULL (N-series), not a break. Do not promote any real assignment.

## Caveats / next
- Syllabifier is rule-based orthographic, not phonetic; the 1841 syllabary's own segmentation may differ (e.g. mute-e handling, digraph splits).
- Homophony is one-directional in the model (many groups → one syllable); the true key may also map one group to multi-syllable strings — not modelled.
- If control recovers: next = inspect stable real assignments for French word formation around anchor windows; try seeded restarts from the modal key with a word-level French scorer.
- If control fails: next = different move set (pair-swap moves), trigram syllable model, or accept that 8-anchor sparsity is below the method's resolution and stand down (null).
