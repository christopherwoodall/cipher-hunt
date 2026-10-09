# Battery report: reseg-82-44-1160 — the 82-44 hapax bigram resolves by re-segmentation

- Worker: battery-worker reseg-82-44-1160, agent 0ad4b441-c5a8-45f6-967f-78badb903ae1
- Date: 2026-10-09 (lock created 2026-10-09T15:11:05Z)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). canonical.py NOT used. R5005 untouched. All @-offsets are repaired-stream 0-based indices.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"(a) enumerate admissible segmentations of @1159-1161 under standing values ('77 | 82 44', '77 82 | 44', word-internal '82-44'); (b) adopt one iff it parses with zero new assumptions and kills/fences all rivals; (c) else fence with stated cause"

Numbered clauses (frozen before testing):
1. The three candidate segmentations are enumerated with standing values only.
2. '77 | 82 44' parses with zero new assumptions.
3. '77 82 | 44' is killed/fenced with stated cause.
4. Word-internal '82-44' spanning 77 is killed/fenced with stated cause.
5. Adopt '77 | 82 44' iff clauses 2–4 pass; else (c) fence with stated cause.

## Method

Re-parsed the repaired stream in-work (1,847 pairs, 96 types confirmed; asserts held). Located the '82 44' hapax, censused '77 82', '44 83', and 82's follower distribution from the stream (not copied from briefs). Tested each segmentation using only standing values: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); battery-promoted (94=ne, 12=n + 48=e, 30=pas, 06=ent); provisional (59=est, 77=le); leads (83=de conditioned, 78=ver-word); prior battery fencings (noun-44 kill, de-frame-44-83-21). No value named for 44 or 21.

## Window-level evidence

**Locus.** Row a6_09, 0-based: @1155='29', @1156='80', @1157='17', @1158='77', @1159='82', @1160='44', @1161='83', @1162='21', @1163='67', @1164='78', @1165='45'.

**Distributional facts (re-derived byte-exact).**
- '82 44' occurs exactly 1× stream-wide (@1159) — the hapax under test.
- '77 82' occurs exactly 2×: @1041 ('40 17 77 82 63 11 67' = "…e fois le m[63] la et…") and @1158 ('80 17 77 82 44 83 21' = "…[80] fois le m[44] de [21]…"). Both sit after 17='fois' (granted) — the parallel "fois le m[X]" frame.
- '44 83' occurs exactly 2× (@1160, @1839); the byte-identical 5-gram '44 83 21 67 78' occurs exactly 2× (@1160, @1839).
- 82 (n=39) followers: 16×11, 48×4, 06×4, 96×3, 94×3, 14×2, 34×2, 98×2, rest ×1 — letter-tier behavior (word-final before word-initial cells; word-initial "mi…" before 34='i' GT).

**Clause 2 — '77 | 82 44' parses with zero new assumptions: PASS.**
Reading: "le" (77="le", provisional — §7-usable, not new) | "m[44]" (82='m' GT letter + 44 word-internal; the noun-44 kill's own fencing states @1160 is "most naturally word-internal 'le m[44]'"; @540 '91 12 44 29 48' gives battery-grade precedent for 44 as word-internal stem, "manière"-shaped) | "de" (83='de', conditioned lead R19-128; @1161 is not in the lead's excluded scope) | "[21]" (noun, stated class: 'la [21]' ×2, 'de [21]' ×3) | "et" (67 by the §7 positional rule: follower 78 is not infinitive-shaped) | "[ver-word]" (78 lead). Full frame: "…[80] fois, le m[44] de [21] et [ver…]…" — a grammatical 1841 French NP (article + noun + de-complement + coordination). Every component is standing; no value is named for 44 or 21; no class is declared for 44 (stem-vs-inflection is the queued stem-44-nominal venue). Zero new assumptions.

**Clause 3 — '77 82 | 44' killed/fenced: PASS (kill grade).**
This option needs 44 as a standalone word. Whole-word noun-44 was KILLED at battery grade (battery-noun-44, 2026-10-08: @1714 '94 44 59 30' forces 44 into a clitic slot; the kill is conditional on 94='ne' battery-promoted and 59='est' provisional — both standing at battery grade, and §7 holds the kill). The "lem[44]…" one-word sub-reading has no French license under standing values (§3 bars inventing a "lemme"-shaped value). The 82-word-final sub-reading ("le…m" word) would overturn provisional 77="le" — an escalation, not a battery resolution. No admissible parse under standing values: killed at kill grade.

**Clause 4 — word-internal '82-44' spanning 77 killed/fenced: PASS (kill grade).**
"lem[44]…" as a single word has no French license under standing values; naming one would invent data (§3). Killed at kill grade. (Note: the boundary-location content of this option — 82-44 bound — is identical to the adopted option; what dies here is only the 77-absorbing variant.)

**Clause 5 — adoption: FIRES.**
Clauses 2–4 pass: adopt '77 | 82 44' — boundary after 77; "le" | "m[44]" (82-44 one word); 44 word-internal, class/value open.

## Adverses (all listed adverses answered — none ignored)

- "82='m' banked GT - no homophony claim without S7 red-team evidence": answered — no homophony is claimed. 82 is the letter "m" (GT) in every option tested; the adopted segmentation uses it word-initially, consistent with the pencil crib ("la pre m i er e", 82 word-internal there) and the @1041 "le m[63]" parallel. §7 intact.

## Verdict: PROMOTE

The 82-44 hapax resolves as '77 | 82 44': "le" | "m[44]", with 44 word-internal (class/value open) and the '44 83 21' frame reading "[m[44]] de [21]" under the standing 83='de' lead. Rivals '77 82 | 44' and 77-spanning word-internal '82-44' are killed at kill grade under standing values.

## Scope (explicit)

Boundary resolution only. Untouched: 44's class/value (the stem-44-nominal venue stays queued; the @1839 whole-word-44 vs @1714 clitic-44 tension is the de-frame-44-83-21 battery's red-team escalation — not re-litigated here); 21's value; 78's lead grading; the noun-44 kill's conditional status (94='ne' pending ratification, 59='est' provisional). No standing or red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands.

No follow-ups required per §4 (promote).

## Provenance

Every number above traces to the repaired 1,847-pair stream re-parsed in-work (1,847 pairs, 96 types; '82 44' ×1, '77 82' ×2, '44 83' ×2, '44 83 21 67 78' ×2, n(82)=39 re-derived, not copied). No invented data. R5005, sealed gates, and the red-team adjudication queue untouched.
