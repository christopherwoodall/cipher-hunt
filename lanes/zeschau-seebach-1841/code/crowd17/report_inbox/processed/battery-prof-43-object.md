# Battery verdict: prof-43-object — 43's class census for the two-word parse's left edge

- Target: `prof-43-object`
- Claim: 43's class census to decide the two-word parse's left edge
- Worker: battery worker prof-43-object (2cf0c2c8-b946-45d3-bd78-dbcae76ae036)
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). 1,847 pairs / 96 types re-verified in-session. `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched. No data invented. @-offsets are 0-based global stream indices (the lane's battery convention).
- Lock: created `code/crowd17/next-token/locks/prof-43-object.lock` on start, deleted on completion.
- Note: the dispatch brief says PRIORITY 3; the queue entry says priority 2 (set by `battery-seg-81-30-boundary`). Queue value kept; discrepancy noted, not "fixed" (priority is the supervisor's field).

## 1. Bar (verbatim from battery-queue.json)

"Name 43's class with >=3 frame legs; if "43 81" forms a direct-object NP under 81-noun, the "…[88] [43] [81] pas" ne-drop-negation parse becomes promotable and this fence re-opens."

Numbered clauses (pre-registered before testing):
- **C1:** Name 43's class with ≥3 frame legs.
- **C2 (conditional):** IF "43 81" forms a direct-object NP under 81-noun, THEN the "…[88] [43] [81] pas" ne-drop-negation parse becomes promotable AND the `seg-81-30-boundary` fence re-opens.

## 2. Method

- Re-derived the repaired stream in-session. 43 census: **n=16** at 0-based @21/@43/@244/@258/@343/@386/@439/@563/@1027/@1092/@1126/@1204/@1303/@1305/@1544/@1724 — byte-identical to the noun-43 battery's independent census.
- 81 census: n=14; left-neighbor census and "43 81" bigram frequency re-derived (§4).
- Standing values adopted, not re-litigated (protocol §5 — never downgrade an existing verdict):
  - F119 (battery-PROMOTE, class-level): 88 is VERB-CLASS (verb stem/governor); 88 takes zero infinitive-class complements; preposition rival rejected.
  - F150 (battery-PROMOTE, class-level): 81 = masculine abstract noun ("le [81]" ×3 legs; "81 pour + INF" purpose-complement diagnostic).
  - F89 (battery-PROMOTE): 30 = "pas" (ne-frame legs @558/@1713-class, not @45).
  - battery-noun-43 (NULL, 2026-10-09): noun-value survivor set empty; "@21 independently kills every monovalent noun at kill grade"; "the noun-43 line is closed at battery level pending red-team act".
  - battery-43-29-segment (PROMOTE, 2026-10-09): @21 "43 29" is word-internal "[43]er" (infinitive, "…qui vient me [43]er ce"); "43 keeps noun standing in 15/16 windows; the verb-stem shape is escalated to the red team"; bar explicitly states **"do not re-name 43 at battery level"**.
  - battery-la-frame-52-37-43-noun (NULL, 2026-10-09): Type-A parse "la [52-37-adj-unit] [43-head-noun]" fenced as RED-TEAM-GATED pending redteam-43-polyvalence.
  - battery-par43-adverbial-attestation (PROMOTE, 2026-10-09): bare "par mesure"/"par condition" adverbial escape closed (Littré + TLF); "par-43 kill is terminal pending only the @21 polyvalence adjudication".
  - battery-frame-43-21-43-doublet (KILL): "43 21 43" at @1303/@1305 are canonical-offset objects (dissolve under either adjacent row's rival offset).
  - battery-seg-81-30-boundary (NULL, 2026-10-09): the @44–45 "81 30" junction fenced; its C2 analysis named the candidate frame "…[88-verb] [43] [81] pas…" needing three ungranted assumptions (88 finite, 43 = NP-internal modifier, clause-final "pas"). This target is its follow-up #2.
  - battery-frame-43-pour-que-1544 (NULL, 2026-10-09): @1544's boundary-vs-government adjudication unresolved at battery grade.
  - Protocol §7: 67 et/veut is the sole true polyvalence.

## 3. Window-level evidence: the 43 class census

Exclusions applied before leg-counting: @21 is word-internal (verb stem, confirmed — not a standalone frame); @1303/@1305 are canonical-offset objects (doublet KILL — not genuine frames).

**Noun-shaped frames:**
- **@563 (a3_02)** — STRONG: `30 67 11 [43] 24 80 97` = "[30] et(67) la(11) [43] [24]". Determiner "la" directly before 43; finite/modal 24 follows: "et la [N] [V]". Clean head-noun frame.
- **@1204 (a7_00)** — STRONG: `45 58 47 [43] 55 61 21` = "ce(45) [58] ce(47) [43] [55] [61]". Determiner "ce" directly before 43; verb-class 55 follows: "ce [N] [V]". Clean head-noun frame. (Adjective impossible after "ce".)
- **@439 (a2_09)** — MODERATE: `63 45 46 [43] 98 80 50` = "[63] ce(45) que(46) [43] [98] [80]". "que [43] vient(98)": "que [N] vienne [80]" ("that [N] comes …") is grammatical; "que [V-fin] [V-fin]" is not. Noun leg.
- **@1092 (a6_06)** — MODERATE: `79 80 06 [43] 07 55 81` = "tout(79) [80] [06] [43] …". Under the 06-attachment rule (06="-ent" iff left neighbor is a verb stem; 80 is verb-frame A8), "80-06" reads as 3pl "[80]ent", and 43 is its complement: "tout [V-3pl] [N]". Noun-as-object leg. (If 06 is syllabic here the frame is undetermined — hence moderate.)
- **@244 (a2_02)** — WEAK: `12 16 56 [43] 00 66 91` = "[56] [43] pour(00) [66]". "[56-N] [43] pour": noun ("X [N] pour [Y]") or finite-verb ("[subj] [V] pour") readings both available; genuinely ambiguous. Half-leg at best.
- **@1126 (a6_07) / @1724 (a8_07)** — GATED ×2: "11 52 37 [43]" = "la [52-37-adj-unit] [43-head-noun]" (Type-A parse). Structurally noun, but red-team-gated (la-frame NULL) — NOT counted toward C1.
- **@1544 (a8_00)** — UNDECIDED: `88 77 78 [43] 00 46 70` = "[88] le(77) [78] [43] pour(00) que(46)". Class-consistent with noun under the government reading ("[N] pour que [subj]"), but the boundary-vs-government adjudication is NULL (frame-43-pour-que-1544) and all "pour que"-licensing noun values are dead (noun-43). Not a clean leg; fenced to the queued target.

**Verb-stem frames:**
- **@21 (a1_00)** — CONFIRMED, word-internal only: `64 98 82 [43] 29 47 33` = "qui(64) [98] m(82)[43]er(29) ce(47)". Promoted segmentation (43-29-segment): 43 is the stem of the infinitive "m[43]er". This is the locus that kills monovalent noun at kill grade (noun-43).
- Standalone verb frames: NONE clean. @244 is ambiguous (above); @439 resists ("que [V] [V]" ungrammatical); @563/@1204 resist (post-determiner); @343/@1027 resist ("par [V]" ungrammatical).

**Adjective-shaped frames:** @258 (`01 91 32 [43] 77 84 74`, predicative-32 complement — weak, "est [43]" admits noun equally); @386 (`52 38 37 [43] 91 36 62`, predicative-37 complement — weak, "37 43 91" strands 91 under every class). No clean adjective leg.

**Hostile frames:** @343/@1027 (`45 64 96 [43] 87 01 …` = "…par(96) [43] ce(87) [01]", ×2) resist noun, verb, AND adjective under standing values — consistent with the promoted par-43 kill (par43-adverbial-attestation). Genuine residuals, not legs for any class.

**Census tally:** noun = 2 strong + 2 moderate + 1 weak (+ 2 gated, + 1 undecided); verb-stem = 1 confirmed (word-internal only); adjective = 0 clean; determiner/prenominal-modifier = 0 frames anywhere.

## 4. The C2 condition: "43 81" as direct-object NP under 81-noun

- The bigram "43 81" occurs **exactly 1x stream-wide** (hapax), at @43–44: `01 24 88 [43] [81] 30 62` (row a1_01). The 88–43 bigram is likewise hapax.
- 81's left-neighbor census (n=14): 55×6 (verb-class: verb+object), 77×4 ("le [81]", the F150 NP legs), 43×1, 98×1, 39×1, 08×1. The ONLY licensed "X 81" noun phrases on the stream are "le 81" ×4.
- 43's right-neighbor census (n=16): 29, **81**, 00, 77, 87, 91, 98, 24, 87, 07, 00, 55, 21, 77, 00, 98. The ONLY "43 + noun" contact stream-wide is the very bigram under test — 43 never precedes any other noun, and never appears as a prenominal modifier or determiner in any frame (§3: determiner/prenominal-modifier legs = 0).
- For "43 81" to be a direct-object NP with 81 as nominal head, 43 must be a determiner, a prenominal adjective, or an appositive noun. (a) Determiner/adjective: zero legs stream-wide; all of 43's nominal legs are HEAD-position ("la 43", "ce 43", "que 43"), and a hapax determiner class at the single window under test contradicts those frames. (b) Noun–noun: bare "N N" direct object without "de" is ungrammatical in 1841 diplomatic French. (c) The 43-as-verb alternative ("[88] [43-V] [81] pas") abandons the bar's stated NP condition; it additionally fails on its own terms — F119 gives 88 zero infinitive-class complements, and ne-drop with a compound tense is unlicensed.
- The ne-drop arm is independently unpromotable here: no "ne" (94) occurs within ±8 pairs of @45 (re-derived), and 30="pas" was promoted on ne-frames (@558/@1713-class), not at @45. Ne-drop at a hapax junction, with 88's finiteness open (F119 is class-level only) and 43's class open, is exactly the fenced parse of seg-81-30-boundary — nothing in this census removes any of its three blockers.

**C2 antecedent: FALSE.** "43 81" does not form a direct-object NP under 81-noun at battery grade.

## 5. Adverses answered

The brief lists no adverses. Four rival readings were considered and rejected:
- **43 = determiner at @43** ("[88-V] [det] [81-N] pas"): rejected — hapax class with zero corroborating frames; contradicts 43's head-position determiner frames (@563/@1204).
- **43 = verb, 81 = its object** ("[88] [43-V] [81] pas"): rejected — not the bar's NP condition; 88 takes zero infinitive-class complements (F119); compound-tense ne-drop unlicensed.
- **"43 81" as subject NP** (the passing note in battery-x29-80-1596-nominal): rejected — "pas" @45 is preverbal to 62 ("…pas [62] par pour…"); preverbal "pas" without "ne" is ungrammatical, and the note's window (@1596) is not this junction.
- **"43 81" as noun–noun compound**: rejected — no "de", no hyphenation evidence, ungrammatical as a direct object in 1841 diplomatic French.

## 6. Per-clause pass/fail

- **C1 (name 43's class with ≥3 frame legs): FAIL — jurisdictionally blocked, not evidentially empty.** Distributionally, noun clears the ≥3-leg bar (@563 strong, @1204 strong, @439 moderate, @1092 moderate, @244 weak). But naming it at battery grade contradicts three standing verdicts: noun-43's NULL closure ("the noun-43 line is closed at battery level pending red-team act"; "@21 independently kills every monovalent noun at kill grade"), battery-43-29-segment's PROMOTE ("do not re-name 43 at battery level"), and la-frame's NULL red-team gate — and would implicitly declare polyvalence against the confirmed @21 verb stem, violating §7 (67 et/veut is the sole true polyvalence). The verb-stem class has exactly one leg, word-internal (@21), and zero clean standalone frames. No class can be named at battery grade without a red-team act. This is inconclusive-for-now, not a falsification: no window forces the census claim false.
- **C2 (conditional): antecedent FALSE, consequent does not trigger.** "43 81" is a hapax bigram; 43 has zero prenominal-modifier frames stream-wide; 81's only licensed "X 81" NPs are "le 81" ×4; bare N–N direct object is ungrammatical. The "…[88] [43] [81] pas" ne-drop-negation parse is therefore NOT promotable, and the **seg-81-30-boundary fence does NOT re-open — it stays HELD** on its original blockers (43's class, 62's value, 88's finiteness), of which this target tested only the first.

No standing verdict contradicted or downgraded (noun-43, 43-29-segment, la-frame, par43-adverbial-attestation, seg-81-30-boundary, F119/F150/F89, §7 all intact). R5005, sealed gates, red-team queue untouched.

## 7. Verdict: NULL

43's class cannot be named at battery grade: the only ≥3-leg class (noun) is red-team-gated, and the confirmed class (verb stem) is word-internal-only. The "43 81" direct-object NP fails at battery grade, so the ne-drop-negation parse does not promote and the fence stays closed.

**Headline for the red team:** the census sharpens the 43 crisis rather than resolving it. Noun is distributionally the runaway leader (2 strong + 2 moderate + 1 weak standalone legs) yet is triple-barred at battery level (noun-43 closure, 43-29-segment's scope bar, la-frame's redteam-43-polyvalence gate). The fence window's left edge (43) cannot supply the prenominal modifier the "…[88] [43] [81] pas" parse needs — 43 has zero modifier-class frames stream-wide — so even a future grant of 43-nominal would not by itself re-open the seg-81-30-boundary fence; the NP-internal shape of 43 would still need independent evidence.

## 8. Follow-up targets (null regenerates work)

1. **`prof-43-rerun-polyvalence`** (P2) — re-run this exact bar after redteam-43-polyvalence adjudicates 43's nominality. If 43-nominal is granted: name noun (legs banked: @563/@1204 strong, @439/@1092 moderate, @244 weak) and re-test the "43 81" NP (expected: still fails — zero modifier legs — which would permanently close the ne-drop arm). If 43-verbal is granted: the "43 81" NP is dead and seg-81-30-boundary's C2 arm closes. Verified absent from queue. (Distinct from queued `tail-523743-rerun-43poly`, which re-runs the la-frame tail bar, not this census bar.)
2. **`par43-ce-scope`** (P3) — adjudicate the hostile "96 43 87" ×2 windows (@343/@1027, "par [43] ce [01]"), which resist every class under standing values and block ANY 43 class promote. Test: (a) 87="ce" scope at these windows (is "ce" really the token here, or does the 6-gram "45-64-96-43-87-01" invite resegmentation?); (b) "43 87" as a unit; (c) 96="par" alternatives. Discriminating frames for the red-team docket. Verified absent from queue (par43-adverbial-attestation is verdict/promote and covers only the adverbial-value escape, not the 87-scope/resegmentation angle).

Coordination note (not a new target): queued `seg-81-30-offset1` (P3) may dissolve the @43–45 junction entirely under row a1_01's rival phase — if it does, this line closes with it; not duplicated here.
