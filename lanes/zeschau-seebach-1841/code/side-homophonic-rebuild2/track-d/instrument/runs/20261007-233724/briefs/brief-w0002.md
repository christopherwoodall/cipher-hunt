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
  "candidate_label": "a1cd2087",
  "pass_no": 1,
  "text": "memeleursleurslamememelamemetrememememeleurslakemememememeleursmememeleursmeleursmememememelamememememememeleurslapremieretreteleursmemeleursmememememeleurslalamemememekememememeleursmememeleurslameleursmemememekeleursleursmeleursleursmememeleurskememememememeleursleursmemememememememememememememememeleurslamemememeleursmemeleursmememememeeleursmemeleursmememememememeleurskemeleursmememekeleursmememeleursmemememememememememememeleursmeleursmetrememememememeleurslaleursmememememememememememetrememeleursmememelamemeleursmeleursmeleursleurslamemememememeleursmemeleursmeleursmememememememeleursmememeleurslamememememememeleursmememeleurskelamelamemememememelamememelamememeimemeemeleursmememeleurskeleursmemelamemeleursmemeleurskemememelaleursmememekeleursmemeleursdelaleursmememeleursmeleursmememekeleursleursleursmemememememememememememememememeleursdelameleursmememememememememememememememememememememeleursmemememeleursmemememememekeleursmemememememeleursmemememememememeleursmememememeleursimememememememekemeleursmememememelameleurslamemememememememememeleursmemememeleursmememememeleurslameleursmemememememeleursmemememeleursmememememelamememememememememememememekeleursleursmememeleursimememememeleurskeleurskelamelamememeleursmememememeleursmememeleursmelaleursmememeleursimeleursmemememekeleursmeleursikemeleursmemememememekemememememeememelamemememememememememeelamememememeleursmeleursmememememememememeleursmememememememememememememememmemememememeleursmeleurslamekemeleursimememememememememeleursmememememeleursmekekelamekemeleursmemememeleursmememememeleursmemememememememeleursmememememeleursmemememememeleursmemeleursmeleursimeleursmleursmeleurskeleurskeleursmeleursileursmeleursmememememememeleurskemeleurskedeleursmeleursmemememememememelamememekeleursmemememememememememememeleursmememememetretemeleursmeememememememelamememememememeleursmememememekeleursmelaleursleursmememememeleursmememememeleursmeleursmelaleursmemememememememeleursmemememememememememememetremememememememeleursmemememeleursemememeleursleursmememememeleursmemememememeleursmemememeleursmeleursleursmemememememememeleurskememeleursmemeleursmmemememeleursmeleursmemememeleursmemeleursmememeleursmemememememememememememeleursmememememememeleursmemememememememememeemeleursememememeleurskeleursmelamemekemememememeleurskememememeleursememeleursmememememememeleursmeleurskememememememeleursmemeleursmetretemememeleursleursimemememememeleurskelekeleurslamememeleursmemekememememekememeleursmememememememeleursimememememeleursmekelamelamememememememememeleurskemememememememememelaleurslamememememememelakememememememememelamememeememememememememememememememememeleursleurslaleurslamememememememememememeleurslameleursmememememememememememememememeeleursileurslamememeleurslamememememememememememememememeleursmemekemememememeleursmememeleursmememeleurslamememememememememememememememeelameleursmemeemememememememememememememememeleursleursmememememeleursmeleursmelamememeleurskemeleursmemememememememememememememememememememememeleursleursimemememememeleursimememememememememememeleursimemeleursmeleursmememeleurslamelamemeleursimememelamelamememememeleursleursmememeleursleurslameleursmememememememekemeleurskelamememememeeleurslamemeleurskemeleursmemememememememememememememeleursmememememeleurskemememememememememeleurslamememememememeleursmememeleurslamemeemelamemememememememeemelalaleursmemememememememememememememememeleurskememeleurskemelameleursmememememeleursmememeleurskeleursmemememeleurslamelamemememememekeleursmelamememeleursmemememeleurskeleursleursmeleursmeleurskeleursmeleurskemeleursmeleursmemeleursmememeleurskememelamememeleurskememeleurskemelamememeleurskeleursmetreteleursmemememeleursmemelamemeleursmememememeleursmeleursmeleursmelamemekememememememememelamemememeleursmememememeleursmeleursleursmememememememelameleursmememeleursmemememekeleursmememememememeleurskemememememememememememeleursmemeleurslaleursmelamemememememeleurslaleursleursmemememememeleursimemeleursmememeleurskememememememememememememeleursleursmemememememeleursimeleursmemeleursmemememememeleursmemeleursmeleursimememeemememeleursimemeleursdeleursileursleursmemememeleurslalameememememeleurskemememememememememememememememememememeleurskeleursmememeelaleursimememememeleursmemememememeleursmeleurslaleursimememememememeleursmeleursimememelalaleursmeelamememeleursmememelameleursmememeleursmememememeleursmemememelamemememeleursmemelamemememeleursmeleursmemeleursmemememeleurslamemememememememelamelamelamemememeleursdeleursmetre"
 },
 {
  "candidate_label": "264710b9",
  "pass_no": 1,
  "text": "Autour d'un évêque gravite d'ordinaire une escouade de petits abbés, comme autour d'un général une volée de jeunes officiers — ce que saint François de Sales nomme les « prêtres blancs-becs ». Toute puissance a son entourage, toute fortune sa cour ; les chercheurs d'avenir tourbillonnent autour du présent splendide, car l'apostolat ne dédaigne pas le canonicat. Il y a dans l'Église, comme ailleurs, des « grosses mitres » : évêques bien en cour, riches et habiles, traits d'union entre la sacristie et la diplomatie, qui font pleuvoir sur leur suite grasses paroisses et prébendes en attendant les dignités. Leur rayonnement empourpre leur cortège ; c'est tout un système solaire en marche, et Rome est au bout : de la Grandeur à l'Éminence il n'y a qu'un pas, et de l'Éminence à la Sainteté que la fumée d'un scrutin. Monseigneur Bienvenu, humble, pauvre, particulier, n'était pas de ces grosses mitres, et cela se voyait à l'absence complète de jeunes prêtres autour de lui : à peine ordonnés, les séminaristes se faisaient recommander à Aix ou à Auch, car on veut être poussé, et un saint d'une abnégation excessive est un voisinage dangereux — il pourrait communiquer par contagion une pauvreté incurable. De là son isolement, dans une société où réussir est l'enseignement qui tombe goutte à goutte de la corruption : le succès, ce sosie du talent, a pour dupe l'histoire ; « Prospérité suppose Capacité » ; la multitude décerne le génie à quiconque atteint son but, fût-ce un apothicaire inventeur de semelles de carton. Sur sa foi, il n'y a pas à sonder l'évêque de Digne : devant une telle âme, on n'est en humeur que de respect. Jamais ses difficultés de croyance ne se résolvaient en hypocrisie ; il croyait le plus qu'il pouvait — « Credo in Patrem ! » — et puisait dans les bonnes oeuvres cette satisfaction qui dit tout bas : « Tu es avec Dieu. » Mais au-delà de sa foi, il avait un excès d'amour — quia multum amavit — qui le faisait juger vulnérable par les gens raisonnables. Sa bienveillance débordait jusqu'aux choses : il n'avait pas cette dureté irréfléchie que tant de prêtres réservent à l'animal. Les laideurs de l'aspect ne l'indignaient pas ; il semblait y chercher une excuse, comme le linguiste déchiffre un palimpseste. Sa soeur l'entendit un matin, devant une araignée noire et velue : « Pauvre bête ! ce n'est pas sa faute. » Un jour il se donna une entorse pour n'avoir pas voulu écraser une fourmi. Jadis homme passionné, peut-être violent, sa mansuétude était le fruit d'une conviction lentement filtrée dans son coeur, pensée à pensée. À soixante-quinze ans, il n'en paraissait pas soixante : une « belle tête » si aimable qu'on oubliait qu'elle était belle, le rire facile — mais qu'on restât quelques heures près de lui lorsqu'il était pensif, et le bonhomme se transfigurait : la majesté se dégageait de cette bonté sans que la bonté cessât de rayonner, comme un ange souriant qui ouvrirait lentement ses ailes. Prière, offices, aumône, consolation, jardinage, frugalité, étude remplissaient ses journées jusqu'aux bords ; et si le temps le permettait, il passait une heure ou deux dans son jardin avant de dormir, seul avec les constellations, offrant son coeur à l'heure où les fleurs nocturnes offrent leur parfum, ébloui par Dieu plutôt qu'étudiant Dieu, songeant aux infinis qui s'enfonçaient sous ses yeux. « Mystérieux échanges des gouffres de l'âme avec les gouffres de l'univers ! » Que lui fallait-il de plus ? Un petit jardin pour se promener, et l'immensité pour rêver ; quelques fleurs sur la terre et toutes les étoiles dans le ciel."
 },
 {
  "candidate_label": "19f3bb19",
  "pass_no": 1,
  "text": "mememememememeleursmemememelametremeemememememememememememememememeelamemememememeleursmemememememememenotrememememememeleurslamemememeleurskemememememekemekememememememememeleursmemeleurskeleursmeleursmeleursleursleursleursimememetrememememeleursmememememememememememememelamemememeleursimemeleursmekememememelamelamememememememeleursmememeleursmeleurslamemeleursmememelamememememememememememeleursemememememememeleursmememememememeleursmememememememememememememeleursmeleursmeleursmememememememelaleursleursdelamememeleurskemeleursmeleursmemeleursmemememememememeleursmemememememememememememememelamemememememememememeleurskeleursleursileursimememekeleursmeleursmemememeleurskememelamemememememememekemelamememememememememelamemelamememememeleursmemememelapremieremememememememelamememelaleursmeleursmememememememememememememememememememememeleurslamememeleursdelaleursmemememememelamememeleursmemememememememeleursmememememememememememleursmemememememeleursmememememeleursleursmemememememememeleursimemememememelameleurslameleursleursimeleursmemememememememememememememememememememememememememememetremememememememeleurslamemeleursmemeleursimemememememememememememeemememememeleursmememeleursilamemeleurslamemeleursmelameleursimelalalamemeleursimeleurslamemelalamememememememeemememememememememememelamemememeleurslamemememememememememeleursmememememememememememememeleurscomemememememekememekememememeleursleursmemememeleursmememememememeleursmemelamememememememememememelamememememememememememeleursmemekelamemememememelameleursmememememememememeleursleursimememememememememememeemeleursleursimemememememeleurslamemememememememeleursmemememeleursmemememememememememeleursleursmemememelalamememeeleurslamemememelaleursmemelamememememekememememeleursmemeleursmemememememememememememememememememeleursleurslamemememememekelameememememememememeleursleursmemememememelamemememelaleurslamememelamelamemeleurskemelameleursmeleursmeleurslamememememememememeleursmemememememeleursmememememememeleursmememelalamemememememelamelamememememeleursmeleursmemememememelameleursmemekeleursmemememelamememememememeleursleursmemeleurskemememeleursmeleursmememeleurslamemeleurslamememememeleursmeleursilameleursileurslamemeleurslamelameleursilamemememememememelamemememeleursimemememememeleursimememememelamememeleursimeleursmemeleursmememememememeleursmememememeleursimemememekelamememememememeleursmemekemememeleurskeleursimememememememeleurskemememememeleursmelamemeleursmeleursleurscomememelaleursimemeleursimemememelamememekemememememememememeleursimeleursikemememeleursikemememelamememememememeleursmememeleursmeeleursmeleursleursmememeemeleursmeleursmeleursmemememememeleursleursmeleursmemememememelameleursmemememememememememememeemememememeleursmemeleurskelameleursimememeleursmemememememememememememelamememeememememeleursmememememememememememememelamemeleursmeleursnometretrememeleursmememeleurslamelamelaleursmememememememeleursmememememememememeleursmemememeleursmememememememememememememememeleursmemememekeleursmemeememememeleurskekekekeleursmemeleurslamemememeleursmememememememememememelamememememememeleursmemeleursmememememememememelamemememememeleursemememememeleurskelamememememelameleursimemememememememememeleursmeleursmeleursmeleursimeleursmememekemememememekeleurslamemeleursmemememelamemermememememelalamemeleursmemeleursmemememeleurskememeleurskemememelamememleursmememelamemememememekememememememememememememeleursimeleursmememeleursmemememememelamememeelamememememeleursmememememeleursmeleursmememememememelaleursmeleursmemeleurslaleursmemememeleurslamememememeleurslamemememememekelamemememeleursmemeleursimememeleurslamemeleursilamememekemelamemememememekeleursleursememelamemememememekemeleursmememeleurskemememememlamememememememeleursmememememememelamemememecomememememememememememeleurskemememememememeleursmeleursleursleursmememememememememememeleursmemeleursmeleursmememeleursleursmemememememememememetrememekeleursimememememememelamememekemememelamememeleursimemememelamememecomememememememememememeleurslamememememememememememememememeleursmeleurslamelaleursmeleursmemememememeleursmeleursmeleursmemememeleursmemeleursmememememeleurskememememememememememememememeleurskemeleursmemememeleursmemeleursleursmetrekemememememememeleursmememememememeleursemememememememeleursmememememememememememememememememememeleurslametrele"
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
  "worker_id": "w0002",
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
