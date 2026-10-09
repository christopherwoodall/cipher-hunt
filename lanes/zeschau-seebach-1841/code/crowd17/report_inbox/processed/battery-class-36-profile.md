# Battery verdict: class-36-profile

## Bar (verbatim)
"assign 36 ONE class (noun? infinitive? adjective?) with >=3 independent frame-legs, using the 00 x3 'pour'-frames, 59 x2 'est'-frames, and 45-'ce' contact; resolve or fence each window with stated cause"

## Bar as numbered clauses
- (a) Assign 36 exactly ONE class from {noun, infinitive, adjective}, with >=3 independent frame-legs.
- (b) The legs must draw on all three frame groups: the 00 x3 'pour'-frames, the 59 x2 'est'-frames, and the 45-'ce' contact.
- (c) Every one of the 9 windows resolved (class-consistent parse) or fenced with stated cause. No window ignored.

## Method
Read BATTERY-PROTOCOL.md first; created locks/class-36-profile.lock on start. Re-derived the
1,847-pair repaired stream from code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt with the byte-exact upstream tokenization
([s[i:i+2] for i in range(o, len(s)-1, 2)]); never touched canonical.py, R5005,
sealed gates, or the red-team queue. 36 census re-derived: n=9 at
@388/@421/@740/@1174/@1215/@1313/@1449/@1585/@1834 (matches the evidence note
exactly). Predecessors: 00 x3, 59 x2, 91/49/85/45 x1. Successors: 74 x2,
62/29/20/77/67/70/69 x1. Grants used: 00=pour (A9), 59=est (provisional),
45=ce (A11 hold), 29=er / 40=e / 11=la / 70=pre / 82=m / 34=i / 46=que (pencil),
96=par, 64=qui, 30=pas, 06=ent, 21=NOUN class, 85=verb-stem (A3), 33=INF,
24=finite verb.

## Distributional controls (re-derived, not cited)
- 00=pour successors (n=55): 86 x12 (INF, A9), 33 x8 (INF), 66 x7, 92 x6,
  97 x4, 11 x4 ("pour la"), 46 x4 ("pour que"), 36 x3. Pour+infinitive is the
  dominant frame; pour+noun is attested via determiner ("pour la").
- 29=er (n=45) is a MULTI-CLASS ending, not an infinitive-only marker. Witness:
  34-29 = "ier" inside "premier" (11 70 82 34 29 40, ground-truth gloss),
  an adjective. 29 also completes INF-class stems (33-29 x5, 86-29 x4) and is
  followed by 40=e x9 ("ere"). So "36-29" = "36er" is morphologically
  compatible with noun (-er nouns: boulanger-type), adjective (-ier: premier-type),
  or infinitive. It does NOT force a verbal reading of 36.

## Class shoot-out (each candidate scored on all 9 windows)
- INFINITIVE: legs = pour-frames x3 ("pour [36-INF]" matches the dominant
  00->INF frame) + @421 "36er" (infinitive-shaped). But "est [36-INF]" @1449
  and @1834 is ungrammatical in 1841 French under every rescue, and
  "ce [36-INF]" @1215 is ungrammatical (45=ce is an A11 hold). Three hard
  contradictions -> cannot promote; re-segmentation would require ungranting
  provisional 59=est with no evidence from these windows.
- ADJECTIVE: legs = est-frames x2 ("est [36-ADJ]" is the canonical adjective
  frame). But "pour [36-ADJ]" x3 is ungrammatical with no rescue, "ce [36] le"
  @1215 fails (77=le? is determiner-shaped, not a noun for the adjective to
  modify), and "36er" @421 is infinitive/noun morphology. Dead as single class.
- NOUN: every window grammatical, zero hard contradictions (scored below).
  Promoted at class level; value stays open.

## Window-level evidence (@-offsets on the repaired stream)
1. @388 [a2_07] "91 36 62": 91 unvalued; 62=il? demonstrated-but-unpromoted.
   FENCED (neutral): no class confirmed or excluded; stated cause = both
   neighbors unvalued/unpromoted.
2. @421 [a2_08] "49 36 29": "36er". Per the 29 control above, -er is
   multi-class (adjective "premier" attested in ground truth); -er nouns exist.
   49 unvalued. RESOLVED-NEUTRAL for noun: compatible, no contradiction; value
   still open. Not an anti-leg at battery grade.
3. @740 [a5_02] "00 36 20": "pour [36] [20]". NOUN LEG (moderate): "pour [noun]"
   is grammatical in formal/diplomatic register ("pour memoire", "pour
   information", "pour cause de"); 20 is nominal-shaped (frame-20-62-94).
   "pour [36-noun] [20]" parses.
4. @1174 [a6_10] "21 85 36 74": 21=NOUN class, 85=verb-stem (A3, value open).
   "21 85" reads subject+verb-stem; "85 36" = verb + direct object gives a
   CONDITIONAL noun leg for 36 ("[sujet] [verbe] [36-objet] [74]"), conditional
   on 85 finite/transitive (value open). FENCED as primary verdict (85's value
   open; "85 36" word-boundary undetermined) but SUPPORTS noun; contradicts
   nothing.
5. @1215 [a7_00] "96 45 36 77": "par ce [36] le [83]". NOUN LEG (solid):
   "par ce [noun]" is fully grammatical. 77=le? fenced with stated cause
   (provisional value; comma-boundary reading "par ce [36], le [83]..." available,
   so 77 does not strand). This window also answers the battery's purpose: the
   left edge "45 36" parses independently of the 83 fence as "ce [36-noun]".
6. @1313 [a7_04] "00 36 74": "pour [36] [74]". NOUN LEG (moderate): "pour [noun]";
   "36 74" additionally admits noun+postnominal-adjective ("pour motif urgent"
   pattern), 74's class open. Consistent.
7. @1449 [a7_09] "84 59 36 67": "on est [36]". NOUN LEG (restricted): bare
   predicate nominal, grammatical in the profession/status subclass
   ("on est medecin"-pattern) and the "c'est [noun]" pattern ("c'est dommage").
   Leg marked restricted/conditional on 36 being status-like; grammatical
   regardless. 67=et/veut belongs to the following clause.
8. @1585 [a8_02] "00 36 70": "pour [36] [70-pre]". NOUN LEG (moderate):
   "pour [noun]"; 70=pre (pencil syllable) opens the next word. Parses.
9. @1834 [a8_11] "59 36 69": "[16] est [36] [69]". NOUN LEG (restricted): same
   bare-predicate-nominal subclass as @1449. Grammatical.

## Per-clause pass/fail
- (a) PASS: 36 = NOUN, class-level (value not named). Legs: L1 @1215
  ce-contact (solid), L2 @740 pour, L3 @1313 pour, L4 @1585 pour, L5 @1449 est
  (restricted), L6 @1834 est (restricted), L7 @1174 verb-object (conditional).
  Six independent windows >= 3, plus one conditional.
- (b) PASS: all three frame groups used — pour x3 (L2-L4), est x2 (L5-L6),
  ce-contact (L1).
- (c) PASS: 9/9 windows resolved (L1-L6 + @421 neutral + @1174 conditional)
  or fenced with stated cause (@388 neighbors unvalued; @1174 85's value open).

## Adverses
- "no single class granted for 36": ANSWERED — noun assigned here at class
  level (precedent: prof-65's 65=noun-class promote without named value).
- "no window names its value": ANSWERED — value deliberately left open; class
  assignment does not require it. Value-hunting grounds noted below.

## Verdict: PROMOTE (class-level)
36 = NOUN. Value open. Infinitive and adjective are excluded as single-class
readings (3 and 4 hard ungrammatical windows respectively); noun is the only
candidate with zero hard contradictions across all 9 windows. No standing
verdict contradicted or downgraded. R5005, sealed gates, red-team queue untouched.

## Notes for value hunters (not verdicts)
- "36er" @421 and the "par ce [36]" / "pour [36]" frames are the value grounds;
  a profession/agent-noun in -er would fit all frames at once ("est [36]"
  predicative + "36er" morphology + "ce/par/pour [36]").
- 59=est is load-bearing for L5/L6; an independent 59 audit would harden them.
- 74 (follows 36 x2) and 85 (verb-object frame @1174) are the best next
  discriminators for 36's value.
