# Battery report: reseg-3006-w2

Target: `reseg-3006-w2`. Claim: re-segment W2 @1251
('00 67 46 26 30 06 65') without the 'passent' word-reading of 30-06.
Date: 2026-10-09. Stream: repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py`; 1,847 pairs re-verified).
Never used `canonical.py`. R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, pre-registered)

"one grammatical full-row parse (test 'que [26-verb] pas | [06...]' arms
and word-internal '[26]pas' arm) or fence with stated cause; must also
resolve the fenced '00 67 46' ('pour et/veut que') left knot"

Numbered clauses (fixed from the bar text before testing, not modified
after; "full-row" = the 7-group W2 window '00 67 46 26 30 06 65'):

1. C1 — Arm A1: "que [26-verb] pas" parses as a grammatical negative
   finite clause with word boundary 30|06 (06 opens the next word
   "ent[65]..."). PASS iff "pas" is licensed (by "ne", or by a licit
   ne-less "pas" template attested in 1841 French or in lane precedent).
2. C2 — Arm A2: "que [26-verb] pas" parses with "pas" as non-negation
   (noun "pas", "pas de", "pas un", "pas"+adjective/adverb, or other
   licit ne-less template), boundary 30|06. PASS iff one such template
   fits "pas ent[65]" on the bytes.
3. C3 — Arm B: word-internal "[26]pas": 26+30 (or 26+30+06) form one
   French word W such that "que W ..." parses grammatically. PASS iff a
   named word-shape (noun / finite verb / 3pl verb) yields a grammatical
   "que"-clause on the bytes.
4. C4 — Left knot "00 67 46" resolves: PASS iff "pour et/veut que" gets
   one grammatical parse under standing values (67's positional value +
   licit "et que"/"veut que" syntax), or a stated word-internal rescue.

A full-row parse needs C4 plus one of C1–C3. The bar's second disjunct
(fence with stated cause) is the honest outcome if all four fail.

## Method

Byte census on the repaired stream only. Verified: W2 bytes; "ne"
(94/12) absence in the licensing span; "67 46", "00 67 46", "46 X 30"
uniqueness counts; nearest upstream "que" (46) for the "et que"
coordination test; 26's verb-class legs re-derived ("qui/ne/on [26]").
Standing values used: 46='que' (banked), 00='pour' (A9, class-level),
30='pas' (promote-conditional), 06='ent' (promote), 65=noun-class
(promoted 2026-10-08), 67='et'/'veut' sole polyvalence with positional
resolution (67="veut" iff follower infinitive-shaped; §7), 26 verb-class
per the listed adverse. No new values declared (barred at battery level).

## Window-level evidence (@-offsets, 0-based)

W2 bytes (verified): @1246=16, @1247=00, @1248=67, @1249=46, @1250=26,
@1251=30, @1252=06, @1253=65, @1254=46, @1255=01, @1256=61, @1257=31,
@1258=29. Row a7_01 ends "...87 11 00 33 16 00" ("cela pour [33] [16]
pour"); row a7_02 = "67 46 26 30 06 65 46 01 61 31 29 69 88 01 09 11 50
46 69 88 24 30 20 64 47 76 87 76".

- "ne"-absence: zero 94/12 tokens anywhere in row a7_01 (@1219–1247)
  and zero in row a7_02 before @1251 (@1248–1250). No "ne" can license
  "pas" @1251 in-clause ("ne" must be immediately preverbal; the only
  tokens between any candidate "ne" and "pas" are "pour et que [26]").
- "00 67 46" is a hapax trigram (only @1247). "67 46" occurs exactly
  twice: @471 ("...80 06 67 46 84 24..." = "et/veut qu'on [24-verb]" —
  "que" followed by 84='on', a SUBJECT, then the verb) and @1248 (W2,
  "que" followed directly by verb-class 26, no subject). The @471
  template shows "67 46" parses only with a subject between "que" and
  the verb — absent at W2.
- "46 X 30" occurs exactly once stream-wide: @1249 ("46 26 30").
  "que [26] pas" is a hapax — no lane template exists for it.
- "et que" coordination test: nearest upstream 46 is @1191, 57 tokens
  before @1248 ("...84 59 46 07 24 82..." = "que [07] [24-verb]"). A
  57-token coordination span with no parallel structure is implausible.
- 26's verb legs re-derived: "64 26" @530 ("59 37 64 26 32") and @1768
  ("24 87 64 26 37") = "qui [26]"; "94 26" @842 ("20 62 94 26 12") =
  "ne [26]"; "84 26" @154 ("46 66 84 26 35") = "on [26]". 26 is
  finite-verb class; @1249=46 directly abuts @1250=26 (no subject slot).
- 67's positional value at W2: follower @1249=46='que' is not
  infinitive-shaped, so 67='et' (not 'veut'). "pour veut que" would
  additionally put a finite verb after "pour" — ungrammatical per the
  A9 leg-(1) downgrade rationale.

## Per-clause pass/fail

- **C1 — FAIL.** "pas" @1251 has no licit "ne": zero 94/12 in the
  licensing span (verified above). Ne-less "pas" after a finite verb is
  ungrammatical in 1841 French, and the lane holds no ne-drop
  precedent (the pas-30 battery's ne-less windows parse via other
  mechanisms — "pas de"-class, "pas par", clause boundaries — none of
  which fit here). "que [26-verb] pas" without "ne" does not parse.
- **C2 — FAIL.** No licit non-negation template fits "pas ent[65]":
  "pas de" needs "de" (06='ent', no "de"); "pas un" needs an article
  (absent); "pas"+adjective/adverb is blocked because 65 is
  noun-class (promoted) and "ent" intervenes; bare noun "pas" ("step")
  as direct object needs a determiner (absent); elliptical/fragment
  readings ("Pourquoi pas?", "non pas") have no host construction.
- **C3 — FAIL**, all sub-arms:
  - B1 (26+30 = one noun-word, "trépas"-shaped): "que [W-noun]" leaves
    "que" unlicensed — relative-"que" needs subject+verb after
    ("pas"/"ent [65-noun]" supply none); "ne...que" needs "ne"
    (absent).
  - B2 (26+30 = one verb-word, "[stem]passe"-shaped subjunctive):
    "que [W-verb]" needs a subject; @1249=46 directly abuts the word —
    French does not pro-drop.
  - B3 (26+30+06 = one 3pl verb, "[stem]passent"): needs a 3pl
    subject — absent; this is the already-killed 'passent' reading
    with a longer stem.
- **C4 — FAIL.** "pour et que": "et que" coordination needs a parallel
  "que"-clause (nearest @1191, 57 tokens back — implausible) AND a
  subject after "que" (absent per the @471 template contrast). "pour
  veut que" is ungrammatical (finite "veut" after "pour"). Word-internal
  rescues fail: no French word ends "...pour"+"et" before "que", and no
  "pour [X-et-Y] que" template exists. The knot stays fenced — it was
  already fenced as A3 of the pasent battery and as the A9-noted
  "@1247 'pour et/veut que' residual"; this battery confirms the fence,
  it does not resolve it.

## Adverses (listed on the target — answered, not ignored)

- "26 is finite-verb class per pasent-subject-26-56 ('qui/ne/on [26]'
  legs)" — ANSWERED: used as the basis of arms A1/A2 ("que [26-verb]");
  legs re-derived byte-exact above (@530/@1768/@842/@154).
- "'passent' word-reading dead grammatically at all four windows" —
  ANSWERED: respected throughout; sub-arm B3 explicitly re-tests the
  3pl shape and re-confirms the kill (subject absent). Not re-litigated.

## Verdict

**NULL** — no grammatical full-row parse of '00 67 46 26 30 06 65' is
statable under standing values; the window is fenced as a genuine
residual with stated cause. Blockers, in order: (i) subjectless
"que [26-verb]" (@1249=46 directly abuts verb-class @1250=26; the @471
"67 46 84" template shows the subject slot is mandatory); (ii)
unlicensed "pas" (zero 94/12 in rows a7_01–a7_02 before @1251; no
fitting ne-less template); (iii) the "pour et que" left knot
(67='et' forced positionally; coordination implausible at 57 tokens;
"veut" ungrammatical after "pour"). What survives: the letter strings
"pas"+"ent" (unfused — no boundary statable), the 'passent' kill, and
all standing verdicts (no contradiction with 30='pas',
06='ent', 65=noun, 00='pour', §7, or the pasent-subject-26-56 kill).

## Follow-ups proposed (null regenerates work)

1. `w2-pas-nelicense` (P2) — audit the lane's ne-less "pas" windows
   (@1269 "88 24 30 20", @1729 "88 24 30 15", @1222 "24 48 30 09",
   @742 "20 30 67"): the pas-30 battery marked them "Parses." without
   stating the mechanism. Bar: name ONE grammatical mechanism covering
   >=2 of them (e.g. word-internal "[verb]pas", "pas"-noun,
   clause-boundary) or confirm ne-drop as lane precedent. If
   word-internal "[X]pas" wins, re-test W2's "[26]pas" (C3/B1) under it.
2. `w2-16-class` (P3) — 16's class/value (n=28, top unknown on m-beat):
   "16 00 [INF]" x2 (@659→86, @844→33) suggests a "[16] pour [inf]"
   purpose frame that W2's "[16] pour et que" breaks. Bar: assign 16's
   class with >=3 frame-legs; then test whether "cela pour [33] [16]"
   closes the left edge so "00 67 46" can be fenced as clause-initial.
3. `w2-knot-etque` (P3) — "et que" @1248 coordination: run a
   sentence-boundary analysis over a7_00–a7_02 to test coordination
   with the @1191 "46"-clause ("...84 59 46 07 24 82 16 96..."). Bar:
   demonstrate the parallel "que"-clause with a complete parse, or
   fence "00 67 46" as a permanent A9 residual with the 57-token gap
   as the stated cause.

## Bookkeeping

- Report: this file.
- battery-queue.json: `reseg-3006-w2` → status `verdict`, result
  `null`, date 2026-10-09 (temp-file + rename, own entry only).
- Lock `locks/reseg-3006-w2.lock`: created on start, deleted on
  completion. No pre-existing lock was present.
