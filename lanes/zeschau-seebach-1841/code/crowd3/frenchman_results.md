# LE FRANÇAIS — ear-check round 3 (Seebach R5005)
## Contrôle à l'oreille des valeurs candidates — French ear-check of candidate values

**Travail demandé :** lire les fenêtres partiellement déchiffrées *en français*, pas en statisticien.
**Task:** read the partially-decoded windows *as French*, not as a statistician.

**Convention de décodage / decoding convention** (décodeur : `code/crowd3/frenchman_dump.py`) :
- valeur sûre (pencil cribs) en clair : `la`, `ne`, `qui`… / ground truth plain
- valeur provisoire entre crochets : `[ce]`, `[qui]`, `[par]`, `[ne]` / provisional in [brackets]
- groupe inconnu = son numéro : `24`, `52`… / unknown = group number
- la position citée est celle du groupe cible dans le flux de 1846 paires / cited position = target group index in the 1846-pair stream

**Valeurs appliquées / values applied :** 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (sûres) ; 87=[ce], 64=[qui], 96=[par], 94=[ne] (provisoires).

**Note d'autorité / authority note :** la red-team (kill authority) a rétrogradé 87=« ce » à PROVISIONAL après le closer. Mes « CONFIRMÉ À L'OREILLE » ci-dessous sont des verdicts d'oreille indépendants, pas des promotions de statut — le statut lane reste celui de la red-team. / The red team demoted 87="ce" to PROVISIONAL; my "EAR-CONFIRMED" verdicts are independent ear findings, not status promotions — lane status follows the red team.

---

## 1. VERDICTS PAR VALEUR / PER-VALUE EAR VERDICTS

### 87 = « ce » — CONFIRMÉ À L'OREILLE / EAR-CONFIRMED ✓✓✓
*(32 occurrences ; je les ai toutes lues)*

**Ce qui sonne juste / what rings true :**
- `@225 : 42 16 24 89 61 [par] [ce] que 98 83 m [par] 21` → « …**parce que** 98… » — *« parce que » en trois groupes, verrou grammatical.* / "parce que" in three groups — a grammatical lock. Idem @951/@952 et @1525/@1526 : **« parce que » ×3**, à l'identique.
- `@180 : …14 24 [ce] [qui] 23…` → « …**ce qui** 23… » — *le relatif, parfait.* / the relative pronoun, perfect. Idem @1799 (`79 [ce] [qui] 77`), @1767, @1775, @1800 : **« ce qui » ×5**.
- `@163 : …[ce] la 24 m…`, `@201 : 76 [ce] la 92`, `@1241/@1402 : 81 [ce] la…` → « …**cela** … » ×7 — *le démonstratif, naturel.* / the demonstrative, natural.
- `@73 : 69 13 24 56 [ce] 14 24 [ce] la 00 la er 42` → « …13 **en plus, ce** 14 **en cela**… » — *« De/en plus, ce 14… » : transition administrative impeccable ; « en cela » (en + cela) est du français de rapport.* / "Furthermore, this 14… in that…" — flawless administrative transition.
- `@179 : …14 24 [ce] [qui] 23…` et `@1765 : …09 24 [ce] [qui] 26…` → « …**en ce qui** [verbe]… » — *la formule bureaucratique « en ce qui concerne » (verbe non identifié : `23 37 06`, pas proprement « concerne »).* / the bureaucratic formula "as regards…" (verb unidentified).

**Ce qui accroche / what jars :** rien de fatal. `@868 : …00 86 pre [ce] 77 89…` → « …pré**[ce]** 77… » — *soit le mot « précéder/précédemment » (87 = « cé » interne au mot), soit une coquille de segmentation ; à signaler, pas à tuer.* / either the word "précéder" (87 as word-internal "cé") or a segmentation slip — flagged, not killed.

**Verdict :** *L'oreille confirme indépendamment des statistiques : trois « parce que » byte-identiques, c'est une preuve grammaticale, pas un taux. (Statut lane : PROVISIONAL par décision red-team — cf. note d'autorité ; la red-team bloque aussi la re-promotion de 64 sur une anomalie 64→77×3 que mon oreille lit comme « qui [verbe] », verbe non identifié.)* / The ear confirms independently of statistics: three byte-identical "parce que" are grammatical proof, not a rate. (Lane status: PROVISIONAL per red team; red team also blocks 64 re-promotion on a 64→77×3 anomaly my ear reads as "qui [verb]", verb unidentified.)

### 64 = « qui » — CONFIRMÉ À L'OREILLE / EAR-CONFIRMED ✓✓✓
*(46 occurrences ; toutes lues)*

**Juste :**
- « **ce qui** » ×5 (@180, @1767, @1775, @1800, @1772) — *le relatif après démonstratif, parfait.*
- `@290 : …09 [qui] er e 65 16 01 la` et `@684 : …92 [qui] er e 65 [ne] er 60` → « …**qui erre** 65… » ×2 — *« qui » + « erre » (il erre = il se trompe/s'égare) : 29=er + 40=e composent le verbe, la segmentation er|e est celle du chiffreur.* / "qui" + "erre" (he errs/wanders): er|e composes the verb under the encipherer's segmentation.
- `@676 : …03 [qui] 37 77…`, `@938` et `@1632 : …21 [qui] 37 01…` (×2) → « …**qui le** [verbe]… » — *« qui le 77/01 » : relatif + pronom objet + verbe, parfait (« qui le dit/fait »).* / relative + object pronoun + verb, perfect.
- `@790 : …77 [qui] que 07 [qui] 56…` → « …**qui que** 07… » — *« qui que » + subjonctif (« qui que ce soit ») : tour littéraire, très 1841 soutenu.* / literary "whoever" + subjunctive — high 1841 register, not a fault.
- `@508 : …77 62 [ne] [qui] 98…` → « …**personne, qui** 98… » — *« personne qui [verbe] », impeccable.* / "nobody who…" — flawless.
- `@1078 : …77 78 [qui] 06 52…`, `@1665 : …84 [qui] 06 91 la…` → « …**qui** [base-verbale]… » — ***« qui » exige un verbe conjugué ; 06 se comporte en base verbale, pas en « ent »** (voir §6, kill de 06=« ent »).* / "qui" demands a conjugated verb; 06 behaves as a verb stem, not "ent".

**Accrocs :**
- `@148–150 : …84 er [ce] [qui] [par] 47 que 66 84…` → « …**ce qui par 47 que**… » — *ne se lit pas : après « ce qui », « par 47 » ne donne aucun verbe en « par- » gouvernant « que » (« parle que », « paraît que » sans « il » : impossibles). C'est un problème de **47**, pas de « qui » — 47 est la plus grosse inconnue du voisinage.* / unreadable: no "par-" verb governs "que" there. A 47-problem, not a qui-problem — 47 is the biggest unknown in this neighborhood.
- `@725 : …65 [qui] la 00 86…` → « …**qui la** 00… » — *secouru par « qui **l'a** 00 » (« qui l'a dit/fait ») si 11=la fait aussi « l'a » ; sinon heurt.* / rescued by "qui l'a 00" ("who has/saw it done") if 11 doubles as "l'a"; else a jar.
- `@1773 : …62 [ne] 24 [ce] [qui] 59…` → « …**ne 24 ce qui**… » — *pas d'analyse propre (« ne de/en ce qui » impossible) ; heurt léger.* / no clean parse; mild jar.

**Verdict :** *« qui » tient dans tous ses emplois relatifs (sujet, « ce qui », « qui que », « qui le »). Les deux vrais accrocs viennent des voisins (47, 24), pas du pronom.* / "qui" holds in every relative use; both real jars come from neighbors, not the pronoun.

### 96 = « par » — CONFIRMÉ À L'OREILLE / EAR-CONFIRMED ✓✓
*(21 occurrences)*

**Juste :** « **parce que** » ×3 (@224–230, @951, @1525) — *verrou.* / lock. « **par** [nom] » partout ailleurs : @131 `32 [par] 56 [qui]` (« par 56, qui… »), @465 `42 [par] 00`, @602 `39 26 [par] 45`, @846 `33 [par] e 62` (« par e… » = « par écrit/effet/erreur »), @913, @926, @959, @997 `67 la [par] m 33` (« par m… »), @1062, @1212, @47, @1785 — *chaque fois « par » + nom, rien d'agrammatical.* / every time "par" + noun, nothing ungrammatical.

**Accrocs :**
- `@1195 : 59 que 07 24 m 16 [par] m 16 [qui] er 45 58` → « …**m 16 par m 16** qui… » — *redoublement « X par X » : en français ce moule n'existe guère que pour les nombres (« un par un », « deux par deux ») ; ici X = « m 16 », inexpliqué. Heurt non résolu — mais c'est 16 le problème, pas « par ».* / "X par X" reduplication exists in French almost only for numbers ("one by one"); here X = "m 16", unexplained. Unresolved jar — but 16's problem, not "par"'s.
- `@148–150` : voir §64 — le « par 47 que » ; problème de 47.

**Verdict :** *« par » est solide (« parce que » ×3 suffit). Le seul heurt sérieux est une énigme de voisinage.* / "par" is solid ("parce que" ×3 suffices). The one serious jar is a neighborhood puzzle.

### 94 = « ne » — CONFIRMÉ À L'OREILLE, AVEC DEUX LECTURES CONDITIONNÉES / EAR-CONFIRMED, WITH TWO CONDITIONED READINGS ✓✓
*(36 occurrences ; le morphologue l'avait confirmé statistiquement — l'oreille contrôle)*

**Juste :**
- `@1331 : 56 30 06 62 [ne] pre 52 39 83 86 71 [qui] 60` → « …62 **[ne] pre** 52… » = « …**on ne prend pas** 39… » — ***la négation complète, avec « prend » écrit « pre » (le d muet tombe : le chiffreur écrit au son).** C'est la plus belle fenêtre du lot.* / "…on ne prend pas…" — the full negation frame, with "prend" spelled "pre" (silent d dropped: the encipherer spells by ear). The finest window in the batch.
- `@1293` et `@1806 : …35 [ne] 52 80 04…` (×2, byte-identique) → « …**ne pas** 80… » — *« ne pas » + infinitif (« ne pas 80 »), construction soutenue, parfaite.* / "ne pas" + infinitive — formal, perfect.
- `@318 : …59 32 [ne] 06 la 92…` → « …**ne** [base] **la**… » — *« ne » + verbe + « la » (« ne [dit] la ») : 06 est verbal ici, pas « ent ».* / "ne" + verb + "la" — 06 is verbal here.
- `@578/@1181/@1352 : …77 78 [ne] m 06…` → « …**gouvernement**… » — *le trigramme, meilleur déchiffrement disponible.* / the trigram — best available parse.
- « **ne** [verbe] » simple : @65, @101, @250, @349, @494, @558, @699, @784, @840, @1101, @1548, @1686, @1700, @1794 — *rien d'anormal.* / all normal.
- `@160 : …93 52 [ne] 24 [ce] la…` → « …**personne** 24 cela… » — *« per|so|nne » : 94 = « ne » interne au mot, pas la négation. Le chiffreur découpe n'importe comment (cf. « pers|on|ne » en @508) — voir Illumination.* / "personne": 94 as word-internal "ne". The encipherer's cuts are sloppy.
- `@509 : …62 [ne] [qui] 98…` et `@510 (voisin)` → « …**[donn]e, qui** 98… » / « …**personne, qui**… » — *« ne » final de mot + relatif, pas la négation.* / word-final "ne" + relative, not negation.

**Lectures conditionnées (l'oreille rejoint le morphologue : « ne » partout, « en » par endroits) / conditioned readings :**
- `@1168 : …61 [ne] [ce] 83 21…` → « …61 **[ne] ce** 83… » — *« ne ce 83 » heurte ; « **en ce** 83 » (= « en ce moment/cas ») coule.* / "ne ce" jars; "en ce" ("at this moment") flows. → **94 = « en » ici.**
- `@1575 : …52 m [ne] 76 47…` → « …52 **m'[ne]** 76… » — *« m'en 76 » (« je m'en 76 ») coule ; « m'ne » n'existe pas.* / "m'en" flows; "m'ne" doesn't exist. → **94 = « en » ici** (l'anomalie « m'en » du morphologue).
- `@1741 : …12 i [ne] m que 56…` → « …**i ne m que**… » — *illisible dans les deux lectures (« i en m que » pas mieux). La pire fenêtre de « ne » ; irrésolue, pas fatale (1/36).* / unreadable under both readings. Worst "ne" window; unresolved, not fatal.

**Verdict :** *« ne » est confirmé à l'oreille (la négation « on ne prend pas » est un verrou grammatical). Deux îlots « en » (« en ce », « m'en ») : polyvalence conditionnée, pas réfutation.* / "ne" ear-confirmed ("on ne prend pas" is a grammatical lock). Two "en" islets: conditioned polyvalence, not refutation.

### 06 — L'OREILLE TRANCHE LA TENSION / THE EAR SETTLES THE TENSION
*(R4 « ent » vs F21 base verbale — le morphologue laissait coexister les deux)*

*« Ent » comme lecture générale est impossible à l'oreille :*
- `@1078 : …77 78 [qui] 06 52…` → « …**qui ent** 52… » — *impossible : « qui » veut un verbe.* / impossible: "qui" wants a verb.
- `@1665 : …84 [qui] 06 91 la…` → « …**qui ent** 91… » — *idem.*
- `@318 : …32 [ne] 06 la…` → « …**ne ent la**… » — *impossible.*
- `@578 : …61 [ne] m 06 06…` → « …**ne m'ent** 06… » — *« ne m'ent » n'existe pas ; « ne m'[base] » oui.*
- `@758 : …42 [ne] 02 06 er 45…` → « …02 **[ent]er**… » — *« enter » n'existe pas ; « 02[base]er » (infinitif) oui.*

*« Ent » restreint aux 3 trigrammes survit : « 77 78 [ne] m 06 » = « gouvernement » reste le meilleur déchiffrement (@578, @1181, @1350). Et @1181 : « …gouvernement **06** 59… » — le 06 **suivant** le trigramme doit être une base verbale (« le gouvernement [décide] »), pas « ent » : **c'est la polyvalence vue à l'oreille nue** (le même groupe, deux lectures selon la place).*

**Verdict :** *KILL de 06=« ent » général (l'oreille rejoint la réfutation statistique, par une voie indépendante) ; « ent » survit seulement dans les 3 « …nement » ; partout ailleurs 06 = base verbale.* / KILL 06="ent" as a general reading (ear reaches the statistical refutation by an independent road); "ent" survives only in the three "…nement"; elsewhere 06 = verb stem.

---

## 2. FORMULES ÉTABLIES À L'OREILLE / FORMULAE ESTABLISHED BY EAR

- **« parce que »** = 96 87 46, ×3 (@225, @951, @1525), byte-identiques. *Verrou.* / Lock.
- **« ce qui »** = 87 64, ×5 (@180, @1767, @1775, @1799, @1800). *Verrou.* / Lock.
- **« cela »** = 87 11, ×7. *Le démonstratif du rapport.* / The report's demonstrative.
- **« en ce qui [verbe] »** = 24 87 64 …, ×2 nets (@179 : `…14 24 [ce] [qui] 23…`, @1765 : `…09 24 [ce] [qui] 26…`) + @1773/@1771 en variante. *La formule bureaucratique « en ce qui concerne » (tête certaine, verbe non identifié).* / The bureaucratic "as regards…" (head certain, verb unidentified).
- **« on ne prend pas »** = 62 94 70 52, @1331 (`56 30 06 62 [ne] pre 52 39 83 86 71 [qui] 60`). *Négation complète + orthographe phonétique (« prend » → « pre »).* / Full negation + phonetic spelling.
- **« ne pas [infinitif] »** = 94 52 80, ×2 byte-identiques (@1293, @1806 : `…35 [ne] 52 80 04…`). *Construction soutenue.* / Formal construction.
- **« la première [17] »** = 11 70 82 34 29 40 17, @1033 (`[ce] 01 03 er 80 77 la pre m i er e 17`). *« la première fois » si 17=« fois » (piste, une seule fenêtre).* / "la première fois" if 17="fois" (lead, single window). *Noter le découpage hyper-fin « pre|m|i|er|e » : le chiffreur descend jusqu'à la lettre.* / Note the hyper-fine cut "pre|m|i|er|e": the encipherer goes down to single letters.
- **« [qui] par 43 c'est »** = 64 96 43 87 01, ×2 (@343, @1026) — *« c'est » (87+01, cf. @295 « 16 est la ») est solide ; « par 43 » = « par [nom] » (« par exemple/hasard/ailleurs ») ; « parmi » est écarté (ne se combine pas avec « c'est »).* / "c'est" solid; "par 43" = "par [noun]"; "parmi" ruled out here.

---

## 3. KILLS PRONONCÉS À L'OREILLE / EAR KILLS
*(construction agrammaticale nommée à chaque fois / ungrammatical construction named each time)*

| # | Tué / Killed | Construction fautive / faulty construction | Fenêtre / window |
|---|---|---|---|
| K1 | 06=« ent » **général** | « qui ent », « ne ent la » : « qui »/« ne » exigent un verbe, « ent » n'en est pas un | @1078 `@...77 78 [qui] 06 52...`, @1665, @318, @578, @758 |
| K2 | 24=« de » (dans « en ce qui ») | « de ce qui concerne » : « de » + « ce qui » est agrammatical | @179, @1765 |
| K3 | 43=« mi » (« parmi ») **dans la formule** | « parmi c'est » : « parmi » ne se combine pas avec « c'est » (87 01 = « c'est », §4) | @343, @1026 |
| K4 | 01=« ci » (« ceux-ci ») | fréquence 1,57 % trop haute pour « ci » ; « 34 01 » = « ici » ×0 ; @295 exige « est » | @295 `...65 16 01 la 78...` = « 16 **est** la 78 » |
| K5 | 52=« pas » **en lecture unique** | @160 `...93 52 [ne]...` = « per**so**nne » : 52 = « so » interne au mot ⇒ 52 fait autre chose que « pas » | @160 |
| K6 | « ce n'est pas cela » @163 (ma propre fausse piste) | « ce **ne pas** cela » : il manque « est » — *je m'étais laissé séduire, l'oreille a corrigé* | @163 `...52 [ne] 24 [ce] la...` |
| K7 | 56=« plus » **en lecture unique** (tension) | @795 `...[qui] 56 37 44...` = « qui **a** le 44 » : 56 = verbe « a » ici, pas « plus » | @795 vs @73 |

*Non tués mais en sursis / not killed but on notice : 87=« ce » (le « précé[ce] » de @868 : « cé » interne ?), 64=« qui » et 96=« par » (l'énigme « par 47 que » de @148–150 vient de 47, pas d'eux).*

---

## 4. COMPLÉTIONS PROPOSÉES — PISTES, PAS PROMOTIONS / PROPOSED COMPLETIONS — LEADS, NOT PROMOTIONS

| Piste / lead | Fenêtre reine / crown window | Idiome cité / idiom cited | Force |
|---|---|---|---|
| **24 = « en »** | @179 `…14 24 [ce] [qui] 23…` = « en ce qui… » ; @73 « en plus, ce 14, en cela » | « en ce qui concerne », « en plus », « en cela », « qu'en 85 » (@952) | FORTE — 24 est au rang 2 (2,82 %) : « en » colle en fréquence |
| **52 = « pas »** | @1331 « on ne **prend pas** » ; @1293/@1806 « ne **pas** [inf] » ×2 | la négation « ne…pas », « ne pas » + infinitif | FORTE (K5 : pas en lecture unique — « personne ») |
| **62 = « on »** | @1331 « **on** ne prend pas » ; @100 `…21 62 [ne] 93…` = « on ne [verbe] » ; @839, @1361, @1685, @1703 idem | « on ne [verbe] » ×5 | FORTE — et @508 « pers**on**ne, qui… » (« pers|on|ne » : 62=« on » aussi dans le mot !) |
| **37 = « le »** | @1178 `…59 37 77 78 [ne] m 06` = « …**le gouvernement**… » ; @676 « **qui le** 77 » ; @938/@1632 « **qui le** 01 » ×2 | « le » article, « qui le [verbe] » | MOYENNE — tension : @529/@1356/@1443 « 37 [qui] » = « ce/celui qui », pas « le » |
| **01 = « est »** | @295 `…65 16 01 la 78…` = « 16 **est** la 78 » (« 16 is the 78 ») | « est », et « c'est » = 87+01 dans la formule §2 | MOYENNE |
| **56 = « plus »** | @73 `…24 56 [ce]…` = « **en plus**, ce 14… » | « en plus » / « de plus » | MOYENNE (K7 : 56=« a » en @795 — polyvalence ou erreur) |
| **43 = « me »** | @43 `…88 43 81…` = « il **me** [verbe] » ; @439 `…que 43 98…` = « que **me** [verbe] » | pronom objet « me » + verbe | MOYENNE — dans la formule, 43 = autre chose (« par [nom] ») |
| **17 = « fois »** | @1033 « la première **17** » | « la première fois » | FAIBLE — une seule fenêtre, à confirmer |
| **« pre » = « prend »** | @1331 « ne **pre**nd pas » (le d muet tombe) | orthographe phonétique du chiffreur | indice méthodologique, pas une valeur |
| **« en ce qui concerne »** | @179, @1765 (tête 24 87 64 certaine) | la formule diplomatique | tête FORTE, verbe (`23 37 06`) non identifié |

---

## 5. REGISTRE — L'OREILLE DU MINISTRE / REGISTER — THE MINISTER'S EAR

*Le chiffre parle d'un ministre (ou de son secrétaire) qui rend compte de Dresde à Saint-Pétersbourg. Voici ce que l'oreille y entend :*

**Marqueurs de français administratif soutenu / markers of formal administrative French :**
- « **en ce qui** [concerne] » — *la cheville bureaucratique par excellence.* / the bureaucratic filler par excellence.
- « **de plus**, ce 14… » — *transition de rapport.* / report transition.
- « **ne pas** » + infinitif ×2 — *construction de chancellerie.* / chancery construction.
- « **qui que** » + subjonctif (@790) — *tour littéraire.* / literary turn.
- Négations **pleines** (« on ne prend pas ») : aucun « ne » tombé, aucun « ça », aucune interjection — *l'écrit, pas l'oral.* / full negations, no dropped "ne", no "ça" — written, not spoken.
- Sujet : **le gouvernement** — *on rend compte de politique.* / reporting on politics.

**L'écart de registre (« cela » au taux du dialogue des Misérables) — mon explication / the register gap explained :**
*« Cela » n'est pas ici familier : c'est l'anaphore du rapporteur — « cela » = « ce qui vient d'arriver / ce que je viens de décrire ». Dans un compte rendu d'événements politiques, l'anaphore événementielle fait mécaniquement monter « cela », exactement comme dans du dialogue romanesque où « cela » reprend ce qui vient de se dire. L'écart est un effet de **genre** (reportage vs essai), pas de **tenue** (soutenu vs familier).*
/ "Cela" here isn't informal: it's the reporter's anaphora — "cela" = "what just happened / what I just described". In political event-reporting, event anaphora mechanically inflates "cela", exactly as in novelistic dialogue where "cela" picks up what was just said. The gap is a **genre** effect (reportage vs essay), not a **formality** effect.

**Verdict de registre :** *français de dépêche, soutenu et posé — ni familier, ni pressé. Attendre : lexique politique (gouvernement, ministre, chambre, loi, élection, parti), formules diplomatiques (« j'ai l'honneur de », « votre excellence »), subjonctifs après « que », négations pleines. Ne pas attendre : argot, « ça », « ne » élidé, exclamations.*
/ Despatch French, formal and unhurried — neither familiar nor rushed. Expect: political lexicon, diplomatic formulae, subjunctives, full negations. Don't expect: slang, "ça", dropped "ne", exclamations.

---

## 6. OÙ L'OREILLE A CONTREDIT OU CONFIRMÉ LES STATISTIQUES / WHERE THE EAR OVERRULED OR CONFIRMED THE STATISTICS

1. **87=« ce » : l'oreille CONFIRME, par une voie indépendante** *(statut lane : PROVISIONAL — la red-team a rétrogradé la promotion du closer pour rupture de traçabilité (B1), corroboration invalide (B2), jambe circulaire (B3) et jambe « cela » défaillante (B4) ; mon verdict d'oreille ne change pas le statut).* *Les statistiques tuaient les rivaux un par un ; l'oreille apporte le verrou positif : trois « parce que » byte-identiques, cinq « ce qui », sept « cela ». Sur le point faible (taux de « cela » « dialogue ») : l'oreille le reclasse en effet de genre, pas en objection. Noter : la red-team signale une anomalie 64→77×3 contre la re-promotion de 64=« qui » — mon oreille lit « qui 77 84 » comme « qui [verbe] » (grammatical, verbe non identifié) et ne tranche pas.*
2. **06=« ent » général : l'oreille TUE, indépendamment.** *Le morphologue tuait par la phase et 06→29 ; l'oreille tue par la grammaire (« qui ent », « ne ent la » impossibles). Deux instruments, même verdict — et l'oreille ajoute le mécanisme visible : @1181 « gouvernement **06** » montre les deux lectures côte à côte (polyvalence à l'œil nu).*
3. **94=« ne » : l'oreille CONFIRME le morphologue** *et résout ses deux anomalies en lectures conditionnées : « m'en » (@1575 : « je m'en 76 ») et « en ce » (@1168 : « en ce moment ») se lisent naturellement — ce sont des îlots « en », pas des réfutations.*
4. **24=« en », 52=« pas », 62=« on » : l'oreille SEULE propose** *(les statistiques ne les avaient pas) — trois pistes fortes nées de formules (« en ce qui », « on ne prend pas », « ne pas [inf] »), pas de taux.*
5. **L'illumination / the aha : le chiffreur écrit au son et découpe n'importe comment.** *« prend » → « pre » (@1331), « personne » en « per|so|nne » (@160 : 93 52 94) puis « pers|on|ne » (@508 : 77 62 94), « erre » en « er|e » (@290/@684), « première » en « pre|m|i|er|e » (@1033). Deux orthographes du même mot dans le même chiffre ! C'est pourquoi les statistiques de position syllabique patinent (l'échec LOO du tuner, F22) : la segmentation du chiffreur est inconsistante, et l'oreille — qui tolère ça — devient le meilleur instrument. La bande « facteur 2 » n'est pas le problème ; la rigidité syllabique, si.*
6. **Auto-correction / self-correction :** *j'avais lu @163 comme « ce n'est pas cela » (52=« ce », 24=« pas ») — l'oreille a tué sa propre lecture : il manque « est » (« ce ne pas cela » est agrammatical). Cas d'école : une belle formule ne vaut rien s'il manque un mot.*
7. **« parmi ceux-ci » : l'oreille DÉTRUIT sa propre première lecture** *de la formule ×2 (@343/@1026) : 01=« est » (@295 « 16 est la ») donne « c'est », qui ne se combine pas avec « parmi ». Reste « [qui] par [nom] c'est » — nœud signalé au lane-43.*

---

## 7. PROCHAINE ÉTAPE / BEST NEXT STEP

1. **Tester 24=« en », 52=« pas », 62=« on » au second instrument** — *mes trois pistes fortes ; chacune mérite une vérification indépendante (taux d'époque, géométrie des voisins) avant toute promotion. Surtout 52=« pas », déjà borné par « personne ».*
2. **Résoudre 47** — *« …ce qui **par 47** que… » (@148–150) est le plus gros heurt du voisinage « qui/par » ; 47 est le verrou qui bloque trois fenêtres.*
3. **Exploiter l'orthographe phonétique** — *relancer les dragues avec une syllabation lâche/phonétique (« prend »→« pre », « erre »→« er|e ») : la segmentation rigide est prouvée inconsistante par « personne » ×2 orthographes.*
4. **Lane-43 : « [qui] par [43] c'est »** — *la formule ×2 attend son nom (@343/@1026) ; candidats « par exemple / par hasard / par ailleurs / par contre ».*

## 8. RÉSERVES / CAVEATS

- *Je n'ai lu que les fenêtres autour de 87/64/96/94 (±6–8 paires) + les formules connues : ~140 fenêtres, pas le chiffre entier.*
- *Les « complétions » sont des lectures de français, pas des déchiffrements : 24, 52, 62, 37, 43, 01, 17 restent des PISTES (une seule vérification : mon oreille).*
- *La polyvalence (06, 52, 56, 43…) peut aussi être de la variation allophonique du chiffreur (même syllabe, plusieurs groupes — cf. « personne » ×2) : l'oreille ne distingue pas les deux.*
- *Autorité : mes « CONFIRMÉ À L'OREILLE » sont des verdicts d'oreille indépendants, pas des promotions — la red-team (kill authority) a rétrogradé 87=« ce » à PROVISIONAL (B1–B4) et bloque la re-promotion de 64 ; je ne conteste pas.*
- *Aucune poussée GitHub, aucune prétention de cassage. Les nombres cités viennent de `crib_attack.load_pairs` (1846 paires).*
