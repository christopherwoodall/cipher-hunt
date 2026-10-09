# Battery report: noun26-residual-adjud

Date: 2026-10-09. Worker: subagent 52848e8e-a8e5-4694-afa1-1514870dddd5.
Target id: `noun26-residual-adjud` (priority 3).
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed byte-exact like
`code/side-keyhunt/repair_parse.py`; 96 distinct pairs verified).
Never canonical.py. Never R5005.

## Bar (verbatim, pre-registered before testing)

"under the verb-branch of the stated positional rule, @531 ('qui 26 32'),
@1470 (38-gated), @1753 (89-gated) each parse with the blocking neighbor's
class stated, or are fenced with stated cause"

OFFSET CONVENTION: this battery's @-offsets are 0-based repaired-stream
indices of the 26 token (the noun-26 umbrella convention), NOT the
@ = 0-based − 1 lane convention used by pas-frames/la-frames. Verified:
the 26 token sits at 0-based 531/1470/1753 in the three windows below.

## Bar restated as numbered pass/fail clauses

1. @531 (0-based 531, 'qui 26 32'): the window parses under the
   verb-branch with the blocking neighbor's (32's) class stated, or is
   fenced with stated cause.
2. @1470 (0-based 1470, 38-gated): the window parses under the
   verb-branch with 38's class stated, or is fenced with stated cause.
3. @1753 (0-based 1753, 89-gated): the window parses under the
   verb-branch with 89's class stated, or is fenced with stated cause.

Adverses (from queue): "38's and 89's values open (not re-litigated;
class stated or fenced only)".

## Method

Rebuilt the stream from the two primary sources with the repair script's
byte-exact tokenizer. Re-derived all three windows by content match;
ran full censuses of 38 (n=7), 89 (n=14), 24 (n=52) and the bigrams
'64 26' x2, '26 32' x2, '89 26' x1, '26 24' x1, '38 26' x1, '62 38' x1,
'26 12' x4, '77 89' x2, '59 38' x1, '38 30' x1, '24 89' x3.
Standing inputs (cited, not re-litigated): the stated positional rule
(26 = feminine noun iff determiner phrase headed by 11='la', else
verb-class; stated by battery-noun-26, declared by red team only);
64='qui' (promoted); 32 predicative-class (A1 grant: 59->32 x3,
'qui est 32' x2 @314/@1208); 26='est' killed globally (la-frames cl.4);
24 = finite verb, modal-shaped (ne-24-profile PROMOTE, class-level);
85 verb-stem frame (A3); 62's class from collision-62-84 (62='on'
unconditioned KILLED; 62='il' demonstrated, not promoted); 30='pas',
94='ne', 12='n'/48='e' battery-promoted pending ratification;
59='est', 77='le' provisional. §7 sole-polyvalence rule respected
throughout (no polyvalence declared).

## Window-level evidence

### Clause 1 — @531 (0-based 531, row a3_01): "44 59 37 64 *26* 32 16 08 24"

26's left neighbor is 64='qui' (promoted), not 11 → verb-branch per the
stated rule. '64 26' occurs exactly 2x stream-wide: 0-based 530-531
(this window) and 0-based 1768-1769 (the encequi-triple window, 26 =
verb decided). Consistent.

'26 32' occurs exactly 2x stream-wide, one per branch — a minimal pair
for the positional rule: 0-based 129 ('11 02 26 32', noun-branch,
la-frames @128) vs 0-based 531 ('64 26 32', verb-branch, this window).

Parse: "qui [26-verb] [32]" = relative clause ("qui" subject +
finite verb) with 32 as manner-adverbial adjective — grammatical
French (idiom class: "chanter faux", "voir clair", "parler vrai",
"coûter cher"). Blocking neighbor 32's class stated: predicative /
adjective per the A1 grant (59->32 x3; 'qui est 32' x2 controls
re-derived by la-frames cl.4). The manner-adverbial slot is a
secondary extension of 32's granted predicative class, stated as such.

- 26='est' is killed globally (la-frames cl.4), so the "qui est 32"
  copula reading is unavailable; 26 is a lexical verb here.
- The adj-32 'qui 32' verb-tension (@33/@855, adj-32 NULL) does not
  live at this window: there 32 follows 'qui' directly; here 32
  follows 26. No transfer.
- Conditional noted (not verdict-bearing): queued `verb-32` — if it
  promotes 32=verb-form, @531 re-opens ("qui [26-modal?] [32-inf]"
  is unevidenced) and this clause's pass is void.
- Caveat: 26's and 32's values are unnamed; the specific lexical
  pairing is unverified. Class-level parse only, which is what the
  bar requires.

### Clause 2 — @1470 (0-based 1470, row a7_10): "21 02 62 38 *26* 12 41 53 60"

26's left neighbor is 38 (not 11) → verb-branch. The gate is 38's
class. '62 38' and '38 26' are both hapax (0-based 1468-1470).

38 census (n=7, zero battery profiles on record):
- 0-based 384 (a2_07): "82 16 52 *38* 37 43 91"
- 0-based 826 (a5_06): "24 87 59 *38* 82 01 24" — '59 38': predicative
  slot after 59='est' (PROVISIONAL), i.e. predicative-class cue; an
  alternative subject-parse ("[38] me[82]…", new clause) is available,
  so the cue is weak.
- 0-based 1113 (a6_07): "73 41 65 *38* 30 69 11" — '38 30': pas-adjoined,
  '[verb] pas'-shaped parallel to the promoted '26 30' (65 is
  noun-shaped per prof-65 PROMOTE, so "[65] [38] pas" = S-V-pas);
  verb-form cue, with the bare-'pas' caveat (flagged to ne-alone-02-74).
- 0-based 1343 (a7_05): "65 64 52 *38* 47 86 66"
- 0-based 1469 (a7_09): "21 02 62 *38* 26 12 41" — this window's gate.
- 0-based 1650 (a8_04): "31 10 03 *38* 82 16 01"
- 0-based 1828 (a8_11): "86 29 82 *38* 83 24 82"

The contact profile splits: predicative-class ('59 38' @825-826,
weak) vs verb-form ('38 30' @1113-1114, the stronger leg). No single
class is statable without a dedicated 38-profile battery.

Discriminating condition (stated, not decided): '62 38 26' parses
under verb-26 iff 38 takes verb-form as a modal: "[62=il/on]
[38-modal] [26-inf]" ('ne peut [inf]'-shaped; 62's class cited from
collision-62-84, not re-derived). If 38 is predicative-class, the
window is ungrammatical under verb-26 and @1470 becomes a genuine
residual of the positional rule.

Right side '26 12 41' (0-based 1470-1472, one of the four '26 12'
windows): segmentation owned by noun26-26n-exclude (fenced there);
not blocking the 38-gate, recorded here only to scope the fence.

FENCE with stated cause: 38's class is genuinely open (n=7,
unprofiled, split contact). The fence names the exact next battery.

### Clause 3 — @1753 (0-based 1753, row a8_08): "34 07 28 89 *26* 24 85 58 17"

26's left neighbor is 89 (not 11) → verb-branch. The gate is 89's
class. '89 26' and '26 24' are both hapax (0-based 1752-1754).

89 census (n=14), three-way split:
- Noun cue: "77 89" x2 — 0-based 639 (a4_01): "46 60 67 *77* 89 48 20";
  0-based 870 (a5_07): "86 70 87 *77* 89 48 20". "le [89]" article+noun,
  clean — but load-bearing on PROVISIONAL 77='le'.
- Infinitive cue: "24 89" x3 — 0-based 222 (a2_01): "42 16 24 *89* 61";
  0-based 986 (a6_01): "45 01 24 *89* 48"; 0-based 1498 (a7_11):
  "15 59 24 *89* 41". "[24-modal] [89-inf]" modal+infinitive, clean —
  load-bearing on PROMOTED 24=modal (ne-24-profile). This is the
  stronger leg.
- Word-internal rival: '[X]er [89]' x3 — 0-based 275 (a2_03):
  "67 33 29 *89* 84"; 0-based 1377 (a7_06): "00 86 29 *89* 84";
  0-based 1393 (a7_07): "67 86 29 *89* 16". 89 may be a word
  continuation after the 'er' stem marker, not an independent token.
- Remainder: "24 89" done above; 0-based 113 (a1_03):
  "67 93 29 *89* 68"; 0-based 285 (a2_04): "42 48 52 *89* 28";
  0-based 303: "86 91 18 *89* 88".

No single class is statable: noun x2 (provisional-77) vs infinitive
x3 (promoted-24) vs word-internal x3. Note on A8: the A8 verb-frame
grant for 89 is a frame-level grant with value open; nothing here
overturns it — 89's class is fenced as undecided, not granted.

Discriminating condition (stated, not decided): '89 26 24' parses
under verb-26 iff 89 takes the noun/subject reading — "[89-subject]
[26-verb]" with a clause boundary posited before 89 (grammatical
necessity; lane-accepted posit per gov-frames @154, pas-frames
@1559), then a second boundary before 24: "[24-modal] [85-verb-stem]"
(modal+infinitive per promoted 24 + A3 85-frame; "24 85" is 24's #2
successor, x5). If 89 is verb-form, the window needs an unevidenced
89=modal reading ("[89-modal] [26-inf]") and otherwise is
ungrammatical under verb-26 → genuine residual.

FENCE with stated cause: 89's class is genuinely three-way split;
no single class statable; value open per the adverses (not litigated).

## Per-clause pass/fail

1. @531: PASS — parses as "qui [26-verb] [32-manner-adj]" with 32's
   class stated (predicative/adjective, A1 grant); 26='est' killed;
   'qui 32' tension non-transferring; verb-32 conditional noted.
2. @1470: FENCE with stated cause — 38's class genuinely open
   (predicative '59 38' @825-826 vs verb-form '38 30' @1113-1114);
   window parses iff 38=modal ("[62] [38-modal] [26-inf]").
3. @1753: FENCE with stated cause — 89's class genuinely three-way
   split (noun "77 89" x2 vs infinitive "24 89" x3 vs word-internal
   '[X]er [89]' x3); window parses iff 89=noun-subject
   ("[89-S] [26-V]" + boundaries + "[24-modal] [85-inf]").

## Adverses answered

- "38's and 89's values open (not re-litigated; class stated or fenced
  only)": ANSWERED. 38 fenced (class not stated, value untouched);
  89 fenced (three-way split documented, value untouched). Neither
  value litigated; no class granted for either.

## Verdict: NULL

The positive claim — "resolve verb-branch residuals @531/@1470/@1753"
— is not established at battery grade: 1 of 3 windows parses (@531),
2 of 3 are fenced with stated cause (@1470 blocked on 38's class,
@1753 blocked on 89's class). Per the sibling precedent
(battery-noun26-26n-exclude, 2026-10-08: fence disjunct exercised →
"the claim is therefore not established at battery grade" → NULL),
exercising the fence disjunct documents the blocker but does not
establish the claim. The fences above are substantive findings: each
names the exact discriminating condition and the next battery that
unblocks it. No window forces the claim false (not kill); no cleaner
rival demonstrated (not kill); no standing red-team verdict
contradicted (A8's 89 frame-grant untouched — class fenced, not
granted; §7 sole-polyvalence respected — no polyvalence declared).

## Follow-up targets (null-regeneration; for supervisor queuing)

1. noun26-38-profile — bar: state 38's class (n=7, zero prior profiles)
   by adjudicating predicative ('59 38' @825-826, load-bearing on
   provisional 59='est', subject-parse alternative available) vs
   verb-form ('38 30' @1113-1114, '[verb] pas'-shaped, bare-'pas'
   caveat) — stated class or fenced split; unblocks @1470 ('62 38 26'
   parses iff 38 takes the modal reading).
2. noun26-89-class — bar: state 89's class (n=14) by adjudicating noun
   ("77 89" x2 @639/@870, load-bearing on provisional 77='le') vs
   infinitive ("24 89" x3 @222/@986/@1498, load-bearing on promoted
   24=modal) vs word-internal ('[X]er [89]' x3 @275/@1377/@1393) —
   stated class or fenced split; unblocks @1753 ('89 26 24' parses
   iff 89 takes the noun/subject reading).

## Standing constraints observed

- Banked pencil values used; provisional 59/77 flagged wherever
  load-bearing (38's predicative cue, 89's noun cue); promoted 24
  flagged where load-bearing (89's infinitive cue).
- A2 23~26 split, noun26-pas-frames PROMOTE, noun26-gov-frames
  PROMOTE, noun26-la-frames PROMOTE, ne-24-profile PROMOTE,
  collision-62-84 KILL respected; no standing verdict overwritten or
  downgraded. The @531 finding refines rather than overturns the
  umbrella's stated positional rule.
- Section 7 sole-polyvalence rule respected: no second polyvalence
  declared; 89's potential position-dependence flagged as red-team
  territory, not decided.
- No data invented: every number traces to the repaired stream;
  offset convention (@ = 0-based) stated up front.
