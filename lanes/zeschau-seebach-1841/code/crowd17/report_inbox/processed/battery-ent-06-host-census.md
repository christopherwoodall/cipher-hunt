# Battery verdict: ent-06-host-census

**Verdict: PROMOTE** — 06's left-attachment bimodality is resolved as a
decision rule, applied window-by-window across all 44 windows and all 28
preceder groups. No standing verdict is contradicted.

## Bar (verbatim, pre-registered)

> CLAIM: resolve 06's left-attachment bimodality across its 28 preceder groups
> BARS: state at which windows 06 is a finite ending vs a syllable; no 'X-06' stem claim can be stated until this is settled
> ADVERSES: coordinate with ent-06 (battery-promoted, pending ratification)

Numbered clauses (frozen before testing):

1. State, for each 06 window on the repaired stream (by @-offset), whether
   06 functions as a finite verb ending or as a syllable (letters "ent"
   that are not an inflection). Fences are allowed only with stated cause
   and a named downstream gate.
2. Answer the adverse: coordinate with ent-06 (06="ent", verb fork,
   battery-promoted pending ratification) — no contradiction, no overwrite,
   no silent re-litigation.

## Method

Read BATTERY-PROTOCOL.md first. Created
`locks/ent-06-host-census.lock` on start (agent id + UTC 2026-10-09T05:09:30Z);
deleted on completion. Re-derived the stream from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(parsed per `code/side-keyhunt/repair_parse.py`): 1,847 pairs, 96 groups,
06 n=44 confirmed. `canonical.py` never touched. R5005, sealed gates, and
the red-team adjudication queue untouched.

All @-offsets below are 1-based pair indices (the stem-62-ent convention:
its 0-based @665/@1536 = 1-based @666/@1537). 0-based equivalents are given
in parentheses where another report cites them.

Preceder census re-derived (28 groups, matches the brief):
42 x5, 82 x4, 30 x4, 14/80/06/62/64/12 x2,
41/37/78/11/94/01/17/48/77/07/84/86/24/81/16/60/68/40/93 x1.

## The decision rule (the bimodality, resolved)

06 = "ent" (single value; ent-06's promotion is kept — function varies,
value does not). Across the determined windows the split is clean:

- **Finite ending** iff the left neighbor is (or composes) a verb stem:
  06 is the 3pl inflection "-ent" on that stem.
- **Syllable** otherwise: word-initial "ent" after a complete word
  (boundary), or word-internal "ent" inside a stem ("ment-", "entreprenne",
  adverbial "-ment").

Every determined window below obeys this rule. No counter-example was
found. The 19 fenced windows are exactly the windows whose left neighbor's
class is still open — the rule cannot fire until those classes resolve.

## Window-level evidence

### FINITE ENDING — 06 = 3pl verb ending (5 solid + 2 conditional)

- @471 (pre=80): "80 06 67". 80 is verb-class (A8, granted). "[80]ent"
  is the finite 3pl. (ent-06 clause 1 leg; right junction "67" fenced
  there, ending stands.)
- @582 (pre=06): "94 82 06 06 50" = "ne mentent [50]". Second 06 is the
  3pl ending on stem "ment-". (ent-06 F1.)
- @1092 (pre=80): "80 06 43". "[80]ent [43]". (ent-06 clause 1 leg; right
  junction conditional on noun-43, ending stands.)
- @1186 (pre=06): "94 82 06 06 59" = "ne mentent est". Second 06 is the
  3pl ending. (ent-06 F2.)
- @1763 (pre=93): "15 93 06 77". verb-93's own battery (C1, promoted
  class-level) reads "[93]ent" as 3pl finite-shaped. Ending.
- @1123 (pre=14): "14 06 11 52 37 43". CONDITIONAL: finite ending iff
  stem-14-id names a verb stem (already queued). The la-frame excludes the
  adverb fork (adverb + "la" is ungrammatical — ent-06), so no other live
  reading exists.
- @1721 (pre=68): "68 06 11 52 37 43". CONDITIONAL: finite ending iff
  stem-68-id names a verb stem (already queued). Same la-frame logic.

### SYLLABLE — 06 = "ent" letters, not an inflection (18 windows)

- @272 (pre=11): "11 06 67" = "la"+"ent"+[67]. Word-initial after banked
  11="la".
- @347 (pre=01): "01 06 70 12 94" = "[01] entreprenne [74]".
  Word-initial "ent" of "entreprenne" (70-12-94="prenne" battery).
- @371 (pre=17): "17 06 21" = "fois"+"ent"+[21]. Word-initial after
  promoted 17="fois".
- @523 (pre=77): "77 06 55" = "le"+"ent"+[55]. Word-initial (77="le"
  provisional).
- @581 (pre=82): "ne mentent", first 06. Stem-internal: "ment-" is the
  lexical stem of mentir; "m" alone is not a stem, so the first "ent"
  cannot be an ending.
- @739 (pre=82): "18 82 06 00" = "[18]ment pour [36]". Syllable on both
  live forks: adverbial "-ment" (18=adjective stem, adv-18-ment promoted
  locus-level) or 3sg "ment" of mentir (stem-internal).
- @790 (pre=84): "84 06 77" = "on"+"ent"+"le". Word-initial after
  promoted 84="on" (a pronoun takes no ending).
- @1081 (pre=64): "64 06 52" = "qui"+"ent"+[52]. Word-initial after
  promoted 64="qui".
- @1097 (pre=81): "81 06 29" = "[81]ent"+[29]. Word-initial: 81 is a
  masculine abstract noun (noun-81, promoted class-level); a noun takes
  no "-ent".
- @1185 (pre=82): "ne mentent", first 06. Stem-internal "ment-" (same
  mechanism as @581).
- @1253 (pre=30): "30 06 65". "pas"+"ent"+[65]. Word-initial under
  standing 30="pas" (wordbound-30-06-importent clause 3: two-word holds).
- @1329 (pre=30): "30 06 62". "pas"+"ent"+[62]. Same.
- @1356 (pre=82): "94 82 06 52" = "ne"+"ment"+[52]. "m"+"ent" cannot be
  stem+3pl ending ("m" is not a stem). Syllable.
- @1389 (pre=16): "16 06 29" = "[16]ent"+[29]. Word-initial — robust to
  the open 16 conflict: both forks (16=infinitive promoted; 16=finite-verb
  lead, escalated) are word-level, and neither is a bare stem, so 06
  cannot be an ending on 16 either way.
- @1476 (pre=60): "60 06 67" = "[60]ent"+[67]. Word-initial: 60 is a
  postposed adjective (adj-60-2160, frame-leg grade; noun-60 killed); an
  adjective takes no "-ent".
- @1563 (pre=30): "30 06 60". "pas"+"ent"+[60]. Same as @1253.
- @1668 (pre=64): "64 06 91" = "qui"+"ent"+[91]. Word-initial after
  64="qui".
- @1735 (pre=30): "30 06 60". "pas"+"ent"+[60]. Same as @1253.

### FENCED with cause (19 windows) — rule cannot fire; left neighbor open

- @7 (pre=41): 41's class open (§7 split candidate; class-41-contact
  null, regenerating).
- @86 (pre=14): genuinely bimodal — finite ending iff 14 is a verb stem,
  else word boundary. Downstream of stem-14-id (queued).
- @185 (pre=37): 37's predicative frame is granted (A1) but the -06
  windows tension it; 06's function is downstream of 37's class.
- @207, @268, @545, @1189, @1816 (pre=42, x5): 42's class open.
  Downstream of stem-42-verb (null, regenerating).
- @216 (pre=78): 78 open (78="ver" is a red-team lead, R16-005).
- @320 (pre=94): no parse under either fork ("ne"+"ent"+"la"); 94's
  syllabic duality yields no French word here either.
- @400 (pre=48): no parse ("e"+"ent"+"la"; the A7-L2 "tout me [48-verb]"
  alternative is convoluted — ent-06).
- @667, @1538 (pre=62, x2): **the crux.** 62's word-shape is open, so
  06's function here is downstream of 62's class. If 62 is verb-stem-final,
  06 is its finite ending; if 62 is a pronoun/word, 06 is a syllable. The
  06 side cannot settle stem-62-ent — this target's bar is met, but the
  62-windows stay fenced pending subj-62-06-1537 and re-prefix-03-665
  (both queued) and 62's class generally. (Offset note: stem-62-ent's
  @665/@1536 are 0-based positions of 62; the 06s sit at 1-based
  @667/@1538, the offsets used in this report's table.)
- @774 (pre=07): no parse under either fork (formula-94-07-06-94).
- @891 (pre=86): 86 open (le-86 null).
- @968 (pre=24): downstream of the 24-en-verb-conflict (red-team venue;
  not a battery question).
- @1121 (pre=12): the finite fork is KILLED — "prenent" would need the
  clerk single-n spelling of "prennent", and that license is dead at kill
  grade (spell-single-consonant null: "prenne" writes the doubled n;
  spell-pasent-test). Residual word unidentified: fenced.
- @1710 (pre=12): no French word ("n"+"ent"+"er"+"e" — "nentere"-shaped);
  wordbound's mechanism leg only. Fenced.
- @1748 (pre=40): bimodal — finite ending iff the left word is a
  vowel-final verb stem ("créent"-shaped), else word-initial syllable
  after an "e"-final word.

Tally: 7 finite (5 solid + 2 conditional) + 18 syllable + 19 fenced = 44. ✓

## Per-clause results

- **Clause 1 — PASS.** All 44 windows are stated: 25 determined at battery
  grade (7 finite incl. 2 conditional on already-queued stem targets,
  18 syllable), 19 fenced with stated cause and a named downstream gate.
  The bimodality resolves to one rule: 06 is a finite ending iff its left
  neighbor is a verb stem; otherwise it is a syllable. No determined
  window violates it.
- **Clause 2 (adverse ent-06) — ANSWERED.** No contradiction: 06="ent"
  (single value) is kept everywhere — function varies, value does not,
  so ent-06's "no polyvalence" stands. The finite-ending determinations
  at @471/@582/@1092/@1186 reuse ent-06's own legs; the @1121 "prenent"
  correction is applied (finite fork killed, not revived); the la-frame
  conditionals route to the already-queued stem-14-id / stem-68-id.

## What this settles for stem-62-ent

The target's purpose clause ("no 'X-06' stem claim can be stated until this
is settled") is answered negatively for the 62-windows: 06's side is
settled as a rule, but the two "62 06" windows (@667/@1538 1-based,
the 06 positions; stem-62-ent's @665/@1536 are the 0-based positions of
the 62s) stay fenced because 62's
class is open. stem-62-ent cannot be rescued from the 06 side; it needs
62's class (subj-62-06-1537, re-prefix-03-665 queued) or the red team.

## Residual gates (for the supervisor; most already queued)

Already queued: stem-14-id (@86/@1123), stem-68-id (@1721),
subj-62-06-1537 + re-prefix-03-665 (@667/@1538), stem-42-verb follow-ups
(42 x5), class-41-contact follow-ups (@7). Red-team venue: 24-en-verb-conflict
(@968).

Proposed new narrow targets:

1. `word-12-06-1121` (P3) — identify the word containing "12-06" at
   @1121 (and @1710) now that the finite "prennent" fork is killed; bar:
   state the word or fence as a hard residual with the failure stated.
2. `class-37-06-185` (P3) — decide 37's class at @185: predicative
   adjective (then 06 is a word-initial syllable) vs verb stem (then 06
   may be its finite ending); bar: 06's function follows 37's class.
3. `stem-40-06-1748` (P3) — test the left word's class at @1748:
   vowel-final verb stem ("créent"-shaped → 06 finite ending) vs
   "e"-final non-verb word (→ 06 syllable); bar: state which fork the
   left context supports.

## Bookkeeping

- Lock `locks/ent-06-host-census.lock` created on start (agent id
  2ff4652f-d16b-40e0-a1f7-3a13a98a604c, UTC 2026-10-09T05:09:30Z); deleted
  on completion.
- `battery-queue.json`: target `ent-06-host-census` queued → verdict /
  promote (own entry only, temp-file + rename; pre-write assert confirmed
  no prior verdict; JSON re-validated post-write).
- R5005, sealed gates, red-team adjudication queue untouched. No standing
  verdict contradicted or downgraded. ent-06's promotion is used, not
  re-litigated.
