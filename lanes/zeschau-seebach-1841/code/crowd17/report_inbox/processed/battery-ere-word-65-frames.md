# Battery report: ere-word-65-frames

- Target id: `ere-word-65-frames`
- Claim: identify the '-ère'-final word(s) in the three '29 40 65' windows via syllable inventory; decides the "65 opens new clause as subject" parse.
- Date: 2026-10-09
- Worker: battery worker (subagent e57d0117-adc9-46af-ae07-66d31b6717b1)
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  1,847 pairs / 96 types re-verified in-session). `canonical.py` never used.
  R5005, sealed gate instances, and the red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/ere-word-65-frames.lock` (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"name the word(s) iff left-context syllables compose a French word ending
'-ère' with the post-40 boundary (enne-word-64) holding at all three windows;
else fence the window(s) with stated cause"

Numbered pass/fail clauses (restated before testing, not modified after):

1. C1: at W1 (@291, 0-based), the left-context syllables under standing values
   compose a French word ending '-ère' that ends at 40, with the post-40
   boundary (65 begins a new word) held.
2. C2: same composition test at W2 (@685, 0-based).
3. C3: same composition test at W3 (@1710, 0-based).
4. C4: the adverse is answered — the syllabic-'qui' reading (64 absorbed as
   letters inside the '-ère' word) is tested against the granted word
   64='qui'; 06/09/92's open values are not invented; the post-40 boundary
   is not disturbed.

Naming fires iff C1–C3 all pass. Any failure executes the else-branch:
fence the window(s) with stated cause (null, §4).

## Method

1. Re-derived the repaired parse in-session (1,847 pairs, 96 types). Byte-exact
   census of the '29 40 65' trigram: exactly 3 windows, 0-based @291, @685,
   @1710 (1-based @292, @686, @1711). No other '29 40 65' in the stream.
2. Pulled ±8 context at each window; listed only letter/syllable values that
   are banked, granted, or battery-held (inventing open-group letters is
   barred at battery grade).
3. French lexicon check against the lane's side-period corpus
   (`code/side-period/corpus/`, ~32 MB, 1841-register French prose/drama/
   correspondence) plus standard 1841 French morphology. Corpus hits were
   hand-classified (genuine vs OCR artifact).
4. Adopted as premises (not re-litigated): 29='er', 40='e' (banked GT);
   64='qui' as a granted word (§7); 12='n', 94='ne' (battery-promoted,
   pending ratification); 06 syllabic 'ent' (battery-held: word-initial
   'ent' unless left neighbor is a verb stem; rightward ent+follower killed);
   the post-40 boundary — 65 begins a new word (enne-word-64; re-confirmed
   byte-identical at these three windows by noun-65-value Frame A);
   the §7 kill of the '-ère' *value* for 09/92; rel-09-290's battery-grade
   kill of the word-internal "quière" rival (via @1713, where '29 40 65'
   occurs with no preceding 64).

## Window-level evidence

Standing letter strings (banked/granted/held values only; open groups
contribute no letters):

- W1 @291 (row a2_03): `48 52 89 28 00 97 09 64 29 40 65 16 01 11 78 40`
  Left edge of the candidate word: `09 64 29 40`. Licensable string:
  [09:?] + 'qui' + 'er' + 'e'. Fixed suffix "quiere". 09 is nominal
  (rel-09-290) with value open.
- W2 @685 (row a5_00): `77 45 23 09 07 00 92 64 29 40 65 94 29 60 03 39`
  Left edge: `92 64 29 40`. Licensable string: [92:?] + 'qui' + 'er' + 'e'.
  Fixed suffix "quiere". 92's class is open (verb-shaped); its '-ère' value
  is kill-closed (§7).
- W3 @1710 (row a8_06): `30 20 62 94 88 26 12 06 29 40 65 94 44 59 30 64`
  Left edge: `12 06 29 40`. Licensable string: 'n' + 'ent' + 'er' + 'e'
  = "nentere" (or "entere" without 12). 26 further left is value-open
  (no letters licensable).

### Lexicon check

- "quiere"/"quière" as a whole word: the single bare corpus hit
  (nesselrode-v9 "bouti- / quière") is a line-break OCR artifact of
  "boutiquière" (feminine of "boutiquier"). No standalone French word
  "quière" exists.
- French words *containing* final "quière": "acquière", "requière"
  (3sg present subjunctive of acquérir/requérir), "boutiquière".
  All need stem letters ("ac", "re", "bouti") from 09 (W1) or 92 (W2) —
  both value-open, so spelling them is invention at battery grade. Worse,
  all three absorb 64 as letters, which contradicts the granted *word*
  64='qui' (see C4).
- "nentere"/"entere": corpus hits ("présenteren", "enteren", German-file
  OCR garbage, "tenterez") are all OCR/segmentation noise — "présenteren"
  = "présenter en" merged; none is a French word. The "ntère" hits
  ("affrontèrent", "chantèrent", …) are 3pl past historics with letter
  order n-t-è-r-e-n-t — incompatible with "n-e-n-t-e-r-e", and none is
  '-ère'-final (all end -ent).
- No French word ends "entère"/"ntère" as a final (past-historic -èrent
  always carries the -nt; "entrer"/"tenter" end -er). The maximal
  licensable W3 strings admit no French word.
- "ère" (era) as the word = [29][40] alone: letter-compatible at W1/W2
  ("qui ère") and W3 ("ent ère"), but ungrammatical at all three —
  "qui" cannot be followed by a bare noun without a verb, and "ent" is
  not a French word (rightward ent+follower killed; standalone 'ent'
  is a syllable, not a word). Composition without grammar is not a name.

### The syllabic-'qui' arm (adverse)

Tested directly: absorbing 64 as the letters "qui" inside an '-ère' word
("acquière"/"requière"/"boutiquière"-family) contradicts the standing
grant of 64='qui' *as a word* (§7 promoted/granted list; used as a word
by bound-65-64-qui and rel-09-290). The grant's scope is not window-
limited in the standing record, so the syllabic-'qui' reading fails at
battery grade. Whether the grant is global or window-scoped is red-team
venue — escalated, not adopted (follow-up F1).

## Per-clause pass/fail

1. C1 (W1 @291): FAIL. No French '-ère'-final word is licensable from
   [09:?]+'qui'+'er'+'e' without inventing 09's value and without
   contradicting granted 64='qui'. The "quière"-internal rival is
   independently kill-closed by rel-09-290.
2. C2 (W2 @685): FAIL. Same cause with 92 in place of 09; 92's '-ère'
   value is additionally kill-closed (§7).
3. C3 (W3 @1710): FAIL. "nentere"/"entere" admits no French word
   (corpus attestations are OCR noise; "ntèrent" verbs are letter-
   incompatible and not '-ère'-final).
4. C4 (adverse): ANSWERED. The syllabic-'qui' reading was tested and
   fails against the granted word 64='qui'; 06/09/92's values were not
   invented; the post-40 boundary (65 begins a new word) was not
   disturbed at any window.

Naming does not fire (C1–C3 all fail). The else-branch executes.

## Verdict: NULL (fence executed per the bar's else-branch)

Each window fenced with stated cause:

- F-W1 (@291): the '-ère' word is unnameable — "quière" is not a French
  word (sole corpus hit is a "boutiquière" OCR artifact); longer
  "quière"-final words need invented 09 letters and contradict granted
  64='qui'.
- F-W2 (@685): same fence with 92; 92's '-ère' value kill-closed.
- F-W3 (@1710): the '-ère' word is unnameable — "nentere"/"entere" is not
  a French word; no licensable extension (26 open, no letters).

Scope: this fences only the '-ère'-word identification. Untouched:
the post-40 boundary (65 begins a new word, battery-held); 65's noun
class (battery-promoted); rel-09-290's "qui [verb 29-40-65]" relative-
clause parse (a rival reading of the same bytes, not adjudicated here
per the adverse); §7 intact. No standing or red-team verdict
contradicted or downgraded.

## Follow-ups proposed (null per §4 — for supervisor queueing)

### F1 id `qui64-scope-redteam` — priority 2
- claim: "The syllabic-'qui' arm re-opens at W1/W2 iff the red team scopes
  64='qui' as a window-level grant rather than a global word grant."
- bars: "re-open iff the red team narrows the 64='qui' grant's scope AND
  09/92 independently name stem letters ('ac'/'re'/'bouti'-family);
  else the fence stands."
- evidence: "W1 @291 '09 64 29 40', W2 @685 '92 64 29 40'; 'acquière'/
  'requière' are the only licensable 'quière'-final French words;
  both contradict the current global-grant reading."
- adverses: "red-team venue; do not re-litigate the grant at battery level."

### F2 id `val-09-92-stem-letters` — priority 3
- claim: "Census 09's 12 windows and 92's 22 windows for any standing
  letter value that could supply an '-ère'-word stem."
- bars: "re-test the W1/W2 '-ère' composition iff 09 or 92 names letters
  compatible with a 'quière'-final word ('ac'/'re'/'bouti' or novel);
  else fence."
- evidence: "09 n=12 (nominal, value open, rel-09-290); 92 n=22 (class
  open, '-ère' value kill-closed); W1/W2 left edges above."
- adverses: "the '-ère' value kill for 09/92 (§7) is not re-litigated —
  this is a stem-letter search, not a value search."

### F3 id `ere-word-w3-reseg` — priority 3
- claim: "Re-segmentation sweep at W3 (@1710): test whether '12 06' can
  compose a French stem whose letters plus 'ere' yield a word."
- bars: "name the word iff '12 06' + '29 40' compose a French '-ère'-
  final word under standing letter values with zero new assumptions;
  else fence W3 permanently at battery level."
- evidence: "@1710 '26 12 06 29 40 65'; licensable 'nentere'/'entere'
  has no French word (this battery); 26 open."
- adverses: "06='ent' battery-held (syllabic); do not disturb the
  post-40 boundary."

## Standing constraints observed

Did not touch R5005, sealed gate instances, or the red-team adjudication
queue. Nothing promoted or killed by this battery (verdict is null).
No invented numbers: every offset verified on the repaired 1,847-pair
stream; every corpus claim hand-checked with cause.
