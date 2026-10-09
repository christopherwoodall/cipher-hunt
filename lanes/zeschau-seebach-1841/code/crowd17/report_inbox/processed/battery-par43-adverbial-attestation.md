# Battery verdict: par43-adverbial-attestation

## Bar (verbatim from battery-queue.json)
> resolve iff corpus attestations found for bare 'par mesure'/'par condition' in 1841 French; if attested, re-open the noun premise; if not, the par-43 kill is terminal pending only the @21 polyvalence ruling

## Bar restated as numbered clauses (pre-registered, not modified after seeing data)
- **C1**: bare "par mesure" attested as a clause-level adverbial in 1841 French (Littré 1872–1877 / TLF), in the shape needed: "par mesure" with no complement, before a demonstrative "ce"-frame.
- **C2**: bare "par condition" attested as a clause-level adverbial in 1841 French, same shape.
- **C3** (negative arm): if neither attested, the par-43 noun kill is terminal pending only the @21 polyvalence ruling.

## Context
- 43 = the surviving noun candidate pair {condition, mesure} is dead; the last open premise was bare "par [43]" as adverbial ("par mesure ce...", "par condition ce...").
- Byte-verified on the repaired 1,847-pair stream (repaired_offsets.json + upstream-ct_R5005.txt, parse per repair_parse.py):
  - 1-based @343 (0b@342, row a2_05): `45 64 96 43 87 01` = "ce qui par [43] ce [01]"
  - 1-based @1027 (0b@1026, row a6_03): `45 64 96 43 87 01` — byte-identical window.
  - Two occurrences of the same frame: 64='qui' (banked GT), 96='par' (banked GT), 87='ce' (promoted), 01 open. For 43=condition/mesure to parse, "par condition ce"/"par mesure ce" must be a grammatical bare adverbial — no "que" follows 43.

## Method
- Littré article "mesure" (littre.org, fetched 2026-10-09): full locution inventory + all "par mesure" hits with ±260-char context.
- Littré article "condition" (littre.org, fetched 2026-10-09): full locution inventory + all "par condition" hits with ±220-char context.
- TLF locution inventory via Usito (crawled TLF data) for "mesure" and "condition"; grammar lists of locutions conjonctives/prépositives/adverbiales.
- Coordination with venir-a-1841-corpus (queued, not duplicated — this battery ran no 'venir à' leg).
- R5005, sealed gates, red-team queue untouched; canonical.py never used.

## Findings

### "par mesure"
- Littré lists NO "par mesure" locution. Its locutions: "à mesure (que)" (loc. conj.), "à mesure de" (loc. prép.), "au fur et à mesure", "outre mesure" (loc. adv.), "prendre ses mesures", "faire bonne mesure", "se mettre en mesure".
- Both "par mesure" hits in the article are quotations, both commercial/measure-vessel senses, none adverbial:
  1. Fléchier, Hist. de Théodose III.28: "ne s'y donnait que par mesure" — "by the (measuring) vessel", i.e. goods rationed in measured units.
  2. Beaumanoir XXVI.2 ("Toute coze qui se doit paier par mesure"), Roman de la Rose 14672 ("De despens fere par mesure") — 13th–14th c. "by the measure" (commodity sold in measured units).
- TLF (via Usito): "par mesure de" = "en vue de, en raison de" — REQUIRES a "de"-complement; bare "par mesure" is not listed.
- Targeted web search for 19th-c. adverbial "par mesure": only hits are "par mesure générale" (adjective present) and "par mesure dans les Ventricules" (1734 Mercure de France, physical pouring sense). No bare adverbial.

### "par condition"
- Littré lists NO "par condition" locution. Two hits, both in old quotations:
  1. Beaumanoir XII.54: "fere lais par condition" — 13th c., and XII.54's own quote shows the standard form is "fere lais soz condition" (under condition), i.e. a nominal "under condition" frame, not an adverbial.
  2. Commines VII.15: "Par condition qu'ils voulussent attendre à conclurre la ligue de quinze jours" — 15th c., archaic, and it takes an explicit que-clause. The @343/@1027 windows have NO "que" (87="ce" follows 43 directly).
- Grammar lists of condition locutions (locutions de condition): "si", "à condition que", "pourvu que", "au cas où", "en cas de", "à condition de" — no bare "par condition".
- Locutions prépositives lists: "par comparaison à", "par manque de", "par rapport à", "par suite de" — no "par condition".

## Clause results
- **C1: FAIL.** No bare "par mesure" adverbial attested in period French. The closest forms ("par mesure de" with complement; 13th–14th c. "by the measure") are not the needed shape.
- **C2: FAIL.** No bare "par condition" adverbial attested. The one historical form ("Par condition que..." Commines) is archaic and requires a que-clause absent at the windows.
- **C3: FIRES.** Neither attested → the par-43 noun kill is terminal, pending only the @21 polyvalence ruling (red-team docket, untouched here).

## Verdict: PROMOTE
The attestation check resolved conclusively on its negative arm at the lane's standing corpus bar (Littré + TLF, the same method as venir-a-1841-corpus). The noun-43 line's last escape via bare "par mesure"/"par condition" adverbials is closed: **par-43 kill is terminal pending only the @21 polyvalence adjudication** (red-team territory; @21 `43-29` verb-stem question, battery-43-29-segment, not re-litigated). No standing verdict contradicted or downgraded; §7 intact; no polyvalence declared.

## Epistemic scope
- The bar was the lane's dictionary method (Littré 17th–19th c. citations + TLF locution inventory), not a full-text Frantext sweep; a full-corpus search could in principle find an unattested-in-Littré idiom, but under the lane's stated bar the negative result is terminal at battery grade.

## Follow-ups proposed: none required (negative arm is terminal; no regeneration)
The report documents the closure. Two coordinates for the red team (not queued, informational):
1. The @21 verb-stem polyvalence ruling remains the sole surviving reopen path for 43 (red-team docket; battery-43-29-segment).
2. battery-pour-que-lexicon-close (P3) formalizes the 'pour que' discriminator as exhausted.

## Bookkeeping
- Lock created on start, deleted on completion.
- battery-queue.json: par43-adverbial-attestation → status verdict, result promote, date 2026-10-09 (temp-file + rename, pre-write assert confirmed queued/verdictless, JSON re-validated post-write).
- No downgrade of any standing verdict. Adverses: none listed.
