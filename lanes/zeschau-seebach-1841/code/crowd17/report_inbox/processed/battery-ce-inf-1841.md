# Battery verdict: ce-inf-1841

## Bar (verbatim from battery-queue.json)

"validate the 'ce + infinitive' construction in period French; parse or fence @23-24 and @1232 under 33 = verb"

Restated as numbered clauses (pre-registered before testing):

1. The 'ce' + infinitive nominalization is validated as grammatical in 1841 diplomatic French against period sources.
2. @23-24 ('47 33' @23-24, row a1_00) parses or is fenced under 33 = verb.
3. @1232 ('47 33 29' @1232, row a7_01) parses or is fenced under 33 = verb.

## Method

Re-derived on the repaired 1,847-pair stream (`code/side-keyhunt/repaired_offsets.json`
+ `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
pair count verified 1847 in-session). `canonical.py` never touched. R5005, sealed
gates, and the red-team adjudication queue untouched. Standing grants used:
47='ce' (A4 allophone tier), 87='ce' (promoted), 29='er' (pencil), 64='qui'
(promoted), 79='tout' (A5), A10 (33+29 stem/whole HOLD). 33 = verb-class granted
per ce33-noun-slot (not re-litigated). 98='vient' is battery-promoted (unratified),
cited as such. Period validation via period dictionary (Littré 1872-1877),
period-adjacent grammars, and historical-linguistics literature; sources cited
below, brief quotes only.

## Evidence

### Windows under test (byte-exact, repaired stream)

- @23-24 (row a1_00): `17(fois) 64(qui) 98 82(m) 43 29(er) 47(ce) 33 55 81 00(pour) 34(i) 24 30(pas)`
  Cited parse: 'qui vient mener ce [33]' (98='vient' battery-level; 82-43-29='mener').
  'mener' takes a direct-object NP, so '47 33' must be nominal.
- @1232 (row a7_01): `64(qui) 79(tout) 82(m) 48(e) 29(er) 47(ce) 33 29(er) 85 56 10 03 40 67`
  '47 33 29' = 'ce' + [33] + 'er'; under A10, 33-29 is stem+'er', i.e. 'ce' + infinitive.
- '47 33' census: exactly x2 on the repaired stream (@24, @1232) — both windows
  are the full population. No third window exists to rescue the construction.

### Period-corpus findings

1. **Littré, Dictionnaire de la langue française (1872-1877), art. "infinitif":**
   "Le boire est un infinitif employé comme substantif." The substantivized
   infinitive takes the definite article "le". No "ce" + infinitive entry or
   example anywhere in the article.
   Source: https://www.littre.org/definition/infinitif
2. **Calvet & Chompret, Grammaire française (cours moyen):** on the pronoun
   "ce": it "précède un verbe ou un pronom relatif ; il n'est jamais suivi
   immédiatement d'un nom" (precedes a verb or a relative pronoun; never
   immediately followed by a noun).
   Source: https://fr.scribd.com/document/677839595/GF1
3. **TLFi, art. "ce" (Étymol. et Hist.):** the only infinitive-introducing
   construction after "c'est" is "c'est ... que de + inf." (attested 1463,
   Maistre Pathelin) — never bare "ce" + infinitive. "ce" with verbs other than
   "être" is noted as "rare, subsiste dans un style soutenu et plus ou moins
   archaïque" even for the classical period.
   Source: https://www.dicocitations.com/definition_littre/5155/Ce.php
4. **Buridant (via Cairn, "La substantivation de l'infinitif en ancien
   français"):** demonstrative + infinitive ("en cest venir") is documented as
   an OLD French elementary degree of substantivation — a medieval feature,
   not a 19th-century one.
   Source: https://www.cairn.info/article.php?ID_ARTICLE=LF_147_0098
5. **Darmesteter (via openedition):** "Dans la vieille langue, l'infinitif
   pouvait, comme en grec, s'employer substantivement, en se faisant précéder
   de l'article" — the article-preceded substantivized infinitive is framed as
   a feature of "la vieille langue" (the old language).
   Source: https://books.openedition.org/septentrion/115963?lang=en
6. **Neutral pronoun "ce" as direct object:** "ce" cannot serve as a bare
   direct object ("*mener ce" is ungrammatical); it requires "être" or a
   relative clause ("ce qui", "ce que"), per the pronoun-syntax sources above
   and Wikipedia "Pronom démonstratif en français" ("n'est habituellement
   employé qu'en combinaison avec d'autres éléments").

### Structural analysis under 33 = verb

For '47 33' to parse as a nominal direct object of 'mener' (@23-24), "ce" must
be either:
- (a) the demonstrative adjective determining a nominalized infinitive
  ("ce [infinitif substantivé]") — requires the 'ce + infinitive'
  construction; refuted by findings 1-5 above; or
- (b) the neutral pronoun as bare object ("mener ce [33]" apposition) —
  ungrammatical per finding 6 ("ce" never a bare object; "*mener ce").
- Considered and rejected: 47 = "se" (reflexive). Not licensed — A4 fixes
  47='ce' (positional allophone of 87); and "mener se [33]" / "...er se [33]er"
  has no governing structure either. No lane standing supports 47='se'.

## Per-clause results

1. **Validate 'ce + infinitive' in period French — FAIL (kill grade).** The
   period dictionary positively establishes "le" as the substantivized
   infinitive's determiner (Littré); grammars state the pronoun "ce" is never
   immediately followed by a noun; the only "c'est" + infinitive construction
   is "que de + inf."; demonstrative + infinitive is Old French only. Zero
   period attestations of "ce" + infinitive found; the rule against it is
   positively established. The construction does not exist in 1841 French.
2. **@23-24 under 33 = verb — FENCED.** Neither (a) nor (b) parses. The window
   cannot be grammatical under 33=verb via any 'ce'-headed nominal. Fenced as
   'ce' + verb contact residual (unparsed). This executes the conditional arm
   of the already-queued slot-24-fence target (ce33-noun-slot follow-up #3).
3. **@1232 under 33 = verb — FENCED.** 'ce [33]er' requires exactly the
   refuted construction (A10 makes the infinitive reading explicit here).
   Fenced as 'ce' + verb contact residual (unparsed).

## Adverses

- **"Decides whether the @24 window parses (ce33-noun-slot's crux)" — ANSWERED,
  negatively.** The @24 window does NOT parse under 33 = verb. The crux is
  decided: the nominalization route is closed. The window must be fenced
  (slot-24-fence, already queued) or re-segmented — not parsed as 'ce [N]'.

## Verdict: KILL

Headline: 'ce' + infinitive nominalization is ungrammatical in 1841 French —
the period corpus positively establishes "le" as the substantivized
infinitive's determiner (Littré 1872-1877) and confines demonstrative +
infinitive to Old French. Both '47 33' windows (@23-24, @1232 — the complete
population, x2) are therefore unparseable under 33 = verb and are fenced as
'ce' + verb contact residuals. No standing verdict contradicted or downgraded
(33 = verb-class stands; 47 = 'ce' A4 stands; A10 stands). No red-team
escalation required (no contradiction with a red-team verdict).

## Follow-ups

1. `slot-1232-fence` (P3): fence @1232's '47-33-29' contact as a 'ce' + verb
   residual under 33 = verb, mirroring slot-24-fence (already queued for
   @23-24); record both residuals against 47's A4 allophone tier. Rationale:
   this battery fenced @1232 but no dedicated fence target exists for it yet.
   (For a kill, follow-ups are optional; this one is proposed because the
   @1232 window otherwise has no recorded disposition.)

## Bookkeeping

- Lock `locks/ce-inf-1841.lock` created on start (agent id + UTC), deleted on completion.
- Queue: `battery-queue.json` updated via temp-file + rename (this target only;
  status `verdict`, result `kill`, report path, date 2026-10-09; pre-write
  assert confirmed prior status was `queued` — no downgrade).
- R5005, sealed gate instances, and the red-team adjudication queue untouched.
