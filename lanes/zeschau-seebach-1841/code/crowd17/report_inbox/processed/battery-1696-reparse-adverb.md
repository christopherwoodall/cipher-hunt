# Battery `1696-reparse-adverb` — verdict: PROMOTE (B-frame collapse confirmed; surviving parse delivered)

Worker: subagent 1696-reparse-adverb · lock 2026-10-09T13:02:00Z
Follow-up #2 of `15-noun-verify` NULL (2026-10-09). Delivers to red-team input
package `58-det-numeral-tension` (P2, still queued).

## Bar (verbatim from battery-queue.json)

"deliver the surviving parse (or the confirmed B-frame collapse) to the
58-det-numeral-tension docket: (a) clause-boundary-after-58 ('...[85] [58].
[15-adv] [23] 91...'), (b) verb+object+adverb ('que [24] [85] [58-noun]
[15-adv]' - '[inf] [noun] souvent'-shaped), (c) the postposed '94 30'
@1701-1702 geometry"

Restated as numbered pass/fail clauses (not modified after seeing data):
- C1: (a) clause-boundary-after-58 is tested; definitive result delivered
  (survives, or fails with stated cause).
- C2: (b) verb+object+adverb '[inf] [noun] souvent'-shaped is tested;
  definitive result delivered.
- C3: (c) the '94 30' @1701-1702 geometry is tested; definitive result
  delivered (licensed, or unlicensable with stated cause).
- C4: the surviving parse (or the confirmed B-frame collapse) is delivered
  to the `58-det-numeral-tension` docket.
- Adverse: frame A @1756 '[58] fois' is unaffected — do not disturb it.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `code/side-keyhunt/repair_parse.py` (asserts held: 1847 pairs,
96 types). `canonical.py` never used.

Adopted premises (standing, not re-litigated): 46=que (banked ground truth);
85 verb-stem (A3 frame grant, value open); 58 nominal class (R19 grant);
15 adverb-class (15-noun-verify NULL: noun fenced at type level via
A1+A2+§7); 94="ne" single value (R19-167, split closed); 30="pas"
(battery-promoted, per ne-attachable-paradigm); 33 infinitive-class;
88 gov/verb-class and infinitive-capable (licensed reading at @1541:
"Il [93-fin] [88-inf] le [78]"); §7 (67 sole true polyvalence).

CRITICAL PREMISE UPDATE: the bar's (b) was drafted under the pre-R24
premise (24 as finite/modal verb, R17-009 provisional). R24 (red-team,
round 19) supersedes it: 24="en" iff the follower is 85. Byte-confirmed
this session: 24 is followed by 85 at exactly five positions —
[732, 955, 1438, 1693, 1754] — and @1693 is one of them (@1693=24,
@1694=85). Therefore 24@1693 = "en" (standing red-team declaration,
adopted not re-litigated). All parses below are tested under R24.

## Window-level evidence (byte-exact, 0-based)

Target window, row a8_06:

| @ | cell | @ | cell | @ | cell |
|---|------|---|------|---|------|
| 1692 | 46 (que) | 1696 | 15 (adv-class) | 1700 | 33 (inf) |
| 1693 | 24 ("en" per R24) | 1697 | 23 (unvalued) | 1701 | 94 ("ne") |
| 1694 | 85 (verb-stem) | 1698 | 91 (unvalued) | 1702 | 30 ("pas") |
| 1695 | 58 (nominal) | 1699 | 85 (verb-stem) | 1703 | 20 (unvalued) |

Right tail: @1704=62 ('il' killed R19, unvalued), @1705=94 ("ne"),
@1706=88 (verb-class), @1707=26, @1715=59 ("est" provisional).

Frame A (adverse): @1754=24, @1755=85, @1756=58, @1757=17 ("fois"),
@1758=78 → "en [85] [58] fois [78]". Untouched by this battery.

n(58)=7 stream-wide: [@55, @122, @157, @610, @1202, @1695, @1756].
n(15)=10. The B-frame under test is @1695 only.

## Per-clause results

### C1 (a) clause-boundary-after-58: FAILS — fenced with stated cause

Parse: '...[85] [58]. [15-adv] [23] 91...'

The post-58 clause "[15-adv] [23] 91 [85] [33]..." cannot be a clause at
battery grade:
- Subject: no nameable candidate. @1697=23 unvalued (23~26 split holds;
  23 itself unvalued; follow-up `23-1697-class` still queued).
  @1698=91 unvalued. §3 bars inventing values. French finite clauses
  require an overt subject (not pro-drop); no ellipsis license applies.
- Finite verb: none securely nameable. @1699=85 is verb-stem with value
  open (A3); @1700=33 is infinitive-class. Naming 85@1699 finite is an
  ungranted assumption, and even granted, the subject gap remains.
- The left side "que en [85] [58]" completeness likewise requires naming
  85@1694's form (ungranted).

A clause boundary is licensable only if both sides can stand as clauses.
The right side cannot. (a) does not survive. FENCED.

### C2 (b) verb+object+adverb: FAILS as specified — fenced with stated cause

Specified: 'que [24] [85] [58-noun] [15-adv]' — '[inf] [noun]
souvent'-shaped (85=infinitive, 58=object).

- Under standing R24 the material is "que en [85] [58-noun] [15-adv]".
  The bar's original 24-as-modal premise is superseded; testing under R24.
- The specified '[inf]' shape is ungrammatical: declarative "que" does
  not introduce an infinitive clause, and "en" does not govern an
  infinitive (en takes gerundif or finite). "que en [85-inf]" is dead
  in 1841 French.
- "ne...que" restrictive rescue considered and rejected: the @1687–1692
  bracket (94@1687 … 46@1692) has an empty verb slot (@1688=79 "tout",
  not a verb) — independently fenced by neque-verb-slot-wide (15 of 16
  brackets empty; this bracket is one of the 15). Not re-litigated.
- No rescue within ≤1 ungranted assumption preserves BOTH the
  infinitive shape AND 58-as-object. (b) as specified does not survive.

Surviving shape (1 ungranted assumption, delivered under C4): inversion
"qu'en [85-fin] [58-subj-noun] [15-adv]" — "que" complementizer (matrix
leftward, unvalued 27 context, not contradicted) + "en" pronoun (R24) +
85=finite (the single ungranted assumption; A3 verb-stem permits) +
58=subject noun (nominal class granted, R19) + 15=adverb (granted).
"qu'en [verb] [subject] [adverb]" with literary VS inversion in a
"que"-clause ("qu'en parle le ministre souvent"-shaped) is grammatical.
58 is NOMINAL (subject noun) in every viable shape — never numeral.

### C3 (c) postposed '94 30' @1701-1702: ANSWERED — "postposed" is a misread

- '94 30' = "ne pas" (94="ne" per R19-167; 30="pas" battery-promoted).
- As postposed negation of the preceding [85] [33] it would be
  ungrammatical ("ne pas" never follows its verb). That reading is dead.
- Licensed reading: FORWARD negative frame "ne pas … [88]" —
  @1706=88 is gov/verb-class and infinitive-capable (licensed
  "Il [93-fin] [88-inf] le [78]" at @1541). "ne pas" + infinitive with
  intervening material is a licensed frame.
- Grade is conditional, not clean: the second 94 (@1705) intervenes
  between "ne pas" and 88. Adopted from ne-attachable-paradigm
  (PROMOTE), which graded @1701 conditional on exactly this ground —
  not re-litigated here.
- The bar's "postposed" characterization is shown to be a misread: the
  bigram is preverbal to 88, not postposed to 85/33. Answered per §4.

### C4 deliverable: CONFIRMED B-FRAME COLLAPSE + surviving parse

Frame B ("que [24] [85] [58=deux/plusieurs] [15]", the numeral-58 frame
at @1695) is CONFIRMED COLLAPSED:
- Its licensing leg (15-as-noun) was fenced by the parent
  (15-noun-verify: A1+A2+§7 force noun false at type level).
- Rescue (a) fails (C1: no nameable subject for the post-58 clause).
- Rescue (b) fails as specified (C2: R24 makes the infinitive-object
  shape ungrammatical; no in-budget rescue preserves it).
- 58 at @1695 is therefore NOT numeral/determiner-shaped under any
  battery-grade parse.

Surviving parse (1 ungranted assumption, stated above): "que en
[85-fin] [58-subj-noun] [15-adv]" (inversion). 58 = nominal.

### Adverse: HONORED

Frame A @1754–1758 ("en [85] [58] fois [78]") was not modified,
re-valued, re-segmented, or re-parsed in any way.

## Package for the `58-det-numeral-tension` docket (P2, red-team venue)

Headline: at the @1696 window, under 15=adverb, the numeral/determiner
reading of 58 is dead. Frame B contributes NOTHING to the numeral case
anymore — both of its rescues fail at battery grade, and every viable
shape at @1695 has 58 as a NOUN (subject under inversion; object under
the fenced boundary parse). 58=nominal (R19) is consistent with all
surviving shapes here.

The docket's "A&B frames cohere on numeral" claim is reduced to frame A
alone: the numeral reading now rests SOLELY on @1756 "[58] fois"
("deux/plusieurs fois"-shaped). Whether frame A sustains the numeral
against the R19 nominal grant is red-team adjudication — battery grade
cannot resolve a class conflict (per the docket's own bars). This
battery gathers; it does not decide.

Note for the docket (not a battery verdict): the inversion parse's
single assumption (85@1694=finite) is independently testable and would,
if granted, put a finite verb directly under R24's "en" — relevant to
the queued `neque-tail-24-85-clause` investigation of the @1692–1695
tail.

## Verdict: PROMOTE

Deliverable produced: (a) fenced with cause, (b) fenced with cause
under standing R24, (c) answered ("postposed" shown to be a misread;
forward "ne pas" frame at conditional grade), surviving inversion parse
named with its single assumption stated, confirmed B-frame collapse
packaged for the docket, adverse honored.

## Scope

- Contradicts no standing or red-team verdict. R24 adopted and enforced
  (it supersedes the bar's pre-R24 24-premise; applying it is not
  contradicting it). R19-167, ne-attachable-paradigm (PROMOTE),
  neque-verb-slot-wide, 15-noun-verify adopted as premises. §7 intact
  (no class, split, value, or polyvalence declared).
- Untouched: frame A @1756, R5005, sealed gate instances, red-team
  adjudication queue, all other 58 windows (@55/@122/@157/@610/@1202).
- Canonical-stream caveat stands (row a8_06 offsets unvalidated).
- No follow-ups required per §4 (promote). The docket
  `58-det-numeral-tension` carries the open red-team question.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/1696-reparse-adverb.lock` created
  on start (2026-10-09T13:02:00Z), deleted on completion (verified gone).
- Queue update: `1696-reparse-adverb` → status `verdict`, verdict
  `{"result": "promote", "report":
  "code/crowd17/report_inbox/battery-1696-reparse-adverb.md",
  "date": "2026-10-09"}` via same-directory temp-file + rename; JSON
  re-validated from disk; pre-write assert passed (was queued/verdictless);
  only this entry changed; no downgrade.
