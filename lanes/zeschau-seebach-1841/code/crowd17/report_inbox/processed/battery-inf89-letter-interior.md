# Battery `inf89-letter-interior` — verdict: NULL (letter route fenced as exhausted)

**Target:** census 89's 14 windows for letter-tier neighbors that could sit
word-internal to the "[89]e" word.

## Bar (verbatim, pre-registered)

> "name >=1 interior letter of 89's word with byte evidence, or fence the
> letter route as exhausted"

Restated: **C1** (an interior letter of 89's word is named with byte evidence
at battery grade → promote) / **C2** (else the letter route is fenced as
exhausted with stated cause → null).

Adverses: none listed.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(asserts held: 1847 pairs, 96 types). `canonical.py` never used.
Letter-tier premise set (banked): 12='n', 34='i', 40='e', 82='m', 48='e',
29='er'. Censused all 14 89-windows (0-based, row-validated) for letter-tier
predecessors and successors. Standing premises adopted, not re-litigated:
48='e' word-final of "[89]e" (`conj-20-642-subordinator` NULL, locus @641
byte-confirmed "…77(le) 89 48(e) 20…"); 77='le' provisional; 67 et/veut sole
polyvalence (§7); 89 has no polyvalence declaration (one word per cell);
A8 89 verb-frame grant, value open.

## 89 windows (14, byte-exact)

| @ | row | context |
|---|-----|---------|
| 113 | a1_03 | 93 29 **89** 68 21 |
| 222 | a2_01 | 16 24 **89** 61 96 |
| 275 | a2_03 | 33 29 **89** 84 91 |
| 285 | a2_03 | 48 52 **89** 28 00 |
| 303 | a2_04 | 91 18 **89** 88 02 |
| 640 | a4_01 | 67 77 **89** 48 20 |
| 781 | a5_04 | 08 29 **89** 11 24 |
| 871 | a5_07 | 87 77 **89** 48 20 |
| 986 | a6_01 | 01 24 **89** 48 01 |
| 1082 | a6_05 | 06 52 **89** 24 02 |
| 1377 | a7_06 | 86 29 **89** 84 92 |
| 1393 | a7_07 | 86 29 **89** 16 76 |
| 1498 | a7_11 | 59 24 **89** 41 74 |
| 1752 | a8_08 | 07 28 **89** 26 24 |

## Letter-tier adjacency census

- **pre=29('er') ×5**: @113, @275, @781, @1377, @1393 ("29 89" bigram x5
  stream-wide, 0-based 89 at 113/275/781/1377/1393).
- **fol=48('e') ×3**: @640, @871, @986 ("89 48" bigram x3; "77 89 48"
  x2 @640/@871; the third is "24 89 48" @986).
- **12/34/40/82: zero adjacency to 89 anywhere** (all 14 windows checked).

## Per-clause results

### C1 — interior-letter candidates (all fail)

**Candidate A: 48='e' as interior.** 48 is the adopted word-FINAL 'e' of
"[89]e" (battery-grade locus @641; conj-20-642-subordinator C1). For 48 to be
interior, the word would have to extend past 48 ("[89]e…"), but 20's class at
@642 is post-nominal adjective and no license exists for an "e[20]" fusion;
inverting the adopted finality would re-litigate a standing battery finding.
Out.

**Candidate B: 29='er' as interior.** 29 precedes 89 ×5 but the trigram
"29 89 48" is 0× stream-wide — 29 never co-occurs with the "[89]e" final.
Where "[89]e" is attested (@640/@871), 89 is forced word-initial: the
immediate predecessor is 77 ('le', free word under the provisional grant) or
24 (finite/modal under R24). Making 29 interior would require the word
"er[89]e"-shaped at windows whose actual predecessor is 77/24, i.e. a second
89-word — barred by §7 (89 has no polyvalence declaration; 67 remains sole).
In the five "29 89" windows, 29 reads as the '-er' ending on the preceding
verb cell ("[X]er" + word-initial "[89]e"), not as 89's interior. Out.

**Candidate C: 12/34/40/82 as interior.** Zero adjacency to 89 at any window.
Out.

**Value route:** 89's own value is unvalued (A8 frame grant only). The
interior content of "[89]e" is 89 itself + 48-final; nothing letter-tier can
be spelled from within at battery grade.

→ **C1 FAIL. C2 FIRES:** the letter route is fenced as exhausted, with the
stated cause above.

## Verdict rationale

No interior letter is nameable with byte evidence: the only letter-tier
neighbors are 48 (word-final, adopted) and 29 (never co-present with the final,
§7-barred as interior). This is not kill grade — no window forces a standing
claim false; the route is fenced, not killed. §7 intact; no standing/red-team
verdict contradicted or downgraded; canonical-stream caveat stands (rows
unvalidated except the pencil-gloss row).

## Follow-ups proposed (for supervisor queuing)

1. `inf89-er89-boundary` (P3) — decide the word boundary in the five "29 89"
   windows: "[X]er [89]..." vs "[X]er[89]..." (one licensed word-form test per
   window); sharpens whether 29 could ever be interior-adjacent.
2. `word89e-right-bound` (P3) — test the "[89]e" right boundary at
   @640/@871/@986: confirm 48 word-final vs word-extending ("e[20]"-shaped);
   hardens the 48-interior kill arm from the other side.
3. `inf89-rerun-77gate` (P4) — gated re-fire once the red team adjudicates
   77's value: if 77 resolves non-'le', the word-initial forcing at @640/@871
   weakens and the 29-interior arm re-opens.

## Bookkeeping

- Stream: repaired 1,847-pair parse, asserts held; `canonical.py` never used.
- Lock: created on start (2026-10-09T12:50:37Z), deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
