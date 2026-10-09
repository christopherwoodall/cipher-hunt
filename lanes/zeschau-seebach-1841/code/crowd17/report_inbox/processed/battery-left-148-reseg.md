# Battery `left-148-reseg` — verdict: KILL

## Bar (verbatim, pre-registered)

"a complete parse with zero new assumptions, or fence W1 permanently."

## Numbered clauses

- C1: some re-segmentation of '67 64 77 84 29' @143–147 yields a complete-unit parse under standing values with zero new assumptions → claim survives.
- C2: no such re-segmentation exists → fence W1 permanently (re-open is red-team venue only).

## Method

Re-derived the repaired stream in-session: 1,847 pairs / 96 types, asserts held
(pair count, type count). `canonical.py` never used. Locus byte-confirmed:

- 0-based @143–147 = `67 64 77 84 29`, row a1_04.
- Wider window @138–152 = `65 13 66 14 74 | 67 64 77 84 29 | 87 64 | 96 47 46`
  i.e. `…[65] [13] [66] [14] [74] et qui l'on er ce qui par ce que…`
- Standing values from the registry (2026-10-09, post-R19): 67=et/veut
  (positional rule; follower 64='qui' not infinitive-shaped → 67='et'),
  64='qui' (prom), 77='le' (prov), 84='on' (prom, A15 conditions), 29='er'
  (gt, letter tier), 65=[noun,cls] (R19). 13, 66, 14, 74 unvalued at registry
  level (14='en' is a battery-grade promote only — noted as battery premise,
  not banked).

## Findings

Nine re-segmentation route families tested, all dead under standing values
with zero new assumptions:

1. **Relative-clause 'qui' with finite predicate.** Requires a finite verb
   anywhere in @143–152. None exists under standing values: 74 unvalued
   (naming it finite is a new assumption; barred). DEAD.
2. **Bare/exclamatory infinitive.** Requires a French infinitive word. 29='er'
   is letter-tier verb-ending, not a word; bare "er" is not French. "l'on" +
   bare infinitive is ungrammatical in 1841 French (parent's finding, adopted).
   DEAD.
3. **Letter-tier fusion producing a word.** 77+29 → "leer"/"ler": no word.
   84+29 → "oner": no word. 29+87('ce') → "erce": no word. 64='qui' is a
   promoted free word — fusion with it is barred. Leftward 74+29 fusion would
   need a stem value invented (§3 bars invention). DEAD.
4. **Interrogative 'qui'.** "et qui l'on er ?" is still verb-less;
   interrogative mood does not license a missing verb. DEAD.
5. **67='veut' modal reading.** Positional rule: 67="veut" iff follower
   infinitive-shaped; 64='qui' is not → 67='et' forced. DEAD.
6. **Extended-left whole-clause parse** ("65 13 66 14 74 et qui l'on er").
   The left fragment has no finite verb either (13/66/74 unvalued), so even a
   licensed NP "65 13" leaves the clause "et qui l'on er" verb-less. Extending
   the window supplies no predicate. DEAD.
7. **Rightward predicate licensing** (@148–152 "ce qui par ce que" governing
   "qui"). Killed at kill grade by `ce-qui-148-par-rival` (relative 'qui'
   with no finite verb under standing values; "par" is a preposition). DEAD.
8. **'er' as imperative.** French imperatives need a stem; bare "er" is not a
   French word. DEAD.
9. **77='le' article pivot** ("et qui l' on er"). Changes nothing about the
   verb-less clause. DEAD.

The route space is exhausted: any complete-unit parse at this window needs a
finite verb (absent), a word-level infinitive (absent), a licensed letter
fusion (none), or a rightward predicate (killed). Under standing values with
zero new assumptions, W1's left cannot close.

## Verdict: KILL

C1 fails at kill grade — the window forces false any complete-unit parse under
standing values. C2 fires: **W1 fenced permanently at battery grade.** Re-open
is red-team venue only (naming 74/66, a red-team act on 64, or a 29-stem
ruling). Per §4, kills regenerate no follow-ups.

No standing/red-team verdict contradicted or downgraded (R19-191/R24,
R19-167, R18-008, `ce-qui-left-closure` NULL, `ce-qui-148-par-rival` KILL all
adopted as premises); §7 intact; canonical-stream caveat stands (row a1_04
offsets unvalidated).

## Bookkeeping

- Queue: `left-148-reseg` → `status: verdict`, `result: kill`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON
  re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone). R5005, sealed
  gates, red-team adjudication queue untouched.
