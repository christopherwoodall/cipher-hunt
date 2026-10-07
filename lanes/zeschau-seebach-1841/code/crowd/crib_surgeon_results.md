# Crib Surgeon — positional attack results (2026-10-07)

Executor: THE CRIB SURGEON. Lane: `zeschau-seebach-1841`. Pair stream via
`load_pairs` from `code/crib_attack.py` (no independent re-derivation).
Anchors used: 7 pencil cribs + provisional 87=ce (8th, lane-inferred).

## Verdict

The full "la première" sequence **11-70-82-34-29-40 occurs exactly once**,
at pair index **1033 of 1846 (56.0% through the text)** — mid-letter, not an
opening formula. Zero near-miss (single-group substitution/gap) variants
anywhere in the stream. 11-70 ("la pre") is likewise unique to this spot.
The occurrence sits inside a wider grammatical run:

```
... 64 96 43 87(ce) 01 03 29(er) 80 77 | 11 70 82 34 29 40 | 17 77 82(m) 63 11(la) 67 76 85 41 88 29(er) 40(e) ...
```

Decoded with 8 anchors:

```
... ????????ce????er???? | lapremiere | ????m??la??????????ereer???? ...
```

Positional reading: a mid-text back-reference ("la première [fois/lettre/dépêche]"),
consistent with diplomatic correspondence referencing an earlier dispatch. Not
an opening formula, not a date formula.

No 46=que within ±10 groups of the occurrence (checked: none at 1023–1049).

## Recurring formula (positional hard constraint)

The 5-group chain **64-96-43-87(ce)-01 recurs exactly twice**: at 341 and at
1024 (the latter abutting the crib). Continuations diverge:
- @341: `...64 96 43 87 01 | 06 70(pre) 12 94...` → 70-12 is itself a recurring
  "pre+X" word (3×: 347, 1117, 1546).
- @1024: `...64 96 43 87 01 | 03 29(er) 80 77 | la-première...`

Recorded as a repeated set phrase; no value assigned (needs ≥2 checks).

## Value hypotheses (none promoted to anchor; hypotheses only)

### H1: 24 = "est" — STRONG HYPOTHESIS (4 checks, 1 miss, 1 anomaly)
1. Frequency band: freq 52, **rank 1** — top-tier function word. PASS.
2. Bigram asymmetry: 24→87(ce) = 10/52 = **19.2%** vs base P(87)=32/1846=1.73%
   (11× enrichment). PASS.
3. Independent reference (Les Mis, hyphen/apostrophe-stripped tokenization):
   P(ce|est) = 133/1130 = **0.118**, within 2× of observed 0.192. PASS.
4. Elision grammar: 46(que)-24 occurs 3× (546, 953, 1691) = "qu'est"/"que c'est".
   PASS.
- MISS: 24-87-46 "est-ce que" = **0×** (same miss H2b tolerated for 87=ce).
- ANOMALY: 24-87-11 = 3× (73, 162, 828) reads "est cela" — ungrammatical as
  "est"; idiomatic as "c'est cela". But the "c'est"-as-one-group reading is
  refuted by rate: Les Mis P(ce|c'est)=0.026 and P(cela|c'est)=0.007 vs observed
  0.192 / 0.30. The anomaly is unresolved; "est" kept as the lean.
- Status: hypothesis, NOT an anchor. Needs era-corpus confirmation (defer to
  attempt-3 worker's era-matched corpus).

### H2: 77 = "pas" — HYPOTHESIS (3 checks, 1 caveat)
1. Frequency band: freq 44, rank 5 — "pas" is top-tier. PASS.
2. Ratio check (Les Mis word-level): ne/pas = 843/879 = **0.959** vs cipher
   06/77 = 46/44 = **1.045** (if 06="ne"; see H3). PASS.
3. Bigram: 06→77 = 6/46 = **13.0%** vs base P(77)=44/1846=2.4% (5×). PASS.
- CAVEAT: 67→77 = 6/37 = 16.2% is a second "ne"-like predecessor. Explainable as
  "n'ai/n'a pas"-class (67 = negated auxiliary), but 67 is unidentified —
  unverified, so the caveat stands.
- CONFLICT (recorded, unresolved): 77 also leads the r1 repeat
  77-78-94-82(m)-06 (×2, @1179/@1350), whose single-letter m looks
  proper-noun-like. 77-78 occurs 7× with 5 distinct followers, compatible with
  either reading.

### H3: 06 = "ne" — HYPOTHESIS (3 checks)
1. Frequency band: freq 46, rank 3. PASS.
2. Ratio: 06/77 = 1.045 vs Les Mis ne/pas = 0.959. PASS.
3. Bigram: 06→77 13.0% vs 2.4% base. PASS.
- Note: 06 also ends the r1 repeat and precedes 29(er) 5× ("n'er…"-class
  elision possible, unverified).

### H4: 64 is a top-tier word (rank 4, freq 46) heading the recurring
64-96-43-87(ce)-01 formula — NO value hypothesis (insufficient checks).
Recorded for the next worker.

## Null results (first-class)
- N-CS1: crib sequence 11-70-82-34-29-40: **1 occurrence** (@1033), **0**
  single-group-gap/substitution variants in the full 1846-pair stream.
- N-CS2: 11-70 ("la pre") occurs only @1033; 29-40 ("er e") occurs 9× but the
  @1037 hit is inside the crib.
- N-CS3: no 46=que within ±10 groups of the crib occurrence.
- N-CS4: 24-87-46 ("est-ce que") = 0× — a miss against H1("est"), tolerated
  under the same standard as H2b's identical miss.
- N-CS5: no second "première" (no 70-82-34-29-40 without leading 11).
- N-CS6: attempt-2 already owns 64="qui" — not duplicated here.

## Verification
Re-checked against `data/attempt1_results.json`: pairs=1846 ✓, distinct=96 ✓,
odd_digit_lines=28 ✓, offset1_lines=32 ✓, crib_freq {11:44, 70:15, 82:38, 34:10,
29:47, 40:21, 46:29} ✓, repeat counts (2 / 0) ✓. All numbers in this file
recomputed from the pair stream in this run.

## What I'd try next
1. Era-matched corpus (attempt-3 worker's build): re-run H1/H2/H3 rate checks
   against 1830s–40s diplomatic French — Les Mis is literary, not epistolary.
2. Resolve H1's "est cela" anomaly: test whether 24-87-11's 11 could be the
   pronoun (still "la") vs a distinct article use — needs denser anchors.
3. Resolve H2's caveat: identify 67 (candidate negated auxiliary) via its
   before/after profile (67→33 ×6, 67→77 ×6, 67→78 ×4; 21→67 ×8).
4. Value 64 (rank 4): its followers 77/96/29/59/37 — 64-96-43-87-01 is the
   entry point.
5. The 70-12 "pre+X" word (3×: 347, 1117, 1546) — candidate "prés…/pre…" family;
   contexts at 1117/1546 unexamined.
