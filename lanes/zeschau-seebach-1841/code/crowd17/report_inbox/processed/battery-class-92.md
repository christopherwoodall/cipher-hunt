# Battery report: class-92 — 92's class from its 22-window profile

- Target: `class-92` (claim: "92's class is named from its 22-window profile")
- Worker: d80b9d83-903b-482b-82a1-6b4c524f2472
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed like `repair_parse.py`)
- Lock: `code/crowd17/next-token/locks/class-92.lock` (created 2026-10-08T11:06:04Z, no prior lock)

## Bar (verbatim, pre-registered before testing)

"name 92's class iff >=3 windows parse under it with zero forced contradiction; result feeds queued prenne-70-12-94's subject search (92 follows @1548)"

Restated as numbered pass/fail clauses:

- **C1**: ≥3 of 92's 22 windows parse under the named class (parse = grammatical French under standing values, assuming only the class itself).
- **C2**: zero forced contradiction — no window in the 22 forces the class false under standing values.

## Method

Re-derived the full 22-window profile on the repaired stream (did not reuse the finder's counts).
n(92) = 22 at @49, @66, @203, @321, @330, @354, @356, @593, @683, @901, @978,
@1022, @1154, @1218, @1310, @1361, @1379, @1453, @1490, @1550, @1607, @1673.
Predecessors: 00x6, 11x3, 94x2, 84x2, plus 9 singletons (40, 98, 16, 83, 30, 13,
46, 31, 81). Followers: scattered, max 2x (79, 69, 60, 64, 62) — matches the
queue evidence exactly. Tested candidate classes NOUN / INF / VFIN /
VERB-umbrella / CLITIC / ADJ against standing values (§7: 11=la, 00=pour,
84=on per A15 + collision battery 2026-10-08, 94=ne, 64=qui, 46=que, 29=er,
40=e, 79=tout, 47=ce; 67 sole true polyvalence).

## Window-level evidence (@-offsets)

Governor groups (pre → 92):

- **00x6** (`pour`): @49, @330, @593, @978, @683, @1154.
  - '00 92 79' x2 (@49, @593). '96 00 92' only @49 ("par pour [92]" anomalous
    under 00='pour' — 00's problem / A14 set-level frame, values not named;
    not counted against 92's class).
  - @1154: '00 92 29' = "pour [92]er" — 92 takes the -er infinitive ending
    (A10 composition). 92 is verb-stem-shaped here. This is the strongest
    single window in the profile.
  - @683: '00 92 64 29 40 65' = "pour [92] qui er e [65]" — the A6 frame
    ([09/92]-qui-er-e-65). Fenced: value killed, not re-litigated; class-parse
    marginal under every candidate.
- **11x3** (`la`): @203, @321, @1607 ('la [92] [63]' / 'la [92] [60]' /
  'la [92] [65]'). As article + infinitive: ungrammatical (substantivized
  infinitive is masculine). As article + noun/adjective: clean. As object
  clitic + finite verb ("la [V]"): clean.
- **94x2** (`ne`): @66, @1550 — closed set confirmed, no other 94→92
  stream-wide. But @1549's 94 is word-internal to "prenne" (70-12-94):
  @1550 = '46 70 12 94 92' = "que prenne [92]". Only @65-66 is a true
  ne-governor: @60-66 '08 34 29 40 12 94 92' = "[08] i er e n ne [92]"
  (R-enne-61 residual neighborhood; "ne [92]" parses as ne-explétif/literary
  under VERB, ungrammatical under NOUN).
- **84x2** (`on`, holds unconditioned per collision battery): @1022, @1379.
  "on [92]": forces verbal (finite verb or clitic); "on"+noun ungrammatical.
  - @1022: '84 92 64 45 64' = "on [92] qui ce qui" — anomalous under ALL
    classes (verb+"qui" / "on"+noun both ungrammatical). Fenced as residual
    R-class92-1022; red-team eyes.
  - @1379: '89 84 92 69' = "[89] on [92] [69]" — clean under VFIN.
- **Singletons**: @354 '40 92' (40='e' letter; segmentation open — fenced for
  seg battery, not counted as contradiction); @356 '98 92 47' (98 open);
  @901 '16 92 67' (16 open); @1218 '83 92 61' (83 fenced blocker per
  le83-window battery); @1310 '30 92 44' = "pas [92]" (parses under ADJ,
  strained under others — noted, not decisive); @1361 '13 92 62' (13 open);
  @1453 '46 92 62' = "[veut/dire] que [92] [62]" — clean under V-subjunctive;
  @1490 '31 92 39' (31 open); @1673 '81 92 60' (81 open, noun-81 lead).
- **Followers**: '92 64' x2 (@683, @1022) = "[92] qui" — clean under NOUN
  (relative clause), ungrammatical under VFIN. Scatter otherwise (max 2x):
  the listed adverse is confirmed and neutral.

## Key findings

- **F-a.** Three governors point to three disjoint classes: `pour`→verbal
  (x6, incl. "pour [92]er" @1154), `la`→nominal-or-clitic+verb (x3),
  `on`→finite-verbal (x2), `prenne`→nominal-subject (@1550).
- **F-b.** @1154 "pour [92]er" kills NOUN at kill grade ("pour [N]er" is
  impossible; the -er must compose with 92 as verb stem).
- **F-c.** @1550 "que prenne [92]" kills every verbal class at kill grade
  (verb+verb ungrammatical); 92 must be nominal here — specifically an
  inverted subject ("que prenne [92-S]", literary pattern "que vienne le
  jour"). Coordination note for queued prenne-92-noun: the nominal parse is
  inverted-subject, NOT V+direct-object with open S (their bar's DO reading
  leaves the subject slot ungrammatical — recommend re-bar).
- **F-d.** '84 92' x2 kills NOUN ("on"+noun ungrammatical; 84='on'
  unconditioned).
- **F-e.** '11 92' x3 kills whole-word INF as article+infinitive (3 windows).
- **F-f.** '00 92' x6 kills VFIN ("pour"+finite verb, 6 windows).
- **F-g.** No candidate survives C2 (see per-candidate table). The profile is
  genuinely tripartite; under §7 (67 sole true polyvalence) a battery cannot
  declare 92 split or polyvalent.

## Per-candidate clause results

| candidate | C1 (≥3 parse) | C2 (zero forced contradiction) |
|---|---|---|
| NOUN (fem.) | PASS ('la' x3, @1550 subject, '92 qui' x2) | **FAIL** — @1022/@1379 "on [N]", @66 "ne [N]", @1154 "[N]er" |
| INF (whole-word) | PASS ('pour' x6) | **FAIL** — 'la' x3 (article+INF), 'on' x2 |
| VFIN | PASS ('on' x2, @1453, @66) | **FAIL** — 'pour' x6 |
| VERB-umbrella (stem/inf/fin) | PASS | **FAIL** — @1550 verb+verb |
| CLITIC | PASS ('on' x2, 'pour' x6 "pour le V", @66) | **FAIL** — 'la' x3 ("la le"), @1550 |
| ADJ | borderline PASS ('la' x3 substantivized) | **FAIL** — 'pour' x6, 'on' x2 |

The bar's iff is not met by any class: no class is named.

## Verdict: NULL

92's 22-window profile forces disjoint classes at disjoint governor sets.
This does not contradict any standing red-team verdict: A14 granted 92 only
set-level INF-signal ("genuinely ambiguous"); A6's '-ère' value kill is
untouched (@683 fenced, never re-valued); the 09~92 HOLD is untouched.

## Follow-up targets for the supervisor (null regeneration)

### F1 — id "verb-92-subset" (priority 2)
- claim: "92=verb (stem/inf/fin per governor) on its verbal-governor subset"
- evidence: "'pour [92]' x4 (@49/@330/@593/@978) INF; @1154 'pour [92]er' stem (smoking gun); @1379 'on [92]' VFIN; @1453 'que [92]' V-subjunctive; @66 'ne [92]' V (explétif). @1022 and @683 fenced as residuals (anomalous under all classes / A6 frame)."
- adverses: "nominal governors ('la' x3, 'prenne' @1550) fenced as the split question for red team — this battery tests the verbal subset ONLY, never the global class; coordinates with queued prenne-92-noun (noun arm), does not duplicate it."
- bars: "name 92=verb on the subset iff >=3 subset windows parse with zero forced contradiction within the subset (fenced residuals excluded); any new forced contradiction kills the subset claim."

### F2 — id "split-92-adjudication" (priority 1)
- claim: "red team adjudicates 92's tripartite governor profile: split/polyvalence declaration vs governor misread"
- evidence: "full window table from this report: {00x6}->verbal (incl. @1154 stem), {11x3}->nominal, {84x2}->finite-verbal, {@1550}->nominal-subject; §7 sole-polyvalence (67) blocks battery-level split; @1022 residual anomalous under all classes."
- adverses: "A14 set-level INF-signal; queued prenne-92-noun (coordinate, do not duplicate); 92's killed '-ere' value stays killed."
- bars: "red-team adjudication only — battery may gather windows, never decide the split."

### F3 — id "seg-92-354-356" (priority 3)
- claim: "@354/@356 '40 92 98 92' segmentation resolves (word-internal vs two-word)"
- evidence: "@354 '40 92' (40='e' banked letter directly before 92); @356 '98 92 47'; 92's only self-adjacent windows ('92 98 92' sandwich)."
- adverses: "92's killed '-ere' value NOT re-litigated — segmentation only; 98 open."
- bars: "resolve iff one segmentation parses both windows with <=1 non-granted value assumption; else fence."

## Coordination outputs (for sibling targets)

- For queued **prenne-70-12-94**'s subject search: subject found — 92 itself,
  postposed/inverted at @1550 ("que prenne [92-S]"). Their "unresolvable"
  is resolved as inversion.
- For queued **prenne-92-noun**: do not duplicate its value arm; note only
  that its bar's "@1545 reads 'pour que [S] prenne 92' (V + direct object)"
  should be re-barred as inverted subject (the DO reading strands the
  subject slot).
- '94 92' "closed set" correction: only @65-66 is a true ne-governor;
  @1549's 94 is word-internal to "prenne".

## Standing constraints observed

Did not touch R5005, sealed gate instances, or the red-team adjudication
queue. Nothing promoted, killed, or re-valued by this battery. No invented
numbers: every offset verified on the repaired 1,847-pair stream.
Adverses answered: follower scatter re-derived (neutral, confirmed); killed
'-ere' value not re-litigated (@683 fenced); prenne-92-noun coordination
kept to class-level notes, value arm untouched.
