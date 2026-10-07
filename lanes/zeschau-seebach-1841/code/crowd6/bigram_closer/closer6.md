# Round 6 — Bigram Closer: exploit 77="le" (provisional, CONDITIONED)

Worker: bigram_closer_round6 · 2026-10-07 · `code/crowd6/bigram_closer/closer6.py`,
`closer6_era.py`
Numbers: `closer6.json`, `closer6_era.json`, `closer6_quesub.json` (this dir).
Cipher: R5005 **repaired** 1,847-pair parse (`code/crowd4/repaired_parse.py`).
Era: Tocqueville t1+t2 word-space (elision-split for "me"-morpheme; plain for
article frames); Les Mis as register-robustness. F30: word-space legs only;
N22 exclusions enforced (29/82/34 all legs; 40 conditionals). Kill rule:
cipher n≥3 AND era count 0. Band 0.5–2.0 UNCALIBRATED (context only).

Baseline: `code/crowd5/redteam/verify_baseline.py` still PASS (31/31);
re-derived numbers below agree with it exactly where they overlap
(77→86=5 @430/798/877/950/1133; 77→78=7; n78=31; 94→82=4
@578/1182/1353/1742; 87-64-77-84 @1800). Extension (new, re-derived):
n77=44, n84=25 (rank 26), n45=22 (rank 32), n59=27,
78→45=4 @313/573/982/1164, 84→59=4 @1189/1290/1447/1803,
64-77-84 @144/1445/1801, 64-77-84-59 @1445/1801,
77-78-94-82-06 @1180/1351, 77→78 @7/213/647/1077/1180/1351/1542.

## Thread (a): identify 84 — NULL on identity, LEAD on class, re-parse of the slot

**Verdict: 84 is a masculine NOUN (que-clause subject) — LEAD-grade on class;
specific identity NULL (honest, register-robust). 59="verb" supporting LEAD.**

Frame inventory (25 occurrences, all re-derived):
- 77→84 ×7 @145/259/1057/1446/1484/1763/1802 («le 84» ×7)
- 11→84 ×1 @1620 («la 84» ×1)
- 46→84 ×2 @309/@472 («que 84» ×2): @309 = 17-46-84-24, @472 = 67(veut)-46-84-24
- @1485 = 46-77-84-24 («que le 84 24»)
- So 84 = subject of a que-clause ×3 (@309, @472, @1485), article+noun ×8.

Checks (≥2, independent):
1. **Article-frame era inversion** (Tocqueville, plain tokenizer): era words in
   top-40 «le»-followers AND ≥3 after «la»: exactly 4 — «plus» 1.93× (in-band,
   band-edge), «même» 3.56×, «faire» 7.48×, «fait» 6.75×. «plus» is the only
   in-band hit and fails the subject frames grammatically («veut que plus 24»
   ungrammatical). No noun identified.
2. **Que-subject era inversion**: P(W|"que") top-40, unigram band vs P(84):
   in-band hits are «le» 0.64, «dans» 1.19, «des» 0.76, «se» 1.91, «du» 1.34 —
   ALL fail the article frames («le dans», «le se» ungrammatical). No
   subject-word identified.
3. **Register robustness** (Les Mis): article inversion yields only «plus»
   3.18× and «même» 5.48× — both out. NULL holds under both registers.
4. **Kills re-verified**: 84="fait" 6.75× (matches F42's 6.7×); 84="gouvernement"
   6.12× (new — kills the whole-word reading despite the 5-mer coincidence).

Structural advance — the slot re-parse (the thread's real product):
- **F42 undercount corrected: 84→59 is ×4, not ×2** (@1189/@1290 are
  trigram-external; F42 counted only trigram-internal).
- 59→46 ×2 @216/@1190 («59 que») + 59→37 ×6 @528/624/912/1178/1443/1796
  («59 le») → **59="verb" LEAD** (2 legs; needs its own battery — not promoted
  here).
- Hence 64-77-84-59 ×2 (@1445–1448, @1801–1804) = **«qui le [NOUN=84]
  [VERB=59]»** — F42's «ce qui [verbe] 84» becomes «ce qui le [noun] [verb]»:
  **the verb slot is 59, not 84.** The @1800–1803 window is «ce qui le 84 59»,
  verb identified (as a lead), noun still open.
- Bonus coherence: @1178–1184 = 59-37-77-78-94-82-06 = «[59=verb] le
  [gouvernement]» under 37="le"-article (MEDIUM) + the fenced 5-mer host —
  circumstantial, noted not claimed.

Fenced tension (for the 24 battery): «que 84 24» ×2 with 84=noun-subject wants
24=verb, pressuring the 24="en" STRONG lead (F31). Not a kill — flagged.

Loose end: @144–147 = «qui le 84 er» (84→29 ×1): 84=noun + er-initial next
word, or by-ear infinitive split. Single instance, unclassified, not a kill.

For the 87=ce Closer (WO2 coordination): the «ce qui __ ce que» verb battery
should treat 59 — not 84, not 96 — as the verb in the @1800 window. No
duplication: this note covers 84/59 only.

## Thread (b): the "le me"×7 — DISSOLVED (conditionally, no holdouts)

**Verdict: the ×7 dissolves exactly as F38 claimed, on the repaired parse.
Dissolution is conditional twice over (F37's fences stand).**

Re-derived positions: 77→78 ×7 @7/213/647/1077/1180/1351/1542. Classification:
- 2/7 = the «ver»-islet (78→94): @1180, @1351 — both inside the ×2 5-mer
  77-78-94-82-06. Dissolution rides on the FENCED «gouvernement» host
  (77="gou" unconfirmed).
- 5/7 = me-syllable frames: @7 (fol78=18), @213 (06), @647 (52), @1077 (64),
  @1542 (43). Dissolution rides on 78="me"-syllable-LEAD (F38); if that LEAD
  falls, the kill-grade «le me» era-0 adverse revives (F37 fence).

Independent checks:
- B2: era («le»,«me»)=0/4570 re-derived (plain model) — the word-level adverse
  stands, dissolved only under the syllable reading. B3: no 78→45 inside the
  ×7; era («me»,«me»)=0 — the flag doesn't fire.
- B4 (association): P(78|77)=0.1591 (9.48× over base) vs P(78|47)=0.1786,
  P(78|37)=0.1429, P(78|11)=0.0444 — **77 is unremarkable**; 47→78 and 37→78
  are equally strong. The bigram needs no special «le me» construction; it is
  in line with other proclitic→78 rates. Independent dissolution support.
- B1: follower-of-78 inside ×7 = {18,06,52,64,43} + {94:2 islet}; outside
  distribution contains all five (45×4, 40×3, 48×2, 49×2, 41×2, 62×2, 18, 06,
  52, 64, 43, …) — no outlier follower inside the ×7.

Tabulation bug caught and fixed in this worker's code (F26-6 traceability):
the first B1 pass compared 78-positions against the 77-position list
(off-by-one), double-counting the two islets as "outside". Corrected:
exactly two 78→94 in the whole stream, both inside the ×7. Numbers above are
the corrected ones.

## Thread (c): 45="me" — WORD disfavored-strong; 78-45="même" LEAD

**Verdict: 45="me"-WORD → DISFAVORED-strong (not REFUTED: the kill leg is
provisional-conditioned). 78→45 ×4 = «même» (me|me) → LEAD.**

Against 45="me"-word (78→45 ×4 @313/573/982/1164):
- C1: P(45)=0.01191 vs era me-morpheme (m+me, elision-split) 0.00130 →
  **9.14× out** (strict «me»-word: 16.2× out).
- «par me» ×2 (96→45 @?/—) era-0 — fenced on 96="par" provisional (n=2,
  below the kill rule).
- «me qui» ×3 (45→64) era-0 — MEETS the kill rule (n≥3, era 0) but fenced on
  64="qui" provisional. («m'qui» era-0 too.)
- Grade: DISFAVORED-strong. The unigram fail is band-uncalibrated context;
  the kill-rule hit is provisional-conditioned — hence not REFUTED.

For 78-45="même" (syllable bigram me|me):
- Unigram: cipher P(78-45)=0.00217 vs era P("même")=0.00380 → **0.57× in-band**.
- Era locks: «le même» 87×, «même qui» 11×, «ce même» 18×.
- @313 = 24-37-78-45-64: 37-78-45-64 = **«le même qui»** (37="le" MEDIUM) —
  fully grammatical; @982 = 76-47-78-45-01 = «ce même [01]» («ce même» 18× era).
- The F39 sixmer 78-45-13-55-61-94 ×2 (@573/@1164) = «même 13-55-61 [94]».
- Implication: 45="me"-syllable is a **homophone of 78** for the same syllable
  (petit-chiffre sparse homophones, F35); «même»=me|me uses two groups.

Interaction with (b): none of the ×7's 78s is followed by 45 — no «me me»
tension inside the ×7. All four 78→45 hosts are non-islet 78s, i.e. inside
F38's me-syllable population — consistent with the partition.

## Nulls preserved
- 84's specific identity: NULL (register-robust; the systematic inversions
  exhaust the top-400 in-band era words with zero grammatical passers).
- 59="verb": LEAD only (2 legs), needs its own ≥2-check battery — not promoted.
- 45="me"-word: DISFAVORED-strong, not REFUTED (kill leg fenced on 64="qui").
- No new promotion recommended by this worker. 77="le" provisional-CONDITIONED
  stands; its «le me»×7 dependency is now mapped per-instance with both fences
  explicit.
