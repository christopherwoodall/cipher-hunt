# Battery report — en24-311-killpack — VERDICT: KILL

Worker: subagent session 44b0be31 (seebach battery).
Date: 2026-10-09. Target: `en24-311-killpack` (priority 3).
Lock: `code/crowd17/next-token/locks/en24-311-killpack.lock` created
2026-10-09T10:16:26Z, no prior lockfile existed.

## Claim

"kill-grade pack for the residual 24='en' arm at @311: 'on en
[37-predicative]' with no verb in the on-clause"

## Bar (verbatim)

"produce a licensed parse of verb-less 'on en [37-predicative]' or fence
the en-arm at @311 kill grade; reckon with R17-009's standing finite-verb
frame at the @473 twin"

## Bar restated as numbered clauses (pre-registered before testing)

- **c1:** Produce a licensed parse of the verb-less frame "on en
  [37-predicative]" at @311 (24='en'), with every component licensed
  under standing granted values (1841 French). Only the two 24='en'
  sub-arms are in scope: pronominal 'en' and preposition 'en'.
- **c2:** If c1 fails (no licensed parse producible), fence the 24='en'
  arm at @311 at KILL grade: the window itself forces the arm false.
- **c3:** Reckon with R17-009's standing finite-verb frame at the
  byte-identical @473 twin: the @311 fence must be consistent with
  R17-009, never a downgrade of it.

## Method

1. Read the bar before seeing data (copied above verbatim from
   `code/crowd17/next-token/battery-queue.json`, target
   `en24-311-killpack`).
2. Parsed the repaired stream exactly like
   `code/side-keyhunt/repair_parse.py`: row offsets from
   `code/side-keyhunt/repaired_offsets.json`, bytes from
   `data/upstream-ct_R5005.txt`, 1,847 pairs. Never `canonical.py`.
   Never touched R5005.
3. Read the controlling standing verdict: R17-009 in
   `code/crowd17/report_inbox/processed/next-token-redteam-r17.md`.
4. Read the parent report: `battery-tense-24-307.md` (NULL, 2026-10-09).

## Window-level evidence (bytes, repaired stream)

@310–@317 (row a2_04): `84 24 37 78 45 64 59 32`
@473–@480 (row a2_10, byte-identical twin): `84 24 37 78 74 45 93 00`

- @310 = 84 ("on", granted A15 — subject pronoun).
- @311 = 24, the target. Follower @312 = 37 (predicative frame, A1
  granted). @313 = 78 (verb-stem class).
- The byte-identical `84 24 37 78` contact occurs exactly twice
  stream-wide: @310 and @473. (A third `84 24` bigram at @1485 has
  follower 87, a different frame — fenced, not evidence.)
- 24 census (re-derived): n=52 stream-wide.

Standing state on 24 (re-derived, not re-litigated):

- **R17-009 (controlling, class-level PROMOTE):** "24 = finite verb,
  modal-shaped — GRANT PROMOTE (class level). Six subordinate finite
  slots ('que 24' x3 @547/@955/@1693; 'qu'on 24' x2 @311/@474;
  'que l'on 24' x1 @1486), infinitive-taking complements (24->85 x5,
  24->89 x3, 24->80 x2), postverbal 'pas' x3. The preposition arm is
  KILLED at kill grade: eight windows ungrammatical as preposition
  ('que'/'on'/'ne' + preposition)."
- R17-009's @311/@474 (pre-repair offset of the 24 slot = my @311/@474
  post-repair) explicitly names BOTH twin windows as 'qu'on 24'
  finite-verb slots.
- 24='en' never granted anywhere (tense-24-307 evidence 3; R18 §7
  review: "A3 granted the @952 frame, not a 24 value").

## Per-clause results

- **c1 — FAILS (no licensed parse exists).** Both sub-arms of 24='en'
  are ungrammatical at @311 under standing values:
  1. *Pronominal 'en':* a pronominal clitic is the complement of a
     verb. Under 24='en', the on-clause has no verb at all: @310 =
     subject pronoun 'on' (A15), @311 = clitic 'en', @312 =
     predicative adjective (A1). "On en [adjectif]" with no finite
     verb is ungrammatical French. Copular frames with 'en' ("il en
     est capable") still require the verb ("est"); no verb exists here
     and none can be elided into the frame (French licenses no
     zero-verb finite clause). Ellipsis does not delete a clause's
     only verb.
  2. *Preposition 'en':* "on en [37-predicative]" reads 'en' + bare
     adjective with no noun for the preposition to govern — A1 grants
     37 as predicative adjective, not a noun. @313 = 78 is
     verb-stem-class, not a governable noun, so "en [78]" cannot
     rescue the complement. The fixed adverbial "en + adj" escape
     ("voir en grand") also fails: it requires a governing verb.
     Separately and redundantly, R17-009 already KILLED 24's
     preposition arm at kill grade across eight windows, including the
     'on' + preposition shape.
  No other licensed zero-verb finite-clause construction exists in
  1841 French. c1 fails exhaustively.
- **c2 — PASSES (kill grade).** The @311 window itself forces the
  en-arm false: 84='on' is a granted subject pronoun; a subject
  pronoun in a finite clause must be followed by a verb; 24 is the
  only verb-slot candidate (its follower 37 is predicative, A1, and
  cannot head the clause). Under 24='en' the clause has no verb, so
  the frame is ungrammatical — the window forces the claim false at
  kill grade (§4). The 24='en' arm at @311 is fenced KILLED.
- **c3 — PASSES (consistent with R17-009).** The twin window is
  byte-identical (`84 24 37 78` at @310 and @473), so the fence applies
  to the frame, not one window. R17-009 explicitly grants BOTH
  windows (@311/@474 = my @311/@474) as 'qu'on 24' finite-verb
  slots and kills the preposition arm at kill grade. The @311 kill of
  the en-arm is exactly what R17-009's grant entails; no standing
  verdict is downgraded or contradicted. The R17-009 finite-verb
  frame at @473 is not re-tested here (class-level PROMOTE, value
  open — untouched).

Adverses: none listed (adverses: null). Nothing to answer.

## Verdict

**KILL** — the residual 24='en' arm at @311 is fenced at kill grade.
No licensed parse of verb-less "on en [37-predicative]" exists under
standing values (c1 fails on both sub-arms); the @311 window itself
forces the arm false (c2); the fence is consistent with and entailed by
the controlling R17-009 finite-verb grant at the byte-identical @473
twin (c3).

Scope note: the kill is scoped to @311 (and by frame identity to the
@473 twin). 24's 'en' arm at OTHER windows (e.g. the @952 frame-family
conditioned leads) is out of scope and untouched by this verdict. R18's
"24='faire' LEAD, value open" is likewise untouched — nothing here
names 24's value.

No null verdict, so no follow-ups are required (§4: follow-ups are
null-mandated). No escalation: the result agrees with the controlling
red-team verdict.
