# Battery report: noun-43-discriminator

- Target: noun-43-discriminator
- Claim: 43="suite" (discriminated, not just candidate-listed)
- Worker: subagent 1c016d84-e974-4cf4-b7d7-284e9cd9c82a
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py. `canonical.py` never used. R5005 untouched. Red-team adjudication queue untouched. No data invented. @-offsets are 0-based stream indices.
- Lock: created `code/crowd17/next-token/locks/noun-43-discriminator.lock` on start, deleted on completion.

## Bar (verbatim, pre-registered)

"(a) 43 named from a value set that ALSO satisfies the 'la 43 en', '43 pour que', and '37/32-43' frames with >=1 discriminating frame beyond this one; (b) the other three candidates shown failing at >=2 of those frames; (c) coordinate with queued frame-43-* batteries, do not re-run their bars"

## Bar restated as numbered pass/fail clauses

1. Clause (a): "suite" satisfies the 'la 43 en', '43 pour que', and '37/32-43' frames, with at least one discriminating frame beyond the background "par [43]" frame supporting "suite".
2. Clause (b): each of {condition, maniere, mesure} fails at >=2 of those frames.
3. Clause (c): coordination with the queued frame-43-* batteries performed; none of their bars re-run.

## Method

Built the repaired stream (1,847 pairs, 96 distinct groups; 43 census n=16 — matches the ce-frame battery's independent census). Enumerated all 16 windows of 43 with ±8 context. Tested each candidate of the shared set {suite, condition, maniere, mesure} (from the par-rest finder + ce-frame battery; not re-derived) for grammaticality in each frame under 1840s diplomatic French, using only banked/granted values (11=la, 82=m, 29=er, 46=que, 47=ce, 00=pour, 96=par, 64=qui, 17=fois). Named no open group. Used the queued batteries' frame inventory (@1123/@1721 la-52-37-43 with continuations 43-pour-86 / 43-98-39; @1544 pour-que; @1303 doublet; 37/32-43 x4) without testing 52/21/78/37/32 naming.

43 census (n=16): @21 (a1_00), @43 (a1_01), @244 (a2_02), @258 (a2_02), @343 (a2_05), @386 (a2_07), @439 (a2_09), @563 (a3_02), @1027 (a6_03), @1092 (a6_06), @1126 (a6_07), @1204 (a7_00), @1303/@1305 (a7_03), @1544 (a8_00), @1724 (a8_07).

## Window-level evidence

**@21 (a1_00, row interior 0-34 — not a row-boundary artifact):**
`76 45 91 53 17=fois 64=qui 98 82 [43] 29=er 47=ce 33 55 81 00=pour 34 24`
The trigram "82-43-29" decodes "m"+"V(43)"+"er" (82="m", 29="er" banked, non-negotiable; groups atomic). With V(43)="suite" the surface is "msuiteer" — not French. Exhausted word-boundary placements hosting standalone "suite": "…Xm|suite|er…" fails on "er"+"ce"="erce" (no French word begins "erce"; 47="ce" granted A4); "msuite|er…" ("msuite" not French); "m|suiteer…" ("suiteer" is no verb/noun/adjective); "…m|suite|erce…" (no French "suiteerce*"); elided "m'suite" impossible before consonant "s". All fail. Viable parses all require V(43)!="suite": "mener" (V(43)="en": "…qui [98-modal] mener ce [33]" — "qui veut/peut mener ce…" is clean French), "emmener" (98="em"), or a verb-stem "[V43]er" infinitive. Polyvalence is barred (67 et/veut is the sole true polyvalence, protocol §7). **@21 forces 43!="suite".**

**@343 (a2_05) / @1027 (a6_03) — "par [43]" x2 (background frame):**
`40 03 64 31 14 45 64 96 [43] 87 01 06 70 12 94 74 67` / `91 53 84 92 64 45 64 96 [43] 87 01 03 29 80 77 11 70`
"96-43-87-01" = "par [43] ce [01]" (the 6-gram heads @340/@1024). Accepted from the ce-frame battery: "par suite" ("consequently") is the only grammatical reading; "par condition/maniere/mesure" are not French. Favors suite. This is "this one" in the bar — it cannot count as the beyond-frame.

**@563 (a3_02) — "la 43 en":**
`34 17 86 94 59 30 67 11 [43] 24 80 97 13 76 45 94 52`
"11-43" = "la [43]": all four candidates are feminine nouns — suite/condition/maniere/mesure all pass. Follower 24 underdetermined (the "en" working gloss is unestablished; 24/80 open). Consistent, non-discriminating.

**@1544 (a8_00) — "43 pour que":**
`62 06 21 62 93 88 77 78 [43] 00=pour 46=que 70 12 94 92 45 23`
"00-46" = "pour que" (A9 + banked); "70-12-94" = "pre"+"n"+"ne" = "prenne" (subjunctive; compositional on 12="n"/94="ne", battery-promoted pending ratification). Under the government reading ("[43] pour que [subj]"): "condition pour que" ✓ (prerequisite-sense: "la condition pour que…"), "mesure pour que" ✓ ("prendre des mesures pour que…" — peak diplomatic purpose), "suite pour que" ✗ (no such construction), "maniere pour que" ✗ (idiom is "de maniere que / de maniere a ce que"). **Under its discriminating reading this frame favors condition/mesure and kills suite.** Under the boundary alternative ("…78 43. Pour que prenne 92…", purpose clause after a clause-final noun) all four pass and the frame is non-discriminating — that adjudication belongs to queued frame-43-pour-que-1544 (its bar owns the 78 slot and the boundary question); I do not pre-empt it.

**37/32-43 x4:**
- @386 (a2_07): `00 11 50 82 16 52 38 37 [43] 91 36 62 91 84 73 34 67`
- @1126 (a6_07): `70 12 06 14 06 11 52 37 [43] 00 86 52 37 86 24 77 86` (continuation "43-pour-[86-INF]")
- @1724 (a8_07): `30 64 47 68 06 11 52 37 [43] 98 39 88 24 30 15 01 56` (continuation "43-98-39"; 39="a/a" promoted per battery-a-39, still leaves 98/88 open)
- @258 (a2_02): `94 65 63 00 66 01 91 32 [43] 77 84 74 45 93 52 33 42`
Predicative 37/32 + 43: adjective+noun feminine agreement holds for all four candidates; 37/32 values open so no lexical discrimination. Consistent, non-discriminating. (Structural reading — predicative vs nominal slot — is queued frame-43-pred-37-32's bar; not re-run.)

**Fenced (open values, not contradictions; routed to owning queues):** "ce que 43" @439 (`86 29 82 16 78 63 45 46 [43] 98 80 50 78 41 10` — "que"+noun needs a boundary for all four); "ce 43" @1204 (`96 82 16 64 29 45 58 47 [43] 55 61 21 65 64 59` — neuter-"ce"+noun needs a boundary for all four; flagged for queued noun-43); "24 88 43 81" @43; "06 43 07" @1092; "56 43 00 66" @244 ("43 pour [66]" — purpose-adjunct-or-boundary, weak for all four); "43 77" @258/@1305 ("43 le" needs a boundary or 77!="le"; 77 provisional; lever-77-78 queued); doublet "08 43 21 43 77" @1303/1305 (queued frame-43-21-43-doublet's bar).

## Discrimination table (candidate x frame; ✓=grammatical, ✗=ungrammatical)

| frame | suite | condition | maniere | mesure |
|---|---|---|---|---|
| par [43] @343/@1027 | ✓ | ✗ | ✗ | ✗ |
| la [43] @563 | ✓ | ✓ | ✓ | ✓ |
| [43] pour que @1544 (government) | ✗ | ✓ | ✗ | ✓ |
| 37/32-43 x4 | ✓ | ✓ | ✓ | ✓ |
| @21 "82-43-29" | ✗ (forces false) | ✗-class* | ✗-class* | ✗-class* |

\* @21 forces V(43)!="suite" specifically; it independently pulls 43 toward verb-stem/"en"-shape, constraining the whole noun set — flagged for queued noun-43.

## Per-clause pass/fail

1. Clause (a) — **FAIL at kill grade.** (i) Window @21 forces the claim false: no French parse hosts V(43)="suite" under non-negotiable banked values (82="m", 29="er", 47="ce") and the 67-sole-polyvalence rule; the viable parses ("mener"/"emmener"/verb-stem) all require V(43)!="suite". (ii) No discriminating frame beyond "par [43]" supports suite: "la 43 en" and "37/32-43" are consistent but non-discriminating (all four feminine), and "43 pour que" under its discriminating (government) reading favors condition/mesure and rejects suite.
2. Clause (b) — **FAIL.** condition fails 1 frame (par-43) < 2; mesure fails 1 (par-43) < 2; only maniere fails 2 (par-43, pour-que). The >=2 bar is not met for two of the three rivals.
3. Clause (c) — **PASS.** Coordination performed: used the queued batteries' frame inventory and @-offsets (la-52-37-43 @1123/@1721 with both continuations; pour-que @1544; doublet @1303; pred-37-32 x4) and the shared candidate set; named no open group (52/21/78/37/32/98/39/24 untouched); the pour-que boundary-vs-government adjudication and the doublet coordination reading left to their owning batteries.

## Adverses

- "coordinate with queued frame-43-* batteries" — answered: coordination as above; no queued bar re-run. Two findings routed onward: the pour-que-against-suite analysis goes to frame-43-pour-que-1544 (its bar owns the 78 slot and boundary question); the @21 class constraint goes to noun-43 (its noun premise must answer @21).
- "noun-43's value arm owns unconditional naming" — respected: no unconditional naming is claimed. This battery removes "suite" from the set; the value arm (queued noun-43) retains naming authority but must now also reconcile @21, which pulls 43 away from noun-hood entirely.
- No standing red-team verdict is contradicted: the rulings mention "mener" only for group 78 (WO1, 78="me"-syllable context); no ruling exists on group 43.

## Verdict: KILL

"suite" is killed as 43's value: @21 forces 43!="suite", the bar's discrimination math fails (clauses a and b), and the one frame that discriminates beyond "par [43]" points to condition/mesure, not suite. "maniere" is additionally dead (fails par-43 and pour-que). Surviving set: {condition, mesure} — both still wounded by @21's class pull.

## Follow-up target (for the supervisor to queue)

1. at21-82-43-29-adjudicate — PRIORITY 1. Claim: "82-43-29" @19-22 (row a1_00, interior) is word-internal ("mener"/"emmener"-family with 43="en") or a verb-stem slot — 43 is not a standalone noun here. Bars: (a) name 98 (modal/governor, or "em") with "qui 98 mener ce 33" parsing as one grammatical run; (b) state 43's class at @21 (noun vs verb-stem vs "en") with the boundary analysis from this report either confirmed or overturned with cause; (c) reconcile with the "par [43]" noun frames — one value must cover both windows, or petition the red team on the 67-sole-polyvalence rule with stated cause. Evidence: @21 `98 82 43 29 47` = "…qui [98] m[V43]er ce [33]"; banked 82="m", 29="er"; "msuiteer"/"suiteer"/"erce" not French; "mener"/"emmener" French; this kill report. Adverses: "par [43]" x2 pulls noun-ward; 98/33 open; 47="ce" (A4) fixed; "qui [98] mener" needs 98 as modal/governor.
