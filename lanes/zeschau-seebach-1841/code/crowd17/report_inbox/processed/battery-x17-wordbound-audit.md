# Battery `x17-wordbound-audit` — verdict: PROMOTE

## Bar (verbatim, pre-registered)

"Complete the audit (heterogeneity already proved at @1038/@367)."

Restated as numbered pass/fail clauses:

- **C1:** all 15 X-17 windows audited against standing values, each classified word-internal-17 vs standalone-17, with the byte locus stated.
- **C2 (from adverses):** the audit resolves whether 17="fois" is uniformly standalone, feeding any future "fois"-slot typing.

## Method

Repaired 1,847-pair / 96-type stream re-derived in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py` (`load_rows` + `parse`).
Asserts held: 1,847 pairs, 96 types. `canonical.py` never used.
n(17) = 15, byte-confirmed. Standing values used: pencil GT
(11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted/promoted
(17=fois, 87=ce, 64=qui, 96=par, 79=tout [A5], 00=pour [A9], 84=on [A15],
47=ce, 30=pas, 77=le provisional, 59=est provisional, 94=ne strong lead,
98=vient battery-grade, 24 finite/modal class, 76 noun battery-grade,
06 syllable-tier); kills honored (20="fois", 70="première"-abbreviation,
literal "70 17"/"pre fois" route, 62="il" per R19-106/R20-125, 48="est"/"ne"/"de");
splits honored (20~17, 23~26).

Note on the bar's parenthetical: the loci @1038/@367 do not index 17 in the
0-based repaired stream (@1038=29, @367=61). They are the X−1 positions of the
two key windows @1040 ("34 29 40 [17]", X−1=@1038) and @369 ("70 [17]",
X−1=@367). The audit below covers both windows; the numbering discrepancy is
recorded, not litigated.

## Window-level evidence (all 15, 0-based @ of 17)

| @ | row | left-3 | 17 | right-3 | boundary verdict |
|---|-----|--------|----|---------|------------------|
| 17 | a1_01 | 45 91 53 | 17 | 64 98 82 | standalone: "…[53] fois qui vient m…" (98=vient battery); no license for "53·fois" one word |
| 238 | a2_01 | 70 98 41 | 17 | 11 26 12 | standalone: "pre vient [41] fois la [26]…" (41 class-open, no "41·fois" license) |
| 308 | a2_04 | 02 88 20 | 17 | 46 84 24 | standalone FORCED: 20~17 split holds — "20 17" cannot be one word; "…[20] fois que on en…" |
| 369 | a2_06 | 49 61 70 | 17 | 06 21 65 | standalone FORCED: literal "70 17"/"pre fois" route KILLED; 70="pre" is bound, so "…[61]pre \| fois [06]…" |
| 452 | a3_00 | 32 48 79 | 17 | 77 60 65 | standalone (grant-protected): "…[48] tout \| fois le…" — "toutefois" rival FENCED (see below) |
| 556 | a3_03 | 86 59 34 | 17 | 86 94 59 | standalone: "…est i \| fois [86]…" (34="i" GT letter; no "ifois" word) |
| 837 | a5_05 | 59 35 56 | 17 | 98 20 62 | standalone: "…est [35] [56] \| fois vient…" (no "56·fois" license) |
| 880 | a5_06 | 77 86 78 | 17 | 08 31 79 | standalone: "…le [86] [78] \| fois [08]…" (no "verfois"-type word) |
| 925 | a6_00 | 08 65 71 | 17 | 61 96 48 | standalone: "…[71] \| fois [61] par [48]" — 71 quantifier-shaped; French writes "une/deux/trois fois" as two words |
| 1040 | a6_03 | 34 29 40 | 17 | 77 82 63 | standalone (crib-anchored): "…ière \| fois le m…" = "la première fois" (@1034=11, @1035=70, @1036=82) |
| 1157 | a6_08 | 92 29 80 | 17 | 77 82 44 | standalone: "…[80] \| fois le m [44]…" (80 verb-frame A8; no "80·fois" license) |
| 1289 | a7_05 | 68 00 11 | 17 | 84 59 35 | standalone FORCED: "…pour la \| fois on est…" — 11="la" GT determiner forces determiner+noun |
| 1461 | a8_00 | 86 66 79 | 17 | 01 21 62 | standalone (grant-protected): "…[66] tout \| fois [01]…" — "toutefois" rival FENCED (see below) |
| 1558 | a8_02 | 93 61 40 | 17 | 11 26 30 | standalone: "…[61]e \| fois la [26]…" (40="e" free word-edge-capable letter; no "efois" word) |
| 1757 | a8_07 | 24 85 58 | 17 | 78 41 15 | standalone: "…[85][58] \| fois [78]…" (58 nominal-leaning; no "58·fois" license) |

Follower inventory of 17 (15 windows): 77×3 ("fois le"), 11×2 ("fois la"),
64/46/06/86/98/08/61/84/01/78×1 — every follower composes a grammatical
two-word "fois + X" parse under standing values; zero followers license a
"foisX" one-word reading.

## Per-clause pass/fail

- **C1 PASS** — 15/15 windows audited with byte loci, rows, and standing-value
  parses. 0 windows force word-internal-17. Forced-standalone legs: @308
  (20~17 split), @369 ("pre fois" literal-route kill), @1289 (11="la"
  determiner). Crib/determiner positive legs: @1040 ("première fois"),
  @1289 ("la fois"), @925 (quantifier + "fois" two-word construction).
- **C2 PASS** — the adverse question is answered: **17="fois" is uniformly
  standalone at battery grade.** No window admits a word-internal 17 under
  standing values; the left-neighbor inventory is heterogeneous (13 distinct
  X cells: 79×2, 40×2, plus 11 singletons) yet the boundary behavior is
  uniform. "Fois"-slot typing may treat the 17 slot as a word boundary on
  both sides.

## Headlined fenced rival: "toutefois" at @452/@1461

"79 17" occurs ×2 (@452, @1461). The surface string "tout fois" invites the
one-word reading "toutefois" ("however") — semantically perfect at @452
("…[48] toutefois, le [60]…"). This rival is FENCED at battery grade, not
adopted: the A5 grant fixes 79="tout" as a whole word, and "toutefois"
requires 79="toute" (with "e"), contradicting the grant. Revisiting it is
red-team venue (would require touching A5); this battery does not.

## Secondary observation (not decided)

At @369, the forced parse "…[61]pre | fois [06]…" constrains 06 at @370:
06 is syllable-tier attaching left as word-final "-ent" (subj-42-class),
but left-attachment here yields "foisent", which is not French — so 06
cannot left-attach at @370 and must be word-initial "ent…". Noted for the
06-family; not adjudicated here.

## Scope

Boundary audit only. Untouched: 17's value (promoted "fois" standing),
79's A5 grant, 71's value, 06's class, 58's nominal/numeral tension,
41's split/value, and the @340 "ce qui" twin locus. No standing or
red-team verdict contradicted or downgraded; §7 intact. Canonical-stream
caveat stands (68 of 70 row offsets unvalidated).

No follow-ups required per §4 (promote). Natural next question noted for
the supervisor: re-test "79 17" only if the red team ever re-opens A5
(currently granted — do not dispatch on this without red-team venue).

## Bookkeeping

- Lock `code/crowd17/next-token/locks/x17-wordbound-audit.lock` created on
  start (agent af9d0856-9482-422f-aca7-7a72cf709a88, 2026-10-09T15:40:30Z),
  deleted on completion.
- Queue: `x17-wordbound-audit` → `status: verdict`, `result: promote`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; disk re-validated; own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched.
  `canonical.py` never used.
