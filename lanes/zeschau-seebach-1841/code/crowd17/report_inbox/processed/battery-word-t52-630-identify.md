# Battery report: `word-t52-630-identify` — verdict: NULL (fence as underdetermined)

**Target:** `word-t52-630-identify` (Seebach lane next-token pipeline battery worker)
**Worker:** agent ed88f1a0-6ac3-4743-ac3a-a2ec334de61e
**Date:** 2026-10-09
**Stream:** repaired 1,847-pair / 96-type parse re-derived in-session (asserts held:
1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, and the
red-team adjudication queue untouched. All @-offsets are 0-based repaired-stream
pair indices.

## Bar (verbatim, pre-registered)

> "pass iff the 't52' word is named with >=2 independent legs parsing the full @630 window 'ce [78] et 08 52 et [63] [74] que', else fence as underdetermined"

**Numbered clauses (frozen before testing):**
- C1: The "t52" word (@631–632, "08 52") is NAMED as a specific French word,
  supported by ≥2 independent legs, each parsing the FULL @628–636 window
  "ce [78] et 08 52 et [63] [74] que" under standing values with zero new
  assumptions.
- C2: Else (C1 fails) → fence the locus as underdetermined with stated cause.

## Method

Re-derived the repaired stream from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (same tokenization as
`repair_parse.py`). Locus byte-confirmed. Full predecessor census of 52
(n=27). Corpus censuses on `code/side-period/corpus/` (97 files; 170-byte
HTTP-500 stub excluded from counts by the grep filter).

Standing values used: pencil GT (11=la, 70=pre, 29=er, 40=e, 46=que);
granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce);
battery-grade (08='t' via val-08-31-letter + syllable-08-letter-value;
63=verb-class via verb-63-frames; 94='ne' strong lead); conditioned
(60='vient', battery, pending ratification). 67="et" at @630 via the
sole-polyvalence positional rule (follower 08='t' is not infinitive-shaped).

## Findings

### Locus (byte-confirmed)

Row a4_01 (global start 618): `@628=87 @629=78 @630=67 @631=08 @632=52
@633=67 @634=63 @635=74 @636=46`, i.e. `ce [78] et 08 52 et [63] [74] que …`.
Full row: `29 88 37 76 82 14 59 37 33 29 87 78 67 08 52 67 63 74 46 60 67 77
89 48 20`. The "08 52" bigram is a stream hapax; "67 X Y 67" ("et X Y et")
is a stream hapax (@630).

Adopted from parent `val-52-630-frame` (PROMOTE): 08–52 composition is live
("et [t52-word] et [63] …"); 52 is sub-lexical at @630; "et 08 [52-V]"
(52-alone-as-verb) is killed. From `split-52-redteam-input` (PROMOTE,
package): 52 is split-shaped across tiers (verb "qui 52" ×2, adverb
"ne 52 [INF]" ×2 + "la plus" ×3, sub-lexical "t52"/"pre52").

### The "et X et Y" coordination premise fails on corpus evidence

The bar's premise is that 52's letter value or 63's class constrains an
"et X et Y" coordination. 63's class (= verb, battery) is now known — and
it breaks the premise:

- Corpus census of "et X et" (97 files): the frame is overwhelmingly
  NOMINAL/ADJECTIVAL correlative ("et anglais et", "et homme et",
  "et honneur et", "et amour et", "et roi et" — top hits; full examples:
  "cet honneur et te prie", "cet homme et cette femme", "cet amour et de
  cette jalousie"). It is the "both X and Y" nominal coordination.
- "et [t-word] et [verb]": exactly ONE hit stream-corpus-wide —
  "et trente et une" (a number, not a verb). The verbal "et X et Y"
  frame is unattested in 1841 French at battery grade.
- Since 63 is verb-class, "et [t52] et [63-verb]" as correlative
  coordination demands a verb-parallel t52 — a frame with zero corpus
  support. The bar's coordination premise does not survive 63's
  verb-class naming.

### Candidate elimination (each tested against the full window)

- **"tout" (52="out"):** "et tout" = 397× in corpus, but "et tout et" = 0.
  Fails the frame. ("pre"+"out" = "preout" is not French, so uniformity
  fails too — though the bar is locus-level.)
- **"tous"/"tel"/"tant":** "et tous et" = 0, "et tel et" = 0,
  "et tant et" = 0.
- **Single-letter 52 ('a'/'e'/'u'):** "ta"/"te"/"tu". The leading
  uniform value 52='a' (conditioned battery result) gives "ta"
  (possessive determiner) — ungrammatical at @630 ("et ta et [63-verb]";
  "ta" requires a nominal head, 63 is verb-class). This ELIMINATES the
  leading uniform value at this locus and confirms the split — it does
  not name the word.
- **"tend" (52="end"):** the striking uniformity lead — "t"+"end" =
  "tend" (3sg *tendre*), "pre"+"end" = "prend" (3sg *prendre*), both real
  French 3sg verbs; "prend" is consistent with `ne-1331-70-52-parse`
  Arm A (94='ne' particle before the "pre"+52 prendre-family verb head).
  "et prend" = 18× corpus-attested ("et prend la/une/un/son/sa/parti…").
  BUT: "et tend et" = 0; "et [tend] et [63]" has zero frame support;
  "ce"-subjects of content verbs are strained (verb-63-frames @1427
  adverse); and the tail (below) does not parse. One leg (uniformity),
  not two — and the frame leg fails. Recorded as a follow-up lead, NOT
  a naming. Tension note: "tend" as a verb word sits uneasily with the
  parent's "non-verbal" class label at @630, but does NOT contradict the
  parent's evidence (which killed only 52-ALONE-as-verb, Arm A, via the
  standalone-08 impossibility).
- **67@633="veut" alternative:** "et [noun] veut [INF]" IS
  corpus-attested ("et ça veut porter", "et ennemi veut percer",
  "et anglais veut toujours"). The alternative stays live — but no
  t-word candidate works ("et tout veut" = 0, "et tel veut" = 0).
  Unnameable.

### The tail blocks every full-window parse

`[74] que [60]` @635–637: "74 46" is 3× stream-wide (@418, @635, @693);
in all three, "que"+verb lacks a subject ("que [60-vient]" is
ungrammatical; 46='que' cannot be a subject). The full row continues
`… que [60] et [77] [89] [48] [20]`, which does not rescue it. No
"t52" candidate yields a grammatical FULL-window parse because the
@635–637 tail is a residual under every reading. This is an independent,
window-level cause of underdetermination.

### Per-clause ruling

- **C1 — FAIL.** No "t52" word can be named with ≥2 independent legs
  parsing the full window. The best candidate ("tend"/52="end") has one
  leg (cross-locus uniformity) but fails the coordination frame, the
  "ce"-subject strain, and the tail.
- **C2 — FIRES.** The locus is fenced as underdetermined, with three
  stated causes: (i) the "et X et Y" verbal-coordination premise has zero
  corpus support and mismatches 63's verb class; (ii) the leading uniform
  value 52='a' is grammatically eliminated here ("ta" needs a nominal
  head); (iii) the "[74] que [60]" tail is ungrammatical under all
  readings, blocking every full-window parse.

## Adverses answered

- **"52's verb tier ('qui 52' ×2), adverb tier ('ne 52 [INF]' ×2,
  'la plus' ×3) live at other loci — locus-level verdict only."**
  Honored: this verdict is locus-level (@631–632) and does not touch,
  rename, or re-litigate any other 52 locus or tier. §7 intact.
- **Parent `val-52-630-frame` PROMOTE.** Honored: the 08–52 composition
  stands; Arm A ("et 08 [52-V]") stays killed; the "non-verbal,
  sub-lexical" naming is not overturned — the "tend"/52="end" lead is
  packaged as a follow-up hypothesis for red-team adjudication, not as
  a contradiction (it is compatible with the parent's byte evidence;
  only the class label's scope is questioned).
- **`ne-1331-70-52-parse` Arm A.** Consistent: 52 as prendre-family stem
  at @1332 is compatible with 52="end" ("prend").

## Verdict: NULL (fence as underdetermined)

C1 fails; C2 fires. The "t52" word at @631–632 cannot be named at battery
grade. The locus is fenced as underdetermined (evidentiary; re-openable
on a named 52 value, a resolved "[74] que [60]" tail, or red-team
adjudication of the 52 split docket).

## Follow-ups (for supervisor; all verified ABSENT from battery-queue.json)

1. `end-52-uniform-value` (P4) — test 52="end" as a uniform sub-lexical
   value: "tend" (3sg *tendre*) at @630, "prend" (3sg *prendre*) at @1332
   with "ne prend" @1330–1332 (consistent with ne-1331-70-52-parse Arm A).
   Decides whether the cross-locus uniformity survives the
   val-52-630-frame "non-verbal" label; red-team venue if the label
   tension cannot be resolved at battery grade.
2. `t52-74que60-tail` (P4) — resolve the "[74] que [60]" tail @635–637
   (3× "74 46" stream-wide: @418, @635, @693, all subjectless under
   46='que'). The tail blocks every full-window parse of @628–636;
   re-opens the "t52" naming iff a licensed parse is found.
3. `veut-67-633-infinitive` (P4) — test 67="veut" at @633 with 63 as
   infinitive ("et [t52-NP] veut [63-INF] [74] que [60]"). The
   "et [noun] veut [INF]" frame is corpus-attested ("et ça veut porter",
   "et ennemi veut percer"); re-opens the locus iff a t-word nominal
   subject is statable.

## Scope

Locus-level only (@631–632, row a4_01). Untouched: 52's other tiers and
loci, 63's verb class, 74's open class/value, 78's open value, 60's
conditioned 'vient', the 52 split docket (red-team venue), §7. No
standing or red-team verdict contradicted, downgraded, or re-litigated.
Canonical-stream caveat stands (row a4_01 offsets unvalidated).

## Bookkeeping

- Lock: `code/crowd17/next-token/locks/word-t52-630-identify.lock` created
  on start (agent ed88f1a0-6ac3-4743-ac3a-a2ec334de61e,
  2026-10-09T21:23:28Z; no stale lock present), deleted on completion.
- Report: `code/crowd17/report_inbox/battery-word-t52-630-identify.md`
  (this file).
- Queue: `word-t52-630-identify` → `status: verdict`,
  `verdict: {result: null, report: ..., date: 2026-10-09}` — pre-write
  asserted queued/verdictless; written through target-id-unique temp
  file `battery-queue.json.word-t52-630-identify.tmp` + atomic rename;
  disk re-validated; own entry only; no downgrade; no tmp leftover.
- R5005, sealed gate instances, red-team adjudication queue untouched.
