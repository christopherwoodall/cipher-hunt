# Battery report: name-56-verb

Worker: agent a3f87f9a-8dbb-4cc1-adb3-14782ee469cc
Date: 2026-10-09
Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.
Offset convention: 0-based pair indices (matches the noun26 battery family; brief's @795/@1626/@1745 match).

## Bar (verbatim, pre-registered)

"one candidate's valency fits all three windows (@795 'qui [56] 37', @1626 'que [56] 69 26', @1745 'que [56]e ent') or fence the identity as underdetermined"

Numbered clauses (frozen before testing, not modified after):

1. C1 — one of {créer, agréer, suppléer, recréer, gréer} has a valency profile fitting all three windows while the others do not (discrimination).
2. C2 — if C1 fails, fence 56's verb identity as underdetermined, with stated cause.

## Method

Byte re-derivation of the three windows with ±6 context. Valency profiles grounded in Littré (littre.org, fetched 2026-10-09): créer "ils créent", v.a.; agréer "V. a. Recevoir favorablement, trouver bon."; suppléer "v. a. ... Ajouter ce qui manque, fournir ce qu'il faut de surplus."; recréer "v. a. ... Créer de nouveau"; gréer "v. a. Terme de marine. Garnir un bâtiment de voiles, poulies, manœuvres, etc." All five are transitive (verbe actif) -éer verbs; all form 3pl in -éent (créent/agréent/suppléent/recréent/gréent).

Standing premises adopted (not re-litigated): 64='qui', 46='que', 00='pour' (banked/granted); 94='ne' STRONG LEAD; 40='e', 06='ent', 12='n', 48='e' (letter tier); stem-56-whole PROMOTE (56 whole-word, @1745 the single budgeted orphan with the Xéent stem parse clean per rightedge-56-1745 C2); noun26-69-pour-dire PROMOTE (69 = noun, subject of 26 at the formula windows).

## Window-level evidence

- W1 0b@795 (row a5_04): `...64 56 37...` = "qui [56] [37]". 64='qui' banked subject relative; 56 finite 3sg ("crée"-shaped); 37 predicative complement (A1). All five candidates transitive with direct-object valency: "qui crée/agrée/supplée/recrée/grée [37]" all grammatical in frame. No discriminator.
- W2 0b@1626 (row a8_03): `33 46 56 69 26 00 33 21 64` = "[33] que [56] [69] [26] pour [33] [21] qui". 46='que' banked; 56 finite 3sg interposed before the formula "[69-N-subj] [26-V-fin] pour [33]" (noun26-69-pour-dire's parse adopted). 56's subject/object assignment is unresolved at battery grade (69 is 26's subject per the landed battery; whether 69 is 56's postverbal subject or object, or 56's subject lies leftward, is not forced). All five candidates equally compatible under every live assignment — the ambiguity is structural, not valency-driven. No discriminator.
- W3 0b@1745 (rows a8_07/a8_08): `94 82 46 | 56 40 06 | 65` = "ne m que [56]e ent [65]". Xéent-class 3pl ("créent/agréent/suppléent/recréent/gréent"); 40='e' + 06='ent' per standing letters; 65 (noun class, R18-001) postverbal subject; no object present. All five form -éent 3pl; all five are normally object-taking, so the objectless frame strains all five equally. No discriminator.

## Per-clause results

- C1: FAIL — no valency discriminator exists among the five. All five are transitive -éer verbs (Littré v.a. for each); all five form 3pl -éent; all five take a direct object at W1; all five are equally compatible (or equally strained) at W2 and W3. Valency is identical across the candidate set, so no single candidate's valency fits where the others' do not.
- C2: FIRES — 56's verb identity is fenced as underdetermined at battery grade.

## Adverses answered

Mixed-class profile (verb-slot "qui [56]" @795 beside nominal "56 64"/"56 fois"/pre-adjective legs): no value is named and no §7 polyvalence is declared — the noun/verb alternation stays red-team territory (stem-56-whole C2's red-team-eyes analysis adopted as the venue, not duplicated).

## Caveats (stated, not hidden)

- The claim's five-candidate set is not exhaustive: procréer, maugréer, dégréer also form 3pl -éent. Any future naming must first close the set.
- gréer is "Terme de marine" (Littré) — a register consideration, not a valency discriminator; not graded here.

## Verdict: NULL (fence executed)

56's verb identity is fenced as underdetermined. No candidate excluded by valency; no candidate selected by valency.

## Follow-ups proposed (for supervisor queuing)

1. `xeent-register-tiebreak` (P3) — Littré/register tiebreak on the Xéent set in 1841 diplomatic French (gréer/dégréer nautical, maugréer familiar); verify candidate-set exhaustiveness (procréer, maugréer, dégréer, réer) before any naming.
2. `valency-56-wide` (P3) — test the Xéent candidates' valency against 56's other verb-shaped windows (@1732 "[56] pas", @795's 37-complement shape, @1745's postverbal subject 65) for a valency discriminator.
3. `parse-1626-clause` (P3) — resolve the clause structure of "que [56] [69] [26] pour [33]" (56's subject/object assignment); the assignment constrains the verb's valency.
