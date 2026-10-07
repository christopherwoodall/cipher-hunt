# PRE-REGISTRATION — Round-8 59="est" consolidation battery (59-CLOSER)

Date: 2026-10-07. Executor: 59-closer (round-8 work order 2).
Claim under test: **59="est" provisional — CONFIRM, DOWNGRADE, or bound the residual.**
Standing: F52 (round-7 closer; red-team RULINGS-ROUND7: PROMOTION GRANTED with
modification). Four live legs: S1 1.10× vs Nesselrode v8; S2 "qui est" 3/47;
S3 "n'est" 3/37; rivals re-killed 9–51× on diplomatic rates. S4 count-adverse
resolved statistically (L1: binomial P(X≥2|n=27)=0.11–0.31 n.s.).

Two open gaps (this battery):
- **G1 (S5 dependency):** S5 = 59→37 ×6 "[c']est le" (6.47× over, Tocqueville
  basis) is FENCED on 37="le" MEDIUM (F31 frenchman ear + F56 M6 single weak
  rate leg 1.89×). The promotion verdict never used S5 — but the dependency
  was never examined, only fenced.
- **G2 (S4#1 frame):** S4#1 = 06-59-46-29 @216. L2 (structural) FAILED as
  pre-registered: no licensed "NP est que" frame under banked values
  (06 = verb-stem class, not noun-typed). Statistically resolved only.
  Additional wrinkle found in work-order review (to be verified in B4):
  the closer's "S4#2 admits the cleft conditioned on 84=noun" looks
  unlicensed under F53's actual rule (84=noun iff pre(84)∈{77,11};
  pre(84)@1193 = 06 → UNCLASSIFIED).

## Battery legs (run AFTER this file is written)

### G1 — S5 dependency examination
- **A1 [cipher census].** The 6 59→37 windows with ±2-pair context
  (re-derived; verify_f26_17 expects exactly 6). Record predecessor of 59
  at each: is any 87 ("c'est le" trigram) or all bare ("est le")?
- **A2 [rate, register-best].** Cipher P(37|59)=6/27 vs Nesselrode v8
  P(le|est), elision-split tokenization (same as diplomatic_rates.py).
  ALSO the conditioned comparator P(le | est with preceding token ∉ {c',ce})
  ("bare est"), since A1 determines whether the cipher 59s are bare.
  Report both raw ratios (factor-2 band uncalibrated per F26-1 — no band
  verdict, raw numbers only). Also corpus rate of "n'est le"-type
  (n'/ne + est + le) for the @1796 94-59-37 window if 94="ne"∧37="le".
- **A3 [37="le" audit].** Enumerate 37="le"'s positive legs (F31 ear MEDIUM;
  F56 M6 1.89× single weak leg) and cipher-side profile (n37=28;
  37's predecessor/follower sets) — any grammatical hostility under "le"?
  No new 37 claim; grades the dependency only.
- **A4 [sensitivity].** (i) Was S5 load-bearing in the promotion verdict?
  (Verdict rule: L1∨L2 ∧ I1+I2+I3 ∧ L3 ∧ L4 ∧ L5, ≥2 of {L1..L5} — S5 absent.)
  (ii) Under 37="le"-false: 59→37 ×6 = "est"+X, X unidentified → no
  grammatical hostility possible; verdict unchanged. (iii) Under 37="le"-true:
  S5 is worth exactly A2's number. Verdict rule: FENCE-STANDS iff the
  promotion verdict would move under 37="le"-false; else FENCE-DISSOLVED
  (S5 banked as weak corroboration/anomaly per A2, quarantined from 59).

### G2 — S4 frame-level test
- **L0 [forced-reading lemma].** Under 59="est" ∧ 46="que" (GT): is the
  two-word "est"+"que" reading forced? Test: regex `estqu\w*` on raw
  Nesselrode v8 text (letter-level, no tokenization) — count French words
  with adjacent "est"+"qu" letter sequences. Bar: ~0 (≤2, eyeball them) →
  no single-word parse; 59|46 is a word boundary; 59 is the word "est".
  (46|29 boundary: no French word "que"+"er"-second-syllable; state as
  lexical observation, checked against the same regex pass `qu\w*er`
  if needed — keep it light: assert from lexicon knowledge, flag if
  the regex finds candidates.)
- **B1 [frame inventory].** All "est que" bigrams in Nesselrode v8
  (elision-split tokens, same tokenizer as diplomatic_rates.py). For each:
  verbatim pre-word and suc-word. Classify pre-word: closed-class
  {c', ce, n', ne, se, il, elle, ils, elles, on, nous, vous, je, tu, qui}
  exact-match; else "open" (list top open pre-words verbatim).
  Also pull "est qu'" + vowel-initial suc (elided frames).
- **B2 [compatibility].** Compatible pre for S4#1: pre ∉ {c',ce,n',ne}
  (06 is verb-stem class: not ce/ne; not noun-typed per L2) — primary
  filter: pre-word ends in /ɑ̃/ proxy (letters "ent"/"ant"/"an"/"en"/"em";
  06's best-guess sound is restricted-"ent" /ɑ̃/, PLAUSIBLE not confirmed —
  run BOTH the /ɑ̃/-filtered and the unfiltered-not-ce/ne versions and
  report both). Compatible suc: starts with "er"/"err" ("que erX" unelided
  OR "qu'erX" elided — count both, note elision).
  Bar: PASS (frame exists) iff ≥1 instance with compatible pre AND
  er-initial suc. FAIL → residual stands, quantified as 0/N of N
  "est que" instances (report N, closest misses verbatim).
- **B3 [encipherer elision habit].** 46="que" GT: cipher successors 46→X
  where X ∈ {29,34,40} (known vowel-initial syllables: er/i/e). If ≥1
  (already have 46→29 ×2), the encipherer writes "que"+vowel UNELIDED →
  "que er" needs no elision apology; corpus comparison may use unelided
  "que"+"er" forms. If 0 elsewhere, note the elision question as open.
- **B4 [S4#2 predecessor rule-check].** pre(84)@1193 re-derived. F53 rule:
  84="en" iff pre∈{46,94,82}; 84=noun iff pre∈{77,11}; else UNCLASSIFIED.
  If pre=06 → 84 UNCLASSIFIED at S4#2 → closer's "cleft conditioned on
  84=noun" is UNLICENSED → S4#2 frame-unexplained too (correction to the
  round-7 record). Check no other banked rule licenses 84=noun@1193.

## Verdict rule (pre-registered)
- **provisional CONFIRMED** iff: (i) A4 shows the verdict S5-independent
  (fence dissolved or stands-but-quarantined — either way 59 doesn't move);
  AND (ii) B2 PASS (S4#1 frame closed — gap gone) OR B2 FAIL with the
  residual honestly bounded (0/N, closest misses, B4 correction recorded,
  L0 lemma holding). The provisional grade never required frame closure;
  it requires no HIDDEN adverse weight.
- **DOWNGRADE to STRONG LEAD** iff: A2 shows S5 adverse (>2× raw over on
  the bare-est comparator, not explainable) AND A4 shows verdict-sensitivity;
  OR B2 FAIL combines with new adverse (e.g., B3 shows the encipherer DOES
  elide elsewhere, making unelided "que er" anomalous; or L0 fails).
- **Residual statement** (if CONFIRMED with B2 FAIL): "2/2 S4 windows lack
  a licensed grammatical frame under banked values (S4#1: pre=06 verb-stem;
  S4#2: pre(84)=06 → 84 unclassified per F53). Count-level adverse n.s.
  (L1). 59='est' provisional with an explicit unexplained-frame residual."

## Method notes
- Canonical parse: repaired 1,847-pair (`code/side-keyhunt/repaired_offsets.json`);
  loader: `code/crowd5/redteam/verify_baseline.load_stream`.
- Corpus: Nesselrode v8 primary (`code/side-period/corpus/nesselrode-v8.txt`);
  Guizot t5–t6 as the check where a number matters. Tokenizer: copy of
  `code/crowd7/closer/diplomatic_rates.py::tokenize` (elision-split).
- Independence: A2/B1/B2 are corpus-external; A1/A3/A4/B3/B4/L0 are
  cipher-internal or lexical — ≥2 independent legs available per gap.
- T7: per-window nulls only; no bearing-count scoring. No new promotions
  claimed here. Verdict is a recommendation — red team adjudicates.
- Report note: `code/crowd8/report_inbox/closer59-consolidation.md`.
