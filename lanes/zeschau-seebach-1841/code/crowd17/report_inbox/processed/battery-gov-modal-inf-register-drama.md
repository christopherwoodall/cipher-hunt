# Battery gov-modal-inf-register-drama

Target: `gov-modal-inf-register-drama` (priority 3). Completed 2026-10-09.

## Bar (verbatim, pre-registered)

"Corpus-wide census of modal/perception-governed exclamatory infinitives ('il faut voir !', 'Voir pendre !') in drama with any topic; if attested drama-wide with other topics, the reinforced-head gap is head-specific and the cross-register fence stands; if unattested, the zero is register-level"

Restated as clauses:
- C1: run the corpus-wide census on the 14-play drama corpus (one edition per play), any topic.
- C2: genuine modal/perception/causative-governed exclamatory infinitives attested in drama with non-reinforced-demonstrative topics -> the reinforced-head gap is head-specific; the cross-register fence stands.
- C3 (else): zero genuine -> the zero is register-level.

## Method

Exact mirror of the sibling `gov-excl-inf-register-drama` census method,
with the governor set swapped from prepositions to modal / perception /
causative verb forms:

- Corpus: the same 14 distinct-play drama files, one edition per play
  (`hugo-hernani-1870.txt` in, `hugo-hernani.txt` out), total 2,969,582 chars.
- P1 (candidate): for every "!", take the 120 chars before it; run
  MOD_INF = `<governor> (clitics 0-3) <bare infinitive>` over the segment.
  Governor forms: il faut/fallait/faudra/faudrait, faire (all forms),
  laisser, pouvoir, vouloir, devoir, savoir, voir, regarder, entendre,
  ecouter, sentir (finite, infinitive, participle forms). Infinitive-shaped
  word: `[a-z...]{2,}(er|ir|re|oir)`. Keep the match closest to the "!";
  require no [.;] between infinitive end and the "!".
- P2 (banding): tight band dist <= 40 is the discriminating band;
  wide band 40 < dist <= 120 triaged separately.
- Every candidate printed and MANUALLY classified. "Genuine" = a
  modal/perception/causative-governed infinitive phrase standing as an
  INDEPENDENT exclamation: no finite matrix verb in its own unit. Ordinary
  declarative matrix clauses that merely end with "!" (dialogue punctuation)
  are not genuine.

Script: `code/crowd17/next-token/gov_modal_inf_register_drama_census.py`;
raw output: `code/crowd17/next-token/gov-modal-inf-register-drama_census.json`.

Census totals: 13,212 bangs; 347 candidates total; 203 in the tight band.

## Findings

C1 PASS. Census run byte-exact over the 14-play corpus; all 203 tight-band
and 144 wide-band candidates hand-reviewed.

### Genuine attestations (5, across 5 of 14 plays)

1. **scribe-verre-d-eau.txt** — "ABIG., poussant un cri. **Vous faire tuer !**
   pour vous soustraire au danger…" — causative "faire" + "tuer", subject
   "Vous" (personal pronoun topic). Independent exclamatory infinitive.
2. **scribe-bertrand-et-raton.txt** — "Raton continue à demi-voix en
   s'adressant à sa femme.) **Vouloir nuire à mon avancement, à ma
   fortune !**" — modal "vouloir" + "nuire"; topic-less bare infinitive
   exclamation.
3. **hugo-ruy-blas.txt** — "Que dirait-on ? **me voir payer ce que je
   dois !** Ah !" — perception "voir" + "payer"; topic-less.
4. **vigny-chatterton-1835.txt** — "Sortons d'ici. Voir sa dernière retraite
   envahie, son unique repos troublé, sa douce obscurité trahie ; **voir
   pénétrer dans sa nuit de si grossières clartés !** O supplice !" —
   perception "voir" + "pénétrer"; topic-less.
5. **musset-comedies-proverbes-1850.txt** — "Conçoit-on rien à cela ?
   Nous renvoyer, **ne rien vouloir entendre**, laisser sans vengeance un
   coup pareil !" — modal "vouloir" + "entendre" inside an independent
   exclamatory infinitive accumulation; topic-less.

Not one of the five carries a reinforced-demonstrative head
(celui-là / celle-ci / etc.).

### Excluded lookalikes

- **hugo-ruy-blas "Voir pendre à quatre clous au gibet de la ville !"** is
  governed by finite "voudrais" inside a "Que…" optative frame — not an
  independent exclamatory infinitive. Excluded.
- "Il faut mourir, mourir désespéré !", "je veux le savoir, moi !",
  "Allez vous faire pendre !", "il faut jouer Hamlet !" and ~195 others
  are complete matrix clauses (finite verb present) with dialogue "!";
  the "!" punctuates the clause, not an infinitive construction. Excluded.
- Wide-band candidates all sit in sentences whose "!" belongs to a later
  sentence (dist > 40); none forms a governor+infinitive exclamation unit.

### C2 fires

Five genuine modal/perception-governed exclamatory infinitives are attested
drama-wide (5 of 14 plays) with non-reinforced topics (one personal-pronoun
topic, four topic-less). The reinforced-head zero from
`reinforced-modal-inf-drama` NULL is therefore HEAD-SPECIFIC: the
construction exists in drama; it just never takes a reinforced-demonstrative
head. The cross-register fence stands — the prose zero is untouched by this
battery (prose not re-censused here).

C3 does not fire.

## Adverses

"coordinates with gov-excl-inf-register-drama (the preposition-governed
register arm); does not duplicate it" — answered: this battery uses the
modal/perception/causative governor set, a distinct candidate population
from the preposition arm. It does not re-classify the preposition arm's
windows. Note the running workers on `gov-excl-inf-drama-n2` and
`gov-excl-inf-drama-recall` are distinct targets (Scribe-idiolect widening
and recall-gap closing for the preposition arm), not duplicated here.

## Verdict: PROMOTE

All bar clauses pass; the adverse is answered. No standing or red-team
verdict is contradicted; §7 intact; R5005, sealed gates, and the red-team
queue untouched. No follow-ups proposed (promote per §4).

§7 caveat: no polyvalence declared; nothing here licenses a second value
for any banked cell.
