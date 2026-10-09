# Battery report: en14-three-window

- Target id: `en14-three-window`
- Claim: "14='en' (the only letter-strict 'm''+clitic value) is viable as 14's value."
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`;
  asserts hold: 1,847 pairs, 96 groups). `canonical.py` never used. R5005 not touched.
- Lock: `code/crowd17/next-token/locks/en14-three-window.lock` (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"Test 14='en' at 1-based @623, @896, and @178 ('[69] en [24-verb]', the clitic
reading's best leg per tout-slot-14); keep the 'en' arm iff >=1 window yields
a grammatical local parse under standing values; else kill 14='en' at battery grade."

## Numbered clauses (restated before testing, not modified after)

1. (C1) Test 14='en' at the three windows: W1 (82-14 @623-624, row a4_01:
   `76 82 14 59 37 33`), W2 (82-14 @896-897, row a5_08: `98 82 14 98 83 86`),
   W3 (@178-179, row a1_05: `69 14 24`). NOTE on the offset convention: the
   bar's "@623/@896/@178" match the lane's 0-based convention used by
   clitic-14-82-breakers (its W1 "1-based @623" is byte-identical to the
   window tested here: `29 88 37 [76 82 14 59 37 33] 29 87 78 67 08`).
   All three windows were re-derived byte-exact in-session and match the
   brief's rows and contexts; the offset label does not change what is tested.
2. (C2) Keep the 'en' arm iff >=1 of the three windows yields a grammatical
   local parse under standing values (bar says "local parse", not full-window).
3. (C3) Otherwise (0/3), kill 14='en' at battery grade.
4. (C4) Adverses answered: (a) 14's verb class fenced lane-wide (stem-14-84-retest,
   NULL); (b) 14='le' killed globally at kill grade (le-14-kill-1121, KILL);
   (c) W2 kills are value-independent (conditional on 98's verb class).

## Standing values spent (adopted, not re-litigated)

- 82='m' — banked GT, LETTER (this is load-bearing: 82+14 = "m"+"en",
  letters; "m'en" is the reading with the apostrophe supplied by the
  cipher's elision convention — the cipher writes elision via 82='m').
- 64='qui' — banked GT. 11='la' banked. 29='er' banked. 46='que' banked.
- 69=noun class — battery-promote (noun26-69-pour-dire, PROMOTE 2026-10-09,
  10-11 of 12 windows; 69's value open).
- 24=finite verb, modal-shaped — battery-promote class-level (ne-24-profile,
  PROMOTE; the 24-en-verb-conflict red-team docket is live — W3 is
  load-bearing on 24=finite-modal, stated as a caveat below).
- 76=noun — lead, battery-promoted (adopted from clitic-14-82-breakers,
  which stated it as a standing premise).
- 59='est' — provisional.
- 37/32/42 predicative frames — A1 granted (value open).
- 14's verb class — fenced lane-wide (stem-14-84-retest, NULL).

## Window-level evidence

### W1: `76 82 14 59 37 33` (0-based @622-627, row a4_01)

Under 14='en': "[76-noun] m'en est(59) [37-pred]".
- The local core "[76] m'en est [37]" is literary-grammatical on the
  "il m'en est resté / il m'en est garant" pattern: subject (76 nominal),
  clitic cluster "m'en" (elided "me" via 82='m' + adverbial/pronominal "en"),
  finite "est" (provisional), predicative complement (A1).
- "m'en est": "en" after "être" is licensed ("s'en être aperçu",
  "il m'en est resté"); no clitic-order violation ("me"+"en" before the
  finite verb is canonical).
- Full-window blocker (independent of 14's value, adopted from
  clitic-14-82-breakers): "37 33" = predicative + bare infinitive is
  ungrammatical in the same clause. This blocks the full window but does
  NOT block the local parse the bar requires.
- Grammatical local parse under standing values: YES (conditional on
  provisional 59='est' and 76's noun lead — both stated, not hidden).

### W2: `98 82 14 98 83 86` (0-based @895-900, row a5_08)

Under 14='en': "98-fin m'en 98-fin".
- 98 = finite-verb class, promoted (prof-98, R18 standing; vient-98-name
  battery-promoted). The window has a finite verb on both sides of the
  clitic cluster: "...[V-fin] m'en [V-fin]...".
- "vient m'en" after a finite verb: clitics need a verb to serve; the
  only available verbs are both finite and the second one is stranded —
  "vient m'en vient" is ungrammatical in every register. Reading 98 as
  infinitive-shaped would downgrade prof-98 (closed at battery grade).
- Value-independence (adverse (c)): this failure holds for any 14 value —
  it is forced by 98's class, not by 14. Confirmed as value-independent.
- Grammatical local parse under standing values: NO.

### W3: `69 14 24` (0-based @178-180, row a1_05; fuller: `21 69 14 24 87 64`)

Under 14='en': "[69-noun] en [24-fin/modal]".
- "en" is a clitic pronoun/adverb that sits immediately before its verb:
  "[N] en [V-fin]" = subject + en + finite verb — canonical French
  ("Dieu en est témoin"-shaped; "il en prend"). 69 is noun-class
  (noun26-69-pour-dire PROMOTE), 24 is finite-modal class-level
  (ne-24-profile PROMOTE).
- Letter-strictness: no elision needed; 14="en" stands free before 24.
  No compositional alternative (no "men"-word in French; 82 absent).
- No rival parse under the same values is cleaner: 14='le' is globally
  kill-grade dead; the determiner arm is doubly dead at '82 14'
  (clitic-14-82-breakers); verb-class 14 is fenced lane-wide.
- This is tout-slot-14's best clitic leg, confirmed at battery grade.
- Grammatical local parse under standing values: YES.
- Caveat: load-bearing on 24=finite-modal — the live red-team docket
  `24-en-verb-conflict` (24='en' vs 24=verb) is unresolved; if red team
  resolves 24='en', "en [24-en]" dies and W3's leg collapses. Stated,
  not hidden.

## Per-clause pass/fail

1. (C1) Three windows tested at byte-exact, row-confirmed loci: PASS
   (method clause).
2. (C2) >=1 window yields a grammatical local parse under standing
   values: **PASS** — W3 passes cleanly; W1 passes as a conditional
   local core ("[76] m'en est [37]"). The 'en' arm is KEPT.
3. (C3) Kill arm: does NOT fire (C2 passed).
4. (C4) Adverses answered:
   (a) 14's verb-class fence (stem-14-84-retest NULL) is verb-class-scoped;
       'en' is a clitic, not a verb class — no collision.
   (b) 14='le' kill (le-14-kill-1121) is a distinct value; 'en' unaffected.
   (c) W2's failure confirmed value-independent (forced by 98's promoted
       finite-verb class); it does not block the keep clause, which only
       requires >=1 window.

## Verdict: PROMOTE (finding grade — the 'en' arm is kept at battery grade)

14='en' survives as a live value hypothesis for 14: 2 of 3 windows yield
grammatical local parses under standing values (W3 clean, W1 conditional),
and no window forces 14 ≠ 'en' at kill grade. The clitic-14-82-breakers NULL
fenced the clitic-vs-determiner tie; this battery names the surviving clitic
value 'en' — consistent, no downgrade, no contradiction with any standing or
red-team verdict. §7 intact (no polyvalence declared).

This is battery-grade only: needs red-team ratification before banked use.
Load-bearing dependencies (if any falls, re-open):
- 24=finite-modal (red-team docket `24-en-verb-conflict`) — W3's leg.
- 59='est' provisional — W1's core.
- 69=noun battery-promote, 76=noun lead — subject licensing.
- Canonicality caveat: all three rows (a4_01, a5_08, a1_05) carry unvalidated
  upstream offsets; kills/parses hold on the canonical stream per protocol.

## Follow-ups (optional; none required — this is a promote, not a null)

The supervisor may, at its discretion, queue:
1. `en14-value-tighten` (P3) — test 14='en' against the full 14-window census
   (n=15) for any kill-grade contradiction; fence global 'en' iff any window
   forces 14 ≠ 'en' value-independently.
2. `en14-w3-rerun-24en` (P4) — re-test W3's leg iff the red-team resolves
   `24-en-verb-conflict` as 24='en'.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-en14-three-window.md`
- Queue: `battery-queue.json` — `en14-three-window` `queued`→`verdict`/
  `promote`, date 2026-10-09 (pre-write assert passed; temp-file + rename;
  JSON re-validated; own entry only; no downgrade).
- Lock created at start, deleted on completion. `canonical.py` never used.
  R5005, sealed gates, red-team adjudication queue untouched.
