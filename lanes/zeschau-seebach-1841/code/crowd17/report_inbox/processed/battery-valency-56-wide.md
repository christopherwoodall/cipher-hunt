# Battery report: valency-56-wide

Worker: agent 8680f48f-7606-4739-b20a-913a2a04b102
Date: 2026-10-09
Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.
Offset convention: 0-based pair indices (matches the noun26/name-56-verb battery family; brief's @795/@1745 match).

## Bar (verbatim, pre-registered)

"Test the Xeent candidates' valency against 56's other verb-shaped windows (@1732 '[56] pas', @795's 37-complement shape, @1745's postverbal subject 65) for a valency discriminator."

Numbered clauses (frozen before testing, not modified after):

1. C1 — enumerate the Xeent candidates (the full -eent set, including name-56-verb's caveat candidates procreer, maugreer, degreer, reer).
2. C2 — test each candidate's valency against 56's other verb-shaped windows: @1732 '[56] pas', @795's 37-complement shape, @1745's postverbal subject 65.
3. C3 — kill candidates that fail at kill grade (a window's frame is incompatible with the candidate's valency while a rival candidate's valency fits).
4. C4 — if C3 does not fire, fence with stated cause.

## Method

Byte re-derivation of all three windows with ±4 context from the repaired stream. n(56) = 23 windows census-re-derived in session. Valency classes grounded in period lexicons (Littré via littre.org and dicocitations.com Littré mirrors, fetched 2026-10-09; TLFi for maugreer). French 3sg -ee and 3pl -eent forms verified for each candidate. Standing premises adopted (not re-litigated): 64='qui', 46='que', 40='e', 06='ent', 30='pas' (banked/red-team); 37 predicative frame (A1); 65 noun-class (R18-001); stem-56-whole PROMOTE (56 whole-word, @1745 the budgeted orphan).

## C1 — candidate enumeration

Nine French verbs form 3sg -ee / 3pl -eent (the Xee / Xeent class), Littré-grounded:

| candidate | valency (lexicon) | 3sg | 3pl |
|---|---|---|---|
| creer | v.a. (transitive) — Littré | cree | creent |
| agreer | v.a. (transitive); also "agreer que"+subj., intr. "agreer a" (plaire) — Littré | agree | agreent |
| suppleer | v.a. (transitive); also "suppleer a" (intransitive indirect) — Littré | supplee | suppleent |
| recreer | v.a. (transitive) — Littré | recree | recreent |
| greer | v.a., Terme de marine — Littré | gree | greent |
| procreer | v.a. ("Engendrer"); also used absolutely — Littré (fetched 2026-10-09) | procree | procreent |
| maugreer | v.a. (vx/litter.: "maudire quelqu'un") AND v.n./intrans. ("montrer sa mauvaise humeur") — TLFi A./B. | maugree | maugreent |
| degreer | v.a., Terme de marine (parent battery's caveat) | degree | degreent |
| reer | v.a., Terme de charronnage (parent battery's caveat) | ree | reent |

Note: degreer and reer are cited from the parent battery's caveat set; independent lexicon re-verification for these two is outstanding (xeent-register-tiebreak's set-exhaustiveness venue, still queued).

## C2 — window-level evidence

- **W1732 (0-based 1736, row a8_07):** `...30 15 01 56 30 06...` = "...[pas] [15] [01] [56] pas [06]". Finite 3sg 56 + 'pas' (30='pas' red-team promoted). **Test:** negation is valency-neutral. All nine candidates negate identically ("il ne cree/maugree/etc. pas"). Verdict per candidate: FITS (all 9). No discriminator.
- **W795 (0-based 799, row a5_04):** `64 46 07 64 56 37` = "...[07] qui [56] [37]". Relative subject qui + finite 3sg + 37 object/predicative complement. **Test:** all nine candidates take a direct object (creer/agreer/suppleer/recreer/greer/degreer/procreer/reer v.a.; maugreer's transitive arm "maudire quelqu'un"). "qui cree/agree/supplee/recree/gree/procree/ree/maugree [37]" all grammatical. Verdict per candidate: FITS (all 9). No discriminator. Corroborating second instance: **0-based 1658 (row a8_04)** `16 01 56 37` = "[16] [01] [56] [37]" — same finite-3sg + 37-complement shape, all nine fit identically.
- **W1745 (0-based 1749, row a8_08):** `94 82 46 56 40 06 65 34` = "ne m que [56]e ent [65]". Xeent-class 3pl (40='e' + 06='ent'), no object, postverbal subject 65 (noun class). **Test:** all nine form 3pl -eent. The objectless frame strains the strictly-transitive candidates (creer, recreer, greer, degreer, reer) equally — emploi absolu is licensed in French, so strain is not incompatibility — and fits the intransitive-capable ones (maugreer intr., agreer/suppleer a-constructions, procreer absolute) marginally better. Verdict per candidate: FITS (all 9); strain distribution is gradient, not kill-grade.

## Per-clause results

- C1: PASS — nine candidates enumerated with lexicon-grounded valencies.
- C2: PASS — all nine tested against all three windows (plus the @1658 corroborating frame).
- C3: DOES NOT FIRE — no candidate fails at kill grade. No window's frame is incompatible with any candidate's valency: the "pas" window is valency-neutral; the 37-complement window admits all nine (every candidate has a transitive arm); the objectless 3pl window strains transitive-only candidates equally (emploi absolu licensed) without forcing any false. Kill grade requires a window forcing the claim false — not met anywhere.
- C4: FIRES — 56's verb identity is fenced as underdetermined at battery grade, with stated cause: all nine Xeent candidates carry (near-)identical transitive valency profiles, so valency cannot discriminate among them.

## Adverses answered

The target's adverse — "All five candidates transitive (Littre v.a.) -eer verbs with identical valency profiles; no single candidate's valency fits where the others' do not at the three tested windows" — is CONFIRMED, not ignored: the wider nine-candidate test (including the parent's caveat set and maugreer's mixed v.a./v.n. profile) reproduces the uniformity exactly. No candidate's valency fits where the others' do not at any tested window.

## Caveats (stated, not hidden)

- degreer and reer entries are parent-cited; independent lexicon verification is outstanding (pending xeent-register-tiebreak, still queued).
- Register (greer/degreer nautical, maugreer familiar) was not graded here — that is xeent-register-tiebreak's venue, not valency.
- Selectional pressure is value-open: 37's value (A1) and 65's value at @1745 are both open; a named value at either slot could create selectional discrimination where valency cannot.

## Verdict: NULL (fence executed)

Valency cannot discriminate the Xeent candidates at any tested window. No candidate excluded; no candidate selected. 56's verb identity stays fenced as underdetermined.

## Follow-ups proposed (for supervisor queuing)

1. `sel-37-pressure` (P3) — name 37's value (A1 predicative); a named 37 creates selectional pressure on 56's object slot at @795/@1658 (e.g. a naval object would select greer/degreer).
2. `sel-65-1745-pressure` (P3) — name 65's value at the @1745 postverbal-subject slot; a named 65 could discriminate (animate subject vs. rigging-like object).
3. `verb56-register-closeout` (P3) — once xeent-register-tiebreak lands, close out the register venue (greer/degreer nautical vs. maugreer familiar vs. the diplomatic register of the letter) and check whether the remaining valency tie survives.
