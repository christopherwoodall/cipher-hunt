# Battery report: disloc-comedy-governed-inf

- Target id: `disloc-comedy-governed-inf`
- Claim: "governed-shape exclamatory-infinitive census in the comedy corpus (preposition-governed 'à être malade, à se tuer !' shape)"
- Date: 2026-10-09
- Worker: battery worker (subagent 71f819f3-b4bc-4b0e-8264-831fdbbfacc6)
- Stream: not applicable — corpus census against period French comedy, per target charter (same taxonomy as parent batteries). The 1,847-pair repaired parse was not used. R5005, sealed gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "governed exclamatory infinitive" = an infinitive governed by a preposition (pour / à / de) used as an exclamation in its own right ("pour rire !" = the infinitive phrase IS the exclaimed element). "Genuine attestation" = the "!" terminates the governed infinitive phrase itself; the infinitive is not embedded in a finite matrix clause whose "!" belongs to the matrix, and not embedded in an exclaimed noun phrase (per battery-gov-excl-inf-register-drama's definitions, read before testing).

## Parentage

Follow-up #2 of the NULL `disloc-comedy-bare-heads-extension` (2026-10-09), which fenced the BARE demonstrative + bare exclamatory infinitive shape in comedy (0 genuine in 465,531 chars) but flagged the nearest near-miss at scribe-le-savant.txt @4840 ("à être malade, à se tuer !" — preposition-governed). This battery tests whether the fence holds exactly at BARE or generalizes to the governed shape, mirroring `gov-excl-inf-register-drama`'s register-boundary logic (that battery found 1 genuine governed exclamatory infinitive in drama — "Pour conspirer !" — and located the register boundary there).

## Corpus

The 6 comedy-extension files censused by the parent battery (465,531 chars, 3,835 "!", verified in-session):

| file | chars | "!" | candidates |
|---|---|---|---|
| `labiche-29-degres-ombre.txt` | 34,634 | — | — |
| `labiche-affaire-rue-lourcine.txt` | 43,172 | — | — |
| `labiche-la-cagnotte.txt` | 134,353 | — | — |
| `labiche-voyage-perrichon.txt` | 97,395 | — | — |
| `scribe-le-lorgnon.txt` | 67,028 | — | — |
| `scribe-le-savant.txt` | 88,949 | — | — |
| **Total** | **465,531** | **3,835** | **217 (141 tight)** |

Scope note: the 4 other comedy-authored files in the corpus (scribe-bertrand-et-raton, scribe-verre-d-eau, labiche-chapeau-de-paille, labiche-martin-poudre-aux-yeux) are EXCLUDED with cause — `gov-excl-inf-register-drama` censused them as drama and found its 1 genuine ("Pour conspirer !") there; including them would double-count the drama finding as a comedy attestation.

## Bar (verbatim, pre-registered before testing)

">=1 genuine in comedy tests whether the fence holds exactly at BARE (mirroring gov-excl-inf-register-drama's register-boundary logic); confirmed zero fences the governed shape in comedy too"

Numbered pass/fail clauses (restated before testing, not modified after):

1. ≥1 genuine governed exclamatory infinitive (pour / à / de + infinitive as the exclaimed element, any topic) exists in the 6 comedy texts → the fence holds exactly at BARE: the pairing is bounded at the bare-demonstrative-headed shape, not the whole exclamatory-infinitive family (promote).
2. If clause 1's census is a confirmed zero — every candidate window classified, false friends excluded with cause — the governed shape is fenced in the comedy register too (null per §4: zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/disloc-comedy-governed-inf.lock` on start (agent id + UTC timestamp 2026-10-09T08:59:54Z; no prior lock for this id); will delete on completion.
2. Ran `code/crowd17/next-token/disloc_comedy_governed_inf_census.py` (re-runnable, patterns verbatim from `gov_excl_inf_register_drama_census.py`):
   - P1 (candidate): for every "!" in the corpus, take the 120 chars before it; run `\b(pour|à|a|de|d[''])\s+(?:[a-z...]{1,6}\s+){0,2}\b[a-z...]{2,}(er|ir|re|oir)\b` (case-insensitive); keep the match closest to the "!"; between its end and the "!" there must be no [.;].
   - P2 (banding): dist = chars from the end of the infinitive-shaped word to the "!". Tight band dist ≤ 40 (141 candidates) is the discriminating band; wide band 41 ≤ dist ≤ 120 (76 candidates) triaged separately.
   - Raw results: `code/crowd17/next-token/disloc-comedy-governed-inf_census.json`.
3. All 217 candidates hand-classified (regex cannot separate -er infinitives from nouns/adjectives, nor judge exclamatory force or topic status).

## Window-level evidence

### Census yields

- **217 candidates (141 tight, 76 wide) from 3,835 "!" in 465,531 chars.**
- **1 of 217 candidates is genuine.** All 217 classified below.

### The genuine attestation (tight band, dist 1)

- `labiche-voyage-perrichon.txt` char offset 76843 — "Pas pour être témoin !…" The full exchange verbatim:
  - MAJORIN: "Il faut que j'aille à mon bureau… je me ferais destituer."
  - PERRICHON: "Puisque tu as demandé un congé."
  - MAJORIN: "Pas pour être témoin !… On leur fait des procès, aux témoins !"
  - Majorin's turn is a standalone negated purpose exclamation: the "!" terminates the pour-infinitive phrase itself. No finite matrix clause in his turn; not embedded in an exclaimed noun phrase. Zero topic (the anaphor is Perrichon's "tu as demandé un congé"). It is a denial/protest exclamation ("Not to be a witness!"), with the governed infinitive phrase as the exclaimed element — exactly the "pour rire !" shape, mirroring the drama battery's genuine "Pour conspirer !" (which was also an ironic/elliptical zero-topic turn).
- Note: the census produced two candidates for this one utterance ([50] dist=1, [154] dist=48) — same attestation, counted once.

### The 216 exclusions (by confound class, per the parent/drama taxonomies)

**Finite-matrix-governed (dominant confound class, ~55):** the infinitive is the complement of a finite verb and the "!" belongs to the matrix — e.g. [0] "Il ne manquerait plus que de le nourrir !"; [2] "je n'aurais rien à dire !"; [9] "J'ai hâte de la lire !"; [10] "je le déciderai bien à partir !"; [16] "je vous somme de vous expliquer !"; [20] "prenez donc la peine de vous asseoir !"; [21] "quand vous passerez votre temps à geindre ou à rager !"; [22] "nous ne pouvons pas perdre notre journée à vous attendre !"; [25] "a manqué de se tuer !"; [30] "de vous en débarrasser" (être agréable); [34] "c'eût été à moi de me battre, de me faire tuer !"; [35] the parent's near-miss — "Voyez où cela le mène : à être malade, à se tuer !" ("cela" = subject of finite "mène"; "!" terminates the matrix sentence); [49] "ils ont donc passé tout leur temps à se sauver la vie !"; [52] "Vous ne pouvez pas m'obliger à aller à Paris !"; [55] "Je n'aime pas à verser le sang !"; [60] "je n'aime pas à voyager comme ça !"; [74] "ça lui apprendra à ne pas acquitter les droits !"; [95] "je ne vous demande pas de repartir aujourd'hui !"; [104] "on a à épouser une jolie femme" (modal "avoir à"); [116] "je n'ai plus qu'à vous céder la place"; [118] "vous ne pouvez pas m'obliger à manger des truffes"; [121] "tu tiens à former cette chaîne"; [141] "ne craint pas de se présenter"; [147] "Je passe ma vie à lui acheter des mobiliers"; [148] "je m'engage à la prendre en sérieuse considération"; [150] "s'amusent à éplucher"; [152] "Nous convenons de manger une cagnotte"; [160] "permettez-moi de vous remercier"; [185] "nous ne pouvons tarder… à rendre réponse"; [199] "je me suis borné à constater"; [6]/[98]/[161]/[192] recent-past "venir de" ("V'là c'qui vient de paraître !", "que je viens de trouver sans connaissance !"); [71] causative "faire vider" ("On nous a fait vider nos poches !", no preposition); [176] "vous a prié de faire arrêter".

**Adjective-governed impersonal/predicative (~30):** the infinitive complements a predicative adjective, usually in a finite/impersonal matrix — e.g. [4]/[78]/[131] "Impossible de me rappeler !"; [17]/[188] "c'est très difficile à écouler !"; [40] "Effroyable ! effroyable à imaginer !"; [41] "il n'est pas nécessaire de crier ça !"; [58]/[151] "trop commode de venir déjeuner…"; [61] "j'ai eu tort de prendre mon café !" (noun "tort", finite); [67] "trop bêtes pour être dangereux"; [73] "c'est drôle de voyager comme cela !"; [75] "C'est un plaisir de vous avoir pour ennemi !"; [85] "Je suis curieux de voir ce bonhomme-là !"; [86]/[87]/[88] "que c'est donc bête de se laisser pincer comme ça !"; [96]/[177] "il m'est pénible de te voir épouser ma sœur"; [99] "je ne suis pas fâché de voir ça" (+terminator mismatch); [120] "service à me rendre" (noun-governed); [135] "Qu'il est beau d'admirer les splendeurs de la nature"; [138] "chargé de corriger"; [144] "pas sûr de ne pas retourner"; [149]/[159]/[178]/[213] "prête à accepter"; [164] "agréable de se promener"; [169] "trop salissant"; [205] "capable de redoubler".

**Noun-governed within finite clause (~20):** e.g. [9] "hâte de la lire"; [31]/[94] "le plaisir de donner une leçon"; [32] "l'honneur de vous saluer"; [66]/[139] "semblant de me coucher"; [70] "Quelle chance de vous avoir rencontré !" (exclaimed NP head "chance" — the infinitive is its complement, not the exclaimed element); [111] "l'ordre de chercher"; [153]/[158]/[175] "la permission de rester"; [165] "l'honneur de vous présenter"; [167] "La puissance de voir"; [170] "dit de faire venir"; [173]/[202] "la prétention de me donner"; [174] "le secret de multiplier et de prolonger"; [197] "l'habitude de vous fourrer"; [203] "l'honneur de vous attendre"; [216] "peine de voir".

**Purpose adjuncts of finite clauses (~15):** the governed infinitive is a purpose adjunct of a finite matrix — e.g. [3] "Prenons toujours les hardes… pour les brosser !"; [8]/[91]/[125]/[130]/[162]/[182]/[187]/[198] "il me fait : Psch ! psch !… pour me narguer !"; [82] "prêté… pour lire son feuilleton"; [97] "nous jouons pour lui bâtir sa maison d'école"; [143]/[168] "pour se faire jour dans la conscience du prévenu"; [145] "gardé la voiture… pour vous rapporter"; [156] "brûle le pavé pour me tirer des cachots"; [194] "nous partons pour voir les monuments"; [206] "pour mieux enchaîner ma délicatesse"; [212] "à venir voir la mer de Glace".

**No-true-infinitive false positives (~40):** the regex matched nouns/adjectives/determiners in -er/-re/oir — e.g. [1]/[128]/[201] "pour un baiser" (noun "un baiser" = a kiss); [5] "Quel drôle de notaire !"; [7]/[84] "celui de la charbonnière"; [11] "un fermier"; [13]/[15]/[19]/[24]/[26]/[27]/[29]/[36]/[38]/[123]/[157]/[162] "À la bonne heure !" (noun "heure"); [14] "février"; [18] "de marbre"; [23]/[110]/[115]/[135] "de la nature"; [28] "à son dîner"; [31] "grammaire"; [33]/[184] "coup de maître"; [39]/[105]/[134]/[139] "mon écriture"; [42]/[53]/[68] "tournedos à la plénipotentiaire"; [44]/[127]/[133]/[138] "pour une autre fois" ("fois" noun); [46] "pour un notaire"; [51]/[142]/[155]/[160] "notre" (determiner); [62]/[64]/[117]/[122]/[136]/[141]/[146]/[151] "la mère de Glace" (noun "mère"); [69]/[101]/[115]/[119]/[124]/[132]/[196] "votre" (determiner); [108] "montre" (noun); [114] "de la bière"; [171] "pour une heure"; [176] "faire" in "à faire" — finite "a prié de faire arrêter" (finite-matrix); [190] "à la gare"; [193] "à quelle heure".

**Terminator mismatch (~30):** the "!" belongs to a later/separate utterance — the candidate's governed infinitive does not reach the "!" — e.g. [47] "ils ont refusé de payer… voilà !"; [65] "pour me retenir… Partons !"; [66] "de me coucher… et v'lan !"; [81] "il n'y a pas à hésiter… / PERRICHON / Ah !"; [89] "C'est pour nous distraire… entre labadens !"; [90] "rien avoir à me reprocher, pas de réponse !"; [93] "à le combattre… / PERRICHON / Vrai !"; [100]/[124]/[158] "oublié de vous remettre sa carte… / DANIEL / Ah !"; [102] "vient de se produire ? / ARMAND / Tout à fait !"; [106]/[172] "Il n'y a pas à dire… j'ai fait des excuses !"; [112] "à ne pas acquitter les droits ! / PERRICHON / Ah !"; [113] "à me promener… ?… Ah !"; [122] "a beau dire" (fixed expression); [126] "on a beau dire" (fixed); [129]/[166] "à geindre ou à rager ! Nous en avons vu bien d'autres !"; [133]/[154] second "!" in a two-exclamation sequence (only the first terminates the infinitive phrase — [154] is the same genuine utterance as [50]); [140] "à rendre service… c'est une passion malheureuse !"; [149] "à accepter… / PERRICHON / Non !"; [168] "pour se faire jour… Rien ! pas un éclair !"; [180] "à me reprocher… il me fait : Psch !"; [181]/[209] "Pour abréger" (fixed discourse connector, not exclamatory); [189] "à me reprocher… Psch ! psch !"; [191] "pour toucher mon dividende… nous serons quittes !"; [200] "à voyager comme ça ! / PERRICHON / C'est le départ… !"; [204] "rien à faire… / DANIEL / Très-importante !"; [205] "capable de redoubler… ça sera bien fait !"; [206] "pour mieux enchaîner… qui ne me prouvent rien maintenant !"; [207] "arracher… / Mais, hélas !"; [210]/[215] "à partir du" (fixed compound preposition); [211] "pas de me faire auteur… un homme du monde peut avoir des pensées !".

**Adjectival/predicative "à + infinitive" (label reading, 1):** [37] "À louer !" — "à louer" is the predicative passive infinitive ("[appartement] qui est à louer"), a sign/label reading quoted aloud; no exclamatory illocutionary force on the action itself.

**Indefinite-pronoun-governed (2):** [72] "Et rien !… rien pour corrompre ce geôlier !" — the exclaimed element is "rien" (nothing), with "pour corrompre ce geôlier" as its complement; the "!" terminates a "rien"-headed phrase, not the governed infinitive phrase itself. [214] "rien à dire !… que je me fasse transpercer" — pronoun-governed + terminator mismatch.

**Fixed prepositional compounds (3):** [77] "à partir de la salade"; [210]/[215] "à partir du 5" — "à partir de" is a fixed compound preposition, not a governed infinitive.

## Per-clause pass/fail

1. **Clause 1 (≥1 genuine governed exclamatory infinitive in comedy): PASS.** "Pas pour être témoin !" (labiche-voyage-perrichon.txt @76843) is genuine: a negated standalone "pour + infinitive" exclamation with zero topic, "!" terminating the infinitive phrase itself, no finite matrix, exclamatory illocutionary force (denial/protest) — the comedy register's exact parallel to the drama register's genuine "Pour conspirer !".
2. **Clause 2 (confirmed zero):** does not fire — the antecedent is false.

## Verdict

**PROMOTE** — 1 genuine attestation in 217 candidates over 465,531 chars of comedy. The fence holds exactly at BARE: the comedy register, like drama, HAS the governed exclamatory infinitive with a non-demonstrative (here zero) topic, while the bare-demonstrative-headed shape stays fenced (parent NULL, 0/10+12). The register-boundary logic mirrors `gov-excl-inf-register-drama` (PROMOTE, 1/839 genuine in drama). No standing verdict contradicted; §7 intact; no red-team verdict touched.

## Adverses

None listed on the target.

## Follow-ups

Promote, not null — no follow-ups required. One note for the supervisor's consideration: the genuine "Pas pour être témoin !" is negated ("pas pour être témoin"); a P3 follow-up could census whether negation is characteristic of the comedy governed-shape (the drama genuine was positive "Pour conspirer !"), e.g. target `gov-excl-inf-comedy-negation` — left to the supervisor's discretion, not proposed as a mandated follow-up.

## Files

- Report: `code/crowd17/report_inbox/battery-disloc-comedy-governed-inf.md` (this file)
- Census script: `code/crowd17/next-token/disloc_comedy_governed_inf_census.py`
- Raw census JSON: `code/crowd17/next-token/disloc-comedy-governed-inf_census.json`
- Queue: `code/crowd17/next-token/battery-queue.json` — target `disloc-comedy-governed-inf` set to status `verdict`/promote via temp-file + atomic rename, own entry only, pre-write assert + post-write re-validation
