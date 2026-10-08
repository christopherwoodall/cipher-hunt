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

You will score 1 candidate(s). Each assignment is one
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
  "candidate_label": "fed88338",
  "pass_no": 2,
  "text": "En 1815, Charles-François-Bienvenu Myriel, âgé d'environ soixante-quinze ans, occupait depuis 1806 le siège épiscopal de Digne. Sur son passé circulaient toutes sortes de rumeurs, fondées ou non, car les propos que l'on tient sur un homme pèsent souvent aussi lourd dans sa destinée que ses actes. Fils d'un conseiller au parlement d'Aix, issu de la noblesse de robe, on l'avait marié très jeune pour lui transmettre la charge paternelle. Malgré ce mariage, le jeune Charles Myriel, bien fait, élégant et spirituel, avait beaucoup défrayé la chronique mondaine. Puis la Révolution éclata, dispersant les familles parlementaires. Il émigra en Italie dès les premiers jours ; son épouse y succomba à une maladie de poitrine, et ils n'eurent pas d'enfants. Nul ne sut ce qui transforma alors sa destinée — l'effondrement de l'ancien monde, la ruine des siens, les spectacles tragiques de 93 vus de loin — mais lorsqu'il revint d'Italie, il était prêtre. En 1804, on le trouve curé de Brignolles, déjà vieux, vivant retiré. Une affaire de sa paroisse l'amena à Paris vers l'époque du couronnement, où il sollicitait le cardinal Fesch. Attendant dans une antichambre, il croisa Napoléon qui, intrigué par le regard du vieillard, demanda brusquement qui était ce bonhomme. « Sire, répondit Myriel, vous regardez un bonhomme, et moi je regarde un grand homme ; chacun de nous peut profiter. » Le soir même, l'empereur s'enquit de ce curé, et peu après Myriel apprit avec surprise sa nomination à l'évêché de Digne. Il s'installa avec sa soeur, mademoiselle Baptistine, de dix ans sa cadette, et leur unique domestique, madame Magloire, jadis servante de M. le curé, devenue femme de chambre et femme de charge. Le palais épiscopal, attenant à l'hôpital, était un vaste hôtel seigneurial aux jardins magnifiques. L'évêque y mena une existence d'une simplicité extrême. Ayant réclamé les trois mille francs annuels votés pour ses frais de carrosse et de tournées, il en dressa aussitôt la répartition : bouillon pour les malades de l'hôpital, sociétés de charité maternelle, enfants trouvés, orphelins — la totalité reversée. Un sénateur de l'empire s'en indigna par écrit auprès du ministre des cultes, dénonçant le luxe des prêtres. Les pauvres du pays, eux, avaient choisi dans ses prénoms celui qui avait un sens et ne l'appelaient que monseigneur Bienvenu, nom qui lui plaisait : « Bienvenu corrige monseigneur », disait-il."
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
  "worker_id": "w0005",
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
