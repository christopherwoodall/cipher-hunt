# Battery report: noun-26 (umbrella adjudication)
Date: 2026-10-08. Worker: 8131b8e0-c7ec-4a0f-9007-322dd7dcd5c0.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed like repair_parse.py.
Target: "26 noun-vs-verb" — adjudicate the umbrella claim:
one class for 26 across all windows, or a stated positional rule.

## Bar (verbatim from battery-queue.json)
"resolve iff 26 assigned one class with all windows parsing, or positional rule stated".

## Bar as numbered pass/fail clauses
- Clause 1: 26 assigned ONE class with all 17 windows parsing.
- Clause 2: a positional rule stated (class per window stated, with its
  polyvalence cost flagged to the red team; per protocol section 7 a positional
  rule for 26 needs red-team declaration, not battery declaration).

## Method
Full census of token 26 on the repaired stream: n=17 windows (matches A2's
n26=17). Each window classified against standing values:
banked (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que),
promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on,
47=ce), provisional (59=est, 77=le).
Standing battery verdicts cited as decided evidence (not re-litigated):
noun26-pas-frames (PROMOTE: '26 30' x4 = '[verb] pas', noun-26 killed
unconditioned) and noun26-encequi-triple (PROMOTE: 26 = verb in the
'en ce qui [verb]' formula slot).
Queued targets noun26-gov-frames and noun26-la-frames cited as prior art
(not decided); their bars were not re-run here. All windows below were
re-derived on the repaired stream.

OFFSET NOTE: @-offsets below are repaired-stream offsets. They are +1 vs the
offsets cited in the noun26-finder and noun26-pas-frames reports (canonical.py
parse), e.g. pas-frames @654/@991/@1249/@1559 = repaired @655/@992/@1250/@1560;
encequi-triple @1768 = repaired @1769; la-frames @239/@128/@154 = repaired
@240/@129/@155.

## Window-level evidence (17 windows, context = 4 before / target / 4 after)

VERB-branch windows (14):
- @655 [a4_02]: 94 76 49 24 *26* 30 03 62 16 — 'ne [76] [49] [24] [26] pas'
  clitic-chain (pas-frames T1). Decided verb.
- @992 [a6_01]: 01 76 49 24 *26* 30 03 60 67 — '[76] [49] [24] [26] pas'
  (pas-frames T1). Decided verb.
- @1250 [a7_02]: 16 00 67 46 *26* 30 06 65 46 — 'que [26] pas' (pas-frames T1).
  Decided verb.
- @1769 [a8_08]: 09 24 87 64 *26* 37 78 62 94 — 'en ce qui [26] [37]'
  (encequi-triple). Decided verb.
- @155 [a1_04]: 47 46 66 84 *26* 35 58 35 93 — 'on [26] ...' (gov-frames
  T3 @154). Verb-branch per pre-registered analysis; battery queued.
- @601 [a4_00]: 29 40 03 39 *26* 96 45 93 54 — 'a/a [26] par [45]'
  (gov-frames T3 @600). Verb-branch per pre-registered analysis; battery queued.
- @842 [a5_06]: 98 20 62 94 *26* 12 16 00 33 — '[62] ne [26]'
  (gov-frames T3 @841). Verb-branch per pre-registered analysis; battery queued.
- @1707 [a8_06]: 20 62 94 88 *26* 12 06 29 40 — 'ne [88] [26]'
  (gov-frames T3 @1706). Verb-branch per pre-registered analysis; battery queued.
- @531 [a3_01]: 44 59 37 64 *26* 32 16 08 24 — 'qui [26] [32]'. Compatible
  with verb-branch ('qui' as relative-clause subject + [26-verb] +
  [32-adj] predicative complement, parallel to granted 'qui est 32' x2);
  left as verb-branch residual for follow-up (32's verb/noun tension per
  battery-adj-32 also lives here).
- @1470 [a7_10]: 21 02 62 38 *26* 12 41 53 60 — '[62] [38] [26] n[41]...'.
  Verb-branch-compatible only if 38 takes a subject-parse; 38's value is
  open. Fenced as verb-branch residual.
- @1753 [a8_08]: 34 07 28 89 *26* 24 85 58 17 — '[89] [26] [24] [85]'.
  Ambiguous until 89's value resolves (A8 grants 80/89 verb-frames, 89 not
  verb-locked). Fenced as verb-branch residual.
- @406 [a2_08]: 88 53 34 69 *26* 00 33 01 02 — '69 [26] pour dire'
  (trigram, noun26-69-pour-dire T5). Parses under verb-branch
  ('[69] [26-verb] pour dire' purpose-adjunct) once 69 takes subject-parse;
  69's class is queued. Non-discriminating; fenced.
- @934 [a5_10]: 98 83 56 69 *26* 00 33 21 64 — same trigram, byte-identical
  8-gram '69 26 00 33 21 64 37 01' formula-bound. Same fence as @406.
- @1628 [a8_03]: 33 46 56 69 *26* 00 33 21 64 — same trigram, same fence.

NOUN windows (3), all in the '11 (02)? 26' article slot:
- @129 [a1_03]: 82 48 11 02 *26* 32 96 56 64 — "me la [02-adj] [26-noun]
  [32-adj] par ..." (82-48 = 'me', promoted letter reading). Verb-parse of
  'la [26]' is ungrammatical under banked 11=la. Noun.
- @240 [a2_01]: 98 41 17 11 *26* 12 16 56 43 — "...[41] fois, la [26] n[16]..."
  absolute 'une fois la [N]' construction (finder T4). Verb-parse
  ungrammatical after the banked article. Noun.
- @1560 [a8_01]: 61 40 17 11 *26* 30 06 60 71 — "...fois, la [26] pas...".
  The war's crux: 'la [26]' forces noun; '26 pas' forces verb (pas-frames).
  One window, both readings, both banked.

Predecessor census of 26: 02, 84, 11, 69, 64, 39, 24, 94, 69, 24, 46, 38,
11, 69, 88, 89, 64. Only the 3 noun windows have 11=la in the article slot
(@129: '11 02 26'; @240/@1560: '11 26').

## Per-clause pass/fail
- Clause 1 (one class, all windows parsing): FAIL.
  * 26=verb unconditioned: FAILS at @129, @240, @1560 — verb-parse of
    'la [26]' is ungrammatical under banked 11=la. @1560 is already the
    battery-recorded residual forcing a positional rule (pas-frames bar (e)).
  * 26=noun unconditioned: FAILS at 8 decided/claimed verb windows
    (@655/@992/@1250 '26 pas' x3, @1769 'en ce qui', @155/@601/@842/@1707
    governor frames) — noun-26 unconditioned was already killed at promote
    grade by noun26-pas-frames ('26 30' x4 = '[verb] pas'). No re-litigation.
  * The '26n' one-word rival (12 = final 'n') cannot rescue the umbrella:
    excluded/fenced at the verb windows by noun26-pas-frames (decided
    evidence); at the la-windows it is a queued bar of noun26-la-frames.
    Homophone rescue via 23 is barred by the A2 23~26 split (respected, no
    rescue attempted).
- Clause 2 (positional rule stated): PASS (stated, not declared).
  Rule: **26 = feminine noun in the article slot '11 (02)? 26'
  (@129/@240/@1560); 26 = verb-class elsewhere (14 windows).**
  Under this rule all 17 windows receive a stated class; 16/17 parse cleanly
  (verb windows per standing verdicts + gov-frame analyses; noun windows
  @129/@240 parse as article+noun under banked 11=la). The one exception is
  @1560: the rule assigns noun to 'la [26]' but leaves 'pas' unaccounted —
  '...fois, la [26-noun] pas' needs a clause boundary or elliptical matrix
  the battery cannot pin. @1560 is the adjudication-grade residual the rule
  inherits.
  Per protocol section 7, 67 et/veut is the sole true polyvalence; declaring
  a second polyvalence for 26 is a red-team act. This battery STATES the
  rule with its full 17-window evidence and its polyvalence cost, and
  ESCALATES it to the red team. It does not declare or promote the rule.

## Adverses answered
- "one reading must give": neither one-class reading survives; the positional
  rule gives each reading its slot (@129/@240/@1560 noun, 14 verb-branch).
- "26~23 SPLIT granted (A2), no homophone rescue via 23": respected
  throughout; the split is untouched and no rescue was attempted.
- "the queue also holds ... two queued follow-ups": noun26-gov-frames and
  noun26-la-frames remain queued; their bars were not re-litigated and their
  outcomes (when run) feed the red-team adjudication of this rule.

## Verdict: NULL
One-class resolution is falsified (Clause 1 FAIL at kill grade on both sides).
The positional rule is stated with full evidence (Clause 2 PASS as a finding)
but its declaration would violate section 7's sole-polyvalence rule, so the
battery cannot promote it — red-team adjudication required. Headline for the
red team: noun-26's umbrella resolves to a positional noun/verb rule needing
the lane's second declared polyvalence, with @1560's 'pas' as the residual.

## Follow-up targets (null-regeneration)
1. noun26-1560-pas — bar: state ONE parse of repaired @1560
   '...fois, la [26-noun] pas' under the positional rule (clause boundary
   before 'pas', or elliptical matrix licensed by the 1840s register), with
   'pas' accounted; or record @1560 as the adjudication-grade residual for
   the red team with the exact unparsable span named. Resolves the crux the
   rule inherits.
2. noun26-residual-adjud — bar: under the verb-branch of the stated rule,
   @531 ('qui 26 32'), @1470 (38-gated), @1753 (89-gated) each parse with
   the blocking neighbor's class stated, or are fenced with stated cause.
   Resolves the 3 non-formula verb-branch residuals.
3. noun26-26n-exclude — bar: at the 3 la-windows (@129/@240/@1560), exclude
   the '26n' one-word rival (12 = final 'n') with a window-level
   boundary test (12='n' letter is promoted, so the word-boundary decision
   is contact-testable), or fence it. Closes the la-side adverse inherited
   from the pas-frames and la-frames bars.

## Standing constraints observed
- Banked pencil values used; 47='ce' allophone tier noted; provisional 59/77
  not load-bearing (no window's class assignment depends on them).
- A2 23~26 split, noun26-pas-frames PROMOTE, noun26-encequi-triple PROMOTE
  respected; no standing verdict overwritten or downgraded.
- Section 7 sole-polyvalence rule respected: rule stated and escalated, not
  declared.
- No data invented: every number traces to the repaired stream; window
  census n(26)=17 re-derived independently of the A2 count.
