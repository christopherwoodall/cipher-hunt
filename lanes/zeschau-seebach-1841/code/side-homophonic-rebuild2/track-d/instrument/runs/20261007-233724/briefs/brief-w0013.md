# JUDGE WORKER BRIEF — Track D automated judge instrument

You are a FRENCH-FLUENCY JUDGE. This is a blind, mechanical scoring task.
Read every instruction before scoring anything.

## 0. Prompt integrity check (DO THIS FIRST)

The frozen judge prompt lives at this absolute path:

```
/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/judge_prompt.txt
```

Its expected sha256 is:

```
390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d
```

1. Compute the sha256 of that file (e.g. `sha256sum /home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/judge_prompt.txt`
   or Python `hashlib.sha256(open(path,'rb').read()).hexdigest()`).
2. If it does NOT match the expected hash, STOP IMMEDIATELY and return:

```json
{{"aborted": true, "reason": "prompt hash mismatch", "computed": "<your hash>"}}
```

3. If it matches, read the prompt text FROM THAT FILE and use it for
   all scoring below. (The prompt is also reproduced in §2 for
   reference; the file is authoritative.)

Do not score anything if the hash mismatches. This is a hard abort.

## 1. Your assignments

You will score 3 candidate(s). Each assignment is one
(candidate label, pass number, passage). The labels are blind —
they carry no information about the passage's class. Score the
passages in the order given. Judge EACH assignment INDEPENDENTLY:
do not compare candidates to each other, do not anchor on a
previous score, do not try to infer what the "right" answer is.
There is no right answer — only your honest fluency judgment.

Assignments (JSON):
```json
[
 {
  "candidate_label": "d666c7df",
  "pass_no": 3,
  "text": "La maison de l'évêque, qui avait été l'hôpital avant d'être le parloir des bourgeois, se composait d'un rez-de-chaussée et d'un étage : trois pièces en bas, trois chambres en haut, un grenier, et derrière un jardin d'un quart d'arpent. Les deux femmes logeaient au premier ; l'évêque occupait le bas, avec pour salle à manger la pièce ouvrant sur la rue, pour chambre la deuxième, pour oratoire la troisième, d'où l'on ne sortait qu'en traversant la chambre. L'ancienne pharmacie de l'hôpital était devenue cuisine et cellier ; l'ancienne cuisine, une étable où il entretenait deux vaches dont il envoyait chaque matin la moitié du lait aux malades de l'hôpital : « Je paye ma dîme », disait-il. L'hiver, il se retirait le soir dans un compartiment de planches aménagé dans l'étable, son « salon d'hiver », meublé comme la salle à manger d'une table de bois blanc et de chaises de paille. Un vieux buffet peint en rose, habillé de napperons, lui servait d'autel ; les riches pénitentes qui voulaient lui offrir un autel neuf voyaient chaque fois leur argent donné aux pauvres : « Le plus beau des autels, c'est l'âme d'un malheureux consolé qui remercie Dieu. » Il ne lui restait de son ancienne fortune que six couverts d'argent et une grande cuiller, serrés chaque soir dans un placard dont on n'ôtait jamais la clef, plus deux flambeaux massifs hérités d'une grand'tante. « Je renoncerais difficilement à manger dans de l'argenterie », avouait-il. Dans son jardin en croix, madame Magloire cultivait des légumes sur trois carrés ; le quatrième, réservé aux fleurs, lui valut cette remontrance : « Il vaudrait mieux des salades que des bouquets. — Madame Magloire, vous vous trompez. Le beau est aussi utile que l'utile. Plus peut-être. » Aucune porte de la maison ne fermait à clef ; celle de la salle à manger, jadis verrouillée comme une prison, n'était plus close qu'au loquet, jour et nuit. Aux inquiétudes d'un curé, il répondit en citant le psaume : « Nisi Dominus custodierit domum, in vanum vigilant qui custodiunt eam », et il avait écrit en marge d'une bible : « La porte du prêtre doit toujours être ouverte. » C'est dans cet esprit qu'il faut placer l'aventure de Cravatte. Ce lieutenant de brigands infestait la montagne ; le maire du Chastelar supplia l'évêque, en tournée, de rebrousser chemin ou du moins d'accepter une escorte. « Je compte aller sans escorte... Je ne suis pas en ce monde pour garder ma vie, mais pour garder les âmes. » Il partit avec un seul enfant pour guide, passa quinze jours chez les bergers, et voulut chanter un Te Deum sans ornements pontificaux. On apporta alors une caisse contenant la chape d'or, la mitre et la crosse volées un mois plus tôt à Notre-Dame d'Embrun, avec ce billet : « Cravatte à monseigneur Bienvenu. » Au curé qui murmurait « Dieu, ou le diable », l'évêque répondit avec autorité : « Dieu ! » De retour, il déclara à sa soeur : « Le pauvre prêtre est allé chez ces pauvres montagnards les mains vides, il en revient les mains pleines. » Et le soir : « Ne craignons jamais les voleurs ni les meurtriers... Les préjugés, voilà les voleurs ; les vices, voilà les meurtriers. » Quant au trésor, on trouva dans ses papiers cette note : « La question est de savoir si cela doit faire retour à la cathédrale ou à l'hôpital. » Peu après, à un dîner chez le préfet, le sénateur épicurien dont il a été question, un peu égayé, s'écria : « Parbleu, monsieur l'évêque, causons... J'ai ma philosophie. »"
 },
 {
  "candidate_label": "fc12e892",
  "pass_no": 3,
  "text": "mememememememetremeleursmememememeleurslameleursmememeleursmelamemeleursmemelamememetremememeleursmememeleursmemeleursmemememeleursleursmememeleursmemememememememememememelamemememememememememeleursmememetremememememememememetreleursleurskeleursleursimekeleursmemekemememelamememememememememememelameleursmememeleursmeleursmeleursmekelamekeleursmelamemememememeleursmemememememememeleursimeleurslakeleursileurslamemememeleurslamekemeleursmemememememememememememeleurslamemememelamememememememeleursleursmememememelapremieremememelamememememeleursmeleursmememelamememememememeleursmeiememememeleursmemeleursmemememememememememememeleursmememememememememeleurskemememememememeleursmememememeleursmemememememememememememeleursleursimememelamemeleursmememelameleursleursmemeleursmemememememememememememeleursmememememememeleursmemememememememeleursmememetrelamelakememememememeleursmemememeleursmememememememememememeleursmememeleurslamemememememememememeleursmeleurslamememelaleursmememememeleursmemetremelamememekelamemelameleursmemememeleursmememekememekemeleurslamemeleursleursmemememeleursmememememememeleursmeleurslamemememememeleursimemememememeleursmememeleursmeleursmeleursmemememelameleursmemememeleursmleursileursileursmeleursmemememememekeleursimemememememememeleursmemetrememeleursimememememememememememememememememeleursmememememememememememememeleurskemememememememememeememememememeleurslamemememememekeleursmemememelalamemekelamememememememememeleursmemeleursleursmeleursilamememeleursmeleurslamememeleursmeleurslaleursmemememememememememekeleursmeeleurslameleursmememememeleursmememeleursimemeleursmemeleurslalamememeleursmeleurskemeleurskememememememememememememememememememelamemememememeleursmememememememememeleursmemememelamemeleursmememelamememememememememememememememememememeleurslamemelamememeleursmeleursmemekeleurslamememememememeleursmememememeleursmemememekemelameleursmememeleursmemelaleursmememelakemeleursmemeleursmemememekemelamememeleurskemememememeleursimemeleursmememememetremememeleursmeleursmemelamemetreleurskemeleurskememetreleursmemememememememememeleursmememememememememememememememetremememeleurskemememememeleursmememeleursmememememememelamemememeleursimememememememememememememeleursmemeleursmemememememememememememeleursmememememeleursmemememememememememekemememememeleurslamelamemememeleursmemememetrememelamememeleurslameleursimemememememememememeleursimemelamemememememememememememememememememeleurstreleursmeleurslamemememeememememememememememememememememememememememeleursmemememeleursmemeleursmemeleursmemeleursemememememememeleurskeleursmememememeleurslamememeleursimeleursmeleursmeleursmememememememememememememememeleursmememememeleursmemememememeememememememememekememeleursmemememememememeleursmemeleurskememememememememememememememememememememememeleursimekememememelamememememememekemeleursleursleursimememememememememememememememememememememememememememememelaleursmememememememeleursleursimemememememememememememememememelalamemeekelamemememememememememememememememememememememememememelamemememekeleursmemememelalamemelalamememelalamemelameleursmemememeleursmemememeleursmemememeleursmemememememememememeleursmememememememememekeleursmemeleursleursememeleursimemeememelamememeleursmememelamememememememememememeleursilamemeleurslamemememememememememememememeleursmemememememeleursmemememeleurslamememememelamemetreleursleursileursmememememememeleursimemeleursimememememememeleurslamemelameememememeleurspareleursmemememememememememememeleursmemememememememeleurslamemememeleursmememememeleursmememelalamemememememelamemelamemeleursmemeleursmemememememememememememeimemememeleursimememeleursikememeleursmememeleursmememememeemememelalamememememeleursleursmeleursleursmemeleursmemememeleursmememekememememememememememeleursmememeleursmeleursmememeleurslamemeleursmeemememememememememememeleurslaleursmememememememeleursmemememeleursimemeleursmeleursmemememeleursmeleursleursmeikemememememememeleursmemememememememememelamememememememememeleursmemetretrekememememememememememememememeleursmemeleursmememeleursmelamememememeleursmemememeleursmememelametreleursmemeleurslamelamememememememelamememeleursmemememetreleurskemeleursmelamemememememeleurskememememememeleurslamemememememetremememememelaleurslameleursmemememememememememeleursmemeleurslamememememememememememelaleursimeleursmemememeleursleursmememememeemeemememeleursmeme"
 },
 {
  "candidate_label": "a1cd2087",
  "pass_no": 3,
  "text": "memeleursleurslamememelamemetrememememeleurslakemememememeleursmememeleursmeleursmememememelamememememememeleurslapremieretreteleursmemeleursmememememeleurslalamemememekememememeleursmememeleurslameleursmemememekeleursleursmeleursleursmememeleurskememememememeleursleursmemememememememememememememememeleurslamemememeleursmemeleursmememememeeleursmemeleursmememememememeleurskemeleursmememekeleursmememeleursmemememememememememememeleursmeleursmetrememememememeleurslaleursmememememememememememetrememeleursmememelamemeleursmeleursmeleursleurslamemememememeleursmemeleursmeleursmememememememeleursmememeleurslamememememememeleursmememeleurskelamelamemememememelamememelamememeimemeemeleursmememeleurskeleursmemelamemeleursmemeleurskemememelaleursmememekeleursmemeleursdelaleursmememeleursmeleursmememekeleursleursleursmemememememememememememememememeleursdelameleursmememememememememememememememememememememeleursmemememeleursmemememememekeleursmemememememeleursmemememememememeleursmememememeleursimememememememekemeleursmememememelameleurslamemememememememememeleursmemememeleursmememememeleurslameleursmemememememeleursmemememeleursmememememelamememememememememememememekeleursleursmememeleursimememememeleurskeleurskelamelamememeleursmememememeleursmememeleursmelaleursmememeleursimeleursmemememekeleursmeleursikemeleursmemememememekemememememeememelamemememememememememeelamememememeleursmeleursmememememememememeleursmememememememememememememememmemememememeleursmeleurslamekemeleursimememememememememeleursmememememeleursmekekelamekemeleursmemememeleursmememememeleursmemememememememeleursmememememeleursmemememememeleursmemeleursmeleursimeleursmleursmeleurskeleurskeleursmeleursileursmeleursmememememememeleurskemeleurskedeleursmeleursmemememememememelamememekeleursmemememememememememememeleursmememememetretemeleursmeememememememelamememememememeleursmememememekeleursmelaleursleursmememememeleursmememememeleursmeleursmelaleursmemememememememeleursmemememememememememememetremememememememeleursmemememeleursemememeleursleursmememememeleursmemememememeleursmemememeleursmeleursleursmemememememememeleurskememeleursmemeleursmmemememeleursmeleursmemememeleursmemeleursmememeleursmemememememememememememeleursmememememememeleursmemememememememememeemeleursememememeleurskeleursmelamemekemememememeleurskememememeleursememeleursmememememememeleursmeleurskememememememeleursmemeleursmetretemememeleursleursimemememememeleurskelekeleurslamememeleursmemekememememekememeleursmememememememeleursimememememeleursmekelamelamememememememememeleurskemememememememememelaleurslamememememememelakememememememememelamememeememememememememememememememememeleursleurslaleurslamememememememememememeleurslameleursmememememememememememememememeeleursileurslamememeleurslamememememememememememememememeleursmemekemememememeleursmememeleursmememeleurslamememememememememememememememeelameleursmemeemememememememememememememememeleursleursmememememeleursmeleursmelamememeleurskemeleursmemememememememememememememememememememememeleursleursimemememememeleursimememememememememememeleursimemeleursmeleursmememeleurslamelamemeleursimememelamelamememememeleursleursmememeleursleurslameleursmememememememekemeleurskelamememememeeleurslamemeleurskemeleursmemememememememememememememeleursmememememeleurskemememememememememeleurslamememememememeleursmememeleurslamemeemelamemememememememeemelalaleursmemememememememememememememememeleurskememeleurskemelameleursmememememeleursmememeleurskeleursmemememeleurslamelamemememememekeleursmelamememeleursmemememeleurskeleursleursmeleursmeleurskeleursmeleurskemeleursmeleursmemeleursmememeleurskememelamememeleurskememeleurskemelamememeleurskeleursmetreteleursmemememeleursmemelamemeleursmememememeleursmeleursmeleursmelamemekememememememememelamemememeleursmememememeleursmeleursleursmememememememelameleursmememeleursmemememekeleursmememememememeleurskemememememememememememeleursmemeleurslaleursmelamemememememeleurslaleursleursmemememememeleursimemeleursmememeleurskememememememememememememeleursleursmemememememeleursimeleursmemeleursmemememememeleursmemeleursmeleursimememeemememeleursimemeleursdeleursileursleursmemememeleurslalameememememeleurskemememememememememememememememememememeleurskeleursmememeelaleursimememememeleursmemememememeleursmeleurslaleursimememememememeleursmeleursimememelalaleursmeelamememeleursmememelameleursmememeleursmememememeleursmemememelamemememeleursmemelamemememeleursmeleursmemeleursmemememeleurslamemememememememelamelamelamemememeleursdeleursmetre"
 }
]
```

## 2. Scoring protocol (frozen prompt — read it from the file verified in §0)

For reference, the frozen prompt text is reproduced below. The FILE
(at `/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/side-homophonic-rebuild2/track-d/judge_prompt.txt`) is authoritative — if this reproduction ever
differed from the file, the file wins (and the hash check in §0 would
have caught it).

--- PROMPT BEGIN ---
You are a judge of French-language fluency. You will be shown a passage of text. Some passages are fluent French; others are degraded, garbled, or adversarially constructed.

Rate the passage's FRENCHNESS — how much it reads as natural, fluent French prose — on a 0–100 scale:

- 100: flawless, natural French prose (any era)
- 75: clearly French, with minor errors or oddities
- 50: fragmented French; roughly half is broken or non-French
- 25: mostly non-French, with scattered French-like fragments
- 0: not French at all

Judge ONLY fluency as French. Do not reward or penalize subject matter, era of style, or passage length.

Output format (exact): the first line is a single integer from 0 to 100 and nothing else. The second line is exactly one sentence explaining the score. No other text.

PASSAGE:
---
{text}
---
--- PROMPT END ---

For each assignment: substitute the passage text for `{text}`,
apply the prompt, and produce your response in the prompt's EXACT
output format: first line a single integer 0–100, second line
exactly one sentence explaining the score. No other text.

## 3. Hard constraints (violations void the run)

- Score ONLY what the prompt asks: French fluency. Nothing else.
- One integer + one sentence per assignment. No extra commentary,
  no hedging paragraphs, no meta-discussion.
- Do NOT re-score, revise, or "second-guess" any assignment after
  writing it. First honest judgment stands.
- Do NOT discuss these passages with anyone or reference outside
  material. Judge the text in front of you.
- If a passage is empty or unreadable, score it 0 with the
  justification "Empty or unreadable passage." — do not abort.

## 4. Return format (exact)

Return a single JSON object and nothing else:

```json
{{
  "worker_id": "w0013",
  "prompt_sha256_computed": "<sha256 you computed in step 0>",
  "prompt_sha256_expected": "390a1ec0bf1aa9e0e495a5fe98e65107c41025c954cd11b68d1931816c08e21d",
  "results": [
    {{"candidate_label": "<label>", "pass_no": <n>,
      "raw_response": "<int>\\n<one sentence>"}}
  ]
}}
```

One entry per assignment, in the order given. `raw_response` is the
literal two-line string: integer, newline, single sentence.
