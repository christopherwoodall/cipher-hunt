# Battery `24-en-verb-conflict` — verdict: NULL (escalate to red team)

Target: adjudicate the standings conflict blocking 58's classification:
ne-24-profile (2026-10-08, promote: 24 = finite modal verb, class-level)
vs en85-gerund-reaudit (2026-10-08, promote: "24-85" gerund frames with
24='en', A3 GT) + ant-58-ending's use of 24='en' (2026-10-09, kill).
Date: 2026-10-09. Worker: agent f4b8ef2f-ddb5-4960-8205-c0b9782c22a1.
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py`; 1,847 pairs re-derived in-work,
n(24) = 52 re-derived). `canonical.py` never used. R5005, sealed gate
instances, red-team adjudication queue untouched. Lock
`code/crowd17/next-token/locks/24-en-verb-conflict.lock` created on start
(2026-10-09T06:46:01Z); no prior/stale lock existed; deleted on completion.

Indexing: @-offsets are 0-based pair indices of **24** (ne-24-profile /
cede-614-subject convention). For the five 24-85 bigrams, 85 sits at @+1
(en85-gerund-reaudit used 85-position convention: its @733/@956/@1439/
@1694/@1755 = my @732/@955/@1438/@1693/@1754).

## Bar (verbatim, pre-registered BEFORE testing)

"determine whether 24='en' survives at any window or 24=verb wins globally
(section-7: 67 sole polyvalence bars both); state the consequence for the
five 24-85 windows and for 58 at @1695/@1756"

Numbered clauses (fixed BEFORE the stream census, not modified after):

- **C1:** Determine whether 24='en' survives as a global value (all 52 windows).
- **C2:** Determine whether 24=verb (finite modal verb, ne-24-profile's
  class claim) wins globally.
- **C3:** State the consequence for the five 24-85 windows
  (@732, @955, @1438, @1693, @1754).
- **C4:** State the consequence for 58 at @1695/@1756 (0-based; 1-based
  @1696/@1757).

Standing values used: pencil 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted 87=ce, 64=qui, 96=par, 17=fois, 79="tout" (A5), 00="pour" (A9),
84="on" (A15), 47="ce" (A4 allophone tier); provisional 77=le, 59=est;
frames 85 verb-stem (A3), 37/32/42 predicative (A1); HOLD 45="ce" (A11);
§7 sole true polyvalence (67 et/veut). 1841 diplomatic French throughout.
"en" tested in BOTH its functions (adverbial-pronoun "en" and preposition
"en"); a kill of 24='en' at a window requires BOTH functions ungrammatical.

## Method

1. Re-derived the repaired stream byte-exact per `repair_parse.py`; extracted
   all 52 windows of 24 (±4 census, ±10 for discriminating windows).
2. For each discriminating window, tested three parses: 24='en' as
   pronoun (preverbal clitic: must immediately precede a verb; gerund
   "en [V]"), 24='en' as preposition (needs NP complement), 24=finite verb
   (needs an overt subject; French has no pro-drop; "que"+finite needs a
   subject after "que").
3. A window kills a GLOBAL claim iff the reading is ungrammatical there with
   no rescue under standing values (same kill logic as ant-58-ending's
   @1203 kill).

## Window-level evidence — the 'en'-kill set (C1)

Six windows where 24='en' is ungrammatical in EVERY function. In each,
24 is followed by 87='ce' (granted), which is not a verb (kills pronoun
"en") and not an NP complement (kills preposition "en": "en ce moment"
needs the noun; bare "en ce" is ungrammatical):

- **@162** (a1_05): `35 93 52 94 [24] 87 11 24 82 84 53 12` — "ne [24] ce".
  Pronoun: "n'en ce" — "en" must precede a verb; 87='ce' is not one. Dead.
  Preposition: "ne" negates a verb; no verb adjacent ("en cela" cannot
  intervene between "ne" and its verb). Dead. Rescue via "en" attaching to
  a later verb across "cela": clitics cannot skip. Dead. Imperative "en"
  (postverbal): order wrong. Dead. Verb parse ("ne [24]", lone-"ne",
  author's 34/37 norm): clean.
- **@1774** (a8_09): `37 78 62 94 [24] 87 64 59 19` — same "ne [24] ce"
  shape; 62 subject-shaped (nest-subject, promoted). 'en' dead both
  functions, same causes as @162. Verb parse clean.
- **@1486** (a7_10): `62 46 77 84 [24] 87 08 31 92` — "que l'on [24] ce".
  Pronoun: "l'on en ce" — "en"+"ce" ungrammatical. Preposition: "en"+bare
  "ce" ungrammatical. Verb ("que l'on [24]", subject "l'on"=77+84): clean.
- **@190** (a2_00): `33 16 00 66 [24] 87 98 56 47` — "[24] ce [98]" under
  "pour(00) [66]". "en ce [98]": pronoun dead ("en"+non-verb), preposition
  dead (bare "ce"). No verb anywhere in the window for "ne"-less rescue;
  "en" attaches forward only, to 87='ce'. Dead.
- **@643** (a4_02): `77 89 48 20 [24] 87 61 88 77` — "[24] ce [61]".
  "en ce": dead both functions, same causes. No verb in window.
- **@823** (a5_05): `78 40 95 13 [24] 87 59 38 82` — "[24] ce est(59)".
  "en ce est": dead both functions, same causes.

Fenced (NOT in the kill set): @73 ("[14] en cela pour la" — preposition
"en cela" grammatical, so en-prep survives; en-pronoun dead), @829
("en cela" preposition survives), @179 ("en ce qui [23]" possible iff 23
verb-shaped — 23 open), @1766 (same iff 26 verb-shaped — noun-26 null
leans against), @311/@474 ("qu'on en [37]" — en-pronoun dead, 37 is
A1-predicative not a verb; en-prep strained iff 37 adjectival).

## Window-level evidence — the verb-kill set (C2)

Four windows where 24 CANNOT be a finite verb (no overt subject available;
French has no pro-drop; "que"+finite requires a subject after "que"):

- **@955** (a6_00): `86 96 87 46 [24] 85 04 20 67` — "par ce que [24] [85]".
  Verb: "que [finite]" with no subject — ungrammatical. Rescues: subject
  = 86 (sits before "par ce que"; the subordinate clause still lacks one);
  inversion (no postverbal pronoun; 85 is verb-stem, A3); "que" as
  "ne...que" (no 94); 24 as infinitive/participle ("que"+non-finite
  ungrammatical). All dead. 'en'-pronoun: "par ce qu'en [85]" — clean
  gerund (en85 CONFIRM, undisturbed). 'en'-preposition: "qu'en [85-stem]"
  dead (prep+verb ungrammatical) — irrelevant, pronoun wins.
- **@1693** (a8_06): `14 60 27 46 [24] 85 58 15 23` — "que [24] [85] [58]".
  Same as @955: no subject ("que [subject] [verb]" violated; 85 verb-stem
  cannot be an inverted subject). Verb dead. 'en'-pronoun: "qu'en [85]
  [58]" — clean gerund (en85 CONFIRM, undisturbed).
- **@1438** (a7_08): `64 52 82 16 [24] 85 01 52 68` — "m'[16] [24] [85]".
  82='m' (pencil): clitic "m'" forces 16 verb-shaped (en85's clitic
  entailment; "m'" may precede finite or infinitive, either way 16 is a
  verb). Two verbs (16, 24-finite) adjacent with no subject for 24:
  ungrammatical. Subject candidates: 64='qui' (already subjects 52 or 16's
  clause; cannot reach across to 24); 82='m' (accusative). Verb dead.
  'en'-pronoun: "m'[16-verb], en [85]" — clean gerund (en85 CONFIRM,
  undisturbed).
- **@732** (a5_02): `86 48 88 11 [24] 85 93 76 18` — "[88] la(11) [24] [85]".
  Subject candidates for finite 24: 11='la' (accusative, cannot subject);
  88 as verb ("[88] la" = verb+object, then 24 starts a subjectless clause);
  88 as nominal ("88 la" = determiner after noun, ungrammatical); 86/48
  wider ("[86/48] [88-verb] la | [24] [85]" — 24 still subjectless). Verb
  dead. 'en'-pronoun: gerund "en [85]" or "l'en"+finite-85 — BOTH of en85's
  fenced rivals at @733 use 24='en'; 'en' survives here.

Fenced: @547 ("que [24] ce que" — verb dead, no subject; en-pronoun dead
"en"+"ce"; en-prep "qu'en ce que [clause]" possible iff 55-81 form a
clause — uninterpretable at battery grade, residual, NOT a verb leg);
@806/@807 (24-24 doubling: formula/list, cf. ne-24-profile fence).

## Per-clause results

- **C1: FAIL.** 24='en' does NOT survive globally: killed at kill grade at
  6 windows (@162, @1774, @1486, @190, @643, @823), 'en' ungrammatical in
  every function at each, no rescue under standing values. (One
  incompatible window falsifies a global claim — ant-58-ending precedent;
  §7 bars battery-level polyvalence as the escape.)
- **C2: FAIL.** 24=verb does NOT win globally: killed at kill grade at 4
  windows (@955, @1693, @1438, @732), no subject available for a finite 24
  at each, all rescues exhausted.
- **C3: answered.** The five 24-85 windows, 24-positions @732/@955/@1438/
  @1693/@1754 (85 at +1):
  - @732: 'en' parses (gerund AND "l'en"+finite-85 — en85's fenced
    ambiguity stands undisturbed); verb dead (no subject).
  - @955: 'en' parses ("qu'en [85]", en85 CONFIRM stands); verb dead.
  - @1438: 'en' parses ("en [85]", en85 CONFIRM stands); verb dead.
  - @1693: 'en' parses ("qu'en [85] [58]", en85 CONFIRM stands); verb dead.
  - @1754: THREE parses survive — (a) gerund "[26] en [85] [58]";
    (b) modal "[26-subj] [24] [85-inf] [58]" iff 26 nominal;
    (c) pronoun+finite "[26-subj] en [85-finite] [58]" iff 26 nominal and
    85 finite-capable (A3 is frame-level; en85 notes finiteness contradicts
    nothing granted). The ONLY 24-85 window where the verb reading survives.
  - Net at the bigrams: 'en' wins 4, verb wins 0 outright, 1 ambiguous —
    but 'en' is dead globally (C1), so the five windows do not generalize.
    en85-gerund-reaudit's promote is UNDISTURBED (all 4 CONFIRMs still parse
    under 24='en', which survives at those windows); only the UNIVERSALITY
    of A3 "24=en" is fenced.
  - ne-24-profile's promote is NOT downgraded by this battery (never
    downgrade a standing verdict), but its evidence census is now: "que 24"
    x3 → x0 (@547/@955/@1693 all dead as finite slots); "24->85" x5 → x1
    (@1754 only); surviving verb legs include "qu'on 24" x2 (@311/@474, via
    w1-314-ambig forks), "que l'on 24" x1 (@1486), "ne 24" x2 (@162/@1774),
    24->89 x3, 24->80 x2, 24->82->16 x2, 24->30 x3, clause-final 24-87 x10.
- **C4: answered.**
  - @1695 (0-based; 1-based @1696): `46 [24] 85 [58] 15` — the modal parse
    is dead here (C2: no subject after "que"); ant-58-ending already killed
    the 'ant'-ending rival. SOLE surviving parse: "qu'en [85] [58]" —
    gerund + complement. **58 sits in complement (nominal) position** at
    @1695. This constrains, but does not by itself name, 58's class
    (cede-614-subject's distributional anti-noun evidence stands
    unrefuted; complement position is a new pro-nominal datum for the
    red team / 58-noun-adjudicate).
  - @1756 (0-based; 1-based @1757): `26 [24] 85 [58] 17` — all three @1754
    parses survive; 58's role unresolved pending 26's class and 85's
    finiteness. No constraint beyond the status quo.

## Adverses

- "red-team venue likely": ANSWERED and CONFIRMED. The evidence has exactly
  the shape §7 reserves for the red team: two 2026-10-08 battery promotes,
  mutually exclusive as global claims, each with kill-grade exclusive
  windows (6 for 'en'-kill, 4 for verb-kill), and battery-level polyvalence
  barred (67 sole polyvalence). The decision — (a) scope ne-24-profile's
  verb to non-gerund windows and fence A3 "24=en" to gerund windows
  (de-facto polyvalence needing a 67-style positional rule), or (b)
  downgrade one promote — is escalated, not taken here.
- "both standings are promotes from 2026-10-08": honored — NEITHER
  downgraded by this battery. en85-gerund-reaudit's 4 CONFIRMs and
  ant-58-ending's kill (@1203) and its two legs (@1696/@1757, where 'en'
  survives) are all undisturbed. ne-24-profile's promote stands; only its
  evidence census is corrected (C3) for the red team's use.

## Verdict: NULL — escalate to red team (headline)

Not "inconclusive" epistemically: the window-level finding is definite
(mutual kill: 6 windows kill 24='en', 4 windows kill 24=verb, §7 bars the
polyvalence synthesis). It is null because the DECISION the bar poses
("which wins globally") has no battery-grade answer — both candidates are
dead, and the remaining moves (scoped/downgraded promotes, or a 24
polyvalence with positional resolution) belong to the red team. Per §5, no
standing verdict was overwritten.

## Follow-ups proposed (for supervisor queuing)

1. `24-redteam-adjudication` (P1, **venue: red team — not a battery
   target; supervisor routes, do not dispatch a worker**). Package: the 6
   'en'-kill windows (@162, @1774, @1486, @190, @643, @823) vs the 4
   verb-kill windows (@955, @1693, @1438, @1754-positions @732/@955/@1438/
   @1693); corrected ne-24-profile evidence census (C3); downstream impact
   note — EITHER downgrade disturbs consumers (ne-24-profile feeds
   disc-01-24-ci-X, w1-314-ambig; A3 "24=en" feeds en85's frame and
   ant-58-ending's two legs). Bars: red team to rule (a) scoped promotes,
   (b) single downgrade, or (c) 24 polyvalence with a 67-style positional
   resolution rule.
2. `58-complement-1695` (P3) — @1695's sole surviving parse is "qu'en [85]
   [58]" (gerund + complement); @1754's gerund parse agrees. Test 58's
   nominal-hood from complement position at these two windows. Bars:
   promote 58-nominal iff ≥2 independent complement/determiner slots
   confirm AND cede-614-subject's zero-determiner-predecessor evidence is
   answered; kill iff any complement window forces non-nominal. Coordinate
   with (do not duplicate) cede-614-subject's `58-noun-adjudicate`.
3. `26-class-1754` (P3) — @1754 is the only 24-85 window where the modal
   reading survives; 26's class decides between 1 surviving parse (gerund,
   if 26 non-nominal) and 3 (if 26 nominal-subject-shaped). Bars: name 26's
   class with ≥2 independent frame-legs; state which @1754 parses survive
   as a stated consequence. Do not duplicate noun-26.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-24-en-verb-conflict.md` (this file).
- Queue: `24-en-verb-conflict` queued → verdict/null via temp-file + rename,
  own entry only; pre-write assert confirmed no prior verdict (was JSON
  null); JSON re-validated post-write.
- Lock `24-en-verb-conflict.lock`: created on start, deleted on completion.
- R5005, sealed gate instances, red-team adjudication queue untouched.
