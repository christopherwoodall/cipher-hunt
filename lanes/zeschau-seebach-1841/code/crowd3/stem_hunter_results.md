# WO2 — STEM HUNTER results: F21 "06 = verb stem"

Lane: `lanes/zeschau-seebach-1841/`. Script: `code/crowd3/stem_hunter.py`.
All counts recomputed from the pair stream (`load_pairs`); machine JSON:
`code/crowd3/stem_hunter_results.json`. Anchors: 7 ground-truth
(11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); provisional: 87=ce, 64=qui,
96=par, 77=pas (rival: 77=que).

## Verdict board

| Claim | Verdict | Basis |
|---|---|---|
| 06 = verb stem (/mɑ̃/ "demand-/command-") | **CONFIRMED** (4 checks) | §a |
| 06 is polyvalent (also /ɑ̃/ "-ment"/"-ent") | **CONFIRMED** (distributional + phonetic) | §a, §e |
| 67 = "veut"-class modal | **CONFIRMED** (7 checks); "veut" specifically PLAUSIBLE+ | §b |
| 06 & 67 a "pair" | **REFUTED** as same-verb/same-construction; COMPLEMENTARY verb-system slots | §b |
| 77 = "pas" (under verb-stem 06) | **CONFIRMED** (6 checks) | §c |
| 77 = "que" (rival) | **REFUTED** as primary reading | §d |
| Tension w/ WO1's 06="ent" | **DISSOLVED** — different 06s, no conflict | §e |

## (a) 06's full follower profile (46 occ, rank 4)

Followers: 77×6, 29×5, 00×4, 11×4, 67×3, 59×2, 21×2, 52×2, 65×2, 60×2,
06×2, + 11 singles (88,73,70,55,50,40,71,43,14,84,62,91).
Predecessors: 30 distinct / 46 = **diversity 0.652 — second-highest among
top-15 groups** (24: 0.654, 64: 0.609, 29: 0.574).

Compatibility vs verb-stem expectations:
- Known verb-continuations (29=er-inf, 40=e, 34=i, 11=la-obj, 77=pas/que,
  46=que, 64/96/87 prov, 82=m, 70=pre): **17/46 = 37%**.
- + V29 followers (groups taking -er ≥2×, i.e. modal+infinitive-stem
  compatible): 2/46 → **19/46 = 41%**.
- Unexplained 27/46: includes 00×4 (rank-1 group; 00="de"? → "demande de",
  "de parler" — bonus lead, not this WO), 67×3 (residual, §b), 06×2 (the
  /ɑ̃/ subset, §e).

Era verb-continuation profile (Tocqueville 1835/1840, 214,861 words;
word-level, documented in script): mean over 33 common verb forms:
P(pas|verb)=**5.46%**, P(que|verb)=**1.76%**, P(la/le/les|verb)=**5.54%**.
Observed: 06→77 = 6/46 = **13.0%** (2.4× era mean; attested for
faut 11.2%, veulent 10.5%); 06→11 = 4/46 = **8.7%** (1.6×); 06→29 = 5/46 =
**10.9%** infinitive.

The 06="ne" rival is **killed**: era "ne" followed by er-initial word =
**0/1793** vs observed 06→29 = 5/46 = 10.9% (band-independent kill).

**Key methodological finding — the phonetic mute-e model.** The apparent
anomalies 06→77 ("stem+pas") and 06→11 ("stem+la") — a bare stem cannot
directly precede "pas"/"la" (the -e ending always intervenes) — dissolve
if the syllabary is phonetic and mute -e is unwritten (40=e exists for
*pronounced* /e/): "demande pas" = /də.mɑ̃d/+/pa/ = ?+06+77 ✓;
"demande la" = ?+06+11 ✓; "demander"/"demandé" = /də.mɑ̃.de/ = ?+06+29 ✓;
06→40 = /mɑ̃/+/e/ ✓. So 06 = /mɑ̃/ verbal stem ("demand-/command-";
"demander"/"commander" are core diplomatic vocabulary).

**Polyvalence (proven, not hypothesized).** 82→06 occurs 4× (the "-ment"
family); those 4 NEVER take 29/11/77 (0/0/0) while the other 42 do
(5/4/6). Phonetically: /ɑ̃/+"er" ∉ French ("enter" is not a word), while
/mɑ̃/+"er" = "demander" ✓ — so the 82→06 subset (/ɑ̃/, "-ment") and the
06→29 subset (/mɑ̃/) are **phonetically incompatible as one syllable**:
group 06 merges ≥2 distinct syllables. Expected: 96 groups « ~700 French
syllables ⇒ heavy homophone-merging is the cipher's design, not a bug.
Residuals: 06→67 ×3 (06 in subject slot — 3rd value or clause boundary),
06→29→40 ×1 ("…ière"-type, likely a 3rd value).

## (b) Companion 67 (37 occ, rank 11)

Followers: 33×6, 77×6, 78×4, 11×3, 86×3, 64/76/46/08×2.
**67→29 = 0, 67→40 = 0, 67→34 = 0** — never takes endings ⇒ finite verb.
Predecessors: 21×8, 06×3, 20×3 (20 distinct, diversity 0.541).
Decisive chains: **67→33→29 ×3** ("veut parler": modal+infinitive-stem+er;
33→29 = 5/25 total, 33 is a confirmed -er stem), 67→78 ×4, 21→67→77 ×1
("les veut pas"), 21→67→33→29 ×1.

67 = modal/auxiliary **CONFIRMED** (7 checks): governs infinitives (1),
takes pas ×6 (2) / la ×3 (3) / que ×2 (4), never takes endings (5),
21→67 ×8 = object+"veut" (6). **"veut" singled out** over peut/faut (7):
"les veut" ✓ ("il les veut") vs "les peut" ✗ vs "les faut" ✗ —
only *vouloir* takes direct objects among the candidates.

Pair pattern: follower cosine 06/67 = 0.375, Jaccard top-10 = 0.111;
shared predecessors ≥2×: only {06: (2,3), 30: (4,2)}; 06→67 ×3, 67→06 ×0.
**Not** same-verb-different-tense (67 finite-only, 06 takes -er); **not**
same-construction. They are **complementary verb-system slots**:
67 = modal governor, 06 = lexical stem. (67→06→29 = 0: 06 is not governed
by 67 as infinitive.)

## (c) 77 = "pas" under verb-stem 06 — CONFIRMED (6 checks)

1. Rate: 06→77 = 13.0% vs era P(pas|verb) = 5.46% (2.4×; attested).
2. 64→77 = 3: only grammatical X+"pas" for common X is "même pas"
   (64="même" — independently supported, §d-note) — kills 64="qui"
   ("qui pas" ✗; red-team hit on the provisional anchor, flagged).
3. 77→29 = 0 ✓ ("pas" never precedes bare "er").
4. **"pas vraiment"**: 77→78 ×7 (top follower); 78→40 ×3 = "vraie" ⇒
   78 = "vrai/vraie" ("pas vraiment/vraie", "veut vraiment", "la vraie").
5. 77 ≉ 46 distributionally (follower cosine 0.198, Jaccard 0.111) — "pas"
   should not pattern like "que" ✓.
6. 87→77 ×2 = "ce pas" (noun, "this step"): "pas"-adverb/"pas"-noun are
   homophones /pa/ — same group, no contradiction (cf. era P(pas|"ce") =
   0.09% would otherwise be 67× off; era P(que|"ce") = 10.76% noted).
Caveat: predecessors-in-V29 only 29.5% — V29 was miscalibrated for this
check (era pas-predecessors are *finite* verbs est/a/sont, which never
take -er); honest residual, not a refutation.

## (d) 77 = "que" rival — REFUTED as primary; scored honestly

For "que": "ce que" (87→77 ×2; era P(que|"ce")=10.76%); 06→77 = "dit que"-
class (era P(que|dit)=10.7%, sait 27.6%); 67→77 = "veut que" ✓.
Against "que" (decisive): follower-cosine vs 46="que" = **0.198** ("que"
must pattern like "que" — it doesn't); **64→77 = 3 is unexplainable**
("qui que" ✗, "ne que" ✗ — era P(que|"ne") = 0.0%, "même que" ✗);
rate 13.0% vs era P(que|verb) = 1.76% (7.4×); **77→78→40 = 0** kills the
que+subjunctive reading. The "ce que" point is absorbed by the
"ce pas"(noun) homophony (§c.6). Score: **pas wins decisively**.

## (e) Tension with WO1 (06="ent") — DISSOLVED

The 82→06 occurrences (4×: 94-82-06 ×3, 18-82-06 ×1) take **zero** verb
continuations (29/11/77 = 0/0/0); the other 42 take them 5/4/6. The two
06→06 bigrams are both "94-82-06 06" = "-ment"+"entr…" ("seulement
entrer"-type) — both 06-values adjacent across a word boundary. WO1's
"ent" (/ɑ̃/, word-final "-ment") and this WO's stem (/mɑ̃/, word-initial)
are **different syllables sharing group 06** — proven phonetically
(/ɑ̃/+"er" ∉ French) and distributionally (clean split). **No forced
choice, no position-dependent roles needed.** Note for WO1: if 06="ent",
06→29 = "entrer" requires the syllabary to chunk "entrer" as "ent"+"er".

## Bonus leads for the lane (out of WO scope, no claim)

- 64="même" (46×, tied 4th): survives 87→64 ("ce même"), 64→77 ("même
  pas"), 64→29 ("même erreur"), 67→64 ("veut même"); "ne"/"qui" die on
  64→29 (era 0/1793) and 64→77 respectively. Red-teams provisional 64="qui".
- 21="le/les" (object pronoun): 96→21 ("par les"), 33→21 ("demande-les"),
  21→67 ("les veut"), 21→64 ("les mêmes").
- 00="de" (rank 1, 54×): 00→33 ×8 ("de parler"), 06→00 ×4 ("demande de").
- 33 = lexical -er stem governed by 67 ("veut parler" ×2).

## Best next step

1. Add **homophone-merging** to the lane's cipher model (96 groups « ~700
   syllables; groups are sounds, not words — "pas"/"pas", mute-e unwritten).
2. WO1: treat 06 as polyvalent (/ɑ̃/ vs /mɑ̃/); reconcile "ent"+"er"
   chunking for "entrer".
3. Open WOs: 64="même" (with 64="qui" red-team), 21="le/les", 00="de",
   78="vrai", 33's identity; resolve 06→67 ×3 (subject-slot residual).
