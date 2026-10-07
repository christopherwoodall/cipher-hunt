## anchorer48: 48 successor-word anchoring (round-11, work order 2)

- Context: F75 left 48 UNIDENTIFIED with the 10 S-syl shortlist as a datum and
  named two follow-ups (six "on 48" windows; 82="m"×4 frames); F76 left
  48="de"-CONDITIONAL (narrow pronoun+infinitive) as the only live word-reading.
  This executor ran all three as pre-registered batteries (PREREG.md written
  before any fresh era count) on Nesselrode v8 strict, repaired 1,847-pair parse.
  Code + JSON: `code/crowd11/anchorer48/` (anchor48.py, anchor48_results.json).

- Decision:
  - PATH A (six "on 48" → suc {76×2, 98, 77, 21, 56}): FENCED — no shortlist S
    coheres. A1 ("on"+W+"le" @1350-anchored): 0/10 PASS, all ADVERSE(fenced).
    A2 ("on"+W): 8/10 PASS but 6 are word-driven (W==S: à,de,a,il,les,un); only
    "es" (espère + esterhazï[OCR?]) and "com" (commence×3) have proper-syllable
    support; "et","te" 0.
  - PATH B (four 82→48 under mandated "m'"-premise): premise FENCED. B0
    ("m'",W): only "a" attested (145×, all W="a" verb "m'a"); proper-syllable 0
    for every vowel-initial S. B1 ("m'"+W+"la"): 0/6. B2 ("m'"+S+"er",
    two parses): 0/6. Conditional discrimination stands: IF 82="m'" THEN
    48 ∈ {à,a,es,et,il,un}, not {de,les,te,com} — but the premise gets zero
    positive support.
  - PATH D (48="de"-conditional): FENCED with explicit missing legs (not run).
    D1 LICENSED: "de le"+INF 29/29 = 1.00 (all 19 distinct X hand-verified
    infinitives: faire×6, voir×4, prévoir/recevoir×2, +14 singles); "de la"+INF
    13/439 (voir×2, soigner, reprendre, brûler, rattacher, défendre, réaliser,
    tirer, faire, refuser, soutenir, déclarer). @1350 OUT (pre-registered R-c
    exclusion — 78=R-c-nominal ⟂ infinitive; plus "on de" 0/2 genuine:
    "dit-on" inversion + OCR-adjacent "bai on de werther"). @126 OUT
    ([m-final-word]+"de la" = 0 in all of v8, even "nom de la" = 0). @1076
    IN-PENDING. D3: Gate-5 neither veto fires (48="de" not a verb); clitic veto
    stays banked; V1 escape via conditioning (recorded).

- Why: the bars were pre-registered (PASS ≥1 v8 attestation; fences never kills
  — every leg leans on non-GT premises: 62="on" fenced LEAD, 77="le" prov-cond,
  82="m'" hypothesis). A1's all-zero is informative not artifactual:
  ("on",*,"le") = 11× in v8 with W ∈ {ne×5, donne, avait, sait, vous, voudrait,
  veut} — the frame exists, just never with shortlist-initial W. D1's bar
  needed an instrument repair (v1 heuristic's NOUN_STOP wrongly excluded
  "faire", flipping 1.00→0.79): replaced with hand-verified per-X lexicon, full
  lists disclosed in JSON, hand-verdicts marked [FR-JUDGMENT]. The narrow path
  has exactly 1 independent check (D1 era); promotion needs a cipher-side
  suc2=infinitive ID — missing.

- Enlightenment:
  1. @1350's frame ("on"+W+"le") wants a VERB, "ne", or pronoun in the 48 slot
     (v8's 11 hits) — but H_verb killed 48-as-verb and 48="ne" is killed, and no
     shortlist-S fits. The "on"-frames don't just fail to identify 48; they
     point back at the premises. 62="on" (ear-only legs, N39) is the load-bearing
     weak link.
  2. ("m'",W) in v8 = verbs ("a"×145, "ont"×16, "avez"×16, "est"×9, …) +
     pronouns ("en"×28, "y"×5). Under 82="m'", 48's options collapse to killed
     verbs or 24's "en" — the premise fences itself. 82 is likelier
     word-final/initial "m" at these windows, but that needs its own battery.
  3. Era L1 of "de le"+INF (for ML-2): facile/chargé/courage/plaisir/moyen/
     occasion — adjectives/nouns/participles, broader than "[verb] de le".
     ML-2 should hunt adj/noun/participle for pre=12, not just verbs.

- For the report: 48 section (F75/F76 follow-up). Numbers that matter: A1 0/10
  (("on",*,"le")=11, zero shortlist); D1 "de le"+INF 29/29, "de la"+INF 13/439;
  @1350 OUT of narrow path (R-c + "on de" 0/2 genuine); @126 OUT ([m]+"de la"
  0/92,594); @1076 the sole surviving window, IN-PENDING. Net: 0 promotions,
  0 kills, 3 fences (A, B-premise, D-conditional).

- Caveats: every fence is conditional on non-GT premises — none of this kills
  any 48 value. B1/B2 are weak legs (("m'",*,"la")=1 in all of v8 — frame
  rarity, not just S-incoherence). "esterhazï" is likely OCR garbage (flagged,
  counted). Hand-verified French classifications are [FR-JUDGMENT], auditable
  per-X in the JSON. No re-litigation: 48="ne", H_verb, 86=que-family, R-c @1351,
  three mergers all respected. Out-of-scope observation (not a leg): @863 =
  48-47-46 with 47="ce" LEAD, 46="que" GT reads "de ce que" ("de ce que"=10×
  v8, "de ce"=74×) — a SECOND "de"-word frame outside the narrow path;
  candidate follow-up for a broader 48="de"-conditional.
