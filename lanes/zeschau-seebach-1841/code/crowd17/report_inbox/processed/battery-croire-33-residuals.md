# Battery report: croire-33-residuals (dispose the two 33 orphans via 84/12 re-reads)

Worker: 8bdbcb8b-5f3d-49e7-af76-2df9d1cd7008. Date: 2026-10-09.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005, sealed gates, red-team queue untouched.
Lock: `code/crowd17/next-token/locks/croire-33-residuals.lock` created
2026-10-09T03:26:40Z, no prior lock existed; deleted on completion.

## Bar (verbatim, pre-registered, from battery-queue.json)

"resolve iff both windows parse under standing values via 84/12 re-reads; else
fence to the neighbor value"

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. @1502 ("84-33", row a7_11) parses under standing values via an 84 re-read.
2. @1642 ("12-33", row a8_04) parses under standing values via a 12 re-read.
3. If either clause fails, the failing window is fenced to the neighbor value
   (84 at @1502, 12 at @1642) with stated cause.

Standing values used: 84="on" (A15 grant, re-derived as UNCONDITIONED by
battery-collision-62-84, verdict kill 2026-10-08); 12="n" letter tier
(promoted); 94="ne", 30="pas" (battery-promoted); 00="pour" (A9);
86 INF-class (A9); 87="ce", 47="ce" (allophone tier), 46="que", 96="par",
64="qui", 79="tout" (promoted); 29="er", 82="m", 40="e", 11="la", 70="pre",
34="i" (banked GT); 59="est" provisional; 67 et/veut positional rule
(§7 sole polyvalence). 33 set: {dire, [X]er}, both infinitives,
both consonant-initial (inherited from erstem-33-id / orphan-1502;
"croire" rival likewise consonant-initial 'c').

## Method

Re-parsed the repaired stream (1,847 pairs / 96 types confirmed). Re-derived
both windows, the full 33 census (n=25), and the full 12 census (n=23).
Tested every 84/12 re-read available under standing values (letter roles,
elision, word-boundary shifts, clause boundaries, syllabic compositions).
Coordinated with (not duplicated) battery-orphan-1502 (verdict promote,
2026-10-08), which decided @1501-1507; its five parse attempts were
independently verified in structure here. Did NOT re-litigate 33's value.

## Window-level evidence (@-offsets are repaired-stream pair indices)

Premise check (claim's "ungrammatical under both croire and dire"):
- @1502: "84 33" = "on" + infinitive. "on" requires a finite verb in French
  of every period; "on dire", "on croire", "on [X]er" are all ungrammatical.
- @1642: "12 33" = "n" + infinitive. "n dire", "n croire", "n [X]er" are all
  ungrammatical; "n'" elision requires a vowel-initial follower, but every
  33-set member is consonant-initial. Premise HOLDS.

Clause 1 — @1502 (row a7_11): `...41 74 | 84 33 | 42 33 00 86 56...`
(@1501=84, @1502=33, @1503=42, @1504=33, @1505=00, @1506=86).
84 re-reads tested:
(a) 84 as not-"on": BLOCKED — A15 grant stands, re-derived UNCONDITIONED by
    collision-62-84 (kill, 2026-10-08); battery may not overturn it.
(b) 84 word-final "on" of a larger "74-84" word: 74's value is open
    (unverifiable), and 33="dire" would still begin a new word needing a
    governor — "dire pour [86]" needs "pour", which sits AFTER 33, not before.
    FAIL at battery grade.
(c) Clause boundary after 84: "on" cannot end a clause. FAIL.
(d) 33 non-verbal: no determiner present; "on" still needs a finite verb.
    FAIL.
No 84 re-read parses. Clause 1 FAILS. (Confirms orphan-1502's verdict.)

Clause 2 — @1642 (row a8_04): `...35 56 | 12 33 | 98 60...`
(@1641=12, @1642=33, @1643=98). 12='n' letter (promoted); 12 census n=23
re-derived (followers: 48 x5 "ne", 94 x3, 16 x3, 06 x2, 33 x1 — this window
only). 12 re-reads tested:
(a) 12 word-initial 'n' + 33: "ndire"/"ncroire"/"n[X]er" — no French word.
    FAIL.
(b) 12 as elided "n'": 33 consonant-initial under every set member — FAIL.
(c) 12 word-final 'n' of "56-12": 56's value open (unverifiable); "33 98" =
    "dire vient" ungrammatical regardless — "vient" needs a subject, "dire"
    cannot supply one. FAIL.
(d) 12 standalone 'n': not a French word. FAIL.
(e) Clause boundary "56 12 | 33 98": 'n' cannot end a clause; "dire vient"
    ungrammatical. FAIL.
(f) 12-33-98 as one unit: no French word; 98='vient' battery-promoted as a
    word. FAIL.
(g) 12 as the particle "ne" ("ne dire" IS grammatical): UNAVAILABLE at
    battery level — 12='n' is letter-tier promoted; a second "ne" alongside
    94 hits the {48,94} homophone-set kill and the §7 sole-polyvalence rule.
    Red-team act only. Recorded as residual observation, not a finding.
No 12 re-read parses under standing values. Clause 2 FAILS.

Clause 3 — fencing (bar's else-arm):
- @1502 FENCED TO 84 with stated cause: 84="on" (granted, unconditioned)
  forces a finite-verb frame that no 33-set member (infinitives only) can
  satisfy. The strain is 84-driven, not 33-driven. (Standing disposition from
  orphan-1502, confirmed here.)
- @1642 FENCED TO 12 with stated cause: 12='n' (letter, promoted) forces a
  consonant contact that no 33-set member can satisfy; no 12 re-read is
  available under standing values (the "ne"-particle reading needs red-team
  authority per (g)). The strain is 12-driven, not 33-driven.

33 census guard: 33 n=25 re-derived; predecessors 00 x8, 67 x6, 47 x2,
15 x2, 52/37/82/84/42/12/85 x1. The only 84-33 and 12-33 contacts on the
stream are these two windows. Orphan count stands at 2/25 = 8%.

## Per-clause pass/fail

1. @1502 parses via 84 re-read: FAIL — A15 blocks the only viable re-read.
2. @1642 parses via 12 re-read: FAIL — no standing-value re-read parses
   (exhaustive a–g above).
3. Fence failing windows to neighbors: PASS — @1502 fenced to 84, @1642
   fenced to 12, both with stated cause.

## Adverses disposition

"fenced to 84 (A15-C2 collision queued as collision-62-84) / 12 rather than
33" — ANSWERED on both halves. The parenthetical is now RESOLVED:
collision-62-84 returned KILL (2026-10-08), confirming 84="on" UNCONDITIONED,
so the @1502 fence to 84 rests on firmer ground than when this target was
queued. The @1642 fence to 12 is established by this battery (clause 2/3).
In both windows the strain is in the NEIGHBOR, not in 33: 33 is exonerated
under the dire hypothesis, the croire hypothesis, and the [X]er stem face.

## Standing-verdict check

No contradiction with any standing verdict: A15 (84="on") respected and
reinforced; 12="n" letter promotion respected; §7 untouched (no new
polyvalence declared — the "ne"-particle reading of 12 was NOT taken);
A10 33+29 HOLD untouched; orphan-1502's verdict confirmed, not altered.
Nothing to escalate.

## Verdict: promote (guard/dispositional success, NOT a value promotion)

The bar's else-arm carried: neither window parses via neighbor re-reads, so
both are fenced to their neighbors with stated cause (@1502 → 84, @1642 →
12). The claim's essential content holds — the ungrammaticality of both
windows under croire AND dire is located in the neighbors (84/12), not in
33. The two 33 orphans are disposed; the 33 set's 8% orphan rate is intact;
no third orphan exists. 33 needs no defense against these windows under any
of its candidate values.

Residual note for the red team (not a finding): reading 12 as the particle
"ne" at @1642 ("ne dire") would parse cleanly but requires 12="ne", a
second "ne" alongside 94 — barred at battery level by the {48,94}
homophone-set kill and §7.
