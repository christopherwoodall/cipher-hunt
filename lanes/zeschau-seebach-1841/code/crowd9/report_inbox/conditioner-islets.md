# CONDITIONER round-9 report — islet registry, 84 residuals, formula/verb tests, 86 battery

2026-10-07 · conditioner (islet-registry owner) · pre-registered in
`code/crowd9/conditioner/PREREG9.md` BEFORE any new computation · evidence
`code/crowd9/conditioner/census.py` + `census_results.json` + `era9.py` +
`era9_results.json` · registry `code/crowd9/conditioner/islet_registry.md`
(shared with 06-falsifier-watch and 67-finisher) · positions 0-based
repaired 1,847-pair starts · era corpus = `code/side-period/corpus`
(despatches_primary N=372,751 for frame rates; diplomatic_all N=4,220,440;
nesselrode-v8 alone N=92,677 French-only for pour-rates); elision-split
tokenizer per F53. **No status changes merged — all verdicts are
recommendations for red-team ruling.**

## 1. Islet registry — built and current

`code/crowd9/conditioner/islet_registry.md` now records every conditioned
reading with exact conditioning rule, n/n_eff, supporting windows, banked
falsifier + status, and leftover unclassified windows: 84="en"
iff pre∈{82}∪{66,89} (LEAD, F62); 00="le" iff pre=96 (LEAD, F54);
06="ent" iff pre=82 (LEAD, F61; falsifier hunt owned by watch06);
67 et/veut fork (SUPPORTED, F63; bookkeeping only); 96=verb-stem
iff pre==64 & suc==47 (LEAD, F55/F63); 66-class and 89 noun-class
(84-extension dependencies, confirmed this round); 64-77-84-59 ×2
(refined this round); 86 identity (que-family refuted this round);
formula watch (45-64-96-43-87-01 ×2, 46-84-24-37-78 ×2);
killed/rescoped list.

## 2. 84's 9 residual windows — all classified (honest)

n84=25 verified: 5 en-islet + 2 withdrawn + 1 fenced + 8 rescoped-noun +
9 residual = 25 ✓. The 4 EN-EXTENSION windows were F62-GRANTED (not
re-derived). The 9: @391 RESIDUAL (en-lean n=1, 91 unknown); @788 RESIDUAL
(65="des"/"se" REFUTED — the «s'en» conditional cannot fire); @412/@1021
RESIDUAL (53-84 ×2 recurs but 53, n=11, has no class signature —
recurrence without class does not extend islets); @857 RESIDUAL, lean
CHANGED — round-8's adverse-lean is WITHDRAWN (it was conditional on
48="ne", KILLED F60); @1501 RESIDUAL, adverse-lean kept («te en»
unelided strained, fenced on 74="te"-LEAD); @1189/@1290 RESIDUAL, en-lean
(«en est» bigram era-real P=0.0156, n=708 — but subjectless
«[V-stem]/fois en est» strained); @1418 RESIDUAL, plain (32 unknown).
No new islet extension: the only recurrent pre (53 ×2) has no class.

## 3. qui-96-43 ×2 formula — HOLD (not confirmed, not extended)

Windows re-derived on repaired stream: @341/@1025 (not @1024 — the +1
shift applied; verified by search). Both extend LEFT: 45-64-96-43-87-01
×2 (6-mer; right of 01 differs: 06-70 vs 03-29). Bars: (a) parallel wider
context — PARTIAL (left only); (b) era «qui [V] me» = 3/1597 (nonzero but
rare); (c) 96=verb-stem's banking requires suc==47 (F55) — here suc==43,
so the reading would be an unbanked EXTENSION. Verdict: HOLD —
formula stays FORMULA-UNCONFIRMED (recurrence recorded, reading open).
New banked datum: 43="me" suffers a clitic-order adverse IN THIS FRAME
(French object clitics precede the verb — «qui [V] me» ungrammatical as
verb+object); 43="me" WEAK stands globally, but not here. 87-01=«c'est»
parses cleanly.

## 4. «qui le [verb=84-59]» ×2 — REFINED (frame strengthened, unit hypothesis-internal)

Windows @1445/@1801 (64-77-84-59; the 84s are @1447/@1803).
(i) Noun+"est" parse DEAD: «qui le X est» 2/4.2M (both rescued/broken),
«ce qui le X est» 0/4.2M. (ii) 59="est"-as-WORD after 84 is era-absent:
«qui le [V] est» 0/4.2M for ALL verbs — adverse datum for 59="est" AT
THESE TWO WINDOWS (not globally). (iii) The viable parse is F62's
bisyllabic-verb unit: «[N] qui le [V-bi], [main clause]» is era-common
(«qui le distingue saura», «qui le menaçait mis», «qui le nomma son» —
V often bisyllabic and clause-final in the relative). (iv) The prereg
falsifier does NOT fire: -este-family verbs are era-common (déteste 17,
conteste 19, atteste 36, proteste 20, manifeste 132, reste 1251).
Verdict: STRENGTHEN at frame level (77="le" pronoun + verb; 59="est"-word
dead here); the UNIT reading (84-59 = one bisyllabic verb) is
HYPOTHESIS-INTERNAL — it requires 59 conditioned polyvalence
(59="est"-word vs 59=verb-final-syllable), UNBANKED, no clean split
statable yet (59 pre: 84 ×4, 64 ×3, 94 ×3, 06 ×2, …). Follow-up: 59
conditioned-polyvalence battery + identify the -este verb.

## 5. 86's identity — que-family REFUTED (kill-grade); B3 STANDS; ratemodel caveat CORRECTED

Fresh battery, all pre-registered legs run: L1 unigram in-band
(uninformative); L2 «pour qu'» 12/55=0.218 vs era 0.0104 (21× OVER),
«pour que» 0.218 vs 0.0238 (9.2× OVER) — adverse; L3 finite-frame absence
non-discriminating; L4 86-vs-46(que-GT) profile parity fails (Jaccard
0.33/0.25, dominant contexts differ); L5 elision kills 86="qu'":
86→70 (70="pre"-GT, consonant), 86→52 ×2 (52="pas"-STRONG), 86→56 ×4
(56="plus"-MEDIUM) — «qu'pre/qu'pas/qu'plus» impossible at 3–7/12
windows; L6 («le que» ×5): 77="le" banked at all five 77-86 windows
(@431/@799/@878/@951/@1134), era P("que"|"le")≈0.00007,
P("qu"|"le")≈0.00003 — kill-grade adverse (mild circularity via F37 leg
1 broken by F37 legs 2+3, noted in registry). **Recommendation: 86 =
que-family REFUTED.** F40's verb-stem-class working hypothesis stands
(M1 F33-grade; @431 «[86]er» infinitive banked in F37); specific value
NULL (honest). **B3 correction:** the ratemodel's "86=que-family
dissolves B3 (16/55=0.29 vs era 0.31)" is wrong twice over — the era
number is 0.0343 French-only (not 0.31), so it would be 8.5× OVER, and 86
isn't que-family anyway. **B3 (3.19×) STANDS; the dissolution premise is
dead.** Open: 86-56 ×4, 86-52 ×2, 86-59, 77-86 non-29 windows.

## 6. 66/89 class readings — CONFIRMED (84-extension dependencies hold)

- 66: «pour 66» ×7 verified; era «pour»+subject-only-pronouns
  (il/on/ils/je/tu)=0 — 66 is not a subject pronoun; 66-84 ×2 grammatical
  under «[66] en [V]». Class CONFIRMED broad: {noun, infinitive,
  nous/vous-type pronoun} («pour nous»/«pour vous» era-grammatical —
  noted honestly; all three are "en"-compatible, so the 84 islet's
  dependency holds regardless). Specific value NULL.
- 89: three legs re-verified on repaired stream — 77-89 ×2 («le [89]»),
  29-89 ×5 (infinitive-object, 29-89-84 ×2), 89-48 ×3 («[89] ne»
  subject); full 14-window census: no kill-grade adverse; 24-89 ×3
  («en [89]») compatible. NOUN-CLASS CONFIRMED. Fenced tension: 52-89 ×2
  («pas [89]» bare — restricted, not kill-grade).

## What the red team must rule on

1. 86=que-family → REFUTED (kill-grade, ≥4 legs) — recommendation.
2. B3 dissolution premise → DEAD (ratemodel caveat corrected) — B3 stands.
3. 64-77-84-59 ×2 → frame STRENGTHENED, unit reading HYPOTHESIS-INTERNAL
   (needs unbanked 59 conditioned polyvalence) — no promotion.
4. qui-96-43 formula → HOLD (unconfirmed); 43="me" clitic-order adverse
   datum in this frame — bank it.
5. 84 residuals → all 9 RESIDUAL as classified (no islet change);
   @857's lean change (adverse-lean withdrawn) — note it.
6. 66-class (broad) / 89 noun-class → CONFIRMED — 84 islet's pre∈{66,89}
   arm dependencies hold.
7. 59="est"-word adverse datum at @1447/@1803 (era-0 «qui le [V] est») —
   bank it (59="est" provisional stands elsewhere).

## Open threads / follow-ups for other lanes

- 59 conditioned-polyvalence battery (word-"est" vs verb-final-syllable)
  + identify the -este verb at 84-59 (needs 84's first-syllable profile).
- 86's specific value (que-family dead; verb-stem-class working
  hypothesis; 86-56/52/59 and 77-86 non-29 windows open).
- 06-falsifier-watch: W06 verified [579,737,1183,1354] (pre-82
  positions); hunting per its prereg — results merge into the registry.
- 48-successor: @857's lean change flagged. 77/78-hunter: ISLET 8's
  59/77 dependencies flagged.
