# Battery verdict: lon-09-reseg

## Bar (verbatim, pre-registered)

"test word-initial 09 in a longer word with the following verb-class group, or a clause boundary between 09 and 98/24"

Restated as numbered clauses:
- C1: enumerate admissible segmentations of the 'l'on 09 [98/24]' windows under standing values.
- C2: adopt one segmentation iff it parses with zero new assumptions AND kills/fences all rivals.
- C3 (else-branch): fence with stated cause.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/lon-09-reseg.lock` on start
(agent id + UTC timestamp); deleted on completion per protocol.
Re-derived the repaired stream from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`):
1,847 pairs / 96 types verified. `canonical.py` never touched. R5005, sealed
gates, red-team adjudication queue untouched.

Standing values used (§7): GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce;
provisional 59=est, 77=le. Battery-grade (not standing): 98='vient'
(vient-98-894-reaudit), 45='ce' demonstrative pronoun (A11), 06='ent'
(06-forces-84). Docketed (unresolved): 24 = 'en' vs finite-modal. Kills honored:
09/92 "-ère" (A6); 09~92 HOLD; 67 sole true polyvalence (§7). lon-09-verb's
battery findings used as leads only: @290 forces 09 nominal ("[97] [09]
qui(64)" on granted 64='qui'); 09's class stays open.

## Window inventory (byte-exact, 1-based @)

Exactly two `77 84 09` windows exist in the 1,847-pair stream:

- **W1 @1060** (row a6_04): `... 1056:45 1057:23 | 1058:77 1059:84 1060:09 | 1061:98 1062:83 1063:82 1064:96 1065:21 1066:62 ...`
  Full: `[29=er][40=e][29=er] [74][74] [45=ce-A11] [23] | l'on(77 prov, 84 granted)
  [09] | [98=vient batt] [83] m(82 GT) par(96 granted) [21] [62]`
- **W2 @1766** (rows a8_08/a8_09): `... 1762:93 1763:06 | 1764:77 1765:84 1766:09 | 1767:24 1768:87 1769:64 1770:26 1771:37 1772:78 ...`
  Full: `[85][58][17=fois][78][41][15][93][06=ent batt] | l'on [09] |
  [24 modal-docket] ce(87) qui(64) [26] [37] [78]`

(The brief's @1060/@1766 are 09's 1-based positions; 77 sits at 1058/1764,
84 at 1059/1765, X=98 at 1061, X=24 at 1767.)

## C1: admissible segmentations of "77 84 09 X"

- **S1 (status quo):** [77 84] | [09] | [X] — "l'on" + standalone 09 + X.
- **S2 (bar hypothesis A):** [77 84] | [09 X] — 09 word-initial in a longer
  word with the following verb-class group.
- **S3 (bar hypothesis B):** [77 84] | [09] ‖ [X] — clause boundary between
  09 and 98/24.
- **S4:** [77] | [84 09] | [X] — "le" + "on-09" word.
- **S5:** [77 84 09] | [X] — one word "l'on09...".

## C2: adoption test (zero new assumptions + kill/fence all rivals)

- **S1:** parses structurally with no new assumptions (09's value stays open;
  lon-09-verb already fenced the verb-09 reading, S1 needs only non-verbal 09).
  Nothing in the stream forces a resegmentation, so **S1 cannot be killed** —
  adoption of any rival already fails the "kill/fence all rivals" half of C2.
- **S2 at W1 ([09 98] one word):** needs 98='vient' (battery-grade, not §7
  standing — assumption 1) and 09 = a verbal prefix ('sur'/'de'/'re'/'con' in
  "survient/devient/revient/convient" — assumption 2; 09's class is open).
  Worse, a general prefix-class for 09 is **killed at battery grade**: @290
  "[97] [09] qui(64)" forces 09 nominal on granted 64='qui', and §7 licenses
  67 as the SOLE true polyvalence — 09 cannot be nominal at @290 and
  verbal-prefix at @1060 without red-team positional resolution. As a purely
  local segmentation it is unfalsifiable without 09's value. Not adoptable.
- **S2 at W2 ([09 24] one word):** 24's class is docketed. On the finite-modal
  reading, French modals take no productive prefix — "[09][modal]" has no
  grammatical parse (hostile). On the 'en' reading (unresolved), "[09]en" one
  word needs 09's value (new assumption). Not adoptable.
- **S3 at W1 ("l'on [09]. ‖ vient [83]-m par [21]..."):** clause-initial
  "vient" (3rd sg) with no subject; the post-verbal "[83]-m par [21]" cannot
  supply one (a "par"-phrase cannot head a subject NP). Ungrammatical on
  standing values; rescue needs values for 83/21 (new assumptions). Fenced —
  structurally hostile.
- **S3 at W2 ("l'on [09]. ‖ [24] ce qui [26]..."):** parses ONLY as the idiom
  "En ce qui [26]..." ("as for / regarding"), which needs 24='en' (docketed,
  unresolved) + 26 = 'concerne'-class (unknown) — two new assumptions. On the
  modal-24 reading, "[24] ce qui" is ungrammatical ("*doit ce qui"). Not
  adoptable; the "en ce qui" frame is a live lead for the 24 docket.
- **S4 ([84 09] word):** 'on' is a complete grammatical word (84='on'
  granted); suffixing 09 needs a value assumption with no French morphology
  behind it. Fenced — no gain, new assumption.
- **S5 ([77 84 09] word):** discards the "l'on" elision frame (granted 84)
  for an unnamed word; needs 09's value. Fenced.

No candidate parses with zero new assumptions; S1 (status quo) cannot be
killed. C2 fails for every rival.

## C3: fence (fires)

The resegmentation claim is **fenced**, not killed: no admissible
segmentation meets the adoption bar, and S1 stands unkilled. Stated cause:
every resegmentation (S2–S5) needs at least one new assumption — a value or
class for 09 (unvalued, class open), a docketed value (24='en'), battery-grade
98='vient', or values for unknown neighbors (83/21/26) — while the
clause-boundary rival is structurally unfalsifiable from the digit stream.
Additionally, S2 as a general claim is killed at battery grade (@290 nominal
+ §7 sole-polyvalence); only red-team positional resolution could revive it
locally.

## Frame caveat

The whole "l'on 09" frame rests on provisional 77='le'. If 77 resolves
otherwise, this target's frame needs re-audit (cf. armed `lon-77-le-gate`,
NULL).

## Adverses

None listed in the target brief.

## Standing-state check

No standing verdict contradicted or downgraded. No red-team verdict on 09's
segmentation exists. §7 honored — no polyvalence declared; S2's general form
stays dead under the 67 sole-polyvalence rule pending red-team action.

## Verdict: NULL (fence executed)

## Follow-ups proposed (for supervisor queuing)

1. `pos-09-290-1060` (P3): red-team positional adjudication for 09 — nominal
   at @290 ("[09] qui"-antecedent on granted 64='qui') vs verbal-prefix at
   @1060 ("[09]vient"); §7 sole-polyvalence blocks battery resolution.
2. `en24-cequi-1766` (P3): test "En ce qui [26]..." at @1766 under S3 —
   gated on the red-team 24='en' vs finite-modal docket; name 26's class
   (concerne-frame?).
3. `vient98-1060-frame` (P3): under standing S1, resolve the W1 clause —
   "[29er][40e][29er] [74][74] ce(45) [23] l'on [09] vient(98) [83]m par(96)
   [21]" — name 09's non-verbal value (interjection/adverb lead) and 83/21;
   gated on 98='vient' ratification.
