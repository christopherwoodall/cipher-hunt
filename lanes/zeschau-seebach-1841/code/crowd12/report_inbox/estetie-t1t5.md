## este-tiebreaker: -este verb tie-breakers T1–T5 (round 12 WO7)

- Context: F80 banked H0 — the -este verb stays set-valued
  {manifeste, atteste, proteste, conteste, déteste} — and named five
  tie-breakers. I pre-registered bars for each (PREREG-T1T5.md, written
  before any new query), ran them from code against the repaired
  1,847-pair stream, and era-checked on a 3.6M-word clean 1841-French
  corpus (Guizot/Metternich/Pozzo/Levant/Talleyrand/RDM; Nesselrode
  v7–v10 phrase zeros VOID per the OCR word-split caveat; AZ/ADB excluded
  as German). Red team adjudicates; I recommend only.
- Decision: **H0 holds — the set does not narrow on T1–T5.** All five
  tie-breakers return null/inconclusive/clean-negative. No promotion, no
  demotion, no kill recommended. @1291 stays fenced; the conditional
  {manifeste, proteste} discriminator stays conditional.
- Why (per tie-breaker):
  - **T1 (84 stem ID outside este frames): NO independent stem ID.**
    21 free 84-windows catalogued. Sharpest test @146
    «qui le 84-er» (64=qui prov, 77=le prov-cond, 29=er GT): stem+"er"
    gives conter/manifer/atter/proter/déter. "conter" is word-real
    (16/3.6M) but (a) «qui le conter» is era-zero AND ungrammatical
    (infinitive after «le»), (b) "conter" (narrate) ≠ "contester"
    (dispute) — a different lexeme, so it can't carry conteste's stem
    anyway. "atter" (12) is a German OCR fragment; "déter" (18) is
    "déter-miner" hyphenation fragments — both non-words, closing the
    loophole for atteste/déteste. Per a3 case law all of this is
    polyvalence-data, never kills.
  - **T2 («le» antecedents): INCONCLUSIVE.** @1448 parses as
    «[68] [est?] [37], qui le V» — 37 is the relative head (subject=qui),
    so «le» ≠ 37; the antecedent sits left of 68 among {68,1,85,24,16…},
    all unidentified. @1804: «[42] [ne?] [est?] [37] 91 79, ce qui le V»
    — antecedent among {79,91,37,42,56,86}, all unidentified. No
    masculine noun pinned by ≥2 legs → no selectional force on any verb.
  - **T3 (06="pro" ⇒ proteste): COMPATIBLE-UNCONFIRMED.** ISLET-3 does
    NOT fire at @1188 (pre(06)=42≠82); by-ear cut pro|t|este ∈ banked
    options; «proteste que» era-attested (2/3.6M, proteste=19). But the
    only independent "pro" witness, @346 «ce [1] 06-pre(70=GT) 12»,
    fails as a leg: "propre" needs the mute -e unwritten (tension with
    the crib's 40="e" habit, cf. N17) and 06-70 is multiply ambiguous
    (re-/sur-/en-/com- + "pre" + -ndre verbs). Global 06 screen
    (06→77 ×6 "prole"✗, 06→29 ×4 "proer"✗, 06→59 ×2, 06→0 ×3) rules out
    global-06="pro" — scoping data for the live 06-polyvalence, not a
    window-local kill.
  - **T4 (17/35 for @1291): STAYS FENCED.** 17 (n=15): «la fois»+finite
    verb is era-unsupported («la fois»=665, followers de/la/et/les/le/
    dans/l'/un/une/à/d'/si/plus/par/des — no verbs; «la fois que»=2/665),
    so 17="fois" is strained at @1289 (already WEAK); 17→64 @17 («17
    qui», noun+relative signature) adds tension; 17 unidentified. 35
    (n=10): «59 35 94» byte-identical ×2 (@1291/@1805, positional
    parallel confirmed); 64→35 @1359 («qui 35» — verb-slot signature,
    tension with the subject role); no subject-position signature
    anywhere; 35 unidentified. Un-fencing bar (both ≥2 legs) not met.
  - **T5 (second «qui le [84-59]»): CLEAN NEGATIVE, byte-exact.**
    64-77-84-59 = exactly 2× (@1445→p59 1448, @1801→p59 1804). The only
    near-miss is @144: 64-77-84-29 (the T1 «qui le 84-er» window).
- Enlightenment: the @146 window looked like conteste's lifeline
  ("conter" is a real word) until the lexeme check — "conter"≠"contester"
  kills the rescue more cleanly than the grammar does. And the
  «59 35 94» ×2 byte-identity (@1291/@1805) is the strongest structural
  fact in T4, but structure without values can't un-fence: it tells us
  the two windows share a skeleton, not what hangs on it.
- For the report: belongs in the round-12 este-verb section. Numbers that
  matter: T5 = 2× exactly (clean negative); «qui le»+any -este verb =
  0/3.6M clean-diplo (F-B neutrality confirmed on second corpus); «la
  fois»+verb = 0 (followers listed in estetie_era_followup.json);
  06="pro"@1188 = compatible, unconfirmed. Evidence:
  `code/crowd12/estetie/` (PREREG-T1T5.md, estetie.py,
  estetie_results.json, estetie_era_followup.json).
- Caveats: 77="le" is provisional-CONDITIONED and 64="qui"/87="ce" are
  provisional — T1/T2 lean on them; if any falls, the window glosses
  shift (the byte counts don't). «conter»'s 16 hits are literary-register
  (conter fleurette/son histoire), not diplomatic — flagged, not counted
  against the despatch register. The «[68] [est?] [37]» parse at @1448
  assumes 59="est" provisional; if 59 there is "-este", the clause
  boundary moves but the antecedent conclusion (unidentified) stands.
