# Battery report — orphan86-716 (@716's 86 does not resolve via 66's class)

Worker: 4712158d-4be1-4929-aec3-122d20ddd574. Date: 2026-10-08.
Lock: `code/crowd17/next-token/locks/orphan86-716.lock` created 2026-10-08T20:08:04Z
(no lock present); deleted on completion.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
(asserted 1,847 pairs / 96 groups before counting). `canonical.py` not used.
R5005 not touched. No invented numbers: every count below was re-derived from
the stream in this run.
Coordination: no overlap with queued `frame-97-profile` (owns naming 97's
class), `prof-98` (owns 98's class), or `stem-86` (owns 86's whole/stem
adjudication). 97's class is not named here; 98's class is not named here.
Sibling orphan batteries `orphan86-300` and `orphan86-1131-1147` (both KILL,
2026-10-08) are inherited, not re-litigated.

## Bar (verbatim, from battery-queue.json)

"resolve iff 66's named class makes 'pour [66] [86] [01]' parse
(adverb-before-infinitive? verb+infinitive complement?) with zero
contradiction; else confirm orphan"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. A 66 class is named from 66's contact profile on the repaired stream, and
   `00-66-86-01` @714-717 parses as "pour [66] [86] [01]" under that class
   (via the adverb-before-infinitive shape "pour [adv] [86-inf] [01]" or the
   verb+infinitive-complement shape "pour [66-modal] [86-inf] [01]") with
   zero contradiction at any of 66's windows → claim resolves.
2. Otherwise → confirm orphan: every viable 66 class is eliminated by stated
   hard windows (banked/promoted/granted neighbors only), and any
   two-class rescue is recorded against the §7 sole-polyvalence bar rather
   than declared → the resolution claim is refuted.

## Method

Re-derived 66's full census (n=19) with predecessor/follower distributions on
the repaired stream. Enumerated every 66 window with ±4 context. Tested six
candidate classes (plain infinitive, modal infinitive, adverb, noun, finite
verb, disjunctive pronoun) window-by-window, counting a contradiction only
where banked/promoted/granted neighbors force ungrammatical French. Checked
the @948 `86-01` control window and 01's standing (general 'ci'/'faisant'
values KILLED, battery-ci-01-value 2026-10-08; only bound "-ci" in "ceci"
fenced). Inherited stem-33-86's per-window adjudication (86: 4 stem / 23
whole / 4 orphans / 1 fenced over n=32; orphans = @300/@716/@1131/@1147).

## Window-level evidence

Target window @716 (row a5_01), repaired-stream pair indices:

`@710:48 @711:71 @712:12 @713:63 @714:00 @715:66 @716:86 @717:01 @718:02 @719:21 @720:80`

= "…[63] pour [66] [86] [01] [02]…" (00="pour" A9 class-level; 86 INF-class
A9 class-level subject to stem/whole caveat; 66/01 open). Note the same row
carries a second 66 at @705 (`12-66-21`).

66 census re-derived (n=19; offsets [88, 123, 140, 153, 189, 246, 254, 457,
705, 715, 766, 1018, 1109, 1150, 1346, 1459, 1494, 1533, 1622]):

- pre: 00 x7 (@188/@245/@253/@714/@1108/@1493/@1532 — exact match to the
  queued evidence), 86 x2, 13 x2, 77/58/46/12/88/15/33/78 x1.
- fol: 98 x3, 73 x3, 14 x2, 84 x2, 91 x2, 01/21/86/24/79/15/67 x1.
- `66-86` bigram: exactly 1 stream-wide (@715). `86-01`: exactly 2 (@716,
  @948). Control @948 (row a6_00): `…62 98 96 [86] 01 77 86…` =
  "…par [86] [01] le…" — the `[86] [01]` tail recurs after "par", so it is a
  real constituent independent of 66; 01's value stays open (general values
  killed), giving no rescue.

The 19 windows fall into four governor groups:

- (a) pour-governed x7: @189 `00-66-24`, @246 `00-66-91`, @254 `00-66-01`,
  @715 `00-66-86` (target), @1109/@1533 `00-66-73`, @1494 `00-66-15` →
  non-finite class required (INF / noun / adverb-before-INF / disjunctive
  pronoun; "pour"+finite verb impossible).
- (b) `66-84` x2: @153 `46-66-84` ("que [66] on [26]", 46="que" banked GT,
  84="on" A15 grant, 26=verb here since pre=84 not 11), @1150 `33-66-84`
  ("[33] [66] on [02]", 33 dire/croire LEAD unpromoted) → "que [66] on" is
  ungrammatical for every non-finite class; only a finite-verb
  ("[verb]-t-on") shape fits, and that needs an unwritten euphonic -t-.
- (c) `X-66-98` x3: @88 `77-66-98` ("le [66] [98]", 77="le" provisional),
  @123 `58-66-98`, @766 `88-66-98` → nominal-shaped ("le [noun] [verb]" if
  98 is verbal; prof-98 still queued).
- (d) post-infinitive x2: @1346 `86-66-73`, @1459 `86-66-79` ("[86-inf]
  [66] …", 86 whole-infinitive per stem-33-86 — neither is a stem window)
  → adverb ("manger bien") or noun-object fit; modal/finite do not.

Contradiction table (hard = banked/promoted/granted neighbors force the
failure):

| candidate class | hard contradictions |
|---|---|
| plain infinitive | @715 "pour [inf] [86-inf]" (86 INF-class, A9); @1346/@1459 "[86-inf] [inf]"; @153 "que [inf] on" |
| modal infinitive ("pouvoir"-shaped) | @1346/@1459 "[86-inf] [modal]"; @153 "que [modal] on" |
| adverb | @153 "que [adv] on" HARD (banked 46 + granted 84); @88 "le [adv] [98]" (77 provisional — medium) |
| noun | @715 "pour [noun] [86-inf]"; @153 "que [noun] on"; @1150 soft (33 open) |
| finite verb | "pour [finite]" x7 (group a) — seven hard contradictions |
| disjunctive pronoun | @153 "que [pron] on" |

Every candidate carries ≥1 hard contradiction. Group (a) demands non-finite;
group (b) demands finite-verb-shaped; the intersection is empty. The only
rescue is two classes for 66 — a second polyvalence, which §7 reserves to
the red team (67 et/veut is the sole true polyvalence). No window can be
fenced at battery level: fencing @153 would need 46≠"que" (contradicts
banked GT) or 84≠"on" (contradicts the A15 grant); fencing @88 would need
77≠"le" with no evidence (inventing data).

The bar's two suggested shapes both die on the same rock: the
adverb-before-infinitive parse ("pour [adv] [86-inf] [01]") is grammatical
at @715 and has a genuine leg at @1346 ("[86-inf] [adv] [73]" = "manger
bien [73]"), but @153 "que [adv] on" is a hard contradiction; the
verb+infinitive-complement parse ("pour [66-modal] [86-inf] [01]") is
grammatical at @715, but @1346/@1459 "[86-inf] [modal]" and @153 kill it.

## Per-clause pass/fail

1. Name-66's-class + zero-contradiction parse of @714-717: FAIL — no single
   class is nameable from 66's profile without hard contradictions (table
   above); the profile's only concentration is pre=00 x7, and every class
   licensed by it is killed by group (b)/(d) windows with banked/granted
   neighbors.
2. Confirm orphan: PASS — all six viable classes eliminated on stated
   grounds; the two-class rescue is fenced to the §7 bar (red-team act),
   not declared; 86@716's own orphan status (stem-33-86) is untouched and
   consistent.

## Adverses disposition

- "66's class fully open": ANSWERED — it remains open. No class is named;
  the elimination table is the finding. Fenced with stated cause, not
  ignored.
- "§7 polyvalence bar if 66 must be two things": FENCED — the evidence does
  pull toward two classes (pour-governed non-finite x7 vs finite-verb-shaped
  "66-84" x2), which is exactly the bar's trigger condition. Declaring a
  second polyvalence is a red-team act; this battery records the tension
  and proposes it as follow-up #1 rather than deciding it.

## Standing-verdict check

No contradiction with any standing red-team or battery verdict. A9's
00="pour" class-level grant and 86 INF-class grant untouched (no window
re-valued). stem-33-86's null (with @716 in its orphan list) is confirmed,
not contradicted. The 10%-orphan arithmetic consequence is stated below, not
decided here. No escalation required (no standing verdict contradicted).

## Verdict: kill

The claim "@716's 86 resolves via 66's class" is refuted at kill grade: no
66 class can be named that makes "pour [66] [86] [01]" parse with zero
contradiction — every candidate class is killed by hard windows with
banked/granted neighbors, and the two-class rescue hits the §7
sole-polyvalence bar (red-team territory). Per the bar's else branch, the
@716 orphan is CONFIRMED.

Arithmetic consequence for stem-33-86's clause 3 (orphan rate ≤10%): with
@300, @1131, @1147 already confirmed orphans (sibling kills, 2026-10-08),
confirming @716 holds 86 at 4/32 = 12.5% orphan — the ≤10% bar stays unmet
(it would have flipped to 3/32 = 9.4% on a resolve).

## Follow-ups

Kill verdicts do not regenerate work by default, but the §7 tension surfaced
here is new (no queued target owns 66) and decides the one live arithmetic
question in the lane, so two are proposed:

1. **poly-66-split** (priority 2): test whether 66 splits into two classes —
   pour-governed non-finite (x7: @188/@245/@253/@714/@1108/@1493/@1532) vs
   the finite-verb-shaped "66-84" x2 (@153/@1150) and nominal "X-66-98" x3
   (@88/@123/@766). Bars: distributional split per the {33,86} precedent
   (successor/predecessor permutation); if the red team declares the split,
   re-test @716 under the pour-class alone (a resolve there flips stem-86
   to 3/32 = 9.4% and meets the bar).
2. **adv-66-conditional** (priority 3): re-test 66=adverb
   ("pour [adv] [86-inf] [01]") iff the red team fences @153 with stated
   cause. Legs banked here: @715 target shape, @1346 "[86-inf] [adv] [73]",
   @189 "pour [adv] [24]" conditional on 24's form (ne-24-profile promote,
   pending ratification). @88's "le [adv]" tension rides on provisional
   77="le" and is the weaker adverse.

## Reproducibility

All censuses re-derived inline in this session against the repaired stream
only (asserted 1,847 pairs / 96 groups before each count). `00-66` offsets
re-derived as [188, 245, 253, 714, 1108, 1493, 1532] — exact match to the
queued evidence. `66-86` exactly 1 (@715); `86-01` exactly 2 (@716, @948).
No writes outside this report, the queue entry, and the lockfile.
