# Battery report: dict-45-w3-ceci

- Target id: `dict-45-w3-ceci`
- Claim: "47-78-45-01 @981-984 reads 'ce verdict-ci' (positive leg for positional 45='dict')"
- Date: 2026-10-08
- Worker: battery worker (session 79ae0a49-74c1-48c9-8c2d-1ae33341ce8d)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
  re-derived in-session: 1,847 pairs / 96 groups confirmed).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/dict-45-w3-ceci.lock (created at start,
  deleted at end; no prior lock existed).
- Scope: W3 of the dict-45 battery family — the single 78-45-01 window
  (@982-984). The other post-78 windows (@313, @573, @1165) are not re-tested
  here; they belong to the proposed follow-up dict-45-circle-break.

## Bar (verbatim, pre-registered before testing)

"(a) 01='ci' coheres with ci-01-value's discriminators (coordinate, do not re-run); (b) the '24 89' ("en [89]") continuation parses after the NP; (c) if 01!='ci', record W3 neutral, not adverse"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (a) 01='ci' coheres with ci-01-value's discriminators: the bound '-ci'
   reading at @984 is not forced false by anything ci-01-value decided.
2. (b) The '24 89' continuation parses after the NP "ce verdict-ci"
   (author's parenthetical gloss: "en [89]").
3. (c) If 01 != 'ci', W3 is recorded neutral for the 45='dict' leg, not adverse.

## Method

1. Re-derived the repaired stream in-session (1,847 pairs, 96 groups).
   Window re-derived, not cited from memory: @978-988 (row a6_01) =
   `92 07 76 47 78 45 01 24 89 48 01`. The claim window @981-984 =
   `47 78 45 01`; continuation @985-986 = `24 89`; @987-988 = `48 01`.
   45-01 occurs exactly once on the stream (@983) — re-derived; matches
   ci-01-value and feeder-ceci-47-45.
2. Tested the claim parse (R1) against standing verdicts only, with every
   dependency stated:
   - 47='ce' (A4, granted, allophone tier)
   - 78='ver' (LEAD; ver-78-rebar NULL, escalated to red team)
   - 45='dict' syllable post-78 (lead R16-004; A11 HOLD has 45='ce';
     dict-45-contact-update battery-PROMOTE of the post-78 contact boundary,
     unratified)
   - 01='-ci' demonstrative suffix (un-named; see bar a)
   - 24='faire' (battery-PROMOTE by disc-01-24-ci-X, UNRATIFIED)
   - 89 = verb-frame (A8 grant)
3. Compared against the rival standing parse (R2) from disc-01-24-ci-X W3:
   45='ce' (A11 HOLD) + 01='en' (battery-PROMOTE, local) + 24='faire' ->
   "ce en fait [89]". Did not re-run either battery; coordinated only.

## Window-level evidence

### The claim parse (R1)

`47 78 45 01 24 89` @981-986 =
"ce(47) verdict(78-45) -ci(01) fait(24) [89-inf]" =
"ce verdict-ci fait [89]" ("this very verdict brings about [89]").

- The NP "ce verdict-ci" is the standard discontinuous French demonstrative
  (ce + N + -ci), not a word-internal composition. '-ci' is the bound
  demonstrative morpheme — the same morpheme as the fenced ceci bound-'-ci',
  here in the post-nominal slot rather than collapsed onto 'ce'.
- "fait [89]": 24=faire (battery-promoted, unratified) as causative +
  infinitive [89] (A8 verb-frame). One of the x3 24->89
  modal/infinitive-frame contacts (@221/@985/@1497). Grammatical.
- Full-window coverage: all six tokens @981-986 parse; zero dangling tokens.
  @980=76 and @987=48 remain outside the claim window (76's value open;
  48's value open) — neither touches the claim.

### Clause 1 — bar (a): coherence with ci-01-value's discriminators

ci-01-value killed GENERAL 01='ci' at the 01-24 discriminator windows
(@40, @828): "ci" never heads a phrase and never precedes a finite verb;
the ci-compound rescue died under the 24 class grant. Its W3 (@984) was
the ONE surviving 'ci' window: "ce(45)-ci [24]" = "ceci [24]" parses
because bound '-ci' + finite verb is grammatical.

The claim's 01 is bound (demonstrative suffix), not a phrase head. The
discriminators' force was against general/phrase-head 'ci' — they do not
extend to bound '-ci'. At morpheme level the claim coheres with the kill.

Caveat (stated, not hidden): the fenced bound-'-ci' hypothesis
(ci-01-value fence; ci-bound-01 queued NULL; feeder-ceci-47-45 NULL) was
restricted to ce-ADJACENT positions (87-01 x2, 47-01, 45-01@984). The
claim places '-ci' after a noun ('verdict' = 78-45) — a NEW environment.
Same morpheme, new position. The extension is not forced false by any
discriminator, but it carries its own burden: no other "ce N-ci" window
for 01 is on record. Owned by follow-up ci-demonstrative-census.

Grade: CONDITIONAL PASS (morpheme-level coherence holds; positional
extension is new and untested).

### Clause 2 — bar (b): the '24 89' continuation after the NP

Under R1 the continuation parses: "fait [89]" = causative faire +
infinitive complement [89] (A8). "ce verdict-ci fait [89]" is a complete
grammatical clause. Conditional on unratified 24='faire' and A8 — both
stated.

Parenthetical gloss mismatch (recorded, bar not rewritten): the author's
"en [89]" does not occur anywhere under the claim's parse — 01 is '-ci',
not 'en'. The "en" echoes disc-01-24-ci-X's rival frame ("ce en fait
[89]", 01='en' clitic-climbed). If the "en" was substantive rather than
shorthand for the faire+infinitive frame, the bar would be internally
inconsistent (it would require 01='en', contradicting the claim's
01='-ci'). Read as shorthand, the continuation parses.

Grade: CONDITIONAL PASS on the shorthand reading; the gloss mismatch is
flagged above.

### Clause 3 — bar (c): the 01 != 'ci' conditional

01='-ci' is NOT established at battery grade: the rival 01='en' holds a
standing battery-level PROMOTE at this exact window (disc-01-24-ci-X W3,
unratified but un-downgraded), and the '-ci' demonstrative-suffix
environment is new (clause 1 caveat). Per the bar's own conditional, W3
is therefore recorded NEUTRAL for the 45='dict' leg — not adverse, and
not positive either.

## The circularity (headline finding)

This window cannot serve as an INDEPENDENT positive leg for 45='dict':

- The claim's 'verdict' composition is conditional on 78='ver' (LEAD,
  ver-78-rebar NULL escalated to red team).
- ver-78-rebar's two positive 'verdict' legs (@573, @982 — this window is
  @982) are themselves conditional on the 45='dict' lead (R16-004).
- 78='ver' and 45='dict' are mutually conditional AT THIS WINDOW. The
  window was already counted once, conditionally, by ver-78-rebar. It
  adds no new independent support for either value here.

This is fenced, not a kill: no window forces the claim false, and R1
parses with full coverage. But a "positive leg" that re-counts the same
conditional window is not a leg.

## Adverses

1. "all reads conditional on 78='ver' LEAD (ver-78 null)": FENCED with
   stated cause. ver-78-rebar: all three bar clauses passed on the
   repaired stream, but promote would contradict standing red-team
   grading R16-005 (LEAD, not settled) — recorded NULL and escalated.
   The 'ver' read at @982 was one of its two 'verdict' positives,
   conditional on 45='dict'. Mutual conditionality with this claim's
   'dict' leg: see circularity section. Not answerable at battery grade;
   owned by the red team (ver78-45-dependency-gate is queued).
2. "01='ci' un-named": FENCED with stated cause. General 'ci' KILLED
   (ci-01-value); bound '-ci' fenced to ce-contexts and NULL at both
   follow-ups; the demonstrative-suffix environment is new (clause 1);
   rival 01='en' is battery-PROMOTED at this window (disc-01-24-ci-X,
   unratified). Not answerable at battery grade; owned by follow-up
   w3-01-adjudicate.

## Per-clause pass/fail

1. (a) 01='ci' coheres with ci-01-value's discriminators: CONDITIONAL PASS
   (bound morpheme, not the killed general value; new post-nominal
   environment flagged and owned by a follow-up).
2. (b) '24 89' continuation parses after the NP: CONDITIONAL PASS on the
   shorthand reading ("fait [89]", causative + infinitive); the
   parenthetical "en" is unmatched under the claim's parse — flagged,
   not rewritten.
3. (c) 01 != 'ci' conditional: APPLIES — 01='-ci' not established; W3
   recorded NEUTRAL, not adverse.

## Verdict: NULL

R1 ("ce verdict-ci fait [89]") parses with full window coverage and no
window forces the claim false — not kill. But promote is blocked on
three independent grounds: (i) the queue's never-downgrade rule —
promoting 01='-ci' at @984 would downgrade disc-01-24-ci-X's standing
battery promote of 01='en' at the same window; (ii) the
78='ver' <-> 45='dict' mutual conditionality means the window adds no
independent positive leg (it re-counts ver-78-rebar's conditional
positive); (iii) both adverses fence rather than answer. Bar (c) itself
directs the neutral recording. No standing red-team verdict is
contradicted or downgraded (disc-01-24-ci-X is battery-level, not
red-team; A11, A4, A8 relied on, not challenged). No escalation beyond
the existing ver-78 / fork-78-45 red-team items.

## Follow-up targets (nulls regenerate work; none duplicate queued targets —
checked against all 317 queue ids)

1. **dict-45-circle-break** (priority 2): give 45='dict'-syllable an
   independent leg at the post-78 windows where 01 is ABSENT: @313
   (78-45-64), @573 and @1165 (byte-identical 78-45-13-55-61 5-grams).
   Bar: "resolve iff all three compose as ver+dict-syllable with stated
   follower parses (64='qui' promoted; 13-55-61 per
   dict-frame-78-45-13-55-61 — coordinate, do not re-run); kill iff any
   window forces non-dict." Adverses: A11 45='ce' HOLD (positional
   allophone account — state which windows each value owns);
   dict-78-45-wordbound boundary (coordinate). Evidence: this report's
   circularity finding; dict-45-contact-update census (78-45 x4 at
   @313/@573/@982/@1164).
2. **w3-01-adjudicate** (priority 2): resolve 01@984 directly between 'en'
   (disc-01-24-ci-X battery promote) and '-ci' demonstrative suffix (this
   claim), on full-window coverage. Bar: "name 01@984 iff one value parses
   @981-988 with zero dangling tokens and the other leaves >=1 token
   unparsed or needs >=1 extra assumption; the loser is fenced with stated
   cause — no queue verdict is downgraded, this is the adjudication the
   never-downgrade rule requires before either can promote." Adverses:
   78='ver' NULL (both readings conditional — state the dependency, do
   not re-litigate); §7 sole-polyvalence (exactly one value may win).
   Evidence: this report (R1 vs R2); disc-01-24-ci-X W3.
3. **ci-demonstrative-census** (priority 3): test whether bound '-ci'
   occurs outside ce-adjacent positions. Census all 28 windows of 01 for
   "ce ... N-ci" demonstrative frames (01 not adjacent to the opening
   ce-token 47/87/77/11, inside an NP it closes). Bar: "name the
   demonstrative-suffix environment iff >=2 additional windows parse as
   'ce N-ci' with stated NP boundaries; else fence @984 as the unique
   '-ci'-after-noun window with stated cause." Adverses: the three
   01='en' windows (disc-01-24-ci-X — coordinate); ci-bound-01's
   ce-context restriction (coordinate, do not re-run). Evidence: this
   report's clause-1 extension finding.

## Reproducibility

Stream re-derivation: `code/side-keyhunt/repair_parse.py` (`load_rows` +
`parse` with `rep['a5_03']=0`), run in-session 2026-10-08: 1,847 pairs,
96 groups; @978-988 = `92 07 76 47 78 45 01 24 89 48 01` (row a6_01);
78-45 x4 at @313/@573/@982/@1164; 45-01 x1 at @983. No writes outside
this report, the queue entry, and the lockfile.
