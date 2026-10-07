# Red Team — crowd round 3 (2026-10-07)

Executor: RED TEAM (kill authority over every new CONFIRMED claim this round).
Every cipher count re-derived from `crib_attack.load_pairs()` (run from `code/`);
every era rate re-derived from Tocqueville t1+t2 with the attempt-3 tokenizer.
Machine verdicts: `red_team_results.json`. Reviewed: closer, morphologist,
stem hunter, scorer smith (round 3), plus the tuner (7th executor, material to
the phase-instrument question).

## Verdict table

| # | Claim (worker) | Verdict |
|---|---|---|
| 1 | 87="ce" PROMOTED to CONFIRMED (closer) | **DEMOTE** → PROVISIONAL (strengthened) |
| 2 | 94="ne" CONFIRMED (morphologist) | **DEMOTE** → PROVISIONAL (strong) |
| 3 | 06="ent" general REFUTED (morphologist) | **UPHOLD** (two legs downgraded) |
| 4 | 94-82-06 family PLAUSIBLE (morphologist) | **UPHOLD** |
| 5 | 06=/mɑ̃/ "demand-/command-" CONFIRMED (stem hunter) | **KILL** (ground-truth contradiction) |
| 6 | 06=verb stem, class-level (stem hunter) | **DEMOTE** → PROVISIONAL (CONFIRMED never earned) |
| 7 | 06 polyvalent (/ɑ̃/+/mɑ̃/) CONFIRMED "proven" (stem hunter) | **DEMOTE** → PLAUSIBLE |
| 8 | 67="veut"-class modal CONFIRMED (stem hunter) | **DEMOTE** → PROVISIONAL (class); "veut" PLAUSIBLE |
| 9 | 77="pas" CONFIRMED (stem hunter) | **DEMOTE** → INCONCLUSIVE (round-2 status) |
| 10 | 77="que" REFUTED (stem hunter) | **DOWNGRADE** → DISFAVORED |
| 11 | 06-tension DISSOLVED (stem hunter) | **DEMOTE** → OPEN ("coexistence under test") |
| 12 | scorer BROKEN-ON-CONTROL (scorer smith) | **UPHOLD** |
| 13 | phase→position NULL (tuner) | **UPHOLD** (endorse) |

---

## 1. Closer: 87="ce" → DEMOTE to PROVISIONAL

**Re-derived (all reproduce):** n(87)=32, rank 16/96 1-based, share 1.733%;
followers {11:7, 64:5, 46:3, …}; P(11|87)=7/32=0.2188 CI [0.110,0.388];
P(64|87)=5/32=0.1562 CI [0.069,0.318]; P(46|87)=3/32=0.0938 CI [0.032,0.242];
14 distinct predecessors; all three 87→46 have predecessor 96 (@225/@952/@1526);
87 is the #1 predecessor of 11=la (7 vs 00:4, 06:4, 47:3, 67:3…).
Era: n("ce")=1134, compounds cela 47 / ceci 74 / cet 121 / cette 529 / ceux 287 /
celui 168 / celle 144 / celles 68; denom ce+cela=1181, full-morpheme=2572.
Wilson CIs verified. 87-inversion re-derived: "ce" the only n>100 era word
passing both bigram legs (next: puissances n=23, objets 62, celles 68, …);
#1 on Les Mis. 24-inversion: empty under era, Les Mis, and union — verified.

**Upheld (the analysis is strong):**
- **N1 rival battery:** se/ne/le/je/on/en die on grammatical count-zeros
  (n≥669) against the cipher's 95% CIs; "ce" inside both. This is the strongest
  evidence 87="ce" has ever had — count-zeros, not band judgments. The
  {cela, ce que} pair alone kills all six without the provisional 64="qui"
  prong (verified: all six outside CI [0.032,0.242] on P(que|R) and outside
  [0.110,0.388] on P(la|R)).
- **N2 inversion:** "ce" unique frequent fit; exhaustive over ~4,000 words.
- **C1 correction:** F19's era P(ce|par)=132/1036=0.1274 was wrong — 132 is
  n("parce"), not the (par,ce) bigram. True word-space P(ce|par)=13/1036=
  **0.0125** (verified). The syllabary-aware repair —
  n(parce)/(n(par)+n(parce))=132/1168=0.1130 vs cipher P(87|96)=3/21=0.1429
  (**1.26×**, verified) — is strictly better than F19's number. 96="par"
  keeps its status on a repaired leg.
- **P(que∨qu|"parce")=132/132=1.0000** (verified: 43 que + 89 qu'): every
  "parce" takes que/qu'. The frame leg is real.
- **24-inversion mixed-union:** still empty. Robust null, honestly reported.

**Broken checks (why not CONFIRMED):**
- **B1 — traceability break.** `closer_results.md`'s steelman headline ratios
  (P_qui 1.15×, P_que 1.10×, cela 5.5×) use denominator **1181** (ce+cela
  only). But `closer.py`'s archived `ce_model` uses denominator **2572**
  (all compounds), giving 1.89×/1.98×/12× — with the que-leg at the
  **1.98× band edge** (cf. round-2 B2: survival decided by 0.03 of ratio).
  The .md's favorable denominator is post-hoc ("no te/x spike" is an
  observation, not a pre-registered modeling choice) and the numbers do not
  trace to the archived code/JSON. REPORTING.md violation. The inbox note
  honestly gives the range ("era 5–12×"), the .md headline does not.
- **B2 — invalid corroboration.** R1's "independent corroboration" recycles
  round-2's P(87|24)=0.1923 as "est ce" register evidence. That number's
  meaning died with 24="est" (killed round 2); 24 is unidentified, so 0.1923
  cannot corroborate anything about "ce". The legitimate register evidence
  is F10 (cela 6.7× gap, attempt 3) — and the JSON-version cela-fail
  (**12×**) exceeds even that gap.
- **B3 — circular leg.** N3 (96-frame) is admitted mutual support with
  96="par" (which used 87="ce" as a leg). Cannot count toward CONFIRMED.
- **B4 — failing headline leg.** The cela-leg (7/32, the most distinctive
  check) fails the lane's era instrument at 5.5×–12× depending on the
  post-hoc denominator; the 87-inversion excluded it by caveat. A CONFIRMED
  grade cannot rest on 2/3 legs with the most distinctive leg failing on
  the primary instrument.

**Net:** 87="ce" stays PROVISIONAL — upgraded from "best-tested" to
"rival-excluded on counts, inversion-unique". The closer's honesty points
stand (falsifiers listed, N3 circularity admitted, 82↔87 Jaccard anomaly
flagged, rivals given equal rigor — no strawmanning).

**Blocked downstream:** 64="qui" re-promotion: **NO** — its check (b) still
conditions on a provisional, and it has a new anomaly (see §8 note below:
64→77×3 vs era P(pas|"qui")=0/2360). 96="par" keeps round-2 status. All
drags using 87 inherit provisional uncertainty.

---

## 2. Morphologist: 94="ne" → DEMOTE to PROVISIONAL

**Re-derived (all reproduce):** 94→82 = 4× @[578,1181,1352,1741]; @1181 inside
repeat #1 — the WO's "@578/@1181 extras" was wrong; true extras @578/@1741,
and @1741 is 94-82-**46**, not -06 (morphologist's correction verified).
Trigram 94-82-06 = 3× @[578,1181,1352]; 5-mer 77-78-94-82-06 ×2 @1179/@1350
byte-identical; 82→94 = 3× @[650,1100,1574], all "52-82-94-76/74";
82→06 non-94 @737 ("18-82-06-00").

**Broken checks:**
- **B1 — void instrument.** Leg 3 ("phase medial") uses the contactor
  phase→position mapping the tuner **falsified** (A=medial falsified
  outright: 0/4 A-anchors modal-medial; LOO phase-constrained 2/34 vs
  baseline 6/34). The morphologist's §a ("06 not word-final", p≈0.001)
  inherits the same void instrument.
- **B2 — non-discriminating leg.** Trigram rate cipher 3/1844=0.163% matches
  BOTH era -nement (529 words, 0.246%, 0.66×) and **-rement** (274 words,
  0.128%, **1.28×**). Live rival **94="re"** ("-rement": entièrement 61,
  particulièrement 23, proprement 21, …) is rate-competitive (scorer-seg
  P("re")=0.0149 vs P("ne")=0.0147, both ~1.3× under cipher 0.0195) and was
  killed only on overstated "m-re impossible" geometry. Round-4 lead: test
  the -rement family.
- **B3 — unexplained instances.** @1741 ("12-i-ne-m-que-56") unparsed: 25%
  of the 94→82 family. 82→94×3 ("52-m-ne-76/74") unexplained under "ne".

**Upheld:** WO correction; rate leg 1.025× (36/1846 vs era 6886/362028,
verified); rival 94="en" kill (1.79× + "en-m-ent" is no word — solid);
**the refutation attempt was genuine and exemplary** — corrected the WO
against its own test bed, ran six counter-arguments, refuted its own
06="ent", graded the family PLAUSIBLE not CONFIRMED.

**Net:** 94="ne" → PROVISIONAL (strong: best rate match + "en"-kill + trigram
coherence). Not CONFIRMED: one independent check (rate) + conditional
coherence + rival exclusion ≠ two independent checks.

---

## 3. Morphologist: 06="ent" general REFUTED → UPHOLD (legs downgraded)

The refutation direction is correct, but two legs need downgrading:
- **Phase leg VOID** per tuner NULL (the p≈0.001 calculation assumed
  unvalidated B=word-initial).
- **"ent|er ungrammatical" OVERSTATED.** 62 "enter"-words in era
  (présenter 14, représenter 12, augmenter 12, tenter 9, …). Downgrade to
  "strained": 5/46 as "ent|er" needs enter-splits at ~2.4× the era
  enter-word rate **plus** an unattested split convention.

**Standing legs:** rate 1.26× over the generous era upper bound (band
uncalibrated — noted, not hidden); 06→29×5 strained as "ent|er"; the
positive F21 case from both workers. 06="ent" survives only as the
**restricted, PLAUSIBLE** claim on the 3 -ment instances (polyvalence
uncorroborated) — upheld.

---

## 4. Stem hunter: 06=/mɑ̃/ "demand-/command-" CONFIRMED → KILL

**Kill reason — ground-truth contradiction (same structure as H5-K2).**
The claim requires mute -e to be **unwritten** ("demande pas" = ?+06+77,
"demander" = ?+06+29). But the pencil-crib ground truth "la première" =
11-70-82-34-29-40 writes **40="e" for the mute final -e** of "première"
(/pʁə.mjɛʁ/). The cipher demonstrably writes mute -e, so "demande" would be
?+06+40 and "demande pas" ?+06+40+77 — observed **0×**. The 6× 06→77 cannot
be "demande pas". The phonetic mute-e model, load-bearing for all four
"checks" (it converts 06→77/11 from ungrammatical to confirming), is
refuted by the crib. **KILL** the /mɑ̃/-specific CONFIRMED claim.

**Demoted remainder:** 06=verb stem (class-level, F21's original claim)
reverts to **PROVISIONAL** — the CONFIRMED was never earned. What survives:
06→29×5 (infinitive slot), 30 distinct predecessors, the 06="ne" kill
(era ne+er-initial 0/1793 vs 5/46 — band-independent). What does not:
- (a) compat 37% is **circular** (counts 06→77 assuming 77="pas"/"que",
  the very hypotheses under test) and **ungrammatical** (06→11 "la-object",
  06→70 "pre" as "verb continuations" of a bare stem). Honest paradigmatic:
  06→29/40/34 = 6/46 = **13%**.
- **V29 is contaminated**: 4/10 members are ground-truth non-stems
  (11=la, 46=que, 40=e, 34=i). "Takes 29≥2×" ≠ stem-ness. The (c) 29.5%
  predecessor-verbness is inflated (worker honestly flagged the
  miscalibration in its inbox note — finite verbs don't take -er).
- 0-based ranks vs the lane's 1-based convention.

**Honesty:** the stem hunter CONFRONTED the 06-tension head-on (§e:
partition by predecessor-82, both 06-06 contexts, "entr" exploration) —
did not dodge. But §e's note contains a letter-alignment error ("entrer"
cannot chunk as "ent"+"er": e-n-t-r-e-r ≠ e-n-t+e-r; the "enter"-words are
présenter-type). And "if 06='ent', 06→29='entrer'" confuses "ent" with
"entr".

---

## 5. Stem hunter: 06 polyvalent CONFIRMED → DEMOTE to PLAUSIBLE

"/ɑ̃/+'er' ∉ French" is **false** (62 enter-words, §3). The /mɑ̃/ side is
killed (§4). What remains — the distributional split (82→06 4× take
29/11/77 at 0/0/0 vs 5/4/6 elsewhere) — is suggestive at n=4, not proof.
"96 groups « ~700 syllables ⇒ homophony" makes polyvalence PLAUSIBLE, not
proven. (Agrees with the morphologist's restricted-PLAUSIBLE.)

## 6. Stem hunter: 67="veut"-class CONFIRMED → DEMOTE to PROVISIONAL

Solid distributional core (upheld): takes pas/la/que (×6/×3/×2), never takes
endings (67→29/40/34=0) — a genuine finite-verb profile. But:
- Check 1 (67→33→29 ×3, verified) depends on 33 being a "**confirmed**
  -er stem" — 33 is unconfirmed (V29 member only); the .md says ×3 in §b
  and ×2 in the bonus lead.
- Checks 6–7 depend on **21="les"** (unconfirmed bonus lead); the worker's
  own inbox note admits 21→67→33→29 is "ungrammatical under 21='les'".
- The {veut, peut, faut} candidate set is arbitrary.
→ PROVISIONAL (finite-verb/modal class); "veut" specifically PLAUSIBLE.

## 7. Stem hunter: 77="pas" CONFIRMED → DEMOTE to INCONCLUSIVE

- Check 1: 2.4× over the era mean, cherry-picked high end (faut 11.2%);
  band uncalibrated.
- Check 2: conditional on unconfirmed 64="même" — circular as a
  confirmation leg. (It IS a legitimate red-team hit on provisional
  64="qui", see note below.)
- Check 4: internally inconsistent — 78="vrai" (for 78→40="vraie") vs
  78="vraiment" (for 67→78); "pas vrai" vs "pas vraiment" muddled.
- Check 6: a 67× era gap (P(pas|"ce")=0.09% vs cipher 6.25%) excused by
  "pas"-noun homophony — an excuse, not evidence.
→ INCONCLUSIVE (round-2 status; best-tested rival, not confirmed).

**Note — new anomaly for 64="qui" (provisional):** 64→77×3 (verified) vs
era P(pas|"qui")=**0/2360**. "qui pas" is ungrammatical (sentence-boundary
or pas-noun readings strained at ×3). "même pas" fits grammatically but is
5.3× over era. 64="qui" is pressured, not killed; re-promotion is OFF.

## 8. Stem hunter: 77="que" REFUTED → DOWNGRADE to DISFAVORED

Direction right (follower-cosine 0.198 vs 46="que" is real; 7.4× rate),
but the legs are distributional/band-based, not grammatical — not
refuted-grade. Round-2 INCONCLUSIVE was the honest grade; "disfavored" now.

## 9. Stem hunter: tension DISSOLVED → DEMOTE to OPEN

The /mɑ̃/ side is killed and "/ɑ̃/+'er' ∉ French" is false, so the
"dissolution" fails. The morphologist's "coexistence under test" stands:
F21 the working general reading, restricted-"ent" PLAUSIBLE on 3 instances.

---

## 10. Scorer smith: BROKEN-ON-CONTROL → UPHOLD

**Control-first rule RESPECTED — exemplary.** Pre-registered bar
(top1≥3×chance ∧ MRR≥0.30 ∧ n≥10): top-1 0.045 vs chance 0.0112 (4.0×,
passes the sub-bar), MRR 0.217 < 0.30 → BROKEN. Real drag NOT run. Correct.
Note: the "support" signal is saturated (median 1.000 for true and top-1
alike) — the consistency signal does not discriminate; diagnosis TODO
unfilled (minor).

## 11. Tuner: phase→position NULL → UPHOLD (endorse)

LOO phase-constrained 2/34 vs baseline 6/34 across 4 configs; A=medial
falsified at anchor level (0/4 modal-medial); the tune disagrees with
itself on flagship anchors across rules (29=er final/modal-medial;
40=e initial/final). **Critical calibration finding:** cipher 29 is 2.55%
of pairs (rank 3) vs corpus bare-'er' 0.038% — a **67× segmentation
mismatch**. The 1841 syllabary's "er" ≠ any rule-based segmenter's "er".
**Consequence:** every corpus rate check involving "er" (06→29, V29,
-er paradigms) is uncalibrated until the syllabary's own segmentation is
recovered (tuner step 2: read `data/upstream-syll*.py`). This VOIDS the
morphologist's phase legs (§2-B1, §3) — applied above.

---

## 06-tension adjudication (round fault line)

**F21 (verb stem, class-level) is the better general reading** — both
workers converge (morphologist's tension table: 43/46 frames vs 3/46;
stem hunter's paradigmatic 06→29). **06="ent" general REFUTED**
(upheld, legs downgraded). **06="ent" restricted to the 3 -ment trigrams:
PLAUSIBLE** (polyvalence uncorroborated). Neither worker holds a CONFIRMED
claim on 06 anymore: the stem hunter's /mɑ̃/ CONFIRMED is KILLED
(§4), its class claim reverts to PROVISIONAL; the morphologist never
claimed CONFIRMED on 06. No methodology is "wrong" in a kill-sense — but
the stem hunter's V29/compat machinery must never be cited as establishing
F21, and the morphologist's phase legs are void per the tuner.

## Mixed-register model (work-order item c)

**Principled as a robustness check, not as a confirmation instrument.**
The closer's documented union (fit if EITHER corpus passes) is the
charitable-to-hypothesis version — and the 24-intersection is STILL empty,
which makes the null strong rather than weak. As a confirmation
instrument it is unfalsifiable-adjacent: any failing leg can be excused as
"register". Standing rule for future rounds: a register excuse must (i)
cite a measured gap (F10-style), (ii) show both denominators/instruments,
(iii) favor no rival. The closer met (i) and (iii) but not (ii) in the .md.

## Methodology flags for the lane

- **M1:** Phase→position instrument VOID (tuner). No phase-position
  arguments until the rotation's meaning is found.
- **M2:** 'er' 67× segmentation mismatch — resolve before any corpus tuning.
- **M3:** Factor-2 band UNCALIBRATED (standing); closer's que-leg at 1.98×
  shows the edge arbitrariness is load-bearing.
- **M4:** The crib writes mute -e (40 in "première"). Phonetic models must
  account for it — kills "mute-e unwritten" cleanly.
- **M5:** Homophony/polyvalence is now an open question (two workers,
  96 groups « ~700 syllables). The lane needs a position, not an
  assumption — but "proven" at n=4 is overclaimed.
- **M6:** Traceability — .md numbers must reproduce from archived
  code/JSON (closer violated; REPORTING.md rule).
- **M7:** Rank convention is 1-based (stem hunter used 0-based).
- **M8:** V29 ("takes 29≥2×") is contaminated by known non-stems — not a
  stem proxy without anchor validation.

## Honesty audit summary

- **Morphologist's refutation: GENUINE (exemplary).** Corrected the WO's
  instance list against its own test bed, ran six counter-arguments,
  refuted its own 06="ent", graded the family PLAUSIBLE.
- **Stem hunter's tension: CONFRONTED, not dodged** (§e partition, 06-06
  contexts, "entr" exploration) — but verdicts overclaimed and the /mɑ̃/
  model crib-contradicted.
- **Closer's rivals: EQUAL RIGOR** — same battery, grammatical zeros, no
  strawmanning; falsifiers listed. (Headline selective in .md, honest in
  inbox note.)
- **Scorer smith: control-first RESPECTED.**

## Best next step

1. **87="ce":** needs a register-matched corpus (1830s–40s diplomatic
   despatches) or a second ce-collocation anchor (the groups for "ci"/"te"
   testing ceci/cette spellings). Repair closer .md traceability first.
2. **94:** test **94="re"** ("-rement" family) as the live rival;
   resolve @1741 and 82→94×3 ("m'en" vs "mne"-words).
3. **06:** identify the stem — 06→29×5 infinitives + 30 distinct
   predecessors is the thread; test restricted-"ent" via @737
   (18→82→06→00).
4. **64="qui":** address the 64→77×3 anomaly (era 0/2360); do NOT
   re-promote; "même" rival stays open.
5. **77/78:** resolve — 78="vrai" vs "vraiment" conflict; the repeat's
   "gouvernement" parse needs 77/78 ("gou"/"ver" both phase-weak).
6. **Cipher model:** resolve the 'er' segmentation (read
   `data/upstream-syll*.py`); take an explicit position on homophony.

## Caveats (not verified)

- Elision handling of the cipher remains uncalibrated (round-2 standing).
- Injectivity (one group = one value) is now questioned, not assumed —
  no replacement model is validated.
- Era corpus is Tocqueville (political essay), not diplomatic despatches;
  the register gap is measured (F10) but the true register is unknown.
- The closer's Les-Mis leg figures were re-derived from the local Les Mis
  text; the dialogue-register inference is the closer's, audited as above.
- 94="re" rival is red-team-constructed (rate-checked), not worker-tested.

## Other round-3 material (no promotion claims; not ruled on)

- **Segmenter** (`segmenter.py`, `segmenter_results.{json,md}`): word-boundary
  semi-Markov model. No verdict claimed; the instrument reads as NULL/broken:
  the era prior alone scores boundary 22/22 (edge LRs add nothing), MAP
  degenerates to mean word length 1.15 pairs vs era 1.75 syllables
  (chi²=618.8), and the "la première" checkpoint shows internal boundary
  posteriors ~0.95 (should be low inside "première"). Do not use for
  word-final arguments until repaired.
- **Bigram battery** (`battery.py`, `bigram_battery_raw.json`): raw L1/L2/L2b/L3a
  legs for 38 groups × candidate readings. Data product only — zero
  "confirm/promot/verdict" tags. No claims to rule on; the L3a grammatical
  kills are usable inputs for future WOs.
- **frenchman** (`frenchman_dump.py`, windows txt): ear-check window dumps
  with PROV including 94="ne" (provisional). Helper, no claims.
