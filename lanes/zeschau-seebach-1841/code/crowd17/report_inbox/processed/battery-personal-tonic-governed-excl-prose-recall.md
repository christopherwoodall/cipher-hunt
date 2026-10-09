# Battery report: personal-tonic-governed-excl-prose-recall

- Target id: `personal-tonic-governed-excl-prose-recall` (P3)
- Claim: mirror recall-gap closure on the 27.66M-char prose corpus (400-char windows + '?' termination)
- Date: 2026-10-09
- Stream: corpus census per target charter; the 1,847-pair repaired parse is not applicable (no cipher data touched). `canonical.py` never used. R5005, sealed gates, the red-team adjudication queue: untouched.
- Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause, set off by a pause, resumed by a pronoun. "Governed exclamatory infinitive" = an infinitive led by a preposition (pour/de/a) that carries the exclamatory force itself ("Moi, pour rire !"). "Tonic pronoun" = moi/toi/lui/elle/nous/vous/eux.

## Parentage

Prose-register recall mirror of `personal-tonic-governed-excl-prose` (NULL 2026-10-09: 26 candidates, 0 genuine, 180-char windows, '!' only). Method mirrors the drama recall sibling `personal-tonic-governed-excl-recall` (NULL 2026-10-09: 356 candidates, 0 genuine, 400-char windows, '!'/'?' termination), which proposed exactly this target as follow-up #1.

## Bar (verbatim, pre-registered)

"0 genuine confirms the prose zero is not a window/termination artifact; any genuine re-opens register-wide"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (zero arm):** 0 genuine hand-classified candidates under the widened net (400-char windows, '!' or '?' termination) confirms the parent zero was not a window/termination artifact.
2. **C2 (re-open arm):** any genuine tonic-topic + governed exclamatory infinitive re-opens the licensor class register-wide.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/personal-tonic-governed-excl-prose-recall.lock` on start (2026-10-09T15:12:00Z, agent id inside); no prior lock existed.
2. Re-runnable script: `code/crowd17/next-token/personal_tonic_governed_excl_prose_recall_census.py`; raw results in `code/crowd17/next-token/personal-tonic-governed-excl-prose-recall_census.json`.
3. P1/P3 copied VERBATIM from the prose parent (not modified after seeing data):
   - P1: `\b(moi|toi|lui|elle|nous|vous|eux)\s*[,;:]` case-insensitive.
   - P3: strict `\b(?:pour|de|d'|a)\s+[a-z…]{2,}(er|ir|re|oir)\b`; loose clitic-tolerant variant tagged separately.
   - Changed ONLY: window = text from the pronoun through the next `[!?]` (inclusive), cap 180 → 400 chars. P2 filter = '!' or '?' (was '!' only). Hand-classification used ±700-char context.
4. Corpus identical to the parent (20 files, pinned): 17 files in `code/side-period/corpus/` (guizot-memoires t1/t2/t3/t5-t6, nesselrode v7-v10, revue-deux-mondes-1841 q1-q4, metternich-papiere v4/v6, talleyrand-memoires-v1, pozzo-di-borgo-correspondance-v1, levant-correspondence-1841-p3) and 3 files in `data/` (gutenberg-17489-miserables1, gutenberg-30513-tocqueville-t1, gutenberg-30514-tocqueville-t2).

## Yield

27,656,185 chars and 4,495 pronoun-comma hits — counts match the parent exactly (re-computed in-session). **295 candidates (218 strict, 77 loose-only).** Recall-gap check: all 26 parent candidates re-appear in the widened net (offset-set overlap 26/26). **269 new candidates**, every one hand-read with ±700-char context. **0 genuine.**

## Classification of the 269 new (all read, grouped by confound class)

**Finite-matrix-governed (dominant class).** The '!'/'?' terminates a finite clause; the infinitive is a complement or adjunct of a finite verb or participle.
- rdm-q2 @485887 — "Lui, depuis six mois entiers qu'il est investi de la dictature, qu'a-t-il fait?" — topic of a finite question; no infinitive with exclamatory force.
- rdm-q4 @76251 — "moi, de si bon accord, qu'il me proposa une partie de chasse pour le lendemain. Le moyen de refuser?" — finite clause; "de refuser" depends on the noun "moyen".
- rdm-q3 @1619489 — "n'est-ce pas la choquer évidemment ... que de faire de Jesus-Christ un moyen geometrique ...?" — finite rhetorical question; "de faire" governed by "que".
- rdm-q4 @867310 — "quand l'heure du repos aurait sonne pour lui, serait-il necessaire de recourir aux soins d'un inconnu?" — finite question; "de recourir" governed by "necessaire".
- rdm-q4 @1212527 / @1212564 — "Quand vous m'avez demande un rendez-vous, dit Louise, ai-je craint, moi, de me compromettre?" — rhetorical finite question; "de me compromettre" governed by "craint".
- metternich-v4 @1012434 — "Le dernier rapport ... ne me laisse pas de doute que ... nous aurons de la peine a reconnaitre l'endroit." — finite declarative.
- pozzo @110613 — "Mais comment changer de nature?" — finite question; "de gouverner"/"de nature" noun-phrase level.
- miserables1 @615126 — "Vous trouverez chez moi ... Je n'ai plus rien a ajouter. Prenez-moi. Mon Dieu!" — finite clauses; "a ajouter" governed by "rien".
- tocqueville-t2 @388544 — "ou de laisser tomber tous les citoyens ... n'en serait-ce pas assez pour vaincre bien des doutes ...?" — finite question.

**Pronoun governed by a preposition (no dislocation).** The tonic pronoun is the object of pour/de/a/parmi, not a topic.
- rdm-q2 @422412 — "Je vous le demande, non-seulement pour moi, qui ne suis que votre vieille amie ... Helas!" — "pour moi" complement of "demande".
- rdm-q2 @898899 — "Il faut pardonner a vos enfans pour l'amour de moi." — "de moi" inside "pour l'amour de".
- rdm-q2 @2378707 — "Il s'arrete en face d'eux" — "d'eux" object of "en face de".
- rdm-q4 @77247 — "dont la jalousie etait evidemment concentree sur moi" — "sur moi" complement.
- rdm-q4 @1261535 — "Je m'engage a te le ramener" — "te" clitic object; finite clause.

**Vocative or apposition of a finite clause.** The pronoun addresses or labels, it does not topicalize an infinitive.
- rdm-q3 @2633420 / @2633559 — poem vocatives "Vous, bleus ne m'oubliez pas" / "Et Vous, ne vous laissez plus voir" — finite imperatives.
- rdm-q4 @945944 — "il me plait, a moi, et charbonnier est maitre en sa maison." — parenthetical "a moi"; finite.
- miserables1 @141028 — "--Et moi, dit l'hote, je n'ai pas de chambre." — vocative; finite.
- miserables1 @297671 — "Donnez-lui une pique, il fera le 10 aout" — imperative + finite.
- talleyrand @891261 — "car vous, Sire, vous etes particulierement le souverain ..." — double vocative; finite.

**Noun-phrase false positives.** The regex matched de/a + a noun (not an infinitive).
- rdm-q2 @2273527 — "sa traduction a-t-elle completement un contre-sens de caractere?" — "de caractere" is a noun.
- rdm-q4 @1392455 — "exclut les ameliorations du present et l'intelligence de l'avenir" — "de l'avenir" is a noun.
- rdm-q2 @1514912 — "l'auteur du Philtre, de la Baijadere" — nouns.
- metternich-v6 @1311731 — "l'Angleterre par un esprit de vengeance de son premier Ministre" — nouns; "Un autre que moi rendrait outrage" — "moi" object of "que".

**Bare infinitives (outside the governed-shape bar, noted for follow-up).**
- rdm-q1 @1332013 — "Moi, voler!" — genuine tonic-topic + exclamatory infinitive, but the infinitive is bare, not governed by pour/de/a. The bar tests only the governed shape; this near-miss motivates follow-up #1.
- nesselrode-v7 @396326 — "Moi. —" is a dialogue speaker label; "de quoi rire" is governed by "il y a".

**Rhetorical finite questions (large subgroup).** '?' terminates a finite clause whose verb governs or precedes the infinitive.
- rdm-q2 @1041890 / @1042067 — "devions-nous perdre l'occasion de defaire ce que le cabinet russe avait fait?" — finite; "de defaire" governed by "occasion".
- rdm-q2 @1047329 — "Qu'est-ce a dire?" — "lui" is topic of the finite clause; no exclamatory infinitive.
- rdm-q2 @2052910 — "dites-le-nous, o Allemagne, notre soeur, filez-vous le linceul de votre genie ...?" — finite.
- rdm-q4 @1240883 — "J'espere, monsieur, ... que vous n'avez pas l'intention de recourir a un lache assassinat?" — finite.
- talleyrand @348914 — "Quel moyen ... de s'avouer incapable de comprendre ce mysterieux langage?" — finite; infinitives governed by "moyen".
- metternich-v4 @889391 — "M. Stratford-Canning ... a-t-il agi en vertu d'ordres positifs de son Gouvernement?" — finite.
- levant @817983 — "Pensez-vous, my Lord, que ... il serait bon de suggerer ...?" — finite.

**Quoted speech and interjections carrying the mark.**
- rdm-q2 @416037 — "me regarde et s'ecrie: O mon Dieu!" — the '!' belongs to the interjection, not an infinitive.
- rdm-q2 @2138896 — quoted refrain "ce que personne ne peut nier, ne peut nier!" — finite; "de la mere" is a noun.
- rdm-q4 @798899 — "pour vous, chere enfant, que ne ferais-je pas!" — finite conditional; "pour vous" is a benefactive adjunct.

**Poem/verse fragments.** Line breaks mimic dislocation; clauses stay finite.
- rdm-q3 @909187 — "Partout ou l'homme atteint, oh! nous l'aurions trouve." — finite.

**Mis-attributed topics (postposed subjects, datives, objects).**
- miserables1 @609362 — "L'accuse, lui, les avait ecoutees" — "lui" is a postposed subject of a finite clause.
- miserables1 @601854 — "Je ne sais pas expliquer, moi" — postposed subject; finite.
- miserables1 @431431 — "Mais lui, il m'avait perdu toute ma robe" — "lui" subject of finite.
- rdm-q2 @1431855 — "Voila ce qui reste a votre seigneurie de ses trois chiens, lui dit tristement le geolier." — "lui" dative object.
- miserables1 @650407 — "puis elle accrocha la clef au clou ou il la prenait d'habitude" — "lui" object of "l'"; finite.

**Earlier tranche ([0]–[132]) same verdict.** Same confound mix: finite-matrix-governed, pronoun-as-preposition-object, finite vocatives, noun false positives. Borderlines re-checked and rejected: [58] nesselrode-v7 @396326 (dialogue label), [86] rdm-q1 @33995 (topic of a finite clause), [103] rdm-q1 @1332013 ("Moi, voler!" — bare, out of bar), [106] rdm-q1 (complement, force not on the infinitive).

## Per-clause pass/fail

1. **C1: PASS.** 0 genuine across 295 candidates (26 parent + 269 new) under 400-char windows with '!'/'?' termination. The prose zero is not a window/termination artifact.
2. **C2: PASS (vacuous).** No genuine tonic-topic + governed exclamatory infinitive found; nothing re-opens. The licensor class stays closed register-wide.

## Verdict

**NULL** — confirmed zero at recall depth, not a refutation (§4: zero is an absence, not a kill). The reinforced fence now stands on a 295-candidate prose base (parent 26 + recall 269), alongside the 356-candidate drama recall base at register level, 0 genuine in both registers. The recall gap for window size and '?'-termination is closed for prose.

## Follow-ups proposed (nulls regenerate work; all three verified ABSENT from queue)

1. **personal-tonic-governed-interr-prose (P3)** — interrogative-force variant. The widened net caught many rhetorical finite questions; the bar tested only exclamatory force. Run a targeted census for tonic-topic + pour/de/a-governed infinitive terminated by '?' where the question force plausibly falls on the infinitive itself ("Moi, pour quoi faire ?"): ≥1 genuine names the interrogative shape; 0 genuine closes the force dimension.
2. **prose-drama-gov-excl-rate-diff (P4)** — distributional rate comparison. Candidate density differs by register (prose recall 295/4,495 hits ≈ 6.6%; drama parent 29/2,971 ≈ 1.0%). Formal test: is governed-exclamatory candidate density register-dependent? A significant difference would fence the null by register; no difference strengthens the cross-register fence.
3. **personal-tonic-governed-inf-negation-prose (P4)** — negation-scoped subclass. Scan tonic-topic + governed infinitive windows that contain negation ("ne ... pas") with '!'/'?' termination: emphasis constructions may license the shape where plain ones do not ("Moi, pour ne pas rire !"). ≥1 genuine re-opens the negation subclass; 0 genuine keeps it closed.

## Standing items

- R5005, sealed gates, red-team adjudication queue: untouched.
- Standing §7 values (banked/promoted/kills/splits/holds): untouched, none contradicted.
- `canonical.py` never used; repaired 1,847-pair stream not applicable here (corpus battery, caveat stands).
- Lock created on start (2026-10-09T15:12:00Z), deleted on completion.
- No stale-lock issue: no prior lock existed for this id.
