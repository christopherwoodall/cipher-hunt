# Battery verdict: en85-gerund-reaudit

**Verdict: PROMOTE** — 4 of 5 "en [85]" legs confirm as gerund frames on the repaired stream; the A3 "en [85]" x5 count re-derives exactly.

## Bar (verbatim from battery-queue.json)

> (a) adjudicate @733's 'l'en'+finite-85 rival parse vs the gerund parse with banked values only; (b) adjudicate @1439's "m'[16] en [85]" shape; (c) confirm or correct the A3 'en [85]' x5 count on record. Promote iff >=4 of 5 legs confirm as gerund frames; null with corrected count otherwise.

Numbered clauses:
1. Adjudicate @733 ("l'en" + finite-85 rival vs gerund parse) using banked values only.
2. Adjudicate @1439 ("m'[16] en [85]") shape.
3. Confirm or correct the A3 "en [85]" x5 count.
4. Promote iff >= 4 of 5 legs confirm as gerund frames.

## Method

- Parsed the repaired 1,847-pair stream exactly per `code/side-keyhunt/repair_parse.py`
  (`repaired_offsets.json` + `data/upstream-ct_R5005.txt`; byte-exact
  `[digits[i:i+2] for i in range(o, len(digits)-1, 2)]`). Total 1847 pairs confirmed;
  crib "11 70 82 34 29 40" hits at 0-based 754 (a5_03) and 1034 (a6_03), matching
  repair_parse.py's asserts. `canonical.py` never touched.
- Census: every `24-85` bigram in the stream, with row ids and wide windows.
  Convention: @ = 0-based position of 85 (same convention as battery-stem-85's report).
- Banked values used (and only these): pencil 11=la, 82=m, 46=que; granted
  96=par, 87=ce; A3 ground truth 24=en. No value named for 85, 16, 26, 58, 88, 93,
  01, 52, or any other open group. 1841 diplomatic French throughout.
- "Confirm as a gerund frame" = the 24-85 bigram reads as gerund "en [85]" with
  no viable rival parse under banked values. A leg whose gerund parse needs an
  ungranted free assumption, or which admits a second grammatical parse, does
  not confirm.

## Census (bar clause 3)

Exactly **5** occurrences of the 24-85 bigram in the 1,847-pair stream — no more,
no fewer. The A3 "en [85]" x5 count is **confirmed**, not corrected.

| @ (85-pos) | row   | window (24 +/- 4)              |
|------------|-------|--------------------------------|
| @733       | a5_02 | 86-48-88-**11-24-85**-93-76-18 |
| @956       | a6_00 | 86-96-87-**46-24-85**-04-20-67 |
| @1439      | a7_08 | 64-52-82-**16-24-85**-01-52-68 |
| @1694      | a8_06 | 14-60-27-**46-24-85**-58-15-23 |
| @1755      | a8_08 | 07-28-89-**26-24-85**-58-17-78 |

(85's full predecessor census: 24 x5, 29 x3, 79 x2, 81/76/21/56/91 x1 — consistent
with stem-85's "que [85]er" x1 leg at the 46-29-85 window; no second 46-85 bigram exists.)

## Leg-by-leg adjudication

### @956 (a6_00): `96-87-46-24-85` — CONFIRM

"par (96) ce (87) que (46) en (24) [85]" = "par ce qu'en [85]". The 46-24
junction forces the "qu'en" elision; the gerund adjunct attaches to the
preceding main clause. No clitic ambiguity, no forced rival segmentation, no
banked value obstructs. Clean gerund frame.

### @1694 (a8_06): `46-24-85-58` — CONFIRM

"que (46) en (24) [85] [58]" = "qu'en [85] [58]". Elision forced; 58 open as the
gerund's complement (cf. ant-58-ending follow-up from stem-85, not assumed
here). No rival parse. Clean gerund frame.

### @1755 (a8_08): `26-24-85-58` — CONFIRM

"[26] en (24) [85] [58]". The gerund adjunct "en [85]" is recognizable with no
forced alternative; 26's openness leaves the host main clause unparsed but does
not obstruct or rival the frame. No banked value forces a non-gerund reading.
Clean gerund frame (matches stem-85's assessment).

### @1439 (a7_08): `82-16-24-85-01-52` — CONFIRM (bar clause 2)

"m' (82) [16] en (24) [85]". Adjudication with banked values only:

- 82=m is pencil ground truth. A clitic "m'"/"me" must attach to a following
  verb; therefore **any** grammatical parse of this window forces 16 to be
  verb-shaped (vowel-initial for the "m'" elision, consonant-initial "me [16]"
  otherwise — surface detail only). This is clitic-entailed, not a free
  ungranted assumption.
- Given 16 verb-shaped, the unique clean parse is the gerund frame:
  "m'[16-verb], en [85] [01] [52]".
- Rival check: "en" as adverbial pronoun + finite 85 ("m'[16] en [85-finite]")
  is ungrammatical — "en" is preverbal except in imperatives, and no imperative
  shape is available post-verbally here. No other rival exists; 16's
  intervention blocks any "l'en"-style cluster (unlike @733).

The murkiness flagged by stem-85 resolves: the shape is a gerund frame, with
16's verbhood forced by the m' clitic (stated cause, not assumed).

### @733 (a5_02): `88-11-24-85-93` — FENCED, does not confirm (bar clause 1)

"la (11, pencil) en (24, A3 GT)" forces the surface elision **"l'en"**. Two
parses, both grammatical in 1841 French using banked values only:

- (a) Gerund: "[88-verb] la (direct object), en [85] (gerund adjunct) [93]".
- (b) Pronoun cluster + finite 85: "[88] l'en (= la + en, cf. "il l'en informa")
  [85-finite] [93]".

No banked value rules out either parse; 88's and 93's classes are open, and 85
being finite in this one window contradicts nothing granted (A3 is frame-level,
verb-compatible either way). The stem-85 battery's "genuinely ambiguous"
assessment stands — re-derived, not cited. This leg confirms the 24-85 frame
but **not** the gerund reading specifically. Fenced with stated cause; recorded
as residual, not re-litigated.

## Per-clause results

1. @733 adjudicated: rival parse is real and grammatical under banked values;
   leg genuinely ambiguous → fenced, not counted as a gerund confirm. **Done.**
2. @1439 adjudicated: unique grammatical parse is the gerund frame; 16's
   verbhood is clitic-entailed by pencil 82=m. **Confirm.**
3. A3 "en [85]" x5: confirmed exactly 5 on the repaired stream. **Done.**
4. Tally: 4 of 5 legs confirm (@956, @1694, @1755, @1439); @733 fenced.
   Threshold (>=4) met. **PROMOTE.**

## Adverses

- "no value named — frame-level only": answered — this battery is frame-level by
  design; no value for 85 (or any open group) is named or promoted.
- "@1439 murky (16 open)": answered — adjudicated; gerund parse unique, 16
  verb-shaped by clitic entailment.
- "@733 'l'en'+finite rival": answered — rival verified as grammatical; leg
  fenced, excluded from the confirm count.
- "A3 leg count headline is 6 not 7": answered — the total A3 correction
  (5 gerund + 1 "que [85]er" = 6) stands; the "en [85]" sub-count x5 re-derives
  exactly and needed no correction.

## Verdict: PROMOTE

The five-leg gerund frame evidence for A3 re-derives on the repaired stream at
battery grade: 4 clean gerund legs, 1 genuinely ambiguous leg fenced with
stated cause, count confirmed at x5. No standing verdict contradicted or
downgraded. R5005, sealed gate instances, and the red-team adjudication queue
untouched. Residual: @733's "l'en"+finite rival remains a live ambiguity inside
the A3 evidence (fenced, not resolved).
