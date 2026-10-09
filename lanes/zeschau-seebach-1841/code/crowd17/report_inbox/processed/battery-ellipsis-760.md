# Battery verdict: ellipsis-760 — **KILL**

**Target:** `ellipsis-760` (priority 2)
**Date:** 2026-10-08 (CDT)
**Worker:** d9aefc55-4439-4848-97fb-b88112c71f1e

## Pre-registered bar (verbatim from battery-queue.json)

> CLAIM: re-examine W1 (@760) under the ellipsis hypothesis — "la première" nominalized, 20 clause-initial
> BARS: test 20 as clause-initial particle against @760/@839/@1703 with @307 fenced as the det/adj leg
> ADVERSES: @307 det/adj leg
> EVIDENCE: battery-noun-20-value.md follow-up #2

**Numbered clauses:**
- (c1) 20 parses as a clause-initial particle at @760, with "la première" (`11 70 82 34 29 40`, all GT) nominalized ("the first one", noun elided).
- (c2) The same clause-initial-particle reading parses @839.
- (c3) The same clause-initial-particle reading parses @1703.
- (a) The @307 det/adj leg is fenced (excluded from scope) with stated cause.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/ellipsis-760.lock` on start. All counts re-derived from the repaired 1,847-pair stream (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`: `load_rows` + `parse`). `canonical.py` never touched. R5005, sealed gates, and the red-team adjudication queue untouched. Standing values used: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que), banked (17=fois, 30=pas, 59=est provisional, 87=ce, 64=qui), leads (94='ne' STRONG LEAD R17-001, 62='il' battery lead, 98='vient' battery promote). Kill holds honored: 20='fois' (§7).

## Window-level evidence (re-derived, @-offsets on repaired stream)

**Structural fact 1:** the trigram `20 62 94` occurs **exactly 3×** in all 1,847 pairs — at @760, @839, and @1703, i.e. exactly the bar's three test windows. The clause-initial hypothesis is therefore a hypothesis about this trigram: "[20-particle] il ne…".

**Structural fact 2:** the bigram `94 30` ("ne pas", 94='ne' lead + 30=pas promoted) occurs **exactly once** in the stream: @1701–1702, immediately preceding the @1703 test window.

**@760** (`…40 67 11 70 82 34 29 40 20 62 94 59 39 88 66 98 80…`): "…[40] [67] la première [20] il n'est [39] 88 [66] vient [80]…". Under the hypothesis: "la première" nominalized ("the first one"); then "[20] il n'est [39]…" with 20 a clause-initial particle ("donc / or / mais / certes…" class): "la première ; [20], il n'est [39]…" — grammatical, no unstated assumptions beyond the granted nominalization.

**@839** (`11 77 76 59 35 56 17 98 20 62 94 26 12 16 00 33 96 40 62 21…`): "…[56] fois vient [20] il ne [26]…". Particle reading: "…fois, [X] vient ; [20], il ne [26]…" — requires **one unstated assumption** (clause boundary after 98=vient). Grammatically tolerable.

**@1703** (`58 15 23 91 85 33 94 30 20 62 94 88 26 12 06 29 40 65 94 44…`): "…85 [33] ne pas [20] il ne [88]…". The stream's unique "ne pas" positively selects a verbal (infinitive) complement — "ne pas" + X requires X infinitive in every period of French; a clause-initial particle cannot occupy that slot, and "ne pas" cannot terminate a clause without its complement. Attachment check: `33 94 30` cannot be "ne [33-finite] pas" (wrong order) nor "ne pas [33-inf]" (wrong order); "ne pas" must scope **forward** onto 20. No evidenced re-segmentation exists. The particle reading is not merely unsupported here — it is **grammatically excluded**.

**Corroboration:** `30 20` ("pas [20]") occurs twice (@1269–1270 and @1702–1703). At @1270 (`88 24 30 20 64 47 76` = "…[24] pas [20] qui…", 64=qui banked) the "pas" lacks "ne" but the frame still selects a verbal element — a clause-initial particle after "pas" is likewise ungrammatical. Both "pas [20]" windows agree: 20 sits in a verbal slot, never a particle slot.

## Per-clause results

- **(c1) @760 — PASS.** The W1-local ellipsis reading is clean: nominalized "la première" + clause-initial 20 + "il n'est [39]…".
- **(c2) @839 — MARGINAL PASS.** Parses with one unstated assumption (clause boundary after "vient").
- **(c3) @1703 — FAIL AT KILL GRADE.** "ne pas [20]" forces 20 into a verbal-complement slot; the clause-initial-particle reading is grammatically impossible. The window forces the uniform claim false.
- **(a) @307 — FENCED with stated cause** (per the bar's instruction): `88 02 88 20 17 46` = "…[20] fois que…" is the unique det/adj leg — the fois-battery corpus result stands (91 "X fois que" bigrams in 1840–42 diplomatic French, predecessors exclusively determiners/adjectives, zero nouns); 20='fois' killed (§7). Excluded from this hypothesis's scope, not explained by it.

## Verdict: **KILL**

The **uniform** clause-initial-particle account of 20 is killed at @1703: "ne pas" positively requires a verbal complement, which a particle cannot satisfy. (c1) shows the W1-local ellipsis reading is itself grammatical — what dies is the uniformity, not the @760 parse.

**Surviving rescue (stated, not declared):** conditioned behavior — 20 = clause-initial particle in the "20 62 94" frames (@760/@839), verbal complement of "ne pas" (@1703), determiner/adjective before 17 (@307). That is polyvalence, and per §7 (67 et/veut sole true polyvalence) declaring it is a **red-team act**. This battery states the candidacy only. It coordinates with — and does not duplicate — the existing P1 `poly-20-docket` (proposed as noun-20-value follow-up #3).

No standing verdict contradicted or downgraded. R5005, sealed gates, and the red-team adjudication queue untouched.

## Follow-ups proposed

1. `inf-20-nepas` (P2): test 20 as infinitive at @1703 ("ne pas [20-inf]") with @1270 ("pas [20]" without "ne") as the second leg — a verbal-20 value that parses both "pas [20]" windows feeds the poly-20 docket and discriminates the verbal face of 20 from the particle face killed here.
