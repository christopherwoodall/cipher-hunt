# Phonetician pass 1 — fuzzy-equivalence rules for the Slider

Lane: `zeschau-seebach-1841` (R5005, French two-digit syllabary, 18 Jan 1841).
Authority of status: the red team (kill authority); the frenchman's ear-verdicts are
independent readings, not status promotions. This document turns the
spells-by-ear evidence into explicit, numbered, graded matching rules for the
Slider's fuzzy crib-bootstrap pass.

**Strength legend:** SOLID = ground-truth or kill-grade evidence (pencil cribs,
red-team kills); PROVISIONAL = attested but conditional, single-instrument, or
inference-from-scorer; SPECULATIVE = derived from a principle, not directly
attested — test before relying on it.

---

## RULES

### R1 — Mute final -e may be written as its own group (40) — SOLID
- **Rule:** when an era-French candidate word ends in mute -e, the match must
  ACCEPT the group 40 ("e") after the stem, e.g. `-re` → …29(er)+40(e),
  `-me` → …+40(e). Absence of 40 does not kill the candidate (see R7);
  its presence is positively licensed.
- **Evidence:** pencil-crib ground truth "la première" = 11-70-82-34-29-40
  = la|pre|m|i|er|e, with 40="e" standing for the mute final -e
  (STATE.md standing facts; `code/crowd3/frenchman_results.md` §2). Confirmed
  mid-letter back-reference (F12, STATE.md).
- **Scope/limits:** proven to occur. Does NOT mean always written. Red-team
  methodology flag M4/F26: phonetic models must account for written mute-e.
- **For the Slider:** never require mute-e absence; never forbid 40 after a
  candidate ending.

### R2 — Inconsistent cutting: one word, several segmentations — SOLID
- **Rule:** the same word may be cut differently in different positions of
  the SAME cipher. Match candidates against any cut compatible with R3/R9;
  do NOT demand cut-identity across instances.
- **Evidence:** "personne" appears as 93-52-94 = per|so|nne @160 AND as
  77-62-94 = pers|on|ne @508 — two spellings in one cipher
  (`code/crowd3/frenchman_results.md` §1 "94=ne" and §6.5; recorded in
  STATE.md as the main-fleet enlightenment). "la première" itself is cut
  hyper-fine: pre|m|i|er|e (§2).
- **Scope/limits:** proven mechanism, but n=1 word with dual attestations.
  Do not yet assume ALL words cut twice; assume cut-fuzziness, not
  cut-multiplicity.
- **For the Slider:** positional priors and rigid syllabification are VOID
  (F30, red-team M1). Tolerance for the ear, not the statistician.

### R3 — Spells by ear: silent consonants dropped — SOLID
- **Rule:** orthographic silent consonants may be dropped in favor of the
  pronounced sound. Match "prend" against 70="pre" (silent -d- dropped);
  generally, match candidate words against their PHONETIC realization, not
  their orthography.
- **Evidence:** "on ne prend pas" = 62-94-70-52 @1331 reads "…on ne
  pre[nd] pas…" — "prend" spelled "pre" (silent d dropped), "the finest
  window in the batch" (`code/crowd3/frenchman_results.md` §1 "94=ne").
- **Scope/limits:** attested for -d- ("prend"→"pre"). Generalization to
  other silent consonants (-s, -t, -x) is SPECULATIVE (R11) until observed.
- **For the Slider:** build candidate spellings phonetically first,
  orthographically second.

### R4 — The er|e split: -re may be cut as 29+40 — SOLID
- **Rule:** a word ending in pronounced -re may be cut as 29("er") +
  40("e"), i.e. the encipherer's own cut for "erre" in "qui erre" ×2
  (@290, @684). When matching a stem ending in -r- + mute-e, ACCEPT
  …29-40 as a full rendering of the ending.
- **Evidence:** "qui erre" ×2 (@290 `@…09 [qui] er e 65…`, @684
  `@…92 [qui] er e 65 [ne] er 60`): "29=er + 40=e compose 'erre' under the
  encipherer's er|e split" (`code/crowd3/frenchman_results.md` §1 "64=qui").
- **Scope/limits:** attested ×2 in the same formula. Does not pin whether
  -re is ALWAYS cut this way; combined with R7 it must not.
- **For the Slider:** do not demand a single "-re" group; 29-40 is a
  licensed -re rendering.

### R5 — Polyvalence: one group, several readings — SOLID (mechanism; unquantified)
- **Rule:** the same group may carry multiple readings, conditioned by
  position/context. 94 = "ne" (negation, @1331) AND "ne" word-internal
  ("per|so|nne" @160, "pers|on|ne" @508) AND "en" ("en ce" @1168,
  "m'en" @1575); 52 = "pas" (negation, @1331, @1293/@1806) AND "so"
  word-internal ("per|so|nne" @160); 06 = "-ent" in the 3 -ment trigrams
  AND verb-stem elsewhere (bare polyvalence visible @1181:
  "gouvernement" 06 vs the following stem-06).
- **Evidence:** frenchman §1 "94=ne" (conditioned "en" islets), §6 K5
  (52="so" kills 52="pas" as a single reading), §6 "06" (kill of 06="ent"
  general, restricted survival in 3 trigrams); red-team adjudication
  (STEM-HUNTER rulings 4–7, §9); STATE.md F25/F31 ("established as the
  cipher's mechanism", "unquantified").
- **Scope/limits:** the mechanism is established; its extent is UNQUANTIFIED
  (STATE.md work-order item 10: the lane's explicit open problem). Do NOT
  cite it as proven for a specific group beyond the attested ones.
- **For the Slider:** keep multiple readings per group; do not prune on a
  single established value.

### R6 — Elision: 11="la" may double as "l'a" — PROVISIONAL
- **Rule:** elided forms may be written with the base word's group: "l'a"
  may appear as 11 alone. Do not demand a separate "l'" group before "a".
- **Evidence:** @725 `…65 [qui] la 00 86…` — "qui la 00" is rescued as
  "qui l'a 00" ("who has/saw it done") IF 11=la doubles as "l'a"; otherwise
  it jars (`code/crowd3/frenchman_results.md` §1 "64=qui"). Round-2
  standing: elision handling remains uncalibrated
  (`code/crowd3/red_team_results.md` caveats).
- **Scope/limits:** one conditional instance; rescue-type evidence only.
  Generalization to other elisions (d'un, s'en, qu'il) is SPECULATIVE.
- **For the Slider:** when "la" + vowel-initial context produces a jar,
  try the elided reading before killing the window.

### R7 — Final -er: written (R4) OR stripped — PROVISIONAL
- **Rule:** word-final -er may appear as bare 29 after the stem, OR as
  29+40 (R4), OR be stripped entirely (encipherer strips final "-er",
  scorer smith inference F22, STATE.md crowd-round-2). All three are
  licensed renderings of infinitive/future -er endings.
- **Evidence:** F22 "encipherer stripped final '-er' (inference from scorer
  smith — provisional)" (STATE.md). R4 shows the written variant exists
  ("erre" = 29+40). 06→29×5 as infinitive slot frames (stem hunter,
  STATE.md).
- **Scope/limits:** F22 is an inference, not a crib — provisional. The
  Frenchman's ear prefers the 06→29 frames as true infinitives.
- **For the Slider:** when matching an infinitive, accept stem+29, stem+29+40,
  and stem alone (with the stripped form as the weakest variant).

### R8 — Orthographic doubles spelled once (by-ear corollary) — PROVISIONAL
- **Rule:** geminate consonants in orthography may be spelled once, since
  French pronounces one: "erre" /ɛʁ/ is written 29+40 = "er"+"e" (single-r
  sound), not "er"+"re" with a doubled r.
- **Evidence:** same "qui erre" windows as R4 (@290, @684;
  `code/crowd3/frenchman_results.md` §1 "64=qui"): the cut 29=er + 40=e
  renders a four-letter "-rre" tail as two groups with one r-sound.
- **Scope/limits:** ×2 in one formula; a corollary of R3, not an
  independent observation.
- **For the Slider:** when aligning candidate text against groups, collapse
  orthographic doubles to their single pronounced consonant.

### R9 — Letter-level cutting: down to single letters — SOLID
- **Rule:** the encipherer cuts as finely as single letters. 82="m",
  34="i", 40="e" are single-letter groups in the ground-truth crib
  (pre|m|i|er|e). Candidates may be rendered one group per letter.
- **Evidence:** pencil-crib ground truth "la première" = 11-70-82-34-29-40
  (STATE.md standing facts; `code/crowd3/frenchman_results.md` §2 notes
  "the encipherer descends to the letter"). Cited in
  `code/crowd3/red_team_round3b_results.md` §(f).
- **Scope/limits:** proven. Do not invert: not every group is a letter
  (29="er", 70="pre" are syllabic in the same crib).
- **For the Slider:** both letter and syllable granularity must be tried;
  a mixed letter+syllable segmentation is the NORMAL case, not an
  exception.

### R10 — Readings are position-conditioned — PROVISIONAL
- **Rule:** a polyvalent group's reading is expected to segregate by local
  position/context rather than alternate freely: at @1181 the 06 INSIDE
  "gouverne|ment" reads "-ent" while the 06 IMMEDIATELY FOLLOWING the
  trigram reads as a verb stem ("le gouvernement [décide]") — "polyvalence
  seen with the naked eye" (frenchman §6 "06").
- **Evidence:** `code/crowd3/frenchman_results.md` §6 "06"; red-team §9
  (morphologist's coexistence table 43/46 vs 3/46; 82→06 4× vs 5/4/6
  split on 29/11/77 elsewhere).
- **Scope/limits:** distributional, n small; the conditioning variable is
  not yet identified (not word-position phases — tuner NULL).
- **For the Slider:** condition candidate readings on local predecessor/
  successor context, not on global phase/position.

### R11 — Silent-consonant dropping generalizes beyond -d- — SPECULATIVE
- **Rule (do not use for kills):** if R3 holds, silent -s, -t, -x, -p
  ("temps"→"tan", "fils"→"fi") and other mute letters may likewise be
  dropped. TEST as a generator of candidates only.
- **Evidence:** none direct; derived from R3 + R2's "writes by ear" principle.
- **Scope/limits:** untested hypothesis. Any match found this way needs an
  independent leg before it counts for anything.

---

## FORBIDDEN BY THE EVIDENCE

These are not opinions; each killed a lane claim. The Slider must not
reintroduce them.

1. **Mute-e-always-unwritten models.** KILLED by ground-truth contradiction:
   the 06=/mɑ̃/ "demand-/command-" CONFIRMED claim died because it needed
   mute-e unwritten ("demande pas" = ?+06+77, "demander" = ?+06+29) while
   the crib writes 40="e" for mute final -e in "première"; observed 06→40→77
   is 0× (`code/crowd3/red_team_results.md` §4; STATE.md N17, M4/F26).
2. **Rigid syllabification / era-syllable-conditional rate legs on
   morphological or phonetic fragments.** VOID — "rigid syllabification
   DEAD as an instrument (F30)" (STATE.md); "no era-syllable-conditional
   rate … on morphological/phonetic fragments" (round3b explicit rule);
   red-team M1 (phase→position VOID).
3. **Era rate/attestation legs on groups 29, 82, 34, and era-'e'-conditionals
   on 40.** Cipher "er" is 2.55% of pairs (rank 3) vs corpus bare-"er"
   0.038% — a 67× segmentation mismatch; red team round3b excludes
   29/82/34 and adds: "40='e' CONDITIONAL legs are uncalibrated too — the
   era 'e' syllable ≠ the cipher's word-final mute-e 40."
4. **V29 ("takes 29≥2×") as a stem proxy.** CONTAMINATED: 4/10 members are
   ground-truth non-stems (11=la, 46=que, 40=e, 34=i) (red-team M8).
5. **Single-reading absolutism.** 52="pas" as a single reading died on
   "per|so|nne" @160 (frenchman K5); 06="ent" general died (§6, red-team §3);
   94="ne" exclusive of "en" died on the two "en" islets (frenchman §1);
   77="pas" REFUTED→DISFAVORED-strong (round3b). Injectivity
   (one group = one value) is questioned, not assumed (red-team caveats).
6. **06 = specific stems (demand-, command-, …).** The /mɑ̃/ CONFIRMED
   claim was KILLED (§4, N17); letter-alignment errors ("entrer" cannot
   chunk as "ent"+"er") documented. 06 remains a provisional verb-stem
   CLASS (F21), never a specific stem.
7. **Formulas missing a mandatory constituent.** The frenchman killed its
   own "ce n'est pas cela" reading of @163 because "est" is missing
   ("ce ne pas cela" is ungrammatical) (frenchman K6). Do not fuzzy-match
   a formula across a missing required word.
8. **Value-specific grammar kills:** 24="de" inside "en ce qui" (K2:
   "de ce qui concerne" ungrammatical); "parmi c'est" — 87+01="c'est"
   cannot combine with "parmi" (K3); 01="ci" (K4: rate 3.84× over, "ici" ×0).
9. **Factor-2 band judgments and register excuses without the three
   conditions.** The factor-2 band is UNCALIBRATED (M3); the que-leg at
   1.98× shows edge arbitrariness is load-bearing. A register excuse must
   (i) cite a measured gap (F10-style), (ii) show both
   denominators/instruments, (iii) favor no rival (red-team
   mixed-register section).
10. **Treating provisional anchors as confirmed.** 87="ce", 64="qui",
    96="par", 94="ne" are PROVISIONAL (red-team authority). Any fuzzy
    match conditioning on them inherits provisional uncertainty; the
    frenchman's "CONFIRMÉ À L'OREILLE" verdicts are independent ear
    findings, not status promotions (authority note, frenchman_results.md).
11. **Homophony hand-waves.** A systematic rate gap (e.g. cipher vs era
    67×) excused by "pas"-noun homophony "is an excuse, not evidence"
    (red-team §7 on 77="pas"). Polyvalence is PLAUSIBLE, not proven, at
    n=4 (red-team §5).

---

## How the Slider should use this

- Match era-French candidate words against group sequences under R1–R9 as
  fuzzy equivalence: write the candidate the way the encipherer hears it
  (R3), cut it inconsistently (R2), allow letter granularity (R9), allow
  er|e for -re (R4), write mute-e (R1), and never forbid the alternative
  readings of polyvalent groups (R5, R10).
- Apply R11 only as a candidate generator, never as a discriminator.
- Reject any leg that violates items 1–11 of FORBIDDEN; that is the
  red-team's bar, and it has already killed better claims than ours.
