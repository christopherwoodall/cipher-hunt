# Battery report: redteam-01-split-input (GATHER-ONLY evidence package)

- Target id: `redteam-01-split-input`
- Date: 2026-10-09
- Worker: battery worker (subagent 805d2567-ddec-441b-a0c1-89e513c5ccd0)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  Re-derived in-session: 1,847 pairs, 96 types, n(01)=28. All @-offsets are
  0-based repaired-stream indices marking the 01 token unless stated.
  Never used canonical.py. R5005 not touched. Red-team adjudication queue
  not touched.
- Lock: code/crowd17/next-token/locks/redteam-01-split-input.lock (created at
  start, deleted on completion; no prior lock for this id existed).

## Bar (verbatim, pre-registered before testing)

"gather only, do not declare: 'en' survives cleanly only at @988; 'on' at
@893/@970/@40; the three '37 01' windows need word-internal 01 under A12.
Uniform value impossible under standing values -> split/polyvalence venue
for 01"

Numbered pass/fail clauses (restated before testing, not modified after):

1. 'en' survives cleanly ONLY at @988: the byte window is documented and no
   other 01 window offers a clean uniform-'en' leg.
2. 'on' readings at @893/@970/@40: the three byte windows are documented
   with the stated reading and its standing-value dependencies.
3. The three '37 01' windows (@940, @1634, @1818, 01-positions) need
   word-internal 01 under the A12 frame: documented with the standing
   battery result.
4. Uniform value impossible under standing values: the kill counts for each
   uniform candidate are re-stated from the standing battery record.
5. Do not declare: this package names no 01 value and decides no
   split/polyvalence — that is red-team venue per protocol §7.

## Method

1. Re-derived the repaired parse in-session (1,847 pairs / 96 types).
2. Byte-exact adjacency census for 01: '37 01' x3, '76 01' x2, '48 01' x1,
   '41 01' x1, '01 24' x3; full predecessor/follower census of all 28
   01-windows re-derived (matches battery-val-01-census exactly).
3. Extracted +-5 byte windows at every locus named in the bar.
4. Collated the standing battery/red-team record on 01 (cited, not
   re-litigated): battery-val-01-census (NULL), battery-wordinternal-37-01
   (PROMOTE, battery-level), battery-disc-01-24-ci-X (PROMOTE,
   battery-level), R17-015 (KILL 01='ci'/'faisant' global), R20-016
   (DUPLICATE; GRANT LEAD 24={faire} + 01="en" local LEAD), R20-113 (GRANT;
   reading (i) wins at @984, 01='en' reading (iii) REJECTED there),
   R20-085 (CONFIRM A12 37-01 unit).

## Window-level evidence (all byte-exact, re-derived)

### Clause 1 — 'en' @988 (sole clean leg)

- 01@988, row a6_01: `45 01 24 89 48 01 76 49 24 26 30`
- '48 01' is stream-unique (x1, @987-988). Predecessor 48, follower 76.
- Standing battery record (battery-val-01-census, C2): uniform 01='en'
  dies at 9 kill-grade windows: @40 ("en [V-fin]", fol=24 finite/modal),
  @295 ("en la", fol=11='la' GT), @596 ("en er", fol=29='er' GT),
  @828 ("en [V-fin]"), @893 ("en vient", fol=98), @949 ("en le",
  fol=77='le' provisional), @970 ("en vient"), @976 ("en pour",
  fol=00='pour' granted), @984 ("en [V-fin]"). Sole clean leg: @988,
  fol=76 (promoted masculine noun) -> "en [N-masc]" ("en France"-shaped).
- No other 01 window offers a clean 'en' leg: the remaining 18 windows are
  undetermined (open-value neighbors) or hostile per the census.
- Clause 1: PASS (evidence as stated in the bar).

### Clause 2 — 'on' @893 / @970 / @40

- 01@893, row a5_08: `00 86 06 77 76 01 98 82 14 98 83`
  ('76 01' @892-893; fol=98).
- 01@970, row a6_00: `19 24 06 77 76 01 98 48 51 45 08`
  ('76 01' @969-970; fol=98). '76 01' is x2 stream-wide, byte-identical
  left 4-gram `06 77 76 01` at both.
- 01@40, row a1_01: `08 91 39 64 41 01 24 88 43 81 30`
  ('41 01' @39-40, stream-unique; fol=24).
- Stated readings per battery-val-01-census (new rival tested):
  @893/@970: 01='on' + 98='vient' -> "on vient";
  @40: "[41] on [24-fin]" (01='on' token, fol=24 finite/modal);
  @984 also lives ("on [24-fin]") but is NOT in this bar's list.
- Standing dependencies/notes: 98='vient' is battery-grade/LEAD;
  uniform 01='on' is killed at 5+ windows (@34 fol=08 letter-tier,
  @596 "on er", @976 "on pour", @988 "on [76-N]", @1029 "on [03]er")
  and the three 37-01 unit windows are hostile under A12; it also
  creates an unlicensed homophone with promoted 84="on" (A15) —
  red-team venue.
- Tension flagged (not resolved): @40 is simultaneously the
  battery-promoted 01='en'-local window of battery-disc-01-24-ci-X
  ("en faire", 24={faire} LEAD per R20-016) and the census's 'on' leg
  ("[41] on [24-fin]"). Both are battery-level/unratified; R20-113
  rejected the 'en' reading at @984 only, not at @40/@828.
- Clause 2: PASS (windows and readings documented as stated in the bar).

### Clause 3 — word-internal 01 in the three '37 01' windows under A12

- 01@940, row a5_10: `00 33 21 64 37 01 07 50 40 08 62`
- 01@1634, row a8_03: `00 33 21 64 37 01 74 87 74 74 35`
- 01@1818, row a8_10: `50 42 06 29 37 01 02 09 19 00 97`
- '37 01' is x3 stream-wide (37-positions @939/@1633/@1817), no other
  adjacency. W1/W2 share the byte-identical left 8-gram
  `56 69 26 00 33 21 64 37` (@932-939, @1626-1633).
- Standing battery result (battery-wordinternal-37-01, PROMOTE,
  battery-level, unratified): the three windows parse as ONE word, a
  "faire"-compound 3sg finite verb ("satisfait"/"contrefait"-shaped);
  01 = "fait" (/fE/) as a LOCAL word-internal syllable. Named disjuncts
  killed: "-faisant" compound adjective, "-ci" ending, "-tain" ending
  (all dead at "qui"+non-verb, W1/W2). A12's 37-01 unit grant affirmed
  (not re-litigated); 37's global value not named.
- The 01="fait" syllable is local to these three windows and disjoint
  from the 'en'/'on' window sets.
- Clause 3: PASS (evidence as stated in the bar).

### Clause 4 — uniform value impossible under standing values

Re-stated from the standing record (battery-val-01-census, verdict NULL;
C1 PASS / C2 FAIL):

- 01='en' uniform: 9 kill-grade deaths (listed under Clause 1). FAIL.
- 01='tain' uniform: zero positive legs under standing values; the
  37-01 windows would need 37='cer' (killed, rival-37-01-certain). FAIL.
- 01='on' uniform: 5+ kill-grade deaths + 3 hostile A12 unit windows +
  unlicensed homophone with 84="on" (A15). FAIL.
- Global kills standing: R17-015 killed 01='ci' and 01='faisant'
  (ci-01-value KILL CONFIRMED).
- Protocol §7: 67 et/veut is the sole true polyvalence; no second
  polyvalence has been declared.
- The surviving local readings are mutually exclusive as a uniform
  value: 'en'@988 (preposition + nominal), 'on'@893/@970/@40/@984
  (pronoun + finite verb), 'fait'-syllable in 37-01 x3, 'en'-local at
  the 01-24 windows (R20-016 LEAD; @984 rejected by R20-113 in favor
  of bound '-ci'/ceci), bound '-ci' at 87-01/47-01/45-01 windows.
- Clause 4: PASS (uniform impossibility documented as stated in the bar).

### Clause 5 — no declaration made

- This package names no 01 value, promotes nothing, kills nothing, and
  decides no split/polyvalence. All readings above are cited at their
  standing grades (battery-level/unratified, LEAD, or NULL) and every
  grade is preserved exactly as found.
- Clause 5: PASS.

## Per-clause pass/fail

1. 'en' sole clean leg @988: PASS.
2. 'on' windows @893/@970/@40: PASS.
3. Word-internal 01 in 37-01 x3 under A12: PASS.
4. Uniform value impossible: PASS.
5. No declaration: PASS.

## Verdict: NULL (gather-only by design)

Evidence package complete. All five bar clauses pass as documentation
clauses. No standing or red-team verdict is contradicted, downgraded, or
re-decided: R17-015, R20-016, R20-085, R20-113, A12, A15, R24, and §7 are
adopted exactly as standing.

## Follow-up targets (per §4)

1. **redteam-01-split-docket** (P1): red-team decision item — the 01
   split/polyvalence venue. Input: this package. The question: whether
   the disjoint local readings ('en'@988, 'on'@893/@970/@40(/@984),
   'fait'-syllable in 37-01 x3, 'en'-local @40/@828, bound '-ci'
   elsewhere) warrant a conditioned split, a declared polyvalence
   (second after 67), or continued deferral. Red-team only per §7.
2. **en-988-standalone-leg** (P3): give the @988 'en' local reading a
   frame/corpus leg or fence it — currently its only support is the
   single clean window (fol=76 promoted masculine noun). Discriminates
   whether the 'en' survivor is a lead or a coincidence.
3. **on-01-vs-84-homophony** (P2): adjudicate the 01='on' local reading
   against promoted 84="on" (A15): conditioned split (positional
   resolution, cf. the 67 precedent), homophone license, or kill of
   the 01='on' legs. Red-team venue; battery gathers the positional
   distribution (01='on' lives: @40/@893/@970/@984; 84="on": C1–C3
   conditions).

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-redteam-01-split-input.md
- Queue entry `redteam-01-split-input`: status -> verdict,
  verdict.result = null (gather-only), report path + date recorded.
- Lock deleted on completion.
- Scope: R5005 untouched; sealed gate instances untouched; red-team
  adjudication queue untouched; no values named; no registry change
  proposed.
