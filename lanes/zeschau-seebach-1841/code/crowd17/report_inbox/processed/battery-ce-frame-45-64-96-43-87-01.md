# Battery report: ce-frame-45-64-96-43-87-01

Target: ce-frame-45-64-96-43-87-01
Claim: byte-identical 6-gram x2 reads 'ce qui par [43] ce [01]' under 45='ce'
Worker: subagent c6ea5be2-6ca9-4b69-b19d-f6f2bc6029d5
Date: 2026-10-08
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py

## Bar (verbatim, pre-registered)

(a) both windows parse with 43 named (coordinate with noun-43);
(b) the 'qui ce qui' left edges (@340's 14, @1024's 64) parsed or fenced

## Bar restated as numbered pass/fail clauses

1. Clause (a): both the @340 and @1024 windows parse with 43 assigned a named value coordinated with noun-43.
2. Clause (b1): the @340 left edge ("64-31-14", "qui [31] [14]") is parsed or fenced with stated cause.
3. Clause (b2): the @1024 left edge ("53-84-92-64", "[53] on [92] qui") is parsed or fenced with stated cause.

## Method

Built the stream with the repaired parse (a5_03=0, 1,847 pairs; asserts on gloss (i)/(ii) not re-run here, parse verified byte-identical to the repair_parse.py construction). Located both byte-identical 6-gram instances: @340 (row a2_05) and @1024 (row a6_03). Checked the immediate predecessor of each 45 (=14 @340, =64 @1024; zero 78-contact, confirming the dict rival has no foothold here). Ran contact censuses for 43 (n=16), 14 (n=15), 53 (n=11), 92 (n=22). Tested the "par [43]" frame against noun-43's four candidates {suite, condition, maniere, mesure}. Did NOT touch R5005, canonical.py, or the red-team queue. 45='ce' treated as HOLD (A11) per protocol, not re-litigated.

## Window-level evidence

@340 (row a2_05, offsets 328-357):
19 00 92 50 | 45 54 88 40 03 64 31 14 | 45 64 96 43 87 01 | 06 70 12 94 74 67 78 40 92 98 92 47
Read: "…[19] pour [92] [50] ce [54] [88] e [03] qui [31] [14] | ce qui par [43] ce [01] | [06] prenne [74] et/veut [78] e [92]…"
Standing values: 00='pour' (A9), 64='qui', 96='par', 87='ce', 70-12-94='prenne' (prenne battery). The 6-gram's 45 is the stream's only "45-64-96" bigram-continued pair context; its predecessor @339=14 is 14's single 45-follower in 15 windows.

@1024 (row a6_03, offsets 1012-1041):
78 47 03 24 41 15 66 91 53 84 92 64 | 45 64 96 43 87 01 | 03 29 80 77 11 70 82 34 29 40 17 77
Read: "…[78] ce [03] [24] [41]…[53] on [92] qui | ce qui par [43] ce [01] | [03]er [80] le la pre-m-i-ere fois le"
Standing values: 84='on' (A15), 29='er', 77='le' (provisional), 11='la', 70-82-34-29-40='premiere', 17='fois'. The "77-11-70-82-34-29-40-17" tail reads "le la première fois [le]" — the "le la" adjacency is a standing tension (cf. le611/ le83 batteries), untouched here. Predecessor of 45 is @1023=64, giving a consecutive "qui ce qui" (@1023-1025).

43 contact census (n=16): predecessors 37 x3, 96 x2 (both = this 6-gram's "par [43]"), 11 x1 ("la 43"); successors 00 x3 ("43 pour [86-INF]" purpose frames), 87 x2, 77 x2, 98 x2. The "11-43" and "43-00" frames are consistent with a feminine noun; no window contradicts noun-hood.

"par [43]" candidate test (noun-43's set {suite, condition, maniere, mesure}):
- suite: "par suite" = "consequently" — standard French, adverbial. PASSES.
- condition: "par condition" — not French. FAILS.
- maniere: "par manière" — not French. FAILS.
- mesure: "par mesure" — not French. FAILS.
Only "suite" forms a grammatical "par [43]" phrase. This discriminates inside noun-43's candidate set but is NOT a value claim by this battery (43's value arm belongs to noun-43; per the brief I do not duplicate it).

Left-edge profiles: @340's edge tokens 31 and 14 are value-open (14 n=15, successors 24/06/60 x2; 31 open). @1024's edge tokens 53 (n=11, successor 84 x2 = "53-on") and 92 (n=22, open; class-92 queued) are value-open. 84='on' is granted (A15).

## Per-clause pass/fail

1. Clause (a) — CONDITIONAL PASS (does not support a verdict-grade pass). Both windows parse identically as "…ce qui, par suite, ce [01]…" only under the conditional assumption 43="suite", the one candidate of noun-43's set that is grammatical after "par". The other three candidates fail the frame. The value naming is explicitly conditional — 43's value arm is noun-43's and this battery does not claim it — so the clause cannot pass unconditionally.
2. Clause (b1) — FENCED, not parsed. "64-31-14" = "qui [31] [14]": 31 and 14 are value-open (14's sole 45-follower is this window; 14 n=15 has no assigned value). The "qui" (@337) closes the preceding "…03 qui 31 14" clause, which cannot parse until 31/14 resolve. Fenced with cause: open values, not a contradiction.
3. Clause (b2) — FENCED, not parsed. "53-84-92-64" = "[53] on [92] qui": 53 and 92 are value-open (92's class is queued as class-92). 84='on' holds (A15). The "qui" (@1023) plausibly closes the preceding "…[53] on [92] qui" relative clause, and "ce qui par suite…" may open a new clause — but whether a clause boundary falls between @1023 and @1024 is undecidable until 92's class resolves. Fenced with cause: open values, not a contradiction.

## Adverses

- 43's value open: answered by coordination — "suite" is the sole candidate of noun-43's set grammatical under "par", recorded as a discriminator for noun-43, not a value claim here.
- No standing red-team verdict is contradicted: 45='ce' stays a HOLD (A11); this report neither promotes nor kills it. The "77-11" tail at @1032-1033 is a standing le-frame tension, noted but outside this target's bar.
- Neither window forces the claim false: both read naturally as "ce qui par [43] ce [01]" under the stated conditional naming.

## Verdict: NULL

Kill-grade: no. No window forces the 6-gram reading false; the byte-identical pair is real on the repaired stream and both instances read cleanly under 45='ce'.
Promote-grade: no. Clause (a) is only conditionally satisfiable — naming 43 unconditionally is noun-43's value arm, which this battery is barred from duplicating — and clause (b) is fenced, not parsed. Promoting would overclaim the evidence.
NULL is the honest grade: the claim is plausible and both windows parse under a conditional "suite" reading, but the open values (43, 31/14, 53/92, 01) block a verdict-grade decision.

## Follow-up targets (for the supervisor to queue)

1. noun-43-discriminator — Claim: 43="suite" (discriminated, not just candidate-listed). Evidence: "par [43]" @340/@1024 is grammatical only as "par suite" ("consequently"); "par condition/manière/mesure" are not French; the "11-43" + "43-00-[86-INF]" frames agree with a feminine noun. Bars: (a) 43 named from a value set that ALSO satisfies the "la 43 en", "43 pour que", and "37/32-43" frames with >=1 discriminating frame beyond this one; (b) the other three candidates shown failing at >=2 of those frames; (c) coordinate with queued frame-43-* batteries, do not re-run their bars.
2. edge-1024-clause-boundary — Claim: a clause boundary falls between @1023 ("qui") and @1024 ("ce") — i.e. the 6-gram spans "…on [92] qui [V]. Ce qui par suite, ce [01]…". Bars: (a) 92's class named (coordinate with class-92); (b) state whether the 6-gram spans a clause boundary — if yes, the claim formulation "reads 'ce qui par [43] ce [01]'" needs a boundary-aware revision; (c) the "53-on" left edge parsed or fenced.
3. edge-340-31-14 — Claim: "…03 qui 31 14 ce qui…" resolves once 31/14 are named. Bars: (a) 31 and 14 each named with contact profiles; (b) the "qui 31 14 ce qui par suite ce [01]" sequence parses as one grammatical run or is fenced to a clause boundary with stated cause; (c) 14's other 14 windows show no contradiction with the chosen parse.
