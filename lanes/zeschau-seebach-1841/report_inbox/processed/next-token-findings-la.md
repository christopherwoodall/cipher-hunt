# Next-token findings: followers of 11="la"

Beat: all 45 occurrences of 11. Method: extracted every 11 window (index, predecessor, 3 followers) from the repaired 1,847-pair stream, clustered by follower pattern first, predicted from 1840s diplomatic French.

## De-duplication (load-bearing)

- 7 windows are **87-11 = "cela"** (compositional, established): excluded from "la" counts.
- 3 windows are **47-11 = "cela"** via the 47="ce" allophone (@270, @358, @499): excluded from "la" counts. (Without this, "ce la" looks like a frame; with it, it's "cela".)
- **Standalone "la": 35 windows.** All predictions below use these 35.

Top predecessors of standalone "la": 00 ×4, 06 ×4, 67 ×4, 37/17/88/91/39 ×2.

---

## P1 (HIGH). "[X]-ent la [NOUN]" frame ×3 → 06="ent" LEAD

- @320: `94-06 la 92-60-15`
- @1123: `14-06 la 52-37-43-00`
- @1721: `68-06 la 52-37-43-98`

Three windows share `[stem]-06 la [feminine noun]`. Two independent readings, both grammatical: (a) 3rd-pl verb + article — "…[94]ent la [92]" ("they [verb] the [92]"); (b) "-ment" adverb + article — "…[94]ment la [92]". Either way **06 is a grammatical ent/ment ending**, 06 occurs 44× (function-word frequency), and its top followers include 77="le" ×6 (`[verb]ent le [infinitive]` — "peuvent le faire"-shaped, which also supports 77="le" as pronoun). Cross-frame: the qui-finder's independent "concern-ent" (@179: 23-37-06) puts 06="ent" in a verb slot — two frames, one ending.

**Propose 06="ent/ment" as a LEAD** (not promotion: the verb-vs-adverb fork needs the stem battery).
**Testable:** (1) 06 contact-profile battery as verbal ending vs adverb ending; (2) stems 94/14/68 — verb stems or adjective stems? (3) 52 and 92 as feminine direct-object nouns (noun batteries); (4) does "06-77" ×6 pattern as `[verb]ent le`?

## P2 (HIGH). "la 52-37-43" ×2 — two-leg noun phrase, votes in the 37 war

- @1123: `14-06 [la 52-37-43] 00`
- @1721: `68-06 [la 52-37-43] 98`

Byte-identical trigram after "la", both preceded by `[X]-06`. "la [52] [37] [43]":

- 37 **cannot be a finite verb here** — no grammar licenses "la NOUN VERBfin". So 37 = adjective/participle ("la [52] [37-adj]"), or 52-37 is one word, or 52=adjective and 37=noun. Every live reading **votes 37=adjective** (or at minimum non-finite) — against the verb readings ("en ce qui [23/26]-37", "que 84-24-37").
- 52 = feminine noun (two legs); 43 continues the phrase.

**Testable:** (1) 37's contact profile at @1123/@1721 vs its est-37 adjective frames vs qui-37 verb frames — this cluster can decide the 37 tension; (2) 52 noun battery (27 occurrences); (3) 43's profile after 37.

## P3 (HIGH). 78 fork splits by window — positional allophony hypothesis

- @296: `16-01 [la 78-40] 97-86` → "la [78]-e-97"
- @1669: `06-91 [la 78-55] 81-92` → "la [78]-55-81"

@296's "la 78-40" exactly mirrors the "l'ère" shape (la + er + e, cf. pencil "premi-ere" = 34-29-40): under 78="er", it reads "l'ère [97]". Under 78="ver", "la ver-e-97" has no French ("vérité" needs vé-ri-té). → **@296 votes 78="er".**

@1669's "la 78-55-81" is "la vérité"-shaped (78-55-81 = vé-ri-té?; "vérité" is core diplomatic vocabulary — "la vérité est que…"). Under 78="er", "l'ère 55-81" fails. → **@1669 votes 78="ver".**

**Hypothesis: 78 is a positional/contextual allophone** (ver before some groups, er before others) — same species as the 47/87 split. The fork isn't random; it's conditioned.
**Testable:** (1) 78 contact-profile battery split by following group (40 vs 55 and beyond); (2) minimal pair: 97 ("l'ère"-continuation after 78-40) vs 56 ("l'ère"-continuation after 29-40 @499-excluded… note @499 is now cela-classified; use the crib's 29-40 instead); (3) 55/81 as "ri/té" (noun-syllable battery).

## P4 (MEDIUM-HIGH). "l'en-X" ×3 — elided nouns after "la"

- @731: `48-88 [la 24-85] 93-76`
- @782: `29-89 [la 24-42] 94-74`
- @1656: `56-37 [la 24-48] 47-98`

24="en"; "la en" is ungrammatical **unless elided**: "l'en-85", "l'en-42", "l'en-48". Diplomatic candidates: **envoi** ("l'envoi de la dépêche" — peak register), entrée, enquête. Three different second syllables → three words, or one word with allophone seconds.
**Testable:** (1) 85/42/48 second-syllable batteries vs known noun syllables; (2) do 85/42/48 share a contact profile (one word) or diverge (three words)?
**FLAG:** 48 also sits in "est [pred] 48" frames — if 48="trée" (entrée), that frame needs re-examination. Tension noted, not resolved.

## P5 (MEDIUM). "…fois, la [26]" ×2 — 26 = feminine noun, tensions 26=verb

- @239: `98-41-17 [la 26-12] 16-56` → "…41 fois, la [26]-12…"
- @1559: `61-40-17 [la 26-30] 06-60` → "…40 fois, la [26]-30…"

Both windows: `[X] fois, la [26]…` — the absolute/elliptical "une fois la [décision] prise" construction. 26 = feminine noun, **two legs**. This **directly tensions** 26=verb ("concerne" in "en ce qui 26-37", the 23/26 homophone-pair hypothesis).
**Testable:** (1) 26 noun-vs-verb contact profile; (2) if 26 is a noun here, re-examine "en ce qui 26-37" — does the verb-slot reading survive? (3) Third leg-ish: @127 `m-48 la 02-26-32` ("la [02]-26" — adjective+noun or one word).

## P6 (MEDIUM). "et/veut la [43/86]-en-80" ×2 — same-slot noun pair

- @562: `30-67 [la 43-24-80] 97` (prev 67 = et/veut)
- @670: `20-67 [la 86-24-80] 03`

"et/veut la [43/86] en [80]": 43 and 86 occupy the **same slot** (feminine nouns — new same-slot pair, compare 23/26, 09/92), with a shared "en-80" tail ("en [80]" word/bigram). Both forks grammatical here (conjunction+"et la [N]" / verb+"veut la [N]"), so no fork vote — the frame is the finding.
**Testable:** (1) 43/86 noun batteries; (2) "24-80" bigram profile — one word ("en[80]") or "en"+"80"? (3) Note 43 also closes P2's "la 52-37-43" — busy cell, profile both frames.

## P7 (MEDIUM). "pour que la [21] veut [93]" — clean clause, fork vote

- @108: `00-46 [la 21-67] 93-29` → "pour? que la [21] et/veut [93]"

Under 67="veut": **"que la [21] veut [93]"** — a complete SVO clause ("that the [21] wants [93]"). Grammatical, no strain. Under 67="et": "…et la [21]…" also grammatical (weaker). → mild vote for **67="veut" at @108**; 21 = feminine subject noun (single leg).
**Testable:** 21 noun battery; 93's verb-profile after "veut".

## P8 (MEDIUM-LOW). 11 = object pronoun "la" at some windows

- @1044: `82-63 [la 67] 76-85-41` → under 67="veut": **"[63] la veut [76]"** ("[he] wants it") — pronoun+verb, fully grammatical. Under 67="et": "…la et [76]" strains.
- The four "67-11" predecessors (@562, @670, @997) and four "06-11" predecessors are article-compatible ("et la [N]", "[verb]ent la [N]"), so the pronoun reading is window-specific, not global.

Note: article/pronoun duality is one French word ("la"), not cipher polyvalence — same species as 77="le". No new polyvalence claimed.
**Testable:** classify all 35 "la" windows by article-vs-pronoun frame; the pronoun set should pattern with verb followers.

## Anomalies (flagged, not forced)

- **A1. "la la" doublet @1523/@1524**: `31-24-[11-11]-48-96-87-46` = "…en la la 48 par ce que…". "la la" is impossible. Leading hypothesis: article + la-initial word ("en la [la-48…] par ce que" — "langue/lettre/liberté"-shaped); alternative: one 11 = "là". **Battery:** 48's word-second-syllable profile.
- **A2. @1288 "pour la fois"**: `68-00-[11-17]-84-59-35` = "…pour? la fois 84-est…". "pour la fois" is unidiomatic (the idiom is "pour la première fois"). Tests **00="pour"** and **17="fois"** simultaneously at this window. Marginal save: "pour la fois où…" ("for the occasion when…"). **Battery:** 68's profile; 84's profile (84 also in "que 84-24-37" and "la fois 84").
- **A3. @997 "et/veut la par"**: `60-67-[11-96]-82-33-00` = "…et/veut la par-m-33". "la par" parses under no reading of 96="par". Either 96≠"par" here, or 11-96-82 begins a word ("l'ap-par-…" — "appareil/apparence"-shaped, though 82="m" strains it). **Battery:** 96's profile at @997 vs its "par"-frame profile.

## Supporting observations

- **@754 "la première [20]"**: the second pencil crib is followed by 20, not "fois" (@1034 has 17="fois"). "la première [20]" = feminine-singular-noun slot — **instantiates leg #1 of 20's paradox** (feminine noun vs determiner/adjective-before-"fois-que"). Constraint for 20's battery.
- **"pre-39 la" ×2** (@1069, @1606): "70-39" bigram before "la" — "pre[39]" ("premier"? "pré[39]"?) — mini-cluster for whoever owns 39/70.
- **@1116 "la 88-pre-12"**: "la [88] pre[12]" — "la"-initial "pre-" word ("l'appré…"-shaped) or "la [88] première" (postposed adjective).
- **@52 "la toute-85"**: `79-37 [la 79-85] 58` — "la toute [85]" ("la toute première"-shaped) — mild support for 79="tout".
- **@1619 "la 84-78"**: `42-44 [la 84-78] 66` — 84 (the "que 84" clitic candidate) before 78 (P3's fork cell). Cross-cluster link for the battery.

## Ranked battery queue

1. 06="ent/ment" lead battery (P1) + stem classification (94/14/68).
2. 37 frame battery at @1123/@1721 vs est-37 vs qui-37 (P2 — may decide the 37 war).
3. 78 fork-resolution battery, split by following group (P3).
4. 85/42/48 second-syllable batteries (P4); resolve the 48 tension.
5. 26 noun-vs-verb battery (P5); re-examine "en ce qui 26-37".
6. 43/86 noun batteries + "24-80" bigram (P6).
7. 21 noun battery; 67="veut" check at @108 (P7).
8. Article-vs-pronoun classification of all 35 "la" windows (P8).
9. A1/A2/A3 anomaly batteries (doublet, "pour la fois", "la par").

## Honest nulls

- No specific noun identified after "la" in any window — "la France / la cour / la note" level predictions all failed to pin (52, 92, 26, 21, 43, 86 remain unnamed nouns).
- The "l'ère" reading (@296 via P3) is shape-based, single-leg, unconfirmed.
- 06's verb-ending vs adverb-ending fork (P1) is unresolved — both readings grammatical at all three windows.
- "cela"-classification of the three 47-11 windows is inherited from the parle-finder, not re-derived here; @499's "cela 29-40" ("cela ere…") doesn't parse and is flagged back.
