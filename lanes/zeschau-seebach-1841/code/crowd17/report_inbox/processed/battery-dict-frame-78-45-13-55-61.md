# Battery report: dict-frame-78-45-13-55-61

Target: `dict-frame-78-45-13-55-61`. Claim: byte-identical 5-gram x2 reads
'verdict [13-55-61]' under 78='ver'+45='dict'.
Date: 2026-10-08. Worker: ddf67f9c-85d2-4fed-90ca-c9fb71b6603c (battery worker).
Lock `locks/dict-frame-78-45-13-55-61.lock` created 2026-10-08T14:59:08Z (no
stale lock; locks dir held NOTE.md plus two other workers' live locks);
deleted on completion.

## Bar (verbatim, pre-registered)

"(a) both windows parse with 13-55-61 named as one unit; (b) @574's '...61 94
82 06' parses as a 'ne me/m'' negation frame; (c) @1165's '21 67' left context
fenced with stated cause"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. Both windows (queue @574/@1165 = stream @573/@1164, 0-based) parse with
   13-55-61 named as one French unit (word).
2. Stream @577-580 ("...61 94 82 06", the queue's @574 window) parses as a
   'ne me/m'' negation frame.
3. Stream @1162-1163 ("21 67", the queue's @1165 left context) is fenced with
   stated cause.

Offset convention: @n below = 0-based pair index in the repaired 1,847-pair
stream. The queue's evidence cites 1-based offsets (@574/@1165); stream indices
are one less (@573/@1164). Verified byte-identical:
seq[573:578] = seq[1164:1169] = ['78','45','13','55','61'].

## Method

Repaired 1,847-pair stream only: `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
(stride-2 pairing per row offset). Verified 1,847 pairs / 96 types before
testing. `canonical.py` never used. R5005 untouched (read-only parse). No
sealed gates, no red-team contact. Every number traces to the stream.

Standing values used (protocol §7 + post-R17): banked GT 11=la, 82=m, 29=er,
40=e, 46=que; granted 87=ce, 47="ce" (allophone tier), 06="ent" (R17-007,
conditional on 94="ne" STRONG LEAD); leads: 78="ver" (R16-005, confirmed
R17-006/R17-021), 94="ne" STRONG LEAD (R17-001), 45="ce/dict" (A11 HOLD +
R16-004 lead); 67 et/veut sole true polyvalence with the positional rule
(67="veut" iff follower infinitive-shaped).

## Window-level evidence

W1 — 5-gram @573-577 (row a3_02):
`@571:52 @572:87 | 78 45 13 55 61 | @578:94 @579:82 @580:06 @581:06 @582:50`
→ "ce(87) verdict(78-45) [13-55-61] ne(94) mentent(82-06-06) …".
87='ce' granted; 78-45 one-word boundary promoted (verdict-w2-574-gate);
94='ne' STRONG LEAD; "ne mentent" granted-conditional (R17-007 — the red team
re-derived this exact frame "61 94 82 06 06 50" @578).

W2 — 5-gram @1164-1168 (row a6_09):
`@1162:21 @1163:67 | 78 45 13 55 61 | @1169:94 @1170:87 @1171:83 @1172:21`
→ "… 21 et/veut(67) verdict(78-45) [13-55-61] ne(94) ce(87) [83] …".
94-87 bigram is stream-unique (1/1847, this window only); "ne ce" is
ungrammatical under 94='ne' + 87='ce' (granted).

13/55/61 contact profiles (re-derived on the repaired stream):
- 13, n=12: suc {24x3, 66x2, 55x2 (the two targets), 93x2, 52x1, 92x1};
  13->55 occurs ONLY in the two 5-grams.
- 55, n=12: suc {81x6, 61x3, 83x2, 68x1}; 55->61 x3 (third @1205:
  "29 45 58 47-43 [55 61] 21 65 …", 47='ce' granted).
- 61, n=18: suc {96x2, 59x2, 94x2 (the two targets), 21x2, 20, 88, 70, 12,
  24, 31, 56, 15, 40}; pred {55x3, 62x2, 89, 37, 20, …} — scattered, no
  dominant class.
- 13-55-61 trigram x2 = exactly the two target windows, zero elsewhere.

## Per-clause pass/fail

1. **FAIL.** 13-55-61 cannot be named as one French unit with evidential
   support: the three contact profiles are scattered and no candidate word
   survives cross-window triangulation (55->81 x6 noun-context vs 55->61 x3
   vs W1's 3pl-subject requirement below). W1's "ne mentent" (3pl, R17-007)
   has no identifiable subject in X or its context ("ce verdict" is
   singular; X unnameable). W2's right context "94 87" = "ne ce" is
   ungrammatical under 94='ne' STRONG LEAD (R17-001) + 87='ce' (granted),
   and 94-87 is a stream-unique bigram (no pattern rescue).
   Not kill-grade: the claim is conditional on unsettled leads (78='ver'
   LEAD, 45='dict' lead) — per the fork-78-45-rerun precedent an unfired
   conditional is null, not kill. The "ne ce" is a 94-problem outside the
   claim's "under 78='ver'+45='dict'" scope, and 94='ne' is STRONG LEAD, not
   grant. No cleaner rival value was demonstrated on the 5-gram frames; the
   one-word 78-45 boundary stands promoted (verdict-w2-574-gate).
2. **PASS (conditional).** Stream @577-581 = 61 94 82 06 (+06 @581):
   "ne mentent" — 94='ne' STRONG LEAD (R17-001), 82='m' banked GT,
   06='ent' granted-conditional (R17-007). The 'ne me/m'' negation frame is
   clean. Caveat per R17-001: downstream of the 94='ne' STRONG LEAD, which
   keeps its stated caveats.
3. **PASS (fence).** Stream @1162-1163 = 21 67 (21->67 x8 stream-wide: 21's
   top successor, 67's top predecessor; sample @109/@115/@505/@850/@1162).
   67='et' by the §7 positional rule: 67="veut" iff follower
   infinitive-shaped; 78 is noun-shaped (16/31 determiner predecessors per
   ver-78/R17-014; the fork battery requires 78 noun-shaped at W4), so
   67='et'. The 'et' coordinates the preceding 21-phrase ("… 44 83 21";
   83's value open, 'de' lead held per R17) with the "verdict [13-55-61]"
   noun phrase. Full parallelism unverifiable — 21's value is open (no
   battery has named it). Fenced with stated cause: 67 forced by the
   positional rule; the blocker is 21's (and 83's) open value, not 67.

## Adverses answered

- "78='ver' queued": answered — 78='ver' is red-team LEAD (R16-005,
  confirmed R17-006/R17-021), examined not unexamined. The claim's
  conditional form ("under 78='ver'") is respected; LEAD is not promotion,
  so the 'verdict' value reading stays conditional and cannot promote at
  battery level (fork-78-45-rerun precedent).
- "does not duplicate dict-45's syllable-profile bar": answered — the
  contact-profile boundary was promoted separately (dict-45-contact-update,
  Fisher p=0.00205 on post-78 4/4 vs standalone 2/18); cited here, not
  re-run. This battery tested only the 5-gram unit bar plus the two scoped
  clauses.

## Verdict: null

Headline: clause 1 unsatisfiable — 13-55-61 unnameable with evidential
support; W1's "ne mentent" subjectless, W2's "ne ce" a hapax anomaly.
Clauses 2 (conditional on 94='ne' STRONG LEAD) and 3 (fenced) pass. No
standing red-team verdict is contradicted (R17-001/R17-006/R17-007,
R16-005, A11 scoping per verdict-w2-574-gate all respected) — no
escalation; the W2 "94 87" hapax is flagged as a 94-frame anomaly for
red-team awareness (follow-up 2).

## Follow-up targets (null regenerates work; all absent from queue, verified 2026-10-08)

1. **name-13-55-61** (priority 2). Claim: 13-55-61 names as one French word
   via cross-window triangulation. Bars: (a) 13/55/61 contact profiles
   stated (13->24 x3, 55->81 x6, 61 scattered n=18); (b) name X iff one
   French word fits both 5-gram windows + the third 55-61 window @1205;
   (c) W1's "ne mentent" 3pl subject identified under the named X.
   Evidence: this report. Adverses: W2 "ne ce" hapax; scattered profiles.
2. **ne-ce-1169** (priority 2). Claim: 94@1169 (stream-unique 94-87 bigram,
   "ne ce") resolves. Bars: (a) census 94's 37 windows; state why 'ne'
   fails or parses at @1169; (b) resolve iff @1169 parses under 94='ne'
   STRONG LEAD with stated cause, or a rival 94-value is demonstrated at
   this window; (c) do not overturn R17-001 (94='ne' stays STRONG LEAD) and
   do not declare a second 94 value without red-team declaration (§7).
   Evidence: this report. Adverses: 87='ce' granted; 94-87 hapax.
3. **w1-573-subject** (priority 3). Claim: W1's "ne mentent" subject
   identified. Bars: (a) parse "ce verdict [13-55-61] ne mentent [50] …"
   with the 3pl subject named and the clause boundary stated; (b)
   coordinate with name-13-55-61 (merge if X is the subject). Evidence:
   this report; R17-007 ("ne mentent" granted-conditional). Adverses:
   94='ne' STRONG LEAD caveat (R17-001).

## Reproducibility

All counts re-derived in-session from the repaired stream (1,847 pairs /
96 types asserted before testing). No analysis script retained — window
dumps and censuses above are the record. No writes outside this report,
the queue edit, and the lockfile (deleted).
