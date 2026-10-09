# Battery verdict: dict-45-independent-leg

- Target: `dict-45-independent-leg` (battery-queue.json, priority 3, status queued)
- Claim: Hunt a 45='dict' leg independent of 78-adjacency - the missing half of the composition; its discovery re-opens the full "verdict" composition arm
- Worker: 2a6e0836-79ed-4b41-8c87-c259e9617e29
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; re-derived in-session, asserts held: 1,847 pairs / 96 types).
- `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered before testing)

"An independent 45='dict' leg stated at battery grade"

Numbered pass/fail clauses (frozen before testing):

1. C1 — State >=1 window, with 45 NOT 78-adjacent, where 45='dict' parses at battery grade (zero ungranted assumptions, positive selectional pressure over the standing 45='ce' A11 HOLD).
2. C2 — (alternative) Record the hunt failure with stated scope: every non-78-adjacent 45-window classified (leg / dead / conditional / anti-'dict').

Adverses: none listed on the queue entry. Standing: 45=['ce/dict','lead'] (registry), 78=['ver','lead'] (R16-005), A11 45='ce' HOLD.

## Method

1. Re-derived the repaired stream in-session. n(45)=22 at 0-based offsets: 14, 104, 262, 314, 332, 340, 401, 437, 478, 569, 574, 603, 678, 697, 974, 983, 1024, 1055, 1165, 1201, 1214, 1551.
2. The four 78-adjacent windows (@314=W1, @574=W2, @983=W3, @1165=W4) are excluded by the bar; the parent `verdict-arm-819-strengthen` NULL and `dict-independence-census` NULL already cover them. Hunt set = the remaining 18 windows.
3. Two 'dict' readings tested per window: (a) syllabic 'dict' (/di/ as in ver-dict) composing a French word with its predecessor; (b) word-level 'dit' (past participle of dire) in a grammatical frame.
4. Closed the syllabic host inventory on the lane corpus (code/side-period/corpus/, 98 files): French words ending in the /di/-pronounced "dict" syllable are exactly **verdict** (17x) and **interdict** (45x). The "-dict-" hits of the /dik/ family (juridiction, contradiction, dictee, dicter...) are a different syllable and cannot host 45='dict'.

## Window-level evidence (0-based @-offsets, byte-confirmed)

### (a) Syllabic route — dead at all 18 windows

Predecessors of the 18 hunt windows and their standing values: 76(open), 59(est-prov), 74(open), 50(open), 14(open), 11(la-GT), 63(verb-cls), 96(par), 77(le-prov), 51(open), 64(qui), 29(er-GT), 92(open). None is 'ver' (78 is the sole 'ver' and is bar-excluded); none is 'inter'. With the host inventory closed at {verdict, interdict}, no standalone 45 can compose a 'dict'-final word. The route's only remaining opening is an unvalued predecessor (76/74/50/51/92) turning out to be 'inter' — see follow-up 2.

Note @1201 ("64 29 45"): 29='er' cannot be word-final (poly-42-syllable-word: "er"+42 is one word at all three windows), so "29 45" would have to be one word "er"+"dict" = *"erdict" — not French. Dead.

### (b) Word-level 'dit' route — zero legs; three anti-'dict' windows

'dit' frames in 1841 French: "a dit (que)", "dit-il/on" (inversion), "est dit (que)" (passive), "X dit que". 45's followers stream-wide: {91, 28, 93, 64, 54, 88, 46, 94, 13, 8, 1, 23, 36, 58} — no 84 ('on'), no 62 ('il' killed), so no inversion frame; no 52 ('a') predecessor, so no "a dit" frame.

- @14 (a1_00): "76 45 91" — "[76] dit [91-fin]" broken (participle + finite verb); "ce" equally broken. DEAD both ways.
- @104 (a1_03): "93 59 45 28" = "[93-verb] est dit [28]" — 93 is verb-class (registry), so the subject slot for the passive is unfilled and 28 cannot host the "que"-complement. Broken. DEAD.
- @262/@478 (a2_02/a2_11): "74 45 93" — "[74] dit [93-verb]" broken. DEAD.
- @332 (a2_05): "50 45 54" — both neighbors open; "dit" and "ce" both conditional. NO DISCRIMINATION.
- @340 (a2_05): "14 45 64 96" — "[14] dit qui par" broken; "[14] ce qui par" parses (standing verbless "ce qui par" window, verbless-cequi-relatives PROMOTE). **ANTI-'dict', pro-'ce'.**
- @401 (a2_08): "11 45 88" — "la dit" broken (needs "l'a dit"); "la ce" broken. DEAD both ways.
- @437 (a2_09): "63 45 46" = "[63-verb] 45 que" — 63 is verb-class (registry). Under 'dit': "[V] dit que" ungrammatical (finite verb + bare participle). Under 'ce': "[V] ce que" grammatical object clause. **ANTI-'dict', pro-'ce' at class grade.**
- @569 (a3_02): "76 45 94" — "[76] dit ne" broken. DEAD.
- @603 (a4_00): "96 45 93" — "par dit" broken. DEAD.
- @678 (a5_00): "77 45 23" — "le dit" broken ('dit' is not a noun). DEAD.
- @697 (a5_01): "50 45 28" — both neighbors open; no discrimination. NO DISCRIMINATION.
- @974 (a6_01): "51 45 08" — "[51] dit [08-t]" broken. DEAD.
- @1024 (a6_03): "64 45 64 96" — "qui dit qui par" broken; "qui ce qui par" parses (standing verbless window, byte-identical tail to @340). **ANTI-'dict', pro-'ce'.**
- @1055 (a6_04): "74 45 23" — neighbors open; no discrimination. NO DISCRIMINATION.
- @1214 (a7_00): "96 45 36" — "par dit" broken. DEAD.
- @1551 (a8_00): "92 45 23" — neighbors open; no discrimination. NO DISCRIMINATION.

### Tally of the 18 hunt windows

- Legs for 45='dict': **0**
- Anti-'dict' (45='ce' parses, 'dit' fails): 3 (@340, @437, @1024)
- Dead both ways: 11 (@14, @104, @262, @401, @478, @569, @603, @678, @974, @1201, @1214)
- Non-discriminating conditionals: 4 (@332, @697, @1055, @1551)

## Per-clause pass/fail

1. C1 (state >=1 independent 'dict' leg at battery grade): **FAIL** — zero legs. The syllabic route is closed (host inventory {verdict, interdict}, no eligible predecessor); the word-level route's two cleanest frames die on registered classes (@437: 63 verb-class kills "[V] dit que"; @104: 93 verb-class + missing complement kills "est dit").
2. C2 (record the hunt failure with stated scope): **FIRES** — all 18 windows classified above.

## Verdict: NULL

Headline: the independent-'dict' hunt fails with stated scope — no non-78-adjacent window legs 45='dict' at battery grade, and three windows (@340, @437, @1024) actively discriminate against 'dit' in favor of the standing 'ce'. This does not contradict 45's ['ce/dict','lead'] status (the lead already records 'dict' as unratified) and does not re-litigate any post-78 window. Kill is not met (no window forces 45≠'dict' globally; the existential claim is unfalsified, just unsupported).

## Scope

Hunt-level question only: 78-adjacent windows untouched (parent batteries own them); 45's lead status, A11 HOLD, 78's 'ver' LEAD, §7 all intact; no standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands.

## Follow-ups (null regenerates work; all verified ABSENT from battery-queue.json 2026-10-09)

1. `dict-conditional-resolve` (P4): name the open neighbors at the four non-discriminating windows — 50/54 @332, 28 @697, 74/23 @1055, 92/23 @1551. The word-level 'dit' route survives only if a "dit"-licensing frame emerges; else it is exhausted stream-wide. Bars: >=1 "dit"-licensing frame stated with zero ungranted assumptions, or fence the word-level route with the four windows' resolutions cited.
2. `dict-inter-sweep` (P4): test each unvalued 45-predecessor {76, 74, 50, 51, 92} against the 'inter' value — the syllabic route's last opening (host "interdict"). Bars: 'inter' named at battery grade at >=1 predecessor, or fence the syllabic route stream-wide.
3. `ce-45-antidict-package` (P4, gather-only): package the three anti-'dict' windows (@340 "[14] ce qui par", @437 "[63-verb] ce que", @1024 "qui ce qui par" — each with 45='ce' parsing and 45='dit' failing at class/grammaticality grade) as red-team input on the 45 ['ce/dict'] lead. Bars: evidence feed only, no adjudication.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-dict-45-independent-leg.md`
- Queue: `dict-45-independent-leg` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.dict-45-independent-leg.tmp` + atomic rename per protocol §5.2; JSON re-validated from disk; own entry only; no downgrade).
- Lock `locks/dict-45-independent-leg.lock`: created on start (agent 2a6e0836-79ed-4b41-8c87-c259e9617e29, 2026-10-09T21:06:00Z), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
