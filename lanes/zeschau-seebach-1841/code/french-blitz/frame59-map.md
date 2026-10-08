# 59-FRAME MAP — conditioned «est» / «-este» audit (2026-10-07)

59-FRAME MAPPER (direct French-work agent, no coordinator). Task: map every 59
window against 1841 diplomatic French syntax; test ISLET 10's conditioning rule;
predict the @1448/@1804 deaths.

## Stream
Repaired parse, 1,847 pairs (`code/side-keyhunt/repaired_offsets.json`), 0-based
pair positions. n59=27 (verified by census; matches lane).

## Corpus
3.87M French tokens: clean diplomatic core (Nesselrode v7/v9/v10, Pozzo di Borgo,
Guizot t5–t6 despatches, Levant 1841 P3, Talleyrand, Metternich v4/v6 = 1.6M) +
RdM 1841 Q1–Q4 + Guizot t1–t3 (2.3M). Lane `tok_elision` tokenizer verbatim
(elisions split: «n'est» → `n' est`). Nesselrode v8 kept OUT of phrase queries
(OCR word-split caution per round-11 flag); spot-checked separately where noted.
All counts below are on the 3.87M pool unless marked v8.

## Key corpus facts (new numbers)
- «qui est» = 1033 · «n'est» = 3674 · «ne l' est» = 51 · «on n'est» = 44
- «la est» = 0 · «ce est» = 0 · «qui le est» = 0 · «ce qui le est» = 0
- «cela est» = 173 (alternative at @463 — LIVE)
- «y est» = 213 (grammatical, but «m'y est» ungrammatical — @1833 still dead)
- «est le» = 1079 (S5 bigram viable)
- «n'est le» = 10, ALL as «si ce n'est le» (restrictive; 5 Metternich v6, 1 v10, 3 RdM) — @1796 lacks «si ce»
- «est le qui» = 0 (@528/@1443 trigram — adverse for S5 at those windows)
- «pour est» = 1 (OCR garbage: «un droit de pour est plus qu'» — effectively 0)
- «reste en» = 21 (@1496 verb-unit alternative viable)
- «en ce» = 441 (moment 195, qui 76, genre 32... — @825's frame is noun-or-qui, never «est»)
- «m' est» = 150 («il m'est» dative type)

## Per-window table

| pos | window (pre-59-suc) | ±3 context | French verdict | bucket |
|---|---|---|---|---|
| @103 | 93-59-45 | on ne l' EST 45 | «on ne l'est» — 51 hits, clean | EST-ARM ✓ |
| @216 | 06-59-46 | le 78 06 EST que er | [06-59] verb-unit + «que»; F52 caveat-3 dissolved | FENCED SUB-TIER |
| @316 | 64-59-32 | 45 qui EST 32 | «qui est» — 1033 hits, clean | EST-ARM ✓ |
| @448 | 61-59-32 | on 61 EST 32 | «on [61-59]» frame-forced unit (needs «on»; cf @1511) | FENCED SUB-TIER |
| @463 | 11-59-42 | ce la EST 42 | «la est»=0 kills naive; «cela est»=173 LIVE if 87-11=«cela» (over-split, cf Frenchman H-split) | **F1-WATCH** (nearest miss) |
| @528 | 44-59-37 | 47 44 EST 37 qui | S5-fenced; «est le qui»=0 → adverse for S5 HERE even granting 37=«le» | S5-FENCED (flagged) |
| @554 | 86-59-34 | pour 86 EST i | «pour»+«est»=0 → [86-59] unit lean stands | FENCED LEAN |
| @559 | 94-59-30 | 86 ne EST 30 | «n'est» — 3674 hits, clean | EST-ARM ✓ |
| @624 | 14-59-37 | m 14 EST 37 | S5-fenced; «m' [14] est le» conditional on 14 | S5-FENCED |
| @763 | 94-59-39 | on ne EST 39 | «on n'est» — 44 hits, clean | EST-ARM ✓ |
| @825 | 87-59-38 | en ce EST 38 | «ce est»=0 kills word-«est»; «en ce»=441 takes noun/«qui» — value OPEN | UNCLASSIFIED (est ruled out) |
| @834 | 76-59-35 | la le 76 EST 35 | «le [76] est» conditional on 76=noun (76 unknown) | UNCLASSIFIED |
| @912 | 83-59-37 | qui 83 EST 37 | S5-fenced; «qui [83] est le» conditional on 83 | S5-FENCED |
| @1178 | 48-59-37 | 32 48 EST 37 | S5-fenced; 48 unidentified | S5-FENCED |
| @1186 | 06-59-42 | m 06 06 EST 42 | «ne me [06-59]» unit | FENCED SUB-TIER |
| @1190 | 84-59-46 | 06 84 EST que | [84-59] verb-unit + «que» — firm | ESTE-ARM ✓ |
| @1210 | 64-59-32 | 65 qui EST 32 | «qui est» — clean | EST-ARM ✓ |
| @1291 | 84-59-35 | la 17 84 EST 35 | verb-unit vs «la [17-84] est» — needs 17/35 | FENCED |
| @1443 | 68-59-37 | pas 68 EST 37 | S5-fenced; «est le qui»=0 → adverse for S5 HERE | S5-FENCED (flagged) |
| @1448 | 84-59-36 | qui le 84 EST 36 | «qui le [V-este]»; word-«est» DEAD («qui le est»=0) — **rule predicts this** (pre=84) | ESTE-ARM ✓ (death predicted) |
| @1496 | 15-59-24 | pour 66 15 EST en | «[15-59=reste] en [89]» (21 hits) vs «[15] est en» — needs 15 | FENCED |
| @1511 | 61-59-39 | 12 61 EST 39 | pre=61 but NOT frame-forced (no «on»; cf @448) | UNCLASSIFIED |
| @1715 | 44-59-30 | ne 44 EST 30 | «ne [44-59]» frame-forced unit | FENCED SUB-TIER |
| @1777 | 64-59-19 | ce qui EST 19 | «ce qui est» — clean | EST-ARM ✓ |
| @1796 | 94-59-37 | 42 ne EST 37 | S5-fenced; «n'est le» licensed ONLY as «si ce n'est le» (10/10) — window lacks «si ce» → adverse for S5 HERE | S5-FENCED (flagged) |
| @1804 | 84-59-35 | qui le 84 EST 35 | «qui le [V-este]»; word-«est» DEAD («qui le est»=0) — **rule predicts this** (pre=84) | ESTE-ARM ✓ (death predicted) |
| @1833 | 16-59-36 | en m i EST 36 | «m'y est» ungrammatical; «m'i» not a word — word-«est» strained; value OPEN | UNCLASSIFIED (est strained) |

## The @1448/@1804 deaths (as tasked)
Both have pre=84. ISLET 10's rule says pre=84 → verb-final «-este», never
word-«est». Corpus: «qui le est» = 0/3.87M and «ce qui le est» = 0 — word-«est»
is era-absent after «qui le», exactly as the rule predicts. The rule doesn't
just accommodate the deaths; it *requires* them. ✓✓

## Conditioning rule — AUDIT VERDICT: HOLDS, no widening
- **EST-ARM** (59=word-«est» iff pre∈{64,94,93}): 6/6 windows clean
  (@103 «ne l'est», @316/@1210/@1777 «(ce) qui est», @559/@763 «n'est»).
  n_eff=6. No adverse.
- **ESTE-ARM** (59=verb-final iff pre=84): @1190 firm, @1448/@1804 firm
  (deaths predicted), @1291 fenced. n_eff=3.
- **F1** (pre∉{64,94,93} window REQUIRING word-«est»): NOT FIRED. Nearest
  miss is @463 («cela est»=173 viable, but doesn't *require* word-«est»;
  87=«ce» is provisional). Bank @463 as **F1-WATCH**: if 42's identity ever
  forces «cela est [42]», widen rule to pre=11 iff pre-pre=87.
- **F2/F3/F4**: no new data; standing.

## New adverse data for the S5 fence (reported, NOT re-litigated)
The S5 fence (59-37 windows pending 37=«le» MEDIUM) has three new adverses:
1. @528 & @1443: «est le qui» = 0/3.87M — even granting 37=«le» and 64=«qui»,
   the trigram is era-absent.
2. @1796: «n'est le» occurs 10× but EXCLUSIVELY as «si ce n'est le»; the
   window (56=plus 42 94 59 37) lacks «si ce».
Flagged to the conditioner; the fence itself stands (not my docket).

## Genuinely open (non-fenced) windows
- @825: word-«est» ruled out («ce est»=0); «en ce»+noun/«qui» frame open — 59's value here is unknown (third value? misparse?).
- @834: conditional on 76=noun.
- @1511: pre=61 leftover — the @448/@1511 asymmetry (frame-forcing needs «on»?) is unexplained.
- @1833: word-«est» strained; value open.

## Provisional-status verdict: HOLD (do not narrow, do not fall)
ISLET 10 survives this audit intact: 6/6 est-arm clean, both deaths predicted
by the pre=84 arm, no F1 firing. The provisional stands as conditioned
(est-arm + este-arm + fenced sub-tiers). Narrowing further would discard the
fenced sub-tiers prematurely; falling would ignore 6 clean proclitic frames.

## Recommended follow-ups
1. **@463 F1-WATCH**: identify 42 — if it forces «cela est [42]», widen the rule.
2. **@825**: the only non-fenced window where word-«est» is ruled OUT — prime
   candidate for 59's third value or a parse check.
3. **S5 triage**: the conditioner should confront the three new adverses
   (@528/@1443 trigram, @1796 «si ce» requirement) before spending more on 37.
4. **@448/@1511**: name what makes @448 frame-forced — test whether «on» is
   the licensor (predicts: no other pre=61 window without «on» reads as unit).
