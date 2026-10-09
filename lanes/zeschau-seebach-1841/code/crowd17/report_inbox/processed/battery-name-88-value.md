# Battery verdict: name-88-value — one value across 88's 23 windows?

- Target: `name-88-value` (priority 2)
- Claim: 88 takes one value across its 23 windows, deciding the 'à [88]' complement at @1725
- Worker: battery-worker name-88-value (agent ce508cb5-bfd5-437c-b056-95cfaa8e3606)
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, repair_parse.py tokenization). canonical.py never used. R5005 untouched. Sealed gates untouched. No invented numbers.
- Lock: created code/crowd17/next-token/locks/name-88-value.lock on start (no pre-existing lock; nothing stale to note).
- Verdict: **KILL**

## 1. Bar (verbatim from battery-queue.json)

"name 88 iff one value (infinitive vs noun) parses >=80% of its 23 windows with the '39 88' x3 ('à [88]': @765 'est à [88]', @1514 'à [81] [88]', @1727 'vient à [88]') and the article followers ('88 77' x3, '88 11' x2) resolved; then re-test '43 vient à [88]'"

Numbered clauses (pre-registered from the queue text BEFORE any window analysis; bar not modified after seeing data):

1. The three 'à [88]' frames parse under the candidate value: @765 'est à [88]', @1514 'à [81] [88]', @1727 'vient à [88]'.
2. The article followers resolve under the candidate value: '88 77' x3 (@86, @646, @1541), '88 11' x2 (@730, @1514).
3. One value — infinitive or noun — parses >=80% of 88's 23 windows (>=19/23).
4. Re-test '43 vient à [88]' (@1724–1728) under the named value.

Index note: the claim's "@1725" is the 43-98-39-88 window's anchor convention (43 @1724, 98 @1725, 39 @1726, 88 @1727 in repaired-stream indexing; cf. battery-cont98-43-value.md). No data discrepancy — 88 is at @1727. Census re-derived: 88 n=23 at @42, 86, 210, 304, 306, 334, 402, 497, 513, 616, 619, 646, 730, 765, 904, 1049, 1117, 1260, 1267, 1514, 1541, 1706, 1727. Predecessors: 39 x2 (@765, @1727), 69 x2 (@1260, @1267); successors: 77 x3 (@86, @646, @1541), 11 x2 (@730, @1514), 24 x2 (@1267, @1727). All match the queue's evidence gloss.

Standing values used (status-labeled): granted §7 (11=la, 70=pre, 82=m/me, 34=i, 29=er, 40=e, 46=que, 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77=le); battery-promoted 2026-10-08 (39=à/à, 94=ne, 30=pas, 06=ent, 12=n, 48=e letters); battery-grade (98=vient, 24=finite-verb class, 65=noun); demonstrated-not-promoted (62='il'); A9 (86 INF-class); 67=et/veut sole polyvalence.

## 2. Method

Every 88 window extracted ±7 pairs on the repaired stream. Each window graded under H1 (88 = infinitive verb) and H0 (88 = noun): PASS = admits a grammatical French reading under standing values with strain (if any) localized to open tokens; FAIL = 88's slot ungrammatical under the candidate (forces candidate false at that window). Counts use solid PASS only; conditional/marginal passes reported separately and do not count toward the 80%.

## 3. Window-level evidence

H1 = 88 infinitive; H0 = 88 noun. Annotated with standing values; [NN] = open.

- @42 `01 24 [88] 43` — "[24-finite-verb] [88-inf] [43]": finite verb + infinitive + object ✓. H1 PASS. H0 FAIL ("[24] [88-noun]" bare noun object ungrammatical).
- @86 `[06-ent] [88] le [66]` — "[88-inf] le [66]" = infinitive + determiner-headed object NP ("aimer le [noun]" shape) ✓. H1 PASS (conditional on 14-06 left context). H0 FAIL.
- @210 `[44] [50] [88] [19] [74]` — no forced contradiction; neighbors open. H1 WEAK PASS. H0 FAIL (bare "[50] [88-noun]").
- @304 `[89-verbframe] [88] 02 [88]` — "[89] [88-inf]" verb+infinitive ✓. H1 PASS (conditional on 02 as coordinator). H0 FAIL.
- @306 `[88] 02 [88] [20] fois` — "[inf] [02] [inf]" coordination ✓ (strain on 20 fenced). H1 PASS. H0 FAIL.
- @334 `[54] [88] e [03]` — "[54] [88-inf]" conditional; "[88]e[03]" syllabic boundary fenced (strain not at 88's word slot). H1 PASS. H0 FAIL.
- @402 `la ce [88] [53]` — "ce [88]": 45='ce' (A4 grant) is a demonstrative determiner; "ce"+infinitive ungrammatical, "ce"+finite verb ungrammatical, "ce"+noun clean. **H1 FAIL. H0 PASS. Window forces 88=noun.**
- @497 `tout [88] ce la` — "tout [88-verb]" ✓ (cf. A5 "tout [80]" pronoun+verb re-read). H1 PASS. H0 FAIL (bare "tout [noun]" needs article).
- @513 `[65-noun] [88] [56]` — underdetermined both ways. H1 WEAK. H0 WEAK.
- @616 `pré [88] [10]er [88]` — formula "70 88 10 29 88 37" (two 88s, shared with @619): "pré[88]" is prefix+stem shaped, i.e. syllabic/sub-word 88, not a free word of either candidate class. H1 FAIL. H0 FAIL. Fenced as formula/syllabic residual.
- @619 (same formula, second 88) — H1 FAIL. H0 FAIL. Same fence.
- @646 `[61] [88] le [78]` — "[88-inf] le [78]" = infinitive + NP object ✓. H1 PASS. H0 FAIL.
- @730 `e [88] la [24-finite-verb]` — "e [88]" strained (86-48 syllabic boundary) and "[88] la [24]" ungrammatical under both ("la"+finite verb impossible; "la" cannot head the needed NP). H1 FAIL. H0 FAIL.
- @765 `ne est à [88] [66]` — "est à [88-inf]" canonical ("être à + inf") ✓. H1 PASS. H0 WEAK PASS ("est à [place]" marginal, place-noun only).
- @904 `et [16] [88] [18]` — 16 open (frame-82-16 queued). Both CONDITIONAL, no force either way.
- @1049 `[41] [88]er e` — "[88]er": 88 + 'er' (29='er' granted) = infinitive morphology on 88 itself. **H1 PASS (strongest verb-morphology leg).** H0 FAIL ("[noun]er" ungrammatical).
- @1117 `[69] la [88] prennent` — "la [88]": 11='la' (pencil); "la"+infinitive-as-verb ungrammatical, "la"+finite verb ungrammatical, "la"+noun clean. **H1 FAIL. H0 PASS. Window forces 88=noun.** (Post-88 "prennent" number tension fenced to 70-12-06, not to 88's slot.)
- @1260 `er [69] [88] [01]` — 69/01 open. Both CONDITIONAL.
- @1267 `que [69] [88] [24] pas` — "que [69-finite-verb] [88-inf]" ✓ ("que [veut] [faire]" shape, conditional on 69); post-88 "[24] pas" fenced. H1 PASS. H0 FAIL ("que [fv] [bare-noun]" ungrammatical).
- @1514 `est à [81] [88] la [31]` — with clause boundary: "…est à [81]. [88-inf] la [31]…" = infinitive + "la [31]" object NP ✓. H1 PASS. H0 FAIL ("[88-noun] la [31]" article-after-noun ungrammatical).
- @1541 `[93] [88] le [78]` — "[88-inf] le [78]" ✓. H1 PASS. H0 FAIL.
- @1706 `[62] ne [88] [26]` — 94='ne' (battery-promoted): "ne"+infinitive ungrammatical, "ne"+noun ungrammatical, "ne"+finite verb clean (ne littéraire); elided "n'"+vowel-initial reading still selects finite verb. **H1 FAIL. H0 FAIL. Window forces 88=finite verb** (conditional on 94='ne' standing; 62 open but the 'ne' slot constraint is 62-independent).
- @1727 `[43] vient à [88] [24] pas` — "[43] vient à [88-inf]" canonical "venir à + inf" ✓; post-88 "[24] pas" fenced. H1 PASS. H0 WEAK PASS ("venir à [lieu]" place-noun only).

Tallies (solid PASS only):
- H1 infinitive: 13/23 (57%) — @42, 86, 304, 306, 334, 497, 646, 765, 1049, 1267, 1514, 1541, 1727. At most 17/23 (74%) counting weak/conditional (@210, 513, 904, 1260).
- H0 noun: 2/23 solid (@402, @1117); 4/23 with weak (@765, @1727 place-noun marginals).
- Fails both: @616, @619 (formula/syllabic), @730 (strained both sides).

Forced-value windows (kill-grade):
- @402 "ce [88]" forces noun.
- @1117 "la [88]" forces noun.
- @1706 "[62] ne [88]" forces finite verb.
- @1049 "[88]er" demonstrates infinitive morphology.
Three distinct word-classes forced across windows; no single value covers them.

## 4. Per-clause pass/fail

1. '39 88' x3 frames: @765 PASS ("est à [88-inf]" clean); @1514 PASS with clause boundary ("…à [81]. [88-inf] la [31]"); @1727 PASS ("vient à [88-inf]" clean). **Clause 1: PASS** (under infinitive; noun passes only @1727 marginally as place-noun).
2. Article followers: '88 77' x3 all PASS (@86 "le [66]", @646/@1541 "le [78]" — infinitive + determiner-headed object NP); '88 11' x2: @1514 PASS ("la [31]" object NP), @730 FAIL (unresolvable under either candidate; fenced). **Clause 2: PARTIAL (4/5 resolved).**
3. One value >=80% (19/23): infinitive 13/23 solid (17/23 max with generous conditionals); noun 2–4/23. **Clause 3: FAIL** — neither candidate reaches the bar.
4. Re-test '43 vient à [88]': recorded as observation — @1727 "[43] vient à [88-inf]" is grammatical under the majority (infinitive) reading; 43's value remains undiscriminated (condition/mesure tie stands per battery-cont98-43-value.md). No value was named, so the re-test cannot complete as a decision.

## 5. Adverses answered

1. "88's article followers tension a pure verb reading" → ANSWERED: 4/5 resolve as infinitive + determiner-headed object NP (@86, @646, @1541, @1514); the residual @730 is fenced with strain localized to the 86-48 syllabic boundary and 24, and @730 independently fails both candidates.
2. "88's verb-class grant" → CONSISTENT, not overturned: the kill refutes one-value-ness, not verb-class (13/23 infinitive-compatible; @1049 "[88]er" is verb morphology). Per §7, declaring a second polyvalence for 88 is a red-team act — this battery does NOT declare values, it kills the one-value claim; the polyvalence question is flagged for the red team (see follow-ups).

## 6. Verdict: KILL

The claim "88 takes one value across its 23 windows" is false at kill grade: @402 ("ce [88]") and @1117 ("la [88]") force 88=noun; @1706 ("[62] ne [88]") forces 88=finite verb; @1049 ("[88]er") shows infinitive morphology. The bar's binary (infinitive vs noun, >=80%) fails on both arms — infinitive 13/23 (57%), noun 2/23 (9%). No standing red-team verdict is contradicted (88 was never red-team adjudicated; the class-level verb grant from battery-cont98-43-value.md is untouched). R5005, sealed gates, and the red-team queue untouched.

## 7. Recommended follow-up targets (for supervisor queueing)

F1. id: `noun-88-det` | priority: 2
claim: "88=noun at determiner-governed windows (@402 'ce [88]', @1117 'la [88]')"
bars: "name the noun iff one value parses both windows + >=1 further determiner/adjective-governed 88 window, zero contradictions"
evidence: "this battery: @402/@1117 force noun (45='ce' A4, 11='la' pencil); 88 n=23 census re-derived"
adverses: "@1117 post-88 'prennent' number tension fenced to 70-12-06; §7 sole-polyvalence rule — value declaration is red-team-gated if it coexists with verb-88"

F2. id: `finite-88-ne` | priority: 2
claim: "88=finite verb at @1706 ('[62] ne [88] [26]')"
bars: "resolve iff 88's finite form parses the ne-frame with 26's class stated; scan 88's 23 windows for further ne-governed instances"
evidence: "this battery: @1706 '62 94 88' with 94='ne' battery-promoted forces finite (ne/n' + infinitive/noun ungrammatical)"
adverses: "62 open (demonstrated 'il', not promoted); 26's class open (noun-26 null); §7 sole-polyvalence rule — red-team-gated"

F3. id: `inf-88-restricted` | priority: 3
claim: "88=infinitive holds on the à-governed + -er windows once the forced windows are fenced"
bars: "name 88=inf iff >=80% of the non-forced windows parse with @402, @1117, @1706 explicitly excluded and fenced with stated cause"
evidence: "this battery: 13/23 solid infinitive-compatible; 'est à [88]' @765, 'vient à [88]' @1727, '[88]er' @1049"
adverses: "exclusion of forced windows concedes multi-value 88 — red-team must bless the framing per §7 before promotion"
