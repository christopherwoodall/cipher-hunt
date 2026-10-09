# Battery report: temp-65-en-frame

- Target: `temp-65-en-frame`
- Verdict: **KILL** (en-frame arm fenced at kill grade)
- Date: 2026-10-09
- Worker: 4524425a-5a09-4152-b69f-61caa7201920
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json`
  + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`).
  `canonical.py` never used. R5005, sealed gate instances, red-team
  adjudication queue untouched. @-offsets are 0-based pair indices of the
  65 slot (det-65-gender-adjudicate convention); 1-based equivalents in
  parentheses.
- Protocol: read BATTERY-PROTOCOL.md in full before work. Lock
  `code/crowd17/next-token/locks/temp-65-en-frame.lock` created on start
  (2026-10-09T16:33:16Z); no prior or stale lock existed; deleted on
  completion.

## Bar (verbatim, pre-registered BEFORE testing)

"name the temporal/locative reading iff a period-evidenced frame licenses it;
else fence the en-frame arm"

## Bar restated as numbered clauses (fixed BEFORE the stream census)

- **C1:** A temporal/locative reading of "en [65]" at @812 and/or @1383 is
  NAMED iff a period-evidenced frame licenses it. License needs three legs:
  (i) 24 = preposition "en" is live at the window; (ii) 65 is a
  temporal/locative noun at battery grade; (iii) period French grammar
  licenses the combined "en [temporal/locative noun]" frame.
- **C2:** If C1 fails, the en-frame arm is FENCED with stated cause for each
  failed leg (noted, never ignored).

Listed adverses: "65 noun-class (R20-047); 'en'+N is polysemous".

## Method

Re-derived the repaired stream in-work (1,847 pairs / 96 types asserted).
Extracted all '24 65' bigrams: exactly two, 24 at 0-based @811 and @1382
(65 at @812, @1383; 1-based @813/@1384). Full ±8 windows taken byte-exact.
Checked each of C1's three legs against standing verdicts (protocol §7,
battery promotes/kills, red-team docket untouched — not re-litigated).

## Stated period evidence

- Period French grammar (1841 diplomatic French, the lane's standing frame;
  corpus grammars `corpus-grammars19c/` are too OCR-degraded for fine frame
  citation — the 1843 Girault-Duvivier text discusses "préposition en"
  vs. the pronoun "en" only at gross level) licenses: preposition "en" +
  [time noun] → temporal reading ("en janvier", "en 1841"); preposition
  "en" + [place noun] → locative reading ("en France", "en ville"). This
  frame class holds in every period of French, including 1841. C1(iii)
  is therefore licensed as a FRAME; it does not by itself instantiate
  "en [65]". Instantiation needs legs (i) and (ii).
- Standard French: the pronoun "en" is a preverbal clitic — it must precede
  a verb, never a bare noun. An "en [noun]" shape is preposition "en"
  only. So leg (i) requires the preposition reading specifically.

## Window-level evidence

### @812 (row a5_05)

0-based 804–820, byte-exact:

`53 69 24 24 41 12 48 [24] 65 14 29 49 74 74 47 78 40`

Left context: `41 12 48 [24]` = "[41] n(12) e(48) [24]" — letter-tier grants
(12=n, 48=e per R17/lane convention). This is the "ne [24]" shape.

- Leg (i) FAILS. The standing battery-promoted parse (ne-24-profile,
  not downgraded; 24-en-verb-conflict escalated to red team but explicitly
  left the promote standing) consumes this window: lone-"ne" negation of a
  finite 24, with 65 in the post-finite-verb direct-object slot
  (prof-65 L3). Preposition-"en" would need "12 48" to belong elsewhere —
  ungranted. Pronoun-"en" is ungrammatical before a noun (65 is
  noun-class, prof-65 PROMOTE). Independently: 24='en' is killed at kill
  grade at 6 windows (24-en-verb-conflict C1: @162, @1774, @1486, @190,
  @643, @823), and its surviving windows are the gerund "24-85" frames
  (@732/@955/@1438/@1693/@1754) plus fenced (@73/@179/@1766/@311/@474) —
  @811 is in neither set. No battery-grade support for 24='en' at @811.
- Leg (ii) FAILS. 65's full 25-window noun profile (prof-65 PROMOTE, six
  legs: qui-relative head x3, que-relative head x1, post-finite-verb
  direct object x2, post-"-ere" slot x3, post-verb x1, subject-NP member
  x2) contains ZERO temporal or locative frames. vient-65-complement
  explicitly tested 65 for a time/locative reading (@511) and found none;
  det-65-gender-adjudicate found no temporal/locative agreement evidence.
  Positing a temporal/locative 65 is ungranted.
- Result: no "en [65]" reading of any kind is licensed at @812; the
  temporal/locative arm specifically fails both legs independently.

### @1383 (row a7_06)

0-based 1375–1391, byte-exact:

`86 29 89 84 92 69 13 [24] 65 68 52 82 16 06 29 67 86`

- Leg (i) FAILS. Battery-level parse consumes the window: `13 [24] 65 68`
  = [13-nominal-closing-suffix] + finite verb 24 + 65 in object slot + 68
  (prof-65 L3; reseg-13-armA PROMOTE for 13's class). The en-surviving
  window set (above) likewise does not contain @1382. Pronoun-"en" is
  ungrammatical before noun 65. Preposition-"en" is ungranted.
- Leg (ii) FAILS for the same reason as @812: 65's profile has no
  temporal/locative leg anywhere.
- Result: the temporal/locative arm fails both legs independently at @1383.

## Per-clause pass/fail

- **C1: FAIL at kill grade.** Both windows force the claim false. Leg (i):
  24 is not 'en' at @811/@1382 at battery grade (standing verb parses
  consume both windows; 24='en' has no surviving-window support at either;
  pronoun-'en' is ungrammatical before noun 65). Leg (ii): 65 is not a
  temporal/locative noun at battery grade (full 25-window profile, zero
  temporal/locative frames; explicitly tested in vient-65-complement and
  det-65-gender-adjudicate). Leg (iii) passes as a frame class (period
  evidence states it) but cannot instantiate without (i) and (ii).
- **C2: PASS.** The en-frame arm is fenced. Stated cause, per leg:
  F1 (24≠'en' at the windows): standing "ne [24-verb] [65]" (@811) and
  "[24-verb] 65 68" (@1382) parses (ne-24-profile promote, prof-65 L3);
  24='en' globally killed at 6 windows and absent from the en-surviving
  window set at @811/@1382; the red-team 24 docket is untouched and
  unadjudicated here.
  F2 (65 not temporal/locative): six-leg noun profile with no
  temporal/locative frame; the one prior time/locative test
  (vient-65-complement @511) found none.
  F3 (polysemy adverse): 'en'+N is polysemous (manner/material/state/time/
  place), so a bare "en [65]" could never license the NAMED temporal/
  locative reading without a licensed temporal/locative noun — which is
  absent.

## Adverses answered

- "65 noun-class (R20-047)": ANSWERED. 65 = noun-class stands (prof-65
  PROMOTE, six frame legs; this verdict does not downgrade or touch it).
  The noun-class standing is precisely what the fence rests on: 65's noun
  profile is fully enumerated and has no temporal/locative leg.
- "'en'+N is polysemous": ANSWERED. Absorbed as F3 — the fence does not
  infer any other 'en' sense either; it only excludes the arm the bar
  tested.

## Verdict: KILL

The temporal/locative "en [65]" reading is excluded at kill grade at both
@812 and @1383. The "name" arm fails definitively (C1 fails at kill grade;
both windows force the claim false on two independent legs), and cleaner
battery-grade rival parses consume both windows ("ne [24-verb] [65]" @811,
"[24-verb] 65 68" @1382). The en-frame arm is fenced per C2. No standing
verdict contradicted or downgraded; the red-team 24 docket and all other
24/65 targets are untouched. No null → no §4 follow-ups mandated.
Residual 65-value work belongs to the already-queued `noun-65-value`
target (not duplicated here).

## Provenance

All pair indices 0-based; n(65)=25 re-derived; '24 65' occurs exactly
twice (24 at @811, @1382). Lock
`code/crowd17/next-token/locks/temp-65-en-frame.lock` created
2026-10-09T16:33:16Z, deleted on completion.
