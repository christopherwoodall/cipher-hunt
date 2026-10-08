# PREREG — battery48 (round 14, WO-14 item 4: 74-class + H_stem)

Runner: 48-BATTERIES. **Written 2026-10-07 ~18:35 CDT — BEFORE any new data
query by this worker beyond re-derivation checks already performed
(@863=[74,48,47,46] @862–865 confirmed; n74=34; n48=38; P[866]=0).**
Round-13 partials read (not re-run): `code/crowd13/carry-rest/{PREREG.md,
carry_results.json}` — frozen inputs, not scored legs here. Red-team R-CR48
second-shift caveat (3) is binding on this battery: *"H_stem's ne-marginals
tension stays open — name the stem-before-verb construction or drop the leg."*

Positions 0-based on the repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` via
`code/crowd7/keystruct/aliasing.load_stream()`; NEVER `canonical.py`).
N=1847 asserted at runtime.

## Standing inputs (frozen, not scored legs)
- GT {11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que}; provisional {87=ce,
  64=qui, 96=par, 59=est}, 77="le" provisional-CONDITIONED (F37),
  94="ne" provisional-strong (F24/N24), 62="on" FENCED STRONG LEAD,
  52="pas" STRONG, 33=infinitive-class, 78 polyvalent (F38/F103).
- KILLED (not re-litigated): 48="ne" (F60), H_verb for 48 (N50/K2),
  48="de"-unconditioned (french-blitz, 11 windows).
- SPLIT (not re-litigated): {48,94} ne-distributed class-mates — do NOT tie
  48↔94 as values. (Contact adjacency 94→48 is a datum, not a value tie.)
- Islet status: 48="de" iff "de ce que" LEAD-weak, n=1 @863 (F110; R-CR48 GRANT).
- H_stem status: ONE LEG (round-13 B1+B2: 3-window compatibility + 13.3%
  [stem]["er"] license). 48's value needs ≥2 legs for any LEAD (standing rule).
- Corpus: clean-diplo pool (same 13 files as round-13 carry-rest). v8
  phrase-zeros VOID (F77); v8 L1s NOT reused. Tokenizer: round-11
  este_verb.py's (NFC, lower, '-normalized, elision kept on stem).
  By-ear syllabifier: round-13 hstem.py verbatim (v1.2).

## Battery 1 — 74-class (promotes/kills the @863 "de ce que" islet)

Frame: @862=74, @863=48, @864=47, @865=46, @866=0, @861=74 (74-74 bigram),
@860=49. Question: is 74 a licensor (adjective/participle/noun) for "de ce que"?

### Leg A3 (cipher, NEW) — 74's class on banked values only
Re-derive all 34 74-windows ±3, glossed. Class-signature tests, each with a
pre-registered falsifier on GT/provisional values:
- A3-verb: suc(74)=77 ("le?" prov-COND) ×2 already banked ADVERSE (round-13).
  NEW: 74's successor set vs inflection inventory {29,40,6,59} (verb stems
  take inflection successors); pre(74) ∈ {94,62} (subject/negation frame).
  Falsifier: 74 pins VERB iff suc(74)∩INF ≥3 AND pre(74)∩{94,62} ≥2.
- A3-adj: 74→89 (89 noun-class 14/14, F102: adj-noun order) ≥2, or
  pre(74) ∈ {70} ("pre 74" — adjective after preposition? weak; report only).
- A3-noun: pre(74) ∈ {11,87} (determiner adjacency) ≥2.
- A3-part: pre(74) ∈ {59} ("est 74" participle signature) ≥1.
- A3-func (KILL-path): 74 pins to a NON-licensor function class (subject
  pronoun / article / preposition / conjunction) on banked values, AND era
  A4 shows that class licenses "de ce que" at 0/pooled-genuine.
- A3-syl (FENCE-path): 74-74 bigram rate = 1/33 = 3.03% vs era word-bigram
  self-repeat rate on clean pool. If era rate < 0.5% → SYLLABLE-LEG for 74
  (word reduplication «X X de ce que» ungrammatical for every word class) →
  74 is not a word-class licensor at @862; battery FENCED (islet HOLD).
  (Offset caveat KE1: the bigram sits on upstream EM offsets; disclosed.)

### Leg A4 (era, NEW) — "de ce que" L1 re-licensing, artifact-excluded
Exhaustive clean-pool "de ce que" census (tokens + L1 + left context for
absolute-use detection). Pre-registered ARTIFACT set (non-governing L1):
{et, aussi, surtout, enfin, exactement, seulement, pas, autres, même} ∪
vocatives {roi, majesté}. Two analyses disclosed: (a) modifiers excluded,
vocatives kept; (b) both excluded. "nature"/"répondant" kept as nouns
(genuine governors possible). Class definitions: adjective (takes "de"
complement: heureux/fâché/satisfait/content/curieux/inquiet/honteux/peiné…),
noun (compte/exemple/partie/raison/besoin/contraire/rien→pronoun…),
participle (past participle, verbal force: dit/peinée…), verb (finite or
reflexive governing "de": plaindre/féliciter/souvenir…), pronoun (rien,
indefinite), artifact (per set). Per-token classification disclosed in raw JSON.
- A4-dom: a class DOMINATES iff ≥70% of pooled genuine L1s (same bar as
  round-13 A1 — no goalpost move). No class ≥70% → CLASS-AMBIGUOUS stands.
- A4-abs: absolute-"de ce que" rate = tokens with no L1 governor (preceded by
  sentence boundary [.!?;:—«"()…] or string start) / all tokens. If >20% →
  the licensor requirement is substantially weakened → 74-class battery
  FENCED regardless of A3 (islet HOLD; 74's class not decisive).
- A4-neg (KILL-support): for the class 74 pins to (if A3 pins one), report its
  genuine-L1 count. 0 → kill-grade adverse for the islet via that class.

### Battery-1 verdict bar (pre-registered)
- PROMOTE islet → word-lead "de" iff ≥2 independent legs agree from
  {A3 class-pin on banked values, A4 dominant-class license, clean @863
  gloss with no banked contradiction}.
- KILL islet (48="de" FULLY DEAD) iff kill-grade adverse: (i) A3-func pins
  74 to a non-licensor class on banked values AND A4-neg = 0 for that class;
  OR (ii) @863 fails byte-exact re-derivation as [74,48,47,46].
- Else HOLD: islet stays LEAD-weak; 74-class stays OPEN (sub-outcome
  FENCE-74-SYLLABLE if A3-syl fires, or FENCE-ABSOLUTE if A4-abs >20%).

## Battery 2 — H_stem (48-er×2 / 48-e×1 as stem+inflection)

Cipher data: 48→29 ("er" GT) @1229 (pre=82="m" GT), @1589 (pre=65);
48→40 ("e" GT) @1398 (pre=78). H_stem: 48 = vowel-initial verb-stem syllable
cell. Coherent coexistence (not scored here, stated): conditioned polyvalence
— 48 stem-valued before inflection cells {29,40}, "de"-syllable-valued in the
48-47-46 frame (lane precedent: F33 conditioned polyvalence).

### Leg B3 (cipher, NEW)
- B3a (re-derivation, asserts): PAIRS[1229]=48 & PAIRS[1230]=29;
  PAIRS[1589]=48 & PAIRS[1590]=29; PAIRS[1398]=48 & PAIRS[1399]=40;
  PAIRS[1228]=82. ±4 glosses with banked values. PASS iff all re-derive and
  no window contradicts a GT value; FAIL (kill-grade datum) iff any window
  contradicts on GT.
- B3b (successor habitat census, n48=38): suc(48) split into INF={29,40,6,59}
  (inflection inventory: 29/40 GT, 6 "ent" restricted-prov, 59 prov) vs
  WSEG={46,47} (word cells that cannot follow a stem mid-word) vs other.
  Comparators: 06 (verb-stem provisional) and 94 ("ne" prov-strong word) suc
  profiles; Fisher 2×2 (INF vs non-INF) 48-vs-06 and 48-vs-94, p reported.
  Kill-grade falsifier (pre-registered): 48→INF = 0 AND 48→WSEG ≥ 5
  (stem-habitat absent where word-habitat present). (Expected NOT to fire:
  round-13 found 48→29×2, 48→40×1 — the falsifier is honest anyway.)
- B3c (red-team caveat 3 — NAME THE CONSTRUCTION): pre(48) census; test the
  «94 48» construction: pre(48)=94 count; gloss each «94 48 X» window —
  «ne/n' + [vowel-initial verb stem]» (94="ne" prov-strong; "ne" elides to
  "n'" before vowel-initial stems, so a vowel-initial stem syllable is
  EXACTLY what follows "n'"). NAMED iff ≥2 «94 48» windows gloss as
  ne/n'+verb-compatible on banked values → the ne-like marginals are
  explained BY H_stem (48 follows ne) rather than competing with it.
  If pre(48)=94 is 0 → tension stands UNRESOLVED (leg not dropped, flagged).

### Leg B4 (era, NEW) — contact-profile-conditioned licensing
- B4a: among clean-pool -er infinitives (same is_inf rule), share with
  by-ear parse exactly [stem]["er"] AND stem vowel-initial (48 must be
  vowel-initial: 82="m" elides only before vowel, @1229 GT datum).
  Bar: ≥5% → LICENSES (same bar as round-13 B2, conditioned).
- B4b: "m'"+vowel-initial-er-infinitive contact: count tokens "m'" followed
  by a vowel-initial -er infinitive (the @1229 «m' 48-er» habitat).
  Bar: ≥3 genuine tokens → CONTACT-LICENSES.
- B4c (report-only): vowel-initial verb-form habitat for 48-e: count
  vowel-initial tokens with by-ear parse exactly [stem]["e"], stem
  vowel-initial, len(stem)≥2; report n + top-20 examples. No bar (habitat
  existence leg).

### Battery-2 verdict bar (pre-registered)
- LEAD-grade iff B3a PASS AND B4a LICENSES (≥5%) AND B4b CONTACT-LICENSES
  (≥3). (This is the pre-registered LEAD bar per WO.)
- KILL iff B3a FAIL (GT contradiction) OR B4a < 1% OR (B4b = 0 AND B4a < 5%).
- Else HOLD: H_stem keeps its one leg (round-13), not LEAD; B3c names or
  fails to name the construction (reported either way).

## Outputs
- `code/crowd14/battery48/{PREREG.md,common.py,a74.py,hstem.py,verdicts.py,
  a74_raw.json,hstem_raw.json,battery48_results.json}`
- Final report to parent: per-battery verdicts, 74's classification, H_stem
  status, ranked 48 hypotheses.
