# Battery verdict: val-03-letter-probe

- Target: `val-03-letter-probe` (battery-queue.json, priority 3, status queued)
- Claim: establish 03's letter content (@1237 '[10] [03]e', the '40 03' junctions @336/@599 word-internal vs boundary, and other letter-adjacent 03 windows); letter inventory is the prerequisite for lexeme candidates at battery grade.
- Worker: ae909021-ced2-436c-9e6e-2f53865f78af. Date: 2026-10-09.
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005, sealed gates, red-team adjudication queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream. Asserts held: 1,847 pairs, 96 types, n(03)=20.
- Lock: `code/crowd17/next-token/locks/val-03-letter-probe.lock` created on start (no lock present, no collision); deleted on completion.

## Bar (verbatim, pre-registered before testing)

"name 03's letter content with byte evidence at >=2 windows; else fence the letter arm"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (name arm):** a single letter value for 03 is named with byte evidence (exact-frame repeats or GT-letter adjacency) at >=2 independent windows, with zero kill-grade contradictions at any window.
2. **C2 (fence arm):** otherwise, fence the letter arm (no letter content nameable at battery grade).
3. **C3 (adverses):** the 03/71 split is NOT adjudicated (evidence only, per R20 deferral); R19-178's conditioned scope is used as premise, never re-litigated; no settled kill is re-opened.

## Standing values and premises used (protocol §7)

Pencil GT: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que. Granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce, 12=n, 48=e (letters). Provisional: 59=est, 77=le.

**Load-bearing red-team standings (used as premises, not re-tested):**
- **R19-178 (GRANT-WITH-CORRECTIONS):** stem-03 promoted as verb-stem **conditioned to the "03 29" frame x3**. F1 @1321-1b (0-based @1320, row a7_04): "24 03 29" passes on R17-009's finite/modal class taking bare infinitives — i.e. "03 29" is the bare infinitive word. F3 @1595-1b (0-based @1594, row a8_02): "03 29" passes. Registry: ["03","verb-stem","cls"], conditioned scope.
- **R19-179 (GRANT, window-local):** at @1594, "03 29" = stem+ending FORCED (given 03 word-shaped + §7).
- **R19-180:** noun family for 03 ('[03] qui' x4 kill-grade nominal since 64='qui' needs a nominal antecedent; "[03]e" @1237 noun-compatible).
- **R20:** 03/71 §7 splits DEFERRED — untouched here.
- **§7 sole-polyvalence rule:** 67 et/veut is the only true polyvalence. A letter hypothesis for 03 is therefore global — it stands or falls at every window.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session; byte-confirmed n(03)=20 and all 20 windows.
3. Census of 03's adjacency to known letters: 40='e' is the ONLY banked letter adjacent to 03 — 40->03 x2 (@336, @599), 03->40 x1 (@1237). Zero adjacency to 12='n' or 48='e'. n("03 29")=3 (@1030 fenced at red-team level per R19-142/R20-038 — not used as a leg; @1320, @1594).
4. Tested the global letter hypothesis H ("03 = a single letter L") against the conditioned "03 29" infinitive frames.

## Findings — the kill

### K1 @1320 (row a7_04): the letter hypothesis forces a nonexistent word — KILL GRADE

Bytes @1318–1322: `15 24 03 29 80`.

Per R19-178 F1 (conditioned grant, settled): "24 03 29" = finite/modal (R17-009) + **bare infinitive "03 29"** — one word, two cipher units. Banked GT: 29="er". So the infinitive word is exactly [03]+"er".

Under H (03 = one letter L), this infinitive is L+"er": a **3-letter -er infinitive**. French has no 3-letter -er infinitive (shortest attested: 4 letters — "oser", "user", "aimer"). H forces a word that does not exist in the language. The claim "03 is a letter" is forced false at this window. Kill grade.

### K2 @1594 (row a8_02): corroborating kill — KILL GRADE

Bytes @1592–1596: `81 03 29 80`.

Per R19-179 (window-local grant, settled): "03 29" = **stem+ending forced**. Under H the "stem" would be a single letter before "-er" — the same 3-letter impossibility as K1. Independent window, same kill.

### Letter-adjacent windows (evidence gathered, no letter forced)

- **@336 (a2_05):** bytes @334–338 `88 40 03 64 31` = "88 e [03] qui 31". 03 is nominal-forced here (R19-180: '[03] qui' x4, kill-grade nominal). Junction reading: "e" + nominal 03. Boundary-favoring ("e | [03-nominal]"), but 40 is a bound letter at R20's "82 34 29 40" windows, so a word-internal "e[03…]" reading (03 = multi-letter stem after initial e) is not excluded. **Undetermined at battery grade; no letter forced.**
- **@599 (a4_00):** bytes @597–601 `29 40 03 39 26` = "er e [03] a 26". Reads as "…ere [03] à…" (boundary: feminine "-ere" word, then 03-word, then 'a') or word-internal "ere[03]". **Undetermined; no letter forced.**
- **@1237 (a7_01):** bytes @1235–1239 `56 10 03 40 67` = "56 10 [03] e 67". "10 [03]e": R19-180 lists "[03]e" as noun-compatible (feminine "-e" word-shape). With 03 multi-letter, "[10][stem]e" or "[10] [stem]e" both parse. **No letter forced.**
- **"10 03" bigram x2** (@1237 pre=10, @1649 pre=10): byte-identical repeat consistent with 03 as a multi-letter unit; a single letter would not form a fixed bigram with an unknown syllable. Weak corroboration only.

### Contact census (byte-derived)

n(03)=20. Predecessors: 60 x4, 30 x3, 40 x2, 80 x2, 47 x2, 10 x2, 77/37/01/24/81 x1. Successors: 64 x4, 39 x3, 29 x3, 62 x2, 91/02/60/24/40/30/38/00 x1. The only banked-letter contacts are with 40='e' (3 windows above). "03 64" x4-5 ('qui' follower) and "30 03" x3 ('pas' predecessor) are word-level contacts where a single-letter 03 is ungrammatical — consistent with the kill, not independent kills (they load on R19-180's nominal arm).

## Clause results

- **C1: FAIL AT KILL GRADE.** No letter can be named: @1320 forces "03 29" = bare infinitive = [03]+"er"; a single-letter 03 yields a nonexistent 3-letter -er infinitive. Corroborated at @1594 (R19-179 stem+ending forced). The name arm is not merely unsupported — it is dead.
- **C2: FIRES (as kill consequence).** The letter arm is fenced AND killed: 03 cannot be a single letter. Lexeme work on 03 must proceed through the stem arm (R19-178 conditioned scope) and the nominal arm (R19-180), never the letter arm.
- **C3: PASS.** Adverses answered:
  - The 03/71 §7 split is untouched — this battery decides no split; the kill is letter-tier only and is consistent with R19-178's conditioned stem scope, R19-180's noun family, and R20's deferral (a stem and a nominal can both be multi-letter; the split question is about class, not letterhood).
  - R19-178's conditioned scope was used as premise, not re-litigated; @1030's fenced window was not used as a leg.
  - No settled kill re-opened.

## Consistency check (protocol §5.2)

No standing red-team verdict is contradicted. R19-178 grants 03 as verb-stem (class-level, conditioned) — a stem is multi-letter; consistent with this kill. R19-180's noun family — multi-letter nominal; consistent. R20's 03/71 split deferral — untouched. Sibling batteries val-03-value-census (NULL, uniform-verb fenced), val-03-noun (NULL), seg-77-03-722 (NULL) — none names a letter; all consistent. §7 intact (no second polyvalence declared or needed).

## Verdict: KILL (letter arm)

03 is not a single letter: at kill grade via @1320 (R19-178 F1 conditioned infinitive frame), corroborated at @1594 (R19-179). The letter arm is closed; no follow-ups per §4. Lexeme candidacy for 03 proceeds via the stem/nominal arms only.
