# Battery report: val-16-84-role

Target: `val-16-84-role` — "Name 16's role at @83 specifically ('62 16 [14]06'), independent of the fenced global finite-verb class; a 16-role test that does not load the finite premise."
Parent: `stem-14-84-retest` (2026-10-09) — follow-up #1.
Date: 2026-10-09. Lock created/deleted per protocol.
Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, byte-exact per `repair_parse.py`). `canonical.py` never touched. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, from battery-queue.json)

1. "Ground 16's role at @83 in the stream evidence; do not assume the fenced global finite-verb class."
2. "Fail closed: null with follow-ups if 16's role is underdetermined."

Numbered clauses (fixed before testing):
- C1: Ground 16's role at @83 in the stream evidence — name the role iff the evidence forces one role with zero new assumptions.
- C2: Do not assume the fenced global finite-verb class — test independently of it (the locus-level 'a'/'est' values from val-91-pp-adj are finite and excluded).
- C3 (fail-closed): if 16's role is underdetermined, verdict NULL with follow-ups.

## Method

1. Read BATTERY-PROTOCOL.md in full. Created `locks/val-16-84-role.lock` on start.
2. Re-derived the repaired stream in-session (1,847 pairs, 96 types verified).
3. Read the parent report (battery-stem-14-84-retest.md) and val-91-pp-adj's 16 findings before testing.
4. Enumerated every candidate role for 16 at the locus and tested each against standing values only.

## Window evidence

Locus (1-based @, row a1_02 mid-row, no row boundary):
`@81=98 @82=51 @83=62 @84=16 @85=14 @86=06 @87=88 @88=77 @89=66 @90=98`

Standing premises used (not re-litigated):
- 98 = finite verb class, battery-promoted ('vient'; boundary-98-839 names its distributional function; complement inventory {83, 00, 82}).
- 14 = 'en' battery-promoted (en14-value-tighten, 15/15 windows); 14's verb class fenced lane-wide (parent battery).
- 06 = 'ent' (red-team R17 promote). Host rule (ent-06-host-census): finite "-ent" iff the left neighbor is (or composes) a verb stem; else syllabic.
- 88 = verb class, battery-promoted (prof-88, 7 frame-legs).
- 77 = 'le' provisional. Banked: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que. Granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce.
- 16's global finite-verb class: FENCED (val-16-a-vs-est NULL; parent records the fence). 16's verb-LIKE distributional profile stands as battery-level evidence: n(16)=28, predecessors 82='m' x11 ("m 16" clitic+verb shape), followers 00='pour' x4 ("16 pour [inf]").

Byte-exact checks in-session:
- "62 16" occurs exactly 4x stream-wide: @83 (follower 14), @659 (follower 00), @1142 (follower 29), @1298 (follower 02). No uniform follower class.
- @84's locus values 'a'/'est' (val-91-pp-adj, at "82 16 91" windows) are finite-verb values — excluded by the bar's own C2.
- 06 at @86: left neighbor is 14='en' (a clitic, not a verb stem; 14's verb class is fenced). Per the host rule, 06 is NOT a finite ending here — it is syllabic 'ent' needing a host.

## Role-by-role test (16 at @84, frame "62 16 [14='en'] [06='ent']")

- **Finite verb — EXCLUDED by C2.** The bar forbids assuming the fenced global finite-verb class; the locus 'a'/'est' legs are finite. Not tested further.
- **Infinitive — FAIL.** No licensed governor: 62 is value-open (no modal/preposition leg), 51 is open, and 98='vient' at @81 selects complements {83,00,82} — 51/62/16 are not in its inventory (boundary-98-839). Right side: 14='en' after an infinitive is the wrong clitic order ("[inf] en" is not a French constituent; cf. nepas-20-adverb-gate's value-independent "[inf] ne [verb]" kill).
- **Past participle — FAIL.** No auxiliary to the left; 62 has no auxiliary value standing.
- **Adverb — FAIL.** (a) Contradicts 16's verb-like profile ("m 16" x11, "16 pour" x4) — an adverb reading would need the §7 polyvalence act (red-team venue). (b) The 'en ent' tail is ungrammatical under every 16-role (see below); the adverb arm does not repair it.
- **Pronoun — UNDERDETERMINED.** Under 62='il' ("il [16-pron]") it is ungrammatical, but 62's value at @83 is open (62='il' is battery-promoted only at other windows, e.g. @1704). Naming 16's role here requires 62's value — one new assumption. Fenced.
- **Noun — UNDERDETERMINED.** Needs 62 as determiner/adjective; 62 has no such leg standing. Requires 62's value. Fenced.
- **Determiner — UNDERDETERMINED.** Needs 62 nominal; same gate. Fenced.
- **Adjective — UNDERDETERMINED.** Needs an adjacent head noun; 62='il' cannot be modified, 14='en' cannot be head. Gated on 62. Fenced.
- **Preposition — UNDERDETERMINED.** Under 62='il', "il [16-prep] en" is ungrammatical; with 62 open the arm cannot be killed or adopted. Fenced.
- **Word-internal left ("62-16" one word) — FAIL.** 16 has no letter value; no French word statable without inventing one.
- **Word-internal right ("16-14[-06]" one word) — FAIL.** Same defect: 16 has no letter value.
- **Clause boundary (before or after 16) — FENCED.** Mid-row a1_02, no byte evidence for a boundary; cannot be adopted, cannot be killed.
- **Interjection/particle — FAIL.** No standing license; the tail defect persists regardless.

**Structural crux (value-independent):** the right edge "14 06" = "en"+"ent" is defective under EVERY 16-role. 06's left neighbor (14='en', a clitic — and 14's verb class is fenced) is not a verb stem, so 06 is syllabic 'ent' with no licensed host in-window ("ent"+[88-stem] would need 88's open value to complete a French word; 88's value is open). No 16-role repairs this tail — so even the best-case role leaves the window a multi-residual. The tail is 16-independent, but it caps what a "role naming" can claim: the frame "62 16" cannot be fully grounded while the window's right half strands.

## Per-clause results

- **C1: FAIL.** The evidence forces no single role with zero new assumptions. The finite class is barred (C2); the non-finite verbal arms die on licensing (no governor, no auxiliary); adverb/preposition/word-internal arms die on profile or morphology; the nominal family (pronoun/noun/determiner/adjective/preposition) is gated on 62's open value; the boundary arm has no byte evidence.
- **C2: PASS.** The fenced finite-verb class was never assumed; locus 'a'/'est' values excluded throughout.
- **C3: FIRES.** 16's role is underdetermined → verdict NULL with follow-ups.

No standing or red-team verdict contradicted or downgraded; §7 intact. The parent's fence of 14's verb class is untouched (adopted as premise). Note: the parent brief's three-bar restatement ((1) parse @83 with 16 in candidate roles; (2) name iff zero new assumptions; (3) else fence) is satisfied by this same analysis — the queue's fail-closed bars are the stricter superset and are what the verdict follows.

## Verdict: NULL (fail closed)

## Follow-ups proposed (all verified absent from battery-queue.json, 2026-10-09)

1. `val-62-83-role` (P3) — name 62's value/role at @83. Every non-verbal 16-role is gated on it: if 62='il' holds at @83, the nominal/adjectival/prepositional 16-arms die at kill grade ("il [noun/adj/prep]" ungrammatical); if 62 is nominal, the determiner/noun arms open. Census the four "62 16" windows (@83/@659/@1142/@1298) for 62's value.
2. `tail-14-06-88-host` (P3) — resolve the value-independent "en"+"ent" tail: test "06 88" as word-initial "ent"+[88-stem] composition vs 06 as stranded syllable. The tail defect blocks every 16-role; until it resolves, @83–86 stays a multi-residual.
3. `reseg-62-16-83` (P4) — re-test "62 16" as a one-word vs two-word unit once 62 names; the word-internal arm needs 62's letter value first (16 has none).

## Bookkeeping

Report: code/crowd17/report_inbox/battery-val-16-84-role.md.
Queue: val-16-84-role → status `verdict`, result `null`, date 2026-10-09 (pre-write assert confirmed queued/verdictless; temp-file + rename; JSON re-validated post-write; own entry only). Lock created on start, deleted on completion.
