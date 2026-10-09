# Battery `re83-gar-test` — verdict: KILL

Target: 83="gar" ("regarder" @906/@1611) across the full 83 census (n=15),
keeping the five 98-conditioned 'de' windows (@228/@898/@931/@1061/@1784) intact.
Date: 2026-10-09. Worker: a51b2e5a-694.
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`), re-derived in-session and asserted
(1,847 pairs / 96 types). Parsed like `code/side-keyhunt/repair_parse.py`.
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
Lock `crowd17/next-token/locks/re83-gar-test.lock` created on start
(2026-10-09T07:53:43Z), deleted on completion. No stale lock encountered.

Numbering note: all @-offsets below label the 83 position (0-based pair index),
matching the de-83-sweep / fence-83-1217 census. The claim's @906/@1611 label the
55 ("re") position immediately before 83@907 / 83@1612 — same windows.

## Bar (verbatim, pre-registered before testing)

"Promote 83="gar" iff all non-'de' windows parse with <=1 unstated assumption, kill iff any window forces otherwise."

## Bar restated as numbered pass/fail clauses (pre-registered before testing)

- **C1 (promote):** Every non-'de' window — @614, @907, @911, @1161, @1171,
  @1217, @1334, @1612, @1829, @1840 — parses under 83="gar" with <=1 unstated
  assumption per window. The five 98-conditioned 'de' windows
  (@228/@898/@931/@1061/@1784) are excluded from the test per the claim's
  conditioned split; they are kept intact, not re-litigated.
- **C2 (kill):** Any single non-'de' window forces otherwise — no grammatical
  French parse exists under 83="gar" with standing values and <=1 unstated
  assumption — kills the claim.

"Unstated assumption" = filling an OPEN value slot (e.g. 44="la"). Overturning
a banked, granted, promoted, or provisional standing value is not an "unstated
assumption" — it is a contradiction of standing, and does not count as a parse.

Standing values used: banked 11=la, 70=pre, 82=m, 29=er, 46=que;
granted/promoted 87=ce, 64=qui, 47=ce, 30=pas, 39=a/a, 94=ne, 12=n, 48=e,
24=finite-verb (class), 21=noun-class (registry), 86=INF-class;
provisional 59=est, 77=le.

## Method

Re-derived the repaired stream independently. 83 census n=15 at
@228/@614/@898/@907/@911/@931/@1061/@1161/@1171/@1217/@1334/@1612/@1784/@1829/@1840 —
byte-identical to the de-83-sweep and fence-911-de censuses. Each of the 10
non-'de' windows tested under 83="gar" as (a) word-level "gar…"/"…gar" and
(b) word-internal syllable, against 1841 French, with standing values fixed.

The claim's "regarder" framing at @907/@1612 (55="re", 54/71="der") is part of
the claim itself — stated, not counted against the assumption budget. Coherence
check: 55="re" fits 55's full census independently — "55 81" x5 ("re"+81,
cf. 81's open stem battery), "55 61" x3 (55-61-94 word-unit lead), "55 83" x2
("regarder"), "55 68" x1 — so the regarder legs are the claim's strongest
windows, not question-begging.

## Window-level evidence

**@614 — `02 58 47 77 87 [83] 70 88 10 29 88` (row a4_00): KILL-GRADE.**
"…ce le ce gar pre [88] er [88]". 87='ce' granted, 70='pre' banked.
Word-level: "ce" + "gar…": "ce garde/garder pre" ungrammatical; "garpre" is not
a French word. Word-internal "cegarpre": not French. Word-final "…cegar": no
French word ends "-cegar". No parse without overturning granted/banked values.
Forces otherwise.

**@907 — `67 16 88 18 55 [83] 54 49 64 83 59` (row a5_09): PARSES.**
"…[18] regarder [49] qui…" — 55="re", 83="gar", 54="der" (claim-stated).
Infinitive grammatical in context (open 18/49 governors, no contradiction;
67='et' here since 67's follower 16 is not infinitive-shaped, and "et … regarder
[49] qui…" is grammatical). 0 unstated assumptions.

**@911 — `55 83 54 49 64 [83] 59 37 96 09 02` (row a5_09): KILL-GRADE.**
"…qui gar est". 64='qui' granted, 59='est' provisional. "qui garde/garder est"
ungrammatical; word-internal "quigarest" not French. The only rescue —
59="de"-syllable ("qui garde [59]") — contradicts provisional 59='est'
(est-59-frames battery-promoted); that is a standing revision, not an unstated
assumption. Forces otherwise. (This window is independently kill-grade for
unconditioned 83='de', already escalated to the red team by fence-911-de.)

**@1161 — `80 17 77 82 44 [83] 21 67 78 45 13` (row a6_09): KILL-GRADE.**
"…[80] fois le m [44]gar[21] et/veut…". "garde"/"gare"/"regarder" continuations
all require the follower 21 to be "de"/"e"/"der" — 21 is noun-class (registry):
blocked. Word-internal "hangar" (44="han", 1 assumption) strands "77 82" =
"le m" and needs a second assumption for the missing article. Forces otherwise.

**@1171 — `13 55 61 94 87 [83] 21 85 36 74 32` (row a6_09): KILL-GRADE.**
"…[55-61-94 word] ce gar [21]…". "ce garde" (verb after "ce") and "ce garder"
ungrammatical; word-internal "cegar" not French. The live rival at this exact
window is 87-83="cède" (frame-87-83-cede, verdict NULL, rival kept live) — a
different 83 value, incompatible with 83="gar". Forces otherwise.

**@1217 — `48 96 45 36 77 [83] 92 61 24 48 30` (row a7_00): PARSES (1 assumption).**
"…[36] le garde [61]…" with 92="de" — 92's value is open, so this is 1 unstated
assumption, within budget. 77='le' provisional. "le garde" grammatical (noun).
Positive leg for the "gar" syllable.

**@1334 — `62 94 70 52 39 [83] 86 71 64 60 08` (row a7_05): PARSES, conditional (1 assumption).**
"…il ne pre[52] a gardé [71] qui…" with 86="dé" — 86's syllable slot is open
(INF-class grant is class-level; the syllabic fork is positional, cf. syll-83-de),
so 1 unstated assumption, within budget. 39='a' promoted. "a gardé [71]"
grammatical pending 71. Tension recorded: if 86's INF-class ever narrows to
exclude the "dé" syllable, this leg falls.

**@1612 — `92 65 23 08 55 [83] 71 48 31 76 42` (row a8_03): PARSES.**
"…[08] regarder e[31]…" — 55="re", 83="gar", 71="der" (claim-stated).
Infinitive grammatical pending open neighbors (08/31 open, no contradiction).
0 unstated assumptions.

**@1829 — `00 86 29 82 38 [83] 24 82 16 59 36` (row a8_11): KILL-GRADE.**
"…pour [86]er m[38]gar [24-finite]…". 24 is class-level promoted FINITE verb.
"garde"/"gare"/"garder" all require 24="de"/"e"/"der" — contradicts the promoted
finite-verb class. "hangar" (38="han", 1 assumption) yields "…me hangar [verb]"
— broken French. Forces otherwise.

**@1840 — `69 64 22 42 44 [83] 21 67 78 49 74` (row a8_11): KILL-GRADE.**
"…[42][44]gar[21] et/veut…". Same 21 noun-class block as @1161: every
"gar+X" continuation needs 21="de"/"e"/"der". "hangar" (44="han") needs a
second assumption for the article ("[42] hangar"). Forces otherwise.

## Per-clause pass/fail

- **C1: FAIL.** 6 of 10 non-'de' windows do not parse under 83="gar"
  (@614, @911, @1161, @1171, @1829, @1840). Promote is out.
- **C2: FIRES.** Six independent windows force otherwise — each is unfalsifiable
  under standing values: @614 (granted 87='ce' + banked 70='pre' block every
  shape), @911 (provisional 59='est' blocks the only rescue), @1161/@1840
  (21 noun-class blocks every "gar+X" continuation), @1171 (live 'cède' rival
  owns the window), @1829 (promoted 24 finite-verb class blocks every
  continuation). The bar's kill condition is met six times over.

## Verdict: KILL

83="gar" is killed as a conditioned value across the non-'de' windows. This is
falsification at bar grade, not underdetermination: the failures turn on
banked, granted, and promoted standing values, and no window's failure is
rescuable within the <=1-unstated-assumption budget.

Standing check: no standing verdict promotes 83="gar" or depends on it. The
five 98-conditioned 'de' windows were excluded per the claim and are untouched.
The 83='de' lead (de-83-sweep NULL), the 'cède' rival (frame-87-83-cede NULL),
the '-de' syllable fork (syll-83-de NULL), and the fence-911-de red-team
escalation are all untouched. No red-team verdict contradicted; nothing
downgraded.

Surviving observation (not a follow-up proposal): the "gar" SYLLABLE is live at
four windows — "regarder" x2 (@907/@1612, the claim's exemplar legs, with 55="re"
independently coherent), "le garde" (@1217, 1 assumption), "a gardé" (@1334,
1 assumption). A narrowed syllable-only target restricted to those windows was
not tested here; the claim as barred — all non-'de' windows — is dead.

## Adverses

None recorded ("adverses": null in queue). All standing neighbor verdicts
checked for contradiction: none found.

## Bookkeeping

- Report: this file (`code/crowd17/report_inbox/battery-re83-gar-test.md`).
- Queue: `re83-gar-test` -> status `verdict`, result `kill`, date 2026-10-09
  (temp-file + rename; pre-write assert confirmed queued/verdictless; JSON
  re-validated post-write; only this target's entry touched).
- Lock `re83-gar-test.lock`: created on start, deleted on completion.
