# Battery report: frame-43-la-52-37

Worker: 31d99601-b4f1-428f-98cf-2297a1689b42. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt). canonical.py NOT used. R5005 NOT touched.
No invented numbers. Every @-offset below was re-derived from the stream.

## 1. Bar (verbatim from battery-queue.json)

"resolve iff (a) 52 (or the 52-37 unit) is named with both windows parsing;
(b) one 43 value satisfies BOTH continuations (43-pour-[86-INF] and 43-98-39);
(c) feminine agreement via la (11) holds"

Numbered clauses:
1. (a) 52, or the 52-37 unit, takes a named value, and both target windows
   parse under that value.
2. (b) At least one value of 43 satisfies BOTH continuations:
   "43-pour-[86-INF]" and "43-98-39".
3. (c) Feminine agreement through "la" (11) holds in both windows.

Note on sources: the f-qui-par finder report named in the brief
(code/crowd17/report_inbox/processed/next-token-findings-f-qui-par.md) is NOT
on disk (checked report_inbox/, report_inbox/processed/, full lane find).
The 4-gram claim was therefore re-derived from the stream, not taken on trust.
A1 context read from code/crowd15/report_inbox/next-token-redteam.md (A1
section). The A1 predicative-frame grant is NOT re-litigated (standing
constraint, protocol section 7).

## 2. Method

Parsed the repaired stream per code/side-keyhunt/repair_parse.py (1,847
pairs, assert passed). Located the 4-gram 11-52-37-43 by exact match.
Profiled 52 (n=27), 37 (n=28), 43 (n=16), 98 (n=40): predecessor/successor
censuses plus wide-context windows. Tested each queued 43 candidate
{suite, condition, maniere, mesure} against both continuations for French
grammaticality. Tested 52/unit naming against all 52-37 contexts.

## 3. Window-level evidence

Target frames (byte-identical 4-gram, verified):
- @1123: [1122]06 [1123]11 [1124]52 [1125]37 [1126]43 [1127]00 [1128]86
  [1129]52 [1130]37 [1131]86 [1132]24 [1133]77 [1134]86
- @1721: [1720]06 [1721]11 [1722]52 [1723]37 [1724]43 [1725]98 [1726]39
  [1727]88 [1728]24 [1729]30 [1730]15 [1731]01

Shared 5-gram "06-11-52-37-43" byte-identical x2 (@1122, @1720).
06 = 'ent' verb ending (battery-promoted, ent-06). Read: "[verb-ent] la
[52-37] 43" in both windows. This supports the determiner-frame reading:
a finite verb takes "la [52-37] 43" as its direct object.

Continuation A (@1127): 43-00-86. 00 = "pour" (A9, leg-1 class-level);
86 = INF-class (A9 class-level grant). Read: "43 pour [INF]" (purpose).
43-00 occurs x3/16 (@244 "43 pour [66]", @1126, @1544 "43 pour que [70]").
43 is a "pour"-governor at 3/16 = 19% of its windows.

Continuation B (@1725): 43-98-39. 98-39 is a HAPAX bigram (only @1725).
39 = "a"/"a" (battery-promoted a-39, allophone tier; "a" vs "a" is not
cipher-testable). 98 is open (n=40; top successors 83 x5, 82 x3, 80 x3,
98 x3, 00 x3). Read: "43 [98] a/a [88] que [30] ...".

Other 52-37 contexts (unit = 52-37, n=4):
- @1129 (inside target 1's tail): "43-00-86-52-37-86" = "43 pour [86]
  [52-37] [86]". The trigram 52-37-86 is a HAPAX; segmentation is
  ambiguous ("[52-37] [86]" vs "[86-52] [37-86]"; 86-52 occurs x2:
  @1099, @1128).
- @1356: "94-82-06-52-37-64-35" = "ne m'[ent] [52-37] qui [35]"
  (64 = "qui", granted). Unit before a relative clause.

52 profile (n=27), the naming problem for clause (a):
- "la 52": x3 (@1007 "la 52 [35]"; @1123/@1721 in-frame). Nominal slot.
- "ne 52 [80]": x2, byte-identical 6-gram "84-59-35-94-52-80" @1293/@1806
  ("on est [35] ne 52 [80-verb]"). 52 sits in clitic slot ("ne [clitic]
  [verb]").
- "52-82" ("52 m'/me"): x5 (@649, @1100, @1385, @1435, @1574). Verbal
  clitic government.
- "52-30" ("52 pas"): x2 (@482, @1308), but "94-52-30" ("ne 52 pas")
  trigram = ZERO. No clean negation frame.
- "52-80" x2 (same windows as "ne 52 [80]").
No one French value fits the nominal slot ("la 52"), the clitic slot
("ne 52 [verb]"), and "52 m'" government at the same time. Declaring
polyvalence is a red-team act (protocol section 7: 67 is the sole true
polyvalence). Naming the 52-37 unit from "la __ 43" x2 + @1129 + @1356
does not converge on one word without guessing.

43 profile (n=16): successors 00 x3, 77 x2, 87 x2, 98 x2, 29/81/91/24/07/
55/21 x1. Predecessors: 37 x3, 96 x2 ("par 43" @343, @1027), 11 x1
("la 43" direct @562-563), 82/88/56/32/46/06/47/08/21/78 x1.
"37-43" x3 (@385, @1125, @1723).

## 4. Per-clause pass/fail

Clause (a) — FAIL (untestable as written at battery grade).
52's contact profile pulls three ways (nominal "la 52" x3; clitic "ne 52
[verb]" x2; "52 m'" x5). The 52-37 unit's adjective slot in "la __ 43"
is the best single reading, but no value name is derivable without
guessing, and the @1129/@1356 contexts do not converge on the same word.
Per protocol section 4, a genuinely untestable bar is recorded as a
finding and counts as a null. No polyvalence declared (red-team act).

Clause (b) — PASS at existential grade; PARTIAL on discrimination.
Continuation A ("43 pour [INF]") discriminates the candidate set 4 -> 2:
- "suite": FAILS. "suite" governs "de"/"a" ("donner suite a",
  "suite de"). "la suite pour [inf]" is not idiomatic French.
- "condition": PASSES. "les conditions pour [inf]" / "la condition pour
  [inf]" is idiomatic ("les conditions pour reussir").
- "maniere": FAILS. "maniere" governs "de" ("la maniere de faire").
  "la maniere pour [inf]" is not idiomatic French.
- "mesure": PASSES. "des mesures pour [inf]" is idiomatic ("prendre des
  mesures pour proteger"); singular "la mesure pour [inf]" is
  grammatical.
Continuation B ("43-98-39"): 98's value is open, so B cannot discriminate
further now. B is COMPATIBLE with both survivors: if 98 is copula-like,
"la mesure est a [inf]" ("etre a + inf") and "la mesure reste a [inf]"
("rester a + inf") are grammatical, and the same holds for "condition".
98 is therefore FENCED as the blocker (stated cause: value open,
98-39 hapax), not ignored.
Result: at least one 43 value (in fact two: condition, mesure) satisfies
both continuations; suite and maniere are killed by continuation A. The
claim's "divergent continuations discriminate 43's value" is borne out
as a 4 -> 2 narrowing, not a singleton identification.

Clause (c) — PASS.
11 = "la" is banked pencil ground truth (feminine singular article).
Both windows read "[verb-ent] la [52-37] 43": "la" heads the noun phrase
in both, so head noun 43 must be feminine. All four queued candidates are
feminine. Zero masculine-agreement evidence anywhere in 43's 16 windows.

## 5. Adverses answered

1. "52's value open" — CONFIRMED open. Answered: fully profiled (n=27;
   nominal vs clitic vs "m'"-government pull documented above); fenced
   as underdetermined, not ignored. This is the cause of the null.
2. "37 predicative-vs-nominal tension (A1 frame grant vs nominal slot
   here)" — NOT re-litigated per standing constraint. Fenced with stated
   cause: A1 grants the 59->37 predicative FRAME with value open; the
   nominal slot in "la 52-37 43" is the known standing tension, already
   escalated to the red team via battery-frame-37-reexam (null
   2026-10-08). No new claim made here.
3. "none of the four queued candidates takes pour+INF naturally
   (de-government instead) - the frame may kill all four" — SHOWN
   MISREAD in part, CONFIRMED in part. Re-derived: "condition" and
   "mesure" DO take "pour + INF" naturally ("les conditions pour
   [inf]", "des mesures pour [inf]"); "suite" ("suite a/de") and
   "maniere" ("maniere de") do NOT. The frame kills two of the four,
   not all four. The adverse's blanket claim is corrected.

## 6. Verdict: NULL

Clause (a) is untestable as written at battery grade (protocol section 4:
counts as null). Clauses (b) and (c) are evaluated above. No standing
red-team verdict is contradicted: no red-team ruling exists on 52, 98,
or this frame; 43's value was left open here (naming bar belongs to the
parallel noun-43-discriminator worker — coordinated, not duplicated);
the A1 frame grant is untouched.

## 7. Follow-up targets (null regenerates work)

F1. id: "cont98-43-value" | priority: 2
claim: "Naming 98 (copula-like vs other) decides condition vs mesure via
continuation B (43-98-39)"
bars: "name 98 iff >=2 independent frames parse under one value with zero
contradictions across its 40 windows; then re-test @1725 under 43 =
condition vs 43 = mesure and record which value continuation B selects"
evidence: "43-98-39 hapax @1725 (39 = a/a); 98 n=40, top suc 83 x5 / 82 x3
/ 80 x3 / 00 x3; second 43-98 window @439 ('43-98-80'); 'etre a + inf' /
'rester a + inf' are the live grammatical readings for B"
adverses: "98-98 doubled x3 pairs; 98-83 x5 ('de'-follower) tensions a
copula reading; frame-vient-parvenir's French for 98 is unconfirmed"

F2. id: "unit-52-37-name" | priority: 2
claim: "The 52-37 unit takes one name across 'la 52-37 43' x2, @1129
'[86] 52-37 [86]', and @1356 'ne m'[ent] 52-37 qui [35]', or the
nominal-vs-clitic split is referred to the red team"
bars: "name the unit iff one value parses all three context types with
<=10% orphan; else state the split candidacy (52~52) with per-window
parses for red-team adjudication — do not declare polyvalence at battery
level"
evidence: "52-37 bigram x4 (@1124/@1129/@1356/@1722); 52 n=27: 'la 52' x3
vs 'ne 52 [80]' x2 (byte-identical 6-gram '84-59-35-94-52-80') vs '52-82'
x5; '94-52-30' trigram x0; 52-37-86 trigram hapax (segmentation open)"
adverses: "protocol section 7: 67 is the sole true polyvalence —
declaring a second is a red-team act; @1129 hapax segmentation"

F3. id: "frame-43-pour-census" | priority: 3
claim: "The 4 -> 2 discrimination (suite/maniere killed, condition/mesure
survive) holds across ALL of 43's 'pour' windows, not just @1126"
bars: "confirm-or-reject the 4 -> 2 at every 43-00 window (@244 '43 pour
[66]', @1126 '43 pour [86-INF]', @1544 '43 pour que [70]') plus the
second 43-98 window (@439 '43-98-80'); record per-window survivor sets"
evidence: "43->00 x3/16 (19% pour-government); 43->98 x2/16; @1544 '43
pour que' is the noun-43 queue's own discriminating frame"
adverses: "@439's 98-80 (verb-frame follower, not 98-39); 66/70 followers
open; feeds (does not duplicate) the parallel noun-43-discriminator
naming bar"
