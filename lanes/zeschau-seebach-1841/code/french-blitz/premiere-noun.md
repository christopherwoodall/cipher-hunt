# PREMIÈRE-NOUN HUNT — final report (2026-10-07, French-blitz, direct agent)

## Task
Identify the noun after "la première" @754/@1034. Pencil crib: 11=la, 70=pre,
82=m, 34=i, 29=er, 40=e (all GT). Repaired stream (1,847 pairs) re-derived
this session:
- @754: `11 70 82 34 29 40 | 20 62 94 59 39 88 ...`
- @1034: `11 70 82 34 29 40 | 17 77 82 63 11 67 ...`
Both windows have 40 immediately after 29 ("followed by 40=e").

## (a) Census: "la première X" in 1840–42 diplomatic French

Method: lane-standard tokenizer + paragraph-level French langvote over the
period corpus (nesselrode v7–v10, guizot t1/t2/t3/t5-t6, levant-p3 FR paras,
metternich v4/v6, RdM 1841 q1–q4, pozzo-di-borgo, talleyrand). ~3.1M French
words. Nesselrode-v8 phrase figures flagged per the OCR word-split caveat
(its "ment" tokens are splits; "la première" itself is split-resistant).

Grand total (top): fois 168, de 46, et 29, partie 25, occasion 22, est 16,
moitié 14, nouvelle 11, année 11, place 10, ...

É-initial X (the task's class): épreuve 3 (+1 unaccented "epreuve"),
expédition 3, entrevue 3, époque 2 (+2 unaccented "epoque"), édition 3,
enfance 3, étincelle 2. ("et"/"est"/"elle" are function words, not nouns.)

## (b) The framing adjudication: H-A vs H-B

The task frames H-B: 40=e *starts* the noun (é-initial). The lane's bedrock
is H-A: 40 is the word-final mute-e *of "première"* (N20: "cipher 40 is the
word-final mute-e writer per the crib"; also NOTES.md:283, :457, :1057 —
"première" writes 40="e" for mute final -e; pencil gloss "la première" spans
all 6 groups). H-B requires dropping the feminine mute-e ("la premier" —
ungrammatical, no precedent cited); H-A is the established position.

**Decisive: the lane already tested H-B and killed it.** N42 (round 6,
period-drag T3): "T3 NULL — the memo's shared é-initial-noun theory is dead
(entrevue/expédition 0 fits; épreuve fits @759 only, killed @1039; @1039
admits only [e,?,le] words)."

My independent re-derivation corroborates N42 exactly (see below). The
H-B premise in the task brief is therefore superseded — reported here so
the parent can retire it.

## (c) Candidate analysis

By-ear syllabification (cipher convention — over-splits vs spoken French):
- épreuve /e.pʁœv/ → é|preuve (2 cells)
- entrevue /ɑ̃.tʁə.vy/ → en|tre|vue (3 cells; initial is nasal ɑ̃, NOT é)
- expédition /ɛks.pe.di.sjɔ̃/ → ex|pé|di|tion (4 cells; initial ɛks, NOT é)
- époque /e.pɔk/ → é|poque (2 cells)
- fois /fwa/ → fois (1 cell)
- nouvelle /nu.vɛl/ → nou|velle (2 cells)
- lettre /lɛtʁ/ → lettre (1 cell)

Board (relevant): 62="on" fenced STRONG, 94="ne" prov-strong, 59="est"
conditioned (pre=94→"n'est" per ISLET 10), 77="le" prov-cond, 82="m" GT,
11="la" GT, 17="fois"-WEAK, 20=unknown.

**Under H-B** (noun = 40 + following groups; already killed per N42, shown
for completeness):
- entrevue: 40=e ≠ en /ɑ̃/ → KILLED (phonetic first-syllable mismatch).
  The cipher has 24="en" (STRONG) for /ɑ̃/; 40 cannot be nasal.
- expédition: 40=e ≠ ex /ɛks/ → KILLED (same).
- épreuve: W1 é→40 ✓, preuve→20 (unknown, no contradiction); W2 é→40 ✓,
  preuve→17 vs 17="fois"-WEAK → tension; cross-window preuve→20 vs →17
  needs uneconomical homophony → STRAINED, and N42 already killed it @1039.
- époque: identical structure to épreuve → STRAINED, same kill.

**Under H-A** (noun = [20]/[17], single groups; the live hypothesis):
W1: "la première [20], on n'est [59]…" — [20] is a complete word (bounded
by 62="on" fenced strong). W2: "la première [17], le…" — [17] complete
(bounded by 77="le"). Both slots are monosyllabic (1 group).
- fois (1 cell, census 168 — dominant 3.7× over runner-up): W2 fits
  17="fois"-WEAK directly; W1 needs 20="fois" as a homophone of 17
  (economical — cipher has homophones; needs its own battery).
  → FRONTRUNNER.
- lettre (1 cell, census 2): fits either slot, no board contradiction.
  → VIABLE (thin census).
- nouvelle (2 cells): ≠ 1 group → KILLED (syllable count).
- entrevue/expédition/épreuve/époque (2–4 cells): ≠ 1 group → KILLED
  (syllable count).

## (d) Ranked verdict

1. **fois — FRONTRUNNER (LEAD-grade).** Dominant census collocation
   (168/3.1M, next noun at 25), monosyllabic fits the 1-group slots,
   17="fois"-WEAK corroborates @1034, "la première fois, on n'est…"
   parses cleanly @754 with ISLET-10 "n'est". Open: 20="fois" homophone
   battery for @754.
2. **lettre — VIABLE (weak LEAD).** Monosyllabic, 2 census hits, zero
   board contradictions. Thin.
3. **épreuve — DEAD.** N42 T3 killed it @1039; independent corroboration
   (17-tension + cross-window homophony). Do not resuscitate without new
   evidence.
4. **époque — DEAD.** Same structural kill as épreuve.
5. **entrevue — DEAD.** N42 "0 fits"; phonetic kill (ɑ̃≠é).
6. **expédition — DEAD.** N42 "0 fits"; phonetic kill (ɛks≠é).
7. **nouvelle — DEAD.** Syllable count (2≠1); also n≠é under either
   hypothesis.

## Meta-finding for the parent
The task's H-B premise ("40=e favors é-initial nouns") was already
adjudicated and killed by the lane (N42, round 6, T3 NULL) — the period
fleet's memo did not survive contact with the round-6 drag battery, and my
independent re-derivation agrees on every point. The live question is the
H-A monosyllabic slot ([20]/[17]), where "fois" leads. Recommend: (i)
retire the é-initial-noun work order; (ii) run the 20="fois" homophone
battery (round 12/13); (iii) the @1034 "la première fois" reading is
LEAD-grade now (17-WEAK + census + fit = 3 legs, needs red-team ruling
for promotion consideration).
